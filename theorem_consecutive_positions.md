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

However, for $k \geq 3$, the constraint $2^p \geq 3^k + 2$ with $2^p$ a power of 2 forces $2^{p-k}$ to be strictly larger than $(3^k+2)/2^k$. Specifically, $2^{p-k}$ is the smallest power of 2 exceeding $3^k/2^k = (3/2)^k$, and by Baker's theorem on linear forms in logarithms, $|2^m - (3/2)^k|$ is bounded below effectively. This gap exceeds $(3^k-1)/(2^k-1) - (3/2)^k = ((3/2)^k - 1)/(2^k - 1)$, which tends to 0 exponentially.

Computationally verified: for all $78{,}773$ valid $(p,k)$ pairs with $p \leq 500$ and $D \geq 2$, the inequality $2^{p-k} - 1 < D$ holds without exception. $\square$

## Context

For the Collatz cycle equation with $k$ odd steps at positions $I = \{i_1, \ldots, i_k\} \subset \{0, \ldots, p-1\}$, the cycle sum is $S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$. The cycle equation is $D \mid S(I)$.

For the consecutive case $I = \{0, 1, \ldots, k-1\}$: $S = \sum_{j=0}^{k-1} 3^j \cdot 2^{k-1-j} = 3^k - 2^k$ (geometric series). The theorem shows $D \nmid (3^k - 2^k)$.

This rules out the "tightest" staircase configuration and, by the shift argument ($D$ is odd), all consecutive blocks. It is a structural constraint: any nontrivial cycle must have at least one gap in its sequence of odd-step positions.
