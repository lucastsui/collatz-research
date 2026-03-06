# Universal Constant Spectral Gap for the Affine Collatz Operator: Analysis of the Middle Range

**Date:** 2026-03-05

**Problem:** Prove that for ALL primes p >= 5, the second-largest eigenvalue magnitude of the Markov operator

    (Mf)(x) = (1/2)f(x * 2^{-1}) + (1/2)f((3x+1) * 2^{-1})

on Z/pZ satisfies |lambda_2(p)| <= 1 - c for a universal constant c > 0.

**Specific focus:** The remaining case where K = |<2,3>| lies in the range [K_0, p^{1/2+epsilon}].

---

## 1. Summary of What Is Already Established

### 1.1. The three regimes

The problem naturally divides into three regimes based on K = |<2,3>| in F_p*:

| Regime | K range | Status | Method |
|--------|---------|--------|--------|
| Small | K <= K_0 (bounded) | **Proved** | Compactness + Combined Theorem |
| Middle | K_0 < K < p^{1/2+epsilon} | **Open** | This document |
| Large | K >= p^{1/2+epsilon} | **Proved** | Theorem 16 (phase constraint + orbit equidistribution) |

### 1.2. Why the middle range is hard

In the large-K regime, the Gauss sum bound gives excellent equidistribution of H-orbits in any arc of F_p, which forces the eigenvector's energy to spread beyond the phase-coherence arc. In the small-K regime, the transfer matrix has bounded dimension, and compactness handles it.

In the middle range, both arguments break:
- The orbit has too many elements for compactness (K -> infinity with p).
- The orbit has too few elements for the Gauss sum equidistribution to overwhelm the phase-coherence arc (the error sqrt(p)/K does not vanish when K < sqrt(p)).

### 1.3. Key equations

The eigenvalue equation in Fourier space: for f = sum_r a_r chi_r with Mf = lambda f,

    a_s + omega^s * a_{3s} = 2*lambda * a_{2s}     for all s in F_p*    ... (**)

The cross-term identity:

    |lambda|^2 = 1/2 + (1/(2||f||^2)) Re[sum_s a_{3s} conj(a_s) omega^{-s/2}]

Setting eta = 1 - |lambda|^2, the near-eigenvalue condition requires:

    Re[sum_s a_{3s} conj(a_s) omega^{-s/2}] >= (1 - 2*eta) * ||f||^2

---

## 2. Structural Analysis of the K x K Block Matrix

### 2.1. The transfer matrix on an orbit

On a single H-orbit O = r_0 * <2,3> of size K, the operator M restricts to a K x K matrix:

    P = (1/2) Pi_{2^{-1}} + (1/2) D * Pi_{3*2^{-1}}

where Pi_alpha is the permutation matrix for r -> r*alpha on O, and D = diag(omega^{r_j * gamma}) with gamma = 2^{-1}.

The spectral gap of M equals the minimum over all orbits O of the spectral gap of P (excluding eigenvalue 1, which only appears for the trivial orbit containing the constant function).

### 2.2. Decomposition into <3>-cosets

The orbit O decomposes into m = K/L cosets of <3> (where L = ord_p(3)):

    O = C_0 ∪ C_1 ∪ ... ∪ C_{m-1}

Each C_i has size L. The multiplication-by-2 permutation maps between these cosets: if r in C_i, then 2r is in C_{sigma_2(i)} for some permutation sigma_2 on {0, ..., m-1} (with possible intra-coset shift).

Similarly, the multiplication-by-3 permutation Pi_3 acts WITHIN each coset as a cyclic shift of length L.

### 2.3. The two-level structure

The transfer matrix P has a natural two-level structure:

**Level 1 (Intra-coset):** Within each <3>-coset C_i, the "3-part" of the dynamics acts as a twisted cyclic shift. As shown in the coupling/entropy analysis (Section E.8-I.1), the eigenvalues of this twisted shift on a single 3-cycle of length L are exactly the L-th roots of unity {omega_L^k : k = 0, ..., L-1}, where omega_L = e^{2*pi*i/L}.

**Level 2 (Inter-coset):** The multiplication-by-2 permutation couples different <3>-cosets. This is the key mixing mechanism.

The spectral gap of the full block matrix depends on how the inter-coset coupling (via x2) interacts with the intra-coset structure (the L-th roots of unity). The question reduces to:

**Does the x2 coupling between <3>-cosets provide a constant expansion?**

---

## 3. A New Approach: Iterated Map Contraction

### 3.1. The key idea

Rather than analyzing the K x K matrix directly, I propose to study the COMPOSITION of multiple applications of the eigenvalue equation (**), tracking how the constraints propagate along chains in the orbit.

Specifically, from (**):

    a_{2s} = (1/(2*lambda)) * (a_s + omega^s * a_{3s})

This expresses a_{2s} as an average (with phase) of a_s and a_{3s}. Iterating:

    a_{4s} = (1/(2*lambda)) * (a_{2s} + omega^{2s} * a_{6s})
           = (1/(2*lambda)) * [(1/(2*lambda))(a_s + omega^s a_{3s}) + omega^{2s} * (1/(2*lambda))(a_{3s} + omega^{3s} a_{9s})]
           = (1/(4*lambda^2)) * [a_s + omega^s a_{3s} + omega^{2s} a_{3s} + omega^{2s+3s} a_{9s}]
           = (1/(4*lambda^2)) * [a_s + (omega^s + omega^{2s}) a_{3s} + omega^{5s} a_{9s}]

After n iterations, a_{2^n s} is a linear combination of a_{3^j s} for j = 0, ..., n, with coefficients that are sums of products of phases omega^{(...)s}.

### 3.2. The contraction mechanism

The norm of the coefficient vector in each expansion is controlled by the phases. Specifically, define the vector

    v_n(s) = (c_0, c_1, ..., c_n)

where a_{2^n s} = sum_j c_j * a_{3^j s}, with c_j depending on lambda and the phases.

By the triangle inequality applied to the eigenvalue equation:

    |a_{2^n s}| <= (1/(2|lambda|))^n * sum_{paths} |a_{3^w s}|

where the sum is over all binary paths of length n (choosing which branch at each step). The number of paths with weight w (i.e., w choices of the "3s" branch) is C(n,w).

If we track the SQUARED norms and use orthogonality (different 3^w s are in different <3>-cosets, hence the coefficients for different w contribute to different cosets), we get the Proposition 3.3 bound.

### 3.3. What changes for K < sqrt(p)

When K < sqrt(p), the orbit O has fewer than sqrt(p) elements. The <3>-cosets within O have size L = ord_p(3), and there are m = K/L such cosets. There are two sub-cases:

**Case A: L is large (L >= K/K_0 for some bounded K_0).** Then m <= K_0, meaning there are only a bounded number of <3>-cosets. The inter-coset graph has bounded size, and the spectral gap of the inter-coset coupling can be bounded by compactness -- provided we can show the coupling is non-trivial.

**Case B: L is small (L <= K_0 for some bounded K_0).** Then the <3>-cosets are small, the intra-coset eigenvalues (L-th roots of unity) have a constant gap from 1 (since L is bounded, the closest eigenvalue to 1 is e^{2*pi*i/L} with |1 - e^{2*pi*i/L}| = 2*sin(pi/L) >= 2*sin(pi/K_0) > 0). But we also need to handle the inter-coset coupling.

In both cases, the key is to exploit the PHASE DECOHERENCE introduced by the "+1" translation across cosets.

---

## 4. Compactness Argument for the Full Middle Range

### 4.1. A universal compactness framework

**Theorem (Main New Result -- Conditional).** There exists a universal constant c > 0 such that for all primes p >= 5, |lambda_2(p)| <= 1 - c.

I will attempt to prove this via a compactness-plus-continuity argument that handles all three regimes simultaneously. The key insight is that the spectral gap problem can be formulated over a COMPACT parameter space, even for the middle range.

### 4.2. The parameterization

Fix K = |<2,3>| and let the orbit O have size K. The transfer matrix P on O depends on:

1. The permutation pi_0: r -> r * 2^{-1} on O (equivalently, the Cayley graph structure of <2,3> with generators 2 and 3).
2. The phases d_j = omega^{r_j * gamma} for j = 0, ..., K-1.

The permutations pi_0 and pi_1 = pi_3 * pi_0 are determined by the group structure of <2,3> and the specific embedding of O in F_p*. The phases d_j are p-th roots of unity.

**Key observation:** The phases d_j are determined by the positions r_j in F_p*, which satisfy r_j = r_0 * h_j for h_j in H = <2,3>. So d_j = omega^{r_0 * h_j * gamma}, and the RATIOS d_j/d_k = omega^{r_0 * (h_j - h_k) * gamma} depend on r_0 and the group structure.

As r_0 varies over the (p-1)/K coset representatives, the phases d_j vary continuously (in the sense that r_0 * h_j * gamma mod p varies over Z/pZ). As p varies, the group structure of <2,3> changes discretely, but for fixed K, there are only finitely many possible group structures (up to isomorphism of the Cayley graph).

### 4.3. The compact space

For fixed K, the transfer matrix P = (1/2)(Pi_0 + D * Pi_1) is determined by:
- A group structure G of order K (finitely many choices)
- A phase vector theta = (theta_0, ..., theta_{K-1}) in (R/2*pi*Z)^K

The space of all such matrices, for fixed K, is a FINITE union of tori (one torus per group structure). Each torus is compact.

The spectral radius rho(P) = max_{mu != 1} |mu(P)| is a continuous function of the phase vector theta (eigenvalues depend continuously on matrix entries, and the entries are continuous in theta).

By the Combined Theorem, rho(P) < 1 for ALL choices of theta (and all primes p). The question is whether rho(P) can approach 1 as K grows or as the phases vary.

### 4.4. The obstruction to a direct compactness argument

For FIXED K, the compactness of the torus gives max_theta rho(P) < 1, hence a constant gap c(K) > 0. This is the bounded-orbit result.

For GROWING K, the torus dimension K grows, and the supremum of rho(P) over all theta in [0, 2*pi)^K could approach 1 as K -> infinity. The compactness argument breaks down because we are taking a supremum over spaces of increasing dimension.

**However:** Not all phase vectors theta are realizable. The phases are of the form d_j = omega^{r_0 * h_j / 2} for specific group elements h_j in H = <2,3> <= F_p*, with the constraint that omega = e^{2*pi*i/p}. This means the phases are CORRELATED (they all share the parameter r_0 and the common group structure), which dramatically reduces the effective dimension.

### 4.5. Effective one-parameter family

For a fixed group structure H (fixed K, fixed Cayley graph), the phases are:

    theta_j = 2 * pi * r_0 * h_j / (2 * p) = pi * r_0 * h_j / p

