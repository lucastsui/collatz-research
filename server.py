"""
Math Research Pipeline — Browser Dashboard with live-rendered LaTeX.
Closed research loop: user provides direction, extractor feeds back findings
and suggested next directions to the thinker each round.
"""

import asyncio
import json
import time
import os
import threading
from contextlib import asynccontextmanager
from datetime import datetime, timezone

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from openai import OpenAI

# ── Config ──────────────────────────────────────────────────────────────────

API_BASE = "https://spark-4a7e.tail2214e5.ts.net/v1"
API_KEY = "assignment6"
MODEL = "gpt-oss-120b"

FINDINGS_PATH = os.path.expanduser("~/Desktop/math/findings.jsonl")

EXTRACTION_PROMPT = """You are a proof advisor. The user's goal is to prove or solve the following problem:

PROBLEM: {problem}

Below is the thinker's latest proof attempt. Your job is to:
1. Identify what progress was made toward actually proving/solving the problem.
2. Find any logical gaps, errors, or unjustified steps in the argument.
3. Decide what the thinker should try next to make concrete progress on the proof.

Produce EXACTLY two sections:

FINDINGS:
Summarize what was established so far (state key results precisely in LaTeX).
Point out any errors or gaps that need fixing.

DIRECTION:
Give a specific, actionable instruction for the next proof attempt. For example: "Try applying contradiction by assuming X", "Use induction on n with base case...", "The gap in step 3 can be fixed by...", "Bound the integral using Y instead". Be concrete — do NOT just say "continue exploring".

PROOF ATTEMPT:
{derivation}
"""

client = OpenAI(base_url=API_BASE, api_key=API_KEY)

# ── Shared State (thread-safe via GIL for simple appends/reads) ─────────

class StreamState:
    """Append-only event log. Frontend polls by index."""
    def __init__(self):
        self.thinker_events = []   # list of {type, data}
        self.extractor_events = []
        self.completed_queue = []
        self.round_num = 0
        self.extraction_count = 0
        self.start_time = time.time()
        self.running = False
        # Feedback loop state
        self.user_topic = ""           # initial research direction from user
        self.user_direction = ""       # mid-run override direction from user
        self.accumulated_findings = [] # list of findings strings from extractor
        self.extractor_direction = ""  # last suggested direction from extractor
        self.extractor_done_round = 0  # last round the extractor finished analyzing

state = StreamState()


def parse_extractor_output(text):
    """Parse FINDINGS and DIRECTION sections from extractor output.
    Handles variants like FINDINGS:, **FINDINGS**, **FINDINGS:**, etc.
    """
    import re
    findings = ""
    direction = ""
    # Match FINDINGS/DIRECTION headers with optional markdown bold and colon
    fi_match = re.search(r'\*{0,2}FINDINGS\*{0,2}\s*:?\s*', text, re.IGNORECASE)
    di_match = re.search(r'\*{0,2}DIRECTION\*{0,2}\s*:?\s*', text, re.IGNORECASE)
    if fi_match and di_match:
        findings = text[fi_match.end():di_match.start()].strip()
        direction = text[di_match.end():].strip()
    elif fi_match:
        findings = text[fi_match.end():].strip()
    elif di_match:
        direction = text[di_match.end():].strip()
    else:
        findings = text.strip()
    # Strip leading --- separators that the model sometimes adds
    findings = re.sub(r'^---+\s*', '', findings).strip()
    direction = re.sub(r'^---+\s*', '', direction).strip()
    return findings, direction


