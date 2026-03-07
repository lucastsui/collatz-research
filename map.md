# Collatz Conjecture — Problem Decomposition Map

*Last updated: 2026-03-06 (Session 8)*

**Legend:** ✅ proved/done · ✘ failed/dead end · ❌ blocked/open · ⚠ error found · ~ partial · ❓ unexplored · ★ recommended

---

```
Collatz Conjecture
│
├── Part 0: INVENT THE MISSING MATHEMATICAL FRAMEWORK           ★ TRUE GOAL
│   │
│   │  THE PROJECT'S CORE FINDING: 14+ rounds of systematic exploration
│   │  confirm that NO existing mathematical framework can prove Part 1.
│   │  Every known tool either decomposes D into primes (→ abc barrier)
│   │  or works at full modulus D (→ equivalent to the conjecture).
│   │  The gap between polynomial-scale tools and exponential-scale targets
│   │  is structural, not technical. New mathematics is required.
│   │
│   │  THE MISSING TOOL MUST BE:
│   │  (1) GLOBAL at scale D: talk about divisibility by D = 2^p - 3^k
│   │      as a single event, not a conjunction of events mod prime factors.
│   │  (2) STRUCTURE-AWARE: exploit that S(I) = Σ 3^{k-j}·2^{i_j} is a
│   │      structured sum (geometric weights, ordered positions, {a,b}-smooth),
│   │      not a generic integer of its size.
│   │  (3) NON-ABELIAN: capture correlations between {q | S(I)} events
│   │      across primes q | D, or bypass prime decomposition entirely.
│   │      The CRT/sieve is abelian and assumes independence — this fails.
│   │
│   │  HISTORICAL PARALLELS:
│   │  ├─ FLT (regular primes) → Kummer invented ideal theory (1850s)
│   │  ├─ Weil conjectures → Grothendieck invented étale cohomology (1960s)
│   │  ├─ FLT (full) → Wiles invented modularity lifting (1995)
│   │  └─ Mordell conjecture → Faltings invented height machinery (1983)
│   │  In each case: existing tools hit a hard barrier, new framework
│   │  was required that could "see" structure invisible to prior methods.
│   │
│   │  THE TWO BARRIERS (why every attempt fails):
│   │  ┌─────────────────────────────────────────────────────────────┐
│   │  │ Barrier 1: SIZE-COUNTING (= abc)                          │
│   │  │ Blocks: methods that bound #{I : D|S} by comparing        │
│   │  │ C(p,k) to D. Includes sieve, character sums, lattice      │
│   │  │ counting, probabilistic arguments.                         │
│   │  │ Diagnosis: needs rad(D) > 2^{0.95p}, which is abc.        │
│   │  ├─────────────────────────────────────────────────────────────┤
│   │  │ Barrier 2: REFORMULATION (= equivalence)                   │
│   │  │ Blocks: methods that restate D|S(I) without reducing it.   │
│   │  │ Includes lattice certificate, defect identity, carry       │
│   │  │ analysis, parity tower, all of 6g-ii.                      │
│   │  │ Diagnosis: every reformulation collapses to the cycle      │
│   │  │ equation under normalization. No reduction achieved.       │
│   │  ├─────────────────────────────────────────────────────────────┤
│   │  │ A WORKING METHOD MUST AVOID BOTH:                          │
│   │  │ (a) Not size-counting — prove D ∤ S(I) structurally,      │
│   │  │     not by bounding solution counts against modulus size.  │
│   │  │ (b) Non-trivially reducing — derive a condition strictly   │
│   │  │     WEAKER than the cycle equation, yet still impossible.  │
│   │  └─────────────────────────────────────────────────────────────┘
│   │
│   │  DIRECTIONS FOR INVENTION (all explored, all fail):
│   │
│   ├─ 0A. Non-abelian sieve methods                                  ✘ EXPLORED, CIRCULAR
│   │  │  IDEA: exploit anti-correlation between {q₁|S(I)} and {q₂|S(I)}
│   │  │  for prime factors q₁,q₂ of D. Geometric coefficients create
│   │  │  rank-dependent coupling → different "phase patterns" per prime
│   │  │  → interference → anti-correlation.
│   │  │
│   │  │  COMPUTATION (norm_constraint.py, anticorrelation_deep.py):
│   │  │  Anti-correlation confirmed for all tested composite D.
│   │  │  (10,6): D=5×59, P(5)·P(59)=0.014, P(D)=0. Ratio=0.
│   │  │  (16,10): D=13×499, P(13)·P(499)=0.0006, P(D)=0. Ratio=0.
│   │  │  Individual primes show EXCESS divisibility, joint is 0.
│   │  │
│   │  │  STRUCTURAL RESULT: S(I) is never divisible by b = 3
│   │  │  (last term is 2^{i_k}, coprime to 3). First structural
│   │  │  non-divisibility not requiring abc. But b ∤ D anyway.
│   │  │
│   │  │  WHY IT FAILS: need pairwise ε > 0.45 in composite Weil bound.
│   │  │  Far beyond any known result. And the anti-correlation itself
│   │  │  may be EQUIVALENT to the conjecture (not independent of it).
│   │  │  Proving anti-correlation from structure = proving no cycles.
│   │  │  File: agent_nonabelian_sieve.md
│   │
│   ├─ 0B. Arithmetic intersection theory on R = Z[x]/(x^p - b^k)     ✘ EXPLORED, FAILS
│   │  │  The cycle equation is: does the lattice point c_I lie in
│   │  │  the sublattice (x-a)R of covolume D? (from 6g-ii)
│   │  │
│   │  │  ANALYSIS (Session 6, arakelov_0B.md):
│   │  │  ├─ R = Z[x]/(x^p - 3^k), order in Q(3^{k/p}), rank p         ✅ set up
│   │  │  ├─ p embeddings sigma_m: alpha -> zeta^m * 3^{k/p}             ✅ computed
│   │  │  ├─ Near-degenerate: |sigma_0(x-2)| ~ D/(p*2^{p-1})            ✅ verified
│   │  │  ├─ Product of |sigma_m(x-2)| for m!=0 ~ p*2^{p-1}             ✅ verified
│   │  │  ├─ Norm lower bound: |N(f)| >= D for f in (x-2)R              ✅ proved
│   │  │  │  But h_inf(f) >= log(D)/p ~ 0.035 (constant!), too weak
│   │  │  ├─ Successive minima: lambda_1 = O(1), F_I ~ 2^{0.63p}        ✅ computed
│   │  │  │  Lattice contains short vectors; no size contradiction
│   │  │  ├─ q-adic filtration (q above 3): v_q(x-2) = 0                ✅ proved
│   │  │  │  3-adic structure gives no constraint on (x-2)R
│   │  │  ├─ Arithmetic Bezout: too weak by factor p                     ✅ computed
│   │  │  └─ Coefficient entropy: (x-2)*x^m has O(1) entropy             ✅ disproved
│   │  │
│   │  │  WHY IT FAILS:
│   │  │  Membership in (x-2)R is a LINEAR (lattice) condition.
│   │  │  Heights measure SIZE, not residue class. The lattice (x-2)R
│   │  │  contains elements of ALL sizes and shapes. No height-based
│   │  │  method can distinguish "structured sparse" from "generic"
│   │  │  elements within a single residue class of R/(x-2)R ~ Z/DZ.
│   │  │
│   │  │  NOTE: This used the SINGLE-variable ring R = Z[x]/(x^p - 3^k).
│   │  │  The later Fermat curve framework (Session 8 late) uses the
│   │  │  TWO-variable ring A = Z[s,t]/(t^p - s^k), which has a DUAL
│   │  │  degree bound and richer geometric structure. The failure of 0B
│   │  │  does not preclude the Fermat curve approach.
│   │  │  File: arakelov_0B.md, arakelov_verify.py
│   │
│   ├─ 0D. TRANSVERSAL ZERO-SUM BARRIER                               ★ NEW FRAMEWORK
│   │  │
│   │  │  KEY DISCOVERY (Session 3): The Collatz no-cycles conjecture
│   │  │  is equivalent to a RESTRICTED ZERO-SUM TRANSVERSAL problem:
│   │  │
│   │  │  S(I) = Σ 3^{k-j} · 2^{i_j} is a weighted sum from k "slices"
│   │  │  A_j = {3^{k-1-j} · 2^r mod D : r = 0,...,p-1} in Z/DZ.
│   │  │  The unrestricted sumset A_0 + ... + A_{k-1} is ALWAYS all of
│   │  │  Z/DZ. But the restricted sumset (distinct positions, monotone
│   │  │  weight assignment) NEVER contains 0. Verified for all p ≤ 21.
│   │  │
│   │  │  EMPIRICAL FINDINGS:
│   │  │  ├─ U = Z/DZ for all tested (p,k)                              ✅
│   │  │  │  (Proved via Cauchy-Davenport for prime D.)
│   │  │  ├─ 0 ∉ R for all tested (p,k) up to p=21                     ✅ empirical
│   │  │  ├─ For (5,3) and (8,5): 0 is the ONLY excluded residue       ✅
│   │  │  ├─ Zero-sum with distinct positions requires ≥1 inversion     ✅
│   │  │  │  from the anti-sorted Collatz convention
│   │  │  └─ The organized 3-divisibility of the certificate is the     ✅ structural
│   │  │     algebraic mechanism enforcing the transversal constraint
│   │  │
│   │  │  WHY THIS AVOIDS THE BARRIERS:
│   │  │  ├─ Not size-counting: "0 ∉ R" is set-membership, not a
│   │  │  │  count against D. No abc/rad(D) needed.
│   │  │  ├─ Structure-aware: exploits the DISTINCT-POSITION constraint
│   │  │  │  (= orbit visits each timestep once) and MONOTONE WEIGHT
│   │  │  │  assignment (= geometric 3-coefficients decrease with rank).
│   │  │  └─ Connects to new tools: additive combinatorics, transversal
│   │  │     theory, zero-sum Ramsey theory, Cauchy-Davenport.
│   │  │
│   │  │  PROOF PROGRAM:
│   │  │  1. Prove U = Z/DZ for all (p,k).                              ~ mostly done
│   │  │     Done for prime D (Cauchy-Davenport). For composite D:
│   │  │     CRT + C-D per factor covers all tested except (13,8)/q=233.
│   │  │     Empirically verified U = Z/DZ for ALL (p,k), p ≤ 25.
│   │  │  2. Prove 0 ∉ R.                                               ❌ = CONJECTURE
│   │  │     CASCADE REDUCTION (C7): 0 ∉ R ⟺ no Syracuse periodic
│   │  │     points. Proved for k ≤ 30 (C9). For general k: reduces to
│   │  │     Collatz conjecture for n ≤ (3/2)^{k-1}.
│   │  │  3. Status: cascade fully characterizes the problem but        ⚠
│   │  │     does not escape the equivalence barrier. The cascade IS
│   │  │     the Collatz iteration (C7), so proving it fails = proving
│   │  │     the Collatz conjecture. No independent reduction found.
│   │  │
│   │  │  RECURSIVE DESCENT (computational theorem):
│   │  │  For all (p,k) up to p=18: peeling off the first term and
│   │  │  checking if any valid i_1 exists gives ZERO dangerous cases.
│   │  │  The archimedean bound explains why: 2^{i_1} ≤ 3nΔ forces
│   │  │  i_1 to be tiny, but ordering constraint i_1 < min(I')
│   │  │  eliminates it. For n=1: i_1 < 0 always (proved).
│   │  │
│   │  │  ARCHIMEDEAN CASCADE (new theorem):
│   │  │  If D|S(I), positions must be tightly packed:
│   │  │  i_j ≈ j*log_2(3) + O(j). Starting value n ≥ 1/(3Δ) ≈ p^10.
│   │  │  Recovers Steiner bound from pure sumset reasoning.
│   │  │  File: theorem_archimedean_descent.md
│   │  │
│   │  │  2-ADIC CASCADE (Sessions 4-5, theorems C1-C10):        ★ KEY RESULTS
│   │  │  ├─ C1: WLOG i_1 = 0 (D odd, factor out 2^{i_1})        ✅ proved
│   │  │  ├─ C2: n must be odd and coprime to 3                    ✅ proved
│   │  │  ├─ C3: Positions uniquely determined by n via v_2        ✅ proved
│   │  │  ├─ C4: n=1 → trivial cycle (p=2k) or no solution        ✅ proved
│   │  │  ├─ C5: k ≤ 4: no nontrivial cycles for ANY p            ✅ proved
│   │  │  ├─ C6: All p ≤ 60 (83 pairs, 3.3M candidates): 0 found ✅ computed
│   │  │  ├─ C7: SYRACUSE-CASCADE DUALITY                         ✅ proved
│   │  │  │  c_j = (3·S^j(n)+1)·3^{k-1-j} where S = Syracuse map
│   │  │  │  Cascade succeeds iff n is period-k point of S
│   │  │  ├─ C8: Fixed-k bound: n_max → (3/2)^{k-1} - 1          ✅ proved
│   │  │  ├─ C9: k ≤ 30: no nontrivial cycles for ANY p           ✅ proved
│   │  │  │  (all odd n ≤ 127834 verified to reach 1)
│   │  │  ├─ C10: Post-orbit obstruction: odd n≥3 ⟹ n∤4          ✅ proved
│   │  │  └─ Min distance to 0: stays at 1 (exclusion tight)      ✅ empirical
│   │  │  File: theorem_cascade.md, cascade_syracuse.py,
│   │  │         cascade_extended_v2.py, cascade_nearcritical.py
│   │  │
│   │  │  CONFIRMED RISK: The Syracuse-Cascade Duality (C7) proves
│   │  │  that 0 ∉ R IS exactly the Collatz conjecture (not just
│   │  │  equivalent: the cascade literally IS the Syracuse iteration).
│   │  │  However, the cascade provides: (a) efficient computation,
│   │  │  (b) clean proofs for fixed k (C9: k≤30), (c) the post-orbit
│   │  │  obstruction "n∤4" (C10), and (d) the reduction to Collatz
│   │  │  verification for bounded n values (C8+C10). These are genuine
│   │  │  structural insights even if they don't escape the barrier.
│   │  │
│   │  │  Files: framework_transversal_zero_sum.md,
│   │  │         distinct_position_barrier.py,
│   │  │         monotone_weight_barrier.py,
│   │  │         residue_zero_special.py
│   │  │
│   └─ 0C. Motivic / categorical structure on {a,b}-smooth sums       ✘ EXPLORED, FAILS
│      │  ANALYSIS (Session 7, motivic_0C.md):
│      │  Systematically explored 10 frameworks:
│      │  ├─ Toric geometry (BKK mixed volume): bounds common zeros,     ✘
│      │  │  not integer evaluation. (2,3) not on curve G=0.
│      │  ├─ Log geometry ({2,3}-smooth monoid): captures multiplicative ✘
│      │  │  structure, but Collatz ADDS smooth numbers (breaks log).
│      │  ├─ Zeta function: no varying parameter, no functional eq.      ✘
│      │  ├─ Tropical geometry: captures v_2, v_3 but loses D-adic info  ✘
│      │  ├─ F_1-geometry (lambda-rings): "+1" breaks Frobenius lifts    ✘
│      │  ├─ Configuration space cohomology: discrete, trivial H^i       ✘
│      │  ├─ Derived categories: ideal membership is LINEAR              ✘
│      │  ├─ Galois representations: encode field, not element divisib.  ✘
│      │  ├─ Determinant method: requires polynomial, not exponential    ✘
│      │  └─ Pila-Wilkie (o-minimal): too weak for growing dimension     ✘
│      │
│      │  WHY IT FAILS (the deepest diagnosis):
│      │  The Collatz condition D|S(I) lives at the INTERSECTION of
│      │  the exponential world (2^{i_j}, 3^{k-j}) and the algebraic
│      │  world (divisibility by D = 2^p - 3^k). ALL existing
│      │  cohomological/motivic methods handle polynomial/algebraic
│      │  objects. The exponential function 2^x is NOT algebraic.
│      │  There is no algebraic variety whose integer points are the
│      │  Collatz cycles. Without a variety: no cohomology, no
│      │  Frobenius, no trace formula, no functional equation.
│      │  Building such a framework = multi-decade program comparable
│      │  to inventing etale cohomology.
│      │  File: motivic_0C.md, motivic_verify.py
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
│   │  │  ├─ log₂(rad)/p ≥ 0.82 for all p ≥ 9 tested                  ✅ empirical
│   │  │  │
│   │  │  └─ PATH 1: Improve Baker for (log 2, log 3)                   ❓ OPEN RESEARCH PROGRAM
│   │  │     Baker's method bounds |β₁ log 2 + β₂ log 3| > exp(-C√p log p).
│   │  │     Converting to rad(D) lower bound loses a square root.
│   │  │     TARGET: improve exp(c√p/log p) → exp(cp) for rad(2^p - 3^k).
│   │  │     This is a specific problem in transcendence theory — does NOT
│   │  │     require proving full abc, only abc for the family 2^p = 3^k + D.
│   │  │     Open since Baker (1960s). Progress incremental (Laurent,
│   │  │     Mignotte, Nesterenko, Matveev, Yu). The gap (√p vs p) is
│   │  │     enormous but the problem is well-defined and has a community.
│   │  │     DIFFICULTY: decades-open. Would be a major result in
│   │  │     Diophantine approximation independent of Collatz.
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
│   │     THE FUNCTION FIELD KEY (Session 8):                     ★ DEEPEST INSIGHT
│   │     Over F_q[t], the cycle equation is TRIVIALLY unsolvable:
│   │     deg(S) = i_k ≤ p-1 < p = deg(D), and S ≠ 0. One line.
│   │     This works because: (1) the degree is ultrametric,
│   │     (2) coefficients (= constants in F_q) have degree 0, and
│   │     (3) divisibility respects degree.
│   │     Over Z, the proof breaks at OSTROWSKI'S THEOREM: no
│   │     non-archimedean absolute value on Q has |2| > 1 (needed
│   │     for the degree gap) because |2| = |1+1| ≤ max(|1|,|1|) = 1.
│   │     The GAP-CONSTRAINT DICHOTOMY: "top" (highest 2-power)
│   │     gives the gap but not the divisibility constraint; "bottom"
│   │     (v_2) gives the constraint but not the gap. Function field
│   │     degree gives BOTH. No single measure on Q gives both.
│   │     THIS UNIFIES ALL THREE BARRIERS: they are all consequences
│   │     of Q having exactly one archimedean place (not ultrametric).
│   │     A proof requires: a "smooth degree" on Z with |2|>1, |3|=1,
│   │     ultrametric — bypassing Ostrowski via ring extension, F_1-
│   │     geometry, or a fundamentally different proof structure.
│   │     File: function_field_collatz.md
│   │     │
│   │     FERMAT CURVE HEIGHT FRAMEWORK (Session 8, late):       ★ NEW DIRECTION
│   │     The cycle equation D|S(I) is equivalent to IDEAL MEMBERSHIP:
│   │     R_I in (s-3, t-2) inside A/DA, where A = Z[s,t]/(t^p - s^k)
│   │     is the coordinate ring of the Fermat curve C: t^p = s^k.
│   │     R_I(s,t) = sum s^{k-j} t^{i_j} is the two-variable lift.
│   │     KEY: R_I has DUAL DEGREE BOUND: deg_s < k AND deg_t < p,
│   │     strictly less than D in BOTH variables. Over Q, this makes
│   │     ideal membership impossible (= function field proof).
│   │     Over Z/DZ, the question is open.
│   │     R_I has STAIRCASE structure: k nonzero 0-1 entries at
│   │     positions (k-j, i_j) forming a monotone anti-diagonal.
│   │     THE TWO-CONSTRAINT INSIGHT: The function field proof uses
│   │     only Constraint 1 (degree). The integer proof may need BOTH
│   │     Constraint 1 (bidegree on C) AND Constraint 2 (D|S(I)).
│   │     The function field proof is an "incomplete shadow" —
│   │     a degenerate case where one constraint suffices.
│   │     PROPOSED: Collatz = HEIGHT INEQUALITY on Fermat curve C,
│   │     for staircase functions evaluated at (3,2) mod D.
│   │     Connects to: Arakelov theory, Vojta's conjecture, Frey curves.
│   │     Specific case may be weaker than full abc/Vojta.
│   │     File: fermat_curve_height.md
│   │     │
│   │     SELF-REFERENTIALITY HUNCH (Session 8):               ★ FUTURE THREAD
│   │     β = 2/3 mod D, D = 2^p - 3^k, perturbations are 2^{e_j}.
│   │     All three (the ratio, the modulus, the perturbations) are
│   │     built from the SAME two primes (2 and 3). They are not
│   │     independent objects. The geometric sum Σ β^j wraps around
│   │     Z/DZ, but the wrapping is constrained by β^k = 2^{k-p} mod D
│   │     — which ties the sum length k to the modulus D.
│   │     A "generic" sum over a "generic" modulus would hit 0 at rate
│   │     1/D. But this sum over THIS modulus might be algebraically
│   │     prevented from hitting 0, precisely because they share the
│   │     same DNA (2 and 3). Unexploited. May be the real proof path.
│   │     │
│   │     No known framework. Likely requires genuinely new mathematics.
│   │     Full task specification: TASK_6g_structured_non_divisibility.md
│   │     │
│   │     ATTEMPTS:
│   │     │
│   │     ├─ 6g-i. GPT-OSS-120B: Zsigmondy + S-unit equations             ✘ SAME WALL
│   │     │  Zsigmondy gives a primitive prime q | D not dividing any term
│   │     │  of S(I). Reduces to S-unit equation with k+2 terms over S={2,3}.
│   │     │  Evertse-Schlickewei gives FINITENESS, but the bound on
│   │     │  exponents depends on k (= number of terms), which grows with p.
│   │     │  So finiteness only holds for fixed k, not k ~ 0.63p → ∞.
│   │     │  This is the sieve rediscovered with a different entry point.
│   │     │  File: gpt_oss_response_6g.md
│   │     │
│   │     └─ 6g-ii. Codex: Global lattice reformulation                    ✘ EQUIVALENT TO CONJECTURE
│   │        D | S(I) iff coefficient vector c_I ∈ M·Z^p, where M is a
│   │        companion-type matrix with det = ±D. Equivalently:
│   │        [F_I(x)] ∈ (x-a)R in the order R = Z[x]/(x^p - b^k).
│   │        │
│   │        Gives a rigid certificate sequence q with:
│   │        (a) strict negativity: q_r < 0 for all r
│   │        (b) sparse geometric differences: q_{r-1} - a·q_r ∈ {0, b^0,...,b^{k-1}}
│   │        (c) trailing-b divisibility: b^{s_r} | q_r
│   │        After normalization u_r = -q_r / b^{s_{r+1}}, the certificate
│   │        IS the Collatz orbit: u_{r+1} = u_r/2 or (3u_r+1)/2.
│   │        │
│   │        Clean global reformulation native at scale D (no prime
│   │        decomposition), but (a)+(b)+(c) inconsistency = no nontrivial
│   │        cycles = the FULL CONJECTURE (not a weaker sub-problem).
│   │        File: agent_global_lattice.md
│   │        │
│   │        Follow-up (agent_q_defect.md): proved the defect identity
│   │        Δ = Σ_{r∈I} log(1 + 1/(3u_r)), showing the near-critical
│   │        slack is distributed across tiny jumps at odd steps.
│   │        When Δ = O(p^{-9}), all odd orbit values ≫ p^9.
│   │        But this is essentially the classical Collatz orbit bound
│   │        (Steiner, Simons-de Weger) in logarithmic language.
│   │        │
│   │        VERDICT: The lattice reformulation looked like a new angle,
│   │        but the certificate constraints collapse to the full cycle
│   │        equation under normalization. No reduction achieved —
│   │        proving (a)+(b)+(c) inconsistent IS proving Part 1.
│   │     │
│   │     OPEN RESEARCH PROGRAMS (paths that haven't been ruled out):
│   │     │
│   │     ├─ 6g-iii. Quantitative ×2 ×3 rigidity                          ✘ EXPLORED, FAILS
│   │     │  Furstenberg (1967): only ×2-and-×3-invariant measures on R/Z
│   │     │  are Lebesgue and atomic. Rudolph (1990), EKL (2006).
│   │     │  │
│   │     │  STRUCTURAL FAILURE (not technical):
│   │     │  (1) Cycle measure μ = (1/p)Σδ_{u_r/D} is ATOMIC (finitely
│   │     │      supported on rationals) — explicitly ALLOWED by the
│   │     │      Furstenberg-Rudolph classification.
│   │     │  (2) μ is T-invariant (Collatz map), NOT ×2- or ×3-invariant.
│   │     │      Approximate invariance is meaningless: pushforward (×2)_*μ
│   │     │      has support {2u_r/D}, which ≠ {u_r/D}.
│   │     │  (3) The dual action on (Z/DZ)* reduces to the sieve via CRT.
│   │     │  (4) Simultaneous 2-adic + archimedean Diophantine constraints
│   │     │      are compatible for n ~ p^{10} (no contradiction).
│   │     │  (5) Decomposition mod 2^p and mod 3^k gives trivial info
│   │     │      (gcd(D, 2^p) = gcd(D, 3^k) = 1).
│   │     │  │
│   │     │  CONCLUSION: the thematic connection (Collatz uses ×2 and ×3,
│   │     │  log2/log3 irrational) is real but the formal connection to
│   │     │  measure rigidity is broken. Atomic measures on rationals
│   │     │  are the "allowed case" and that's exactly what cycles are.
│   │     │  File: agent_x2x3_rigidity.md
│   │     │
│   │     ├─ 6g-iv. Multi-adic Hasse obstruction                           ❓ SPECULATIVE
│   │     │  Work in Z_2 × Z_3 simultaneously. In Z_2, the Collatz map
│   │     │  is conjugate to a shift on binary sequences — periodic 2-adic
│   │     │  orbits are plentiful and classified. In Z_3, the ×3 steps
│   │     │  are contractions and "+1" additions create different rigidity.
│   │     │  │
│   │     │  NEEDED: show the 2-adic periodic point set and the 3-adic
│   │     │  constraint set have empty intersection in Z_{>0}.
│   │     │  A Hasse-principle-failure argument: cycle exists locally
│   │     │  (in Z_2 and Z_3 separately) but not globally.
│   │     │  DIFFICULTY: high. Hasse failures usually need Brauer-Manin
│   │     │  obstruction or descent, which require algebraic variety
│   │     │  structure. Collatz map doesn't live on a variety.
│   │     │
│   │     └─ 6g-v. Composite-modulus character sums for e_k                ❓ SPECULATIVE
│   │        Estimate Σ_{|I|=k} χ(S(I)) for characters χ mod D WITHOUT
│   │        CRT-decomposing into prime characters. The structure
│   │        F(t) = e_k(γ_0,...,γ_{p-1}) (elementary symmetric polynomial)
│   │        might admit Weil-type bounds at composite modulus that
│   │        don't factor through primes.
│   │        │
│   │        NEEDED: a Weil-type bound for e_k evaluated at roots of
│   │        unity of composite order. Does not exist in the literature.
│   │        Would be a contribution to algebraic combinatorics even
│   │        independent of Collatz.
│   │        DIFFICULTY: the composite-modulus Weil bound is itself a
│   │        hard open problem (cf. Bourgain on exponential sums to
│   │        composite moduli).
│   │     │
│   │     NEW DIRECTIONS (Session 7, not yet explored):
│   │     │
│   │     ├─ 6g-vi. Carry automaton (finite-state self-reference)        ✘ PREDICTED FAIL (Q4)
│   │     │  Barrier diagnostic Q4: carry automaton = cascade = Syracuse (C7).
│   │     │  Reformulation, not reduction. State space 2^k equivalent to
│   │     │  checking all n ≤ (3/2)^{k-1}. Same as Simons-de Weger route.
│   │     │
│   │     ├─ 6g-vii. Cascade increment correlation                       ✘ EXPLORED, FAILS
│   │     │  Independence rate I(log_2(3)) ≈ 0.055, but need > log(3/2) ≈ 0.405.
│   │     │  GAP FACTOR: 7.4×. Independence predicts exp(0.351k) → ∞ cycles.
│   │     │  SURPRISE: correlations are POSITIVE (Corr ≈ +0.02 to +0.04),
│   │     │  making Var[G] > Var_indep. Correlations HURT, not help.
│   │     │  Some candidates have G < p (long g=1 streaks). "G > p always" is FALSE.
│   │     │  The 7.4× gap = quantitative expression of Barrier 1 (abc) in cascade language.
│   │     │  File: cascade_correlation.md, cascade_correlation_verify.py
│   │     │
│   │     ├─ 6g-viii. Prime-D sieve completion + composite-D descent     ✘ EXPLORED, FAILS
│   │     │  CORRECTION: D is prime for only ~6-10% of pairs, NOT ~50%.
│   │     │  PRIME D: Block decomposition PROVABLY fails for p ≥ 5.
│   │     │  Need ord_D(2) ≤ p (for blocks) AND ord_D(2) > 2√D (for Gauss).
│   │     │  These require p > 2√D, i.e., p² > 4D ≈ 4·2^p. IMPOSSIBLE.
│   │     │  Computation: L = 0 blocks for ALL tested prime D (D > 5).
│   │     │  Character sums: C-S gives |ΣF(t)| ≤ D·√C, need < C.
│   │     │  Excess factor: D/√C ≈ 2^{0.525p} → ∞. Exponentially insufficient.
│   │     │  COMPOSITE D: Need handleable fraction > 0.95, but many D have
│   │     │  it < 0.90. Smallest lpf ratio = 0.18. The "large prime factor
│   │     │  conjecture" for 2^p - 3^k reduces to abc-type input.
│   │     │  ROOT CAUSE: Scale gap p vs D ≈ 2^p. Same as abc barrier.
│   │     │  File: prime_d_sieve.md, prime_d_sieve_verify.py
│   │     │
│   │     ├─ 6g-ix. Digital constraint propagation (CSP approach)        ✘ PREDICTED FAIL (Q4)
│   │     │  Barrier diagnostic Q4: CSP encodes cycle equation exactly.
│   │     │  Self-consistency creates long-range interactions preventing
│   │     │  bounded treewidth. Reformulation into CS language, not reduction.
│   │     │
│   │     ├─ 6g-x. Induction on k via orbit compression                 ✘ PREDICTED FAIL (Q4)
│   │     │  Barrier diagnostic Q4: reduces to Collatz for n ≤ (3/2)^{k-1}
│   │     │  via Syracuse-Cascade Duality (C7) and post-orbit obstruction
│   │     │  (C10). Same as Simons-de Weger route. Cannot complete for
│   │     │  general k without proving Collatz for all n.
│   │     │
│   │     └─ 6g-xi. Non-archimedean dynamics on Z_2                     ✘ EXPLORED, FAILS
│   │        T: Z_2 → Z_2 conjugate to full shift σ: {0,1}^N → {0,1}^N.
│   │        Every parity pattern gives unique n(ε) = S(ε)/D ∈ Z_2.
│   │        Self-consistency automatic. Constraint purely: D | S(ε).
│   │        CORRECTION: Cycles are REPELLING in Z_2 (|3^k/2^p|_2 = 2^p),
│   │        not attracting. Original entry confused archimedean/2-adic.
│   │        p-adic Fatou/Julia: INAPPLICABLE (T piecewise, not analytic).
│   │        No-wandering-domain theorem: VACUOUS (no Fatou components).
│   │        ROOT CAUSE: "n(ε) ∈ Z_{>0}" is ARCHIMEDEAN, invisible to
│   │        2-adic topology. Same barrier as 0A/0B/0C in different language.
│   │        File: nonarchimedean_Z2.md, nonarchimedean_verify.py
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
- **Session 3** (2026-03-06): Part 0 attack. Discovered the Transversal Zero-Sum Barrier (direction 0D). Key finding: unrestricted sumset always contains 0, but distinct-position constraint excludes it. New framework connecting Collatz to additive combinatorics and transversal theory.
- **Session 4** (2026-03-06): Proved WLOG i₁=0 reduction, n parity constraints, complete n=1 classification (trivial cycle iff p=2k), k≤4 no-cycles theorem. Developed 2-adic cascade method. Verified no nontrivial cycles for all p≤34 and near-critical (46,29). Min-distance analysis shows exclusion of 0 is tight (distance 1).
- **Session 5** (2026-03-06): Proved Syracuse-Cascade Duality (C7): cascade remainders c_j exactly track the Syracuse orbit of n. Proved fixed-k bound (C8): n_max → (3/2)^{k-1}. Proved k≤30 no-cycles (C9) via Collatz verification for n≤127834. Proved post-orbit obstruction (C10): odd n≥3 fails via n∤4. Extended cascade to p≤60 (83 pairs, 3.3M candidates). Proved U=Z/DZ for most composite D via CRT+Cauchy-Davenport. Established that the cascade IS the Collatz iteration (equivalence barrier confirmed for 0D).
- **Session 6** (2026-03-06): Explored direction 0B (Arakelov/arithmetic intersection theory on R = Z[x]/(x^p - 3^k)). Developed full analysis: embeddings, near-degenerate sigma_0, norm bounds, successive minima, q-adic filtration, coefficient entropy, Bezout inequality, theta functions. Result: all height-based methods fail because lattice membership is LINEAR — heights measure size, not residue class. Direction 0B closed.
- **Session 7** (2026-03-06): Explored direction 0C (motivic/categorical structure on {a,b}-smooth sums). Systematically analyzed 10 frameworks: toric geometry, log geometry, zeta functions, tropical geometry, F_1-geometry, configuration space cohomology, derived categories, Galois representations, determinant method, Pila-Wilkie. All fail for the same root cause: the Collatz condition involves EXPONENTIAL functions (2^{i_j}), but all cohomological/motivic methods work with ALGEBRAIC objects. No algebraic variety encodes the Collatz cycle set. Closest tool: o-minimal/Pila-Wilkie, but too weak for growing dimension. Direction 0C closed. ALL Part 0 directions now explored and closed. Then brainstormed 6 genuinely new research directions (6g-vi through 6g-xi): carry automaton, cascade increment correlation, prime-D sieve completion, digital CSP, induction on k, non-archimedean dynamics. These avoid the known barriers through different mechanisms and are recorded for future exploration.
- **Session 8** (2026-03-06): Explored direction 6g-xi (non-archimedean dynamics on Z_2). Proved: T conjugate to full shift (verified computationally), cycles are REPELLING in Z_2 (correcting the map entry which incorrectly said attracting), self-consistency automatic, p-adic Fatou/Julia inapplicable (T piecewise not analytic), no-wandering-domain vacuous. Root cause of failure: "n(eps) in Z_{>0}" is archimedean, invisible to 2-adic topology. Then developed barrier diagnostic: 6 questions predicting which barrier a proposed framework hits (100% retroactive accuracy). Applied prospectively to screen 6g-vi through 6g-x: three predicted to fail (Q4/equivalence), two ambiguous (6g-vii, 6g-viii). Explored 6g-vii (cascade increment correlation): computed halving excess, correlation structure, large deviation rates for k up to 30. Key findings: (1) independence rate I=0.055 vs needed rate 0.405 gives 7.4× gap; (2) SURPRISE: lag-1 correlations are POSITIVE (+0.02 to +0.04), making Var[G] > Var_indep — correlations hurt; (3) some candidates have G < p (Mersenne-like n with long g=1 streaks), so "G > p always" is false; (4) the 7.4× gap is Barrier 1 (abc) in cascade language. Direction 6g-vii closed. Explored 6g-viii (prime-D sieve completion): PROVED block decomposition impossible for prime D when p ≥ 5 (requires p² > 4D ≈ 4·2^p, impossible). Computation: ord_D(2) > p for ALL prime D tested (L=0 blocks always). Character sums: Cauchy-Schwarz excess 2^{0.525p}. CORRECTED: D is prime for only 6-10% of (p,k) pairs, not ~50%. Composite D: smallest lpf ratio = 0.18, handleable fraction often < 0.90. Both sub-problems reduce to abc barrier variants. ALL SIX directions 6g-vi through 6g-xi now CLOSED. No remaining unexplored direction passes the barrier diagnostic. Then developed the DEEPEST insight of the project: the function field Collatz analogy. Over F_q[t], the cycle equation is trivially unsolvable (deg(S) ≤ p-1 < p = deg(D), one-line proof). The proof doesn't lift to Z because of Ostrowski's theorem: no non-archimedean absolute value on Q has |2| > 1 (since |2| = |1+1| ≤ max(|1|,|1|) = 1). This gives the GAP-CONSTRAINT DICHOTOMY: the "top" measure gives the degree gap but not the divisibility constraint; the "bottom" measure (v_2) gives the constraint but not the gap; the function field degree gives BOTH. This UNIFIES all three barriers as consequences of Q having exactly one archimedean place (which is not ultrametric). A proof would need to circumvent Ostrowski: via ring extension, F_1-geometry, or a new proof structure. The Collatz conjecture might be "trivially true" from a viewpoint we haven't built yet. Finally, developed the FERMAT CURVE HEIGHT FRAMEWORK: the cycle equation D|S(I) is equivalent to ideal membership R_I in (s-3, t-2) inside A/DA where A = Z[s,t]/(t^p - s^k) is the coordinate ring of the Fermat curve C: t^p = s^k. The two-variable lift R_I(s,t) = sum s^{k-j} t^{i_j} has a DUAL DEGREE BOUND: deg_s(R_I) < k AND deg_t(R_I) < p, strictly less than D in BOTH variables. Over Q, this makes ideal membership impossible (= function field proof). R_I has rigid STAIRCASE structure (monotone anti-diagonal with 0-1 entries). KEY INSIGHT: the function field proof uses only one constraint (degree), but the integer proof may need BOTH the bidegree constraint AND the divisibility structure — the function field proof is an "incomplete shadow." This frames Collatz as a HEIGHT INEQUALITY on the Fermat curve, connecting to Arakelov theory, Vojta's conjecture, and Frey curves. The specific case (specific curve, specific point, specific functions) may be tractable even when the general conjectures are not. THEN pushed further into computation: discovered that P(3) = S(I) is a polynomial with STRICTLY DECREASING power-of-2 coefficients evaluated at x=3, and by the REARRANGEMENT INEQUALITY, the staircase gives the MINIMUM over all k! permutations. Unordered permutations hit 0 mod D at rate ~1/D (random); ordered (staircase) NEVER hits 0. Proved k<=4 independently using Rearrangement + size bounds (new method). Developed the AFFINE WALK interpretation: cycle equation = walk w->3w+c mod D starting at 1, with INCREASING power-of-2 perturbations, reaching 0. Discovered the THREE-CONSTRAINT structure: (1) perturbations are powers of 2, (2) strictly increasing order, (3) exponential growth c_m >= 2^m. NO single constraint or pair suffices; all three together exclude 0.

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
| `framework_transversal_zero_sum.md` | **Direction 0D: Transversal Zero-Sum framework** |
| `distinct_position_barrier.py` | Computation: unrestricted vs restricted sumsets |
| `monotone_weight_barrier.py` | Computation: inversion analysis for zero-sum |
| `residue_zero_special.py` | Why residue 0 is structurally special |
| `session3_summary.md` | Session 3 summary and findings |
| `theorem_cascade.md` | **Session 4: 2-adic cascade theorems C1-C6** |
| `cascade_verifier.py` | Cascade verification for standard pairs |
| `cascade_extended.py` | Extended cascade to p≤34 |
| `cascade_p46.py` | Optimized cascade for (46,29) near-critical |
| `gap_analysis.py` | Min-distance-to-0 analysis |
| `cascade_syracuse.py` | **Session 5: Syracuse-Cascade Duality verification** |
| `cascade_extended_v2.py` | Extended cascade to p≤60 + U=Z/DZ analysis |
| `cascade_nearcritical.py` | Near-critical pairs (54,34) and (59,37) |
| `arakelov_0B.md` | **Session 6: Arakelov analysis on R = Z[x]/(x^p-3^k)** |
| `arakelov_verify.py` | Computational verification of Arakelov quantities |
| `motivic_0C.md` | **Session 7: Motivic/categorical analysis (10 frameworks)** |
| `motivic_verify.py` | Computational verification: Newton polygons, MV, tropical, partition fn |
| `nonarchimedean_Z2.md` | **Session 8: Non-archimedean dynamics on Z_2 (shift conjugacy, repulsion)** |
| `nonarchimedean_verify.py` | Computational verification: shift conjugacy, repulsion, 2-adic expansions |
| `barrier_diagnostic.md` | **Session 8: Barrier pre-screening checklist (6 questions, 3 barrier families)** |
| `cascade_correlation.md` | **Session 8: Cascade increment correlation (7.4× gap, positive correlations)** |
| `cascade_correlation_verify.py` | Computational verification: G distribution, correlations, large deviations |
| `prime_d_sieve.md` | **Session 8: Prime-D sieve completion (scale gap impossibility)** |
| `prime_d_sieve_verify.py` | Computational verification: primality, ord_D(2), factorization, handleable fraction |
| `function_field_collatz.md` | **Session 8: Function field analogy + Ostrowski obstruction (deepest insight)** |
| `fermat_curve_height.md` | **Session 8: Fermat curve framework — cycle eq. as ideal membership, dual degree bound, height inequality** |
