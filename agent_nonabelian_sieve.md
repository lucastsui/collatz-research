# Attempt at Direction 0A: Non-Abelian Sieve via Anti-Correlation

*Analysis -- 2026-03-06*

## 0. Executive Summary

**Empirical finding:** For composite D = q₁·q₂, the events {q₁ | S(I)} and {q₂ | S(I)} show strong anti-correlation: individual probabilities exceed 1/q (excess divisibility), but joint probability is 0. This is observed for all tested composite D.

**Theoretical status:** The anti-correlation is real but may be trivially true (it's equivalent to "no cycles exist"). The challenge is proving it FROM the structure of S(I), rather than deriving it FROM the non-existence of cycles.

**One genuinely new structural observation:** S(I) is never divisible by b = 3 (the last term 2^{i_k} is coprime to 3). This is the first structural non-divisibility result that doesn't require abc.

---

## 1. The Anti-Correlation Phenomenon

### Computation

For each composite D = 2^p - 3^k with D = q₁ · q₂:

| (p,k) | D | q₁ | P(q₁\|S) | q₂ | P(q₂\|S) | Product | P(D\|S) | Ratio |
|--------|---|-----|-----------|-----|-----------|---------|----------|-------|
| (10,6) | 295 | 5 | 0.286 | 59 | 0.048 | 0.0136 | 0 | 0 |
| (15,9) | 13085 | 5 | 0.168 | 2617 | 0.002 | 0.000336 | 0 | 0 |
| (16,10) | 6487 | 13 | 0.082 | 499 | 0.007 | 0.000573 | 0 | 0 |

In all cases: **individual probabilities EXCEED 1/q (excess divisibility), yet joint probability is exactly 0 (perfect anti-correlation).**

For (16,10): the product formula predicts ~4.6 solutions, but the actual count is 0.

### Control experiment

For Q = 6 = 2·3 (which does NOT divide D):
- P(3 | S(I)) = 0 identically (structural: see Section 2)
- P(2 | S(I)) = (p-k)/p (structural: depends on whether 0 ∈ I)

The mod-2 and mod-3 behaviors are STRUCTURALLY determined, not statistical. This suggests looking for structural reasons for the anti-correlation at primes dividing D.

---

## 2. Structural Non-Divisibility by b = 3

### Theorem

For all subsets I with |I| = k: gcd(S(I), 3) = 1.

### Proof

$S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$.

The term with j = k has coefficient $3^0 = 1$, so it contributes $2^{i_k}$ to S(I). All other terms ($j < k$) have coefficient divisible by 3.

Therefore $S(I) \equiv 2^{i_k} \pmod{3}$.

Since $\gcd(2, 3) = 1$: $2^{i_k} \not\equiv 0 \pmod{3}$.

Hence $3 \nmid S(I)$. QED.

### Generalization

For general $(a, b)$: $S(I) = \sum b^{k-j} a^{i_j}$. The last term is $b^0 \cdot a^{i_k} = a^{i_k}$. So $S(I) \equiv a^{i_k} \pmod{b}$. Since $\gcd(a, b) = 1$ (multiplicatively independent): $b \nmid S(I)$.

Similarly: $S(I) \equiv b^{k-1} \cdot a^{i_1} + \text{(terms with higher powers of a)} \pmod{a}$. The first term contributes $b^{k-1} \cdot a^{i_1}$. If $i_1 = 0$: $S(I) \equiv b^{k-1} \pmod{a}$, so $a \nmid S(I)$. If $i_1 \geq 1$: $a | S(I)$, but $a \nmid D$ (since $D = a^p - b^k$ is coprime to $a$), so this is irrelevant.

**This is the first structural non-divisibility result for S(I) that doesn't invoke prime factorization of D.**

---

## 3. Why the Anti-Correlation Might Be Provable

### The geometric coefficient structure

The coefficients $3^{k-1}, 3^{k-2}, \ldots, 1$ form a geometric progression in 3. Modulo a prime $q$:

$S(I) \equiv \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j} \pmod{q}$