def save_findings(round_num, findings_text, direction_text):
    """Append a round's findings to the persistent JSONL file."""
    entry = {
        "round": round_num,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "findings_text": findings_text,
        "direction": direction_text,
    }
    os.makedirs(os.path.dirname(FINDINGS_PATH), exist_ok=True)
    with open(FINDINGS_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")


# ── Thinker Thread ──────────────────────────────────────────────────────

def build_thinker_prompt(round_num):
    """Build the thinker prompt incorporating feedback from previous rounds."""
    parts = [
        "You are a rigorous mathematician. Your SOLE goal is to prove or solve the following problem. "
        "Do NOT merely list properties, definitions, or background. Instead, construct an actual proof "
        "or solution step by step. Every step must be justified. Use LaTeX "
        "(use $...$ for inline and $$...$$ for display math).",
        "",
        f"PROBLEM TO PROVE/SOLVE: {state.user_topic}",
    ]

    # Include accumulated findings from the extractor (what's been established, gaps found)
    if state.accumulated_findings:
        parts.append("")
        parts.append("Progress so far from previous rounds:")
        for i, f in enumerate(state.accumulated_findings, 1):
            parts.append(f"  Round {i}: {f[:500]}")

    # The extractor's direction tells the thinker what to try next
    direction = state.user_direction or state.extractor_direction
    if direction:
        parts.append("")
        parts.append(f"ADVISOR INSTRUCTION FOR THIS ROUND: {direction}")
        parts.append("Follow this instruction. Build on previous progress and fix any identified gaps.")
    else:
        parts.append("")
        parts.append("This is your first attempt. Start the proof from scratch.")

    # Clear the mid-run override after using it once
    if state.user_direction:
        state.user_direction = ""

    return "\n".join(parts)


def thinker_thread():
    while state.running:
        state.round_num += 1
        rn = state.round_num

        prompt = build_thinker_prompt(rn)
        topic_display = state.user_topic[:80]

        has_direction = "ADVISOR INSTRUCTION" in prompt
        print(f"[Thinker] Starting round {rn} (has extractor direction: {has_direction})", flush=True)
        state.thinker_events.append({
            "type": "round_start",
            "round": rn,
            "topic": topic_display,
        })

        full_response = ""
        try:
            stream = client.chat.completions.create(
                model=MODEL,
                messages=[{"role": "user", "content": prompt}],
                stream=True,
                max_tokens=4096,
                temperature=0.8,
            )

            for chunk in stream:
                if not state.running:
                    break
                if chunk.choices and chunk.choices[0].delta.content:
                    token = chunk.choices[0].delta.content
                    full_response += token
                    state.thinker_events.append({
                        "type": "token",
                        "round": rn,
                        "token": token,
                    })

        except Exception as e:
            print(f"[Thinker] Error in round {rn}: {e}", flush=True)
            state.thinker_events.append({
                "type": "error",
                "round": rn,
                "error": str(e),
            })
            time.sleep(5)
            continue

        print(f"[Thinker] Round {rn} complete ({len(full_response)} chars)", flush=True)
        state.thinker_events.append({
            "type": "round_end",
            "round": rn,
            "length": len(full_response),
        })

        if len(full_response) > 100:
            state.completed_queue.append((rn, topic_display, full_response))

        # Wait for the extractor to finish analyzing this round before continuing
        print(f"[Thinker] Waiting for extractor to finish round {rn}...", flush=True)
        while state.running and state.extractor_done_round < rn:
            time.sleep(1)
        print(f"[Thinker] Extractor done with round {rn}, proceeding.", flush=True)
        time.sleep(1)


# ── Extractor Thread ────────────────────────────────────────────────────

def extractor_thread():
    while state.running:
        if not state.completed_queue:
            time.sleep(2)
            continue

        rn, topic, derivation = state.completed_queue.pop(0)
        state.extraction_count += 1
        truncated = derivation[:3000] if len(derivation) > 3000 else derivation
        print(f"[Extractor] Analyzing round {rn} ({len(truncated)} chars)...", flush=True)

        state.extractor_events.append({
            "type": "extract_start",
            "round": rn,
            "topic": topic,
        })

        full_response = ""
        try:
            stream = client.chat.completions.create(
                model=MODEL,
                messages=[{
                    "role": "user",
                    "content": EXTRACTION_PROMPT.format(problem=state.user_topic, derivation=truncated)
                }],
                stream=True,
                max_tokens=2048,
                temperature=0.3,
            )

            for chunk in stream:
                if not state.running:
                    break
                if chunk.choices and chunk.choices[0].delta.content:
                    token = chunk.choices[0].delta.content
                    full_response += token
                    state.extractor_events.append({
                        "type": "token",
                        "round": rn,
                        "token": token,
                    })

        except Exception as e:
            print(f"[Extractor] Error on round {rn}: {e}", flush=True)
            state.extractor_events.append({
                "type": "error",
                "round": rn,
                "error": str(e),
            })
            state.extractor_done_round = rn
            continue

        # Parse findings and direction, store for feedback loop
        findings, direction = parse_extractor_output(full_response)
        state.accumulated_findings.append(findings)
        if direction:
            state.extractor_direction = direction
        print(f"[Extractor] Round {rn} — direction parsed: {bool(direction)}", flush=True)
        save_findings(rn, findings, direction)
        state.extractor_done_round = rn

        print(f"[Extractor] Round {rn} analysis complete ({len(full_response)} chars)", flush=True)
        state.extractor_events.append({
            "type": "extract_end",
            "round": rn,
        })


# ── FastAPI App ─────────────────────────────────────────────────────────

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Pipeline does NOT auto-start — waits for POST /start
    print("[Pipeline] Server ready. Waiting for user to submit a research direction.", flush=True)
    yield
    state.running = False

app = FastAPI(lifespan=lifespan)


@app.post("/start")
async def start_pipeline(request: Request):
    """User submits initial research direction to start the pipeline."""
    body = await request.json()
    topic = body.get("topic", "").strip()
    if not topic:
        return JSONResponse({"error": "topic is required"}, status_code=400)
    if state.running:
        return JSONResponse({"error": "pipeline already running"}, status_code=409)

    state.user_topic = topic
    state.running = True
    state.start_time = time.time()
    t1 = threading.Thread(target=thinker_thread, daemon=True)
    t2 = threading.Thread(target=extractor_thread, daemon=True)
    t1.start()
    t2.start()
    print(f"[Pipeline] Started with topic: {topic}", flush=True)
    return {"status": "started", "topic": topic}


@app.post("/direction")
async def update_direction(request: Request):
    """User updates research direction mid-run."""
    body = await request.json()
    direction = body.get("direction", "").strip()
    if not direction:
        return JSONResponse({"error": "direction is required"}, status_code=400)
    state.user_direction = direction
    print(f"[Pipeline] User updated direction: {direction}", flush=True)
    return {"status": "updated", "direction": direction}


@app.get("/poll/thinker")
async def poll_thinker(since: int = 0):
    """Return thinker events since index `since`."""
    events = state.thinker_events[since:]
    return {"events": events, "next": len(state.thinker_events)}


@app.get("/poll/extractor")
async def poll_extractor(since: int = 0):
    """Return extractor events since index `since`."""
    events = state.extractor_events[since:]
    return {"events": events, "next": len(state.extractor_events)}


@app.get("/stats")
async def get_stats():
    elapsed = time.time() - state.start_time
    return {
        "elapsed_seconds": int(elapsed),
        "rounds_completed": state.round_num,
        "extractions": state.extraction_count,
        "model": MODEL,
    }


@app.get("/", response_class=HTMLResponse)
async def index():
    return HTML_PAGE


# ── HTML / JS / CSS ─────────────────────────────────────────────────────

HTML_PAGE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Math Research Dashboard</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@14.0.0/marked.min.js"></script>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'Georgia', 'Times New Roman', serif;
    background: #0a0a0f;
    color: #e0e0e0;
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }

  header {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #2a2a4a;
    flex-shrink: 0;
  }

  header h1 {
    font-size: 1.3em;
    color: #a0c4ff;
    font-weight: 400;
    letter-spacing: 1px;
  }

  #stats {
    font-family: 'Courier New', monospace;
    font-size: 0.85em;
    color: #7a8a9a;
  }

  #stats span { margin-left: 20px; }
  .stat-value { color: #a0c4ff; font-weight: bold; }

  .panels {
    display: flex;
    flex: 1;
    overflow: hidden;
    gap: 1px;
    background: #1a1a2e;
  }

  .panel {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    background: #0d0d14;
  }

  .panel-header {
    padding: 10px 16px;
    font-size: 0.9em;
    font-weight: 600;
    letter-spacing: 0.5px;
    flex-shrink: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .panel:first-child .panel-header {
    background: linear-gradient(90deg, #0d2818, #0d0d14);
    color: #4ade80;
    border-bottom: 1px solid #1a3a2a;
  }

  .panel:last-child .panel-header {
    background: linear-gradient(90deg, #0d1828, #0d0d14);
    color: #60a5fa;
    border-bottom: 1px solid #1a2a3a;
  }

  .panel-content {
    flex: 1;
    overflow-y: auto;
    padding: 16px 20px;
    line-height: 1.8;
    font-size: 1.05em;
    scroll-behavior: smooth;
  }

  .panel-content::-webkit-scrollbar { width: 6px; }
  .panel-content::-webkit-scrollbar-track { background: transparent; }
  .panel-content::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }

  .round-header {
    margin: 20px 0 12px 0;
    padding: 8px 12px;
    border-radius: 6px;
    font-family: 'Courier New', monospace;
    font-size: 0.85em;
  }

  .panel:first-child .round-header {
    background: #0a1f14;
    border-left: 3px solid #4ade80;
    color: #4ade80;
  }

  .panel:last-child .round-header {
    background: #0a1420;
    border-left: 3px solid #60a5fa;
    color: #60a5fa;
  }

  .content-block {
    word-wrap: break-word;
  }

  .content-block h1, .content-block h2, .content-block h3, .content-block h4 {
    color: #c8d8e8;
    margin: 16px 0 8px 0;
    font-weight: 600;
  }
  .content-block h1 { font-size: 1.4em; border-bottom: 1px solid #2a2a4a; padding-bottom: 4px; }
  .content-block h2 { font-size: 1.2em; }
  .content-block h3 { font-size: 1.1em; }
  .content-block p { margin: 8px 0; }
  .content-block strong { color: #f0f0f0; }
  .content-block em { color: #b0c4de; }
  .content-block ul, .content-block ol { margin: 8px 0 8px 24px; }
  .content-block li { margin: 4px 0; }
  .content-block code {
    background: #1a1a2e;
    padding: 2px 6px;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
    color: #a0c4ff;
  }
  .content-block pre {
    background: #1a1a2e;
    padding: 12px;
    border-radius: 6px;
    overflow-x: auto;
    margin: 8px 0;
  }
  .content-block pre code { padding: 0; background: none; }
  .content-block blockquote {
    border-left: 3px solid #4a4a6a;
    padding-left: 12px;
    margin: 8px 0;
    color: #9a9aba;
  }
  .content-block hr {
    border: none;
    border-top: 1px solid #2a2a4a;
    margin: 12px 0;
  }

  .error { color: #f87171; font-style: italic; }

  .status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
  }
  .status-dot.active {
    background: #4ade80;
    box-shadow: 0 0 6px #4ade80;
    animation: pulse 1.5s infinite;
  }
  .status-dot.idle { background: #666; }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }

  .katex { color: #e8e8e8; font-size: 1.1em; }
  .katex-display { margin: 12px 0; overflow-x: auto; overflow-y: hidden; padding: 4px 0; }
  .katex-display > .katex { text-align: left; }

  footer {
    background: #1a1a2e;
    padding: 8px 24px;
    font-size: 0.75em;
    color: #555;
    text-align: center;
    border-top: 1px solid #2a2a4a;
    flex-shrink: 0;
  }

  /* Startup overlay */
  #startup-overlay {
    position: fixed; inset: 0;
    background: rgba(10,10,15,0.92);
    display: flex; align-items: center; justify-content: center;
    z-index: 100;
  }
  #startup-overlay.hidden { display: none; }
  #startup-box {
    background: #1a1a2e;
    border: 1px solid #2a2a4a;
    border-radius: 12px;
    padding: 32px 40px;
    max-width: 540px;
    width: 90%;
    text-align: center;
  }
  #startup-box h2 { color: #a0c4ff; font-weight: 400; margin-bottom: 8px; font-size: 1.3em; }
  #startup-box p { color: #7a8a9a; margin-bottom: 20px; font-size: 0.9em; }
  #startup-input {
    width: 100%;
    padding: 10px 14px;
    background: #0d0d14;
    border: 1px solid #3a3a5a;
    border-radius: 6px;
    color: #e0e0e0;
    font-size: 1em;
    font-family: Georgia, serif;
    outline: none;
  }
  #startup-input:focus { border-color: #a0c4ff; }
  #startup-btn {
    margin-top: 16px;
    padding: 10px 32px;
    background: linear-gradient(135deg, #1a3a5e, #16213e);
    border: 1px solid #3a5a8a;
    border-radius: 6px;
    color: #a0c4ff;
    font-size: 1em;
    cursor: pointer;
    font-family: Georgia, serif;
  }
  #startup-btn:hover { background: linear-gradient(135deg, #1a4a7e, #1a2a4e); }

  /* Direction bar */
  #direction-bar {
    display: none;
    padding: 6px 24px;
    background: #16213e;
    border-bottom: 1px solid #2a2a4a;
    flex-shrink: 0;
    gap: 8px;
    align-items: center;
  }
  #direction-bar.visible { display: flex; }
  #direction-input {
    flex: 1;
    padding: 6px 10px;
    background: #0d0d14;
    border: 1px solid #3a3a5a;
    border-radius: 4px;
    color: #e0e0e0;
    font-family: Georgia, serif;
    font-size: 0.9em;
    outline: none;
  }
  #direction-input:focus { border-color: #a0c4ff; }
  #direction-btn {
    padding: 6px 16px;
    background: #1a3a5e;
    border: 1px solid #3a5a8a;
    border-radius: 4px;
    color: #a0c4ff;
    font-size: 0.85em;
    cursor: pointer;
    white-space: nowrap;
  }
</style>
</head>
<body>

<!-- Startup overlay -->
<div id="startup-overlay">
  <div id="startup-box">
    <h2>Math Research Pipeline</h2>
    <p>Suggest a research direction to begin.</p>
    <input id="startup-input" type="text" placeholder="e.g. Explore connections between the Riemann zeta function and prime distribution" autofocus>
    <br>
    <button id="startup-btn" onclick="startPipeline()">Start Research</button>
  </div>
</div>

<header>
  <h1>Math Research Dashboard</h1>
  <div id="stats">
    <span>Elapsed: <span class="stat-value" id="elapsed">00:00</span></span>
    <span>Rounds: <span class="stat-value" id="rounds">0</span></span>
    <span>Extractions: <span class="stat-value" id="extractions">0</span></span>
    <span>Model: <span class="stat-value">gpt-oss-120b</span></span>
  </div>
</header>

<!-- Direction bar (visible after start) -->
<div id="direction-bar">
  <label style="color:#7a8a9a;font-size:0.85em;white-space:nowrap;">New direction:</label>
  <input id="direction-input" type="text" placeholder="Override research direction for next round...">
  <button id="direction-btn" onclick="sendDirection()">Send</button>
</div>

<div class="panels">
  <div class="panel">
    <div class="panel-header">
      <span><span class="status-dot idle" id="thinker-dot"></span>Thinker — Live Derivations</span>
      <button onclick="clearPanel('thinker')" style="background:none;border:1px solid #333;color:#888;padding:2px 8px;border-radius:4px;cursor:pointer;font-size:0.8em;">Clear</button>
    </div>
    <div class="panel-content" id="thinker"></div>
  </div>
  <div class="panel">
    <div class="panel-header">
      <span><span class="status-dot idle" id="extractor-dot"></span>Extractor — Novel Results</span>
      <button onclick="clearPanel('extractor')" style="background:none;border:1px solid #333;color:#888;padding:2px 8px;border-radius:4px;cursor:pointer;font-size:0.8em;">Clear</button>
    </div>
    <div class="panel-content" id="extractor"></div>
  </div>
</div>

<footer>
  Pipeline: vLLM (gpt-oss-120b) &rarr; Thinker Agent &rarr; Extractor Agent | Markdown + LaTeX rendered live
</footer>

<script>
const thinkerEl = document.getElementById('thinker');
const extractorEl = document.getElementById('extractor');
const thinkerDot = document.getElementById('thinker-dot');
const extractorDot = document.getElementById('extractor-dot');

// Polling cursors
let thinkerCursor = 0;
let extractorCursor = 0;

// Current content block and raw text per panel
let thinkerBlock = null;
let thinkerRaw = '';
let extractorBlock = null;
let extractorRaw = '';

// Track if content changed since last render
let thinkerDirty = false;
let extractorDirty = false;

let pipelineStarted = false;

marked.setOptions({ breaks: true, gfm: true });

// ── Startup and direction ──

async function startPipeline() {
  const input = document.getElementById('startup-input');
  const topic = input.value.trim();
  if (!topic) { input.focus(); return; }
  try {
    const res = await fetch('/start', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({topic}),
    });
    if (res.ok) {
      document.getElementById('startup-overlay').classList.add('hidden');
      document.getElementById('direction-bar').classList.add('visible');
      pipelineStarted = true;
    }
  } catch(e) { console.error(e); }
}

// Allow Enter key to start
document.getElementById('startup-input').addEventListener('keydown', (e) => {
  if (e.key === 'Enter') startPipeline();
});

async function sendDirection() {
  const input = document.getElementById('direction-input');
  const direction = input.value.trim();
  if (!direction) { input.focus(); return; }
  try {
    const res = await fetch('/direction', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({direction}),
    });
    if (res.ok) input.value = '';
  } catch(e) { console.error(e); }
}

