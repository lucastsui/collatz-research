# The Archimedean Bound Argument

## Setup

Suppose $D \mid S(I)$ where $S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$ with $i_1 < \ldots < i_k$.

Write $n = S(I)/D \geq 1$.

## The Key Bound

**Lemma (Position-Constrained Bound).** If $D \mid S(I)$ with $n = S(I)/D$, then for each $j = 1, \ldots, k$:

$$2^{i_j} \leq \frac{n \cdot D}{3^{k-j}} = n \cdot \frac{2^p - 3^k}{3^{k-j}}$$

**Proof.** $S(I) = n \cdot D$. The term $3^{k-j} \cdot 2^{i_j}$ is at most $S(I)$ (since all terms positive). So $3^{k-j} \cdot 2^{i_j} \leq n \cdot D$, giving $2^{i_j} \leq nD/3^{k-j}$.

In particular, for $j = 1$ (the first/smallest position):
$$2^{i_1} \leq \frac{nD}{3^{k-1}}$$

Since $D = 2^p - 3^k$ and $3^{k-1} = 3^k/3$:
$$2^{i_1} \leq \frac{3n(2^p - 3^k)}{3^k} = 3n\left(\frac{2^p}{3^k} - 1\right) = 3n(e^\Delta - 1)$$

where $\Delta = p \log 2 - k \log 3 > 0$ is the criticality slack.

For the near-critical case ($\Delta \ll 1$): $e^\Delta - 1 \approx \Delta$, so:
$$2^{i_1} \leq 3n\Delta$$

Since $\Delta = O(p^{-10})$ for the best rational approximation: $2^{i_1} \leq 3n/p^{10}$.

For $i_1 \geq 1$: $2 \leq 3n/p^{10}$, giving $n \geq 2p^{10}/3$. **This is the Steiner bound on starting values.**

## Application to Recursive Descent

