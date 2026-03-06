"""
Math Thinker Agent — Streams chain-of-thought math derivations in LaTeX.
Logs all output to a shared log file for the extractor to consume.
"""

import asyncio
import json
import time
import os
from openai import AsyncOpenAI

API_BASE = "https://spark-4a7e.tail2214e5.ts.net/v1"
API_KEY = "assignment6"
MODEL = "gpt-oss-120b"
LOG_FILE = os.path.join(os.path.dirname(__file__), "thinking_log.jsonl")
STREAM_FILE = os.path.join(os.path.dirname(__file__), "live_stream.txt")

MATH_TOPICS = [
    "Explore connections between the Riemann zeta function and prime distribution. Derive novel bounds or identities. Show all work in LaTeX.",
    "Investigate properties of partition functions in number theory. Derive asymptotic formulas or discover recurrence relations. Show all derivations in LaTeX.",
    "Explore the relationship between eigenvalues of random matrices and zeros of L-functions. Derive any interesting identities or bounds in LaTeX.",
    "Investigate novel inequalities involving special functions (Gamma, Beta, hypergeometric). Attempt to derive tighter bounds than known results. Show all work in LaTeX.",
    "Explore combinatorial identities involving Catalan numbers, Stirling numbers, and binomial coefficients. Try to discover or prove new identities. Show all work in LaTeX.",
    "Investigate the analytic continuation of Dirichlet series and derive functional equations or transformation formulas. Show all derivations in LaTeX.",
    "Explore connections between modular forms and elliptic curves. Derive interesting q-series expansions or congruences. Show all work in LaTeX.",
    "Investigate extremal problems in graph theory and derive bounds using algebraic or probabilistic methods. Show all derivations in LaTeX.",
]

client = AsyncOpenAI(base_url=API_BASE, api_key=API_KEY)


async def think_about_math(topic: str, round_num: int):
    """Stream a math derivation and log everything."""
    prompt = (
        f"You are a research mathematician exploring open problems. "
        f"Think deeply and show all derivations step by step in LaTeX (use $...$ for inline and $$...$$ for display math). "
        f"Be rigorous. If you discover something that seems novel or surprising, highlight it clearly.\n\n"
        f"Topic: {topic}"
    )

    # Clear live stream file for this round
    with open(STREAM_FILE, "w") as f:
        f.write(f"=== ROUND {round_num} ===\n")
        f.write(f"Topic: {topic}\n")
        f.write("=" * 60 + "\n\n")

    full_response = ""
    chunk_buffer = ""

    try:
        stream = await client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
            max_tokens=4096,
            temperature=0.8,
        )

        async for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                token = chunk.choices[0].delta.content
                full_response += token
                chunk_buffer += token

                # Write to live stream file
                with open(STREAM_FILE, "a") as f:
                    f.write(token)

                # Print to stdout in real time
                print(token, end="", flush=True)

                # Periodically flush to log (every ~200 chars)
                if len(chunk_buffer) > 200:
                    _append_log(round_num, "chunk", chunk_buffer)
                    chunk_buffer = ""

        # Flush remaining buffer
        if chunk_buffer:
            _append_log(round_num, "chunk", chunk_buffer)

        # Log the complete response
        _append_log(round_num, "complete", full_response, topic=topic)
        print("\n\n" + "=" * 60 + "\n")

    except Exception as e:
        print(f"\n[Thinker Error] {e}")
        _append_log(round_num, "error", str(e))

    return full_response


def _append_log(round_num: int, event_type: str, content: str, topic: str = ""):
    entry = {
        "timestamp": time.time(),
        "round": round_num,
        "type": event_type,
        "content": content,
    }
    if topic:
        entry["topic"] = topic
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")


async def main():
    print("=" * 60)
    print("  MATH THINKER AGENT — Continuous Exploration")
    print("=" * 60)
    print()

    round_num = 0
    while True:
        topic = MATH_TOPICS[round_num % len(MATH_TOPICS)]
        round_num += 1
        print(f"\n>>> ROUND {round_num}: {topic[:80]}...\n")
        await think_about_math(topic, round_num)
        # Brief pause between rounds
        await asyncio.sleep(2)


if __name__ == "__main__":
    asyncio.run(main())