document.getElementById('direction-input').addEventListener('keydown', (e) => {
  if (e.key === 'Enter') sendDirection();
});

function autoScroll(el) {
  const isNearBottom = el.scrollHeight - el.scrollTop - el.clientHeight < 150;
  if (isNearBottom) el.scrollTop = el.scrollHeight;
}

function protectLatex(text) {
  const placeholders = [];
  let idx = 0;
  text = text.replace(/\$\$([\s\S]*?)\$\$/g, (m) => {
    const ph = `%%LB${idx}%%`; placeholders.push({ ph, val: m }); idx++; return ph;
  });
  text = text.replace(/\\\[([\s\S]*?)\\\]/g, (m) => {
    const ph = `%%LB${idx}%%`; placeholders.push({ ph, val: m }); idx++; return ph;
  });
  text = text.replace(/(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)/g, (m) => {
    const ph = `%%LI${idx}%%`; placeholders.push({ ph, val: m }); idx++; return ph;
  });
  text = text.replace(/\\\((.+?)\\\)/g, (m) => {
    const ph = `%%LI${idx}%%`; placeholders.push({ ph, val: m }); idx++; return ph;
  });
  return { text, placeholders };
}

function restoreLatex(html, placeholders) {
  for (const { ph, val } of placeholders) html = html.replace(ph, val);
  return html;
}

