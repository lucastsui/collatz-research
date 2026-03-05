# Collatz Conjecture — Problem Decomposition Map

*Last updated: 2026-03-05*

**Legend:** ✅ proved/done · ✘ failed/dead end · ❌ blocked/open · ⚠ error found · ~ partial · ❓ unexplored · ★ recommended

---

```
Collatz Conjecture
├── Part 1: No nontrivial cycles ← ACTIVE FOCUS
│   │
│   ├─ FORMULATION
│   │  n₀ = S(I)/D where S(I) = Σ 3^{k-j}·2^{i_j}, D = 2^p - 3^k
│   │  Cycle exists ⟺ D | S(I) for some nontrivial pattern I
│   │  Key structural fact: 3^k/2^p ≡ 1 mod D (multiplicative part is identity)
│   │  So cycle question is purely about TRANSLATION C_b mod D
│   │
│   ├─ PROVED RESULTS
│   │  ├─ Theorem 4: Equidistribution of S mod q (prime q ≥ 5)          ✅
│   │  ├─ Theorem 5: Extension to composite squarefree moduli            ✅
│   │  ├─ Theorem 6: abc ⟹ no nontrivial cycles (conditional)          ✅
│   │  ├─ Special cases k=1 (trivial), k=2 (exhaustive), k=p-1 (D<0)   ✅
│   │  ├─ Kolmogorov reduction: only 2^{0.37p} candidate patterns       ✅
│   │  └─ Computation: no cycles for p ≤ 29 (correct formula)           ✅
│   │
│   ├─ ROUND 1: Equidistribution + Sieve
│   │  ├─ Per-prime equidistribution (block decomposition + Gauss sums)  ✅ PROVED
│   │  ├─ Independence across primes (CRT + composite Gauss sums)        ✅ PROVED
│   │  ├─ Direct equidistribution mod D                                  ✘ IMPOSSIBLE
│   │  │  └─ Block size > p when ord_D(2) > 2√D → zero complete blocks
│   │  └─ Sieve needs rad(D) > 2^{0.95p}                                ❌ BLOCKED
│   │     ├─ abc conjecture gives it                                     ✅ conditional
│   │     ├─ Stewart 2013: log rad ≥ c√p/log p                          ✘ need 0.95p
│   │     └─ Gap equivalent to proving abc                               ✘ HARD BARRIER
│   │
│   ├─ ROUND 2: Bypass abc barrier? (4 agents)
│   │  ├─ Transfer matrix spectral analysis                              ✘ all eigenvalues = 1
│   │  ├─ Weyl differencing                                              ✘ same sum bounds
│   │  ├─ Algebraic structure 2^p ≡ 3^k mod D                           ✘ tautological
│   │  └─ Second moment method                                           ✘ circular
│   │
│   ├─ ROUND 3: Invent new approaches (4 agents)
│   │  ├─ Circle method (Hardy-Littlewood)                               ✘ IS Fourier mod D
│   │  ├─ Fixed-point / 2-adic feedback ("Modular Feedback Thm")        ⚠ formula error
│   │  ├─ Binary carry / digit analysis                                  ~ structural insights
│   │  └─ Entropy / Kolmogorov complexity                                ✅ reduction proved
│   │
│   ├─ ROUND 4: Modular Feedback Theorem (Path 1)
│   │  ├─ Computational verification (WRONG formula C_b = Σ 2^{p-i-1})  ⚠ artifacts
│   │  ├─ Correct formula identified: C_b = Σ 3^{k_{>i}} · 2^i          ✅
│   │  ├─ Self-consistency IS automatic with correct formula              ✅ confirmed
│   │  └─ PATH 1 PRUNED — based on formula error                        ✘ DEAD END
│   │
│   ├─ ROUND 5: Sparse equidistribution
│   │  ├─ Adapt Tao's 2019 Syracuse technique?                           ✘ 4 obstructions
│   │  │  ├─ Wrong modulus (3-adic vs D-adic)                            ✘
│   │  │  ├─ Entropy deficit: log(4/3) available, need log(3)            ✘
│   │  │  ├─ Average-case only                                           ✘
│   │  │  └─ Self-selection (cycles defeat random model)                 ✘
│   │  ├─ Large sieve for sparse sets?                                   ✘ error too large
│   │  │  ├─ Best bound: 2^{0.185p}, need < 1                           ✘ gap 2^{0.8p}
│   │  │  └─ Conditional: works if max|g(t)| ≤ 0.306p                   ✅ unproved
│   │  └─ IRREDUCIBLE CORE:
│   │     |Σ_{c<p} e(t·2^c/(2^p - 3^k))| ≤ p^{1-ε}
│   │     Short exponential sum: p terms in modulus 2^p
│   │     All known methods need D^ε terms. We have log(D).
│   │
│   ├─ ROUND 6: Properties P1-P8 for a new technique
│   │  ├─ P1: Ultra-short sum capability (log D terms)                   required
│   │  ├─ P2: Modulus-specific (exploit D = 2^p - 3^k)                  required
│   │  ├─ P3: Deterministic/worst-case                                   required
│   │  ├─ P4: Additive-multiplicative bridge                             required
│   │  ├─ P5: Multi-prime coherence                                      required
│   │  ├─ P6: Self-referential awareness                                 required
│   │  ├─ P7: Multi-scale                                                required
│   │  └─ P8: Non-archimedean + archimedean fusion                      required
│   │
│   ├─ ROUND 7: Candidate frameworks (2 agents)
│   │  ├─ Furstenberg ×2,×3 measure rigidity                            ✘ FAILS
│   │  │  ├─ ×2 invariance: O(1) error (fatal)                          ✘
│   │  │  ├─ No natural ×3 operation on patterns                         ✘
│   │  │  └─ "Proving μ is invariant IS the conjecture restated"         ✘
│   │  └─ Affine expansion (Bourgain-Gamburd style)                     ★ MOST VIABLE
│   │     ├─ Zariski closure = full Aff₁                                 ✅
│   │     ├─ Walk length p = mixing time O(log D)                        ✅
│   │     ├─ Satisfies P1,P2,P4,P5,P7,P8 (6 of 8)                      ✅
│   │     ├─ P3,P6 need second moment argument                           ⚠ achievable
│   │     └─ THREE REMAINING GAPS:
│   │        ├─ Gap 1: Spectral gap for solvable affine group            ❌ OPEN
│   │        │  └─ For PRIME D: Bourgain 2005 sum-product nearly works   ★ CLOSEST
│   │        ├─ Gap 2: Arithmetic of D (ord_q(2) large for q|D)         ❌ OPEN
│   │        │  └─ Related to Artin's conjecture                         conditional on GRH
│   │        └─ Gap 3: Probabilistic → deterministic (2nd moment)        ❌ OPEN
│   │           └─ Bound pair correlations of {C_b mod D}               tractable once 1+2 solved
│   │
│   ├─ ROUND 8: Research program execution (3 agents)
│   │  ├─ Spectral gap computation (93 primes, p=5 to 499)               ✅ COMPUTED
│   │  │  ├─ Affine walk gap ≈ 0.30, CONSTANT across all primes          ✅ remarkable
│   │  │  ├─ Multiplicative walk gap ≈ 0 ("+1 advantage" is enormous)    ✅ confirmed
│   │  │  ├─ No correlation with ord_p(2) or ord_p(3)                    ✅ robust
│   │  │  └─ |λ₂| ≈ 0.70 for all primes — does not decay                ✅ strong
│   │  ├─ Theoretical proof of spectral gap                              ~ PARTIAL
│   │  │  ├─ PROVED: |λ₂| ≤ 1 - c/p (unconditional, all primes)        ✅ novel
│   │  │  ├─ NOT proved: constant gap (numerical 0.30 >> proved c/p)     ❌ gap
│   │  │  └─ Heuristic: phase accumulation gives ≈ 1/2 contraction      ~ unrigorous
│   │  ├─ Baker's theorem for prime factors of D                         ✘ INSUFFICIENT
│   │  │  ├─ D CAN have small prime factors (e.g., p=10: 5|D)           ✘ counterexample
│   │  │  ├─ Cannot guarantee all q|D have q > p                         ✘
│   │  │  └─ Zsygmondy N/A (different exponents on different bases)      ✘
│   │  └─ QUANTITATIVE GAP DISCOVERED:
│   │     Even with constant gap δ=0.30, error D·(1-δ)^p = 2^{0.485p}
│   │     exceeds main term C(p,k)/D ≈ 2^{-0.05p}
│   │     Need |λ₂| < 0.483 but numerical |λ₂| ≈ 0.70
│   │     ⟹ Spectral gap alone is NOT STRONG ENOUGH
│   │
│   └─ CURRENT FRONTIER: Beyond spectral gap                            ❓ OPEN
│      │
│      ├─ WHAT WE PROVED (novel, potentially publishable):
│      │  ├─ Spectral gap |λ₂| ≤ 1 - c/p unconditionally                ✅
│      │  ├─ Numerical: constant gap ≈ 0.30 for all tested primes        ✅
│      │  └─ "+1 advantage": affine walk mixes, multiplicative doesn't   ✅
│      │
│      ├─ WHAT'S STILL NEEDED:
│      │  ├─ Either: prove |λ₂| < 0.483 (stronger than observed 0.70)   ❌ seems false
│      │  ├─ Or: find additional structure beyond spectral gap            ❓
│      │  └─ Or: entirely new approach not based on random walk mixing   ❓
│      │
│      └─ THE HONEST STATUS:
│         The spectral gap is real but not strong enough.
│         The "+1 advantage" is genuine but insufficient by itself.
│         The problem remains equivalent to the abc conjecture in difficulty.
│
└── Part 2: No divergent trajectories                                    ❌ NOT ADDRESSED
    ├── Tao 2019: almost all orbits bounded                              ✅ known
    └── Full proof for all orbits                                        ❌ requires different techniques
```

---

## Key References

- Bourgain, "Mordell's exponential sum estimate revisited" (JAMS, 2005)
- Bourgain-Gamburd, "Uniform expansion bounds for Cayley graphs of SL₂(p)" (Annals, 2008)
- Bourgain-Gamburd-Sarnak, "Affine linear sieve, expanders, and sum-product" (Inventiones, 2010)
- Tao, "Almost all orbits of the Collatz map attain almost bounded values" (Forum of Math Pi, 2022)
- Shmerkin, "On Furstenberg's intersection conjecture" (Annals, 2019)
- Stewart, "On divisors of Lucas and Lehmer numbers" (Acta Math, 2013)
- Eliahou, "The 3x+1 problem: new lower bounds on nontrivial cycle lengths" (Discrete Math, 1993)
