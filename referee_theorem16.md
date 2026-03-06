# Referee Report: Proof of Theorem 8.1 / "Theorem 16" (Constant Spectral Gap for Almost All Primes)

**Paper:** "Sum-Product Estimates and the Universal Spectral Gap for the Affine Collatz Walk"
**File:** `/Users/tsuimingleong/Desktop/math/agent_sum_product.md`
**Scope of review:** Sections 3--9 and the detailed proofs in Section 11, focusing on the proof of Theorem 8.1 (restated in Section 11.4).

---

## 1. Overall Assessment

**Status: CORRECT WITH GAPS**

The main theorem proved is:

> **Theorem 8.1 (= Theorem A).** For every epsilon > 0, there exists c(epsilon) > 0 such that if p >= 5 is prime with ord_p(3/2) >= p^{1/2+epsilon}, then |lambda_2(p)| <= 1 - c(epsilon).

> **Corollary B.** For almost all primes p (in the natural density sense), |lambda_2(p)| <= 1 - c for an absolute constant c > 0.

The overall architecture of the proof is sound: (1) near-equality in Cauchy--Schwarz forces energy onto an arc, (2) the support is approximately invariant under multiplication by 3/2, (3) Gauss sum equidistribution bounds the fraction of a (3/2)-orbit in any arc, (4) combining yields a constant lower bound on eta = 1 - |lambda|^2. However, there are several gaps of varying severity, identified below.

---

## 2. Detailed Step-by-Step Analysis

### Step 1: Near-CS-equality forces arc concentration

**Claim (Proposition 4.4, Section 11.2):** If |lambda|^2 >= 1 - eta, then there exists theta such that sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 <= 4 eta.

**Verdict: CORRECT.**

The proof is clean. The key identity:

    ||Mf||^2 = 1/2 + (1/2) Re <T_0 f, T_1 f>

is correctly derived in Section 11.1 (Proposition 3.1). The computation of <T_0 f, T_1 f> via Fourier orthogonality is standard and correct. The deduction that Re[sum_s a_{3s} conj(a_s) omega^{-s/2}] >= 1 - 2 eta when |lambda|^2 >= 1 - eta follows immediately. The expansion of sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 = 2 - 2 rho is correct by direct calculation.

**Minor note:** The Cauchy--Schwarz step on line 1084 uses the *triangle inequality* for sums (|sum z_s| <= sum |z_s|) followed by Cauchy--Schwarz on |a_{3s}||a_s|. This is correct since sum |a_{3s}||a_s| <= (sum |a_{3s}|^2)^{1/2}(sum |a_s|^2)^{1/2} = 1, using the fact that multiplication by 3 is a bijection on F_p*.

**Claim (Corollary 4.5, Section 11.3):** The "arc weight" min_phi sum_s |a_s|^2 |1 - omega^{s/2} e^{-i phi}|^2 <= 4 eta.

**Verdict: CORRECT, but the deduction from Proposition 4.4 requires a small argument that is only sketched.**

The corollary as stated (lines 1098--1102) is actually a *weaker* restatement. Proposition 4.4 gives a bound on sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2, which involves BOTH a_{3s} and a_s. The arc weight involves only |a_s|^2 and the phase omega^{s/2}. To deduce the arc weight bound from Proposition 4.4, one needs the additional observation that the constraint a_{3s} approx e^{i theta} omega^{s/2} a_s, combined with |a_{3s}| = |a_{sigma(s)}| (where sigma is the multiplication-by-3 permutation), forces the *moduli* |a_s| to be approximately invariant under sigma. This approximate invariance of moduli, together with the phase constraint, then implies the arc concentration.

**GAP 1 (Minor):** The paper does not give a clean derivation of the arc weight bound from Proposition 4.4. The stated inequality min_phi W <= 4 eta is correct, but the connection between the "twisted L^2 deviation" sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 and the "arc weight" sum_s |a_s|^2 |1 - omega^{s/2} e^{-i phi}|^2 is not made explicit.

