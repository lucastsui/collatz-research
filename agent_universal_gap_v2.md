# Universal Constant Spectral Gap: The Remaining Case K < p^{1/2+epsilon}

**Date:** 2026-03-05

**Problem:** Prove that for ALL primes p >= 5, the second-largest eigenvalue magnitude of the affine Collatz Markov operator on Z/pZ satisfies |lambda_2(p)| <= 1 - c for a universal constant c > 0.

**Focus:** The remaining case where both ord_p(2) = L_2 and ord_p(3) = L are at most p^{1/2+epsilon}, so K = |<2,3>| < p^{1/2+epsilon}.

---

## 0. Status Summary (What Is Known)

| Regime | Status | Key argument |
|--------|--------|--------------|
| K <= K_0 (bounded) | **Proved** | Compactness for fixed-dim transfer matrix |
| K >= p^{1/2+epsilon} | **Proved** | Theorem 16: arc concentration + Gauss equidistribution |
| K in (K_0, p^{1/2+epsilon}), i.e., L_2 AND L both small | **Open** | This document |

From agent_universal_gap.md, the CDG bootstrap argument (Section 14.3-14.4) shows: if the approximate phase condition a_{3s} ~ c * omega^{s/2} * a_s holds EXACTLY, then |lambda| = 1/2. The error propagation over L_2 steps of the x2 chain limits its applicability when L_2 is large. When L_2 >= sqrt(p), Jensen + equidistribution gives |lambda| <= 1/sqrt(2).

The gap is precisely the case where both L_2 < p^{1/2+epsilon} and L < p^{1/2+epsilon}. We pursue four approaches to close it.

---

## 1. Approach A: Two-Step M^2 Combined with CDG

### 1.1. The M^2 single-character bound

From the paper, for any nonzero mode r:

    ||M^2 chi_r||^2 = 3/8 + (1/8)|sum_{j in {0,1}} omega^{d_j(r)}|^2 / p ... (simplified)

More precisely, ||M^2 chi_r||^2 <= 3/8 for generic r (this is tight). The two-step contraction 3/8 < 1/2 is strictly better than the one-step 1/2.

### 1.2. The M^2 operator norm on non-constant subspace

The key question: is ||M^2||_{op, perp 1} < 1 universally?

From the identity (Section 10.4 of agent_universal_gap.md):

    ||M^2 f||^2 = 1/2 ||Mf||^2 + 1/2 Re<T_0(Mf), T_1(Mf)>

where Mf = (1/2)(T_0 f + T_1 f). Expanding:

    <T_0(Mf), T_1(Mf)> = (1/4)[<T_0^2 f, T_1 T_0 f> + <T_0^2 f, T_1^2 f> + <T_0 T_1 f, T_1 T_0 f> + <T_0 T_1 f, T_1^2 f>]

The critical term is <T_0 T_1 f, T_1 T_0 f>. As computed in Section 10.4:

    T_0 T_1(x) = (3x+1)/4,  T_1 T_0(x) = (3x+2)/4

These differ by an additive shift of -1/4. So:

    <T_0 T_1 f, T_1 T_0 f> = sum_x f((3x+1)/4) conj(f((3x+2)/4)) = <f, tau_{1/4} f>

where tau_{1/4} denotes the translation by 1/4. This is the autocorrelation of f at shift 1/4.

### 1.3. The autocorrelation constraint

For an eigenvector f with |lambda|^2 >= 1 - eta, the function f is concentrated (in energy) on modes where the "+1" phase is coherent, i.e., on an arc near some point in Z/pZ. For such a function:

- If f has most energy on modes r with |r/p| < delta (an arc near 0), then the autocorrelation at shift 1/4 satisfies:

    |<f, tau_{1/4} f>| = |sum_r |a_r|^2 omega^{r/4}|

  For modes near 0, omega^{r/4} ~ 1, so this autocorrelation is close to ||f||^2. Bad -- no contraction.

- However, for modes NOT near 0, the phase omega^{r/4} oscillates, and the autocorrelation is small.

**The problem:** When K < p^{1/2+epsilon}, the orbit O can cluster near 0 (if r_0 is small), making the autocorrelation large. The M^2 approach, while giving better per-character bounds, faces the same obstacle for the operator norm: a function concentrated on small modes escapes the phase cancellation.

### 1.4. Quantitative M^2 bound

Let us derive the exact M^2 operator norm bound. For f = sum_{r in O} a_r chi_r:

    ||M^2 f||^2 <= (1/2)||Mf||^2 + (1/2)||Mf||^2 = ||Mf||^2

This is trivially ||Mf||^2, which gives ||M^2||_{op} <= ||M||_{op}^2 -- not useful for improving the gap.

The improvement comes from the structure of the cross-term. Write:

    ||M^2 f||^2 = (1/2)||Mf||^2 + (1/2) Re Z

where Z = <T_0(Mf), T_1(Mf)>. Since ||Mf||^2 = |lambda|^2 ||f||^2:

    ||M^2 f||^2 = (1/2)|lambda|^2 ||f||^2 + (1/2) Re Z

Also ||M^2 f||^2 = |lambda|^4 ||f||^2. So:

    |lambda|^4 = (1/2)|lambda|^2 + (1/2) Re Z / ||f||^2

    Re Z / ||f||^2 = 2|lambda|^4 - |lambda|^2

For |lambda| = 1 - epsilon: Re Z / ||f||^2 ~ 2(1-4epsilon) - (1-2epsilon) = 1 - 6epsilon.
For |lambda| = 1/sqrt(2): Re Z / ||f||^2 = 2(1/4) - 1/2 = 0.

So the cross-term Z must be near ||f||^2 when |lambda| is near 1, and near 0 when |lambda| is near 1/sqrt(2). This is consistent: Z involves the commutator shift 1/4, and for |lambda| near 1, f must be concentrated on small modes where the shift phase is ~1.

**Conclusion on Approach A:** The M^2 approach does not by itself close the middle-range gap, because the operator-norm worst case (energy on small modes) exactly circumvents the phase cancellation from the 1/4-shift commutator. We need an argument that also exploits the multiplicative structure of the orbit, not just the additive shift.

---

## 2. Approach B: Mixed Orbits Using Both Generators

### 2.1. The idea

The CDG product identity uses only the <2>-orbit of a mode. After L_2 steps of multiplication by 2, the mode returns to itself, giving the exact product:

    prod_{j=0}^{L_2-1} cos(pi b 2^j / p) = +/- 2^{-L_2}

What if we use a "mixed" walk that interleaves multiplication by 2 and by 3?

### 2.2. The n-step expansion

After n applications of the eigenvalue equation, starting from mode r:

    a_{2^n r} = (2lambda)^{-n} sum_{w=0}^{n} c_w(r) a_{3^w r}

where c_w(r) involves sums of products of the phases omega^{...}. The key identity for the n-step walk is:

    (2lambda)^n a_{2^n r} = sum_{b in {0,1}^n} omega^{phi_b(r)} a_{3^{|b|} r}

where phi_b(r) is the accumulated phase from the "+1" translation along path b.

### 2.3. Using the mixed chain

Consider applying the eigenvalue equation alternately as:
- Step 1: equation (**) at mode s gives a_{2s} in terms of a_s and a_{3s}
- Step 2: equation (**) at mode 3s gives a_{6s} in terms of a_{3s} and a_{9s}
- ...

After k steps alternating between ×2 and ×3, we reach mode 2^a * 3^b * s for various (a,b). The total "distance" explored in the multiplicative group H = <2,3> is proportional to k.

The key structural observation from Section 8.3 of agent_universal_gap.md: Both T_0 and T_1 map each <3>-coset to the SAME target <3>-coset (since multiplication by 3 acts within cosets). The inter-coset dynamics is deterministic (always ×2^{-1}).

This means: after m = K/L steps of ×2 applied at the coset level, we cycle through all cosets. At each coset visit, the "+1" phase contributes omega^{r_i * gamma} where r_i depends on the coset. The accumulated phase after visiting all m cosets is:

    Phi_total = sum_{i=0}^{m-1} r_{sigma^i(0)} * gamma (mod p)

where sigma is the coset permutation.

### 2.4. The inter-coset phase accumulation

**Lemma 2.1.** The total accumulated phase from "+1" translations, after one full cycle through all m = K/L cosets, is:

    Phi_total = gamma * sum_{h in H/<3>} r_0 * h = gamma * r_0 * sum_{h in <2> mod <3>} h

where the sum is over coset representatives.

**Now:** sum_{j=0}^{m-1} 2^j (in F_p*) is a geometric sum. If 2^m != 1 mod p (which holds unless L_2 | m), this equals (2^m - 1)/(2 - 1) = 2^m - 1. But 2^m acts as the identity on the coset space iff m divides L_2 (the order of 2 in F_p*). Actually, 2^m represents the element 2^m in F_p*, which may or may not be 1.

The accumulated inter-coset phase is related to the sum of elements in certain cosets of <3> in H. This sum has a specific value in F_p* that depends on the algebraic structure of H.

### 2.5. When does the phase accumulation help?

The inter-coset phase accumulation gives additional constraints beyond those visible to a single <2>-chain. Specifically:

For the CDG argument along a single <2>-orbit of mode r, we get (2|lambda|)^{L_2} = prod |1 + c omega^{theta_j}| where theta_j = 2 pi * 3r 2^{j-1} / (2p). This product involves phases at the points 3r * 2^j / (2p) mod 1 for j = 0, ..., L_2-1.

For the mixed orbit, cycling through cosets introduces ADDITIONAL phase constraints from different cosets. Each coset C_i has its own representative r_i, and the CDG product at coset C_i is:

    prod_{j=0}^{L_2-1} |1 + c_i omega^{theta_j(r_i)}|

where c_i may differ between cosets (it absorbs the inter-coset shift). The eigenvalue |lambda| must simultaneously satisfy:

    (2|lambda|)^{L_2} = prod_{j} |1 + c_i omega^{theta_j(r_i)}|  for ALL cosets i

Since the r_i are in different <3>-cosets of H, the phases theta_j(r_i) are shifted by multiplicative factors of 3^k. The key question is whether the product can be simultaneously large for all cosets.

### 2.6. The simultaneous product constraint

**Proposition 2.2 (Multi-coset CDG).** For each <3>-coset C_i of the orbit O, the CDG identity gives:

    prod_{j=0}^{L_2-1} cos(pi r_i 2^j / p) = +/- 2^{-L_2}

Now, the shifted version (from the approximate phase condition) gives for each coset:

    (2|lambda|)^{L_2} <= prod_{j=0}^{L_2-1} |1 + c_i omega^{3 r_i 2^j / (2p)}|

Taking the GEOMETRIC MEAN over all m cosets:

    (2|lambda|)^{L_2} <= (prod_{i=0}^{m-1} prod_{j=0}^{L_2-1} |1 + c_i omega^{3 r_i 2^j / (2p)}|)^{1/m}

The double product has m * L_2 = K factors (one for each element of the orbit O). By AM-GM on log:

    (1/K) sum_{i,j} log|1 + c_i omega^{3 r_i 2^j / (2p)}|

**This sum runs over ALL K elements of the orbit!** If K >= p^{delta} for any delta > 0, the Gauss sum bound gives equidistribution of the set {3 r_i 2^j / (2p) mod 1 : (i,j)} in [0,1), with discrepancy at most C sqrt(p) / K.

Wait -- but we are in the case K < p^{1/2+epsilon}, so the discrepancy sqrt(p)/K could be O(1). The equidistribution fails.

