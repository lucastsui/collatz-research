# Collatz Conjecture — Problem Decomposition Map

*Last updated: 2026-03-05 (Session 2)*

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
│   │  ├─ P8: Non-archimedean + archimedean fusion                      required
│   │  │
│   │  INFORMATION-THEORETIC REFRAMING (discovered late):
│   │  ├─ The ×3/÷2 dynamics is an INFORMATION CHANNEL
│   │  │  ├─ Each +1 injects 1 bit of additive information
│   │  │  ├─ Each ÷2 destroys 1 bit (discards lowest bit)
│   │  │  ├─ Net over p steps: k - p = -0.37p bits (DEFICIT)
│   │  │  └─ This IS the Kolmogorov bound (2^{0.37p} reachable patterns)
│   │  ├─ The spectral gap IS the channel error rate
│   │  │  ├─ δ ≈ 0.30 means 0.30 bits of additive noise per step
│   │  │  ├─ After p steps: signal degraded by 0.70^p ≈ 0
│   │  │  └─ Not enough surviving info to specify target (0 mod D)
│   │  ├─ ALL 8 PROPERTIES REDUCE TO ONE:
│   │  │  ★ Prove the channel error rate δ is bounded away from 0
│   │  │  ★ i.e., prove the spectral gap is CONSTANT (not c/p)
│   │  │  ★ Proved: δ ≥ c/p. Measured: δ ≈ 0.30. Gap: c/p vs constant.
│   │  ├─ ⚠ CORRECTION (Session 2): spectral gap alone does NOT
│   │  │  prove no cycles. The gap gives equidistribution mod each
│   │  │  prime q separately, but the SIEVE combining across primes
│   │  │  still needs rad(D) > C(p,k) ≈ 2^{0.95p} (the abc barrier).
│   │  │  Spectral gap is ONE ingredient, not the whole proof.
│   │  │  Two things needed: (1) constant gap AND (2) rad(D) large.
│   │  │
│   │  PROOF ATTEMPT (Round 10):
│   │  ├─ PROVED: ||Mχ_r||² = ½ exactly for all r ≠ 0                  ✅
│   │  │  Single characters contract by 1/√2 per step.
│   │  │  1 - 1/√2 ≈ 0.293 matches numerical gap 0.30.
│   │  ├─ DISCOVERED: does NOT extend to superpositions                  ⚠
│   │  │  ||Mv||² = ½||v||² + ½Re⟨T₀v,T₁v⟩
│   │  │  Cross term can equal ||v||² for orbit-constant functions.
│   │  │  So ||Mv|| = ||v|| IS possible. One-step argument fails.
│   │  ├─ PROVED: only λ = ±1 possible on unit circle                  ✅
│   │  │  |λ|=1 with λ≠±1 ⟹ |2λ-1/λ|=1 ⟹ cos(2φ)=1 ⟹ λ=±1
│   │  ├─ PROVED: λ = 1 ⟹ v = 0 (constant, orthogonal to 1)          ✅
│   │  ├─ PROVED: λ = -1 requires three simultaneous conditions:        ✅
│   │  │  (a) ord_p(2) is even
│   │  │  (b) v constant on orbits of y → 3y + 2^{-1}
│   │  │  (c) ×2 map sends each affine orbit to a DIFFERENT orbit
│   │  │  These are mutually inconsistent for MOST primes.
│   │  ├─ ★ PROVED: λ = -1 impossible for ALL primes p ≥ 5              ✅ KEY LEMMA
│   │  │  Proof (by user):
│   │  │  (1) f(2y)=-f(y) applied twice: f(4y)=f(y)
│   │  │  (2) Substitute y→4y in f(3y+α)=f(y): f(12y+α)=f(y)
│   │  │  (3) Substitute y→3y+α in f(4y)=f(y): f(12y+4α)=f(y)
│   │  │  (4) Therefore f(u)=f(u+3α) for all u (since gcd(12,p)=1)
│   │  │  (5) 3α=3·2⁻¹≠0 mod p, and Z/pZ prime ⟹ f constant ⟹ f=0  ∎
│   │  │
│   │  └─ COMBINED THEOREM:                                              ✅ PROVED
│   │     For every prime p ≥ 5, every eigenvalue of the affine
│   │     Collatz operator on the non-constant subspace satisfies |λ|<1.
│   │     Proof: |λ|=1 ⟹ λ=±1 (algebraic) ⟹ f=0 (both cases).
│   │
│   │     REMAINING QUANTITATIVE QUESTION:
│   │     Is |λ₂| ≤ 1 - c for a UNIVERSAL constant c?
│   │     ├─ Proved: |λ₂| < 1 for each individual prime              ✅
│   │     ├─ Measured: |λ₂| ≈ 0.70 for all 93 tested primes           ✅
│   │     ├─ Not proved: universal constant bound                       ❌
│   │     └─ This is now a QUANTITATIVE gap, not a structural one.
│   │        The structural obstruction (λ on unit circle) is eliminated.
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
│   ├─ ROUND 9: Beyond spectral gap (2 agents)
│   │  ├─ Second moment / pair correlation                               ✘ PROVED IMPOSSIBLE
│   │  │  ├─ Cauchy-Schwarz + Parseval requires C(p,k) > D              ✘
│   │  │  ├─ But C(p,k) ≈ 2^{0.95p} < D ≈ 2^p                         ✘ wrong regime
│   │  │  ├─ Gap: D/C ≈ 2^{0.05p} — exponential, unbridgeable          ✘
│   │  │  └─ No weight/sieve variant can overcome this                   ✘ PROVED
│   │  └─ Direct algebraic impossibility (6 approaches)                  ✘ ALL FAIL
│   │     ├─ 2^p ≡ 3^k mod D relation                                   ✘ no contradiction
│   │     ├─ Size bounds on S and n₀                                     ✘ range too large
│   │     ├─ Mod-q sieve for q|D                                         ✘ → abc barrier
│   │     ├─ Transfer matrix / closed loop                               ✘ tautological
│   │     ├─ Obstruction certificates (2-adic)                           ✘ necessary not sufficient
│   │     └─ Monotonicity / convexity                                    ✘ too weak
│   │
│   └─ CURRENT STATE
│      │
│      ├─ WHAT WE PROVED (novel results):
│      │  ├─ Theorem 4: Equidistribution of S mod q                      ✅ rigorous
│      │  ├─ Theorem 5: Composite moduli extension                       ✅ rigorous
│      │  ├─ Theorem 6: abc ⟹ no nontrivial cycles                     ✅ conditional
│      │  ├─ Theorem 11: Spectral gap |λ₂| ≤ 1 - c/p (weak bound)     ✅ novel, unconditional
│      │  ├─ Theorem 12: ||Mχ_r||² = ½ (single-character contraction)  ✅ exact
│      │  ├─ Theorem 13: |λ|=1 ⟹ λ=±1 (algebraic restriction)        ✅ rigorous
│      │  ├─ Theorem 14: λ=1 ⟹ f=0 on non-constant subspace           ✅ rigorous
│      │  ├─ Theorem 15: λ=-1 ⟹ f=0 (key lemma, user's proof)        ✅ rigorous
│      │  ├─ ★ COMBINED THEOREM: No unit-circle eigenvalues for M       ✅ MAIN RESULT
│      │  │  For every prime p ≥ 5, every eigenvalue of M on the
│      │  │  non-constant subspace satisfies |λ| < 1.
│      │  │  Proof: |λ|=1 ⟹ λ=±1 (Thm 13) ⟹ f=0 (Thms 14,15).
│      │  ├─ Numerical: constant gap ≈ 0.30 (93 primes tested)          ✅ strong evidence
│      │  ├─ "+1 advantage": ratio > 16000× over multiplicative walk    ✅ confirmed
│      │  ├─ Kolmogorov reduction to 2^{0.37p} candidates               ✅ rigorous
│      │  └─ No cycles for p ≤ 29 (correct formula)                     ✅ computational
│      │
│      ├─ ACTIVE FRONTIER:                                               ~ PARTIAL
│      │  Prove |λ₂| ≤ 1 - c for a UNIVERSAL constant c > 0.
│      │  ├─ Structural: no eigenvalues on unit circle                   ✅
│      │  ├─ Corrected numerics: |λ₂| ∈ [0.66, 0.81] for 166 primes    ✅
│      │  ├─ ★ THEOREM 16 (NEW): constant gap for ALMOST ALL primes     ✅ PROVED
│      │  │  If |⟨2,3⟩| ≥ p^{1/2+ε}, then |λ₂| ≤ 1 - c(ε).
│      │  │  By Erdős-Murty: holds for density-1 set of primes.
│      │  │  Proof: phase constraint + orbit equidistribution + Gauss sums.
│      │  │  Full proof in agent_sum_product.md, Sections 3-9.
│      │  ├─ Bounded orbit → constant gap (by compactness + Combined Thm) ✅
│      │  ├─ If universal gap proved: info-theoretic ⟹ no cycles        ★
│      │  │
│      │  ├─ REMAINING GAP: primes where |⟨2,3⟩| < p^{1/2+ε}          ❌ OPEN
│      │  │  Both ord_p(2) and ord_p(3) are O(√p).
│      │  │  3 agents independently converge to same algebraic core:
│      │  │  ├─ B-G: standard framework fails (D=1), need bilinear      ✘
│      │  │  │  sum-product with phases
│      │  │  ├─ Sum-product: Gauss equidistribution needs ℓ > √p        ✘ partial
│      │  │  ├─ Coupling/entropy: all 4 approaches → same core          ✘ identified
│      │  │  └─ ★ THE ALGEBRAIC CORE:
│      │  │     Inter-coset expansion: how ×2 mixes energy between
│      │  │     ⟨3⟩-cosets within ⟨2,3⟩-orbits. Cayley graph of
│      │  │     F_p*/⟨3⟩ with generator 2·⟨3⟩.
│      │  │
│      │  └─ APPROACHES DISPROVED:
│      │     ├─ Orbit-averaged sin² lemma: FALSE (decays as C/log p)    ✘
│      │     ├─ sin²-weight Lyapunov: weighted op norm grows O(p)       ✘
│      │     └─ ||M²||_op uniform bound: grows → 1                     ✘
│      │
│      ├─ WHAT'S BEEN RULED OUT:
│      │  ├─ Equidistribution mod D directly                             ✘ blocks too large
│      │  ├─ Sieve + rad(D) unconditionally                              ✘ abc barrier
│      │  ├─ Tao's 3-adic technique                                      ✘ wrong modulus + entropy
│      │  ├─ Circle method                                               ✘ IS Fourier mod D
│      │  ├─ Modular Feedback Theorem                                    ✘ formula error
│      │  ├─ Second moment / Parseval                                    ✘ C < D regime
│      │  ├─ Spectral gap alone (info-theoretic needs |λ₂|<0.483)      ✘ numerical |λ₂|≈0.70
│      │  ├─ Furstenberg measure rigidity                                ✘ invariance has O(1) error
│      │  └─ All 6 direct algebraic approaches                          ✘ insufficient
│      │
│      └─ GENERAL FORMULATION (Collatz-free):
│         Given multiplicatively independent integers a, b:
│         Can a SHORT linear combination of mixed powers a^i · b^j
│         (O(log D) terms) vanish modulo D = a^n - b^m?
│         i.e., can short sums of {a,b}-smooth numbers be divisible
│         by specific {a,b}-smooth targets?
│         This is the fundamental open problem at the boundary of
│         additive combinatorics, multiplicative number theory,
│         and Diophantine approximation.
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