The condition $q | S(I)$ restricts the positions I based on the interaction of $\operatorname{ord}_q(2)$ (which determines the "phase pattern" of the $2^{i_j}$ terms) and $\operatorname{ord}_q(3)$ (which determines the "weight pattern" of the $3^{k-j}$ coefficients).

For two primes $q_1, q_2 | D$: the conditions $q_1 | S(I)$ and $q_2 | S(I)$ impose different phase-weight patterns. If $\operatorname{ord}_{q_1}(2), \operatorname{ord}_{q_1}(3)$ and $\operatorname{ord}_{q_2}(2), \operatorname{ord}_{q_2}(3)$ are "generically different" (which they are, since $q_1 \neq q_2$), the two patterns may be incompatible for most subsets I.

### Precise formulation

Define the "divisibility set" for a prime $q$:

$$\mathcal{D}_q = \{I \subset \{0,\ldots,p-1\} : |I| = k, \; q \mid S(I)\}.$$

**Anti-Correlation Conjecture:** For primes $q_1, q_2 | D$ with $q_1 q_2 | D$:

$$|\mathcal{D}_{q_1} \cap \mathcal{D}_{q_2}| \leq |\mathcal{D}_{q_1}| \cdot |\mathcal{D}_{q_2}| / \binom{p}{k} \cdot (1 - \delta)$$

for some $\delta > 0$ depending on $p$ but not on $q_1, q_2$.

This says: the sets of "divisible" subsets for different primes overlap LESS than independence would predict.

### Why this might be true

The character sum at composite modulus $Q = q_1 q_2$:

$$\Sigma_Q(t) = \sum_{|I|=k} e(t S(I)/Q)$$