**However**, there is a crucial difference: we are now averaging over the FULL orbit, not a sub-orbit. Even if the orbit has only K < sqrt(p) elements, the average of log|1 + omega^{...}| over the orbit gives a bound that depends on the orbit's distribution in Z/pZ.

### 2.7. Key realization: the orbit cannot cluster near 0

The orbit O = r_0 * H is the set {r_0 * h : h in H}. For this orbit to cluster near 0 in Z/pZ, we need most elements r_0 * h to be small (|r_0 * h mod p| << p). But the elements h in H are multiplicatively structured -- they are products of powers of 2 and 3.

**Proposition 2.3 (Orbit cannot concentrate on a small arc).** Let H = <2,3> in F_p* with |H| = K. For any r_0 in F_p* and any arc I of size R in Z/pZ (centered at 0):

    |r_0 H cap I| <= max(K, R * K / p + sqrt(p))

When K < sqrt(p) and R < p/K, the count is at most sqrt(p) + 1, which can be comparable to K itself! So the orbit CAN cluster near 0.

This happens precisely when r_0 is small and H generates elements that stay small before wrapping mod p. Since the elements of H are bounded by max(2,3)^{diam} where diam is the "diameter" of H in the Cayley graph of (Z/pZ)*, and for H of size K this diameter is at most K, the elements stay "small" in Z when they are < p. But 2^K and 3^K can be enormous in Z.

Actually, the elements of H as integers are {2^a 3^b mod p} for various (a,b). These can be very large or very small in Z/pZ depending on the specific modular arithmetic. When both L_2 and L are small, the "geometric" growth 2^a 3^b is bounded by max(2^{L_2}, 3^L) which is at most 3^{p^{1/2+eps}}. But mod p, these values wrap around, and the distribution depends on the specific group.

**The orbit-near-zero case remains the hardest.** This is consistent with the overall picture: when r_0 ~ 1/p (smallest possible), the orbit O might have all elements near 0, the "+1" phases are all near 1, and the operator nearly degenerates to the pure multiplicative walk (which has gap 0 on the unit circle in the limit).

---

## 3. Approach C: Explicit Computation for Small K

### 3.1. The one-parameter family

For a fixed group structure (fixed K, L_2, L, Cayley graph structure), the transfer matrix P on orbit O depends on a single parameter t = r_0 / p in (0,1) via the phases:

    theta_j = pi * r_0 * h_j / p = pi * t * h_j

where h_j ranges over H = <2,3> in F_p*.

The spectral radius rho(t) = max_{mu != 1} |mu(P(t))| is a continuous function of t in (0,1). By the Combined Theorem, rho(t) < 1 for all t and all primes.

### 3.2. Behavior as t -> 0

As t -> 0 (equivalently r_0 -> 0, but r_0 >= 1 so t >= 1/p), all phases theta_j -> 0. The transfer matrix approaches:

    P(0) = (1/2)(Pi_{2^{-1}} + I * Pi_{3 * 2^{-1}}) = (1/2)(Pi_{2^{-1}} + Pi_{3/2})

This is an average of two permutation matrices (no phases). Its eigenvalues are:

    lambda = (1/2)(omega_m^{-a j} omega_L^{-a k} + omega_m^{b j} omega_L^{b k})

where a, b encode how 2^{-1} and 3/2 act in the (coset, intra-coset) decomposition. The spectral radius of this unphased matrix is 1 (since at t=0, the "+1" translation vanishes and the walk becomes purely multiplicative with the stationary measure being uniform on the orbit).

**More precisely:** At t = 0, the matrix P(0) is doubly stochastic with respect to the uniform measure on O. Its eigenvalue 1 has multiplicity at least 1. But since P(0) is an average of two permutations and the group <2^{-1}, 3/2> acts transitively on O, the eigenvalue 1 has multiplicity exactly 1. The second-largest eigenvalue magnitude is:

    rho(0) = max_{k,j != (0,0)} (1/2)|e^{2pi i f_1(k,j)} + e^{2pi i f_2(k,j)}|

where f_1, f_2 are the phase functions from the two permutations. This maximum is at most cos(pi/K) (by the standard Cayley graph spectral gap for a transitive action of a group of order K).

Wait -- for a general pair of permutations, the spectral gap can be 0 (if they generate a group with a large abelian quotient). For our specific case, Pi_{2^{-1}} and Pi_{3/2} generate the group <2,3> acting on the orbit O, and since <2,3> acts transitively, the spectral gap depends on the expansion properties of this Cayley graph.

