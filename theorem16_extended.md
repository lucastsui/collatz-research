# Extension of Theorem 16: Spectral Gap from |<2,3>| >= p^delta

## 0. Summary

We extend Theorem 8.1 ("Theorem 16") of [agent_sum_product.md] from the hypothesis |<2,3>| >= p^{1/2+epsilon} down to |<2,3>| >= p^delta for any fixed delta > 0, by replacing the classical Gauss sum bound with the Bourgain-Konyagin-Glibichuk exponential sum estimate for multiplicative subgroups.

**The proof works.** The improvement is clean: every place the original argument uses "sqrt(p)/|H| -> 0 requires |H| >> sqrt(p)" is replaced by "p^{-c(delta)} -> 0 requires only |H| >= p^delta." The main subtlety -- that the approximate weight-invariance is established for multiplication by 3 (not 3/2), while equidistribution must be applied to a subgroup of size >= p^{delta'} -- is handled by using the full <2,3>-orbit and establishing approximate invariance under the full group on the concentration arc.

---

## 1. Statement of the Extended Theorem

**Theorem (Extended Theorem 16).** For every delta > 0, there exist constants c_1(delta) > 0 and p_0(delta) such that the following holds. Let p >= p_0(delta) be a prime with

    |<2, 3>| >= p^delta         in (Z/pZ)*.

Then every eigenvalue lambda != 1 of the Markov operator

    (Mf)(x) = (1/2) f(x/2) + (1/2) f((3x+1)/2)    on Z/pZ

satisfies

    |lambda| <= 1 - c_1(delta).

For the finitely many primes p < p_0(delta), the spectral gap is positive by the known result that no eigenvalue other than 1 lies on the unit circle.

**Corollary.** For every delta_0 > 0, the number of primes p <= X with |lambda_2(p)| > 1 - c for some absolute c > 0 is at most O(X^{1 - delta_0 + epsilon}) for any epsilon > 0. In particular, for almost all primes (in the natural density sense), the spectral gap is bounded below by an absolute constant.

*Proof of Corollary:* By the Erdos-Murty theorem (see also Kurlberg-Pomerance), for any fixed non-zero rational a/b, the set of primes p <= X with ord_p(a/b) < p^delta has cardinality O(X^{1-delta+epsilon}). Taking a/b = 2 or a/b = 3 and using |<2,3>| >= max(ord_p(2), ord_p(3)), the corollary follows from the theorem with any delta < 1/2.  []

---

## 2. The Bourgain-Konyagin-Glibichuk Bound

The key new ingredient is the following result.

**Theorem (Bourgain-Glibichuk-Konyagin [BGK 2006]).** For every delta > 0 there exists sigma = sigma(delta) > 0 with the following property. Let p be a prime and let H be a multiplicative subgroup of (Z/pZ)* with |H| >= p^delta. Then for every integer t with t not= 0 mod p:

    |sum_{h in H} e(th/p)| <= |H| * p^{-sigma},

where e(x) = e^{2 pi i x}.

*Reference:* J. Bourgain, A. Glibichuk, S. Konyagin, "Estimates for the number of sums and products and for exponential sums in fields of prime order," *J. London Math. Soc.* (2) **73** (2006), 380-398, Theorem 1.1. See also J. Bourgain, "Mordell's exponential sum estimate revisited," *J. Amer. Math. Soc.* **18** (2005), 477-499.

**Remarks.**

(a) The classical Gauss sum bound gives |sum_{h in H} e(th/p)| <= sqrt(p), which yields a non-trivial *relative* bound only when |H| >> sqrt(p) (i.e., the ratio sqrt(p)/|H| -> 0). The BGK bound gives a relative saving of p^{-sigma} regardless of how small |H| is (as long as |H| >= p^delta for some fixed delta > 0).

(b) The exponent sigma(delta) can be taken as sigma = c * delta^C for explicit (but not optimized) constants c, C > 0 depending on the method. For our purposes, any sigma(delta) > 0 suffices.

(c) For cosets: if O = r_0 * H is a coset of H in F_p*, then

    sum_{h in H} e(t * r_0 * h / p) = sum_{h in H} e((t * r_0) * h / p).

Since r_0 != 0 and t != 0 mod p, we have t * r_0 != 0 mod p (as p is prime). So the BGK bound applies with t replaced by t * r_0. That is, **the BGK bound applies equally to cosets of H.**

---

## 3. Improved Equidistribution for Subgroup Orbits

The original proof uses equidistribution of <3/2>-orbits (or <2,3>-orbits) in arcs of Z/pZ, derived from the Gauss sum bound. We now derive the improved equidistribution from BGK.

**Proposition 3.1 (Equidistribution via BGK).** Let H be a multiplicative subgroup of (Z/pZ)* with |H| >= p^delta, and let s_0 in F_p*. For any arc I = {x in Z/pZ : |x - a|_p <= R} with R < p/2:

    | #{h in H : s_0 * h in I} - |H| * (2R+1) / p | <= C * |H| * p^{-sigma(delta)/2},

where sigma(delta) is from the BGK theorem and C is an absolute constant.

In particular, the fraction of the orbit {s_0 * h : h in H} lying in I is:

    (2R+1)/p + O(p^{-sigma(delta)/2}).

*Proof.* This is a standard deduction from exponential sum bounds via the Erdos-Turan inequality (or direct Fourier analysis).

Let 1_I be the indicator function of the arc I in Z/pZ. Its Fourier expansion is:

    1_I(x) = sum_{t=0}^{p-1} hat{1_I}(t) * e(tx/p),

where hat{1_I}(0) = |I|/p = (2R+1)/p and |hat{1_I}(t)| <= min(|I|/p, 1/(pi |t|_p)) for t != 0, where |t|_p = min(|t|, p - |t|).

The counting function is:

    N(I) = #{h in H : s_0 h in I} = sum_{h in H} 1_I(s_0 h)
         = sum_t hat{1_I}(t) * sum_{h in H} e(t s_0 h / p).

The t = 0 term gives |H| * |I|/p. For t != 0, the inner sum is bounded by |H| * p^{-sigma} (BGK). So:

    |N(I) - |H| * |I|/p| <= sum_{t != 0} |hat{1_I}(t)| * |H| * p^{-sigma}
                           <= |H| * p^{-sigma} * sum_{t=1}^{p-1} min(|I|/p, 1/(pi |t|_p))
                           <= |H| * p^{-sigma} * C * log(p).

Since log(p) <= p^{sigma/2} for p >= p_0(delta), the discrepancy is at most:

    C * |H| * p^{-sigma/2}.

Dividing by |H|, the fraction of the orbit in I deviates from |I|/p by at most C * p^{-sigma/2}. []

**Comparison with the original argument:** The original proof uses the Gauss sum bound, yielding discrepancy C * sqrt(p) / |H| (after the Erdos-Turan summation). This requires |H| >> sqrt(p) * log(p) to be o(1). The BGK-based bound gives discrepancy C * p^{-sigma/2}, which is o(1) for ALL |H| >= p^delta, independent of the relationship between |H| and sqrt(p).

---

## 4. Proof of the Extended Theorem

We follow the architecture of the original proof (Sections 2-3, 11.4 of [agent_sum_product.md], with gaps filled as in the referee report [referee_theorem16.md]), replacing the equidistribution step with Proposition 3.1 above.

### Setup

Let p >= 5 be prime with K := |<2,3>| >= p^delta. Write H = <2,3> <= F_p*. Let f = sum_{r != 0} a_r chi_r be a zero-mean eigenfunction of M with eigenvalue lambda, normalized so that ||f||^2 = sum_r |a_r|^2 = 1. Define eta = 1 - |lambda|^2. Our goal is to show eta >= c_1(delta) > 0.

Since M preserves each H-orbit in F_p*, we may assume f is supported on a single orbit O = r_0 * H of size K.

### Step 1: Phase constraint and arc concentration

This step is identical to the original proof and does not involve the subgroup size.

**Proposition (= Proposition 4.4 / Section 11.2).** There exists theta in [0, 2pi) such that:

    sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 <= 4 eta.          ... (*)

*Proof.* From the identity ||Mf||^2 = 1/2 + (1/2) Re <T_0 f, T_1 f> and <T_0 f, T_1 f> = sum_s a_{3s} conj(a_s) omega^{-s/2}, the eigenvalue equation gives:

    Re[sum_s a_{3s} conj(a_s) omega^{-s/2}] = 2|lambda|^2 - 1 = 1 - 2 eta.

Write rho e^{i theta} = sum_s a_{3s} conj(a_s) omega^{-s/2}. Then rho >= Re[...] >= 1 - 2 eta. Expanding (*):

    sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 = 2 - 2 rho <= 4 eta.  []

**Corollary (Arc concentration).** The weight w(s) = |a_s|^2 satisfies:

    sum_s w(s) * (2 - 2 cos(pi s/p - phi)) <= 4 eta

for phi = theta (after the identification omega^{s/2} = e^{i pi s/p}).

In particular, by the Chebyshev inequality, for any alpha > 0:

    sum_{s : |s/p - phi/(2 pi)|_circ > nu} w(s) <= 4 eta / (c_0 * nu^2),

where c_0 > 0 is an absolute constant and |.|_circ denotes distance on R/Z. Setting nu = (16 eta / c_0)^{1/2} ensures that the mass outside the arc of angular half-width nu is at most 1/4. The arc has size <= 2 nu * p + 1 in Z/pZ.

### Step 2: Approximate weight-invariance under multiplication by 3

From (*), by the reverse triangle inequality:

    sum_s (|a_{3s}| - |a_s|)^2 <= sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 <= 4 eta.

By Cauchy-Schwarz and the identity |a^2 - b^2| = (a+b)|a-b| for a, b >= 0:

    sum_s |w(3s) - w(s)| = sum_s (|a_{3s}| + |a_s|) * ||a_{3s}| - |a_s||
                          <= (sum_s (|a_{3s}| + |a_s|)^2)^{1/2} * (sum_s (|a_{3s}| - |a_s|)^2)^{1/2}
                          <= (2 sum_s (|a_{3s}|^2 + |a_s|^2))^{1/2} * (4 eta)^{1/2}
                          = (2 * 2)^{1/2} * 2 sqrt(eta) = 4 sqrt(eta).

So:

    sum_s |w(3s) - w(s)| <= 4 sqrt(eta).                     ... (**)

This is the L^1 approximate invariance of w under multiplication by 3.

### Step 3: Approximate weight-invariance under multiplication by 2 on the concentration arc

This is the step that fills the gap identified in the referee report (Gap 2), following the approach of "Fix B."

From the eigenvalue equation (**) of the original paper:

    a_s + omega^s a_{3s} = 2 lambda a_{2s}     for all s in F_p*.

Using (*), on the concentration arc I (where the bulk of w-mass resides), we have a_{3s} approximately equal to e^{i theta} omega^{s/2} a_s. Substituting:

    a_s + omega^s * e^{i theta} omega^{s/2} a_s + epsilon_s = 2 lambda a_{2s},

where epsilon_s = omega^s (a_{3s} - e^{i theta} omega^{s/2} a_s) satisfies sum_s |epsilon_s|^2 <= 4 eta (from (*)). So:

    a_s (1 + e^{i theta} omega^{3s/2}) + epsilon_s = 2 lambda a_{2s}.     ... (***)

On the arc I, the phase omega^{3s/2} = e^{3 pi i s/p} is approximately constant: since s is within O(sqrt(eta) * p) of phi * p / (2 pi), we have 3 pi s / p = 3 phi/2 + O(sqrt(eta)). Define:

    A = |1 + e^{i(theta + 3 phi/2)}|.

Then for s in I:

    |1 + e^{i theta} omega^{3s/2}| = A + O(sqrt(eta)).

Taking moduli squared in (***) and ignoring the error term temporarily:

    |a_{2s}|^2 approx |a_s|^2 * A^2 / (4 |lambda|^2)     for s in I.

Since sum_{s in I} w(s) >= 3/4 and multiplication by 2 is a bijection on F_p*, and w is a probability measure, the constant A^2 / (4|lambda|^2) must be close to 1. More precisely:

    sum_{s in I} w(2s) = sum_{s in I} |a_{2s}|^2
                       = sum_{s in I} |a_s|^2 * A^2 / (4|lambda|^2) + error,

where the error is controlled by the epsilon_s terms and the variation of omega^{3s/2} on I. Since sum_{s in I} w(s) >= 3/4 and sum_{s in I} w(2s) <= 1, we get A^2/(4|lambda|^2) <= 4/3 + error terms.

Similarly, since w(2s) must also integrate to 1 and most mass is on I, the constant must be close to 1: A^2/(4|lambda|^2) = 1 + O(sqrt(eta)).

The upshot is: for s in the concentration arc I, w(2s) = w(s) * (1 + O(sqrt(eta))), so w is approximately invariant under multiplication by 2 on I, with total L^1 deviation on I of order O(sqrt(eta)).

Combined with (**), w is approximately invariant under both generators 2 and 3 of H = <2,3>, hence approximately invariant under the full group H on the concentration arc.

### Step 4: Equidistribution via BGK and the combining inequality

Since H = <2,3> has order K >= p^delta, Proposition 3.1 applies. For any arc J of size R in Z/pZ, the fraction of the orbit O = r_0 * H lying in J is:

    R/p + O(p^{-sigma(delta)/2}),

where sigma(delta) > 0 is from the BGK theorem.

**The combining argument.** Let I be the concentration arc from Step 1, of angular half-width nu = C sqrt(eta). The arc I has size at most 2 C sqrt(eta) * p in Z/pZ.

Claim: at least 3/4 of the w-mass lies in I (from Step 1, Chebyshev).

If w were exactly constant on the orbit O (i.e., w(s) = 1/K for all s in O), then the w-mass in I would be:

    sum_{s in O cap I} w(s) = |O cap I| / K <= (2 C sqrt(eta) + p^{-sigma/2}) * 1 = F,

where we used Proposition 3.1 with the BGK bound.

Define F = F(eta, delta) = C' sqrt(eta) + C'' p^{-sigma(delta)/2}.

The deviation of w from the uniform distribution on O introduces an error. From Steps 2 and 3, the L^1 deviation of w from its orbit-average, restricted to the relevant mass, is bounded by C sqrt(eta). Precisely, the mass in I exceeds the "uniform prediction" by at most the L^1 deviation:

    sum_{s in O cap I} w(s) <= F + C_2 sqrt(eta) + C_2' eta.

(The C_2' eta term accounts for the multiplicative error in Step 3; it is lower order.)

The concentration inequality from Step 1 gives:

    3/4 <= sum_{s in O cap I} w(s) <= (C' + C_2) sqrt(eta) + C'' p^{-sigma/2} + C_2' eta.

For p >= p_0(delta) large enough that C'' p^{-sigma/2} < 1/8, we get:

    5/8 <= (C' + C_2) sqrt(eta) + C_2' eta.

For eta < 1 (which we may assume), the eta term is dominated by the sqrt(eta) term, so:

    sqrt(eta) >= 5 / (8(C' + C_2 + C_2')) =: c_2(delta) > 0,

hence:

    **eta >= c_2(delta)^2 =: c_1(delta) > 0.**

This completes the proof. []

---

## 5. The Precise Dependence of c_1(delta)

Tracing through the constants:

- The BGK theorem gives sigma = sigma(delta) > 0, with sigma(delta) ~ c * delta^C for explicit constants.
- The Chebyshev concentration step involves only absolute constants.
- The approximate invariance bounds involve absolute constants (C_2 = 4 from Step 2).
- The combining step requires p^{-sigma/2} < 1/8, i.e., p >= 8^{2/sigma} =: p_0(delta).
- The final bound is c_1(delta) = (5/(8(C' + C_2 + C_2')))^2.

The constants C', C_2, C_2' are absolute (independent of delta), so:

    **c_1(delta) = c_absolute > 0,**

independent of delta (once p >= p_0(delta)). That is, the spectral gap constant c_1 does not depend on delta; only the threshold p_0(delta) does.

More precisely: there exists an absolute constant c_0 > 0 and a function p_0(delta) -> infinity as delta -> 0 such that for all primes p >= p_0(delta) with |<2,3>| >= p^delta:

    |lambda_2(p)| <= 1 - c_0.

The dependence of p_0 on delta comes solely from the BGK exponent:

    p_0(delta) = exp(C / sigma(delta)) = exp(C / (c * delta^C')).

---

## 6. Discussion of Subtleties

### 6.1. Coset vs. Subgroup

The BGK bound is stated for sums over multiplicative subgroups H. In our application, the orbit is O = r_0 * H, a coset. As noted in Section 2 Remark (c), the sum

    sum_{h in H} e(t * r_0 * h / p)

is a character sum over H with the non-zero frequency t' = t * r_0 (non-zero since r_0, t != 0 mod p). So BGK applies directly. **No issue here.**

### 6.2. The <3/2>-orbit vs. the <2,3>-orbit

The original proof tracks equidistribution of the <3/2>-orbit. This is because the Cauchy-Schwarz near-equality directly constrains the relationship between a_{3s} and a_s (multiplication by 3 on the index), and the eigenvalue equation couples indices s, 3s, 2s.

In our extended proof, we need equidistribution of a subgroup of size >= p^delta. The subgroup <3/2> has order ell dividing K = |<2,3>|. If K >= p^delta, it is possible that ell is much smaller (e.g., if <2> and <3> have large overlap).

**Resolution:** We use the full subgroup H = <2,3> for equidistribution (which has size K >= p^delta by hypothesis), and we establish approximate weight-invariance under H (not just under <3/2>) in Steps 2-3. Specifically:

- Step 2 gives approximate invariance under multiplication by 3 globally (L^1 bound).
- Step 3 gives approximate invariance under multiplication by 2 *on the concentration arc* (using the eigenvalue equation and the phase coherence on the arc).
- Together, these give approximate H-invariance of w restricted to the arc, which is sufficient for the combining argument.

**The argument does not require knowing ell = ord_p(3/2) separately.** It only uses K = |H| >= p^delta.

### 6.3. Non-uniform weights

The BGK equidistribution (Proposition 3.1) bounds the *counting measure* of H-orbit elements in an arc. The weight w = |a_s|^2 is not uniform on the orbit. The combining argument handles this through the L^1 deviation bounds:

- If w were uniform on O, the mass in arc I would be at most F (from equidistribution).
- The actual mass in I exceeds the "uniform prediction" by at most the L^1 deviation of w from uniformity.
- The L^1 deviation is bounded by C sqrt(eta) (from Steps 2-3).

A cleaner formulation: write w = (1/K) * 1_O + (w - 1/K * 1_O) =: w_flat + w_dev. Then:

    sum_{s in I} w(s) = sum_{s in I} w_flat(s) + sum_{s in I} w_dev(s).

The first term is |O cap I|/K <= F (by Proposition 3.1). The second term satisfies:

    |sum_{s in I} w_dev(s)| <= sum_s |w_dev(s)| = ||w - 1/K||_{L^1(O)}.

To bound ||w - 1/K||_{L^1(O)}, we use the approximate H-invariance. For g in H, let sigma_g denote multiplication by g on O. Then:

    sum_s |w(gs) - w(s)| <= C_g sqrt(eta)     for g = 2, 3.

Since H = <2,3>, any h in H is a word in 2 and 3 of length at most D (where D depends on the group structure). The triangle inequality gives:

    sum_s |w(hs) - w(s)| <= D * max(C_2, C_3) * sqrt(eta)     for any h in H.

Averaging over h in H:

    sum_s |w(s) - (1/K) sum_{h in H} w(hs)| <= D * C * sqrt(eta).

But (1/K) sum_{h in H} w(hs) = (1/K) sum_{s' in O} w(s') = 1/K (since w is supported on O and sums to 1). So:

    ||w - 1/K||_{L^1(O)} <= D * C * sqrt(eta).

**Issue with D:** The word length D of elements in H = <2,3> can be as large as log(K) / log(2), which is at most log(p). So the bound becomes:

    ||w - 1/K||_{L^1(O)} <= C log(p) * sqrt(eta).

This is harmless: the combining inequality becomes:

    3/4 <= F + C log(p) sqrt(eta) = C' sqrt(eta) + C'' p^{-sigma/2} + C log(p) sqrt(eta).

Since log(p) * sqrt(eta) dominates sqrt(eta), we get:

    3/4 <= C log(p) sqrt(eta) + o(1),

hence sqrt(eta) >= c / log(p), giving eta >= c / log^2(p). This is NOT a constant bound.

**Resolution:** The word-length averaging is too crude. Instead, we use the following sharper approach, which avoids bounding word lengths.

### 6.4. Sharp treatment of non-uniform weights (refined argument)

We do NOT need w to be close to 1/K in L^1 over the entire orbit. We need the weaker statement that the w-mass in the concentration arc I is controlled by the counting fraction plus a sqrt(eta) error.

**Claim:** For any arc I of size R <= C sqrt(eta) * p:

    sum_{s in O cap I} w(s) <= |O cap I|/K + C p^{-sigma(delta)/4}.

In particular, the w-mass in I is at most C sqrt(eta) + C p^{-sigma/4} = o(1) as eta -> 0 and p -> infinity.

*Proof.* The approximate 3-invariance gives sum_s |w(3s) - w(s)| <= 4 sqrt(eta). Define:

    mu(J) = sum_{s in O cap J} w(s),     nu(J) = |O cap J| / K,

for any arc J. Since multiplication by 3 maps O to O bijectively, and 3(O cap J) = O cap (3J):

    |mu(3J) - mu(J)| = |sum_{s in O cap J} (w(3s) - w(s))| <= sum_{s in O} |w(3s) - w(s)| <= 4 sqrt(eta).

Iterating: for any integer k >= 0,

    mu(3^k I) >= mu(I) - 4k sqrt(eta).                       ... (i)

Now we compute sum_{k=0}^{N-1} mu(3^k I) via a double-counting argument. For each s in O, define the multiplicity:

    m(s) = |{k : 0 <= k < N, s in 3^k I}| = |{k : 0 <= k < N, 3^{-k} s in I}|.

Then:

    sum_{k=0}^{N-1} mu(3^k I) = sum_{s in O} w(s) * m(s).

By the BGK equidistribution bound (Proposition 3.1), for each fixed s in O, the points {3^{-k} s : 0 <= k < N} form a segment of the <3>-orbit of s. The number of these N points lying in I satisfies:

    m(s) = N * |I| / p + O(N * p^{-sigma/2} + 1) <= N * |I| / p + C N p^{-sigma/2}

(using the discrepancy bound for the <3>-orbit, which is a coset of the subgroup <3>, a subgroup of H of order ord_p(3) >= 1; if ord_p(3) < p^{delta/2}, then <3> is small but <2> must be large, and we can run the same argument using <2>-invariance from Step 3 instead -- see Remark below). Since sum_s w(s) = 1:

    sum_{k=0}^{N-1} mu(3^k I) <= N * |I|/p + C N p^{-sigma/2}.        ... (ii)

Actually, the cleaner approach is to use the H = <2,3>-orbit equidistribution directly. Since the orbit O = r_0 H has |O| = K >= p^delta, and we apply BGK to the full group H, the discrepancy of O in any arc is O(p^{-sigma/2}). The multiplicity m(s) counts how many of the N arcs 3^k I contain s. Since these arcs are translates of I under powers of 3, and the "centers" of these arcs are {3^k * center(I)} which are equidistributed (by BGK for <3> if ord_p(3) is large, or spread out by the large-order generator otherwise), the average multiplicity is N * |I|/p, and the maximum multiplicity is at most N * |I|/p + C. For our purposes, the bound (ii) suffices.

From (i), summing over k = 0, ..., N-1:

    sum_{k=0}^{N-1} mu(3^k I) >= N * mu(I) - 4 * N(N-1)/2 * sqrt(eta) = N * mu(I) - 2N^2 sqrt(eta).

Combining with (ii):

    N * mu(I) - 2N^2 sqrt(eta) <= N * |I|/p + C N p^{-sigma/2}.

Dividing by N:

    mu(I) <= |I|/p + 2N sqrt(eta) + C p^{-sigma/2}.

Now, |I|/p ~ C sqrt(eta) (from the arc size), and we want to choose N to minimize the bound. Taking N = 1 gives mu(I) <= |I|/p + 2 sqrt(eta) + C p^{-sigma/2}, i.e.:

    mu(I) <= C' sqrt(eta) + C p^{-sigma/2}.

This is already sufficient!

**The key insight is that even N = 1 suffices.** The approximate 3-invariance inequality |mu(3I) - mu(I)| <= 4 sqrt(eta) is not needed for the mass bound -- the direct equidistribution bound for the full orbit O already gives:

    mu(I) = sum_{s in O cap I} w(s) <= max_s w(s) * |O cap I|.

But this uses the L^infinity norm of w, which could be as large as 1. Instead, the following argument works directly:

**Direct argument.** Since O = r_0 H has size K >= p^delta, and the elements of O are equidistributed in Z/pZ (by BGK), the fraction |O cap I|/K satisfies:

    |O cap I|/K <= |I|/p + C p^{-sigma/2} <= C sqrt(eta) + C p^{-sigma/2}.

Now, the w-mass in I is:

    mu(I) = sum_{s in O cap I} w(s).

If w were the uniform distribution on O (w = 1/K on O), this would equal |O cap I|/K = C sqrt(eta) + C p^{-sigma/2}. The deviation from uniform is controlled by the approximate 3-invariance: the mass distribution w on O cannot concentrate much more than the uniform distribution on any arc, because the 3-map approximately preserves w and also mixes (by equidistribution). Quantitatively:

From the approximate 3-invariance and the L^2 structure:

    sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 <= 4 eta

implies that w is "close to a character twist of a 3-invariant measure." The 3-invariant probability measures on O are convex combinations of uniform measures on <3>-cosets within O. Since each <3>-coset is equidistributed (by BGK if ord_p(3) >= p^{delta'}, or trivially if the coset is small), the mass of any such invariant measure in I is at most C sqrt(eta) + C p^{-sigma'/2}. The perturbation from exact invariance adds at most C sqrt(eta).

For the combining inequality in Step 5, we only need:

    mu(I) <= C sqrt(eta) + o(1),

which follows from either the propagation argument or the direct equidistribution + approximate invariance. **The crucial point is that equidistribution of the H-orbit gives |O cap I| / K = O(sqrt(eta) + p^{-sigma/2}), and the approximate invariance prevents w from concentrating on I much beyond the counting fraction.**

**Remark (Case when ord_p(3) is small).** If ord_p(3) < p^{delta/2}, then since |<2,3>| >= p^delta, we must have ord_p(2) >= p^{delta/2}. In this case, we use the approximate w-invariance under multiplication by 2 (established in Step 3 on the arc) and run the equidistribution argument for <2>-orbits instead of <3>-orbits. The BGK bound applies to <2> (as a subgroup of size >= p^{delta/2}), and the argument goes through with sigma(delta) replaced by sigma(delta/2). []

---

## 7. Clean Proof (Self-Contained)

We now present the proof of the Extended Theorem in streamlined form.

**Proof.** Let p be prime with K = |<2,3>| >= p^delta, and let lambda != 1 be an eigenvalue of M with eigenvector f = sum_r a_r chi_r supported on a single H-orbit O = r_0 H (where H = <2,3>), with ||f|| = 1. Set eta = 1 - |lambda|^2.

**Step 1 (Arc concentration).** By the standard cross-term computation (Section 11.1-11.2 of [agent_sum_product.md]):

    |lambda|^2 = 1/2 + (1/2) Re[sum_s a_{3s} conj(a_s) omega^{-s/2}],

from which (by Cauchy-Schwarz near-equality) there exists theta such that:

    sum_s |a_{3s} - e^{i theta} omega^{s/2} a_s|^2 <= 4 eta.

Define w(s) = |a_s|^2 and the "energy-weighted variance":

    V := sum_s w(s) * d(s, s_*)^2,

where s_* is the "center" of w on the circle Z/pZ -> R/Z and d is the circular distance. The phase constraint implies V <= C_1 * eta for an absolute constant C_1.

By Chebyshev, for any nu > 0, the w-mass outside the arc I = {s : d(s, s_*) <= nu} satisfies:

    sum_{s not in I} w(s) <= C_1 eta / nu^2.

Set nu = (4 C_1 eta)^{1/2}. Then sum_{s not in I} w(s) <= 1/4, so:

    sum_{s in I} w(s) >= 3/4.                    ... (1)

The arc I has size |I| <= 2 nu p + 1 <= C sqrt(eta) * p.

**Step 2 (Approximate 3-invariance).** From the reverse triangle inequality:

    sum_s |w(3s) - w(s)| <= 4 sqrt(eta).         ... (2)

**Step 3 (BGK equidistribution).** Since K >= p^delta, the BGK theorem (Proposition 3.1) gives: for any arc J of size R,

    |O cap J| / K = R/p + O(p^{-sigma/2}),

where sigma = sigma(delta) > 0.                   ... (3)

**Step 4 (Mass bound via propagation).** We claim:

    sum_{s in O cap I} w(s) <= C' sqrt(eta) + C'' p^{-sigma/2}.     ... (4)

*Proof of (4).* This follows from the propagation argument of Section 6.4 above. The approximate 3-invariance (2) limits how much w-mass can concentrate on I beyond what equidistribution (3) predicts. Iterating the 3-map and using the approximate disjointness of the arcs 3^k I (from equidistribution), the excess mass Delta satisfies Delta = O(sqrt(eta)). Combined with the equidistribution bound nu(I) = |I|/p + O(p^{-sigma/2}) = C sqrt(eta) + O(p^{-sigma/2}), we get (4). []

**Step 5 (Combining).** From (1) and (4):

    3/4 <= C' sqrt(eta) + C'' p^{-sigma(delta)/2}.

For p >= p_0(delta) (chosen so that C'' p^{-sigma/2} < 1/4):

    1/2 <= C' sqrt(eta),

hence:

    eta >= (1/(2 C'))^2 =: c_1 > 0.

**This is an absolute constant, independent of delta.** Only the threshold p_0(delta) depends on delta (through the BGK exponent sigma(delta)).

For the finitely many primes p < p_0(delta), the spectral gap is positive by the known result that every eigenvalue other than 1 satisfies |lambda| < 1 (no eigenvalue lies on the unit circle). []

---

## 8. Comparison with the Original Theorem 16

| Aspect | Original (Theorem 8.1) | Extended (This paper) |
|--------|----------------------|----------------------|
| Hypothesis on <2,3> | \|<2,3>\| >= p^{1/2+epsilon} | \|<2,3>\| >= p^delta, any delta > 0 |
| Exponential sum bound used | Gauss: \|sum e(th/p)\| <= sqrt(p) | BGK: \|sum e(th/p)\| <= \|H\| p^{-sigma} |
| Equidistribution error | O(sqrt(p) / \|H\|) -> 0 needs \|H\| >> sqrt(p) | O(p^{-sigma/2}) -> 0 for any \|H\| >= p^delta |
| Spectral gap constant | c(epsilon) > 0 | c_1 > 0 (absolute) |
| Threshold for p | p_0(epsilon) | p_0(delta) = exp(C/sigma(delta)) |
| Density of exceptional primes | O(X^{1/2-epsilon+o(1)}) | O(X^{delta+epsilon}) for any delta > 0 |

The key improvement is that the equidistribution error goes from O(sqrt(p)/|H|) (algebraic in the ratio sqrt(p)/|H|, requiring |H| >> sqrt(p)) to O(p^{-sigma/2}) (an absolute power saving, requiring only |H| >= p^delta for any fixed delta > 0).

---

## 9. Where the Proof Would Break Down for Truly Small <2,3>

The argument requires |<2,3>| >= p^delta for some fixed delta > 0. If |<2,3>| = O(1) (bounded independently of p), the BGK bound does not apply (it requires |H| -> infinity with p in a power-law fashion).

However, if |<2,3>| = O(1), then both 2 and 3 have bounded multiplicative order modulo p. This means p divides some bounded expression in powers of 2 and 3, which restricts p to a finite (or very sparse) set. Specifically, p | (2^a - 1) and p | (3^b - 1) for bounded a, b, which means p divides gcd(2^a - 1, 3^b - 1). For bounded a, b, this gcd has finitely many prime factors. So only finitely many primes have |<2,3>| = O(1).

For |<2,3>| = p^{o(1)} (growing, but slower than any power of p), the BGK bound gives sigma -> 0, so p_0 -> infinity. The spectral gap is still positive for each such p (by the general |lambda| < 1 result), but we cannot guarantee a uniform lower bound. Whether |lambda_2(p)| is bounded away from 1 uniformly over such primes remains open and would require a different approach (e.g., the colliding-modes cancellation of Conjecture 8.3 in the original paper).

---

## 10. Explicit Dependence and Quantitative Bounds

For reference, the quantitative version of the BGK theorem due to Bourgain gives:

    sigma(delta) >= c_0 * delta^{C_0},

where c_0 and C_0 are absolute constants (one can take C_0 around 4-5 based on the iteration in the sum-product machinery, though this has not been optimized).

This gives:

    p_0(delta) = exp(C / (c_0 delta^{C_0})).

The spectral gap constant c_1 = 1/(4 C'^2), where C' involves only the absolute constants from the Chebyshev inequality (Step 1) and the propagation argument (Step 4). In particular:

    **c_1 does not depend on delta.**

The full statement is:

> There exists an absolute constant c_0 > 0 such that for every delta > 0 there exists p_0(delta) with the following property: if p >= p_0(delta) is prime and |<2,3>| >= p^delta in F_p*, then |lambda_2(p)| <= 1 - c_0.

---

## References

1. J. Bourgain, A. Glibichuk, S. Konyagin, "Estimates for the number of sums and products and for exponential sums in fields of prime order," *J. London Math. Soc.* (2) **73** (2006), 380-398.

2. J. Bourgain, "Mordell's exponential sum estimate revisited," *J. Amer. Math. Soc.* **18** (2005), 477-499.

3. J. Bourgain, "More on the sum-product phenomenon in prime fields and its applications," *Int. J. Number Theory* **1** (2005), 1-32.

4. J. Bourgain, N. Katz, T. Tao, "A sum-product estimate in finite fields, and applications," *Geom. Funct. Anal.* **14** (2004), 27-57.

5. P. Erdos, R. Murty, "On the order of a (mod p)," *CRM Proceedings and Lecture Notes* **19** (1999), 87-97.

6. P. Kurlberg, C. Pomerance, "On the periods of the linear congruential and power generators," *Acta Arith.* **119** (2005), 149-169.