does NOT factor as $\Sigma_{q_1}(t_1) \cdot \Sigma_{q_2}(t_2)$ (because $e_k$ of a Hadamard product $\neq$ product of $e_k$'s).

The non-factorization creates interference between the $q_1$-pattern and $q_2$-pattern. If this interference is DESTRUCTIVE (reducing the character sum), it gives anti-correlation.

**Key insight:** The geometric coefficients $3^{k-j}$ create a COUPLING between the rank $j$ and the value of the coefficient mod each prime. This coupling is different for each prime (because $\operatorname{ord}_{q_1}(3) \neq \operatorname{ord}_{q_2}(3)$ in general). The rank-dependent coupling makes the mod-$q_1$ and mod-$q_2$ conditions "compete" for the same degrees of freedom (the positions $i_j$), creating anti-correlation.

---

## 4. What Would Be Needed to Make This Rigorous

### Step 1: Composite character sum bound

Prove: for $Q = q_1 q_2$ with $q_1, q_2$ "good" primes dividing $D$:

$$\left|\sum_{|I|=k} e(t S(I)/Q)\right| \leq \binom{p}{k} \cdot Q^{-1/2 - \epsilon}$$

for some $\epsilon > 0$. Compare with the factored bound:

$$\leq \binom{p}{k} \cdot q_1^{-1/2} \cdot q_2^{-1/2} = \binom{p}{k} \cdot Q^{-1/2}$$

The extra $\epsilon$ is the anti-correlation. Even $\epsilon = c/\log Q$ would suffice.

### Step 2: Iterate across prime pairs

If the anti-correlation holds for every pair of primes in D, the sieve gives:

$$\#\{I : D \mid S\} \leq \binom{p}{k} \cdot \prod_{q|D} q^{-1/2-\epsilon} = \binom{p}{k} \cdot D^{-1/2-\epsilon}$$

For this to be $< 1$: need $D^{1/2+\epsilon} > \binom{p}{k} \approx 2^{0.95p}$.

Since $D \approx 2^p$: need $(2^p)^{1/2+\epsilon} > 2^{0.95p}$, i.e., $1/2 + \epsilon > 0.95$, i.e., $\epsilon > 0.45$.

This is an ENORMOUS $\epsilon$. The per-pair anti-correlation would need to be very strong (almost as strong as the full equidistribution).

### Why this fails

The needed $\epsilon > 0.45$ means we need $Q^{-0.95}$ instead of $Q^{-0.5}$ for composite character sums. This would be an improvement of the Weil bound from $\sqrt{Q}$ to $Q^{0.95}$ for composite moduli.

But the Weil bound $\sqrt{Q}$ is SHARP for individual characters. Getting $Q^{0.95}$ requires cancellation across MULTIPLE characters, which is exactly what the sieve does. So the non-abelian sieve collapses back to the standard sieve.

---

## 5. A Modified Approach: Cumulative Anti-Correlation

Instead of pairwise anti-correlation, consider the CUMULATIVE effect across all $\omega(D)$ primes simultaneously.

### Setup

Let $q_1 < q_2 < \cdots < q_m$ be the prime factors of $D$ (so $m = \omega(D)$).

Define the conditional probabilities:

$$p_j = P(q_j \mid S(I) \;\mid\; q_1 \cdots q_{j-1} \mid S(I)).$$

By the chain rule:

$$P(D \mid S(I)) = p_1 \cdot p_2 \cdot p_3 \cdots p_m.$$

The standard sieve assumes $p_j \approx 1/q_j$ (independence). Anti-correlation means $p_j < 1/q_j$ for $j \geq 2$.

### The key question

Does the CONDITIONING on divisibility by $q_1, \ldots, q_{j-1}$ make divisibility by $q_j$ LESS likely?

Intuitively: the subsets I surviving the first $j-1$ divisibility conditions are "selected" — they have specific structural properties (related to the positions $i_1, \ldots, i_k$ matching the phase patterns of $q_1, \ldots, q_{j-1}$). These selected subsets may be LESS compatible with the $q_j$ phase pattern.

### Numerical evidence

For (16,10), D = 13 × 499:
- P(13|S) = 0.082 (656 subsets out of 8008)
- Among those 656 subsets: P(499|S | 13|S) = 0/656 = 0

So the conditional probability drops from 0.007 (unconditional) to 0 (conditional on 13|S). This is TOTAL conditional anti-correlation.

But this is just restating "no cycles exist" in conditional probability language. The challenge remains: proving this from structure.

---

## 6. Honest Assessment

### What works

1. **S(I) is never divisible by b = 3** (or by a = 2 when 0 ∈ I). This is a genuine structural result, provable from the coefficient pattern.

2. **Empirical anti-correlation is observed** for all composite D tested. The effect is strong (ratio = 0 in all cases).

3. **The geometric coefficient structure creates rank-dependent coupling** between mod-$q_1$ and mod-$q_2$ conditions. This is a real mathematical phenomenon, not an artifact.

### What doesn't work

1. **The pairwise anti-correlation needed ($\epsilon > 0.45$) is far beyond any known character sum improvement.** Even the best composite-modulus results (Bourgain) give $\epsilon = o(1)$, not $\epsilon > 0.45$.

2. **The empirical anti-correlation might be trivially true** — it might follow from "no cycles exist" rather than implying it. Proving anti-correlation from structure (without already knowing the conjecture) is the unsolved problem.

3. **The cumulative approach** (chain of conditional probabilities) is a repackaging of the sieve, not a genuinely new method.

### Conclusion

Direction 0A (non-abelian sieve) produces a concrete conjecture (anti-correlation across prime factors of D for the geometric-coefficient sum S(I)) with numerical support. But proving this conjecture appears to be AS HARD as the original Collatz conjecture. The anti-correlation is not an independent property of S(I) — it IS the no-cycles property, viewed through the lens of the sieve.

The structural non-divisibility by $b$ is new but insufficient (it only eliminates one prime from consideration, and $b \nmid D$ anyway).

**Status: 0A does not yield a viable path. The anti-correlation is real but circular (proving it = proving the conjecture).**