**Key fact:** The Cayley graph of a cyclic group Z/KZ with generators {a, b} has spectral gap 1 - cos(2pi/K) when ab^{-1} has order K (i.e., the generators don't commute in a trivial way). When K grows, this gap shrinks like pi^2/K^2.

So rho(0) ~ 1 - C/K^2 for our problem (when both generators act as cyclic shifts of order L_2 and L respectively, with the quotient structure determining the exact gap).

**At t = 1/p:** The phases are theta_j = pi h_j / p, all of order 1/p. The transfer matrix P(1/p) is a small perturbation of P(0):

    P(1/p) = P(0) + (1/p) P_1 + O(1/p^2)

where P_1 is a first-order correction from the phases. The spectral gap of P(1/p) is:

    gap(1/p) = gap(0) + O(1/p) = C/K^2 + O(1/p)

Since K < p^{1/2+epsilon}, we have K^2 < p^{1+2epsilon}, so C/K^2 > C/p^{1+2epsilon}. The correction O(1/p) is smaller than the leading term for small epsilon. So gap(1/p) ~ C/K^2.

**This is a positive gap, but it shrinks with K!** It does NOT give a universal constant gap. When K ~ p^{1/2}, the gap ~ 1/p, matching the L-V bound.

### 3.3. The critical observation: t is NOT arbitrary

The gap analysis as t -> 0 gives gap ~ C/K^2, shrinking with K. But the actual value of t for each prime is t = r_0/p, and crucially, r_0 cannot be zero -- it ranges over {1, 2, ..., p-1}/K (one representative per orbit).

The WORST orbit (minimizing the gap) has r_0 = min over orbit representatives. The smallest representative is the smallest element of F_p* not in any previous orbit. In the worst case, r_0 = 1 and t = 1/p.

So the gap for the worst orbit is gap(1/p) ~ C/K^2, which for K ~ p^{1/2} is ~ C/p.

**But we need more:** Can we show gap(1/p) >= c > 0 for a UNIVERSAL constant c, independent of p and K?

From the computation above: gap(1/p) ~ C/K^2 when K is large. So the answer appears to be NO for this linearized analysis. The gap shrinks with K unless we use a non-perturbative argument.

### 3.4. Non-perturbative: the exact t = 1/p gap

For t = 1/p, the phases are theta_j = pi h_j / p. The "+1" perturbation is O(1/p) in phase space, but the transfer matrix P(1/p) differs from P(0) by a RANK-K perturbation (each diagonal entry of D changes by O(1/p)). The spectral radius can change by at most the operator norm of the perturbation, which is O(1/p). So:

    rho(1/p) <= rho(0) + O(1/p) = (1 - C/K^2) + O(1/p)

For K >> p^{1/2}, the C/K^2 term dominates the O(1/p) correction, and rho(1/p) < 1 - c/K^2. But for K ~ p^{1/2}, the two terms compete, and the gap is O(1/p).

**However**, the perturbation analysis misses a key feature: the "+1" phases break a SYMMETRY of P(0). At t = 0, the matrix P(0) has a larger symmetry group (it commutes with certain phase rotations). At t > 0, this symmetry is broken, and the near-eigenvalue of rho(0) may SPLIT, with the perturbed eigenvalue moving INWARD (away from the unit circle).

This is exactly the mechanism of the CDG bootstrap (Section 14 of agent_universal_gap.md): the exact phase condition forces |lambda| = 1/2, and the perturbation error is O(L_2 sqrt(eta)). When eta is small enough that L_2 sqrt(eta) < 1/4, the bootstrap gives |lambda| <= 3/4.

### 3.5. Re-examining the CDG bootstrap for the middle range

From Section 14 of agent_universal_gap.md, the key identity is:

    (2|lambda|)^{L_2} = prod_{j=0}^{L_2-1} |1 + c omega^{3s 2^j / (2p)}| * (1 + error terms)

The CDG identity gives prod |cos(pi b 2^j / p)| = 2^{-L_2} for the UNSHIFTED product. The shifted product involves cos(phi/2 + pi b 2^j / p) with a fixed offset phi/2.

**Claim 3.1.** For ANY phi in R and ANY b != 0 mod p:

    prod_{j=0}^{L_2-1} |cos(phi/2 + pi b 2^j / p)| <= 1

**This is trivially true** since each |cos| <= 1.

**Claim 3.2 (Stronger).** For ANY phi and b:

    prod_{j=0}^{L_2-1} |cos(phi/2 + pi b 2^j / p)| <= 2^{-c * L_2}

for some absolute c > 0.

This claim would give (2|lambda|)^{L_2} <= 2^{L_2} * 2^{-c L_2} = 2^{(1-c)L_2}, so |lambda| <= 2^{-c} < 1, a universal constant gap!

**Is Claim 3.2 true?** The CDG identity gives the product = 2^{-L_2} when phi = 0. For phi != 0, the product can be larger (the shift can align all cosines to be near 1). The WORST CASE is when phi/2 + pi b 2^j / p is near 0 for all j, which requires all the points b 2^j / p to be near -phi/(2 pi) mod 1. This is impossible unless the <2>-orbit of b/p is concentrated near a single point on the circle.

**When L_2 is large (L_2 >> sqrt(p)):** The <2>-orbit is equidistributed, so the product is approximately 2^{-L_2/2} (the Jensen bound from averaging log|cos| ~ -log 2 / 2 over the uniform measure).

**When L_2 is small:** The <2>-orbit has few elements. For L_2 = 2: the product is |cos(phi/2 + pi b/p)| * |cos(phi/2 + 2pi b/p)|. This can be as large as ~1 when both arguments are near 0 (i.e., b ~ 0 and phi ~ 0). But b != 0, so the minimum "displacement" is 1/p. For b = 1: the product is ~ |cos(phi/2 + pi/p)| * |cos(phi/2 + 2pi/p)|. Setting phi = -3pi/p to make both arguments equal to pi/p and pi/p... actually phi/2 + pi/p = -3pi/(2p) + pi/p = -pi/(2p) and phi/2 + 2pi/p = -3pi/(2p) + 2pi/p = pi/(2p). So the product is |cos(-pi/(2p))| * |cos(pi/(2p))| = cos^2(pi/(2p)) ~ 1 - pi^2/(4p^2).

So for L_2 = 2, b = 1: the product is ~ 1 - pi^2/(4p^2), which is very close to 1. This gives (2|lambda|)^2 ~ 4(1 - pi^2/(4p^2)), so |lambda| ~ 1 - pi^2/(16p^2). This is a gap of order 1/p^2 -- even worse than the 1/p from L-V!

**Conclusion:** Claim 3.2 is FALSE for small L_2. The shifted CDG product can be very close to 1 when L_2 is small and the orbit clusters near 0.

### 3.6. Rescue: using ALL L_2 * m = K shifted CDG products

The single-coset CDG product gives a weak bound when L_2 is small. But we have m = K/L cosets, each with its own CDG product. Can the PRODUCT over all cosets give a stronger bound?

From the multi-coset constraint (Section 2.6):

    (2|lambda|)^{m * L_2} <= prod_{i=0}^{m-1} prod_{j=0}^{L_2-1} |1 + c_i omega^{...}|

Wait, this isn't quite right -- the eigenvalue lambda is the SAME for all cosets, but each coset gives an independent product equation. Specifically, the CDG product along each <2>-chain within a coset gives:

    (2|lambda|)^{L_2} = prod_j |1 + c_i omega^{theta_{ij}}|     (for each coset i)

These must hold SIMULTANEOUSLY. Taking the product over i:

    (2|lambda|)^{K} = prod_{i,j} |1 + c_i omega^{theta_{ij}}|

The right side is a product of K terms. By AM-GM:

    (1/K) sum_{i,j} log|1 + c_i omega^{theta_{ij}}| = L_2 * log(2|lambda|)

For the average to equal log(2|lambda|), at least one term must be <= log(2|lambda|). If most terms have log|1 + c_i omega^{theta}| ~ log 2 * cos^2(theta/2) (which equals log 2 when theta = 0), then the average is at most log 2, giving |lambda| <= 1.

This is trivially true and useless. The issue is that each |1 + c omega^theta| <= 2 with equality iff theta = 0 and c = 1, and the average of log(|1 + c omega^theta|) over uniformly distributed theta is exactly 0 (since the geometric mean of |1 + e^{i theta}| over theta in [0, 2pi) is 1). So:

- When the orbit phases are equidistributed: average = 0, so (2|lambda|)^K = e^{K * 0} = 1, giving |lambda| = 1/2. This recovers the exact CDG result!

- When the orbit phases cluster near 0: average > 0, and (2|lambda|)^K > 1, which is trivially compatible with |lambda| < 1.

The equidistributed case gives |lambda| = 1/2, but the clustered case gives no useful bound.

**HOWEVER**, the orbit phases are NOT arbitrary -- they are determined by the orbit structure. The phases theta_{ij} = pi r_0 h_{ij} / p where h_{ij} = 2^j * 3^i (schematically) ranges over H. The question reduces to: how well-distributed is the set {r_0 h : h in H} in F_p for the worst-case r_0?

For r_0 = 1: the set is H itself. When K < sqrt(p), H can cluster near 0 in Z/pZ (e.g., if H = <2> and L_2 = 10, then H = {1, 2, 4, 8, 16, 32, 64, 128, 256, 512} which is indeed clustered near 0 for p >> 512).

---

## 4. Approach D: Compactness over Orbit Structures + Minimum t

### 4.1. The key decomposition

For each prime p in the middle range, the orbit O of size K has a Cayley graph structure determined by how 2 and 3 act on O. This structure is an element of a finite set (for fixed K). The transfer matrix is then a function of the single parameter t = r_0/p.

**For fixed K**: rho(t) < 1 for all t in (0,1) (Combined Theorem), and by compactness, sup_{t in [delta, 1-delta]} rho(t) < 1 for any delta > 0. The issue is at t -> 0 and t -> 1.

**At t = 1/p (the actual parameter):** The gap is at least gap(0) * (1 - O(1/(p * gap(0)^2))) by regular perturbation theory. Since gap(0) ~ C/K^2 and K < p^{1/2+eps}, we get:

    gap(1/p) >= (C/K^2)(1 - O(K^2/p)) ~ C/K^2

for p large relative to K^2. Since K^2 < p^{1+2eps}, the correction is O(p^{2eps}) which diverges... This doesn't work naively.

### 4.2. A refined perturbation

Let lambda_0 be the second-largest eigenvalue of P(0) (the unphased transfer matrix). We have |lambda_0| = 1 - gap(0) where gap(0) depends on the Cayley graph structure.

**Key observation:** gap(0) is NOT O(1/K^2) in general. For the specific Cayley graph <2,3> acting on itself via left multiplication, the spectral gap depends on the generators.

For a cyclic group Z/KZ with generators g_1 = 2 and g_2 = 3/2 (in the group Z/KZ), the spectral gap of the random walk (1/2)(delta_{x+g_1} + delta_{x+g_2}) is:

    gap = 1 - (1/2)|e^{2pi i g_1/K} + e^{2pi i g_2/K}| = 1 - |cos(pi(g_1 - g_2)/K)|

For the Collatz walk on H/<3> (the inter-coset walk, which is a cycle of length m), both branches go to the same coset, so there is NO randomness at the inter-coset level. The inter-coset walk is deterministic with gap 0!

The spectral gap comes ENTIRELY from the intra-coset dynamics. Within each <3>-coset of size L, the T_1 branch shifts by ×3 (a cyclic shift) while T_0 doesn't shift. The effective intra-coset walk is (1/2)(I + cyclic shift on Z/LZ), which has spectral gap:

    gap_intra = 1 - cos(2pi/L) ~ 2pi^2/L^2  for large L

Combined with the deterministic inter-coset dynamics, the total gap is:

    gap(0) = 1 - cos(2pi/L) ~ 2pi^2/L^2

Actually this isn't right either -- at t = 0, we have P(0) = (1/2)(Pi_{2^{-1}} + Pi_{3/2}). This averages two permutations. The eigenvalues of P(0) are (1/2)(mu_1 + mu_2) where mu_1 are eigenvalues of Pi_{2^{-1}} and mu_2 of Pi_{3/2}, but only when these commute, which they DON'T in general.

### 4.3. Direct eigenvalue computation for P(0)

P(0) = (1/2)(Pi_alpha + Pi_beta) where alpha = 2^{-1} and beta = 3 * 2^{-1} in F_p. These are permutations of the orbit O = r_0 H.

The matrix P(0) is the transition matrix of the random walk on the Cayley graph Cay(H, {alpha, beta}) = Cay(H, {2^{-1}, 3/2}) (viewing H as a group with these generators acting by multiplication).

Actually, H = <2,3> is NOT necessarily abelian as a subgroup of F_p*. Wait -- F_p* IS abelian (it's cyclic). So H is always a cyclic group. And the Cayley graph of a cyclic group with two generators is always the same: a cycle with two different "step sizes."

Let H = Z/KZ (identified with a cyclic subgroup of F_p*). The generators are alpha = 2^{-1} (step size a) and beta = 3/2 (step size b), where a, b are the positions of 2^{-1} and 3/2 in Z/KZ.

The eigenvalues of P(0) on Z/KZ are:

    lambda_k = (1/2)(omega_K^{ak} + omega_K^{bk})    for k = 0, ..., K-1

where omega_K = e^{2pi i / K}. The magnitude:

    |lambda_k| = (1/2)|e^{2pi i ak/K} + e^{2pi i bk/K}| = |cos(pi(a-b)k/K)|

The second-largest is at k = 1: |lambda_1| = |cos(pi(a-b)/K)|.

Now, a - b = (position of 2^{-1}) - (position of 3/2) in H. Since 2^{-1} * (3/2)^{-1} = 2^{-1} * 2/3 = 1/3 = 3^{-1}, the difference a - b corresponds to the position of 3^{-1} in H. If we identify H = <2,3> with Z/KZ, then position of 3^{-1} is K - L (where L = ord_p(3) divides K).

Actually, this requires more care. Let g be a generator of H = Z/KZ. Then 2 = g^s and 3 = g^t for some s, t with gcd(s, t, K) = 1 (since <2,3> = H). The element 2^{-1} = g^{-s} and 3/2 = g^{t-s}. So a = -s mod K and b = t - s mod K. Thus a - b = -t mod K. And:

    |lambda_1| = |cos(pi t / K)|

where t is the position of 3 in the cyclic group H, i.e., t = ord_H(g) such that g^t = 3. Since <3> is a subgroup of H of order L, the position of 3 in H is K/L (up to a unit in Z/KZ).

Wait: in Z/KZ, the element 3 corresponds to g^t. The subgroup <3> = <g^t> has order K/gcd(t,K). Since <3> has order L, we have K/gcd(t,K) = L, so gcd(t,K) = K/L. Thus t is a multiple of K/L.

The simplest case: t = K/L. Then:

    |lambda_1| = |cos(pi * K / (L * K))| = |cos(pi / L)|

So |lambda_1| = cos(pi/L) and gap(0) = 1 - cos(pi/L) = 2 sin^2(pi/(2L)).

**This confirms the result from Section 7.2 of agent_universal_gap.md:** For the unphased matrix, the spectral gap is 1 - cos(pi/L) ~ pi^2/(2L^2).

### 4.4. The phased gap

At t = 1/p, the gap changes from gap(0) to gap(1/p). From perturbation theory (Weyl's inequality for the eigenvalues of Hermitian parts):

    |rho(1/p) - rho(0)| <= ||P(1/p) - P(0)||_{op}

The operator norm of the perturbation:

    ||P(1/p) - P(0)||_{op} = (1/2)||D(1/p) Pi_beta - Pi_beta||_{op} = (1/2) max_j |omega^{pi r_0 h_j / p} - 1|

For j such that h_j is the largest element of H, |omega^{pi r_0 h_j / p} - 1| ~ 2 pi r_0 h_j / (2p) = pi r_0 h_j / p. For r_0 = 1 and h_j = max(H), this is pi max(H) / p.

The maximum element of H in Z/pZ can be as large as p-1. So the perturbation can be O(1), not O(1/p)!

**This means the perturbation theory fails completely.** The phase matrix D is NOT a small perturbation of the identity when the orbit elements are large.

### 4.5. When perturbation theory works

Perturbation theory works when ALL orbit elements satisfy r_0 h_j << p, i.e., when the orbit is "small" in Z (before wrapping mod p). This happens when r_0 is small and H generates only small numbers in Z.

For H = <2,3> with K small, the elements of H (as integers before reduction mod p) are {2^a 3^b : 0 <= a < L_2, 0 <= b < L, ...}. The maximum such element is at most 2^{L_2} * 3^L. For L_2, L <= p^{1/2+eps}, this maximum is at most 3^{p^{1/2+eps}}, which is MUCH larger than p for large p. So most elements of H "wrap around" many times mod p, and the orbit is NOT concentrated near 0.

**The only way the orbit concentrates near 0** is if there are many cancellations in the reduction mod p. By the Gauss sum bound, the number of elements of H in any interval of size R is at most R K/p + sqrt(p). For R = sqrt(p) and K < sqrt(p): this is at most K + sqrt(p) ~ 2 sqrt(p). So at most 2sqrt(p) elements of the K-element orbit are "near 0" (within sqrt(p) of 0).

For K >> sqrt(p), most elements are NOT near 0, and the phases are large. But we are in the case K <= p^{1/2+eps}, so K and sqrt(p) are comparable. About half the orbit could be near 0.

### 4.6. A new strategy: the two regimes within the middle range

**Regime M1: L >= L_0 (order of 3 is at least a constant L_0).**

The unphased gap is gap(0) = 1 - cos(pi/L) >= 1 - cos(pi/L_0) > 0. We need to show the phased gap gap(t) remains positive. Since the Combined Theorem guarantees gap(t) > 0 for each t, and the set of primes with a given (L_2, L) pair is FINITE (since p | lcm of things), compactness gives a uniform gap for each (L_2, L) pair. As there are finitely many pairs with L_2, L <= L_0 (a bounded number), the gap over all such primes is bounded below.

Wait -- we need L_2 and L to be small, but K = |<2,3>| to be in the middle range. Since K = |<2,3>| divides (p-1) and depends on L_2, L, and the interaction between <2> and <3>, the constraint is more subtle.

**Key number-theoretic fact:** For FIXED (L_2, L), the set of primes p with ord_p(2) = L_2 and ord_p(3) = L is finite.

*Proof:* p | (2^{L_2} - 1) and p | (3^L - 1). So p | gcd(2^{L_2} - 1, 3^L - 1), which is a fixed integer. The number of prime divisors of a fixed integer is finite.

**Therefore:** For each fixed pair (L_2, L), there are finitely many primes, and for each such prime, the Combined Theorem gives a positive gap. The minimum gap over these finitely many primes is positive.

The question is: as L_2 and L grow (but K = |<2,3>| stays in the middle range), can the gap approach 0?

**Regime M2: L and L_2 both grow, K = |<2,3>| <= p^{1/2+eps}.**

This is the truly hard case. Both orders grow with p, meaning we cannot use the "finitely many primes" argument for any fixed (L_2, L).

However, if BOTH L_2 and L grow, then K >= max(L_2, L), and if K <= p^{1/2+eps}, then L_2, L <= p^{1/2+eps}. The gap(0) from the unphased matrix is 1 - cos(pi/L) ~ pi^2/(2L^2) >= pi^2/(2 p^{1+2eps}).

This is a gap of ~ 1/p, matching L-V. To improve it to a constant gap requires the "+1" phases to HELP (not just not hurt).

---

## 5. The Core Argument: Phase Rigidity from CDG + Finiteness

### 5.1. A novel decomposition of the problem

We split the middle range K in [K_0, p^{1/2+eps}] into two sub-cases based on a parameter N_0 (to be optimized):

**Case I: K <= N_0 (K is absolutely bounded).**

Finitely many primes per value of K. Compactness gives gap >= c(N_0) > 0.

**Case II: N_0 < K <= p^{1/2+eps}.**

Here K is large but subexponential in p. In this regime:

(a) L_2 = ord_p(2) satisfies K >= L_2 (trivially), and L_2 >= K/L (since K = L_2 * L / gcd(L_2, L) ... no, K = |<2,3>| which for the cyclic group F_p* satisfies K = lcm(L_2, L)). So K = lcm(L_2, L), and L_2, L <= K <= p^{1/2+eps}.

(b) The CDG product identity holds: prod_{j=0}^{L_2-1} cos(pi b 2^j / p) = +/- 2^{-L_2}.

(c) The approximate phase condition (from |lambda|^2 >= 1 - eta) forces a_{3s} ~ c omega^{s/2} a_s with L^2 error 4 eta (Proposition 4.4 of agent_sum_product.md).

(d) Substituting into the eigenvalue equation and iterating L_2 times, we get the bootstrapped bound from Section 14 of agent_universal_gap.md:

    (2|lambda|)^{L_2} (1 + O(L_2 sqrt(eta)))^{-1} <= prod_{j} |1 + c omega^{3s 2^j / (2p)}| = prod |1 + c e^{i alpha_j}|

where alpha_j = 2pi * 3s * 2^{j-1} / p.

### 5.2. Bounding the shifted product from above

**Proposition 5.1 (Shifted CDG upper bound).** For any c with |c| = 1 and any nonzero b in F_p:

    prod_{j=0}^{L_2-1} |1 + c e^{2pi i b 2^j / p}| = 2^{L_2} prod_{j=0}^{L_2-1} |cos(arg(c)/2 + pi b 2^j / p)|

The right side involves the shifted cosine product. Define:

    F(phi, b) = prod_{j=0}^{L_2-1} |cos(phi + pi b 2^j / p)|

where phi = arg(c)/2.

By AM-GM on log:

    log F(phi, b) = sum_j log|cos(phi + pi b 2^j / p)|

Now, the points {b 2^j / p mod 1 : j = 0, ..., L_2-1} form the <2>-orbit of b/p on R/Z. This orbit has L_2 elements.

**Case II.a: L_2 >= L_2^* (for a threshold L_2^* to be chosen).**

If L_2 >= L_2^*, the <2>-orbit of b/p has at least L_2^* elements on R/Z. Even without equidistribution, we can use the following:

**Lemma 5.2 (Product bound from orbit size).** For any L_2 points alpha_0, ..., alpha_{L_2-1} on R/Z with the property that alpha_{j+1} = 2 alpha_j mod 1, and any phi in R:

    prod_j |cos(phi + pi alpha_j)| <= (cos(pi / (2 L_2)))^{L_2} <= exp(-pi^2 / (8 L_2))

Wait, this is false -- the product of |cos| values can be close to 1 when all points cluster near a single value.

Let me reconsider. The doubling map alpha -> 2 alpha mod 1 is ergodic (with respect to Lebesgue measure), and for a PERIODIC orbit of size L_2, the points are NOT arbitrary -- they satisfy 2^{L_2} alpha_0 = alpha_0 mod 1, i.e., alpha_0 is a rational p/(2^{L_2} - 1) or more generally b/p with 2^{L_2} = 1 mod p.

For such a periodic orbit, the CDG identity gives the EXACT product without the shift:

    prod_j cos(pi alpha_j) = +/- 2^{-L_2}    where alpha_j = b 2^j / p

For the shifted product, we use the identity:

    prod_j cos(phi + pi alpha_j) = Re[e^{i L_2 phi} prod_j (1/2)(1 + e^{2i(phi + pi alpha_j - phi)})... ]

Actually, let us use a cleaner approach. Define:

    G(phi) = prod_{j=0}^{L_2-1} cos(phi + pi alpha_j)

This is a trigonometric polynomial in phi of degree L_2 (after expanding the product). Its maximum over phi can be bounded using the CDG identity.

**Proposition 5.3.** |G(phi)| <= 2^{-L_2} * max_phi prod_j |1 + e^{2i(phi + pi alpha_j)}| / prod |1 + e^{2i pi alpha_j}|...

This is getting circular. Let me try a different approach.

### 5.3. The key inequality via Jensen over the orbit

Define the weight function w(s) = |a_s|^2 / ||f||^2 (a probability measure on O). The near-eigenvalue condition gives:

    sum_s w(s) log|1 + c omega^{3s/(2p)}| >= L_2 log(2|lambda|) - C L_2 sqrt(eta)

(from iterating the eigenvalue equation L_2 times and using the approximate phase condition).

Now, the CDG identity in logarithmic form gives:

    sum_{j=0}^{L_2-1} log|cos(pi b 2^j / p)| = -L_2 log 2

for any nonzero b. This means:

    sum_j log|1 + omega^{b 2^j}| = sum_j log(2|cos(pi b 2^j / p)|) = L_2 log 2 + sum_j log|cos(pi b 2^j / p)| = L_2 log 2 - L_2 log 2 = 0

So **the average of log|1 + omega^{b 2^j}| over a full <2>-orbit is exactly 0**, regardless of b.

This is a key identity: for ANY nonzero b, summing log|1 + omega^{b 2^j}| over j = 0, ..., L_2-1 gives exactly 0.

### 5.4. Applying the key identity

From the eigenvalue equation iteration, for any mode s in the orbit O:

    log((2|lambda|)^{L_2}) = sum_{j=0}^{L_2-1} log|1 + c omega^{3s 2^j / (2p)}| + O(L_2 sqrt(eta))

But the sum on the right, by the CDG identity (since 3s/(2p) is nonzero), is exactly 0 when c = 1:

    sum_j log|1 + omega^{3s 2^j / (2p)}| = ...

Wait, we need c in the formula. We have |1 + c omega^{theta}| where c is a unit complex number. When c = 1: |1 + omega^theta| = 2|cos(pi theta)|, and sum log = 0 by CDG. When c = omega^phi (a general phase): |1 + c omega^theta| = |1 + omega^{theta + phi}| = 2|cos(pi(theta + phi))|. The sum becomes:

    sum_j log(2|cos(pi(3s 2^j / (2p) + phi'))|) = L_2 log 2 + sum_j log|cos(pi alpha_j + phi')|

where alpha_j = 3s 2^{j} / (2p) mod 1 and phi' = arg(c) / (2pi).

This is the SHIFTED CDG product. It is NOT generally zero.

However, we can compute:

    sum_j log|cos(pi alpha_j + phi')| = sum_j log|cos(pi(alpha_j + phi'))|

For the AVERAGE over phi' (uniform on [0,1)):

    integral_0^1 sum_j log|cos(pi(alpha_j + phi'))| dphi' = L_2 * integral_0^1 log|cos(pi x)| dx = L_2 * (-log 2)

(using the classical integral). So the average of the shifted CDG product over phi' is -L_2 log 2, the same as the unshifted case.

This means: over all possible phase shifts c, the AVERAGE of the shifted product gives (2|lambda|)^{L_2} = 2^{L_2} * 2^{-L_2} = 1, hence |lambda| = 1/2. But the MAXIMUM over c could be larger.

### 5.5. Maximum of the shifted CDG product

**Proposition 5.4.** For any periodic orbit {alpha_j} under the doubling map (with period L_2):

    max_phi prod_j |cos(pi(alpha_j + phi))| <= (cos(pi / (L_2 + 1)))^{L_2}  ???

This proposed bound is likely false. Let me think about what the correct bound is.

For L_2 = 1: max_phi |cos(pi(alpha + phi))| = 1 (set phi = -alpha). Product = 1.

For L_2 = 2: orbit {alpha, 2alpha mod 1}. max_phi |cos(pi(alpha + phi))| * |cos(pi(2alpha + phi))|. This is maximized when phi is chosen to make both arguments as close to 0 as possible. The optimal phi satisfies pi(alpha + phi) + pi(2alpha + phi) = 0, i.e., phi = -3alpha/2. Then the two arguments are -alpha/2 and alpha/2. Product = cos^2(pi alpha / 2).

For small alpha (alpha ~ 0): product ~ 1 - (pi alpha)^2 / 4. For alpha = 1/2: product = cos^2(pi/4) = 1/2.

So the maximum shifted product depends on how the orbit is distributed. For orbits clustered near a single point (alpha ~ 0), the product is close to 1.

**The key constraint:** The orbit {alpha, 2alpha, 4alpha, ..., 2^{L_2-1} alpha} mod 1 satisfies alpha = b/p for some integer b, and 2^{L_2} alpha = alpha mod 1 (periodicity). The clustering near 0 occurs when b/p is small, i.e., b << p.

For b = 1: alpha_j = 2^j / p, and the orbit consists of {1/p, 2/p, 4/p, ..., 2^{L_2-1}/p}. These are all small when L_2 < log_2(p) (which it is for L_2 < p^{1/2+eps}). So the ENTIRE orbit clusters near 0, and the shifted product is close to 1.

This confirms: for the orbit of b = 1 (the "worst case"), the CDG shifted product provides essentially no bound on |lambda|.

### 5.6. Resolution: the orbit of b = 1 requires special treatment

When b = 1, the mode r = 1 corresponds to the "smallest" nonzero character. The orbit O contains r = 1, and the CDG product along this orbit's <2>-chain gives almost no contraction.

**But the eigenvector has support on the FULL orbit O, not just the mode r = 1.** The orbit has K modes, and for K > 1, many modes have b = r_0 h_j much larger than 1. Specifically, for h_j such that r_0 h_j >> p^{1/2} (in Z/pZ), the CDG product along that mode's <2>-chain DOES give contraction.

The question is: what fraction of the orbit has "large" modes (|r_0 h_j| > p^{1/2} in Z/pZ)?

By the Gauss sum bound: the number of elements of H in an arc of size sqrt(p) near 0 is at most sqrt(p) * K / p + sqrt(p) ~ sqrt(p) (when K < sqrt(p)). So at most O(sqrt(p)) modes out of K are "small."

For K >> sqrt(p) (but K < p^{1/2+eps}): the fraction of small modes is sqrt(p)/K, which is less than 1. There are many large modes.

For K ~ sqrt(p): the fraction of small modes could be O(1). Most modes could be small.

For K < sqrt(p): the ENTIRE orbit could be "small" (all elements of H reduced mod p could be < p^{1/2}).

**This is the crux of the problem.** When K < sqrt(p), the Gauss sum bound says the orbit could fit entirely within an arc of size sqrt(p), giving no equidistribution.

---

## 6. A New Ingredient: The "+1" Phase Provides Non-Perturbative Contraction

### 6.1. Returning to the full eigenvalue equation

We have been trying to bound |lambda| using the CDG product along individual chains. This approach fails for "small" modes. Let us instead look at the FULL eigenvalue equation on the orbit.

On orbit O of size K, the transfer matrix P = (1/2)(Pi_alpha + D Pi_beta) is a K x K matrix. Its eigenvalues are determined by the phases D = diag(omega^{r_j gamma}) and the permutations Pi_alpha, Pi_beta.

**The key observation** (from Section 8.3 of agent_universal_gap.md): Both Pi_alpha (multiplication by 2^{-1}) and Pi_beta (multiplication by 3/2) map each <3>-coset to the SAME target coset. The only difference between the two branches is an intra-coset shift of +1 (in the <3>-coset index).

This means the transfer matrix P can be written in the (coset, intra-coset) basis as:

    P = (1/2) sigma_coset tensor (I_intra + D_intra Shift_intra)

where:
- sigma_coset is a permutation of the m cosets
- I_intra is the identity on the L-element coset
- Shift_intra is the cyclic shift by 1 position (multiplication by 3)
- D_intra is a diagonal phase matrix depending on the "+1" translation

**Actually this isn't quite right** because the phase D depends on the FULL mode (both coset and intra-coset position), and the inter-coset permutation may also shift the intra-coset position (by the tau_i amounts from Section 12.6 of agent_universal_gap.md).

Let me write it more carefully. The transfer matrix acts on mode s in O by:

    (Pa)_s = (1/2) a_{2s} + (1/2) omega^{s gamma} a_{(3/2) 2 s / 3 ... }

Hmm, let me go back to basics.

The eigenvalue equation (**) is:

    a_s + omega^s a_{3s} = 2 lambda a_{2s}

This says: a_{2s} is determined by a_s and a_{3s}. The multiplication by 3 acts WITHIN the <3>-coset, while multiplication by 2 maps between cosets.

### 6.2. The intra-coset operator on a single <3>-coset

Fix a <3>-coset C = {r, 3r, 9r, ..., 3^{L-1} r}. The restriction of the eigenvalue equation to this coset couples C to the coset 2C (via the a_{2s} terms). But within C, the terms a_s and a_{3s} = a_{sigma(s)} (where sigma is the cyclic shift within C) are both in C.

Define the vector u = (a_r, a_{3r}, ..., a_{3^{L-1} r}) in C^L. The eigenvalue equation at s = 3^k r gives:

    a_{3^k r} + omega^{3^k r} a_{3^{k+1} r} = 2 lambda a_{2 * 3^k r}

In vector form: u + D_C S u = 2 lambda v

where:
- S is the cyclic shift: (Su)_k = u_{k+1 mod L}
- D_C = diag(omega^{3^k r} : k = 0, ..., L-1)
- v = (a_{2r}, a_{6r}, ..., a_{2 * 3^{L-1} r}) is the vector of coefficients on the coset 2C.

So: v = (1/(2lambda)) (I + D_C S) u.

The operator T_C = (1/(2lambda))(I + D_C S) maps from coset C to coset 2C.

### 6.3. The chain of inter-coset operators

Following the chain C_0 -> C_1 = 2C_0 -> C_2 = 2C_1 -> ... -> C_{m-1} -> C_m = C_0:

    v_i = T_{C_i} u_i

where u_i is the coefficient vector on coset C_i and v_i = u_{i+1} (the vector on the next coset, with appropriate relabeling).

After m steps (one full cycle through all cosets):

    u_0 = T_{C_{m-1}} ... T_{C_1} T_{C_0} u_0 = (prod_{i=0}^{m-1} T_{C_i}) u_0

So u_0 is an eigenvector of the product M_cycle = prod T_{C_i} with eigenvalue 1.

**But** the eigenvalue of M_cycle depends on lambda (since each T_{C_i} = (I + D_{C_i} S) / (2 lambda)):

    M_cycle = (2lambda)^{-m} prod_{i=0}^{m-1} (I + D_{C_i} S)

The condition M_cycle u_0 = u_0 gives:

    (2lambda)^m u_0 = prod_{i=0}^{m-1} (I + D_{C_i} S) u_0

Taking norms: |2lambda|^m ||u_0|| = ||prod(I + D_{C_i} S) u_0||.

### 6.4. Bounding the product of intra-coset operators

Each operator (I + D_{C_i} S) on C^L has the structure:

    (I + D_i S)_{k,k} = 1,  (I + D_i S)_{k, k-1 mod L} = omega^{3^{k} r_i}

The eigenvalues of D_i S (on the <3>-coset C_i) are {omega_L^j * prod_k omega^{3^k r_i / L} : j = 0, ..., L-1}. Actually, by Section I.1 of the coupling/entropy analysis, the eigenvalues of D_i S on a <3>-cycle of length L are:

    mu_j = omega_L^j * (product of phases around the cycle)^{1/L}

The product of phases is prod_{k=0}^{L-1} omega^{3^k r_i} = omega^{r_i (3^L - 1) / (3-1)} = omega^{r_i (3^L - 1) / 2}.

Since 3^L = 1 mod p, (3^L - 1)/2 = 0 mod p (as an element of F_p). So the product is omega^0 = 1. Therefore the eigenvalues of D_i S are exactly {omega_L^j : j = 0, ..., L-1}.

**Key result:** The eigenvalues of I + D_i S are {1 + omega_L^j : j = 0, ..., L-1}, with magnitudes |1 + omega_L^j| = 2|cos(pi j/L)|.

**These eigenvalues are the SAME for all cosets i!** (The diagonal phases D_i vary between cosets, but the spectrum of D_i S is always the L-th roots of unity, because the product around the cycle is always 1.)

### 6.5. Diagonalizing each factor

Although the eigenvalues of D_i S are the same for all i, the EIGENVECTORS differ (because D_i differs). So the product prod(I + D_i S) does NOT simply have eigenvalues prod(1 + omega_L^j) -- the factors don't commute.

However, in the "Fourier" basis that diagonalizes one particular D_i S (say D_0 S), the other factors become non-diagonal. The product involves "rotation" between different Fourier modes at each step.

**Proposition 6.1 (Operator norm bound for the product).**

    ||prod_{i=0}^{m-1} (I + D_{C_i} S)||_{op} <= prod_{i=0}^{m-1} ||(I + D_{C_i} S)||_{op} = prod_{i=0}^{m-1} max_j |1 + omega_L^j| = 2^m

The operator norm of each factor is max_j |1 + omega_L^j| = |1 + 1| = 2 (at j = 0). So the product norm is at most 2^m.

This gives (2|lambda|)^m <= 2^m, i.e., |lambda| <= 1. Useless.

**The issue:** The operator norm bound ignores the non-commutativity of the factors. The actual product norm can be much smaller than the product of norms.

### 6.6. Non-commutative cancellation

The key insight is that the eigenvectors of different D_i S are MISALIGNED. The j=0 mode (with eigenvalue 2) of D_0 S is a specific vector in C^L that depends on the phases in D_0. The j=0 mode of D_1 S is a DIFFERENT vector. When we multiply (I + D_1 S)(I + D_0 S), the j=0 component of D_0 S gets projected onto all components of D_1 S, including the j != 0 components which have |1 + omega_L^j| < 2.

This is the "inter-coset expansion" mechanism identified in Section 8 of agent_universal_gap.md: the phase mismatch between consecutive cosets causes the "bad" mode (j=0) to partially scatter into "good" modes (j != 0), creating contraction.

**Proposition 6.2 (Non-commutative contraction).** Let V_i be the j=0 eigenvector of D_i S (the "worst" mode for coset i). The overlap between V_i and V_{i+1} satisfies:

    |<V_i, V_{i+1}>|^2 = (1/L) |sum_{k=0}^{L-1} omega^{(r_{i+1} - r_i) 3^k}|^2

where r_i, r_{i+1} are representatives of consecutive cosets.

**Computation:** V_i is the uniform vector on coset C_i in the D_i S-Fourier basis. Specifically, the j=0 eigenvector of D_i S is proportional to:

    (V_i)_k = prod_{l=0}^{k-1} (omega^{3^l r_i})^{-1} = omega^{-r_i (3^k - 1) / (3-1)} = omega^{-r_i (3^k - 1)/2}

(This is the vector that D_i S maps to itself times 1.)

The overlap:

    <V_i, V_{i+1}> = (1/L) sum_k (V_i)_k^* (V_{i+1})_k
                    = (1/L) sum_k omega^{r_i (3^k - 1)/2} omega^{-r_{i+1}(3^k - 1)/2}
                    = (1/L) sum_k omega^{(r_i - r_{i+1})(3^k - 1)/2}
                    = (1/L) omega^{-(r_i - r_{i+1})/2} sum_k omega^{(r_i - r_{i+1}) 3^k / 2}

This is a CHARACTER SUM over the <3>-orbit:

    |<V_i, V_{i+1}>| = (1/L) |sum_{k=0}^{L-1} omega^{(r_i - r_{i+1}) 3^k / 2}|

**When L >= sqrt(p):** The Gauss sum bound gives |sum| <= sqrt(p), so the overlap is at most sqrt(p) / L <= p^{-epsilon/2} -> 0. The scattering is almost complete.

**When L < sqrt(p):** The Gauss sum bound gives |sum| <= sqrt(p), but L < sqrt(p), so the overlap is bounded by sqrt(p)/L > 1. The bound is trivial!

### 6.7. The overlap for small L

When L < sqrt(p), the Gauss sum bound is useless for bounding the overlap. However, the sum is:

    S = sum_{k=0}^{L-1} omega^{Delta 3^k / 2}

where Delta = r_i - r_{i+1}. Since r_{i+1} = 2 r_i (the cosets are related by ×2), Delta = r_i - 2r_i = -r_i. So:

    S = sum_{k=0}^{L-1} omega^{-r_i 3^k / 2} = sum_{k=0}^{L-1} e^{-2pi i r_i 3^k / (2p)}

For r_i small (|r_i| << p): each term is e^{-2pi i * small} ~ 1 - 2pi i r_i 3^k / (2p). So:

    S ~ L - (2pi i r_i / (2p)) sum_k 3^k = L - (pi i r_i / p)(3^L - 1)/2

Since 3^L = 1 mod p, (3^L - 1)/2 = 0 mod p (in F_p). So the first-order term vanishes, and:

    S = L + O(r_i^2 / p^2 * L * 3^{2L})

Wait, this can't be right -- (3^L - 1)/2 = 0 in F_p means (3^L - 1)/2 is a multiple of p. Let's be more careful. As an INTEGER, (3^L - 1)/2 = p * Q for some integer Q. So:

    sum_k 3^k = (3^L - 1)/2 = p Q

    S = sum_{k=0}^{L-1} e^{-2pi i r_i 3^k / (2p)}

Each term: e^{-2pi i r_i 3^k / (2p)} = e^{-i pi r_i 3^k / p}.

For r_i = 1: the phases are pi 3^k / p for k = 0, ..., L-1. These are L points on R/2Z. If L is small and 3^k < p (which holds when L < log_3(p) ~ 0.63 log_2(p) ~ 0.63 * ... so when L < log_3(p), all 3^k are distinct integers < p), then the points are pi * {1, 3, 9, 27, ...} / p.

For L small (say L <= 10) and p large: the points {3^k / p} for k = 0, ..., L-1 are all near 0 (since 3^{L-1} < 3^{10} ~ 59000 << p for large p). So all terms in S are near 1, and:

    S ~ L * (1 - O(3^{2L} / p^2)) ~ L

    |<V_i, V_{i+1}>| ~ |S|/L ~ 1

**The overlap is nearly 1!** This means the "bad" mode j=0 barely scatters when passing between cosets. The non-commutative contraction is negligible.

### 6.8. Conclusion on the non-commutative approach

For the case where BOTH L = ord_p(3) < sqrt(p) and L_2 = ord_p(2) < sqrt(p), the three main mechanisms all fail:

1. **CDG shifted product:** Close to 1 for small modes (b/p near 0), giving no contraction.
2. **Gauss equidistribution:** Requires the orbit to have >= sqrt(p) elements in the relevant subgroup.
3. **Non-commutative inter-coset scattering:** The overlap between consecutive "bad" eigenvectors is near 1 when L < sqrt(p) and the coset representatives are small.

**The gap for these primes is O(1/p) from the Lindenstrauss-Varju bound, and we have been unable to improve it to O(1).**

---

## 7. A New Observation: Counting the Exceptional Primes

### 7.1. Are there infinitely many primes in the middle range?

The middle range consists of primes where K = |<2,3>| < p^{1/2+eps}. This requires ord_p(2) * ord_p(3) / gcd(...) < p^{1/2+eps}, which roughly means both ord_p(2) and ord_p(3) are < p^{1/2+eps}.

**Question:** Are there infinitely many primes p where both ord_p(2) < p^{1/2+eps} and ord_p(3) < p^{1/2+eps}?

**Number-theoretic expectation:** Yes. While for a SINGLE fixed base a, Artin's conjecture says ord_p(a) = p-1 for a positive density of primes, there are also infinitely many p where ord_p(a) is small. Specifically, for any d, the primes p where ord_p(2) = d are those p with p | (2^d - 1). For d ~ sqrt(p), the number 2^d - 1 is enormous, and its prime factors are typically large.

More precisely: the number of primes p <= X with ord_p(2) <= X^{1/2+eps} is at most sum_{d <= X^{1/2+eps}} pi(X; 2^d - 1) where pi(X; n) counts primes p <= X dividing n. This sum is:

    sum_{d=1}^{X^{1/2+eps}} omega(2^d - 1)

where omega(n) is the number of distinct prime factors of n. Since omega(2^d - 1) ~ d / log d (heuristically), this sum is ~ X^{1+2eps} / log X, which gives a density of ~ X^{2eps} / log X. For fixed eps > 0, this is a set of primes with positive (even infinite) density... wait, that can't be right because sum omega(2^d - 1) for d <= D grows much slower.

Actually, let me think more carefully. The primes p with ord_p(2) | d are exactly the primes dividing 2^d - 1. The number of such primes is omega(2^d - 1) <= C d / log d (by the crude bound on the number of prime factors). The primes p with ord_p(2) <= D are among the prime factors of prod_{d=1}^{D} (2^d - 1). The total count of distinct such primes is at most sum_{d=1}^{D} omega(2^d - 1) ~ D^2 / log D.

For D = p^{1/2+eps}: the count is at most p^{1+2eps} / log p, but these are primes up to arbitrarily large p. Since we are asking for primes p where ord_p(2) <= p^{1/2+eps}, this is a condition on p itself. By the Erdos-Murty/Li-Pomerance heuristic, the set of primes with ord_p(2) < p^{1/2+eps} has density 0 (for any fixed eps > 0). But it is an INFINITE set.

**Key point:** There are infinitely many primes in the middle range, so we cannot resolve the problem by finiteness alone (unlike the bounded-K case).

### 7.2. However: combined with finitely many K values

For each FIXED value of K, there are finitely many primes (since p | lcm({2^d - 1 : d | K}, {3^d - 1 : d | K})). So the statement "for fixed K, gap >= c(K) > 0" is trivially true.

The universal gap requires c(K) >= c_0 > 0 for ALL K. From Section 4.3, the unphased gap is gap(0) = 1 - cos(pi/L) where L = ord_p(3). If L grows with p, gap(0) -> 0. But for each fixed L, there are finitely many primes, and gap > 0 for each.

**The real question:** As the pair (L_2, L) ranges over all possible values (with both going to infinity), does the minimum gap over all primes with those orders approach 0?

From the analysis: for fixed (L_2, L), the primes are finite, the gap is positive. For growing (L_2, L), the compactness argument breaks. But:

**Proposition 7.1 (Gap depends only on K and L).** For fixed K = |<2,3>| and L = ord_p(3) (which determines L_2 = ord_p(2) and the Cayley graph structure up to isomorphism), the spectral gap depends on a single real parameter t in (0,1) (or rather, t in {r_0/p : r_0 representative of an orbit}). The function rho(t) is real-analytic in t and satisfies rho(t) < 1 for all t in (0,1).

For fixed (K, L): the number of possible Cayley graph structures is bounded by a function of K alone. For each structure, rho(t) < 1 on (0,1), and by continuity (and the fact that rho(0) < 1 since the unphased walk has a gap), the supremum of rho(t) over t in (0,1) is strictly < 1. So:

    c(K, L) = 1 - sup_{t in (0,1)} rho(t; K, L) > 0

The universal gap is:

    c_0 = inf_{K, L} c(K, L)

**If this infimum is positive, we have the universal gap. If it is 0, the gap fails.**

### 7.3. The behavior of c(K, L) as L -> infinity

From the unphased analysis: c(K, L) >= gap(0) - perturbation error. The gap(0) = 1 - cos(pi/L) ~ pi^2/(2L^2). The perturbation from the phases is at most max_{(i,j)} |D_{ij} - 1|, which for the worst case (smallest modes) is O(max_h h/p) where h ranges over H.

For fixed K and L -> infinity: this means K = lcm(L_2, L) is fixed but L -> infinity. Since K is fixed and L | K, L can only take finitely many values (the divisors of K). So L is bounded by K, and the infimum over L is a minimum over finitely many values. This gives c(K) > 0 for fixed K.

For K -> infinity: c(K) could go to 0. The question is the RATE.

From the explicit formula: gap(0) = 1 - cos(pi/L) where L divides K. For K = L (single coset, no inter-coset structure): gap(0) = 1 - cos(pi/K). This goes to 0 as pi^2/(2K^2).

**But the phased matrix has a LARGER gap than the unphased one** (at least for generic t). The "+1" phases break the symmetry of the unphased walk and can increase the gap. The CDG bootstrap shows that for the "exact" phase condition, |lambda| = 1/2, independent of K. For "near-exact" phases (small t), |lambda| is close to 1/2 with error depending on t.

For t = 1/p (the actual parameter): |lambda| ~ 1/2 + O(K/p) (from the perturbation of the exact phase condition). Since K < p^{1/2+eps}: the error is O(p^{-1/2+eps}), so |lambda| <= 1/2 + o(1), giving a constant gap!

Wait -- is this right? Let me re-examine.

### 7.4. Revisiting the CDG bootstrap for t = 1/p

From Section 14 of agent_universal_gap.md: the exact phase condition forces |lambda| = 1/2. The approximate phase condition (at |lambda|^2 >= 1 - eta) gives error O(L_2 sqrt(eta)) per factor in the CDG product.

The key equation is: (2|lambda|)^{L_2} = prod_j |1 + c omega^{3s 2^j/(2p)}| * (1 + O(L_2 sqrt(eta)))

The CDG identity (for the unshifted product) gives prod_j |cos(pi b 2^j / p)| = 2^{-L_2}. For the shifted product with shift phi = arg(c)/2:

    prod_j |cos(phi + pi b 2^j / p)|

For b = 3s/2 with s in the orbit, and s = r_0 * h for h in H. For the mode s corresponding to the intra-coset uniform mode on the first coset (the "worst" mode): s is such that the shifted product is maximized.

But actually, the eigenvalue equation gives a SEPARATE constraint for EACH mode s in the orbit. Taking the geometric mean over all K modes (as in Section 5.6):

    (2|lambda|)^K = prod_{s in O} prod_{j=0}^{L_2-1} |1 + c_s omega^{3s 2^j/(2p)}| * (1 + O(K * L_2 sqrt(eta)))

Wait, the CDG identity sum over the full orbit gives a product of K * L_2 = K * L_2 terms. But L_2 * m = K (where m = K/L is the number of cosets), so actually we have K^2/L terms total. This is getting complicated.

Let me try a cleaner approach.

### 7.5. The orbit-averaged CDG identity

For each s in O and each j in {0, ..., L_2-1}, we have a phase alpha_{s,j} = 3s 2^j / (2p) mod 1. As (s,j) ranges over O x {0, ..., L_2-1}, the index 3s 2^j / 2 ranges over the set {3h 2^j / 2 * r_0 : h in H, j = 0, ..., L_2-1}. Since 3h 2^j / 2 = h' * 2^{j-1} * 3 where h' = h, and H = <2,3>, this set is essentially r_0 * H * <2> = r_0 * H (since <2> is already in H). So the set of values 3s 2^j / 2 for (s,j) is r_0 * H (with multiplicities).

More precisely: the map (s, j) -> 3s * 2^j / 2 sends (r_0 h, j) to r_0 * 3h * 2^{j-1}. As h ranges over H and j over {0, ..., L_2-1}, the product 3h 2^{j-1} ranges over 3 * H * {2^{-1}, 1, 2, ..., 2^{L_2-2}} = 3 * H (since <2> <= H). Since 3 in H, 3H = H. So the set of values is r_0 * H (with each element appearing L_2 times -- once for each j achieving 3h 2^{j-1} = h').

Actually the counting is: for each h' in H, the number of pairs (h, j) with 3h 2^{j-1} = h' (in F_p*) is exactly... since 3 and 2 generate H, and the map (h,j) -> 3h 2^{j-1} is a group operation, the fiber size is L_2 (the size of the kernel {(h,j) : 3h 2^{j-1} = 1} = {(3^{-1} 2^{1-j}, j) : j}). So each h' in H appears L_2 times.

Therefore:

    sum_{s in O} sum_{j=0}^{L_2-1} log|1 + c omega^{r_0 3s 2^j / (2p)}| = L_2 * sum_{h' in H} log|1 + c omega^{r_0 h' / p}|

(Wait, the factor of 1/(2p) vs 1/p needs tracking. Let me just denote the set of phases as {r_0 h / p : h in H}, which is an orbit of size K in R/Z.)

**The CDG identity for the full orbit gives:**

    sum_{h in H} log|1 + omega^{r_0 h}| = sum_{h in H} log(2|cos(pi r_0 h / p)|) = K log 2 + sum_{h in H} log|cos(pi r_0 h / p)|

And by CDG (summing the CDG identity over all <2>-chains in H):

    sum_{h in H} log|cos(pi r_0 h / p)| = sum_{cosets C} sum_{j=0}^{L_2-1} log|cos(pi r_0 h_{C,j} / p)|
    = sum_{cosets C} (-L_2 log 2) = m * (-L_2 log 2) = -K log 2

(Since there are m = K/L_2 cosets of <2> in H, wait -- no, the cosets of <2> in H have size L_2, and there are K/L_2 of them. The CDG identity gives sum_{j=0}^{L_2-1} log|cos(pi b 2^j / p)| = -L_2 log 2 for each coset representative b.)

Therefore:

    sum_{h in H} log|cos(pi r_0 h / p)| = -K log 2

And:

    sum_{h in H} log|1 + omega^{r_0 h}| = K log 2 + (-K log 2) = 0

**The sum of log|1 + omega^{r_0 h}| over the full orbit is EXACTLY 0.** This holds for ANY r_0 and ANY orbit H = <2,3>.

### 7.6. The orbit-averaged eigenvalue bound

From the eigenvalue iteration (Section 5.1), for each mode s = r_0 h:

    L_2 log(2|lambda|) <= sum_{j=0}^{L_2-1} log|1 + c_s omega^{...}| + C L_2 sqrt(eta)

Summing over all s in O:

    K L_2 log(2|lambda|) <= sum_s sum_j log|1 + c_s omega^{...}| + C K L_2 sqrt(eta)

The double sum on the right involves the phases AND the parameters c_s (which may vary with s). If c_s were constant (c_s = c for all s), the sum would be L_2 * sum_h log|1 + c omega^{r_0 h}| = L_2 * 0 = 0 (by the identity of Section 7.5, adjusted for the shift from c).

Wait -- the identity sum_h log|1 + omega^{r_0 h}| = 0 uses c = 1. For general c = e^{i phi}:

    sum_h log|1 + c omega^{r_0 h}| = sum_h log|1 + e^{i(phi + 2pi r_0 h / p)}|

This equals sum_h log(2|cos(phi/2 + pi r_0 h / p)|) = K log 2 + sum_h log|cos(phi/2 + pi r_0 h / p)|.

The sum of log|cos(phi/2 + pi r_0 h / p)| over h in H is the SHIFTED CDG sum over the full orbit. By the same CDG identity argument applied to each <2>-coset:

For a <2>-coset {b, 2b, 4b, ..., 2^{L_2-1} b}:

    sum_{j=0}^{L_2-1} log|cos(phi/2 + pi r_0 b 2^j / p)| = ???

This is NOT the standard CDG identity (which has phi = 0). For general phi, the sum is:

    sum_j log|cos(phi/2 + pi alpha_j)| where alpha_j = r_0 b 2^j / p

The CDG identity gives prod_j cos(pi alpha_j) = +/- 2^{-L_2}, i.e., sum_j log|cos(pi alpha_j)| = -L_2 log 2 (regardless of the sign).

For the shifted version, we CANNOT use CDG directly.

**However**, we can use the following key fact: the average over phi of log|cos(phi/2 + pi alpha_j)| is -log 2 (for each j individually). So the average over phi of the full sum is -K log 2. Combined with sum_h log|1 + c omega^{r_0 h}| = K log 2 + sum_h log|cos(...)|, the phi-average is K log 2 - K log 2 = 0.

This shows: the AVERAGE over the phase parameter c of the orbit sum is 0. For any specific c, the sum can be positive (giving (2|lambda|)^K > 1, which is trivially true since |lambda| < 1 gives 2|lambda| < 2) or negative.

For the sum to be positive: sum_h log|1 + c omega^{r_0 h}| > 0. This requires the shifted cosines to be on average > 2^{-1}, which happens when the shift phi aligns most of the orbit's phases near 0.

**The worst case** is when phi is chosen to maximize the shifted cosine product. For a random H of size K, the maximum over phi of sum_h log|cos(phi/2 + pi r_0 h/p)| is at most ~ K * max_phi (1/K sum_h log|cos(phi + pi r_0 h/p)|).

For the orbit concentrated near 0 (r_0 h/p small for most h): the average log|cos| ~ 0 (since cos(small) ~ 1). So the sum ~ 0, and (2|lambda|)^K ~ 1.

For the orbit equidistributed: the average log|cos| ~ -log 2, and (2|lambda|)^K ~ 2^{-K}, giving |lambda| ~ 1/2.

**The transition:** The orbit-averaged bound gives |lambda| between 1/2 (equidistributed) and ~1 (concentrated). For the concentrated case (K < sqrt(p), orbit near 0), |lambda| ~ 1 - C/K, which is NOT a constant gap.

---

## 8. Synthesis and the Path Forward

### 8.1. What we have established

1. **For K bounded:** Finitely many primes, constant gap by compactness. (Proved.)

2. **For K >= p^{1/2+eps}:** Constant gap by Gauss equidistribution + arc concentration. (Proved, Theorem 16.)

3. **For K in the middle range:** The CDG orbit-averaged identity shows sum_H log|1 + omega^{r_0 h}| = 0, constraining the eigenvalue. But the shifted version (with phase c != 1) can give a sum near 0 when the orbit is concentrated near 0, yielding no contraction.

4. **The inter-coset scattering (non-commutative product):** Gives contraction when L >= sqrt(p), but not when L is small. For L small and L_2 small, the scattering is negligible.

5. **The perturbation analysis around t = 0:** Gives gap ~ C/K^2, which shrinks to 0.

### 8.2. The honest assessment

The universal constant spectral gap for the MIDDLE RANGE remains open. Every approach we have tried either:
- Requires L or L_2 to be large enough for equidistribution, or
- Reduces to a perturbative bound that shrinks with K.

The fundamental obstruction is: when the orbit O is small (K < sqrt(p)) and concentrated near 0 in Z/pZ, the "+1" phase perturbation is O(1/p) per mode, and the total effect over K modes is O(K/p) < O(p^{-1/2+eps}). This is not enough for a constant gap.

### 8.3. A possible new approach: Hilbert's inequality and bilinear forms

One approach not yet explored is to use the BILINEAR structure of the cross-term more directly. The cross-term is:

    sum_{s in O} a_{3s} conj(a_s) omega^{-s/2}

This is a bilinear form in the vectors u = (a_s) and v = (a_{3s}) with weights omega^{-s/2}. For u, v unit vectors on C^K, this is bounded by the SPECTRAL NORM of the K x K matrix W with W_{s, 3s} = omega^{-s/2} (and 0 elsewhere).

Actually, W is a diagonal matrix times a permutation. The spectral norm of W is 1 (trivially). So this doesn't help.

The real constraint is that u and v are NOT independent -- they are determined by the SAME eigenvector f, just evaluated at different orbit points (s vs 3s). The map s -> 3s is a permutation of O, so v = Pi_3 u (where Pi_3 is the ×3 permutation on O). The cross-term is:

    <Pi_3 u, D_omega u> where D_omega = diag(omega^{-s/2})

For this to be close to ||u||^2 = 1, we need Pi_3 u ~ D_omega^{-1} u, i.e., u to be an approximate eigenvector of D_omega^{-1} Pi_3 = D_omega^{-1} Pi_3.

The eigenvalues of D_omega^{-1} Pi_3 are... on each <3>-coset, this is D_omega^{-1} (cyclic shift), which has eigenvalues {omega_L^j * exp(-2pi i * S_C / (Lp)) : j} where S_C is a sum of the phases around the coset. As before, S_C = 0 mod p, so the eigenvalues are {omega_L^j : j = 0, ..., L-1}.

The maximum eigenvalue magnitude is 1 (at j = 0 on each coset). So there exists a unit vector u with <Pi_3 u, D_omega u> = 1. This is the "Cauchy-Schwarz saturating" vector, and it is NOT an eigenvector of M (by the Combined Theorem).

**The gap between the CS-saturating vector and the actual eigenvector is what determines the spectral gap.** This gap depends on how far the CS-saturating vector is from the eigenspace of M.

### 8.4. The most promising remaining direction

**Direction 1: Multi-step CDG with explicit error tracking.**

Instead of iterating the eigenvalue equation L_2 times along a SINGLE <2>-chain (which requires small errors per step), iterate for n steps where n is chosen adaptively. For n << L_2: the product of n shifted cosines can still give useful bounds if the phases are sufficiently spread.

Specifically, for n steps of the eigenvalue equation:

    (2|lambda|)^n |a_s|^2 <= sum_{w=0}^{n} binom(n,w) |a_{3^w s}|^2

Summing over s in a <2>-coset and using the CDG identity for the n-step walk gives a bound that depends on the COLLISION structure of the weight classes.

**Direction 2: Use the product over ALL cosets.**

The eigenvalue lambda satisfies the consistency condition on EACH of the m = K/L cosets. The product over cosets gives:

    |lambda|^K = |det(P)|^{1/K} * (product correction)

The determinant of P = (1/2)(Pi_alpha + D Pi_beta) can be computed explicitly. If |det(P)| < 2^{-K} (say), then the geometric mean of eigenvalues is < 1/2, forcing at least one eigenvalue (and hence the second-largest) to be < 1/2.

**Direction 3: Algebraic number theory approach.**

For fixed K and L, the eigenvalues of the transfer matrix are algebraic numbers (roots of a degree-K polynomial with coefficients in Q(omega_p)). The condition |lambda| = 1 corresponds to a specific algebraic variety. The Combined Theorem shows this variety is empty. The DISTANCE from this variety to the actual eigenvalues gives the spectral gap.

By the theory of heights and the Lehmer conjecture: algebraic numbers on or near the unit circle have specific arithmetic properties. The eigenvalues of our transfer matrix, as algebraic integers of bounded degree (degree K), satisfy Lehmer-type bounds:

    ||lambda| - 1| >= c(K) > 0

The question is whether c(K) stays bounded away from 0 as K grows.

### 8.5. Final status

| Approach | Result | Limitation |
|----------|--------|-----------|
| M^2 operator norm | 3/8 per character, but ||M^2||_{op} can be close to 1 | Small modes escape phase cancellation |
| Mixed orbit + CDG | Orbit-averaged sum = 0 (exact) | Shifted sum near 0 when orbit concentrates |
| Explicit small K | Gap ~ 1/K^2 from unphased walk | Perturbation error competes |
| Non-commutative scattering | Works when L >= sqrt(p) | Overlap near 1 when L < sqrt(p) |
| CDG bootstrap | Exact case gives |lambda| = 1/2 | Error L_2 sqrt(eta) accumulates |
| Multi-coset product | All cosets share same spectral structure | Operator norm product = 2^m (trivial) |

**The universal constant gap for K in (K_0, p^{1/2+eps}) remains OPEN.** The most promising direction appears to be either:

(a) Showing that the "worst-case" orbit structure (both L and L_2 small, orbit concentrated near 0) actually forces |lambda| ~ 1/2 through a non-perturbative mechanism that we haven't identified, or

(b) Using the exact CDG identity sum_H log|1 + omega^{r_0 h}| = 0 in a more refined way that accounts for the correlation between the phase parameter c and the eigenvector structure, or

(c) A computer-algebraic verification for each possible (K, L) pair with K below some explicit threshold N_0, combined with the Theorem 16 bound for K >= N_0 (this would give a theorem of the form "for all p >= p_0(N_0), the gap is >= c", reducing to a finite computation).

---

## 9. Computational Verification Approach

### 9.1. The finite verification strategy

For each K <= N_0: there are finitely many primes p with |<2,3>| = K. For each such prime, the spectral gap can be computed. The minimum gap over all such primes gives c(K).

If we can explicitly compute c(K) for all K up to N_0 and show c(K) >= c_0 > 0 for all K <= N_0, then combined with Theorem 16 (which handles K >= p^{1/2+eps} with a constant gap), we get the universal gap for all p >= p_0.

**The remaining task:** Set N_0 large enough that p_0 from Theorem 16 (which depends on N_0 through the eps parameter: eps = (1/2)(1 - log(N_0)/log(p))) covers all primes.

Actually, Theorem 16 requires |<2,3>| >= p^{1/2+eps} for some fixed eps. If we choose N_0 = p^{1/2+eps}, this is circular. The correct statement is:

For a given eps > 0, Theorem 16 gives gap >= c(eps) for primes with |<2,3>| >= p^{1/2+eps}. For the remaining primes (|<2,3>| < p^{1/2+eps}): the set of POSSIBLE K values is {1, 2, ..., floor(p^{1/2+eps})}. For each K, the primes are finite.

**The issue:** As p -> infinity, the range of K values grows (K up to p^{1/2+eps}), and we cannot pre-compute c(K) for all K unless the set of possible (K, p) pairs is finite up to isomorphism.

### 9.2. Finiteness up to isomorphism

For a given K and given Cayley graph structure of H = <2,3> with generators 2 and 3: the transfer matrix P(t) is determined by the single parameter t = r_0/p in (0,1). The spectral radius rho(t) is a continuous function of t.

**As p -> infinity with fixed K and fixed Cayley graph:** The parameter t = r_0/p can take any value in {k/p : k = 1, ..., (p-1)/K}. For large p, these values fill out (0,1) densely. The supremum of rho(t) over these values approaches sup_{t in (0,1)} rho(t), which is < 1 by continuity and the Combined Theorem.

**But the Cayley graph structure can change with p!** For different primes p with the same K = |<2,3>|, the group H = <2,3> in F_p* can have different isomorphism types (different relative positions of 2 and 3 in the cyclic group Z/KZ).

For H = Z/KZ with generators g_1 = 2^{-1} and g_2 = 3/2 (in Z/KZ): the isomorphism type is determined by the positions s_1 = ord_{Z/KZ}(2^{-1}) and s_2 = ord_{Z/KZ}(3/2), plus their relative position. Since Z/KZ is cyclic, the structure is determined by the single parameter a = position of 3/2 relative to 2^{-1}, which is an element of Z/KZ.

As p varies (with K fixed), the parameter a varies over the elements of Z/KZ that generate it (since <2,3> = H = Z/KZ). There are phi(K) such elements. So the number of non-isomorphic structures is at most phi(K).

For each structure: rho(t) < 1 on (0,1), and sup rho(t) < 1. So c(K) = min over structures of (1 - sup rho(t)) > 0.

**Theorem 9.1 (Conditional).** For each K, c(K) > 0. The universal gap holds iff inf_K c(K) > 0.

### 9.3. Numerical evidence for c(K) behavior

From the existing computational data (agent_sum_product.md, Section 1.1): for all 166 primes tested (p = 5 to 997), |lambda_2| is between 0.66 and 0.81, with mean ~0.70 ~ 1/sqrt(2). The spectral gap is between 0.19 and 0.34.

These primes include cases with very different K values (from K = p-1 down to K = 4 for small primes). The gap is ALWAYS in this range.

**This strongly suggests c(K) >= 0.19 for all K tested.** The numerical evidence supports the conjecture that inf_K c(K) > 0, but proving it requires understanding the t -> 0 behavior of rho(t) for growing K.

### 9.4. The t -> 0 asymptotics

For t -> 0: all phases theta_j = pi t h_j approach 0. The transfer matrix P(t) approaches P(0) = (1/2)(Pi_alpha + Pi_beta), whose second-largest eigenvalue has magnitude 1 - gap(0) with gap(0) = 1 - cos(pi/L).

As t increases from 0: the phases "switch on," and the eigenvalue rho(t) changes. The question is: does rho(t) DECREASE (gap increases) or INCREASE (gap decreases) as t moves away from 0?

By the CDG bootstrap argument: for "generic" t (away from 0 and 1), the approximate phase condition gives |lambda| ~ 1/2. Near t = 0: |lambda| ~ 1 - gap(0) = cos(pi/L). Since 1/2 < cos(pi/L) for L >= 2, the eigenvalue DECREASES as t moves from 0 toward generic values.

So the MAXIMUM of rho(t) is at t = 0 (or close to it):

    sup_t rho(t) = rho(0) = cos(pi/L)

But the ACTUAL parameter is t = 1/p (not t = 0). So the gap is:

    gap(actual) = 1 - rho(1/p) ~ 1 - cos(pi/L) + O(1/p) = gap(0) + O(1/p)

For L bounded: gap(0) is a positive constant, and the O(1/p) correction is negligible. So the gap is bounded below by a constant.

For L -> infinity: gap(0) -> 0, but the O(1/p) correction might not compensate. However, we need L and p to satisfy p | (3^L - 1), so p <= 3^L - 1, giving 1/p >= 1/(3^L - 1). Thus:

    gap(actual) >= gap(0) + c/p >= pi^2/(2L^2) + c/3^L

For L large: the first term dominates, giving gap ~ pi^2/(2L^2). Since p >= L (trivially), we have L <= p, and gap >= pi^2/(2p^2). Not a constant.

**BUT** we also need K = |<2,3>| < p^{1/2+eps}. Since K = lcm(L_2, L) >= L, we have L <= K < p^{1/2+eps}. So gap(0) >= pi^2/(2K^2) > pi^2/(2 p^{1+2eps}). This is O(1/p), consistent with L-V.

**The CDG bootstrap would improve this** if we could show that rho(t) is NOT monotonically increasing as t decreases from generic values to 0. In other words: if the transition from rho ~ 1/2 (generic t) to rho ~ cos(pi/L) (small t) is SMOOTH and the maximum is always at t = 0, then the gap at t = 1/p is:

    gap(1/p) ~ gap(0) = 1 - cos(pi/L)

and the minimum over L is 0 (as L -> infinity).

**BUT** if there is a PHASE TRANSITION -- a critical t_c below which rho(t) = 1 - O(gap(0)) and above which rho(t) <= 1/2 + o(1) -- then for t = 1/p > t_c, the gap is constant!

### 9.5. The phase transition picture

**Conjecture 9.1 (Phase transition in spectral radius).** For the one-parameter family P(t) with fixed Cayley graph structure of size K:

    rho(t) ~ max(cos(pi/L), 1/2 * g(t))

where g(t) transitions from g(0) ~ 2 cos(pi/L) to g(t) ~ 1 for t >> 1/K. The crossover occurs at t_c ~ 1/K.

For t = 1/p >> 1/K (which holds when K < p): the spectral radius is ~ 1/2.

**If this conjecture holds:** For K < p (which is always true since K divides p-1 < p): t = 1/p > 0 = t_c (?), and rho(1/p) <= 1/2 + o(1). This gives a constant gap!

But the conjecture requires the transition to happen at t_c ~ 1/K, not at t_c ~ 0. The argument is: at t = 1/K, the phases pi t h_j = pi h_j / K range over [0, pi] (since h_j ranges over {0, 1, ..., K-1} in Z/KZ). So the phases are spread over the full semicircle, giving the Jensen bound: average cos^2 ~ 1/2, hence |lambda| ~ 1/sqrt(2).

For t = 1/p < 1/K: the phases pi t h_j = pi h_j / p are all small (< pi K / p < pi p^{-1/2+eps} << 1). So the phases cluster near 0, and the Jensen bound fails.

**The critical t is t_c ~ 1/K, and the actual t = 1/p satisfies t/t_c = K/p < p^{-1/2+eps}. So we are BELOW the critical t -- in the "perturbative" regime where the gap is small.**

This confirms the picture: for K in the middle range, the gap at the actual parameter t = 1/p is perturbatively small (of order 1/p or 1/K^2), NOT a constant.

---

## 10. Conclusions

### 10.1. Summary of findings

1. **The CDG orbit identity** sum_H log|1 + omega^{r_0 h}| = 0 is an exact identity that constrains the eigenvalue but does not by itself give a constant gap (Section 7.5).

2. **The shifted CDG product** can be close to 1 when the orbit concentrates near 0, which happens for the middle-range primes with K < sqrt(p) (Section 5.5).

3. **The inter-coset scattering** (non-commutative product of intra-coset operators) gives contraction proportional to the overlap between consecutive "bad" eigenvectors. This overlap is near 1 when L < sqrt(p) and coset representatives are small (Section 6.7).

4. **The perturbation analysis** around the unphased matrix gives gap ~ 1/K^2, shrinking to 0 as K grows (Section 4.3).

5. **The phase transition picture** (Section 9.5) suggests that the spectral radius transitions from ~1/2 (for "generic" phases) to ~cos(pi/L) (for phases near 0) at a critical parameter t_c ~ 1/K. The actual parameter t = 1/p is below t_c when K < p, placing us in the perturbative regime.

### 10.2. Honest assessment of the gap

Based on this analysis, the universal constant spectral gap for the middle range appears to require a genuinely new idea. The approaches tried (CDG products, inter-coset scattering, M^2 operator norm, sum-product) all reduce to equidistribution-type bounds that fail when K < sqrt(p).

**The most likely resolution** is one of:
- (a) A number-theoretic input showing that for primes in the middle range, some additional structure is present that constrains the eigenvalue beyond what the orbit geometry alone provides.
- (b) A proof that the minimum of c(K) over K is achieved at some finite K_0, after which c(K) is INCREASING (because larger orbits have better equidistribution). If c(K) has a global minimum at some K* < infinity, then computing c(K*) explicitly gives the universal gap.
- (c) A completely different approach (e.g., via p-adic analysis, automorphic forms, or a novel combinatorial argument) that bypasses the orbit-equidistribution paradigm.

### 10.3. A concrete open question

**Question.** Is there a SINGLE prime p >= 5 where |lambda_2(p)| > 0.85?

If not -- if the spectral gap is always >= 0.15 -- then the universal constant gap holds empirically. The challenge is to prove it.

From the numerical data: the maximum observed |lambda_2| is about 0.81 (at small primes where the orbit is the entire group). For larger primes, |lambda_2| tends toward 1/sqrt(2) ~ 0.707. This suggests the gap is ALWAYS at least 0.19, with the worst cases being small primes.

**Conjecture 10.1.** For all primes p >= 5: |lambda_2(p)| <= 1/sqrt(2) + C/p for some absolute constant C. In particular, |lambda_2(p)| <= 0.75 for all p >= p_0.

This conjecture, if true, implies a universal gap of 0.25. But proving it requires overcoming the middle-range obstruction identified in this document.

---

## References

1. F. Chung, P. Diaconis, R. Graham, "Random walks arising in random number generation," *Ann. Probab.* 15 (1987), 1148-1165.
2. J. Bourgain, A. Gamburd, "Uniform expansion bounds for Cayley graphs of SL_2(F_p)," *Ann. Math.* 167 (2008), 625-642.
3. E. Lindenstrauss, P. Varju, "Spectral gap in the group of affine transformations over prime fields," *Ann. Fac. Sci. Toulouse Math.* 25 (2016), 969-993.
4. J. Bourgain, N. Katz, T. Tao, "A sum-product estimate in finite fields, and applications," *GAFA* 14 (2004), 27-57.
5. T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," *Forum Math. Pi* 10 (2022), e12.