function renderMarkdownAndLatex(rawText, el) {
  const { text, placeholders } = protectLatex(rawText);
  let html = marked.parse(text);
  html = restoreLatex(html, placeholders);
  el.innerHTML = html;
  renderMathInElement(el, {
    delimiters: [
      { left: '$$', right: '$$', display: true },
      { left: '\\[', right: '\\]', display: true },
      { left: '$', right: '$', display: false },
      { left: '\\(', right: '\\)', display: false },
    ],
    throwOnError: false,
    trust: true,
  });
}

function clearPanel(id) {
  document.getElementById(id).innerHTML = '';
  if (id === 'thinker') { thinkerRaw = ''; thinkerBlock = null; thinkerDirty = false; }
  if (id === 'extractor') { extractorRaw = ''; extractorBlock = null; extractorDirty = false; }
}

// ── Process events from poll responses ──

function processThinkerEvents(events) {
  for (const ev of events) {
    if (ev.type === 'round_start') {
      thinkerDot.className = 'status-dot active';
      // Clear left panel at start of each round
      thinkerEl.innerHTML = '';
      thinkerRaw = '';
      thinkerDirty = false;
      const header = document.createElement('div');
      header.className = 'round-header';
      header.textContent = `Round ${ev.round}: ${ev.topic}`;
      thinkerEl.appendChild(header);
      thinkerBlock = document.createElement('div');
      thinkerBlock.className = 'content-block';
      thinkerEl.appendChild(thinkerBlock);
    } else if (ev.type === 'token' && thinkerBlock) {
      thinkerRaw += ev.token;
      thinkerDirty = true;
    } else if (ev.type === 'round_end') {
      thinkerDot.className = 'status-dot idle';
      if (thinkerBlock) {
        renderMarkdownAndLatex(thinkerRaw, thinkerBlock);
        autoScroll(thinkerEl);
        thinkerBlock = null;
        thinkerDirty = false;
      }
    } else if (ev.type === 'error') {
      const err = document.createElement('div');
      err.className = 'error';
      err.textContent = `Error: ${ev.error}`;
      thinkerEl.appendChild(err);
    }
  }
}

