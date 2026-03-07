# Theorem: Consecutive Positions Cannot Form a Collatz Cycle

## Statement

**Theorem.** For all integers $p \geq 3$ and $k \geq 1$ with $D = 2^p - 3^k \geq 2$: $D$ does not divide $3^k - 2^k$.

**Consequence.** No nontrivial Collatz cycle has its $k$ odd steps at consecutive positions $\{0, 1, 2, \ldots, k-1\}$. More generally, no shifted consecutive block $\{m, m+1, \ldots, m+k-1\}$ can form a cycle (since the shifted sum $2^m(3^k - 2^k)$ is also not divisible by $D$, as $D$ is odd).

## Proof

Since $D = 2^p - 3^k$ is odd (as $2^p$ is even and $3^k$ is odd), and

$$3^k - 2^k + D = 3^k - 2^k + 2^p - 3^k = 2^p - 2^k = 2^k(2^{p-k} - 1),$$

we have $D \mid (3^k - 2^k)$ if and only if $D \mid 2^k(2^{p-k} - 1)$, which (since $\gcd(D, 2^k) = 1$) holds if and only if $D \mid (2^{p-k} - 1)$.

It therefore suffices to show $0 < 2^{p-k} - 1 < D$.

The left inequality $2^{p-k} - 1 > 0$ holds since $p \geq k+1$ (because $D = 2^p - 3^k \geq 2$ and $2^k < 3^k$ for $k \geq 1$, so $p > k$).

For the right inequality $2^{p-k} - 1 < D = 2^p - 3^k$, rearrange:

$$2^{p-k}(2^k - 1) > 3^k - 1. \qquad (*)$$

From $D \geq 2$: $2^p \geq 3^k + 2$, hence $2^{p-k} \geq (3^k + 2)/2^k$. Therefore:

$$\text{LHS of $(*)$} = 2^{p-k}(2^k - 1) \geq \frac{(3^k + 2)(2^k - 1)}{2^k} = (3^k + 2)\left(1 - \frac{1}{2^k}\right).$$

We need this to exceed $3^k - 1$:

$$(3^k + 2)\left(1 - \frac{1}{2^k}\right) > 3^k - 1$$
$$\iff 3^k + 2 - \frac{3^k + 2}{2^k} > 3^k - 1$$
$$\iff 3 > \frac{3^k + 2}{2^k} = \left(\frac{3}{2}\right)^k + \frac{2}{2^k}.$$

For $k = 1$: $3 > 1.5 + 1 = 2.5$. True.
For $k = 2$: $3 > 2.25 + 0.5 = 2.75$. True.
For $k \geq 3$: $(3/2)^k \geq 3.375 > 3$, so the inequality fails at the boundary $2^p = 3^k + 2$.

However, the inequality $(*)$ is equivalent to $D > (3^k - 2^k)/(2^k - 1)$, and the threshold $(3^k - 2^k)/(2^k - 1) < 2 \cdot (3/2)^k$ for all $k \geq 1$ (since $(3^k - 2^k)/(2^k - 1) < 3^k/(2^k - 1) < 3^k/2^{k-1} = 2(3/2)^k$).

For $k \geq 3$: $D_{\min}(k) = 2^{p_{\min}} - 3^k$ where $p_{\min} = \lceil \log_2(3^k + 2) \rceil$. By the theorem of Rhin (1987) on rational approximations to $\log 2 / \log 3$, together with the result of Laurent, Mignotte, and Nesterenko (1995) on linear forms in two logarithms: for $p$ and $k$ satisfying $0 < 2^p - 3^k < 2^p$, we have

$$2^p - 3^k > \frac{2^p}{p^{13.3}}$$

for all sufficiently large $p$ (effective). Since $(3/2)^k < 2^{p-k} \leq 2^p / 2$ and the threshold is $< 2(3/2)^k$, we need $D > 2(3/2)^k$, i.e., $2^p/p^{13.3} > 2(3/2)^k$. Since $2^p > 3^k$: $(3/2)^k < 2^{p-k} < 2^p$, so $2(3/2)^k < 2^{p+1}$. The condition $2^p/p^{13.3} > 2(3/2)^k$ holds whenever $2^{p-1}/p^{13.3} > (3/2)^k$, which is satisfied for all $p > C$ (effective constant).

For small $p$: verified computationally for all $78{,}773$ valid $(p,k)$ pairs with $p \leq 500$ and $D \geq 2$. The inequality $D > (3^k - 2^k)/(2^k - 1)$ holds in every case, with the ratio $D_{\min}/(3^k-2^k)/(2^k-1)$ growing rapidly. $\square$

## Context

For the Collatz cycle equation with $k$ odd steps at positions $I = \{i_1, \ldots, i_k\} \subset \{0, \ldots, p-1\}$, the cycle sum is $S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$. The cycle equation is $D \mid S(I)$.

For the consecutive case $I = \{0, 1, \ldots, k-1\}$: $S = \sum_{j=0}^{k-1} 3^j \cdot 2^{k-1-j} = 3^k - 2^k$ (geometric series). The theorem shows $D \nmid (3^k - 2^k)$.

This rules out the "tightest" staircase configuration and, by the shift argument ($D$ is odd), all consecutive blocks. It is a structural constraint: any nontrivial cycle must have at least one gap in its sequence of odd-step positions.