In the recursive descent, we peel off the first term:
$$S(I) = 3^{k-1} \cdot 2^{i_1} + T(I')$$

For $S(I) = nD$:
$$3^{k-1} \cdot 2^{i_1} = nD - T(I')$$

The required position $i_1$ satisfies:
$$2^{i_1} = \frac{nD - T(I')}{3^{k-1}}$$

For this to be a power of 2 (integer), $3^{k-1}$ must divide $nD - T(I')$.

**Key observation:** $T(I') = \sum_{j=2}^k 3^{k-j} \cdot 2^{i_j}$, so:
$$nD - T(I') = S(I) - T(I') = 3^{k-1} \cdot 2^{i_1}$$

which is automatically divisible by $3^{k-1}$ (tautologically). So the divisibility condition is automatic.

The REAL constraint is: $2^{i_1}$ must be a SPECIFIC positive integer, AND $i_1 < i_2 = \min(I')$.

From the archimedean bound: $2^{i_1} \leq nD/3^{k-1} = 3n(e^\Delta - 1)$.

The value $2^{i_1}$ is determined by $n$ and $I'$: $2^{i_1} = (nD - T(I'))/3^{k-1}$.

For this value to satisfy $i_1 < \min(I')$: need $2^{i_1} < 2^{\min(I')}$, i.e., $(nD - T)/3^{k-1} < 2^{\min(I')}$.

Rearranging: $T(I') > nD - 3^{k-1} \cdot 2^{\min(I')}$.

## The Critical Inequality

**Claim:** For any (k-1)-subset $I' \subseteq \{0, \ldots, p-1\}$ and any positive integer $n$:

$$T(I') > nD - 3^{k-1} \cdot 2^{\min(I')} \quad \text{or} \quad \frac{nD - T(I')}{3^{k-1}} \text{ is not a power of 2}$$

This would prove $0 \notin R$ (no cycles).

**The first condition** says: the tail is "too large" for $i_1$ to be small enough. Rearranging: $T + 3^{k-1} \cdot 2^{\min(I')} > nD$, i.e., $S(\{\min(I')\} \cup I') > nD$ where the first term uses position $\min(I')$ instead of $i_1$. But $\min(I') \in I'$, so this isn't a valid subset (repeated position).

**The second condition** says: even if the inequality fails, the quotient isn't a power of 2.

## Why This Might Be Provable

The tail $T(I')$ is itself bounded:
$$T(I') \geq T_{\min} = \sum_{j=2}^k 3^{k-j} \cdot 2^{j-1} = 3^{k-2} \cdot 2 + \ldots + 2^{k-1}$$

For the critical ratio: $T_{\min} = (3^{k-1} - 2^{k-1})/2 \cdot (2/3)^?$... this needs computation.

The point is: $T(I')$ grows exponentially with $p$ (like $3^k$), while $3^{k-1} \cdot 2^{\min(I')}$ grows like $3^{k-1} \cdot 2^m$ where $m = \min(I')$. For $m$ small (say $m \leq p/2$), the second quantity is $\ll 3^k$, so the first condition holds when $nD \lesssim T + 3^{k-1} \cdot 2^m \lesssim 2 \cdot 3^k \approx 2D$.

For $n = 1$: need $T + 3^{k-1} \cdot 2^m > D$, i.e., $T > D - 3^{k-1} \cdot 2^m$. Since $D = 2^p - 3^k$ and $3^{k-1} \cdot 2^m < 3^k$ (for $m < p$): $D - 3^{k-1} \cdot 2^m > 2^p - 2 \cdot 3^k \approx -3^k < 0$. So the condition $T > \text{negative number}$ is trivially true!

**Wait — this means for $n = 1$, the first condition is ALWAYS satisfied?**

Let me verify: $T(I') > D - 3^{k-1} \cdot 2^{\min(I')}$. We need $T > D - 3^{k-1} \cdot 2^m$.

$D = 2^p - 3^k$. $3^{k-1} \cdot 2^m \leq 3^{k-1} \cdot 2^{p-1} \approx 3^{k-1} \cdot 2^p / 2 \approx 3^k \cdot 2^p / (2 \cdot 3) \approx D/... $ hmm.

For $m = 0$: $3^{k-1} \cdot 2^0 = 3^{k-1}$. $D - 3^{k-1} = 2^p - 3^k - 3^{k-1} = 2^p - 4 \cdot 3^{k-1}$.
$T \geq T_{\min} = 3^{k-2} \cdot 2 + \ldots + 2^{k-1} = 3^{k-1} - 2^{k-1}$ (formula for the min tail).
Need $3^{k-1} - 2^{k-1} > 2^p - 4 \cdot 3^{k-1}$, i.e., $5 \cdot 3^{k-1} > 2^p + 2^{k-1}$.
Since $3^k = 3 \cdot 3^{k-1} < 2^p$: $3^{k-1} < 2^p/3$. So $5 \cdot 3^{k-1} < 5 \cdot 2^p/3 = 5/3 \cdot 2^p$.
And $2^p + 2^{k-1} \approx 2^p$.
So need $5/3 > 1$, which is true. But the bound is tight for large p.

Actually: $5 \cdot 3^{k-1} - 2^{k-1} > 2^p$. Since $3^k \approx 2^p$: $5 \cdot 3^{k-1} \approx 5/3 \cdot 2^p$. And $2^{k-1} \ll 2^p$. So $5/3 \cdot 2^p > 2^p$. YES!

**So for n = 1 and m = 0: the archimedean bound proves $i_1 < 0$, which is impossible!**

But what about n > 1? For $n = 2$: need $T > 2D - 3^{k-1} \cdot 2^m$. $2D \approx 2 \cdot 2^p$, and $T \leq T_{\max} \approx 3^{k-1} \cdot 2^p$. Since $3^{k-1} \approx 2^p/3$: $T_{\max} \approx 2^{2p}/3$. And $2D \approx 2^{p+1}$. So $T_{\max} / 2D \approx 2^p/6 \gg 1$ for large p. The bound is satisfied for ALL n ≤ some threshold.

**This is the core of a potential proof!** The archimedean bound shows that for each n, the required $i_1$ is constrained, and the position constraint $i_1 < \min(I')$ eliminates it.

Let me make this precise...