function processExtractorEvents(events) {
  for (const ev of events) {
    if (ev.type === 'extract_start') {
      extractorDot.className = 'status-dot active';
      const header = document.createElement('div');
      header.className = 'round-header';
      header.textContent = `Analysis of Round ${ev.round}: ${ev.topic}`;
      extractorEl.appendChild(header);
      extractorRaw = '';
      extractorBlock = document.createElement('div');
      extractorBlock.className = 'content-block';
      extractorEl.appendChild(extractorBlock);
    } else if (ev.type === 'token' && extractorBlock) {
      extractorRaw += ev.token;
      extractorDirty = true;
    } else if (ev.type === 'extract_end') {
      extractorDot.className = 'status-dot idle';
      if (extractorBlock) {
        renderMarkdownAndLatex(extractorRaw, extractorBlock);
        autoScroll(extractorEl);
        extractorBlock = null;
        extractorDirty = false;
      }
    } else if (ev.type === 'error') {
      const err = document.createElement('div');
      err.className = 'error';
      err.textContent = `Error: ${ev.error}`;
      extractorEl.appendChild(err);
    }
  }
}

// ── Polling loops ──

async function pollThinker() {
  try {
    const res = await fetch(`/poll/thinker?since=${thinkerCursor}`);
    const data = await res.json();
    if (data.events.length > 0) {
      processThinkerEvents(data.events);
    }
    thinkerCursor = data.next;
  } catch(e) {}
}

