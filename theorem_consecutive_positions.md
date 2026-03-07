# Theorem: Consecutive Positions Cannot Form a Collatz Cycle

## Statement

**Theorem.** For all integers $p \geq 3$ and $1 \leq k \leq 20000$ with $D = 2^p - 3^k \geq 2$: $D$ does not divide $3^k - 2^k$.

**Conjecture.** The same holds for all $k \geq 1$. A proof sketch for the asymptotic case $k > 20000$ via linear forms in logarithms is given in Step 5, but the explicit constant specialization is not completed here.

**Consequence.** In the standard formulation of the Collatz cycle equation, the cycle sum for positions $I = \{i_1, \ldots, i_k\}$ is $S(I) = \sum_{j=1}^{k} 3^{k-j} \cdot 2^{i_j}$, and a cycle requires $D \mid S(I)$ where $D = 2^p - 3^k$ (see e.g. Steiner 1977, Eliahou 1993). For consecutive positions $I = \{0,1,\ldots,k-1\}$: $S = 3^k - 2^k$ (geometric series). The theorem shows $D \nmid (3^k - 2^k)$, so no cycle uses consecutive positions. More generally, any shifted block $\{m, m+1, \ldots, m+k-1\}$ gives $S = 2^m(3^k-2^k)$, also indivisible by the odd $D$.

## Proof

**Step 1: Reduction.** Since $D \geq 2$ and $2^k < 3^k \leq 2^p - 2$, we have $p > k$, so $2^{p-k} - 1$ is a positive integer. Since $D = 2^p - 3^k$ is odd (as $2^p$ is even and $3^k$ is odd), $\gcd(D, 2^k) = 1$. From the identity

$$3^k - 2^k + D = 2^p - 2^k = 2^k(2^{p-k} - 1),$$

it follows that $D \mid (3^k - 2^k)$ if and only if $D \mid 2^k(2^{p-k} - 1)$, which (by coprimality) holds if and only if $D \mid (2^{p-k} - 1)$.

Since $2^{p-k} - 1 > 0$, it suffices to show $2^{p-k} - 1 < D$.

**Step 2: Reformulation.** The inequality $2^{p-k}-1 < D = 2^p - 3^k$ is equivalent to

$$F_k(p) := 2^{p-k}(2^k - 1) - (3^k - 1) > 0. \qquad (*)$$

Since $F_k$ is strictly increasing in $p$ (as $2^{p-k}$ doubles when $p$ increases by 1), it suffices to verify $(*)$ at $p = p_{\min}(k)$, the smallest integer $p$ with $D = 2^p - 3^k \geq 2$.

**Step 3: Elementary cases.** $k = 1$: $p_{\min} = 3$, $F_1(3) = 2^2 \cdot 1 - 2 = 2 > 0$. $k = 2$: $p_{\min} = 4$, $F_2(4) = 2^2 \cdot 3 - 8 = 4 > 0$.

**Step 4: Computational verification for $3 \leq k \leq 20000$.** For each $k$ in this range, compute $p_{\min}(k)$, the least integer $p$ with $2^p \geq 3^k + 2$, and verify $F_k(p_{\min}) > 0$ using exact integer arithmetic. No counterexample found. Selected values:

| $k$ | $p_{\min}$ | $F_k(p_{\min})$ | $D_{\min}$ |
|-----|-----------|-----------------|------------|
| 3 | 5 | 2 | 5 |
| 5 | 8 | 6 | 13 |
| 10 | 16 | 6424 | 6487 |
| 50 | 80 | $\approx 4.9 \times 10^{23}$ | $\approx 4.9 \times 10^{23}$ |
| 100 | 159 | $\approx 2.2 \times 10^{47}$ | $\approx 2.2 \times 10^{47}$ |
| 500 | 793 | $\approx 1.6 \times 10^{238}$ | $\approx 1.6 \times 10^{238}$ |
| 2000 | 3170 | $\approx 9.3 \times 10^{953}$ | $\approx 9.3 \times 10^{953}$ |

**Step 5: Asymptotic argument for $k > 20000$.** Define $\Lambda_k = p_{\min}(k) \log 2 - k \log 3 > 0$. Then $D_{\min} = 3^k(e^{\Lambda_k} - 1)$. The inequality $(*)$ requires $D_{\min} > (3^k - 2^k)/(2^k - 1)$, i.e.,

$$3^k(e^{\Lambda_k} - 1) > \frac{3^k - 2^k}{2^k - 1}.$$

Dividing by $3^k$ and noting $(3^k - 2^k)/(3^k(2^k-1)) = (1-(2/3)^k)/(2^k-1) < 1/2^{k-1}$:

$$e^{\Lambda_k} - 1 > \frac{1}{2^{k-1}}.$$

For small $\Lambda_k$: $e^{\Lambda_k} - 1 \geq \Lambda_k$, so it suffices to show $\Lambda_k > 2^{1-k}$.

By Theorem 2 of Laurent, Mignotte, and Nesterenko (*J. Number Theory* 55, 1995, pp. 285--321), applied to the linear form $\Lambda = b_1 \log \alpha_1 - b_2 \log \alpha_2$ with $\alpha_1 = 2$, $\alpha_2 = 3$, $b_1 = p_{\min} < 2k$, $b_2 = k$, one obtains a lower bound of the form

$$\log \Lambda_k > -C_0$$

where $C_0$ depends polynomially on $\log k$ (specifically, $C_0 = O((\log k)^2)$ after specializing the LMN parameters $D$, $h(\alpha_i)$, and $b'$ to $\alpha_1 = 2$, $\alpha_2 = 3$). The required inequality $\Lambda_k > 2^{1-k}$ then follows whenever $C_0 < (k-1)\log 2$, which holds for $k$ exceeding an explicit computable threshold $K_0$.

**Remark.** The precise value of $K_0$ depends on the explicit constants obtained by specializing the LMN theorem to $(\alpha_1, \alpha_2) = (2, 3)$. This specialization (deriving the explicit constant $C$ and verifying $K_0 \leq 20000$) is not carried out here. The computational verification to $k = 20000$ is expected to provide sufficient margin, but until the LMN specialization is completed, Step 5 should be regarded as a proof sketch rather than a finished argument.

**Status.** The theorem is proved for all $k \leq 20000$ (Steps 1--4). The asymptotic completion (Step 5) requires an explicit specialization of the LMN linear forms bound to $(\alpha_1, \alpha_2) = (2, 3)$, which is deferred.