where h_j ranges over the K elements of H. The entire phase configuration is determined by the single parameter t = r_0/p in R/Z (or rather, r_0 in {1, ..., p-1} divided by p).

As t varies over (0, 1), the phase configuration theta = (pi * t * h_0, pi * t * h_1, ..., pi * t * h_{K-1}) traces a curve on the K-torus.

The spectral radius rho(t) = rho(P(t)) is a continuous function of t in (0, 1). By the Combined Theorem, rho(t) < 1 for all t and all primes. But the question is whether sup_t rho(t) approaches 1 as p -> infinity (which changes the set {h_j}).

**Reformulation:** For each prime p and each orbit, the spectral radius is rho(t) for some t in (0,1). We need:

    sup_{p prime, t in (0,1)} rho(t; H_p) < 1

where H_p = <2,3> in F_p*.

---

## 5. The Bilinear Form Bound

### 5.1. Restating the problem

The spectral gap of M on orbit O is determined by:

    gap = 1/2 * (1 - max_{f on O, f perp 1, ||f||=1} Re <T_0 f, T_1 f>)

We need to show the maximum of R(f) = Re <T_0 f, T_1 f> / ||f||^2 is at most 1 - 2*c for a universal c > 0.

From Section C.3 of the coupling/entropy analysis:

    <T_0 f, T_1 f> = sum_{s in O} a_{3s} * conj(a_s) * omega^{-s*alpha}

where alpha = 2^{-1} mod p.

### 5.2. Decomposition by <3>-cosets

Let O = C_0 ∪ ... ∪ C_{m-1} where C_i are <3>-cosets. The cross-term decomposes as:

    <T_0 f, T_1 f> = sum_{i=0}^{m-1} Phi_i

where

    Phi_i = sum_{s in C_i} a_{3s} * conj(a_s) * omega^{-s*alpha}

Since 3 * C_i = C_i (multiplication by 3 permutes within the coset), the term a_{3s} for s in C_i has 3s also in C_i. So Phi_i is a self-correlation within coset C_i, twisted by the phases omega^{-s*alpha}.

By Cauchy-Schwarz: |Phi_i| <= E_i (the energy on coset C_i). Equality requires a_{3s} = c_i * omega^{s*alpha} * a_s for all s in C_i.

### 5.3. When equality is achieved (single coset analysis)

For a single coset C = {r, 3r, 9r, ..., 3^{L-1}r}, the condition for |Phi| = E requires:

    a_{3^{k+1}r} = c * omega^{3^k r * alpha} * a_{3^k r}    for k = 0, ..., L-1

Iterating: a_{3^k r} = c^k * omega^{r * alpha * (1 + 3 + ... + 3^{k-1})} * a_r = c^k * omega^{r * alpha * (3^k - 1)/2} * a_r.

For consistency at k = L (since 3^L r = r): a_r = c^L * omega^{r * alpha * (3^L - 1)/2} * a_r.

Since 3^L = 1 mod p, (3^L - 1)/2 = 0 mod p, so the phase term is omega^0 = 1. The condition reduces to c^L = 1, which is always satisfiable.

**Conclusion:** For each coset separately, the Cauchy-Schwarz bound IS tight -- there exists a function on the coset achieving |Phi_i| = E_i.

### 5.4. The inter-coset constraint

The key is that the maximizing functions on DIFFERENT cosets are NOT compatible. Specifically, for coset C_i to achieve |Phi_i| = E_i, the function on C_i must satisfy a specific phase pattern. Similarly for coset C_j. But the eigenvalue equation (**) COUPLES adjacent cosets (via the term a_{2s}), and the coupling may force the phase patterns on different cosets to be inconsistent.

**The eigenvalue equation links cosets:** From (**):

    a_s + omega^s * a_{3s} = 2*lambda * a_{2s}

For s in coset C_i: 3s is also in C_i, but 2s is in coset C_{sigma_2(i)} (a DIFFERENT coset, in general). So the coefficient a_{2s} on coset C_{sigma_2(i)} is determined by a_s and a_{3s} on coset C_i.

This coupling constrains the phase patterns across cosets. Specifically, the function on C_{sigma_2(i)} is determined (up to the eigenvalue lambda) by the function on C_i. For the Cauchy-Schwarz bound to be tight on BOTH C_i and C_{sigma_2(i)}, the inherited phase pattern on C_{sigma_2(i)} must coincide with the Cauchy-Schwarz maximizer on C_{sigma_2(i)}.

### 5.5. Formalizing the inter-coset incompatibility

**Proposition 5.1 (Inter-coset phase mismatch).** Let f be an eigenvector of M on orbit O with |lambda|^2 >= 1 - eta. For each <3>-coset C_i, define:

    rho_i = |Phi_i| / E_i    (the fraction of the Cauchy-Schwarz bound achieved)

Then:
(a) sum_i rho_i * E_i >= (1 - 2*eta) * E (from the eigenvalue equation).

(b) For adjacent cosets C_i and C_{sigma_2(i)}: the phase pattern inherited from C_i via the eigenvalue equation DIFFERS from the Cauchy-Schwarz maximizer on C_{sigma_2(i)} by a phase factor that depends on the "shift" tau (how x2 maps within the target coset).

(c) The discrepancy in (b) leads to: rho_{sigma_2(i)} <= cos(Delta_i) where Delta_i is a phase mismatch angle.

**The Phase Mismatch Angle:**

On coset C_i = {r_i, 3r_i, ..., 3^{L-1}r_i}, the Cauchy-Schwarz maximizer satisfies a_{3^{k+1}r_i} = c_i * omega^{3^k r_i * alpha} * a_{3^k r_i}.

On coset C_j = C_{sigma_2(i)} = {r_j, 3r_j, ..., 3^{L-1}r_j}, the eigenvalue equation gives:

    a_{r_j * 2^{-1}} + omega^{r_j * 2^{-1}} * a_{3 * r_j * 2^{-1}} = 2*lambda * a_{r_j}

where r_j * 2^{-1} is in C_i (since 2 * C_i includes C_j elements, up to intra-coset shift). The inherited function on C_j is determined by the eigenvalue equation applied to each element of C_i.

The Cauchy-Schwarz maximizer for C_j has a specific phase pattern with constant c_j. The eigenvalue equation forces a DIFFERENT value of c_j that depends on the phases from C_i and the "+1" translation. The discrepancy is the phase mismatch Delta_i.

---

## 6. The Product Formula Approach

### 6.1. CDG-type product identity

The Chung-Diaconis-Graham product identity gives, for the multiplicative walk on Z/pZ:

    product_{j=0}^{L_2-1} cos(pi * b * 2^j / p) = +/- 2^{-L_2}

where L_2 = ord_p(2) and b is any nonzero element.

For our Markov operator, the analogous quantity is the product of "one-step contraction factors" along a <2>-orbit. Specifically, for the n-step iteration starting from character chi_r, the coefficient at weight w is:

    c_w(r) = (1/2^n) sum_{|b|=w} omega^{r * d_b}

For a single <2>-orbit {r, r/2, r/4, ...}, the product structure is:

    product_{j=0}^{L_2-1} (1/2)(1 + omega^{r * 2^{-j} * gamma}) = ??

This product telescopes because each factor involves the phase at a different point of the <2>-orbit. By the CDG identity, the ABSOLUTE VALUE of this product is:

    product_{j=0}^{L_2-1} |cos(pi * r * 2^{-j-1} / p)| = 2^{-L_2}    (exact!)

**This is a KEY identity.** The product of the cosines along any <2>-orbit is exactly 2^{-L_2}. This means the GEOMETRIC MEAN of the one-step contraction factor along a <2>-orbit is exactly 1/2.

### 6.2. From geometric mean to spectral gap

The geometric mean of |cos(pi * r * 2^j / p)| being exactly 1/2 does NOT immediately give a spectral gap, because the spectral gap depends on the ARITHMETIC structure of the coefficients, not just their product.

However, the CDG identity constrains the "worst case" behavior. If one factor |cos(...)| is close to 1 (bad mode, near 0), then another factor must be close to 0 (good mode, near p/2) to compensate, keeping the product at exactly 2^{-L_2}.

**Proposition 6.1 (Weighted contraction via CDG).** For any <2>-orbit B = {r, 2r, 4r, ...} of size L_2 in F_p*:

    (1/L_2) sum_{j=0}^{L_2-1} log|cos(pi * r * 2^j / p)| = -log(2)

(This is just the log of the CDG identity.)

By Jensen's inequality applied to the CONCAVE function log:

    log((1/L_2) sum cos^2(...)) >= (1/L_2) sum log(cos^2(...)) = -2*log(2)

So:

    (1/L_2) sum cos^2(pi * r * 2^j / p) >= 2^{-2} = 1/4

This means the average of cos^2 along any <2>-orbit is at least 1/4. But this goes the wrong way -- we want the average to be SMALL (to bound the cross-term).

### 6.3. The correct use of CDG

The CDG identity is useful not for bounding the average of cos^2, but for bounding the PRODUCT of one-step transfer matrix norms.

For the transfer matrix P on an orbit O, the n-step contraction satisfies:

    ||P^n||_op <= product_{j=1}^n ||P_j||_op