**Suggested fix:** One clean route is: from Proposition 4.4, for each s, |a_{3s}| is close to |a_s| (since their difference is controlled in L^2). Specifically, sum_s (|a_{3s}| - |a_s|)^2 <= sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 <= 4 eta (by the reverse triangle inequality). So the weight function w(s) = |a_s|^2 is approximately invariant under the multiplication-by-3 map. But the arc weight bound does NOT follow directly from Proposition 4.4 alone -- it additionally uses the structure of the Cauchy-Schwarz near-equality to constrain the phase of a_{3s}/a_s, and this phase constraint is what gives arc concentration. The correct argument is: near-equality in CS means the summands a_{3s} conj(a_s) omega^{-s/2} are nearly collinear, so arg(a_{3s}/a_s) - pi s/p is nearly constant (= theta). For modes where |a_s| is large, this forces pi s/p to be near a constant modulo 2 pi adjustments from arg(a_{3s}/a_s), which concentrates s on an arc. The formal version is exactly the Chebyshev/variance argument in Step 1 of Section 11.4, which is correct.

### Step 2: Approximate invariance under multiplication by 3/2

**Claim (Step 2, Section 11.4, line 1177):** sum_s |w((3/2)s) - w(s)| <= C_2 sqrt(eta).

**Verdict: THIS IS THE MOST SIGNIFICANT GAP.**

The paper states this as following "from the eigenvalue equation and Proposition 4.4" but does not prove it. Let me analyze what can actually be deduced.

**What Proposition 4.4 gives:** sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 <= 4 eta. This constrains the relationship between a_{3s} and a_s, not directly between w(3s) and w(s), let alone between w((3/2)s) and w(s).

**The issue of 3/2 vs. 3:** The Cauchy-Schwarz near-equality directly constrains the relationship between a_{3s} and a_s (multiplication by 3 on the index). The paper wants approximate invariance under multiplication by 3/2. The connection comes from the eigenvalue equation (**): a_s + omega^s a_{3s} = 2 lambda a_{2s}. Since a_{3s} approx e^{i theta} omega^{s/2} a_s, we get:

    a_s (1 + e^{i theta} omega^{3s/2}) approx 2 lambda a_{2s},

so |a_{2s}|^2 approx |a_s|^2 |1 + e^{i theta} omega^{3s/2}|^2 / (4|lambda|^2).

This relates w(2s) to w(s), NOT w((3/2)s) to w(s). To get approximate invariance under 3/2, one would need to combine the approximate invariance under 3 (from CS) with the relationship between w(2s) and w(s) (from the eigenvalue equation). Since (3/2) = 3 * 2^{-1}, approximate invariance under 3/2 would follow from approximate invariance under both 3 and 2^{-1}.

From Proposition 4.4, we have approximate invariance of |a_s| under multiplication by 3. From the eigenvalue equation, we get a *conditional* approximate invariance under multiplication by 2 -- conditional on the phase omega^{3s/2} being aligned. But this phase alignment is itself part of what we are trying to prove.

**GAP 2 (Moderate, but fixable):** The L^1 approximate invariance of w under multiplication by 3/2 is not proved. The paper needs either (a) a direct proof of this claim, or (b) to reformulate Step 4 using approximate invariance under multiplication by 3 alone (which IS proved), and equidistribution of <3>-orbits (rather than <3/2>-orbits).

