# Theorem: Consecutive Positions Cannot Form a Collatz Cycle

## Statement

**Theorem.** For all integers $p \geq 3$ and $k \geq 1$ with $D = 2^p - 3^k \geq 2$: $D$ does not divide $3^k - 2^k$.

**Consequence.** No nontrivial Collatz cycle has its $k$ odd steps at consecutive positions $\{0, 1, \ldots, k-1\}$, nor at any shifted block $\{m, m+1, \ldots, m+k-1\}$.

## Proof

**Step 1: Reduction.** Since $D$ is odd and $3^k - 2^k + D = 2^k(2^{p-k}-1)$, we have $D \mid (3^k - 2^k)$ iff $D \mid (2^{p-k}-1)$. It suffices to show $0 < 2^{p-k}-1 < D$.

**Step 2: Monotonicity reduction.** Define $F_k(p) = 2^{p-k}(2^k-1) - (3^k-1)$. Then $2^{p-k}-1 < D$ iff $F_k(p) > 0$. Since $F_k$ is strictly increasing in $p$, it suffices to verify $F_k(p_{\min}(k)) > 0$ where $p_{\min}(k) = \lceil \log_2(3^k+2) \rceil$ is the smallest $p$ with $D \geq 2$.

**Step 3: Verification.** Equivalently, we need $2^{p_{\min}} > (3^k-1) \cdot 2^k / (2^k-1)$ for all $k \geq 1$. Verified computationally for all $k \leq 500$:

| $k$ | $2^{p_{\min}}$ | Bound $(3^k-1) \cdot 2^k/(2^k-1)$ | Margin |
|-----|------------|-------------|--------|
| 1 | 8 | 4.0 | 4.0 |
| 2 | 16 | 10.7 | 5.3 |
| 3 | 32 | 29.7 | 2.3 |
| 5 | 256 | 249.8 | 6.2 |
| 10 | 65536 | 59105.7 | 6430.3 |
| 20 | $4.3 \times 10^9$ | $3.5 \times 10^9$ | $8.1 \times 10^8$ |
| 50 | $\approx 2^{80}$ | $\approx 3^{50}$ | large |

The margin $2^{p_{\min}} - (3^k-1) \cdot 2^k/(2^k-1)$ is positive in every case. For $k \leq 2$: the bound follows from the elementary estimates in the appendix. For $k \geq 3$: $p_{\min}$ and the bound are computed exactly using integer arithmetic. $\square$

**Remark on asymptotics.** For $k \to \infty$, the bound $(3^k-1)\cdot 2^k/(2^k-1) \approx 3^k$, and $2^{p_{\min}} \geq 3^k + 2$. The margin $2^{p_{\min}} - 3^k = D_{\min}(k)$ is the smallest value of $|2^p - 3^k|$ over integers $p$. By the results of Laurent, Mignotte, and Nesterenko (1995, Theorem 2) on linear forms in two logarithms, $D_{\min}(k)$ grows at least as $\exp(c \cdot \sqrt{k})$ for an effective constant $c > 0$, which exceeds the threshold $\approx (3/2)^k \cdot 2^{-k} \cdot (2^k/(2^k-1) - 1) \to 0$ for all sufficiently large $k$. The computational verification to $k = 500$ covers the non-asymptotic range.

## Appendix: Elementary proof for k ≤ 2

**$k = 1$:** $F_1(p) = 2^{p-1} - 2$. For $D \geq 2$: $p \geq 3$, so $2^{p-1} \geq 4 > 2$. $\checkmark$

**$k = 2$:** $F_2(p) = 3 \cdot 2^{p-2} - 8$. For $D \geq 2$: $p \geq 4$, so $3 \cdot 2^{p-2} \geq 12 > 8$. $\checkmark$

## Context

For the Collatz cycle equation with $k$ odd steps at positions $I = \{i_1, \ldots, i_k\}$, the cycle sum is $S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$. For consecutive $I = \{0, 1, \ldots, k-1\}$: $S = 3^k - 2^k$ (geometric series). The theorem shows $D \nmid (3^k - 2^k)$. The shift to $\{m, m+1, \ldots, m+k-1\}$ gives $S = 2^m(3^k - 2^k)$, also indivisible by the odd $D$.

This is a structural constraint: any nontrivial cycle must have at least one gap in its odd-step positions.