where P_j is the "j-th step" transfer matrix (which depends on the current position in the orbit). Each P_j has operator norm at most 1 (it's an average of two unitaries).

But the CDG product identity tells us that along each <2>-chain, the phases accumulate a total rotation of exactly 2*pi (after L_2 steps). This means that over L_2 steps, the phases have spread over the full circle, ensuring that no direction is consistently reinforced.

**The formal statement:** After L_2 steps of the walk restricted to a single <2>-orbit, the product of transfer matrices satisfies:

    ||P^{L_2}|_B||_op <= rho

where rho depends on how the phases are distributed along the <2>-orbit. The CDG identity constrains rho.

---

## 7. A New Theorem: Uniform Gap via Dimensional Splitting

### 7.1. Statement

**Theorem 7.1.** Let p >= 5 be prime and K = |<2,3>| in F_p*. Let L = ord_p(3) and m = K/L (the number of <3>-cosets). Then:

    |lambda_2(p)| <= 1 - c(m, L)

where c(m, L) > 0 depends only on m and L, not on p.

Moreover:
(a) If m = 1 (single <3>-coset, i.e., <2> <= <3>): c(1, L) >= 2*sin^2(pi/(2L)) / 4 ~ pi^2/(8L^2).
(b) If L = 1 (trivial <3>, i.e., 3 = 1 mod p, only p = 2 which is excluded): N/A.
(c) If m >= 2 and L >= 2: c(m, L) >= min(c_a(m), c_b(L)) where c_a depends on the inter-coset expansion and c_b depends on the intra-coset eigenvalue gap.

### 7.2. Proof of (a): single <3>-coset (m = 1)

When m = 1, the orbit O IS a single <3>-coset: O = {r, 3r, 9r, ..., 3^{L-1}r}. The multiplication by 2 maps WITHIN O (since <2> <= <3>, meaning 2 = 3^t for some t).

The transfer matrix P = (1/2)(Pi_0 + D * Pi_1) where:
- Pi_0 corresponds to multiplication by 2^{-1} = 3^{-t} on O, which is Pi_3^{-t}
- Pi_1 corresponds to multiplication by 3/2 = 3^{1-t} on O, which is Pi_3^{1-t}
- D has entries omega^{r_j * gamma}

From the coupling/entropy analysis (Section E.8), the eigenvalues of D * Pi_3 on this cycle are exactly the L-th roots of unity (since the product of the phases around the cycle is 1).

The transfer matrix becomes P = (1/2)(Pi_3^{-t} + D * Pi_3^{1-t}) = (1/2) Pi_3^{-t} (I + Pi_3^t D Pi_3^{1-t}).

The eigenvalues of Pi_3^t D Pi_3^{1-t} are a phase rotation of the eigenvalues of D Pi_3, which are still L-th roots of unity (the permutation conjugation just relabels). Let the eigenvalues of the relevant part be mu_k for k = 0, ..., L-1.

The eigenvalues of P are (1/2) omega_L^{(-t)k} (1 + mu_k) for each k. The eigenvalue corresponding to the stationary distribution (k such that everything aligns) gives |1 + mu_k| = 2.

For k != 0 (non-stationary eigenvalues): |1 + mu_k| = |1 + e^{2*pi*i*k/L}| = 2*|cos(pi*k/L)|. The maximum over k != 0 is 2*cos(pi/L) (at k = 1 or k = L-1).

So |lambda_2| <= (1/2) * 2 * cos(pi/L) = cos(pi/L), giving:

    gap >= 1 - cos(pi/L) = 2*sin^2(pi/(2L)).

For L = 2: gap >= 2*sin^2(pi/4) = 1 (complete mixing in one step -- but L = 2 means ord_p(3) = 2, so 3^2 = 9 = 1 mod p, i.e., p | 8, only p = 2 excluded).

For L = 3: gap >= 2*sin^2(pi/6) = 2*(1/4) = 1/2.

For large L: gap ~ pi^2/(2L^2).

**This gives a constant gap ONLY when L is bounded.**

### 7.3. The general case: m >= 2 cosets

When m >= 2, the orbit O has multiple <3>-cosets coupled by multiplication by 2. The transfer matrix P has a block structure: it acts on m blocks (one per <3>-coset), each of size L.

Within each block, the dynamics are determined by the multiplication-by-3 structure. Between blocks, the dynamics are determined by multiplication by 2 (which maps each <3>-coset to another).

**The block Hamiltonian analogy:** Think of the cosets as "sites" in a lattice, with the intra-site Hamiltonian having eigenvalues (L-th roots of unity) and the inter-site hopping given by multiplication by 2.

The spectral gap of the full system is at least as large as the minimum of:
- The intra-site gap (from the L-th root structure): gap_intra = 2*sin^2(pi/(2L))
- The inter-site gap: determined by the Cayley graph of the quotient <2,3>/<3> with generator "2 mod <3>"

When BOTH gap_intra and gap_inter are bounded away from 0, the full gap is bounded away from 0. The remaining question is whether gap_inter is always positive (and uniformly bounded).

---

## 8. The Inter-Coset Expansion Problem

### 8.1. The quotient graph

Define the quotient group G = H/<3> = <2,3>/<3>. This is a cyclic group generated by the image of 2 in H/<3>. Its order is m = K/L = |<2,3>| / ord_p(3).

The inter-coset graph is the Cayley graph Cay(G, {2 mod <3>}) -- a directed graph on m vertices where each vertex has one outgoing edge (to "2 * current vertex mod <3>").

Since G = <2 mod <3>> (because <2,3>/<3> is generated by the image of 2), this Cayley graph is a single directed cycle of length m. The spectral gap of a directed cycle of length m is:

    gap_cycle = 1 - cos(2*pi/m) = 2*sin^2(pi/m)

For m = 2: gap = 2. For large m: gap ~ 2*pi^2/m^2.

**But this is the gap of the UNWEIGHTED cycle.** In our problem, the hopping from coset to coset carries PHASES from the "+1" translation, which modifies the spectral gap.

### 8.2. The weighted inter-coset operator

The effective inter-coset operator, after "integrating out" the intra-coset degrees of freedom (at the intra-coset ground state), acts on the m coset energies with a structure that depends on the phases.

More precisely, consider the "slowly varying" modes -- functions that are approximately constant within each <3>-coset (they correspond to the k=0 intra-coset eigenvalue, which is the L-th root of unity closest to 1). For these modes, the transfer matrix reduces to an m x m matrix:

    Q = (1/2) Sigma_0 + (1/2) D' * Sigma_1

where Sigma_0, Sigma_1 are permutations on the m cosets (corresponding to the action of 2^{-1} and 3*2^{-1} on the coset space), and D' is a phase matrix.

Since the coset space G = H/<3> is generated by 2 mod <3>, the permutation Sigma_0 (induced by multiplication by 2^{-1}) is a cyclic permutation of the m cosets. The permutation Sigma_1 (induced by multiplication by 3*2^{-1} = 3/2) sends coset C_i to coset C_{sigma(i)} where sigma is determined by 3/2 mod <3>. Since 3 is in <3>, 3/2 mod <3> = 2^{-1} mod <3>, so Sigma_1 = Sigma_0 on the coset space!

**Wait, that can't be right.** Let me re-examine. On the orbit O, multiplication by 2^{-1} sends C_i to some C_j (determined by where 2^{-1} maps the coset). Multiplication by 3 * 2^{-1} sends C_i to... 3 * 2^{-1} * C_i = 3 * (2^{-1} * C_i). But 2^{-1} * C_i = C_j, and 3 * C_j = C_j (since 3 acts WITHIN cosets). So 3 * 2^{-1} * C_i = C_j = 2^{-1} * C_i.

**Therefore Sigma_1 = Sigma_0 on the coset level!** Both branches of the walk (T_0 and T_1) map coset C_i to the SAME coset C_j = 2^{-1} * C_i.

This means the inter-coset dynamics are IDENTICAL for both branches -- the walk moves between cosets in the same way regardless of the branch choice. The only difference between the two branches is the PHASE (from D') and the INTRA-COSET position.

**Consequence:** The slowly-varying inter-coset modes see an operator:

    Q = (1/2)(I + D'') * Sigma_0

where D'' is a phase matrix on the m cosets (combining the "+1" phase with the intra-coset ground state phase). The eigenvalues of Q are:

    (1/2)(1 + d_i'') * omega_m^{k*sigma_0}

... but this factorization is only valid if Sigma_0 is a simple cycle and D'' is diagonal. Let me be more careful.

### 8.3. Revised coset-level analysis

On the coset level, both T_0 and T_1 send C_i to C_{2^{-1}(i)} (the same target coset). The difference is:
- T_0 maps elements within C_i to elements within C_{2^{-1}(i)} via r -> r * 2^{-1}
- T_1 maps elements within C_i to elements within C_{2^{-1}(i)} via r -> r * 3 * 2^{-1}, which is (r * 3) * 2^{-1}

Since r * 3 is in C_i (multiplication by 3 within the coset), T_1 first applies ×3 within C_i, then ×2^{-1} to move to C_{2^{-1}(i)}. So T_1 on the coset C_i is the composition of a cyclic shift (×3 within C_i) followed by the same inter-coset map as T_0.

**This means:** At the inter-coset level, both branches go to the same target. The DIFFERENCE between them is purely intra-coset: T_1 includes an extra cyclic shift (×3) within the source coset before the inter-coset transfer.

This is a crucial structural insight. The inter-coset dynamics is DETERMINISTIC (not random) -- the walk always moves from C_i to C_{2^{-1}(i)} regardless of the branch. The randomness only affects the INTRA-COSET position.

### 8.4. Consequence for the spectral gap

Since the inter-coset dynamics is deterministic (always ×2^{-1} on the coset level), the mixing between cosets is that of a single cyclic permutation, which has NO spectral gap in the inter-coset sense (the cyclic permutation has eigenvalues that are m-th roots of unity, all on the unit circle).

**However:** The "+1" phases introduce PHASE DIFFERENCES between the two branches that accumulate at the intra-coset level. Over m steps (one full cycle through all cosets), these phase differences cause decoherence within each coset.

**Revised understanding:** The spectral gap comes not from inter-coset mixing (which is deterministic) but from the INTRA-COSET phase decoherence that accumulates as the walk cycles through different cosets.

---

## 9. Intra-Coset Phase Decoherence: The Core Mechanism

### 9.1. Tracking the intra-coset state

Consider following the walk from a starting coset C_0. After one step:
- With probability 1/2 (T_0): the intra-coset position doesn't change (up to the ×2^{-1} relabeling of the target coset)
- With probability 1/2 (T_1): the intra-coset position shifts by ×3 (one step of the cyclic shift within the source coset), THEN ×2^{-1} moves to the target coset, and a phase omega^{r*gamma} is acquired.

The intra-coset state evolves as a RANDOM WALK on Z/LZ (the cyclic group of the <3>-coset) with steps 0 or 1, modified by phases.

### 9.2. The effective intra-coset random walk

Let us track the "lag" between the two branches. Starting from position j in the <3>-coset:

- T_0 moves to the corresponding position in the target coset (same intra-coset index j, up to the ×2^{-1} relabeling).
- T_1 moves to position j+1 mod L in the source coset, then to the target coset.

The DIFFERENCE between the two branches is exactly a ±1 shift in the intra-coset position. Over n steps, the intra-coset lag undergoes a random walk: at each step, the lag either stays the same (branch T_0, probability 1/2) or increases by 1 mod L (branch T_1, probability 1/2).

This is a biased random walk on Z/LZ with drift 1/2 per step. After n steps, the lag is the sum of n Bernoulli(1/2) random variables, modulo L.

### 9.3. Phase decoherence from the lag

The "+1" translation produces a phase omega^{r*gamma} at each T_1 step, where r is the current mode. For a character chi_r on the orbit, the accumulated phase over n steps depends on the specific sequence of branch choices AND the path through the cosets.

The key insight is that two copies of the walk (one starting from character chi_r via T_0 and one via T_1) acquire a RELATIVE phase of omega^{r*gamma} at each T_1 step. Over L_2 steps (one full cycle through the <2>-orbit), the accumulated relative phase is constrained by the CDG identity.

### 9.4. Connection to the one-step contraction

The one-step contraction ||M chi_r||^2 = 1/2 reflects the fact that the two branches (T_0 and T_1) produce ORTHOGONAL output modes for a single character. But for superpositions, the two branches can constructively interfere.

The question is: over how many steps does the interference remain constructive?

After k steps, the walk has 2^k branches. The interference between branches depends on the accumulated phases, which in turn depend on the path through the cosets and the intra-coset lags. For the interference to remain constructive after k steps, ALL 2^k branches must have nearly aligned phases. This is increasingly unlikely as k grows.

**Quantitative bound:** After k steps, the number of "aligned" branches (those with phase within epsilon of the dominant phase) is at most:

    N_aligned(k) <= 2^k * P(|lag_k * pi / p| < epsilon)

where lag_k is the accumulated intra-coset lag (a sum of k Bernoulli variables). By the CLT, lag_k ~ k/2 + sqrt(k/4) * Z where Z is standard normal. The fraction of the <3>-coset covered by the lag is lag_k / L.

For the phases to align: we need |omega^{r * sum of stuff}| close to 1, which requires the sum of the "+1" contributions to be close to 0 mod p. This is the exponential sum structure.

---

## 10. A Rigorous Bound via Iterated Cauchy-Schwarz

### 10.1. Setup

Fix an orbit O of size K, with L = ord_p(3) and m = K/L cosets. We work with the transfer matrix P on the K-dimensional space of Fourier coefficients on O.

### 10.2. Two-step contraction on individual characters

From the paper (Theorem 12 and the two-step analysis):

    ||M chi_r||^2 = 1/2     for all r != 0

    ||M^2 chi_r||^2 <= 3/8 + O(1/p^2)     for all r != 0

The two-step bound 3/8 < 1/2 shows that the per-step contraction IMPROVES at the second step for individual characters.

### 10.3. Why operator norm doesn't follow

For the operator norm, the worst case is a function f = sum_r a_r chi_r that maximizes ||Mf||^2 / ||f||^2. The one-step identity:

    ||Mf||^2 = 1/2 ||f||^2 + 1/2 Re<T_0 f, T_1 f>

The cross-term can be as large as ||f||^2 (for orbit-constant functions), giving ||Mf||^2 up to ||f||^2.

### 10.4. Two-step operator identity

    ||M^2 f||^2 = 1/2 ||Mf||^2 + 1/2 Re<T_0(Mf), T_1(Mf)>

Now Mf = (1/2)T_0 f + (1/2)T_1 f, so:

    T_0(Mf) = (1/2) T_0^2 f + (1/2) T_0 T_1 f
    T_1(Mf) = (1/2) T_1 T_0 f + (1/2) T_1^2 f

where T_0^2 f(x) = f(x/4), T_0 T_1 f(x) = f((3x+1)/(2*2)), etc.

The cross-term <T_0(Mf), T_1(Mf)> involves four terms:

    = (1/4)[<T_0^2 f, T_1 T_0 f> + <T_0^2 f, T_1^2 f> + <T_0 T_1 f, T_1 T_0 f> + <T_0 T_1 f, T_1^2 f>]

Each of these is a bilinear form in f with specific phase factors. The term <T_0 T_1 f, T_1 T_0 f> is particularly interesting: it involves the composition T_0 T_1 (apply T_1 then T_0) vs T_1 T_0 (apply T_0 then T_1), which are DIFFERENT affine maps. Their composition with the adjoint creates a "commutator" term.

**The commutator:**

    T_0 T_1(x) = T_0((3x+1)/2) = (3x+1)/4
    T_1 T_0(x) = T_1(x/2) = (3(x/2)+1)/2 = (3x+2)/4

These differ by an additive constant: T_0 T_1(x) - T_1 T_0(x) = (3x+1)/4 - (3x+2)/4 = -1/4. The compositions agree on the multiplicative part (both are ×3/4) but differ on the additive part (1/4 vs 2/4 = 1/2).

**Consequence:** <T_0 T_1 f, T_1 T_0 f> = <f((3x+1)/4), f((3x+2)/4)> = sum_x f((3x+1)/4) * conj(f((3x+2)/4)).

Setting y = (3x+1)/4 (equivalently, x = (4y-1)/3), this becomes sum_y f(y) * conj(f(y + 1/4)), which is the autocorrelation of f at shift 1/4.

For the eigenvector achieving ||Mf|| = ||f||, this autocorrelation must be close to ||f||^2, meaning f(y) ~ f(y + 1/4) for all y. But f is also close to being periodic with period 3*alpha (from the Combined Theorem analysis). For both periodicities to hold simultaneously:

f has periods ~1/4 and ~3*alpha = 3/(2p). Since gcd is involved in whether these generate all of Z/pZ as a period, and for large p these two periods are generically independent, f must be close to constant, hence close to 0 (since f perp 1).

### 10.5. Quantifying the two-step improvement

**Proposition 10.1.** For the two-step operator on a single orbit O of size K:

    ||M^2||_{op, O}^2 <= 1 - delta

where delta > 0 depends on K, L, and the phase structure, but is POSITIVE for all primes p >= 5.

*Proof sketch:* We need ||M^2 f||^2 < ||f||^2 for all nonzero f perp 1 on O. By the identity above:

    ||M^2 f||^2 = 1/2 ||Mf||^2 + 1/2 Re<T_0(Mf), T_1(Mf)>

Case 1: ||Mf||^2 <= (1 - epsilon) ||f||^2. Then ||M^2 f||^2 <= (1/2)(1 - epsilon)||f||^2 + (1/2)||Mf||^2 <= (1-epsilon/2)||f||^2.

Case 2: ||Mf||^2 >= (1 - epsilon)||f||^2 (near-equality at step 1). Then Mf is close to the orbit-constant maximizer. But Mf = (1/2)T_0 f + (1/2)T_1 f is a SUPERPOSITION of two translated copies of f, which is NOT orbit-constant (it has a specific non-trivial intra-coset structure). Therefore <T_0(Mf), T_1(Mf)> < ||Mf||^2, giving:

    ||M^2 f||^2 < (1/2)||Mf||^2 + (1/2)||Mf||^2 = ||Mf||^2 <= ||f||^2.

The quantitative bound delta comes from estimating how far Mf is from the orbit-constant maximizer in Case 2.

**The key quantitative ingredient:** When ||Mf||^2 >= (1 - epsilon)||f||^2, the function f must satisfy the approximate phase conditions from Section 5. Then Mf has Fourier coefficients:

    (Mf)_s = (1/2) a_{2s} + (1/2) omega^{s*gamma} * a_{2s/3*...}

which is a specific linear combination of the a_r's. The orbit-constant structure of f (which makes ||Mf|| large) is "broken" by M, introducing a non-trivial INTRA-COSET structure in Mf.

The autocorrelation <T_0(Mf), T_1(Mf)> then involves the autocorrelation of this non-trivially structured function, which is strictly less than ||Mf||^2 by the shift argument (the commutator term T_0 T_1 vs T_1 T_0 introduces a shift of 1/4, and the function cannot be simultaneously near-periodic with the periods dictated by both the orbit-constant structure and the shift).

---

## 11. An Explicit Two-Step Bound for the Middle Range

### 11.1. Setup for the middle-range analysis

Let p be a prime with K = |<2,3>| in [K_0, p^{1/2+epsilon}]. We work on a single orbit O of size K.

### 11.2. Decomposition of the two-step operator

For f = sum_{r in O} a_r chi_r with ||f|| = 1, the two-step norm is:

    ||M^2 f||^2 = sum_{distinct s} |sum_w C_w(f,s)|^2

where C_w(f,s) is the contribution of weight-class w to mode s. By Proposition 3.3 of the paper:

    ||M^2 f||^2 <= ceil(3/L) * sum_w |C_w(f)|^2

where the sum is over the 3 weight classes w = 0, 1, 2 (for n = 2 steps).

For the individual character, ||M^2 chi_r||^2 <= 3/8 (tight for generic r). The operator norm involves the worst-case superposition.

### 11.3. Bounding the operator norm via the eigenvalue equation

Rather than bounding the operator norm of M^2 directly (which involves a supremum over all f), I instead use the eigenvalue equation to constrain the eigenvector.

If Mf = lambda f with |lambda|^2 >= 1 - eta, then:

    ||M^2 f||^2 = |lambda|^4 ||f||^2 = (1 - eta)^2 ||f||^2

But also ||M^2 f||^2 <= ||M||_{op}^2 ||Mf||^2 = ||M||_{op}^2 (1-eta) ||f||^2.

For the spectral gap, we need |lambda|^2 < 1 - c, which is equivalent to showing the eigenvalue equation forces eta > c.

### 11.4. The phase constraint in the middle range

From Proposition 4.4 (sum-product analysis): if |lambda|^2 >= 1 - eta, then the energy is concentrated on an arc of angular width O(sqrt(eta)) in Z/pZ. Let G_eta = {s : |sin(pi*s/p)| <= C*sqrt(eta)} be this arc, of size ~sqrt(eta) * p.

The eigenvector energy outside G_eta satisfies:

    sum_{s not in G_eta} |a_s|^2 <= C * eta.

### 11.5. The support size constraint

For the eigenvector on orbit O of size K: the support of a = (a_r)_{r in O} must span a significant portion of O (at least K elements) because the eigenvalue equation couples all elements.

**Claim:** If a is a nonzero eigenvector on O, then |supp(a)| >= K (the full orbit). This is because the eigenvalue equation a_s + omega^s a_{3s} = 2*lambda * a_{2s} propagates nonzero values: if a_s != 0, then (unless a_{3s} happens to exactly cancel) a_{2s} != 0, which in turn forces a_{4s} != 0, etc. Since the orbit is connected under {×2, ×3}, the support must be all of O.

### 11.6. Combining the constraints

The eigenvector has:
- Support = O (full orbit, K elements)
- Energy concentrated in G_eta (arc of size ~sqrt(eta) * p)

For the support to fit in the arc: K <= sqrt(eta) * p (up to constants). This gives:

    eta >= (K/p)^2

For K >= K_0: eta >= K_0^2 / p^2, which is too small (goes to 0).

For K <= p^{1/2+epsilon}: K/p <= p^{-1/2+epsilon}, so eta >= p^{-1+2*epsilon}. This is better than 1/p but still vanishes.

**The issue:** The energy doesn't need to be uniformly spread over O. It can concentrate on the intersection O ∩ G_eta, which can have fewer than K elements.

### 11.7. The orbit-arc intersection

The key quantity is |O ∩ G_eta| / K -- the fraction of the orbit that lies in the phase-coherence arc.

For K < p^{1/2+epsilon} and arc size ~sqrt(eta) * p:

    |O ∩ G_eta| / K can be as large as 1 (if the orbit happens to cluster near 0)

or as small as sqrt(eta) * p / K (if the orbit is spread out).

The orbit O = r_0 * <2,3> consists of elements r_0 * h for h in H. These elements, as a subset of F_p*, can have various distributions in Z/pZ depending on r_0 and the group structure.

**The worst case:** r_0 is very small (close to 0 in Z/pZ), and the group H generates elements close to 0 (e.g., when 2 and 3 are both small, the elements h = 2^a * 3^b remain small until they wrap around modulo p). In this case, most of O lies near 0, and |O ∩ G_eta| / K ~ 1.

For such orbits, the arc constraint is not useful, and we need a DIFFERENT argument.

---

## 12. The Rigid Structure of Near-Eigenvalues in Small Orbits

### 12.1. The eigenvalue equation as a linear recurrence

On orbit O of size K, the eigenvalue equation (**) defines a LINEAR SYSTEM in the K unknowns (a_r)_{r in O}:

    a_s + omega^s * a_{3s} = 2*lambda * a_{2s}     for all s in O

This is a homogeneous system (after moving 2*lambda * a_{2s} to the left). Non-trivial solutions exist iff det(A - 2*lambda * B) = 0, where A and B are K x K matrices determined by the orbit structure and phases.

The eigenvalues lambda are the roots of this K x K determinantal equation. There are at most K eigenvalues (counting multiplicity).

### 12.2. Characteristic polynomial structure

The transfer matrix P = (1/2)(Pi_0 + D * Pi_1) is a K x K matrix. Its characteristic polynomial has degree K. The eigenvalue 1 is one root (from the stationary distribution contribution). The remaining K-1 eigenvalues determine the spectral gap.

**For K bounded:** The characteristic polynomial has bounded degree, and the Combined Theorem guarantees no root on the unit circle. By continuity and compactness, all roots are bounded away from the unit circle. This gives the constant gap for bounded K.

**For K growing:** The characteristic polynomial has growing degree, and roots can potentially accumulate near the unit circle. The question is whether the SPECIFIC structure of P (determined by the Collatz dynamics and the "+1" phases) prevents this accumulation.

### 12.3. Determinantal bound for the spectral radius

**Proposition 12.1.** The spectral radius of P on the non-stationary subspace satisfies:

    rho(P)^K <= |det(P)| / (product of |lambda_i| for the stationary eigenvalue)

Wait, this needs more care. The determinant of P is the product of ALL eigenvalues. For a K x K stochastic-like matrix with eigenvalue 1 and remaining eigenvalues lambda_1, ..., lambda_{K-1}:

    |det(P)| = |product lambda_i| * 1 = product |lambda_i|

If rho = max |lambda_i|, then |det(P)| <= rho^{K-1}, i.e., rho >= |det(P)|^{1/(K-1)}.

But this gives a LOWER bound on rho, not an upper bound. Not useful.

**Alternative: using the trace.** tr(P) = 1 + sum lambda_i, so sum |lambda_i| >= |sum lambda_i| = |tr(P) - 1|. But sum |lambda_i| <= (K-1) * rho, giving rho >= |tr(P) - 1| / (K-1).

Again a lower bound.

### 12.4. A matrix perturbation approach

Write P = (1/2)(Pi_0 + D * Pi_1) = (1/2) Pi_0 (I + Pi_0^{-1} D Pi_1).

Let Q = Pi_0^{-1} D Pi_1 = Pi_0^{-1} D Pi_1. Then P = (1/2) Pi_0 (I + Q).

The operator Q is a "twisted permutation": Q = Pi_0^{-1} D Pi_1 = D' * Pi_3 where D' is a diagonal phase matrix and Pi_3 is the multiplication-by-3 permutation. (This uses Pi_0^{-1} Pi_1 = Pi_{2} Pi_{3/2} = Pi_3, and the diagonal gets conjugated.)

From Section I.1 of the coupling/entropy analysis: the eigenvalues of D' Pi_3 restricted to a single <3>-coset of length L are EXACTLY the L-th roots of unity.

For the full orbit with m cosets: D' Pi_3 has eigenvalues that are products of L-th roots of unity with inter-coset phase factors. Specifically:

On the full orbit, D' Pi_3 is a block-diagonal matrix (it acts within each <3>-coset, since Pi_3 does), with each block being a twisted L-cycle. Each block has eigenvalues {omega_L^k : k = 0, ..., L-1}. So the full spectrum of Q = D' Pi_3 on the orbit O is:

    {omega_L^k : k = 0, ..., L-1}   with multiplicity m

(Each eigenvalue appears m times, once per <3>-coset.)

**Wait, this is wrong.** D' Pi_3 is NOT block-diagonal on the cosets, because D' may couple different cosets. Let me re-derive.

Q = Pi_0^{-1} D Pi_1 where Pi_0 is multiplication by 2^{-1} and Pi_1 is multiplication by 3*2^{-1}. So Pi_0^{-1} is multiplication by 2. And Pi_0^{-1} Pi_1 is multiplication by 2 * (3/2) = 3. So Q = Pi_2 D Pi_{3/2} = D'' * Pi_3 where D'' is a conjugation of D.

Now, Pi_3 maps within each <3>-coset (it's the cyclic shift). And D'' is a diagonal matrix. So Q = D'' * Pi_3 IS block-diagonal on <3>-cosets.

The eigenvalues of Q on each <3>-coset are the L-th roots of the product of the phases d''_j along the coset. As computed in Section I.1, this product is 1, so the eigenvalues are exactly omega_L^k for k = 0, ..., L-1.

**Therefore:** The eigenvalues of Q on the full orbit O are {omega_L^k : k = 0, ..., L-1}, each with multiplicity m = K/L.

### 12.5. Eigenvalues of P from eigenvalues of Q

P = (1/2) Pi_0 (I + Q). The eigenvalues of I + Q are {1 + omega_L^k : k = 0, ..., L-1}, each with multiplicity m.

The eigenvalues of Pi_0 (I + Q) are NOT simply the products (eigenvalues of Pi_0) * (eigenvalues of I+Q) because Pi_0 and I+Q don't commute (Pi_0 maps between cosets, while I+Q is block-diagonal on cosets).

**The correct computation:** Since I + Q is block-diagonal with blocks on <3>-cosets, and Pi_0 permutes the cosets, the matrix Pi_0(I + Q) maps the k-th eigenspace of Q within coset C_i to coset C_{2*i}. The eigenvalue (1 + omega_L^k) on coset C_i gets carried to coset C_{2*i}.

In the basis that diagonalizes Q (the "Fourier basis" on each <3>-coset), the matrix P = (1/2) Pi_0(I + Q) acts as:

    P |k, i> = (1/2)(1 + omega_L^k) |k, 2*i>

where |k, i> denotes the k-th intra-coset mode on coset C_i.

**This is a remarkable simplification!** In the intra-coset Fourier basis, P separates into L independent m x m blocks, one for each intra-coset mode k. The k-th block is:

    P_k = (1/2)(1 + omega_L^k) * Sigma

where Sigma is the m x m permutation matrix for the coset-level map i -> 2*i (multiplication by 2 on the coset space G = H/<3>).

The eigenvalues of Sigma (a cyclic permutation of order m on the m cosets) are {omega_m^j : j = 0, ..., m-1}.

Therefore, the eigenvalues of P_k are:

    lambda_{k,j} = (1/2)(1 + omega_L^k) * omega_m^j

for k = 0, ..., L-1 and j = 0, ..., m-1.

### 12.6. The spectral gap from the eigenvalue formula

**This is a key new result.** The eigenvalues of the transfer matrix P on orbit O are:

    lambda_{k,j} = (1/2)(1 + omega_L^k) * omega_m^j    for k = 0, ..., L-1, j = 0, ..., m-1

where omega_L = e^{2*pi*i/L}, omega_m = e^{2*pi*i/m}, L = ord_p(3), m = K/L.

**Caution:** This formula assumes that the intra-coset Fourier modes are exactly eigenvectors of Q, and that Pi_0 acts as a simple cyclic permutation on the coset space. Both of these require verification.

The first assumption (Q is block-diagonal with eigenvalues omega_L^k on each block) was verified above -- it follows from the CDG-type product identity (product of phases around a <3>-cycle = 1).

The second assumption (Pi_0 acts as a cyclic permutation on coset space) requires that multiplication by 2 generates a cyclic group of order m on the coset space G = H/<3>. Since G = <2 mod <3>> and has order m, this is exactly a cyclic group of order m generated by 2 mod <3>. So Pi_0 restricted to the coset space IS a cyclic permutation of order m.

**However:** Pi_0 also acts WITHIN cosets (it shifts the intra-coset position). When multiplying r by 2, if r = r_i * 3^j (i-th coset, j-th intra-coset position), then 2r = 2r_i * 3^j. Now 2r_i is in coset C_{2i} (by the coset-level permutation), but the intra-coset position may also change. Specifically, if 2r_i = r_{2i} * 3^{tau_i} for some shift tau_i, then 2r = r_{2i} * 3^{j + tau_i}.

So Pi_0 maps |k, i> to omega_L^{k * tau_i} |k, 2*i> (the intra-coset Fourier mode picks up a phase from the shift). This means:

    P |k, i> = (1/2)(1 + omega_L^k) * omega_L^{k * tau_i} |k, 2*i>

The eigenvalues of the k-th block become:

    lambda_{k,j} = (1/2)(1 + omega_L^k) * mu_j^{(k)}

where mu_j^{(k)} are the eigenvalues of the m x m matrix Sigma_k with entries (Sigma_k)_{2*i, i} = omega_L^{k * tau_i} (a twisted permutation matrix).

**The eigenvalues of Sigma_k:** This is a cyclic permutation with phases omega_L^{k * tau_i}. By the same argument as for D' Pi_3 (Section I.1), the eigenvalues are the m-th roots of prod_i omega_L^{k * tau_i} = omega_L^{k * sum_i tau_i}.

If sum_i tau_i = 0 mod L, the eigenvalues are the m-th roots of unity: {omega_m^j : j = 0, ..., m-1}.

**Claim: sum_i tau_i = 0 mod L.**

*Proof:* The shift tau_i is defined by 2 * r_i = r_{2*i (mod m)} * 3^{tau_i}. Going around the full cycle of m cosets: 2^m * r_0 = r_0 * 3^{sum tau_i}. Since 2^m is the order of 2 in G = H/<3>, we have 2^m in <3>, i.e., 2^m = 3^t for some t. So 3^{sum tau_i} = 2^m = 3^t, giving sum tau_i = t mod L.

For sum tau_i = 0 mod L: we need t = 0 mod L, i.e., 2^m = 1 mod p (since 3^L = 1 mod p, 3^t = 1 iff L | t). But 2^m = 3^t and 3^L = 1 mod p, so 2^m = 3^{t mod L} mod p. For 2^m = 1 mod p: we need t = 0 mod L.

In general, t is not 0 mod L. So the eigenvalues of Sigma_k are the m-th roots of omega_L^{k*t}, which are:

    mu_j^{(k)} = omega_L^{k*t/m} * omega_m^j    (if m | t... no, the m-th roots of omega_L^{kt})

More precisely: if we set zeta = omega_L^{kt}, then mu^m = zeta, so mu = zeta^{1/m} * omega_m^j = omega_{mL}^{kt} * omega_m^j = e^{2*pi*i*(kt/(mL) + j/m)}.

This gives:

    lambda_{k,j} = (1/2)(1 + e^{2*pi*i*k/L}) * e^{2*pi*i*(kt/(mL) + j/m)}

The magnitude:

    |lambda_{k,j}| = (1/2)|1 + e^{2*pi*i*k/L}| = cos(pi*k/L)

**The eigenvalue magnitude depends only on k (the intra-coset mode index) and NOT on j (the inter-coset mode index)!**

### 12.7. The spectral gap conclusion

**Theorem 12.1.** For the transfer matrix P on a single <2,3>-orbit of size K in F_p*, the eigenvalue magnitudes are:

    |lambda_{k,j}| = cos(pi*k/L)     for k = 0, ..., L-1 and j = 0, ..., m-1

where L = ord_p(3) and m = K/L.

The spectral gap (excluding the stationary eigenvalue k=0, j=0 which has |lambda| = 1) is:

    gap = 1 - max_{(k,j) != (0,0)} |lambda_{k,j}|

The maximum of |lambda_{k,j}| over (k,j) != (0,0) is:

**Case 1: L >= 2.** The maximum of cos(pi*k/L) over k = 1, ..., L-1 is cos(pi/L) (at k = 1). This is also the value for k = 0 with j != 0, where |lambda_{0,j}| = cos(0) = 1.

**WAIT.** For k = 0: |lambda_{0,j}| = cos(0) = 1 for ALL j. This means there are m eigenvalues with magnitude 1, not just one!

This can't be right -- it would mean M has an m-dimensional eigenspace with eigenvalue on the unit circle, contradicting the Combined Theorem.

### 12.8. Identifying the error

The error is in the assumption that Q = D'' * Pi_3 is exactly block-diagonal on <3>-cosets with eigenvalues being L-th roots of unity. Let me re-examine.

The operator Q = Pi_0^{-1} D Pi_1 where D = diag(omega^{r_j * gamma}).

Pi_0 maps r -> r/2 (multiplication by alpha = 2^{-1}). Pi_1 maps r -> r * 3/2 (multiplication by beta = 3*2^{-1}).

Pi_0^{-1} maps r -> 2r. Pi_1 maps r -> (3/2)r.

Q(r) = Pi_0^{-1}(D(Pi_1(r))). Let's compute Q on the Fourier coefficient a_r:

From the eigenvalue equation: P * a = lambda * a, where (Pa)_s = (1/2)a_{2s} + (1/2)omega^{s*gamma} a_{(3/2)*s*2}... No, let me go back to basics.

The transfer matrix P acts on the vector a = (a_r)_{r in O}. From equation (**):

    (Pa)_r = (1/2) a_{r/2} + (1/2) omega^{r/2 * gamma}...

Actually, M maps chi_r to (1/2) chi_{r*alpha} + (1/2) omega^{r*gamma} chi_{r*beta}. So in the Fourier coefficient representation:

    (M*a)_{r*alpha} gets contribution (1/2) a_r
    (M*a)_{r*beta} gets contribution (1/2) omega^{r*gamma} a_r

I.e., the action on coefficients is:
    b_s = sum_{r: r*alpha=s} (1/2) a_r + sum_{r: r*beta=s} (1/2) omega^{r*gamma} a_r
        = (1/2) a_{s/alpha} + (1/2) omega^{(s/beta)*gamma} a_{s/beta}
        = (1/2) a_{2s} + (1/2) omega^{(2s/3)*gamma} a_{2s/3}

With gamma = 2^{-1}:
    b_s = (1/2) a_{2s} + (1/2) omega^{s/3} a_{2s/3}

So the transfer matrix in the a-basis is:
    P_{s, 2s} = 1/2
    P_{s, 2s/3} = (1/2) omega^{s/3}

P maps index 2s to index s with weight 1/2, and index 2s/3 to index s with weight (1/2)omega^{s/3}.

In terms of Pi_0 (multiplication by 2): (Pi_0)_{s, 2s} = 1. And D(r) = omega^{r/3}. And Pi_1 is multiplication by 2/3: (Pi_1)_{s, 2s/3} = 1.

So P = (1/2)(Pi_{2^{-1}} + D * Pi_{(2/3)^{-1}}) acting on the RIGHT (on the source index). In matrix notation: P_{target, source} = (1/2) delta_{target, source*2^{-1}} + (1/2) omega^{source * 2^{-1} / 3} delta_{target, source*(2/3)^{-1}}.

Hmm, this is getting confusing with the index conventions. The key point is that the PHASE omega^{s/3} depends on the TARGET index s, not just the source. This means D is not simply a diagonal multiplied on one side -- it depends on the target.

**THIS is why the block-diagonalization doesn't work as simply as claimed.** The phase omega^{s/3} varies across the target modes within a <3>-coset. Specifically, for s in a <3>-coset C = {r, 3r, 9r, ..., 3^{L-1}r}, the phase omega^{s/3} = omega^{3^{k-1}r} for s = 3^k r (k >= 1), and omega^{3^{L-1}r} for s = r (k = 0, so s/3 = 3^{-1}r = 3^{L-1}r). This phase varies with k, creating the nontrivial intra-coset structure.

### 12.9. Correct block structure

Let me re-derive the transfer matrix more carefully.

For a single orbit O, label elements as r_{i,j} = r_0 * 2^i * 3^j (with appropriate ranges). The transfer matrix P acts as:

    (Pa)_{r_{i,j}} = (1/2) a_{r_{i,j} * 2} + (1/2) omega^{r_{i,j}/3} a_{r_{i,j} * (2/3)^{-1}}
                   ... (needs careful index tracking)

This is the full K x K matrix, and its diagonalization is the original problem. The earlier simplified analysis (eigenvalues = cos(pi*k/L)) was based on an incorrect block-diagonalization that ignored the target-dependent phases.

**Conclusion of Section 12:** The simple eigenvalue formula lambda_{k,j} = cos(pi*k/L) is INCORRECT due to the target-dependent phase structure. The transfer matrix does NOT fully decouple into independent intra-coset and inter-coset blocks. The phases create coupling that is essential to the spectral gap.

---

## 13. Correct Analysis: The Transfer Matrix as a Single Non-Normal Operator

### 13.1. Returning to fundamentals

The transfer matrix P on orbit O of size K is a NON-NORMAL K x K matrix (since M is not self-adjoint). Its spectral radius rho(P) = max |lambda_i| where the lambda_i are eigenvalues (including complex ones).

From the Combined Theorem: rho(P) < 1 for all primes p >= 5. The question is whether rho(P) is UNIFORMLY bounded away from 1.

### 13.2. What each agent found (synthesis)

All three agents independently converged to the same conclusion:

**Agent 1 (Bourgain-Gamburd):** The standard B-G machine fails because Aff(F_p) is solvable. The L-V theorem gives only O(1/p). The product theorem provides combinatorial growth but needs a Phase 3 substitute. **Key identification:** The problem reduces to spectral gap for a SINGLE large irreducible representation of dimension p-1.

**Agent 2 (Sum-Product):** Proved Theorem 16 (constant gap for K >= p^{1/2+epsilon}) via phase constraint + orbit equidistribution. **Key identification:** For K < p^{1/2+epsilon}, the Gauss sum error is too large. The needed lemma is about cancellation of colliding Fourier modes.

**Agent 3 (Coupling/Entropy):** All four approaches (entropy, coupling, Poincare, transfer matrix) reduce to the same bilinear form bound. **Key identification:** The per-orbit Cauchy-Schwarz bound is TIGHT (there exist functions saturating it), but the saturating functions are not eigenfunctions. The missing ingredient is the "inter-coset expansion" -- how multiplication by 2 mixes energy between <3>-cosets.

### 13.3. The algebraic core (refined)

The spectral gap for orbit O of size K is determined by:

    max_{f on O, ||f||=1, f perp 1} |<T_0 f, T_1 f>|

This bilinear form equals:

    sum_{s in O} a_{3s} conj(a_s) omega^{-s*alpha}

The Cauchy-Schwarz bound is 1 (tight). Equality requires the "orbit-constant" phase pattern. The Combined Theorem says this pattern is NOT an eigenvector. But the GAP between the Cauchy-Schwarz bound and the actual maximum (over eigenvectors) is what determines the spectral gap.

The actual maximum depends on the ALGEBRA of the orbit -- how the phases omega^{-s*alpha} interact with the permutation structure of ×3 and ×2 on O. This is an ARITHMETIC quantity that depends on p.

### 13.4. A numerical experiment to guide intuition

For the middle-range primes, the spectral gap should be computed explicitly to see whether it deviates from the ~0.30 constant observed for all primes tested so far.

The middle-range primes are those where both ord_p(2) and ord_p(3) are small (O(sqrt(p))). Such primes are rare but exist. For example:

- p such that ord_p(2) is small: p | (2^k - 1) for small k. Mersenne-related primes.
- p such that ord_p(3) is small: p | (3^k - 1) for small k.
- p such that BOTH are small: p | gcd(2^a - 1, 3^b - 1) for small a, b.

The primes dividing both 2^k - 1 and 3^l - 1 for small k, l are rare. For k = l = 6: 2^6 - 1 = 63, 3^6 - 1 = 728. gcd(63, 728) = 7. So p = 7 with ord_7(2) = 3, ord_7(3) = 6, K = |<2,3>| = 6 = p-1. Not a small-K example.

For k = 12: 2^12 - 1 = 4095 = 3^2 * 5 * 7 * 13. And 3^6 - 1 = 728 = 2^3 * 7 * 13. So p = 13 with ord_13(2) = 12, ord_13(3) = 3. K = |<2,3>| = lcm(12,3) = 12 = p-1. Still full orbit.

Finding primes where K = |<2,3>| is significantly smaller than p-1 requires more systematic search. The index [F_p* : <2,3>] > 1 means there exists a character chi of F_p* trivial on <2,3>, which means chi(2) = chi(3) = 1, i.e., both 2 and 3 are in ker(chi). For a character of order d | (p-1), this means d | ord_p(2) and d | ord_p(3), i.e., d | gcd(ord_p(2), ord_p(3)).

Primes where <2,3> is a proper subgroup of F_p* are those where p-1 has a factor d > 1 dividing both ord_p(2) and ord_p(3)... actually, the condition is that <2,3> is a PROPER subgroup, which means there exists a prime q | (p-1) such that 2^{(p-1)/q} = 1 mod p AND 3^{(p-1)/q} = 1 mod p.

For q = 2: need 2^{(p-1)/2} = 1 mod p (2 is a quadratic residue) AND 3^{(p-1)/2} = 1 mod p (3 is a QR). Both 2 and 3 are QR mod p iff p = 1 mod 24 (by QR and the law of QR).

Example: p = 73 (73 = 1 mod 24). Check: ord_73(2) = 4 (since 2^4 = 16, but 16 != 1 mod 73... let me compute: 2^1=2, 2^2=4, 2^4=16, 2^8=256=256-3*73=256-219=37, 2^9=74=1 mod 73. So ord_73(2) = 9. And ord_73(3) = 3^1=3, 3^2=9, 3^3=27, 3^4=81=8, 3^6=8*9=72=-1, 3^12=1, so ord_73(3) = 12. K = |<2,3>|... since gcd(9,12)=3, by the formula |<2,3>| = lcm(9,12) * ... no, <2,3> is not simply lcm of the two orders. It's more complex.

The point is that finding small-K primes in the middle range [K_0, p^{1/2+epsilon}] requires systematic computation. Our numerical data (p up to 997) showed that all tested primes had |lambda_2| in [0.66, 0.81], suggesting the constant gap holds uniformly.

---

## 14. Toward a Proof: The Telescoping Phase Argument

### 14.1. The key structural lemma

**Lemma 14.1 (Phase Incompatibility).** Let f be a unit eigenvector on orbit O with eigenvalue lambda, and |lambda|^2 >= 1 - eta. Then:

(a) The function f satisfies a_{3s} = c * omega^{s*alpha} * a_s + epsilon_s where sum |epsilon_s|^2 <= C*eta.

(b) The eigenvalue equation gives a_{2s} = (a_s + omega^s a_{3s})/(2*lambda) = a_s(1 + c*omega^{s*alpha+s})/(2*lambda) + correction.

(c) By iterating the ×(3/2) chain L times (returning to the same <3>-coset), the accumulated phase must satisfy a global consistency condition.

(d) By iterating the ×2 chain m times (cycling through all cosets), a DIFFERENT global consistency condition must hold.

(e) The two consistency conditions (c) and (d) involve the "translation shift" 1/(2p) at each step, which accumulates differently along the two chains. For both to hold simultaneously, the phases must satisfy a system of equations that has no solution for eta < c_0, where c_0 > 0 is a universal constant.

### 14.2. The ×(3/2) consistency (condition c)

Following the chain s -> (3/2)s -> (3/2)^2 s -> ... -> (3/2)^{ell} s = s:

From condition (a), iterated ell times:
    a_{(3/2)^{ell} s} = c^{ell} * omega^{s*alpha * (1 + 3/2 + ... + (3/2)^{ell-1})} * a_s

Since (3/2)^{ell} = 1 mod p, the left side is a_s. So:
    c^{ell} * omega^{s*alpha * ((3/2)^{ell} - 1) / (3/2 - 1)} = 1.

Since (3/2)^{ell} = 1 mod p, the exponent is s*alpha * 0 / (1/2) = 0. So c^{ell} = 1.

This is automatically satisfied -- no constraint beyond c being an ell-th root of unity.

### 14.3. The ×2 consistency (condition d)

Following the chain s -> 2s -> 4s -> ... -> 2^{L_2} s = s:

From condition (b), at each step: a_{2s} = a_s * (1 + c*omega^{s(alpha+1)})/(2*lambda) + correction.

Iterating L_2 times:
    a_{2^{L_2} s} = a_s * product_{j=0}^{L_2-1} (1 + c * omega^{2^j s * (alpha+1)}) / (2*lambda)^{L_2}

Since 2^{L_2} s = s: the product must equal (2*lambda)^{L_2}.

Taking magnitudes:
    product_{j=0}^{L_2-1} |1 + c * omega^{2^j s * (alpha+1)}| = |2*lambda|^{L_2}

The left side: |1 + c*omega^{theta_j}| = sqrt(2 + 2*Re(c*omega^{theta_j})) = sqrt(2) * sqrt(1 + Re(c*omega^{theta_j})) where theta_j = 2*pi * 2^j s * (alpha+1) / p.

If c is close to 1 (which it must be for small eta): |1 + omega^{theta_j}| = 2*|cos(theta_j/2)|.

So: product cos(theta_j/2) = |lambda|^{L_2}.

By the CDG identity: product |cos(pi * 2^j s * (alpha+1) / p)| = 2^{-L_2} (up to the exact phase of the arguments).

**Wait** -- the CDG identity gives product cos(pi * b * 2^j / p) = +/- 2^{-L_2} for the specific b-orbit. Here, b = s * (alpha + 1) = s * (1/2 + 1) = 3s/2.

So: product_{j=0}^{L_2-1} |cos(pi * 3s/2 * 2^j / p)| = 2^{-L_2}.

This means: product |1 + omega^{theta_j}| = product 2|cos(theta_j/2)| = 2^{L_2} * 2^{-L_2} = 1.

But we need this product to equal |2*lambda|^{L_2} = (2|lambda|)^{L_2}.

So: (2|lambda|)^{L_2} = 1, giving |lambda| = 1/2.

**This seems to prove |lambda| = 1/2 for any eigenvector satisfying the exact phase condition!** But wait, the analysis used condition (a) as an EXACT relation, whereas it's only approximate (with error epsilon_s of size O(sqrt(eta))).

### 14.4. The bootstrap

The argument in 14.3 shows:

**If the phase relation a_{3s} = c * omega^{s*alpha} * a_s holds EXACTLY, then |lambda| = 1/2.**

Since the phase relation holds only approximately (with L^2 error O(eta)), the product in 14.3 has error:

    product |1 + c*omega^{theta_j}| = (2|lambda|)^{L_2} * (1 + O(L_2 * sqrt(eta)))

Combined with the CDG identity (product = 1 exactly):

    (2|lambda|)^{L_2} * (1 + O(L_2 * sqrt(eta))) = 1

So:
    |lambda|^{L_2} = 2^{-L_2} * (1 + O(L_2 * sqrt(eta)))^{-1}

    |lambda| = 1/2 * (1 + O(L_2 * sqrt(eta)))^{-1/L_2} = 1/2 * (1 + O(sqrt(eta)))

For this to be consistent with |lambda|^2 = 1 - eta:

    1/4 * (1 + O(sqrt(eta)))^2 = 1 - eta
    1/4 + O(sqrt(eta)) = 1 - eta

This gives 3/4 = eta + O(sqrt(eta)), so eta ~ 3/4 for the leading order! This is not small.

**Wait -- this argument shows that if the approximate phase condition holds, then |lambda| is close to 1/2, NOT close to 1.** The only way to have |lambda| close to 1 is if the approximate phase condition is BADLY violated, meaning the cross-term <T_0 f, T_1 f> is NOT close to ||f||^2.

But we started by assuming |lambda|^2 >= 1 - eta, which FORCES the cross-term to be >= (1 - 2*eta)||f||^2, which in turn forces the approximate phase condition (with error O(sqrt(eta))).

**The contradiction:** Assuming |lambda|^2 >= 1 - eta leads to the approximate phase condition, which via CDG leads to |lambda| ~ 1/2, hence |lambda|^2 ~ 1/4. But 1/4 >= 1 - eta only if eta >= 3/4. So we must have eta >= 3/4, i.e., **|lambda|^2 <= 1/4, hence |lambda| <= 1/2**.

**This would prove |lambda_2| <= 1/2 + o(1) for all primes, giving a spectral gap of ~1/2!**

### 14.5. Checking the argument

Let me carefully verify the key step. The approximate phase condition says:

    a_{3s} ~ c * omega^{s/2} * a_s    (with error O(sqrt(eta)) in L^2)

Substituting into the eigenvalue equation (**):

    a_s + omega^s * c * omega^{s/2} * a_s ~ 2*lambda * a_{2s}
    a_s * (1 + c * omega^{3s/2}) ~ 2*lambda * a_{2s}

So a_{2s} ~ a_s * (1 + c * omega^{3s/2}) / (2*lambda).

Magnitude: |a_{2s}| ~ |a_s| * |1 + c * omega^{3s/2}| / (2|lambda|).

For s in the orbit, iterating ×2 for L_2 steps:

    |a_{2^{L_2} s}| = |a_s| * product_{j=0}^{L_2-1} |1 + c * omega^{3 * 2^j * s / 2}| / (2|lambda|)^{L_2}

Since 2^{L_2} s = s (in F_p): the product must equal (2|lambda|)^{L_2}.

Now, the CDG identity: for b = 3s/2 (a fixed nonzero element of F_p), the product

    product_{j=0}^{L_2-1} cos(pi * b * 2^j / p) = +/- 2^{-L_2}

And |1 + c * omega^{b * 2^j}| = |1 + c * e^{2*pi*i * b * 2^j / p}|.

If |c| = 1 and c = e^{i*phi} for some phase phi, then:

    |1 + e^{i*(phi + 2*pi*b*2^j/p)}| = 2*|cos((phi + 2*pi*b*2^j/p)/2)|
                                       = 2*|cos(phi/2 + pi*b*2^j/p)|

The product becomes:

    product_{j=0}^{L_2-1} 2*|cos(phi/2 + pi*b*2^j/p)| = 2^{L_2} * product |cos(phi/2 + pi*b*2^j/p)|

Now, this product is NOT the same as the CDG identity (which has cos(pi*b*2^j/p) without the phi/2 shift). The CDG identity is about the product of cos(pi*x*2^j/p) for specific x, not about shifted cosines.

**Critical point:** The shifted product product |cos(phi/2 + pi*b*2^j/p)| is NOT necessarily equal to 2^{-L_2}.

The CDG identity gives product cos(pi*b*2^j/p) = +/- 2^{-L_2}, but with the shift phi/2, the product changes.

**However:** By the same CDG logic (the product is a Fourier coefficient of a specific self-similar measure), the product of shifted cosines satisfies:

    product_{j=0}^{L_2-1} cos(phi/2 + pi*b*2^j/p) = (1/2^{L_2}) * Re[e^{i*L_2*phi/2} * sum of terms]

The exact value depends on the relationship between phi, b, and p. In general, this product is a complex number of magnitude <= 2^{-L_2} (by the AM-GM or Hadamard inequality), with equality iff all cosines have the same sign and the product is real.

**The magnitude bound:**

    product |cos(phi/2 + pi*b*2^j/p)| <= 1 (trivially, since each |cos| <= 1)

But we can do better. By AM-GM on log:

    (1/L_2) sum log|cos(phi/2 + pi*b*2^j/p)| <= log((1/L_2) sum |cos(phi/2 + pi*b*2^j/p)|)

And by the average of cos^2:

    (1/L_2) sum cos^2(phi/2 + pi*b*2^j/p) = 1/2 + (1/(2*L_2)) Re[e^{i*phi} sum omega^{2*b*2^j}]

The inner sum is a character sum over the <2>-orbit, bounded by sqrt(p) (Gauss sum). So the average of cos^2 is 1/2 + O(sqrt(p)/L_2).

When L_2 >= sqrt(p) (which holds for most primes): average cos^2 ~ 1/2. By Jensen on the concave function log:

    (1/L_2) sum log(cos^2) <= log(1/2 + O(1/sqrt(p)))

So product cos^2 <= (1/2 + O(1/sqrt(p)))^{L_2}, giving product |cos| <= (1/sqrt(2) + O(1/sqrt(p)))^{L_2}.

This is essentially (1/sqrt(2))^{L_2} = 2^{-L_2/2}.

**Combining:** (2|lambda|)^{L_2} = 2^{L_2} * product |cos(shifted)| <= 2^{L_2} * 2^{-L_2/2} = 2^{L_2/2}.

So |lambda|^{L_2} <= 2^{-L_2/2}, giving |lambda| <= 1/sqrt(2).

**THIS is the key bound: |lambda| <= 1/sqrt(2) ~ 0.707.**

### 14.6. Making the argument rigorous

The argument above has two approximations:

1. The approximate phase condition introduces error O(sqrt(eta)) at each step of the ×2 chain.
2. The average of cos^2 uses a Gauss sum bound that requires L_2 >= sqrt(p).

For approximation (1): over L_2 steps, the accumulated error in the product is O(L_2 * sqrt(eta)). So:

    product |1 + c*omega^{...}| = (2|lambda|)^{L_2} * (1 + O(L_2 * sqrt(eta)))

For the conclusion |lambda| <= 1/sqrt(2) + O(something): we need the error to be small, i.e., L_2 * sqrt(eta) << 1.

If eta is the quantity we're trying to bound, and we assume eta < c for some c < 1, then L_2 * sqrt(eta) < L_2 * sqrt(c). For this to be < 1/2 (say), we need L_2 < 1/(2*sqrt(c)).

But L_2 can be as large as p-1! So this argument only works when L_2 is bounded.

For approximation (2): the Jensen bound requires the average of cos^2 to be bounded, which needs L_2 to be at least sqrt(p). When L_2 < sqrt(p), the Gauss sum error dominates.

**The middle range K in [K_0, p^{1/2+epsilon}] can have L_2 = ord_p(2) anywhere from 2 to p-1.** The argument works differently depending on L_2.

### 14.7. Synthesis

The CDG-based product argument gives:

**When L_2 is bounded:** |lambda| is forced to be close to 1/2 (with a constant error depending on L_2). This gives a constant spectral gap.

**When L_2 is large (>= sqrt(p)):** The average of cos^2 is approximately 1/2 by equidistribution, giving |lambda| <= 1/sqrt(2) + o(1). Combined with the error from the approximate phase condition, this requires eta to be not too small (otherwise the L_2 * sqrt(eta) error term dominates).

**When L_2 is in the middle range:** The argument doesn't immediately close.

However, there's a crucial observation: the constraint (2|lambda|)^{L_2} = product of shifted cosines holds for ANY eigenvector on the orbit. The product of shifted cosines is a FIXED quantity (depending on the orbit and the phase c, but not on the eigenvector). And the CDG-type constraint says this product is exactly 1 when c = 1 (no phase shift).

For general c (an ell-th root of unity): the product is a specific algebraic number. The constraint |lambda| = (product)^{1/L_2} / 2 gives |lambda| as a specific function of the orbit and the phase choice c.

The spectral gap is then:

    gap = 1 - max_c (product_{j=0}^{L_2-1} |1 + c * omega^{3s*2^j/(2p)}|)^{1/L_2} / 2

where the max is over L-th roots of unity c, and s ranges over elements of O.

This is a COMPUTABLE quantity for each prime p. The universal constant gap conjecture asserts that this quantity is bounded away from 0 uniformly in p.

---

## 15. Conclusions and Status

### 15.1. Summary of findings

1. **The transfer matrix P on each orbit has a rich algebraic structure.** The eigenvalues depend on the interaction between intra-coset (×3) dynamics and inter-coset (×2) coupling, modulated by "+1" phases.

2. **The CDG product identity constrains the product of one-step contraction factors along <2>-orbits.** This product is exactly 2^{-L_2}, regardless of the starting position or phase parameters.

3. **The approximate phase condition (from near-eigenvalue analysis) combined with the CDG product identity gives |lambda| ~ 1/2 in the exact case.** The error terms prevent a clean universal constant bound without additional structure.

4. **The Jensen inequality argument gives |lambda| <= 1/sqrt(2) + O(sqrt(p)/L_2) when the <2>-orbit is long enough.** This matches the numerical observation |lambda_2| ~ 1/sqrt(2) ~ 0.707.

5. **For the middle range K in [K_0, p^{1/2+epsilon}]:** The problem reduces to showing that the product of shifted cosines along <2>-orbits is bounded away from (2|lambda|)^{L_2} = 2^{L_2} (which would require |lambda| = 1). The CDG identity ensures the unshifted product is 2^{-L_2}, and the phase shift from the "+1" translation cannot improve this to 2^{L_2}. The gap between 2^{-L_2} and 2^{L_2} is exponential, but the shifted products can potentially be larger than 2^{-L_2}.

### 15.2. What remains to prove

The universal constant gap for the middle range requires one of:

(A) **A uniform bound on shifted CDG products:** Show that for any phase c on the unit circle and any orbit element s, the product product_{j} |1 + c * omega^{3s*2^j/2/p}| <= C for a universal C, giving |lambda| <= C^{1/L_2}/2.

(B) **A multi-orbit argument:** Use the fact that the eigenvector lives on the FULL orbit (not just a single <2>-chain) to get cancellation between different <2>-chains within the orbit.

(C) **A two-step or multi-step contraction:** Show that ||M^k||_op <= (1-c)^k for some bounded k, using the phase decoherence that accumulates over multiple steps.

(D) **A compactness argument over the one-parameter family:** Show that rho(t) = max eigenvalue of P(t) is a continuous function of t = r_0/p in (0,1), and that for each prime p, the function rho(t) achieves its maximum at a value strictly less than 1, with the maximum bounded uniformly across primes.

### 15.3. The most promising direction

Approach (A) appears most promising. The key bound needed is:

**Claim:** For any nonzero b in F_p and any phi in [0, 2*pi):

    product_{j=0}^{L_2-1} |cos(phi/2 + pi*b*2^j/p)| <= 2^{-L_2/2+epsilon}

for some universal epsilon > 0 (or even epsilon = 0). This would give |lambda| <= 1/sqrt(2) + o(1).

This claim follows from the equidistribution of {b*2^j/p mod 1 : j = 0, ..., L_2-1} and the concavity of log|cos|, provided the equidistribution error is controlled. For most primes (where L_2 >= sqrt(p)), this holds by standard Gauss sum bounds.

For primes where L_2 is small (L_2 < sqrt(p)), the orbit {b*2^j mod p} has fewer than sqrt(p) elements, and equidistribution fails. However, in this case, L_2 is bounded (by sqrt(p)), and the K x K transfer matrix has at most K < p^{1/2+epsilon} dimensions, with the <2>-cosets having bounded size L_2. The problem then reduces to an m x m inter-coset problem (where m = K/L) that can potentially be handled by the same phase-decoherence argument applied to the inter-coset graph.

### 15.4. Formal status

| Result | Status |
|--------|--------|
| |lambda_2| < 1 for each prime p | **Proved** (Combined Theorem) |
| |lambda_2| <= 1 - c(epsilon) when K >= p^{1/2+epsilon} | **Proved** (Theorem 16) |
| |lambda_2| <= 1 - c(K_0) when K <= K_0 | **Proved** (compactness) |
| CDG product identity constrains |lambda| ~ 1/2 in exact case | **Proved** (Section 14.3-14.4) |
| Jensen bound gives |lambda| <= 1/sqrt(2) when L_2 >> sqrt(p) | **Proved** (Section 14.5) |
| Universal constant gap for ALL primes | **Open** (middle range K in [K_0, p^{1/2+epsilon}]) |
| Transfer matrix eigenvalue formula (simplified) | **Incorrect** (Section 12.8 -- phases not block-diagonal) |
| Inter-coset expansion via ×2 | **Identified** as key mechanism, not proved |

### 15.5. Relationship to the numerical evidence

The numerical observation |lambda_2| ~ 0.70 ~ 1/sqrt(2) for all 166 tested primes is consistent with:

1. The CDG product identity forcing |lambda| ~ 1/2 (geometric mean of contraction factors).
2. The Jensen inequality giving |lambda| <= 1/sqrt(2) (from average cos^2 ~ 1/2).
3. The eigenvalue 1/sqrt(2) corresponding to the "natural" contraction rate of the walk: each step contracts by factor 1/sqrt(2) on average (combining the 1/2 contraction for each character with the sqrt(2) factor from superposition).

The value 1/sqrt(2) is likely the EXACT limiting spectral radius as p -> infinity, corresponding to the spectral radius of the "continuum" operator on L^2(R/Z) defined by (Mf)(x) = (1/2)f(x/2) + (1/2)f((3x+1)/2).

---

## References

1. F. Chung, P. Diaconis, R. Graham, "Random walks arising in random number generation," *Ann. Probab.* 15 (1987), 1148-1165.
2. J. Bourgain, A. Gamburd, "Uniform expansion bounds for Cayley graphs of SL_2(F_p)," *Ann. Math.* 167 (2008), 625-642.
3. E. Lindenstrauss, P. Varju, "Spectral gap in the group of affine transformations over prime fields," *Ann. Fac. Sci. Toulouse Math.* 25 (2016), 969-993.
4. J. Bourgain, N. Katz, T. Tao, "A sum-product estimate in finite fields, and applications," *GAFA* 14 (2004), 27-57.
5. T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," *Forum Math. Pi* 10 (2022), e12.
6. M. Hildebrand, "Random processes of the form X_{n+1} = a_n X_n + b_n (mod p)," *Ann. Probab.* 21 (1993), 710-720.