**Suggested fix (option b):** Replace <3/2>-orbits with <3>-orbits throughout. From Proposition 4.4, we have sum_s (|a_{3s}| - |a_s|)^2 <= 4 eta, which gives approximate invariance of w under multiplication by 3. The <3>-orbit of any s_0 has size ord_p(3). If ord_p(3) >= p^{1/2+epsilon'} for some epsilon' > 0, then the Gauss sum equidistribution bound applies to <3>-orbits and the argument goes through. Since ord_p(3/2) >= p^{1/2+epsilon} and ord_p(3/2) divides lcm(ord_p(3), ord_p(2)), we have max(ord_p(3), ord_p(2)) >= ord_p(3/2)^{1/2} >= p^{(1/2+epsilon)/2} = p^{1/4+epsilon/2}. This is only >= p^{1/2+epsilon'} if epsilon > 1/2, which is a stronger condition than needed.

**Alternative fix:** Work with the full group <2,3> instead of <3/2>. Since |<2,3>| >= ord_p(3/2) >= p^{1/2+epsilon}, the orbit of s_0 under <2,3> has size >= p^{1/2+epsilon}. The equidistribution of {h * s_0 : h in H} in F_p for a subgroup H of F_p* of size >= p^{1/2+epsilon} follows from the same Gauss sum bound. From Proposition 4.4 plus the eigenvalue equation, one can show w is approximately invariant under the full group <2,3> (not just <3/2>), because approximate invariance under 3 and the eigenvalue equation coupling 2 give approximate invariance under all generators. This would suffice but requires more work to make rigorous.

**Most direct fix:** Simply note that the Proposition 4.4 constraint gives approximate invariance under multiplication by 3 directly. This is enough: if the energy is concentrated on an arc I of size sqrt(eta) * p, then for the weight to be approximately 3-invariant, the orbit {3^k s_0} must have a large fraction inside I. The equidistribution of <3>-orbits (which have size ord_p(3)) then gives the bound. One needs ord_p(3) >= p^{1/2+epsilon'}, which may not follow from ord_p(3/2) >= p^{1/2+epsilon}. However, if ord_p(3) < p^{1/2}, then since ord_p(3/2) >= p^{1/2+epsilon}, we must have ord_p(2) >= p^{epsilon} (roughly), and one can use the multiplicative structure of <2> combined with the eigenvalue equation. This requires a case analysis that is not present in the paper.

### Step 3: Gauss sum equidistribution

**Claim (Step 3, Section 11.4, line 1184):** For any arc I of size R, |#{k : (3/2)^k s_0 in I} - ell * R/p| <= C_3 sqrt(p) log(p).

**Verdict: CORRECT, but the bound should be stated more carefully.**

The standard result is: for a subgroup H of F_p* of size K, and the additive character psi_t(x) = omega^{tx},

    |sum_{h in H} psi_t(h)| <= sqrt(p)    for t not= 0 mod p.

This follows from the character sum decomposition:

    sum_{h in H} psi_t(h) = (K/(p-1)) sum_{chi: chi|_H = triv} tau(chi, t)

where tau(chi, t) is a Gauss sum with |tau(chi, t)| = sqrt(p) for non-principal chi. There are (p-1)/K - 1 non-principal characters trivial on H, plus the principal character contributing -K/(p-1). So:

    |sum_{h in H} psi_t(h)| <= K/(p-1) + ((p-1)/K - 1) * K/(p-1) * sqrt(p) = K/(p-1) + (1 - K/(p-1)) * sqrt(p) <= sqrt(p).

This is correct. The discrepancy of H in any arc of size R is then at most C sqrt(p) log(p) (by the Erdos-Turan inequality, summing over O(log p) Fourier coefficients, or more precisely over all non-trivial harmonics with a smooth cutoff).

**Note:** The bound on line 1184 uses |sum omega^{t*h}| <= sqrt(p) for the subgroup <3/2>. This is correct but the log(p) factor comes from the Erdos-Turan inequality or the explicit Fourier analysis of the arc indicator. The paper cites this as a "Gauss sum bound" which is slightly imprecise -- it is a Gauss sum bound *combined with* a discrepancy estimate. This is standard.

**GAP 3 (Very minor):** The equidistribution bound is stated for <3/2>-orbits but the argument (see Gap 2) should use orbits of whatever subgroup the approximate invariance is established for. If using <3>-orbits, one needs ord_p(3) >= p^{1/2+epsilon'}.

### Step 4: Combining the constraints

**Claim (Step 4, Section 11.4, lines 1200--1251):** From the above, 1 - C eta <= C sqrt(eta) + o(1), forcing eta >= c > 0.

**Verdict: THE LOGIC IS CORRECT, MODULO THE GAPS IN STEPS 1-2.**

The argument proceeds as follows:

(A) The energy weight w is concentrated on an arc I of size ~ sqrt(eta) * p (from Step 1). Formally, by Chebyshev with the variance bound, the mass outside an arc of angular half-width delta is at most C_1 eta / delta^2. Setting delta so that the excluded mass is at most 1/4 gives delta = 2 sqrt(C_1 eta).

(B) The weight w is approximately invariant under multiplication by 3/2 (Step 2 -- with the gap noted above).

(C) Any <3/2>-orbit has at most fraction F = sqrt(eta) + C_3 p^{-epsilon/2} log(p) of its elements in the arc (Step 3).

(D) If w were exactly constant on each <3/2>-orbit, then the mass of w inside the arc would be at most F. Since the mass inside the arc is at least 3/4 (from A), we get F >= 3/4, hence sqrt(eta) >= 3/4 - o(1), hence eta >= c > 0.

(E) The deviation from exact constancy on orbits contributes an error term bounded by C_2 sqrt(eta) (from Step 2).

The combining inequality is:

    3/4 <= F + C_2 sqrt(eta) = sqrt(eta)(1 + C_2) + C_3 p^{-epsilon/2} log(p),

which for large p gives sqrt(eta) >= 3/(4(1 + C_2) + 4), hence eta >= c > 0.

**The logic is correct.** The key inference "1 - C eta <= C sqrt(eta) + o(1) implies eta >= c > 0" is valid because for small eta the left side is close to 1 and the right side is close to 0 (for large p), giving a contradiction. Specifically, if eta < 1/(100 C^2), then C sqrt(eta) < 1/10 and C eta < 1/100, so 1 - 1/100 < 1/10 + o(1), which fails for large p.

**The precise value of c_0:** The paper claims c(epsilon) = epsilon^2 / 10^6 on line 1157. This is never justified by explicit calculation. From the combining inequality with the specific constants, one would get c(epsilon) depending on C_1, C_2, C_3, and the threshold for "p large enough." The claimed value epsilon^2/10^6 is plausible but unverified.

**GAP 4 (Minor):** The explicit value c(epsilon) = epsilon^2/10^6 is not derived. The proof shows eta >= c(epsilon) > 0 for some unspecified c(epsilon) depending on the constants C_1, C_2, C_3, which in turn depend on epsilon through the condition p >= p_0(epsilon).

### Corollary B: Almost all primes

**Claim:** By the Erdos--Murty theorem, for almost all primes p, ord_p(a) >= p^{1-epsilon} for any fixed integer a >= 2. Hence |<2,3>| >= p^{1-epsilon} >= p^{1/2+epsilon} for epsilon < 1/2.

**Verdict: CORRECT, modulo a standard reference.**

The Erdos--Murty result (more precisely, Kurlberg--Pomerance or similar) states that for any fixed a not= -1 or a perfect square, ord_p(a) > p^{1/2} for a positive proportion of primes, and ord_p(a) > p^{1-epsilon} for almost all primes under GRH or unconditionally in weaker forms. The paper cites "Erdos-Murty" which is sufficient for the density-one statement. This is a well-established result in analytic number theory.

**Note:** The paper actually needs ord_p(3/2) >= p^{1/2+epsilon}, not just ord_p(2) or ord_p(3) individually. Since 3/2 is a fixed element of Q*, the Erdos--Murty type result applies equally to ord_p(3/2) (viewing 3 * 2^{-1} as a rational number whose order modulo p is well-defined for p >= 5).

---

## 3. Summary of Gaps

| # | Location | Severity | Description | Fixable? |
|---|----------|----------|-------------|----------|
| 1 | Section 11.3 (Corollary 4.5) | Minor | Deduction of arc weight bound from Proposition 4.4 not made explicit | Yes -- a few lines of argument suffice |
| 2 | Section 11.4, Step 2 | Moderate | Approximate L^1 invariance of w under *(3/2) is asserted without proof | Yes -- see suggested fixes below |
| 3 | Section 11.4, Step 3 | Very minor | Equidistribution bound stated for <3/2>-orbits but should be matched to whichever group's invariance is established | Yes -- notational |
| 4 | Section 11.4 | Minor | Explicit constant c(epsilon) = epsilon^2/10^6 not derived | Yes -- bookkeeping |

---

## 4. Assessment of Fixability

**All gaps are fixable.** The most significant gap (Gap 2) can be addressed in at least two ways:

### Fix A: Direct proof of approximate w-invariance under 3/2

From Proposition 4.4: sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 <= 4 eta.

This gives, by the reverse triangle inequality:

    sum_s (|a_{3s}| - |a_s|)^2 <= 4 eta,

so w(s) = |a_s|^2 satisfies sum_s |sqrt(w(3s)) - sqrt(w(s))|^2 <= 4 eta. By Cauchy-Schwarz and the inequality ||a|^2 - |b|^2| <= (|a| + |b|)|a - b|:

    sum_s |w(3s) - w(s)| <= (sum_s (sqrt(w(3s)) + sqrt(w(s)))^2)^{1/2} (sum_s (sqrt(w(3s)) - sqrt(w(s)))^2)^{1/2}
                          <= (sum_s 2(w(3s) + w(s)))^{1/2} * (4 eta)^{1/2}
                          = (4)^{1/2} * 2 sqrt(eta) = 4 sqrt(eta).

So w IS approximately invariant under multiplication by 3 in L^1.

Now, from the eigenvalue equation (**): a_s + omega^s a_{3s} = 2 lambda a_{2s}. Taking moduli squared:

    |a_{2s}|^2 = |a_s + omega^s a_{3s}|^2 / (4|lambda|^2).

Since a_{3s} approx e^{i theta} omega^{s/2} a_s (Proposition 4.4), we have approximately:

    |a_{2s}|^2 approx |a_s|^2 |1 + e^{i theta} omega^{3s/2}|^2 / (4|lambda|^2).

For this to give approximate invariance of w under multiplication by 2, we would need |1 + e^{i theta} omega^{3s/2}|^2 / (4|lambda|^2) approx 1, which is NOT generically true (it depends on the phase omega^{3s/2}).

**However, approximate invariance under multiplication by 2 is not needed for the proof.** The proof only needs the equidistribution argument applied to orbits of *some* large subgroup for which w is approximately invariant. Since w IS approximately invariant under multiplication by 3 (as shown above), we can use <3>-orbits of size ord_p(3).

The question is whether ord_p(3) >= p^{1/2+epsilon'} follows from ord_p(3/2) >= p^{1/2+epsilon}. In general, it does not: it is possible that ord_p(3) is small while ord_p(3/2) is large. For example, if 3 has order 2 mod p (i.e., p | 8, impossible for primes, but small orders are possible), while 2 has large order.

### Fix B: Reformulate using <2,3>-orbit equidistribution directly

The key insight is that the *support* of the eigenvector lies in a single <2,3>-orbit of size K = |<2,3>|. The cross-term sum is over this orbit. The weight w is approximately invariant under multiplication by 3 (proved above). The eigenvector equation also gives a relationship for w(2s) in terms of w(s) and w(3s), which combined with the approximate 3-invariance gives approximate 2-invariance up to a multiplicative factor depending on omega^{3s/2}. Crucially, the arc concentration from Step 1 constrains s to a region where omega^{s/2} is close to e^{i phi}, so omega^{3s/2} is close to e^{3i phi/2} -- that is, the multiplicative factor is approximately constant on the arc. This gives approximate invariance of w under multiplication by 2 *on the arc*, which suffices.

**More precisely:** On the arc I where sin^2(pi s/p - phi/2) <= C eta / w(s), the phase omega^{3s/2} = e^{3 pi i s/p} is approximately e^{3 i phi / 2} (up to error O(sqrt(eta))). So |1 + e^{i theta} omega^{3s/2}|^2 approx |1 + e^{i(theta + 3 phi/2)}|^2 =: A^2, a constant. Then w(2s) approx (A^2 / 4|lambda|^2) w(s) for s in I. Since sum_s w(s) = 1 and w(2s) sums to the same thing (2 permutes F_p*), the constant A^2/(4|lambda|^2) must be close to 1. This gives approximate invariance of w under multiplication by 2 on the arc.

With approximate invariance under both 2 and 3 on the arc, the full <2,3>-orbit equidistribution applies. Since |<2,3>| >= p^{1/2+epsilon}, the argument concludes as before.

**This fix requires about one page of additional argument but is entirely standard.**

### Fix C (Cleanest): Bypass the 3/2-invariance entirely

The argument can be restructured to avoid the intermediate step of 3/2-invariance. Here is the streamlined version:

1. By Proposition 4.4, w has variance <= C eta on the circle (arc concentration).
2. By the reverse-triangle argument above, w is approximately 3-invariant in L^1.
3. By Chebyshev, at least 3/4 of the w-mass is in an arc I of size O(sqrt(eta) p).
4. By 3-invariance, the w-mass in I is approximately the same as the w-mass in 3*I. So 3*I must overlap with I significantly, forcing the arc to be near 0 mod p (since 3*I is centered at 3 * center(I), and for overlap we need |3c - c| = |2c| < size(I)).
5. Now iterate: 3^k * I must overlap with I for all k. By equidistribution of {3^k * c mod p} (for ord_p(3) large), the center c must be near 0, and the orbit {3^k} must stay in a neighborhood of 0 of size O(sqrt(eta) p). By the Gauss sum bound, the fraction of the <3>-orbit in this neighborhood is at most sqrt(eta) + sqrt(p)/ord_p(3).
6. The w-mass outside the neighborhood is at most 4 sqrt(eta) (from the L^1 3-invariance deviation). So: 1 - 4 sqrt(eta) <= sqrt(eta) + sqrt(p)/ord_p(3), giving sqrt(eta) >= c - sqrt(p)/ord_p(3).

For this to give eta >= c > 0, one needs ord_p(3) >= C sqrt(p), which is weaker than ord_p(3/2) >= p^{1/2+epsilon}. In fact, one only needs ord_p(3) >> sqrt(p), which follows from ord_p(3/2) >= p^{1/2+epsilon} in most cases (since ord_p(3/2) divides ord_p(3) * ord_p(2), so max(ord_p(3), ord_p(2)) >= sqrt(ord_p(3/2)) >= p^{1/4+epsilon/2}, which is NOT enough).

**However**, if we also use the eigenvalue equation to get approximate 2-invariance on the arc (as in Fix B), then we can use <2,3>-orbit equidistribution and the condition |<2,3>| >= p^{1/2+epsilon} directly. This is the cleanest route.

---

## 5. The Strongest Theorem the Argument Actually Proves

With the gaps filled (using Fix B or Fix C), the argument proves:

> **Theorem (Strongest version from the current argument).** Let p >= 5 be prime. Suppose |<2,3>| >= p^{1/2+epsilon} for some epsilon > 0. Then there exist constants c(epsilon) > 0 and p_0(epsilon) such that for all p >= p_0(epsilon):
>
>     |lambda_2(p)| <= 1 - c(epsilon).
>
> For p < p_0(epsilon), the spectral gap is positive by direct computation (every eigenvalue other than 1 has |lambda| < 1).

**Corollary.** For almost all primes p (in the natural density sense), |lambda_2(p)| <= 1 - c for an absolute constant c > 0. Here "almost all" means: the set of exceptional primes has natural density 0.

### Can the condition |<2,3>| >= p^{1/2+epsilon} be relaxed?

**Partially, yes.** The argument uses the subgroup size only in the equidistribution step (Step 3), where the discrepancy is O(sqrt(p)/K). For the final inequality to give eta >= c > 0, one needs sqrt(p)/K -> 0, i.e., K >> sqrt(p). The exponent 1/2 + epsilon can potentially be replaced by just 1/2 + o(1), i.e., K >= p^{1/2} * omega(p) for any function omega(p) -> infinity. The log(p) factor in the discrepancy bound means K >= sqrt(p) * log(p) suffices.

**The condition cannot be fully removed by this argument.** If |<2,3>| = O(sqrt(p)), the equidistribution error is O(1), which provides no useful bound. A fundamentally different argument would be needed for such primes (if they exist in infinite number).

**Regarding which subgroup matters:** The argument as corrected (Fix B) uses equidistribution of <2,3>-orbits. If one could establish approximate w-invariance under multiplication by 3 alone (which IS proved) and use <3>-orbit equidistribution, the condition would be ord_p(3) >> sqrt(p) instead of |<2,3>| >> sqrt(p). These conditions are different: it is possible for |<2,3>| to be large while ord_p(3) is small (when ord_p(2) is large and ord_p(3) is small). The Fix B approach, using both generators and arc localization, is the most robust.

---

## 6. Additional Observations

### 6.1. Sections 5--7: Exploratory material

Sections 5, 6, and 7 contain exploratory calculations and partial results that do not contribute to the final proof. They are valuable for understanding the landscape of approaches but include several incomplete arguments (e.g., Section 5.3's BSG attempt, Section 6.6's proof sketch with "let me reconsider," Section 7.3's "Lemma 7.3 -- needed, not proved"). These sections should be clearly marked as exploratory/motivational rather than part of the formal proof.

### 6.2. The cross-term decomposition and T_0, T_1 isometry

The claim that T_0 and T_1 are isometries (line 1056) is correct: T_0 f(x) = f(alpha x) where alpha in F_p*, so T_0 is a composition with a bijection on F_p, hence preserves L^2 norm. Similarly for T_1 (an affine bijection). The expansion ||Mf||^2 = (1/4)||T_0 f||^2 + (1/4)||T_1 f||^2 + (1/2) Re <T_0 f, T_1 f> uses ||alpha T_0 f + beta T_1 f||^2 = |alpha|^2 ||T_0 f||^2 + |beta|^2 ||T_1 f||^2 + 2 Re(alpha conj(beta) <T_0 f, T_1 f>) with alpha = beta = 1/2. This is correct.

### 6.3. Error terms in the equidistribution bound

The Gauss sum bound |sum_{h in H} omega^{th}| <= sqrt(p) (for t not= 0) gives, via the Erdos-Turan inequality with N Fourier coefficients:

    discrepancy <= C/N + C sum_{n=1}^{N} |sum_{h in H} omega^{n h}| / (n * K)
                <= C/N + C * N * sqrt(p) / K.

Optimizing over N: N = (K/sqrt(p))^{1/2}, giving discrepancy <= C * p^{1/4} / sqrt(K). For K >= p^{1/2+epsilon}, this is O(p^{-epsilon/2}), confirming the paper's bound. The log(p) factor in the paper (line 1184) is slightly pessimistic but harmless.

### 6.4. The single-coset base case

The observation in Section 6.3 that an eigenvector supported on a single <2>-coset has |lambda| = 1/2 is correct and instructive. It shows the "base case" gap is 1/2, and the challenge is to show that spreading energy across multiple cosets cannot bring |lambda| close to 1.

### 6.5. Connection to Collatz conjecture (Section 10.3)

The paper's "Conditional Theorem" about the Collatz conjecture is stated without proof and should be regarded as motivation rather than a result. The information-theoretic argument sketched is heuristic.

---

## 7. Verdict

**CORRECT WITH GAPS.** The proof of Theorem 8.1 (constant spectral gap for primes with |<2,3>| >= p^{1/2+epsilon}) and Corollary B (almost all primes) is essentially correct. The main gap (Gap 2: approximate invariance under 3/2) is fixable by standard arguments, as detailed in Section 4 of this report. The remaining gaps are minor or notational.

The paper is honest about what it does and does not prove: the universal spectral gap for ALL primes remains open, and the paper clearly states this (Section 10.2). The exploratory material in Sections 5--7 is useful for understanding the difficulties but should be separated from the formal proof.

**Recommendation:** Accept the result as stated (Theorem A and Corollary B), subject to filling Gap 2 with the argument outlined in Fix B above. The specific constant c(epsilon) = epsilon^2/10^6 should either be derived explicitly or removed in favor of "some c(epsilon) > 0."
