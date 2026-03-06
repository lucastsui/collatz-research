# Collatz Conjecture — Problem Decomposition Map

*Last updated: 2026-03-06 (Session 2)*

**Legend:** ✅ proved/done · ✘ failed/dead end · ❌ blocked/open · ⚠ error found · ~ partial · ❓ unexplored · ★ recommended

---

```
Collatz Conjecture
│
├── Part 1: No nontrivial cycles ← ACTIVE FOCUS
│   │
│   ├─ 1. FORMULATION
│   │  n₀ = S(I)/D where S(I) = Σ 3^{k-j}·2^{i_j}, D = 2^p - 3^k
│   │  Cycle exists ⟺ D | S(I) for some nontrivial pattern I
│   │  C(p,k) ≈ 2^{0.95p} candidate patterns, D ≈ 2^p
│   │  Heuristic count: C(p,k)/D ≈ 2^{-0.05p} → 0 (5% margin)
│   │
│   ├─ 2. PROVED RESULTS (novel, publishable)
│   │  ├─ Theorem 4: Equidistribution of S mod q (prime q ≥ 5)          ✅
│   │  ├─ Theorem 5: Extension to composite squarefree moduli            ✅
│   │  ├─ Theorem 6: abc ⟹ no nontrivial cycles (conditional)          ✅
│   │  ├─ Theorem 11: Spectral gap |λ₂| ≤ 1 - c/p (weak, all primes)  ✅
│   │  ├─ Theorem 12: ||Mχ_r||² = ½ (single-character contraction)     ✅
│   │  ├─ Theorem 13: |λ|=1 ⟹ λ=±1 (algebraic restriction)           ✅
│   │  ├─ Theorem 14: λ=1 ⟹ f=0 on non-constant subspace              ✅
│   │  ├─ Theorem 15: λ=-1 ⟹ f=0 (key lemma, user's proof)           ✅
│   │  ├─ ★ COMBINED THEOREM: |λ| < 1 for all eigenvalues, all p ≥ 5  ✅
│   │  ├─ Theorem 16: constant gap when |⟨2,3⟩| ≥ p^{1/2+ε}           ✅
│   │  ├─ ★★ Theorem 17: constant gap when |⟨2,3⟩| ≥ p^δ (any δ>0)   ✅
│   │  │  Uses BGK (2006). Gap constant c₁ is ABSOLUTE.
│   │  ├─ Carry Weight Identity: W_c = Σs₁(3^m) - s₁(n₀D)             ✅
│   │  ├─ Hensel lifting: equidistribution mod q^e for e ≥ 2            ✅
│   │  ├─ Kolmogorov reduction: only 2^{0.37p} candidate patterns       ✅
│   │  ├─ Special cases: k=1, k=2, k=p-1 ruled out                     ✅
│   │  └─ No cycles for p ≤ 29 (computation, correct formula)           ✅
│   │
│   ├─ 3. SUB-PROBLEM A: SPECTRAL GAP (per-prime mixing)
│   │  │  Operator M on Z/pZ: (Mf)(x) = ½f(x/2) + ½f((3x+1)/2)
│   │  │  Goal: |λ₂(p)| ≤ 1 - c for a UNIVERSAL constant c > 0
│   │  │  Status: ~95% done. Sub-polynomial subgroup case open.
│   │  │
│   │  ├─ 3a. Structural: no unit-circle eigenvalues                    ✅ DONE
│   │  │  ├─ |λ|=1 ⟹ λ=±1 (Theorem 13, algebraic)                    ✅
│   │  │  ├─ λ=1 ⟹ f=0 (Theorem 14, orbit argument)                   ✅
│   │  │  ├─ λ=-1 ⟹ f=0 (Theorem 15, periodicity trick)               ✅
│   │  │  └─ Combined: |λ₂| < 1 for every prime p ≥ 5                  ✅
│   │  │
│   │  ├─ 3b. Quantitative: constant gap for most primes               ✅ DONE
│   │  │  ├─ Weak bound |λ₂| ≤ 1-c/p (Theorem 11, Fourier + collisions) ✅
│   │  │  ├─ Theorem 16: gap for |⟨2,3⟩| ≥ p^{1/2+ε} (Gauss sums)     ✅
│   │  │  ├─ Theorem 17: gap for |⟨2,3⟩| ≥ p^δ (BGK 2006)             ✅
│   │  │  ├─ CDG product identity: (2|λ|)^{L₂} = shifted cosine product ✅
│   │  │  │  Exact case forces |λ| = 1/2. Jensen gives |λ| ≤ 1/√2.
│   │  │  │  Explains numerical |λ₂| ≈ 0.707.
│   │  │  ├─ Numerical: |λ₂| ∈ [0.66, 0.81] for 240+ primes            ✅
│   │  │  │  ρ(K) does NOT approach 1 as K→∞. gap*p GROWS with p.
│   │  │  └─ Corollary: constant gap for density-1 set (Erdős-Murty)    ✅
│   │  │
│   │  ├─ 3c. OPEN: universal gap for sub-polynomial |⟨2,3⟩|           ❌
│   │  │  ├─ These are primes where |⟨2,3⟩| = p^{o(1)}
│   │  │  ├─ The "+1" perturbation is O(1/p), gap could be O(1/K²)
│   │  │  ├─ But data says gap ≈ 0.30 even for these primes!
│   │  │  │
│   │  │  ├─ Approaches tried:
│   │  │  │  ├─ Orbit-averaged sin²: FALSE (decays as C/log p)          ✘
│   │  │  │  ├─ sin²-weight Lyapunov: op norm grows O(p)                ✘
│   │  │  │  ├─ ||M²||_op uniform bound: grows → 1                     ✘
│   │  │  │  ├─ Bourgain-Gamburd: Aff(F_p) has D=1, Phase 3 fails     ✘
│   │  │  │  ├─ Coupling/entropy: all 4 approaches → same obstruction   ✘
│   │  │  │  ├─ CDG bootstrap: error O(L₂√η) prevents closure          ✘
│   │  │  │  └─ Quotient-graph: modes don't decouple, cocycle unitary   ✘
│   │  │  │
│   │  │  └─ THE ALGEBRAIC CORE:
│   │  │     Everything reduces to bounding F_i(0) = (1/L)Σω^{3^j r_i}.
│   │  │     Small when L large (equidistribution). Can be ~1 when L small.
│   │  │     Equivalent to inter-coset expansion of ×2 on ⟨3⟩-cosets.
│   │  │     Requires non-perturbative method (not just O(1/p) corrections).
│   │  │
│   │  └─ 3d. Even if solved: spectral gap alone ≠ no cycles            ⚠
│   │     The gap gives per-prime equidistribution. Combining across
│   │     primes via sieve still needs rad(D) > 2^{0.95p} (Sub-problem B).
│   │     Spectral gap is ONE ingredient, not the whole proof.
│   │
│   ├─ 4. SUB-PROBLEM B: ARITHMETIC OF D (sieve / combining primes)
│   │  │  Goal: show enough prime factors of D have "good" equidistribution
│   │  │  so the sieve gives #{I : D|S(I)} < 1.
│   │  │  Status: blocked at abc barrier. All local-to-global methods fail.
│   │  │
│   │  ├─ 4a. The squarefree sieve (Theorems 4-5)                      ✅ DONE
│   │  │  P(S ≡ 0 mod q) = 1/q + O(e^{-cp}) for good primes q.
│   │  │  CRT combines across coprime moduli.
│   │  │  Sieve gives: #{I : D|S} ≤ C(p,k)/rad(D) · (1+o(1)).
│   │  │  Need: rad(D) > C(p,k) ≈ 2^{0.95p}.
│   │  │
│   │  ├─ 4b. Prime-power extension                                     ✅ LOCAL, ✘ GLOBAL
│   │  │  ├─ Hensel: ord_{q^e}(2) = ord_q(2)·q^{e-1} for non-Wieferich ✅
│   │  │  ├─ For e ≥ 2: equidistribution condition automatic             ✅
│   │  │  ├─ Gauss sums mod q^e (Iwaniec-Kowalski)                      ✅
│   │  │  ├─ Conductor reduction for non-unit frequencies                ✅
│   │  │  ├─ BUT: D is squarefree ~93% of the time                      ✘
│   │  │  │  Prime powers give ZERO advantage for squarefree D.
│   │  │  └─ CRT is event identity, NOT probability factorization        ⚠
│   │  │     Independence needs composite Gauss sum input (Theorem 5).
│   │  │
│   │  ├─ 4c. The abc barrier                                           ❌ BLOCKED
│   │  │  ├─ abc conjecture ⟹ rad(D) > 2^{(1-ε)p} ⟹ no cycles       ✅ conditional
│   │  │  ├─ Stewart 2013: log rad ≥ c√p/log p                          ✘ need 0.95p
│   │  │  ├─ Potential: log rad ≥ c·p/log p (Baker+Yu p-adic)          ❓ needs verification
│   │  │  ├─ D is prime ~50%, squarefree ~93% (computation)             ✅ empirical
│   │  │  └─ log₂(rad)/p ≥ 0.82 for all p ≥ 9 tested                  ✅ empirical
│   │  │
│   │  ├─ 4d. The "bad primes" reformulation                            ❌ OPEN
│   │  │  After prime-power lifting, the residual obstruction is:
│   │  │  D_bad = ∏{q|D : ord_q(2) > p} q^{e_q}
│   │  │  Need: D_bad < 2^{0.05p}. Equivalently: the "handleable"
│   │  │  prime powers of D have product > C(p,k).
│   │  │  For typical D: most mass is in large primes → D_bad ≈ D.
│   │  │  This is the abc barrier in its sharpest form.
│   │  │
│   │  └─ 4e. WHY ALL SIEVE METHODS HIT THE SAME WALL:
│   │     Every local-to-global method (sieve, spectral, Fourier)
│   │     decomposes D|S into pieces mod individual primes.
│   │     Reassembly requires controlling primes of D at scale > p²,
│   │     where block decomposition has zero complete blocks.
│   │     This is structural: tools at scale p^{O(1)} cannot reach
│   │     moduli at scale 2^p. The gap is EXPONENTIAL.
│   │
│   ├─ 5. SUB-PROBLEM C: DIRECT / CARRY ANALYSIS (abc-free attempts)
│   │  │  Goal: prove D|S(I) has no solution using integer structure
│   │  │  directly, without decomposing into prime-by-prime pieces.
│   │  │  Status: reformulates the conjecture but doesn't solve it.
│   │  │
│   │  ├─ 5a. Carry Weight Identity                                     ✅ PROVED
│   │  │  W_c(I) = Σ_{m=0}^{k-1} s₁(3^m) - s₁(n₀D)
│   │  │  Exact algebraic constraint. W_c = Θ(p²). No abc needed.
│   │  │  2-adic cascade: n₀ determined bit-by-bit by carries.
│   │  │
│   │  ├─ 5b. Parity feedback (self-consistency)                        ✘ = CONJECTURE
│   │  │  ├─ Pattern I determines n₀ = S(I)/D
│   │  │  ├─ n₀'s trajectory determines parities → pattern I'
│   │  │  ├─ Self-consistency: I' = I (fixed-point condition)
│   │  │  ├─ Parity tower = cycle equation algebraically                ✘ NO new info
│   │  │  ├─ "Overdetermination" (1.106 ratio) is ILLUSORY              ✘
│   │  │  ├─ Random-map heuristic: expected cycles ≈ 2^{-0.05p}        ~ conditional
│   │  │  └─ Making decorrelation rigorous IS the conjecture            ✘
│   │  │
│   │  ├─ 5c. 2-adic structure                                          ~ PARTIAL
│   │  │  ├─ Contraction-Expansion Duality:                              ✅ insight
│   │  │  │  Real metric: T^p contracts (3^k/2^p < 1)
│   │  │  │  2-adic metric: T^p expands (factor 2^p)
│   │  │  │  Parity is 2-adic → self-consistency exponentially fragile
│   │  │  ├─ 2-adic expansion rate: ~1.0002/step (barely supercritical) ✅
│   │  │  └─ This is the 5% margin: the system is at edge of criticality ✅
│   │  │
│   │  └─ 5d. WHY CARRY ANALYSIS DOESN'T ESCAPE THE WALL:
│   │     The carry analysis works with S(I) as an integer (good:
│   │     no prime decomposition). But the parity feedback condition
│   │     I' = I is equivalent to D|S(I) (they're the same equation).
│   │     Every reformulation of "integer S divisible by integer D"
│   │     either decomposes into primes (→ abc) or stays global
│   │     (→ equivalent to the conjecture itself).
│   │
│   ├─ 6. SUB-PROBLEM D: NATIVELY GLOBAL METHODS                        ❓ UNEXPLORED
│   │  │  All methods in A-C decompose D|S(I) into local pieces
│   │  │  (mod primes, bit-by-bit). The reassembly always fails because
│   │  │  tools at scale p^{O(1)} cannot reach moduli at scale 2^p.
│   │  │  A solution requires methods that talk about D|S(I) as a
│   │  │  single integer/polynomial equation without breaking it apart.
│   │  │
│   │  ├─ 6a. Function-field lift (Mason-Stothers)                      ✘ EXPLORED, FAILS
│   │  │  abc is proved for polynomials, but the polynomial division
│   │  │  is TRIVIAL: deg_x(S) < deg_x(D), so quotient Q = 0, R = S_I.
│   │  │  Mason-Stothers constrains polynomial relations, not integer
│   │  │  divisibility at (2,3). Resultants, Wronskians also fail.
│   │  │  Full analysis: agent_function_field.md
│   │  │
│   │  ├─ 6a'. Mihailescu-style cyclotomic methods                      ✘ EXPLORED, FAILS
│   │  │  D = 2^p - 3^k = ∏(2 - ζ^m · 3^{k/p}) in Q(ζ_p, 3^{1/p}).
│   │  │  Mihailescu's proof requires D = 1 (Catalan): cyclotomic factors
│   │  │  are UNITS → rigidly constrained by Stickelberger/Thaine/Wieferich.
│   │  │  For D >> 1 (Collatz): factors generate non-principal ideals,
│   │  │  behavior absorbed by CLASS GROUP. Controlling the class group
│   │  │  IS the abc conjecture in algebraic-number-theoretic language.
│   │  │  Stickelberger doesn't apply (K/Q non-abelian). No Wieferich
│   │  │  condition derivable. Norm constraints vacuous over Q.
│   │  │  Full analysis: agent_mihailescu.md
│   │  │
│   │  ├─ 6a''. Corvaja-Zannier / Subspace Theorem                     ~ FINITENESS ONLY
│   │  │  Since x^p - 3^k is irreducible over Q, Corvaja-Zannier (2004)
│   │  │  gives FINITENESS of {x ∈ Z : (x^p - 3^k) | S_I(x)}.
│   │  │  This is the right theorem but INEFFECTIVE: cannot exclude x=2.
│   │  │  An effective version would solve the problem.
│   │  │
│   │  ├─ 6b. 2-adic fixed-point theory                                 ✘ PREDICTED FAIL
│   │  │  T^p is piecewise-linear on Z₂: 2^p branches, one per pattern.
│   │  │  Each branch is affine: n → (3^k/2^p)n + C_I/2^p.
│   │  │  Fixed point of branch I is n₀ = C_I/(2^p-3^k) = S(I)/D.
│   │  │  So the fixed-point equation IS the cycle equation.
│   │  │  Strassmann bounds zeros of analytic functions, but T^p is
│   │  │  not analytic (piecewise). Tools repackage, don't escape.
│   │  │  REASON: reduces to "S(I)/D ∉ Z_{>0}", same size-counting wall.
│   │  │
│   │  ├─ 6c. Polynomial method (Croot-Lev-Pach / capset style)        ✘ PREDICTED FAIL
│   │  │  Encoding D|S(I) over a finite field F_q loses the SIZE info
│   │  │  (D ≈ 2^p is exponentially large, invisible to fixed F_q).
│   │  │  The 5% margin lives in the size comparison C(p,k) < D,
│   │  │  which polynomial methods over fixed finite fields can't see.
│   │  │  Degree k ≈ 0.63p is growing, not fixed.
│   │  │  REASON: needs size of D vs S, which is lost over finite fields.
│   │  │
│   │  ├─ 6d. Transcendence / Subspace Theorem (Schmidt-Schlickewei)    ✘ PREDICTED FAIL
│   │  │  Corvaja-Zannier gives FINITENESS (confirmed in 6a'').
│   │  │  Making it effective requires bounding HEIGHT of solutions,
│   │  │  which for S-units with S = {2,3} reduces to Baker-type bounds
│   │  │  on linear forms in logarithms → same exp(c√p) as Stewart.
│   │  │  REASON: effective height bounds = Baker = abc barrier.
│   │  │
│   │  ├─ 6e. Thermodynamic formalism / transfer operators              ✘ PREDICTED FAIL
│   │  │  Pressure P(β) = lim (1/p) log Σ|S(I)/D|^{-β}.
│   │  │  P(0) ≈ 0.95 (entropy), P(1) ≈ -0.05 (subcritical).
│   │  │  Phase transition EXISTS at β* < 1. But making P(1) < 0
│   │  │  rigorous requires Σ|S(I)/D|^{-1} → 0, which IS the
│   │  │  expected-count-goes-to-zero problem = the original conjecture.
│   │  │  REASON: rigorous pressure = rigorous expected count = abc.
│   │  │
│   │  ├─ 6f. WHY ALL THESE FAIL (the meta-theorem):                    ⚠ KEY INSIGHT
│   │  │  Any method that treats S(I) and D as "generic" integers of
│   │  │  their respective sizes will need to prove 2^{0.95p} random
│   │  │  trials don't hit a target of size 2^p. That's trivially true
│   │  │  (probability 2^{-0.05p}) but making it rigorous for the
│   │  │  SPECIFIC S(I) and D requires controlling their arithmetic
│   │  │  interaction — which is abc. Every framework encounters this
│   │  │  because they all ultimately do size-counting.
│   │  │
│   │  └─ 6g. STRUCTURE-EXPLOITING METHODS                              ❓ ★ TRUE FRONTIER
│   │     │
│   │     THE REQUIRED TECHNIQUE: prove non-divisibility of structured
│   │     sums by structured divisors at exponential scale.
│   │     │
│   │     Formally: show that Σ b^{k-j} a^{i_j} ≢ 0 mod (a^p - b^k)
│   │     for all ordered subsets I ⊂ {0,...,p-1} with |I| = k,
│   │     using the STRUCTURE of the sum, not the factorization of D.
│   │     │
│   │     STRUCTURAL PROPERTIES TO EXPLOIT:
│   │     ├─ All terms positive, {a,b}-smooth (no cancellation)
│   │     ├─ Geometric coefficients: weights b^{k-1},...,b,1
│   │     ├─ Elementary symmetric function (charsum reversal trick)
│   │     ├─ Ordered subset constraint on positions
│   │     ├─ Divisor D = a^p - b^k has matching {a,b}-smooth structure
│   │     └─ Dynamical origin: S/D is an orbit starting value
│   │     │
│   │     WHY NOTHING EXISTING WORKS:
│   │     ├─ Baker: archimedean bound, not D-adic. Gap: √p vs p.
│   │     ├─ Subspace Theorem: finiteness but ineffective
│   │     ├─ Charsum/Weil: already fully exploited → Theorem 4
│   │     ├─ Carry analysis: equivalent to cycle equation
│   │     └─ Every structural property either already used or = conjecture
│   │     │
│   │     WHAT IT WOULD LOOK LIKE:
│   │     An effective quantitative lower bound on |S(I)|_D (the D-adic
│   │     valuation) that uses the geometric structure of the sum to
│   │     bypass prime-by-prime decomposition of D. Equivalently: a
│   │     proof that structured {a,b}-smooth sums with geometric weights
│   │     cannot be divisible by a^p - b^k at exponential scale.
│   │     │
│   │     This is a new type of result: effective S-unit non-divisibility.
│   │     It would live at the intersection of Diophantine approximation,
│   │     additive combinatorics, and algebraic number theory.
│   │     │
│   │     CLOSEST ANALOGUES:
│   │     ├─ Mihailescu (Catalan): proves a^p - b^k ≠ 1, but needs D = 1
│   │     ├─ Baker: bounds |Σ β_i log α_i|, continuous not discrete
│   │     └─ Corvaja-Zannier: finiteness of integer points, ineffective
│   │     │
│   │     No known framework. Likely requires genuinely new mathematics.
│   │     Full task specification: TASK_6g_structured_non_divisibility.md
│   │
│   ├─ 7. FAILED APPROACHES (comprehensive list)
│   │  ├─ Equidistribution mod D directly                               ✘ blocks > p
│   │  ├─ Sieve + rad(D) unconditionally                                ✘ abc barrier
│   │  ├─ Tao's 3-adic technique                                        ✘ wrong modulus, avg-case
│   │  ├─ Circle method (Hardy-Littlewood)                               ✘ IS Fourier mod D
│   │  ├─ Modular Feedback Theorem                                       ✘ based on wrong formula
│   │  ├─ Second moment / Parseval                                       ✘ C < D regime
│   │  ├─ Furstenberg ×2,×3 measure rigidity                            ✘ invariance error O(1)
│   │  ├─ Transfer matrix spectral analysis                              ✘ eigenvalues = 1
│   │  ├─ Weyl differencing                                              ✘ same sum bounds
│   │  ├─ Algebraic structure 2^p ≡ 3^k mod D                           ✘ tautological
│   │  ├─ All 6 direct algebraic approaches                              ✘ insufficient
│   │  ├─ Spectral gap alone for no-cycles                               ✘ needs |λ₂| < 0.483
│   │  ├─ Orbit-averaged sin² (for universal gap)                        ✘ FALSE (C/log p)
│   │  ├─ sin²-weight Lyapunov                                           ✘ op norm grows O(p)
│   │  ├─ ||M²||_op uniform bound                                        ✘ grows → 1
│   │  ├─ Parity tower as independent constraint                         ✘ = cycle equation
│   │  └─ Prime-power sieve for squarefree D                             ✘ zero advantage
│   │
│   ├─ 8. WHY THE PROBLEM IS HARD
│   │  ├─ The 5% margin: C(p,k)/D ≈ 2^{-0.05p}. Barely subcritical.
│   │  ├─ 2-adic expansion rate ~1.0002/step. Barely supercritical.
│   │  ├─ D = 2^p - 3^k is squarefree ~93% of the time.
│   │  ├─ Local-to-global methods (A,B) need scale 2^p, tools reach p^{O(1)}.
│   │  ├─ Global methods (C) are equivalent to D|S(I) — the conjecture itself.
│   │  ├─ Natively global methods (D) are unexplored — the best hope.
│   │  ├─ The problem sits at the intersection of:
│   │  │  ├─ Additive combinatorics (short sums of smooth numbers)
│   │  │  ├─ Multiplicative number theory (radical of 2^p - 3^k)
│   │  │  └─ The abc conjecture (the controlling barrier for local methods)
│   │  └─ GENERAL FORMULATION (Collatz-free):
│   │     Can a SHORT sum of {2,3}-smooth numbers vanish mod 2^p - 3^k?
│   │     This is the irreducible core at the boundary of all three areas.
│   │
│   └─ 9. NUMERICAL DATA
│      ├─ |λ₂| ∈ [0.66, 0.81] for 240+ primes (p=5 to p=1499)         ✅
│      ├─ ρ(K) ≤ 0.81 for all 240+ subgroup sizes K tested             ✅
│      ├─ gap × p GROWS with p → gap is NOT 1/p                        ✅
│      ├─ D squarefree 53/57 tested values                              ✅
│      ├─ log₂(rad(D))/p ≥ 0.82 for all p ≥ 9 tested                  ✅
│      ├─ Strongest predictor of |λ₂|: index of ⟨2,3⟩ (r = -0.36)     ✅
│      └─ "+1 advantage" over multiplicative walk: ratio > 16000×       ✅
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
- Bourgain-Glibichuk-Konyagin, "Estimates for sums and products in fields of prime order" (J. London Math. Soc., 2006)
- Iwaniec-Kowalski, "Analytic Number Theory" (AMS, 2004) — Gauss sums mod prime powers
- Tao, "Almost all orbits of the Collatz map attain almost bounded values" (Forum of Math Pi, 2022)
- Shmerkin, "On Furstenberg's intersection conjecture" (Annals, 2019)
- Stewart, "On divisors of Lucas and Lehmer numbers" (Acta Math, 2013)
- Eliahou, "The 3x+1 problem: new lower bounds on nontrivial cycle lengths" (Discrete Math, 1993)

## Session History

- **Session 1** (2026-03-05): Rounds 1-10. Formulation, equidistribution, sieve, spectral gap, Combined Theorem.
- **Session 2** (2026-03-05/06): Rounds 10-14. Theorems 15-17, carry analysis, prime-power sieve, quotient-graph. 20+ agent analyses. All tractable approaches exhausted.

## File Index

| File | Contents |
|---|---|
| `theorems_and_proofs.md` | All 17 theorems with proofs |
| `theorem16_extended.md` | Theorem 17 (BGK extension) full proof |
| `theorem_prime_power_sieve.md` | Prime-power equidistribution + Hensel |
| `prime_power_lift_obstruction.md` | Why prime-power lift doesn't bypass abc |
| `agent_sum_product.md` | Theorem 16 original proof |
| `agent_bourgain_gamburd.md` | B-G framework analysis |
| `agent_coupling_entropy.md` | Coupling / entropy approaches |
| `agent_universal_gap.md` | CDG product approach |
| `agent_universal_gap_v2.md` | Phase transition analysis |
| `agent_quotient_graph.md` | Quotient-graph decomposition |
| `agent_compactness_gap.md` | ρ(K) computation |
| `agent_carry_analysis.md` | Carry weight identity |
| `agent_parity_feedback.md` | Parity self-consistency |
| `agent_carry_parity_v2.md` | Carry × parity interaction |
| `agent_overdetermined.md` | Overdetermined system (illusory) |
| `agent_radical_D.md` | Radical of D research |
| `referee_theorem16.md` | Theorem 16 verification report |
| `collatz_spectral.py` | Spectral gap computation |
| `collatz_m2_norm.py` | M² operator norm computation |
| `paper_spectral_gap.md` | Draft paper (needs updating) |
| `session_log.md` | Verbatim conversation log |
