"""
Simple single-file runner — runs thinker and extractor concurrently
with colored terminal output. No TUI dependency.
"""

import asyncio
import json
import os
import time
from openai import AsyncOpenAI

API_BASE = "https://spark-4a7e.tail2214e5.ts.net/v1"
API_KEY = "assignment6"
MODEL = "gpt-oss-120b"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(SCRIPT_DIR, "thinking_log.jsonl")
RESULTS_FILE = os.path.join(SCRIPT_DIR, "novel_results.txt")

# ANSI colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"

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

EXTRACTION_PROMPT = """You are a mathematical reviewer. Analyze the following mathematical derivation and identify:

1. **Novel Results**: Any identities, bounds, formulas, or theorems that appear to be new or non-standard.
2. **Interesting Connections**: Unexpected links between different areas of mathematics.
3. **Potential Errors**: Any logical gaps or errors in the derivation.
4. **Significance**: Rate the mathematical significance (Low / Medium / High / Potentially Groundbreaking).

For each novel result found, state it precisely in LaTeX and explain why it might be new.
If nothing novel is found, say "No novel results detected" and explain what was standard.

Be rigorous and skeptical — most derivations will reproduce known results.

DERIVATION:
{derivation}
"""

client = AsyncOpenAI(base_url=API_BASE, api_key=API_KEY)

# Shared state
completed_derivations = asyncio.Queue()


async def thinker():
    """Continuously generate math derivations."""
    round_num = 0
    while True:
        topic = MATH_TOPICS[round_num % len(MATH_TOPICS)]
        round_num += 1

        print(f"\n{GREEN}{BOLD}{'=' * 70}")
        print(f"  THINKER — Round {round_num}")
        print(f"  Topic: {topic[:65]}...")
        print(f"{'=' * 70}{RESET}\n")

        full_response = ""
        try:
            stream = await client.chat.completions.create(
                model=MODEL,
                messages=[{
                    "role": "user",
                    "content": (
                        "You are a research mathematician exploring open problems. "
                        "Think deeply and show all derivations step by step in LaTeX "
                        "(use $...$ for inline and $$...$$ for display math). "
                        "Be rigorous. If you discover something that seems novel or surprising, highlight it clearly.\n\n"
                        f"Topic: {topic}"
                    )
                }],
                stream=True,
                max_tokens=4096,
                temperature=0.8,
            )

            async for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    token = chunk.choices[0].delta.content
                    full_response += token
                    print(f"{GREEN}{token}{RESET}", end="", flush=True)

        except Exception as e:
            print(f"\n{RED}[Thinker Error] {e}{RESET}")
            await asyncio.sleep(5)
            continue

        print(f"\n{GREEN}{DIM}[Round {round_num} complete — {len(full_response)} chars]{RESET}\n")

        # Log to file
        entry = {
            "timestamp": time.time(),
            "round": round_num,
            "type": "complete",
            "topic": topic,
            "content": full_response,
        }
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(entry) + "\n")

        # Queue for extraction
        await completed_derivations.put((round_num, topic, full_response))
        await asyncio.sleep(2)


async def extractor():
    """Process completed derivations and extract novel results."""
    while True:
        round_num, topic, derivation = await completed_derivations.get()

        if len(derivation) < 100:
            print(f"{YELLOW}[Extractor] Skipping round {round_num} — too short{RESET}")
            continue

        print(f"\n{CYAN}{BOLD}{'─' * 70}")
        print(f"  EXTRACTOR — Analyzing Round {round_num}")
        print(f"  Topic: {topic[:65]}...")
        print(f"{'─' * 70}{RESET}\n")

        full_response = ""
        try:
            stream = await client.chat.completions.create(
                model=MODEL,
                messages=[{
                    "role": "user",
                    "content": EXTRACTION_PROMPT.format(derivation=derivation)
                }],
                stream=True,
                max_tokens=2048,
                temperature=0.3,
            )

            async for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    token = chunk.choices[0].delta.content
                    full_response += token
                    print(f"{CYAN}{token}{RESET}", end="", flush=True)

        except Exception as e:
            print(f"\n{RED}[Extractor Error] {e}{RESET}")
            continue

        print(f"\n{CYAN}{DIM}[Extraction complete]{RESET}\n")

        # Save results
        with open(RESULTS_FILE, "a") as f:
            f.write(f"\n{'=' * 60}\n")
            f.write(f"Round {round_num} — {topic[:60]}\n")
            f.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"{'=' * 60}\n")
            f.write(full_response + "\n")


async def main():
    # Clean previous logs
    for f in [LOG_FILE, RESULTS_FILE]:
        if os.path.exists(f):
            os.remove(f)

    print(f"{BOLD}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║          MATH RESEARCH PIPELINE — Live Explorer            ║")
    print("║                                                            ║")
    print("║  {0}Thinker output in green{1}    {2}Extractor output in cyan{1}     ║".format(GREEN, RESET + BOLD, CYAN))
    print("║  Model: gpt-oss-120b       Press Ctrl+C to stop           ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(f"{RESET}\n")

    try:
        await asyncio.gather(thinker(), extractor())
    except KeyboardInterrupt:
        print(f"\n{YELLOW}Shutting down...{RESET}")
        print(f"  Logs:    {LOG_FILE}")
        print(f"  Results: {RESULTS_FILE}")


if __name__ == "__main__":
    asyncio.run(main())
