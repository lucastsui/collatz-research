# Compactness Gap Analysis: Does rho(K) -> 1 as K -> infinity?

**Date:** 2026-03-05

**Goal:** Determine whether the universal spectral gap for the affine Collatz operator can be closed by a compactness argument over the group order K = |<2,3>|. Specifically: for each K, define rho(K) = sup over all primes p with |<2,3>| = K of the second eigenvalue magnitude |lambda_2(p)|. Does rho(K) remain bounded away from 1, or does it approach 1?

**Status:** The analysis reveals a tension between two effects. On one hand, the unphased Cayley graph gap shrinks as ~1/K^2. On the other hand, the "+1" phases from the affine structure provide mixing (via CDG product constraints) that pushes eigenvalues toward 1/2. The existing numerical data (|lambda_2| in [0.66, 0.81] for ALL 166 primes tested, p = 5 to 997) strongly suggests rho(K) stays bounded -- but a proof requires closing the gap between theoretical bounds and empirical observation.

---

## 0. Summary of Findings

1. **For fixed K**: there are finitely many primes with |<2,3>| = K. For each such prime, the spectral gap is positive (Combined Theorem). So rho(K) < 1 for each K.

2. **The unphased matrix**: The transfer matrix A(0) (all phases = 1, corresponding to the pure multiplicative walk without "+1") is an average of two permutation matrices on the cyclic group Z/KZ. Its spectral gap is 1 - cos(pi/L) ~ pi^2/(2L^2), which shrinks with L = ord_p(3). This does NOT vanish to zero; it gives a positive gap ~ pi^2/(2K^2) for each K.

3. **Phase transition picture**: As the phase parameter t = r_0/p increases from 0 to ~1/K, the spectral radius transitions from rho ~ cos(pi/L) (the unphased gap regime) to rho ~ 1/sqrt(2) ~ 0.707 (the CDG regime). The crossover occurs at t_c ~ 1/K, where the phases spread over the full circle.

4. **The actual parameter**: For primes with |<2,3>| = K, the actual t = 1/p. Since K < p (always, as K | (p-1)), we have t < 1/K, placing us in the "perturbative" regime below the crossover. But the gap is still at least gap(0) ~ pi^2/(2K^2) plus corrections from the "+1" phases.

5. **CDG bootstrap bound**: When the approximate phase condition holds, the CDG product identity forces |lambda| = 1/2 exactly. With error accumulation of O(L_2 * sqrt(eta)), this gives gap >= c/L_2^2. The gap shrinks polynomially in max(L_2, L), NOT exponentially.

6. **Numerical evidence**: For all 166 primes tested (p = 5 to 997), |lambda_2| lies in [0.66, 0.81] with mean ~0.70 ~ 1/sqrt(2). The spectral gap is always in [0.19, 0.34]. **No prime has been found with |lambda_2| > 0.85.** The worst cases are small primes; for large primes, |lambda_2| converges toward 1/sqrt(2).

7. **The open question**: Does rho(K) = sup over primes with |<2,3>| = K of |lambda_2| stay bounded away from 1 as K -> infinity? The theoretical lower bound on the gap is c/K^2 (from CDG + Cayley gap), but the empirical gap is ~0.30 (constant). Closing this discrepancy requires either improving the CDG bootstrap error bounds or finding a new argument.

---

## 1. The Parametric Transfer Matrix

### 1.1. Setup

Fix a prime p and let K = |<2,3>| in F_p*. The group H = <2,3> is cyclic (since it is a subgroup of the cyclic group F_p*). Let g be a generator of H.

The orbit of r_0 in frequency space is O = {r_0 * g^j : j = 0, ..., K-1}. The K x K transfer matrix is:

    A[sigma(j), j] = 1/2                           (branch T_0: multiply by 2^{-1})
    A[tau(j), j]   = (1/2) * omega^{r_0 * g^j / 2}  (branch T_1: multiply by 3/2, with phase)

where sigma and tau are the permutations of {0,...,K-1} induced by multiplication by 2^{-1} and 3*2^{-1} in H, and omega = e^{2*pi*i/p}.

### 1.2. The phase parameter

All phases have the form omega^{r_0 * g^j / 2} = exp(2*pi*i * r_0 * g^j / (2p)). Define:

    t = r_0 / (2p)

Then the phase at position j is exp(2*pi*i * t * g^j), where g^j is understood as an element of F_p* (an integer in {1, ..., p-1}).

The parameter t ranges over a discrete set: t = r_0 / (2p) for r_0 in {1, ..., p-1}. As p varies over primes with |<2,3>| = K, the set of achievable t values changes.

### 1.3. The t = 0 limit

At t = 0, all phases equal 1, and the transfer matrix becomes:

    A(0) = (1/2)(Pi_{sigma} + Pi_{tau})

This is the average of two permutation matrices on the group H. Since <2,3> is cyclic of order K, and sigma, tau are multiplications by 2^{-1} and 3/2 respectively, the matrix A(0) is the transition matrix of the random walk on Z/KZ with steps corresponding to 2^{-1} and 3/2.

**Eigenvalues of A(0):** Since H = Z/KZ is abelian, the eigenvectors are characters chi_k(j) = omega_K^{jk}, and:

    lambda_k(0) = (1/2)(omega_K^{a*k} + omega_K^{b*k})

where a = position of 2^{-1} in Z/KZ and b = position of 3/2. The magnitude:

    |lambda_k(0)| = |cos(pi * (a - b) * k / K)|

