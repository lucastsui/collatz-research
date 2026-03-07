# Sharing Guide: Who Should See What

## The Main Document

**`paper_alpha_identity.md`** — The clean writeup containing all three shareable results:
1. The Alpha Identity (Theorem 1): w_t - 4*2^A = -3^{t+1}*n
2. The modular cascade proof for k <= 5 (Theorem 2)
3. The polynomial/Rearrangement observation (Section 5)

This is the document to share. Everything else is working notes.

---

## Tier 1: Researchers Who Work Directly on Collatz Cycles

These people have published on the exact problem (bounding nontrivial cycle lengths):

### Christian Hercher
- **Affiliation**: Europa-Universitat Flensburg
- **Relevance**: Proved no m-cycles with m <= 91 (current best, arXiv:2201.00406). Uses Steiner-type bounds + computation. The Alpha Identity gives an algebraic explanation for WHY this approach works.
- **What to share**: The full paper. Especially Theorem 1 and the modular cascade (Theorem 2), which provides an independent method.
- **Contact**: ResearchGate profile active.

### Bram de Weger (joint with John Simons)
- **Affiliation**: Technische Universiteit Eindhoven (emeritus)
- **Relevance**: Proved no k-cycles with k <= 68 (2005, Acta Arithmetica). Pioneered the computational approach. The Alpha Identity explains the algebraic mechanism behind their computational results.
- **What to share**: Theorem 1 (the identity) and the observation that it reduces no-cycles to convergence algebraically.

### Shalom Eliahou
- **Affiliation**: Universite du Littoral Cote d'Opale
- **Relevance**: Established the foundational lower bounds on cycle lengths (1993). The Steiner bound n < (3/2)^{k-1} used in our proof comes from this lineage.
- **What to share**: The k <= 5 proof (Theorem 2) as a clean new method.

### Lorenz Halbeisen and Norbert Hungerbuhler
- **Affiliation**: ETH Zurich
- **Relevance**: Optimal bounds for rational Collatz cycles (Acta Arithmetica, 1997). Refined Eliahou's criterion. Their algebraic approach is closest in spirit to the Alpha Identity.
- **What to share**: The full paper. The closed-form identity alpha = -3^{t+1}*n is exactly the kind of algebraic result they work with.

---

## Tier 2: Leading Researchers in Related Areas

### Terence Tao
- **Affiliation**: UCLA
- **Relevance**: Proved "almost all Collatz orbits attain almost bounded values" (2022). His work uses Syracuse dynamics and logarithmic density arguments. The Alpha Identity connects to his approach: it shows that convergence implies no-cycles, so his "almost all converge" result immediately gives "almost all don't cycle" via an algebraic route (rather than just probabilistic).
- **What to share**: Brief note highlighting Theorem 1 and the corollary. He likely knows this reduction conceptually but may not have seen the explicit identity.
- **Caveat**: He receives enormous volumes of Collatz-related email. Keep it brief.

### Jeffrey C. Lagarias
- **Affiliation**: University of Michigan
- **Relevance**: The world expert on the 3x+1 problem. Edited "The Ultimate Challenge" (AMS, 2010). His 2021 survey (arXiv:2111.02635) is comprehensive. He would know immediately whether the Alpha Identity is truly new or a known result in disguise.
- **What to share**: Theorem 1 only, with a specific question: "Is this identity known?" He can assess novelty instantly.
- **Caveat**: Same as Tao — brevity essential.

### Joseph Silverman
- **Affiliation**: Brown University
- **Relevance**: Pioneer of arithmetic dynamics. His framework (heights, canonical heights, periodic points) is the natural language for the Fermat curve perspective. The polynomial reformulation (Section 5) connects to his work on dynamics of rational maps.
- **What to share**: Section 5 (polynomial reformulation) and the Rearrangement observation, framed as an arithmetic dynamics question.

---

## Tier 3: Adjacent Fields

### Alex Kontorovich
- **Affiliation**: Rutgers University
- **Relevance**: Joint work with Lagarias on stochastic models for 3x+1. The Alpha Identity's probabilistic consequence (convergent orbits can't cycle) might connect to his probabilistic approach.
- **What to share**: Brief note on Theorem 1.

### Marc Chamberland
- **Affiliation**: Grinnell College
- **Relevance**: Contributed to Lagarias' book on number-theoretic and dynamical aspects. Published on binary representation and Collatz.
- **What to share**: The modular cascade method (Theorem 2) — it's elementary and self-contained.

---

## How to Share

1. **arXiv preprint**: Convert `paper_alpha_identity.md` to LaTeX, submit to arXiv under math.NT (Number Theory) with secondary tags math.DS (Dynamical Systems).

2. **Direct email**: For Tier 1 researchers, a brief email with the preprint link and a 3-sentence summary: "We prove an algebraic identity (alpha = -3^{t+1}*n) connecting the Collatz cascade sum to the starting value. This reduces no-cycles to convergence. Combined with Barina's verification, no cycle has starting value < 2^68."

3. **MathOverflow**: Post the polynomial reformulation (Section 5) as a question: "Is it known that the Collatz cycle equation is equivalent to asking whether a polynomial with strictly decreasing power-of-2 coefficients, evaluated at 3, is divisible by 2^p - 3^k?"

---

## Novelty Assessment

Before sharing, verify novelty by checking:
- Lagarias' survey (arXiv:2111.02635) for the Alpha Identity
- Hercher's paper (arXiv:2201.00406) for the modular cascade method
- Halbeisen-Hungerbuhler for the algebraic approach to cycle bounds

The Alpha Identity may be implicit in the Syracuse-cycle-equation literature but the explicit closed form alpha = -3^{t+1}*n and its proof by telescoping appear to be new.
