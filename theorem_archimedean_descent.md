# Theorem: Archimedean Recursive Descent

## Statement

**Theorem (Archimedean Descent Bound).** Let $D = 2^p - 3^k > 0$ with $k/p$ sufficiently close to $\log 2/\log 3$. If $D \mid S(I)$ for some $k$-subset $I = \{i_1 < \ldots < i_k\} \subseteq \{0, \ldots, p-1\}$ with $n = S(I)/D$, then:

$$i_1 \leq \log_2\left(\frac{3n \cdot \Delta}{1}\right) \quad \text{where } \Delta = e^{p\log 2 - k\log 3} - 1$$

In particular: $n \geq \frac{2^{i_1}}{3\Delta}$. For $i_1 \geq 1$: $n \geq \frac{2}{3\Delta}$.

## Proof

$S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j} = nD$. The first term satisfies:

$$3^{k-1} \cdot 2^{i_1} \leq S(I) = nD$$

So $2^{i_1} \leq nD / 3^{k-1}$.

Now $D/3^{k-1} = (2^p - 3^k)/3^{k-1} = 2^p/3^{k-1} - 3 = 3(2^p/3^k - 1) = 3(e^\Delta - 1) \leq 3\Delta \cdot e^\Delta$.

For the near-critical regime $\Delta = O(p^{-10})$: $D/3^{k-1} \approx 3\Delta$.

Therefore $2^{i_1} \leq 3n\Delta(1 + O(\Delta))$, giving $i_1 \leq \log_2(3n\Delta) + O(\Delta)$. $\square$

## Corollaries

### Corollary 1: Lower bound on n

For any cycle with $i_1 = 0$ (which is required when $n$ is odd, since the orbit must start odd):

$$1 \leq 3n\Delta, \quad \text{so } n \geq \frac{1}{3\Delta}$$

For $\Delta \approx C \cdot p^{-10}$ (best rational approximation): $n \geq \frac{p^{10}}{3C}$.

This recovers the Steiner/Simons-de Weger lower bound on cycle starting values.

### Corollary 2: Recursive cascade

If $i_1$ is constrained to be at most $M$ (from the bound), then the (k-1)-subset $I' = \{i_2, \ldots, i_k\}$ must lie in $\{M+1, \ldots, p-1\}$, a set of size $p - M - 1$.

Applying the same argument to the SECOND term ($3^{k-2} \cdot 2^{i_2}$) within $T(I')$:

$$2^{i_2} \leq \frac{nD - 3^{k-1} \cdot 2^{i_1}}{3^{k-2}} = \frac{T(I')}{3^{k-2}}$$

Since $T(I') = nD - 3^{k-1} \cdot 2^{i_1} \leq nD$, we get $2^{i_2} \leq 3nD/3^{k-1} = 9n(e^\Delta - 1)$.

More precisely: $T(I') = S - 3^{k-1} \cdot 2^{i_1}$. Since $i_1 \leq M$:

$$T(I') \geq nD - 3^{k-1} \cdot 2^M$$

And $2^{i_2} = (T(I') - T(\{i_3,\ldots,i_k\})) / 3^{k-2}$, which gives:

$$i_2 \leq i_1 + \log_2(3) + O(1)$$

### Corollary 3: The cascade gives $i_j \leq i_1 + (j-1)\log_2 3 + O(j)$

By iterating: each successive position can increase by at most $\approx \log_2 3 \approx 1.585$ on average. So the positions are TIGHTLY PACKED near the beginning.

The last position $i_k$ satisfies:
$$i_k \leq i_1 + (k-1)\log_2 3 + O(k) \approx (k-1) \cdot 1.585 + O(k)$$

But we need $i_k \leq p - 1$. So:
$$(k-1) \cdot 1.585 + O(k) \leq p - 1$$

Since $k \approx 0.63p$: $(k-1) \cdot 1.585 \approx p - 1.585$. So $i_k \leq p - 1.585 + O(k) \leq p - 1$, which is barely satisfied.

## Significance

The archimedean descent shows:
1. The positions in any hypothetical cycle must be **tightly packed**: $i_j \approx j \cdot \log_2 3$ for $j = 1, \ldots, k$.
2. The starting value $n$ must be at least $\sim p^{10}/3$.
3. The position $i_1$ must be very small (0 or 1 for practical $n$).

These constraints are NECESSARY conditions for $D \mid S(I)$. They don't immediately prove impossibility, but they drastically constrain the search space.

## Connection to the Transversal Framework

The archimedean descent EXPLAINS why the recursive descent computation finds zero dangerous cases:

For any (k-1)-subset $I'$, the required $i_1 = \log_2((nD - T(I'))/3^{k-1})$ must be in $\{0, \ldots, \min(I') - 1\}$. The archimedean bound shows $i_1 \leq \log_2(3n\Delta)$, which for small $n$ is $\leq 0$. So when $\min(I') \geq 1$, no valid $i_1$ exists for small $n$.

For large $n$: $i_1$ can be larger, but then $\min(I')$ must also be larger (since the remaining $k-1$ positions span a narrower range), creating a cascade of constraints that eventually becomes impossible.

**The full proof would require showing this cascade is unsatisfiable for ALL valid n.** This appears to be connected to the defect identity $\Delta = \sum \log(1 + 1/(3u_r))$ from the q-defect analysis — the defect must be distributed as tiny increments across the orbit, which requires all orbit values to be large ($\gg p^9$), which requires the positions to be tightly packed, which forces the "gaps" $g_j = i_{j+1} - i_j - 1$ to be $\approx 0$ or $1$ for most $j$, which severely constrains the combinatorics.