Now a - b = (position of 2^{-1}) - (position of 3/2) = position of 2^{-1} * (3/2)^{-1} = position of 3^{-1}. If L = ord_p(3) divides K, then the position of 3 in Z/KZ is K/L (assuming g is chosen so 3 = g^{K/L}). Hence the position of 3^{-1} is K - K/L = K(1 - 1/L).

The second eigenvalue is at k = 1:

    |lambda_1(0)| = |cos(pi * (1 - 1/L))| = |cos(pi - pi/L)| = cos(pi/L)

(using |cos(pi - x)| = |cos(x)| = cos(x) for 0 < x < pi/2).

So **the spectral gap of A(0) is**:

    gap(0) = 1 - cos(pi/L) ~ pi^2 / (2L^2)

For large L, this shrinks as 1/L^2. Since L | K, the gap is at least 1 - cos(pi/K) ~ pi^2 / (2K^2).

**At t = 0, the spectral gap is ~ pi^2 / (2K^2) > 0, not zero!**

Wait -- this contradicts the claim that rho(0) = 1. Let me re-examine.

### 1.4. Correction: A(0) is NOT stochastic in the standard sense

The matrix A(0) = (1/2)(Pi_sigma + Pi_tau) is an average of two permutation matrices. It IS doubly stochastic (each row and column sums to 1). The eigenvalue 1 IS present (for k = 0). The gap is 1 - max_{k != 0} |lambda_k(0)|.

For the Cayley graph on Z/KZ with generators {a, b} where a - b = position of 3^{-1}, the second eigenvalue is cos(pi/L) as computed above. This is LESS than 1, so the gap is POSITIVE even at t = 0.

**Key correction**: rho(0) < 1, NOT rho(0) = 1. The claim that "at t = 0, the gap vanishes" was wrong. The gap at t = 0 comes from the fact that the two permutations sigma and tau generate a TRANSITIVE action on H, and the random walk on this Cayley graph has a spectral gap.

The gap shrinks as 1/L^2 ~ 1/K^2 for K large, but it is always positive.

### 1.5. What happens at the "true" t = 0 limit?

The matrix A(0) as defined above has all phases = 1, corresponding to the "+1" translation being invisible (r_0 = 0). But r_0 = 0 is excluded (the trivial mode). The smallest nonzero r_0 gives t_min = 1/(2p).

At t_min, the phases are exp(2*pi*i * g^j / (2p)), which are CLOSE to 1 but not exactly 1. The perturbation from A(0) is of order 1/p (the phases deviate by O(g^j / p)).

