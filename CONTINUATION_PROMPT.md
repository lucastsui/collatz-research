# Continuation Prompt for Next Session

## What This Project Is

You are continuing a multi-session research project on the **Collatz conjecture** (no nontrivial cycles). The project is at `~/Desktop/math/` and pushed to https://github.com/lucastsui/collatz-research.

## Key Files to Read First

1. **`map.md`** — The problem decomposition tree. This is the master document showing all branches explored, what worked, what failed, and where we are now. READ THIS FIRST.

2. **`theorems_and_proofs.md`** — All 15 theorems with complete proofs. The most important are Theorems 12-15 (the Combined Theorem).

3. **`session_log.md`** — Verbatim conversation log. Very long but contains all reasoning.

4. **`paper_spectral_gap.md`** — Draft paper (568 lines) on the spectral gap result. Needs updating with the key lemma (Theorem 15).

## Where We Are Now

### The Big Result (Combined Theorem, PROVED)

For every prime p ≥ 5, the affine Collatz Markov operator M on Z/pZ defined by:

(Mf)(x) = ½f(x·2⁻¹) + ½f((3x+1)·2⁻¹)

has **no eigenvalue of absolute value 1** on the non-constant subspace. Therefore |λ₂(p)| < 1 for every prime.

The proof chain:
- Theorem 12: ||Mχ_r||² = ½ exactly (single-character contraction 1/√2)
- Theorem 13: |λ|=1 ⟹ λ=±1 (algebraic: |2λ-1/λ|=1 forces sinφ=0)
- Theorem 14: λ=1 ⟹ f constant ⟹ f=0
- **Theorem 15 (KEY, proved by user):** λ=-1 ⟹ f=0. Proof: conditions f(2y)=-f(y) and f(3y+α)=f(y) with α=2⁻¹ mod p. Apply first condition twice: f(4y)=f(y). Combine with second condition to get f(u)=f(u+3α) for all u. Since 3α≠0 mod p and p is prime, f is constant, hence zero.

### What Remains (One Quantitative Gap)

**Proved:** |λ₂(p)| < 1 for each individual prime p.
**Measured:** |λ₂| ≈ 0.70 ≈ 1/√2 for all 93 tested primes (p=5 to 499). No decay.
**NOT proved:** |λ₂| ≤ 1 - c for a universal constant c independent of p.

If the universal constant gap is proved, it implies no nontrivial Collatz cycles via an information-theoretic channel capacity argument (each step of ×3/÷2 destroys δ bits of additive information; after p steps, not enough information survives to specify the target 0 mod D).

### The Information-Theoretic Framing

All 8 required properties (P1-P8 in the map) reduce to one:
- The ×3/÷2 dynamics is an information channel
- Each +1 injects 1 bit, each ÷2 destroys 1 bit
- The spectral gap IS the channel error rate
- Constant gap ⟹ lossy channel ⟹ can't hit target ⟹ no cycles

### What Was Tried and Failed (Don't Repeat These)

- **Modular Feedback Theorem** (Rounds 3-4): Based on WRONG formula (C_b = Σ 2^{p-i-1}·3^{k_{>i}} is WRONG; correct is C_b = Σ 3^{k_{>i}}·2^i). Self-consistency is automatic with correct formula. PRUNED.
- **Tao adaptation**: Wrong modulus (3-adic vs D-adic) + entropy deficit. FAILS.
- **Second moment / Parseval**: PROVED impossible (C(p,k) < D regime).
- **All 6 direct algebraic approaches**: Each fails for identified reasons.
- **Circle method**: IS Fourier mod D, no new info.
- **Furstenberg ×2,×3**: O(1) invariance error, no ×3 operation on patterns.
- **Sieve + rad(D)**: Blocked at abc conjecture.

### Promising Next Steps

1. **Prove the universal constant spectral gap.** The structural part is done (no unit-circle eigenvalues). What remains is showing eigenvalues can't accumulate at 1. Approaches:
   - Show ||M²|| < 1 on the non-constant subspace (two-step contraction)
   - Use the fact that the non-contracting directions of M get rotated by M, so M² contracts everything
   - Verified for p=5: ||M²f||²/||f||² = 0.375 for the worst-case f

2. **Update the paper** (`paper_spectral_gap.md`) with Theorem 15 (the key lemma). The paper currently doesn't include it.

3. **Explore the general formulation** (in the map): Can short sums of {a,b}-smooth numbers vanish mod {a,b}-smooth targets? This is the Collatz-free version of the barrier.

## Technical Details

- **Git repo:** `~/Desktop/math/`, remote `origin` at github.com/lucastsui/collatz-research
- **Session logging:** Append verbatim exchanges to `session_log.md` (user requested strict verbatim logging)
- **Map updates:** Update `map.md` after each round of exploration, commit and push
- **Python scripts:** `collatz_spectral.py` (spectral gap computation, 924 lines), `collatz_mft_correct.py` (cycle verification with correct formula), others
- **Numerical data:** Spectral gaps computed for 93 primes, plots in .png files

## The Correct Cycle Equation (IMPORTANT — previous sessions used wrong formula)

S(I) = Σ_{j=1}^{k} 3^{k-j} · 2^{i_j}  where I = {i₁ < ... < i_k} ⊆ {0,...,p-1}
D = 2^p - 3^k
n₀ = S(I)/D (must be a positive integer for a cycle)

The CORRECT C_b formula: C_b = Σ_{i: b_i=1} 3^{k_{>i}} · 2^i (NOT 2^{p-i-1})
