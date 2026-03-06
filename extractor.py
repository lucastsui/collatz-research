"""
Extractor Agent — Monitors the thinker's log in real time,
extracts novel/interesting mathematical results, and logs them.
"""

import asyncio
import json
import os
import time
from openai import AsyncOpenAI

API_BASE = "https://spark-4a7e.tail2214e5.ts.net/v1"
API_KEY = "assignment6"
MODEL = "gpt-oss-120b"
LOG_FILE = os.path.join(os.path.dirname(__file__), "thinking_log.jsonl")
RESULTS_FILE = os.path.join(os.path.dirname(__file__), "novel_results.jsonl")
RESULTS_DISPLAY = os.path.join(os.path.dirname(__file__), "novel_results.txt")

client = AsyncOpenAI(base_url=API_BASE, api_key=API_KEY)


EXTRACTION_PROMPT = """You are a mathematical reviewer. Analyze the following mathematical derivation and identify:

1. **Novel Results**: Any identities, bounds, formulas, or theorems that appear to be new or non-standard.
2. **Interesting Connections**: Unexpected links between different areas of mathematics.
3. **Potential Errors**: Any logical gaps or errors in the derivation.
4. **Significance**: Rate the mathematical significance (Low / Medium / High / Potentially Groundbreaking).

For each novel result found, state it precisely in LaTeX and explain why it might be new.
If nothing novel is found, say "No novel results detected" and explain what was standard.

Be rigorous and skeptical — most derivations will reproduce known results. Only flag something as novel if it genuinely appears non-trivial and unfamiliar.

DERIVATION:
{derivation}
"""


async def extract_results(derivation: str, round_num: int, topic: str):
    """Send a completed derivation to the model for novelty extraction."""
    prompt = EXTRACTION_PROMPT.format(derivation=derivation)

    print(f"\n{'─' * 60}")
    print(f"  EXTRACTING from Round {round_num}")
    print(f"  Topic: {topic[:70]}...")
    print(f"{'─' * 60}\n")

    full_response = ""

    try:
        stream = await client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            max_tokens=2048,
            temperature=0.3,
        )

        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                full_response += token
                print(token, end="", flush=True)

        print("\n")

        # Save result
        entry = {
            "timestamp": time.time(),
            "round": round_num,
            "topic": topic,
            "analysis": full_response,
        }
        with open(RESULTS_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")

        # Append to human-readable display file
        with open(RESULTS_DISPLAY, "a") as f:
            f.write(f"\n{'=' * 60}\n")
            f.write(f"Round {round_num} — {topic[:70]}\n")
            f.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'=' * 60}\n")
            f.write(full_response)
            f.write("\n")

    except Exception as e:
        print(f"\n[Extractor Error] {e}")

    return full_response


async def monitor_log():
    """Tail the thinking log and extract from completed derivations."""
    print("=" * 60)
    print("  EXTRACTOR AGENT — Monitoring for Novel Results")
    print("=" * 60)
    print(f"\n  Watching: {LOG_FILE}")
    print(f"  Results:  {RESULTS_DISPLAY}\n")

    processed_rounds = set()
    file_pos = 0

    # Wait for log file to exist
    while not os.path.exists(LOG_FILE):
        print("  Waiting for thinker to start...")
        await asyncio.sleep(2)

    print("  Log file detected. Monitoring...\n")

    while True:
        try:
            with open(LOG_FILE, "r") as f:
                f.seek(file_pos)
                new_lines = f.readlines()
                file_pos = f.tell()

            for line in new_lines:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue

                # Only process complete derivations
                if entry.get("type") == "complete" and entry["round"] not in processed_rounds:
                    processed_rounds.add(entry["round"])
                    topic = entry.get("topic", "Unknown topic")
                    derivation = entry["content"]

                    if len(derivation) > 100:  # Skip trivially short outputs
                        await extract_results(derivation, entry["round"], topic)
                    else:
                        print(f"  [Round {entry['round']}] Skipped — too short ({len(derivation)} chars)")

        except Exception as e:
            print(f"  [Monitor Error] {e}")

        await asyncio.sleep(3)


if __name__ == "__main__":
    asyncio.run(monitor_log())