async function pollExtractor() {
  try {
    const res = await fetch(`/poll/extractor?since=${extractorCursor}`);
    const data = await res.json();
    if (data.events.length > 0) {
      processExtractorEvents(data.events);
    }
    extractorCursor = data.next;
  } catch(e) {}
}

// ── Render loop (separate from polling to avoid jank) ──

function renderLoop() {
  if (thinkerDirty && thinkerBlock) {
    renderMarkdownAndLatex(thinkerRaw, thinkerBlock);
    autoScroll(thinkerEl);
    thinkerDirty = false;
  }
  if (extractorDirty && extractorBlock) {
    renderMarkdownAndLatex(extractorRaw, extractorBlock);
    autoScroll(extractorEl);
    extractorDirty = false;
  }
}

// Poll every 200ms, render every 400ms
setInterval(pollThinker, 200);
setInterval(pollExtractor, 200);
setInterval(renderLoop, 400);

// ── Stats polling ──
setInterval(async () => {
  try {
    const res = await fetch('/stats');
    const s = await res.json();
    const mins = Math.floor(s.elapsed_seconds / 60);
    const secs = s.elapsed_seconds % 60;
    document.getElementById('elapsed').textContent =
      `${String(mins).padStart(2,'0')}:${String(secs).padStart(2,'0')}`;
    document.getElementById('rounds').textContent = s.rounds_completed;
    document.getElementById('extractions').textContent = s.extractions;
  } catch(e) {}
}, 1000);
</script>

</body>
</html>
"""

# ── Entry point ─────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    print("\n  Math Research Dashboard")
    print("  Open http://localhost:8765 in your browser\n")
    uvicorn.run(app, host="0.0.0.0", port=8765, log_level="warning")