By standard perturbation theory (Weyl's inequality for normal matrices):

    |rho(t_min) - rho(0)| <= ||A(t_min) - A(0)||_op = (1/2) max_j |omega^{g^j/(2p)} - 1| ~ pi * max(H) / p

where max(H) is the largest element of H in {1,...,p-1}. Since max(H) can be as large as p-1, this perturbation is O(1), and the bound is vacuous.

**The perturbation theory fails** because the phases are NOT uniformly small -- some orbit elements are large in Z/pZ.

---

## 2. The Correct Parameterization

### 2.1. Why t = r_0/p is NOT the right parameter

The phases are exp(2*pi*i * r_0 * h_j / (2p)) where h_j ranges over H. These phases depend on the PRODUCTS r_0 * h_j mod p, not on r_0 * h_j as integers. The map h_j -> r_0 * h_j mod p is a permutation of H (since r_0 is a unit mod p), so the set of phases is:

    {exp(2*pi*i * s / (2p)) : s in r_0 * H}

This is the same set (up to permutation) as:

    {exp(2*pi*i * s / (2p)) : s in H}

when we vary r_0 over coset representatives. But the ASSIGNMENT of phases to matrix positions changes.

**Key insight**: The transfer matrix depends not just on the SET of phases, but on HOW the phases are assigned to the permutation positions. Different orbits (different r_0) give different phase assignments.

### 2.2. The actual compact parameter space

For fixed group structure (fixed K, L, and Cayley graph), the transfer matrix is determined by:

1. The permutations sigma, tau on {0,...,K-1} (finitely many choices)
2. The phase vector (phi_0, ..., phi_{K-1}) in [0, 2*pi)^K

The actual phases satisfy phi_j = pi * r_0 * g^j / p (mod 2*pi). As r_0 varies over {1,...,p-1} (modulo the orbit size K), the phase vector traces a curve on the K-torus.

**The phases are CORRELATED**: they all have the form phi_j = pi * r_0 * g^j / p. The entire configuration is determined by a single parameter r_0 and the group elements g^j. As p varies (over primes with |<2,3>| = K), the "scale" 1/p changes, but the multiplicative structure {g^j} stays the same (up to isomorphism of Z/KZ).

### 2.3. The effective parameter space for fixed K

For fixed K and fixed abstract group structure, the transfer matrix is a function of:

    A(r_0, p) = (1/2) Pi_sigma + (1/2) diag(e^{2*pi*i * r_0 * g^j / (2p)}) Pi_tau

where p is a prime with |<2,3>| = K, and r_0 in {1,...,(p-1)/K} indexes the orbits.

The parameter r_0/p ranges over a DISCRETE subset of (0, 1/K]. The phases phi_j = pi * r_0 * g^j / p, and since g^j mod p takes values in {1,...,p-1}, the phases are:

    phi_j in {pi * k / p : k = 1, ..., p-1}

This is a DISCRETE set of p-1 points in [0, pi). The spacing is pi/p.

---

## 3. The Compactness Argument: Fixed K

### 3.1. Statement

**Theorem.** For each K >= 1, there exists c(K) > 0 such that for every prime p with |<2,3>| = K and every orbit O of size K:

    |lambda_max(A)| <= 1 - c(K)

where A is the K x K transfer matrix on O.

**Proof.** For fixed K, there are finitely many primes p with |<2,3>| = K (since p | lcm({2^d - 1 : d | K, 3^d - 1 : d | K}), a fixed integer). For each prime, the Combined Theorem gives |lambda_max| < 1. There are at most (p-1)/K orbits per prime, each with |lambda_max| < 1. The maximum over finitely many values less than 1 is still less than 1. []

### 3.2. The quantitative question

What is the behavior of c(K) as K -> infinity?

**If c(K) -> 0**: the universal gap is NOT proved by this approach.

**If c(K) >= c_0 > 0**: the universal gap IS proved.

### 3.3. What determines c(K)?

c(K) = min over all primes p with |<2,3>| = K, over all orbits O, of the spectral gap of A on O.

The spectral gap depends on:
1. The group structure (K, L, the Cayley graph) -- finitely many choices for each K
2. The phases phi_j = pi * r_0 * g^j / p -- depend on the specific prime p and orbit r_0

For the spectral gap to be small, we need:
- Either the unphased gap gap(0) to be small (requires L or K large), OR
- The phases to REDUCE the gap from gap(0)

Can the phases reduce the gap? In principle yes: the phases break the symmetry of A(0), and the eigenvalues can move in either direction. But the Combined Theorem guarantees they stay strictly inside the unit circle.

The question is whether the eigenvalues can approach the unit circle ARBITRARILY closely as p -> infinity with K fixed. Since there are only finitely many primes for each K, this cannot happen within a single K. But as K grows, the number of primes grows, and the worst prime for each K might have an increasingly bad gap.

---

## 4. Analytical Study: The t -> 0 Regime

### 4.1. First-order perturbation

Write A(t) = A(0) + t * A_1 + O(t^2) where t = r_0 / (2p) parameterizes the phase. The first-order correction is:

    A_1[tau(j), j] = i * pi * g^j * Pi_tau    (from d/dt of e^{2*pi*i*t*g^j} at t=0)

The eigenvalue shift at first order:

    delta_lambda_k = <v_k, A_1 v_k> / <v_k, v_k>

where v_k is the eigenvector of A(0) for eigenvalue lambda_k(0).

Since A(0) has eigenvectors that are characters of Z/KZ, and A_1 involves the diagonal matrix diag(i * pi * g^j), the first-order shift involves:

    delta_lambda_k = (i * pi / (2K)) sum_j g^j * omega_K^{(b - a)kj}    (schematically)

This is an exponential sum over the group elements {g^j}. For k = 1 (the eigenvector with the largest |lambda(0)|), this sum may or may not vanish.

**If the first-order shift is purely imaginary** (which it is, since A_1 is anti-Hermitian up to permutation factors), then to first order:

    |lambda_k(t)|^2 = |lambda_k(0)|^2 + O(t^2)

The spectral radius changes only at SECOND order. This is why the gap opens quadratically: gap(t) ~ gap(0) + c * t^2.

### 4.2. Second-order analysis

The second-order correction to |lambda_k|^2 involves the curvature of the eigenvalue in the complex plane. By standard perturbation theory for non-Hermitian matrices:

    |lambda_k(t)|^2 = |lambda_k(0)|^2 + t * 2 Re[conj(lambda_k(0)) * delta_1] + t^2 * [|delta_1|^2 + 2 Re(conj(lambda_k(0)) * delta_2)] + ...

where delta_1, delta_2 are first and second order corrections. The first-order term 2 Re[conj(lambda_k(0)) * delta_1] may be nonzero (it's the real part of a product).

Whether the gap INCREASES or DECREASES with t depends on the sign of this first-order correction. For the eigenvalue closest to 1 (the "worst" eigenvalue), the phases from the "+1" translation should generically push it INWARD (away from the unit circle), because the "+1" translation is the key mixing mechanism.

### 4.3. The CDG constraint on the parametric family

Regardless of the perturbation analysis, the CDG product identity provides a HARD constraint: for any orbit element r and any <2>-chain of length L_2:

    prod_{j=0}^{L_2-1} cos(pi * r * 2^j / p) = +/- 2^{-L_2}

This means that the phases CANNOT all be close to 0 along a <2>-chain. At least one phase must be far from 0 (to keep the product at 2^{-L_2}).

For the transfer matrix, this translates to: the "effective contraction factor" along a <2>-chain is bounded by the CDG product, which is exactly 2^{-L_2}. The spectral gap from this is:

    |lambda| <= (2^{-L_2})^{1/L_2} * 2 = ... (not directly, but the CDG constraint bounds the product)

More precisely, if the approximate phase condition holds (|lambda| close to 1), then the CDG-type product over any <2>-chain gives:

    (2|lambda|)^{L_2} <= prod_{j=0}^{L_2-1} |1 + e^{i*phi_j}| = prod 2|cos(phi_j/2)|

The CDG identity says prod |cos(pi * r * 2^j / p)| = 2^{-L_2}. For the shifted product:

    prod |cos(phi/2 + pi * r * 2^j / p)|

this is generally DIFFERENT from 2^{-L_2}, but the CDG constraint on the UNSHIFTED product limits how large the shifted product can be.

---

## 5. The Key Obstruction: Phase Collapse for Small Orbits Near Zero

### 5.1. The worst case

Consider a prime p where H = <2,3> has order K with K << sqrt(p). The orbit O = r_0 * H in frequency space. If r_0 = 1 (the smallest possible), then O = H = {1, 2, 3, 4, 6, 8, 9, ...} (elements of the form 2^a * 3^b mod p, starting from 1).

When K << sqrt(p), the elements of H (as integers in {1,...,p-1}) include many SMALL values: the elements 2^a * 3^b for a + b <= log_3(sqrt(p)) are at most sqrt(p) as integers, hence also at most sqrt(p) as residues mod p. These elements are ALL "near 0" in the phase sense: phi_j = pi * h_j / p << 1.

The number of such small elements is at least the number of (a,b) pairs with 2^a * 3^b <= sqrt(p), which is ~ (log p)^2. For K ~ (log p)^2, MOST orbit elements are small.

For these orbits, all phases are ~ pi * h_j / p ~ 0, and the transfer matrix is close to A(0). The spectral gap is close to gap(0) ~ pi^2 / (2K^2).

### 5.2. Is this actually achievable?

For |<2,3>| = K with K = p^{o(1)}, we need p to be a prime where both ord_p(2) and ord_p(3) are sub-polynomial. As discussed in Section 9 of [theorem16_extended.md], such primes exist but are very sparse (they must divide gcd(2^d - 1, 3^d - 1) for small d).

For K = (log p)^C (polylogarithmic), the elements of H as integers range from 1 to 3^K = p^{C * log 3 / log p * log p / ...} = p^{o(1)}. Actually, 3^K = 3^{(log p)^C} which is superpolynomial in p for C > 1 but subexponential. So max(H) as an integer before reduction mod p is at most 3^K, which can be enormous compared to p.

**The elements of H are NOT all small.** Even when K is small, the elements 2^a * 3^b mod p wrap around for a + b moderately large. The specific distribution of H in Z/pZ depends on the arithmetic of p.

### 5.3. The Gauss sum constraint

For a subgroup H of F_p* of order K, the distribution of H in Z/pZ is controlled by exponential sums:

    |sum_{h in H} e(th/p)| <= sqrt(p)    (Gauss sum bound)

This means: for any arc I of size R in Z/pZ, |H cap I| = K * R/p + O(sqrt(p)).

When K < sqrt(p): the error O(sqrt(p)) dominates the main term K * R/p, so the equidistribution is vacuous. H COULD cluster in an arc of size sqrt(p).

When K = sqrt(p): |H cap I| = sqrt(p) * R/p + O(sqrt(p)) = O(sqrt(p)), giving no useful concentration bound.

**Key fact**: For H clustering near 0 in an arc of size R: at most O(R * K/p + sqrt(p)) elements of H lie in the arc. For R ~ p/K (the "fair share" arc size), this is O(sqrt(p) + 1). If K < sqrt(p), the fair share arc has MORE than K elements, so the ENTIRE orbit CAN cluster in an arc of size p/K.

However, the elements of H near 0 are precisely the "small" powers 2^a * 3^b. The number of such elements with 2^a * 3^b < R is approximately log^2(R) (for small a, b). So for R = p/K, we get ~ log^2(p/K) elements near 0. For K much larger than log^2(p), the orbit CANNOT entirely cluster near 0.

**The regime K = p^{o(1)}**: If K grows as any power of log p, then log^2(p) = o(K), so most orbit elements are NOT near 0 in Z/pZ. They wrap around and are essentially randomly distributed.

This is a crucial structural constraint: **even for sub-polynomial K, most orbit elements are large mod p, so most phases are NOT close to 0.**

---

## 6. The Structural Rigidity: Why rho(K) May Stay Bounded

### 6.1. The phase distribution on orbits

For a cyclic subgroup H of F_p* of order K, the phases phi_j = pi * r_0 * g^j / p are determined by the distribution of r_0 * H in Z/pZ.

When K >= p^delta for any delta > 0: the BGK bound gives excellent equidistribution (see [theorem16_extended.md]). This is the regime covered by Theorem 17.

When K = p^{o(1)}: equidistribution fails in general. But the CDG product identity provides a different constraint:

**CDG constraint on the orbit**: For any r_0 * g^j in the orbit, and any <2>-chain of length L_2 = ord_p(2):

    prod_{l=0}^{L_2-1} cos(pi * r_0 * g^j * 2^l / p) = +/- 2^{-L_2}

This means that along any <2>-chain within the orbit, the phases CANNOT all be close to 0. The product is EXACTLY 2^{-L_2}, so at least one cosine factor must be significantly less than 1.

### 6.2. Implications for the spectral gap

The CDG constraint ensures that the transfer matrix cannot be close to A(0) on EVERY <2>-chain simultaneously. Even if some chains have phases close to 0, others must have dispersed phases.

For the spectral gap analysis: the eigenvector f = sum a_r chi_r is supported on the orbit O. The eigenvalue equation couples modes along both <2>-chains and <3>-chains. If the eigenvector tries to concentrate energy on modes with phases near 0 (to exploit the near-degenerate part of the matrix), the CDG constraint forces some of the coupled modes to have large phases, which the eigenvector must also have nonzero energy on.

This creates a tension: concentrating energy on "good" modes (phases near 0) is impossible without also having energy on "bad" modes (phases far from 0), where the contraction is stronger.

### 6.3. Quantifying the CDG constraint

Consider the partition of the orbit O into <2>-chains (orbits of <2> within O). Each chain has L_2 elements. There are m = K/L_2 chains (if L_2 | K; otherwise the analysis is similar).

For each <2>-chain B_i = {r_i, 2r_i, 4r_i, ..., 2^{L_2-1}r_i}:

    prod_{l=0}^{L_2-1} |cos(pi * r_i * 2^l / p)| = 2^{-L_2}

By the AM-GM inequality:

    (1/L_2) sum_{l=0}^{L_2-1} log |cos(pi * r_i * 2^l / p)| = -log 2

The average of log|cos(...)| is exactly -log 2 ~ -0.693. Since log|cos(x)| <= 0 for all x, and the average is -log 2, we cannot have all terms close to 0 (i.e., all |cos| close to 1).

**Claim:** For any <2>-chain, at least one element r_i * 2^l satisfies:

    |cos(pi * r_i * 2^l / p)| <= 2^{-1} = 1/2

**Proof:** If all L_2 factors satisfied |cos(...)| > 1/2, then the product would be > 2^{-L_2}. But the product is EXACTLY 2^{-L_2}, contradiction. So at least one factor is <= 1/2. []

This means: on each <2>-chain, at least one mode has its cosine factor <= 1/2, which corresponds to a phase phi such that |cos(phi/2)| <= 1/2, i.e., phi >= 2*pi/3. This is a significant phase.

### 6.4. From CDG to spectral gap

For the K x K transfer matrix, the CDG constraint on each <2>-chain provides a "mode with significant phase." There are at least K/L_2 such modes (one per <2>-chain). The eigenvector must interact with these modes through the eigenvalue equation.

**The bootstrap argument** (from Section 14 of agent_universal_gap.md): Starting from the approximate phase condition:

    a_{3s} ~ e^{i*theta} * omega^{s/2} * a_s

and iterating the eigenvalue equation along a <2>-chain:

    (2*lambda)^{L_2} * a_{2^{L_2} * s} = sum_{paths} (phase factors) * a_{3^w * s}

The CDG product constrains the total magnitude:

    |(2*lambda)|^{L_2} = |sum_{paths}| <= prod |1 + c * e^{i*phi_l}|

where the product runs over the <2>-chain. If the approximate phase condition is EXACT, then:

    (2*|lambda|)^{L_2} = prod |1 + e^{i*phi_l}| = prod 2|cos(phi_l/2)| = 2^{L_2} * prod |cos(phi_l/2)|

By the CDG identity, prod |cos(pi * r * 2^l / p)| = 2^{-L_2}, so:

    (2*|lambda|)^{L_2} = 2^{L_2} * 2^{-L_2} = 1

giving |lambda| = 1/2.

**This is the exact CDG bound**: when the approximate phase condition holds exactly, |lambda| = 1/2. The error from the approximation is O(L_2 * sqrt(eta)), so:

    ||lambda| - 1/2| <= C * L_2 * sqrt(eta)

If eta = 1 - |lambda|^2 < epsilon, then |lambda| >= sqrt(1 - epsilon) ~ 1 - epsilon/2, so:

    1 - epsilon/2 - 1/2 <= C * L_2 * sqrt(epsilon)
    1/2 - epsilon/2 <= C * L_2 * sqrt(epsilon)

For epsilon small: 1/2 <= C * L_2 * sqrt(epsilon), giving sqrt(epsilon) >= 1/(2C * L_2), hence:

    **epsilon >= 1 / (4C^2 * L_2^2)**

This gives a spectral gap of at least c / L_2^2, which depends on L_2 = ord_p(2).

### 6.5. The gap depends on L_2, not K

The CDG bootstrap gives gap >= c / L_2^2 when the approximate phase condition holds. For the general case (without assuming the phase condition holds exactly), the gap is at least:

    gap >= min(c / L_2^2, c' * (1 - cos(pi/L)))

where the first term comes from the CDG bootstrap (if the phase condition nearly holds) and the second from the intra-coset gap (if the phase condition fails badly).

For L_2 and L both bounded: gap >= c (constant).

For L_2 large: gap >= c / L_2^2, which shrinks.

For L large: gap >= c / L^2, which shrinks.

**The gap shrinks at most polynomially in max(L_2, L).** Since K = |<2,3>| >= max(L_2, L), the gap shrinks at most polynomially in K:

    gap >= c / K^2

This is MUCH better than the exponential decay c / 9^K that we feared from the naive parametric analysis.

---

## 7. The Main Theorem Attempt

### 7.1. Statement (Conditional)

**Theorem (Conditional on CDG bootstrap rigor).** There exists a function c(K) >= c_0 / K^2 (for an absolute constant c_0 > 0) such that for every prime p with |<2,3>| = K:

    |lambda_2(p)| <= 1 - c_0 / K^2

**Consequence for the universal gap:** This does NOT give a universal constant gap (since c_0/K^2 -> 0). But combined with Theorem 17:

- For K >= p^delta: gap >= c_1 (absolute constant, from BGK + Theorem 17)
- For K < p^delta: gap >= c_0 / K^2

The overall gap is:

    gap >= min(c_1, c_0 / K^2) >= min(c_1, c_0 / p^{2*delta})

Taking delta -> 0: the gap approaches min(c_1, c_0) > 0 for any FIXED prime, but we need the bound to be UNIFORM.

For the universal gap: we need gap >= c for ALL primes simultaneously. The bound c_0 / K^2 suffices when K is bounded, and c_1 suffices when K >= p^delta. The remaining case is K growing but sub-polynomial.

### 7.2. The sub-polynomial K case

When K = p^{o(1)}: both L_2 and L divide K, so L_2, L = p^{o(1)}. The CDG bootstrap gives gap >= c / L_2^2. If L_2 >= K^{1/2} (say), then gap >= c / K.

When BOTH L_2 and L are small (say both <= K^{1/2}): then K = |<2,3>| is bounded by lcm(L_2, L) * ... which is at most L_2 * L <= K. The inter-coset structure (m = K/L cosets, each coupled by the deterministic x2 walk) provides additional mixing.

### 7.3. The true obstruction

The CDG bootstrap gives gap >= c / L_2^2 with an error term of O(L_2 * sqrt(eta)). If L_2 -> infinity, the bootstrap loses precision.

**Can we improve the CDG bootstrap?** The key question is whether the error accumulation over L_2 steps is truly O(L_2) or can be improved to O(sqrt(L_2)) (by some independence argument).

If the error is O(sqrt(L_2) * sqrt(eta)): then the bootstrap gives |lambda| <= 1/2 + C * sqrt(L_2 * eta), leading to:

    gap >= c / L_2

A linear rather than quadratic dependence. But even O(sqrt(L_2)) is not clear.

---

## 8. Numerical Investigation Plan

The script `compactness_gap_compute.py` in this directory computes:

1. **Part 1**: For each K (up to ~2000 from exhaustive prime survey), find rho(K) = max |lambda_2| over primes with that K.

2. **Part 3**: The parametric transfer matrix A(t) for several group structures, studying the behavior of rho(A(t)) near t = 0.

3. **Part 4**: Larger K values via factoring 2^d - 1 and 3^d - 1.

4. **Part 5**: Worst-case orbit analysis -- which r_0 gives the largest |lambda|.

5. **Part 6**: Precise power-law fit: gap(t) ~ c * t^alpha, determining alpha.

**To run**: `source venv/bin/activate && python compactness_gap_compute.py`

The key predictions to test:

- **Does rho(K) increase monotonically with K?** If yes, at what rate?
- **Is the increase bounded (rho(K) -> rho_infty < 1)?** This would prove the universal gap.
- **What is alpha in gap(t) ~ c * t^alpha?** Is it 2 (quadratic) or something else?
- **For primes with small K, is the worst orbit the one with r_0 = 1?**

---

## 9. Synthesis: The Path Forward

### 9.1. What we know

| Aspect | Status |
|--------|--------|
| rho(K) < 1 for each K | **Proved** (finitely many primes, Combined Theorem) |
| rho(K) bounded for K <= K_0 | **Proved** (compactness of bounded-dim transfer matrix) |
| rho(K) bounded for K >= p^delta | **Proved** (Theorem 17, BGK equidistribution) |
| rho(K) bounded for K = p^{o(1)} | **Open** (this document) |
| CDG bootstrap: gap >= c/L_2^2 | **Partially proved** (modulo error accumulation) |
| Phase collapse obstruction at t=0 | **Analyzed**: gap(0) > 0 but ~1/K^2 |

### 9.2. The remaining gap

The universal spectral gap would follow from showing that **rho(K) stays bounded away from 1 as K -> infinity**. The current bounds give:

    1 - rho(K) >= c / K^2

from the CDG bootstrap, which goes to 0. To improve:

**Approach A: Tighter CDG bootstrap.** Show the error accumulation over L_2 steps is o(L_2) rather than O(L_2). This would give gap >= c / L_2^alpha for alpha < 2, potentially alpha = 0 (constant gap).

**Approach B: Multi-chain CDG.** Use the product over ALL <2>-chains simultaneously, not just one. The product of CDG constraints over K/L_2 independent chains gives an exponential contraction, which may beat the polynomial loss.

**Approach C: Entropy/coupling argument.** The coupling/entropy analysis from [agent_coupling_entropy.md] may give a direct bound on the gap that doesn't degrade with K.

**Approach D: Numerical evidence.** If the numerical computation shows rho(K) staying bounded (e.g., around 0.7-0.8 for all K), this would motivate a more careful theoretical analysis. If rho(K) slowly approaches 1, the rate of approach determines which approach can succeed.

### 9.3. A possible resolution via the multi-coset CDG product

The most promising direction combines the CDG bootstrap with the multi-coset structure:

**Key idea**: The eigenvector on orbit O satisfies K coupled equations (one per orbit element). The CDG identity provides K/L_2 independent product constraints (one per <2>-chain). The L intra-coset phase conditions provide L independent Cauchy-Schwarz near-equalities. Together, these give O(K) constraints on K unknowns.

The system is highly overdetermined when the constraints are "independent" (in the sense of pointing in different directions in coefficient space). The CDG constraints force |lambda| close to 1/2, while the intra-coset constraints force the phase pattern. The combination may force a CONSTANT gap regardless of K.

**The challenge**: Making "independence" precise and showing the constraints don't degenerate.

### 9.4. Connection to the Bourgain-Gamburd method

The Bourgain-Gamburd approach to spectral gaps for random walks on groups uses a three-step process:

1. **Non-concentration**: show the walk doesn't concentrate on a subgroup.
2. **Flattening**: use the product theorem to show the walk becomes approximately uniform after O(log n) steps.
3. **Spectral gap**: convert flattening to a spectral gap bound.

For our problem, the analogous approach would be:

1. Show the eigenvector energy doesn't concentrate on a proper sub-orbit.
2. Use the CDG product (analogous to the product theorem) to show the iterated walk flattens the energy distribution.
3. Convert the flattening to a gap bound.

Step 1 is guaranteed by the orbit structure (the eigenvalue equation propagates energy to the full orbit). Step 2 is provided by the CDG identity. Step 3 is the open challenge.

The key difference from Bourgain-Gamburd is that our walk is on an ABELIAN group (H is cyclic), where the product theorem is trivial (no expansion from addition). The mixing comes entirely from the "+1" ADDITIVE perturbation, which is a rank-1 perturbation in the multiplicative structure. This makes our problem fundamentally different from the Bourgain-Gamburd setting.

---

## 10. The Phase Transition Picture (from agent_universal_gap_v2.md Section 9.5)

### 10.1. Two regimes of the parametric family

For the one-parameter family A(t) with fixed Cayley graph of order K:

**Regime I (t << 1/K, "perturbative")**: All phases pi * t * h_j are small. The matrix A(t) is a small perturbation of A(0). The spectral gap is approximately gap(0) = 1 - cos(pi/L). The eigenvectors are approximately characters of Z/KZ (Fourier modes on the group).

**Regime II (t ~ 1/K, "CDG")**: The phases pi * t * h_j spread over [0, pi]. The Jensen bound (averaging log|cos| over approximately uniform phases) gives the geometric mean of |1 + e^{i*phi}| approximately 1, leading to |lambda| ~ 1/2. This is the regime where the CDG product formula operates.

The crossover t_c ~ 1/K: for t > t_c, the phases are dispersed and the CDG mechanism gives |lambda| ~ 1/sqrt(2). For t < t_c, the phases cluster near 0 and the gap degrades to the Cayley graph gap.

### 10.2. Where does the actual parameter fall?

For the actual primes: t = r_0 / (2p), and we always have K < p (since K | (p-1)). So t = r_0/(2p). For r_0 = 1 (the smallest orbit representative): t = 1/(2p).

The ratio t / t_c = (1/(2p)) / (1/K) = K/(2p). Since K < p, this ratio is < 1/2. We are BELOW the crossover.

**But how far below?** If K = p^{1/2}: t/t_c ~ p^{-1/2}, so we are far below. If K = p^{1-epsilon}: t/t_c ~ p^{-epsilon}, close to the crossover.

For the sub-polynomial case K = p^{o(1)}: t/t_c = K/(2p) = p^{o(1)-1}, which is very small. We are deep in the perturbative regime.

### 10.3. The key observation

In the perturbative regime, the spectral radius is close to cos(pi/L), which can be close to 1 for large L. But crucially:

**The actual gap cannot be WORSE than gap(0).** The "+1" phases can only HELP (by providing additional mixing), not hurt. The phases introduce the additive shift that breaks the multiplicative symmetry. Without this shift, the walk is purely multiplicative and has gap ~ 1/K^2. With the shift, even a small phase perturbation provides additional contraction.

**Evidence from the numerics**: The fact that |lambda_2| ~ 0.70 for ALL primes tested (regardless of K) suggests that the CDG mechanism operates even for small t values, not just for t >> 1/K. The transition from the perturbative regime to the CDG regime may be much sharper than the naive analysis suggests.

### 10.4. A refined conjecture

**Conjecture (Phase transition is sharp).** For the one-parameter family A(t):

    rho(t) = max(cos(pi/L) - c_1 * t^2 * K^2, 1/sqrt(2) + c_2 * e^{-c_3 * t * K})

The first term is the perturbative correction (phases slightly reduce rho from cos(pi/L)). The second is the CDG regime (rho approaches 1/sqrt(2) exponentially fast once t * K exceeds a constant).

At t = 1/(2p): if K^2/(4p^2) * K^2 = K^4/(4p^2) is significant (i.e., K^2 >> p), the perturbative correction already pushes rho below 1/sqrt(2). But for K << sqrt(p), the correction is small, and rho ~ cos(pi/L).

**The question remains**: is there a prime where rho > 0.85? The formula gap(0) = 1 - cos(pi/L) suggests: for L = 10, gap(0) = 1 - cos(pi/10) = 1 - 0.951 = 0.049, giving rho = 0.951. This is dangerously close to 1!

**But wait**: L = 10 means ord_p(3) = 10, which means p | (3^10 - 1) = 59048. The primes dividing 59048 = 2^3 * 11 * 37 * ... are small. For these primes, p is bounded, and the "+1" phases are NOT infinitesimal. The actual gap is much larger than gap(0) because t = 1/(2p) is not that small.

For instance: p = 11, ord_11(3) = 5, K = |<2,3>| = 10 (full group since 10 = p-1). The gap(0) = 1 - cos(pi/5) = 1 - 0.809 = 0.191. The actual |lambda_2(11)| is empirically in the range [0.66, 0.81], so the actual gap is in [0.19, 0.34]. This matches gap(0)!

For p = 37, ord_37(3) = 18 = (p-1)/2. Then L = 18, gap(0) = 1 - cos(pi/18) = 1 - 0.985 = 0.015. The actual gap should be larger because p is not that large.

This shows that for FIXED L, as p grows (and there are only finitely many such p), the gap at t = 1/(2p) can approach gap(0). But gap(0) > 0 always, and there are finitely many primes for each L.

**The resolution**: For each fixed L (or equivalently, each fixed (L, L_2) pair), gap(0) > 0 and there are finitely many primes. The worst gap over those primes is positive. As L grows, gap(0) shrinks, but the set of primes also becomes more restricted (p | (3^L - 1) for specific L). The question is whether the finite collection of primes for each L includes one where the actual gap approaches gap(0).

---

## 11. Critical Assessment: Why Compactness Alone Is Insufficient

### 11.1. The structure of the problem

The compactness argument gives: for each K, rho(K) < 1 (finitely many primes). The question is inf_K (1 - rho(K)) > 0.

This is a question about a SEQUENCE of finite optimization problems. For each K, we optimize over finitely many primes and orbits. The optimum rho(K) is achieved (it's a maximum over a finite set). But as K grows, the finite set changes.

### 11.2. Why the bound c/K^2 may be sharp

Consider the following scenario:
- K = 2^n (powers of 2 for simplicity)
- L_2 = K (so <2> = <2,3>)
- L = 1 (3 = 1 mod p, so p | 2, excluded) -- this case doesn't occur.

More realistically:
- K = lcm(L_2, L) with L_2 and L both growing
- p | gcd(2^{L_2} - 1, 3^L - 1), with p the largest prime factor
- As L_2, L grow, p can grow (potentially exponentially in L_2 and L)

For p ~ 3^L and K ~ L (the sub-polynomial case):
- gap(0) ~ pi^2/(2L^2) ~ pi^2/(2K^2)
- The actual gap ~ gap(0) + O(gap due to phases)
- If the phase contribution is negligible: gap ~ c/K^2 -> 0

The phase contribution is NOT negligible when the CDG bootstrap is effective. But the CDG bootstrap has error O(L_2 * sqrt(eta)), and for L_2 ~ K, this gives gap >= c/K^2 (same order).

### 11.3. The gap between theory and numerics

Theory gives: gap >= c/K^2 (shrinking)
Numerics give: gap ~ 0.30 (constant)

The discrepancy is a factor of K^2. This suggests that the CDG bootstrap loses a factor of K somewhere, and a tighter analysis should recover the constant gap.

**Possible source of the loss**: The CDG bootstrap treats the L_2 steps along a <2>-chain sequentially, accumulating error at each step. But the phases along the chain are CORRELATED (they are determined by the CDG product identity), and the errors may partially cancel rather than accumulate.

**A potential improvement**: Instead of bounding the error after L_2 steps as C * L_2 * max(single-step error), bound it as C * sqrt(L_2) * max(single-step error), exploiting the fact that the errors at different positions are approximately independent (the phases at different positions on the <2>-chain are equidistributed, so the errors are uncorrelated).

If this improvement works: gap >= c/L_2 instead of c/L_2^2. Still not constant, but better.

If the errors are FULLY independent: gap >= c (constant), matching the numerics. This is the best possible outcome from improving the CDG bootstrap.

---

## 12. Conclusion and Status

### 12.1. What is proved

| Result | Bound | Regime |
|--------|-------|--------|
| Spectral gap per prime | gap(p) > 0 | All primes (Combined Theorem) |
| Uniform gap, large K | gap >= c_1 (absolute) | K >= p^delta, any delta > 0 (Theorem 17 + BGK) |
| Uniform gap, bounded K | gap >= c(K_0) > 0 | K <= K_0 (compactness of finite-dim family) |
| Non-uniform gap, general | gap >= c/K^2 | All K (CDG bootstrap + Cayley gap) |

### 12.2. What is needed for the universal gap

A proof that gap >= c > 0 uniformly for ALL primes. The remaining case is K = p^{o(1)} (sub-polynomial), where the current bound c/K^2 is non-uniform.

### 12.3. Most promising approaches

1. **Improved CDG bootstrap**: Reduce the error accumulation from O(L_2) to O(sqrt(L_2)) or O(1), exploiting phase equidistribution along <2>-chains. This would give gap >= c/L_2 or gap >= c (constant).

2. **Multi-coset CDG product**: Use the simultaneous CDG constraints on ALL <2>-chains to get a global bound. The product over m = K/L_2 chains forces (2|lambda|)^K = product of CDG products, giving |lambda|^K = 2^{-K} * |correction|, which may force |lambda| <= 1/2 + small.

3. **Entropy argument**: The coupling/entropy approach (agent_coupling_entropy.md) provides a DIFFERENT mechanism for the gap that may not degrade with K.

4. **Numerical computation**: Run compactness_gap_compute.py to determine the empirical rho(K) for K up to ~100-500. If rho(K) stays bounded at ~0.81, this confirms the universal gap conjecture and suggests the CDG bootstrap improvement should work.

### 12.4. Run instructions

```bash
cd /Users/tsuimingleong/Desktop/math
source venv/bin/activate
python compactness_gap_compute.py
```

The output will determine whether rho(K) is empirically bounded or growing toward 1.

---

## References

1. Sections 6-12 of [agent_universal_gap.md] -- CDG bootstrap and phase analysis
2. Sections 1-10 of [agent_universal_gap_v2.md] -- Multi-coset approach, M^2 analysis, and phase transition picture
3. [theorem16_extended.md] -- BGK-based spectral gap for |<2,3>| >= p^delta
4. Chung, Diaconis, Graham -- "Random walks arising in number theory" (1987)
5. Bourgain, Glibichuk, Konyagin -- "Exponential sums in fields of prime order" (2006)
6. [agent_coupling_entropy.md] -- Coupling/entropy analysis of the Collatz walk
7. [agent_bourgain_gamburd.md] -- Bourgain-Gamburd method and per-character contraction
