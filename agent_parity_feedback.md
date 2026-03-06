# Parity Feedback Analysis for Collatz No-Cycles

## 1. Overview and Motivation

The carry analysis (Agent C, Round 11) established that for a hypothetical Collatz cycle of period $p$ with $k$ odd steps at positions $I = \{i_1 < \cdots < i_k\}$:

- The cycle equation $n_0 = S(I)/D$ where $S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$ and $D = 2^p - 3^k$
- The carry weight identity $W_c(I) = \sum_{m=0}^{k-1} s_1(3^m) - s_1(n_0 D)$
- The 2-adic cascade determining $n_0$ bit-by-bit

These provide a factor of $\sim 2^{0.05p}$ reduction (from $D | S(I)$). The missing piece is **parity feedback**: the pattern $I$ must be self-consistent with the trajectory it generates. This document analyzes the parity feedback constraint.

---

## 2. The Self-Consistency Condition

### 2.1 Statement

A pattern $I = \{i_1 < \cdots < i_k\} \subseteq \{0, \ldots, p-1\}$ is **self-consistent** if:

1. $D = 2^p - 3^k > 0$
2. $D \mid S(I)$ (arithmetic divisibility)
3. $n_0 = S(I)/D \geq 1$
4. The Collatz trajectory starting at $n_0$ has parity pattern exactly $I$ and returns to $n_0$ after $p$ steps

Conditions 1--3 are the **arithmetic constraint**. Condition 4 is the **parity feedback constraint**.

### 2.2 Why condition 4 is separate from conditions 1--3

The cycle equation $n_0 = S(I)/D$ encodes the identity:

$$T^p(n_0) = \frac{3^k}{2^p} n_0 + \frac{S_{\text{add}}(I)}{2^p} = n_0$$

where $S_{\text{add}}(I)$ accumulates the "+1" contributions from odd steps. This equation is derived by ASSUMING the pattern is $I$ and REQUIRING $T^p(n_0) = n_0$.

But the cycle equation does not guarantee that the ACTUAL trajectory from $n_0$ follows pattern $I$. Starting from $n_0$, the Collatz map produces a definite trajectory $n_0, n_1, n_2, \ldots$ with a definite parity sequence. This actual parity sequence may differ from $I$.

**The cycle equation says:** "If the pattern were $I$, then the orbit would close at $n_0$."
**Self-consistency requires:** "The pattern IS $I$."

These are logically distinct. The cycle equation is necessary but not sufficient.

### 2.3 Trajectory formula

The compressed Collatz map is $T(n) = (3n+1)/2$ if $n$ is odd, $T(n) = n/2$ if $n$ is even. After $j$ steps:

$$n_j = \frac{3^{k_j} \cdot n_0 + C_j}{2^j}$$

where $k_j = |I \cap \{0, \ldots, j-1\}|$ is the number of odd steps in the first $j$ positions, and $C_j$ is the additive contribution from the "+1"s:

$$C_j = \sum_{\substack{\ell \in I \\ \ell < j}} 3^{k_j - k_{\ell} - 1} \cdot 2^\ell$$

The self-consistency condition at step $j$ is:

$$n_j \equiv b_j \pmod{2}, \quad b_j = \begin{cases} 1 & \text{if } j \in I \\ 0 & \text{if } j \notin I \end{cases}$$

which translates to:

$$3^{k_j} \cdot n_0 + C_j \equiv b_j \cdot 2^j \pmod{2^{j+1}}$$

---

## 3. The Parity Congruence Cascade

### 3.1 A chain of binary constraints

For each $j = 0, 1, \ldots, p-1$, the self-consistency gives:

$$3^{k_j} \cdot n_0 + C_j \equiv b_j \cdot 2^j \pmod{2^{j+1}} \quad \ldots (\star_j)$$

Since $3^{k_j}$ is always odd (hence invertible modulo any power of 2), each constraint $(\star_j)$ determines $n_0 \bmod 2^{j+1}$ uniquely:

$$n_0 \equiv (3^{k_j})^{-1} (b_j \cdot 2^j - C_j) \pmod{2^{j+1}}$$

### 3.2 Hierarchical structure

The constraints form a **refining tower**:

- $(\star_0)$ determines $n_0 \bmod 2$. Since $k_0 = 0$ and $C_0 = 0$: $n_0 \equiv b_0 \pmod{2}$. So $n_0$ is odd iff $0 \in I$.
- $(\star_1)$ determines $n_0 \bmod 4$, refining $(\star_0)$.
- In general, $(\star_j)$ determines $n_0 \bmod 2^{j+1}$, refining all previous constraints.

For these to be **mutually consistent**, the residue from $(\star_j)$ must agree modulo $2^j$ with the residue from $(\star_{j-1})$. This is guaranteed by the construction: if $n_{j-1}$ has the correct parity, then the formula for $n_j$ using the correct step (odd or even) automatically gives a consistent refinement.

**Key insight:** The constraints $(\star_0), (\star_1), \ldots, (\star_{p-1})$ are NOT independent. Each one is consistent with all previous ones IF AND ONLY IF the actual trajectory from $n_0$ matches $I$ through step $j$.

### 3.3 The cascade as a single equation

After all $p$ steps, the constraints collectively determine $n_0 \bmod 2^p$. Combined with the cycle equation $n_0 = S(I)/D$, which determines $n_0$ exactly, the self-consistency reduces to:

**Does the unique $n_0 = S(I)/D$ satisfy all $p$ parity constraints simultaneously?**

Each parity constraint is a single-bit condition on the trajectory. If we think of the trajectory as a deterministic function of $n_0$, then the parity pattern is completely determined by $n_0$. The question is whether this determined pattern equals $I$.

### 3.4 Degrees of freedom

The pattern $I$ has $\log_2 \binom{p}{k} \approx 0.949p$ bits of information (for $k \approx 0.631p$).

From $I$, the value $n_0 = S(I)/D$ is computed. Since $n_0 < S_{\max}/D$ and $S_{\max} \approx 2^{p + O(\log p)}$ while $D \approx 2^{p - 0.05p}$, we have $n_0 < 2^{0.05p + O(\log p)}$. Wait -- this needs more care.

Actually, $S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$. The largest possible $S$ is when the large 3-powers are paired with large 2-powers. We have $S < k \cdot 3^{k-1} \cdot 2^{p-1}$ crudely. Since $3^{k-1} \approx 2^{(k-1)\log_2 3} \approx 2^{p - \delta - \log_2 3}$ and $D \approx 2^{p-\delta}(2^\delta - 1)$:

$$n_0 < \frac{k \cdot 3^{k-1} \cdot 2^{p-1}}{D} \approx \frac{k \cdot 2^{2p - \delta - \log_2 3 - 1}}{2^{p-\delta} \cdot (2^\delta - 1)} = \frac{k \cdot 2^{p - \log_2 3 - 1}}{2^\delta - 1}$$

For $\delta \approx 0.05p$: $n_0 < k \cdot 2^{p - 1.585 - 1} / (2^{0.05p} - 1) \approx 0.631p \cdot 2^{0.95p - 2.585} / 2^{0.05p} \approx p \cdot 2^{0.9p}$.

So $n_0$ can be as large as $2^{0.9p + O(\log p)}$. The information content is $\log_2 n_0 \leq 0.9p + O(\log p)$.

However, most of this range is NOT achievable. The Kolmogorov complexity argument shows that only $\sim 2^{0.37p}$ distinct $n_0$ values are reachable (those whose trajectory has exactly $k$ odd steps among $p$ steps). So the effective information in $n_0$ is $\sim 0.37p$ bits.

But $I$ contains $\sim 0.949p$ bits. The map $I \mapsto n_0$ compresses $0.949p$ bits into $0.37p$ bits. This means many patterns $I$ map to the same $n_0$ (on average, $\sim 2^{0.579p}$ patterns per $n_0$ value).

**However**, the parity feedback constraint says: among all patterns mapping to a given $n_0$, at most ONE can be self-consistent (since $n_0$ determines its trajectory, which determines its parity pattern uniquely). So self-consistency selects at most one $I$ per $n_0$ value, eliminating a factor of $\sim 2^{0.579p}$.

But wait: this reasoning needs refinement. Not all $n_0$ values have $D | S(I)$. The number of patterns with $D | S(I)$ is $\sim \binom{p}{k}/D \approx 2^{0.949p - 0.05p} = 2^{0.899p}$. Each such pattern gives a distinct $n_0$ (generically). The self-consistency requires each $n_0$'s actual parity to match, which is a $p$-bit condition on a value determined by a $p$-bit input.

### 3.5 The non-independence problem

If the parity constraints $(\star_0), \ldots, (\star_{p-1})$ were independent (each having probability 1/2 of being satisfied given the previous ones), the self-consistency would contribute a factor of $2^{-p}$, giving:

$$\text{Expected cycles} = \binom{p}{k} \cdot \frac{1}{D} \cdot 2^{-p} \approx 2^{0.949p - 0.05p - p} = 2^{-0.101p} \to 0$$

This would prove no nontrivial cycles! But the constraints are NOT independent -- each constraint $(\star_j)$ is a CONSEQUENCE of the previous constraints if the pattern is correct up to step $j$.

The correct count of independent constraints: the cycle equation $n_0 = S(I)/D$ already incorporates the COMBINATION of all $p$ constraints into one. The individual constraints $(\star_j)$ are redundant with the cycle equation in a subtle way.

**The precise relationship:** The cycle equation encodes $T^p(n_0) = n_0$ ASSUMING pattern $I$. The individual constraints encode $\text{parity}(n_j) = b_j$ for each $j$. The cycle equation is DERIVED from the individual constraints plus closure, so it is a consequence. But the individual constraints are NOT derived from the cycle equation -- the cycle equation is weaker.

**How much weaker?** The cycle equation is one equation ($D | S(I)$, which is $\sim \log_2 D \approx 0.05p$ bits of constraint). The individual parity constraints are $p$ equations. So the "parity feedback" provides approximately $p - 0.05p = 0.95p$ bits of ADDITIONAL constraint beyond divisibility.

But again, these additional bits are not all independent of each other.

---

## 4. Counting Independent Constraints

### 4.1 The bit-by-bit propagation

Consider building $n_0$ bit by bit from the LSB. At step $j$:

- We know $n_0 \bmod 2^j$ (from previous constraints).
- Constraint $(\star_j)$ determines $n_0 \bmod 2^{j+1}$, i.e., it fixes one new bit of $n_0$.
- This new bit is determined by $I$ (specifically, by $b_j$ and the bits of $n_0$ already determined).

So the cascade is perfectly determined: given $I$, there is exactly one $n_0 \bmod 2^p$ satisfying all constraints. This $n_0 \bmod 2^p$ is uniquely determined by $I$ through the cascade.

**But we ALSO know $n_0 = S(I)/D$.** This gives $n_0$ exactly (not just modulo $2^p$). The two determinations must agree.

### 4.2 The 2-adic vs. exact agreement

The cascade gives $n_0 \bmod 2^p$. The cycle equation gives $n_0$ exactly. For consistency:

$$S(I)/D \equiv n_{0,\text{cascade}} \pmod{2^p}$$

Since $S(I) = n_0 \cdot D = n_0 \cdot (2^p - 3^k)$:

$$S(I) \equiv -n_0 \cdot 3^k \pmod{2^p}$$

$$n_0 \equiv -(3^k)^{-1} \cdot S(I) \pmod{2^p}$$

The cascade determines $n_0 \bmod 2^p$ by propagating parities. The cycle equation determines $n_0 \bmod 2^p$ by the algebraic relation $n_0 \equiv -S \cdot (3^k)^{-1} \pmod{2^p}$.

**These two computations give the same result!** Here is why:

The cascade says: starting from $n_0$, apply $T$ according to pattern $I$ for $p$ steps, and enforce each parity. This gives:

$$n_0 \cdot \frac{3^k}{2^p} + \frac{C_p}{2^p} = n_p = n_0$$

$$\Rightarrow n_0 = \frac{C_p}{2^p - 3^k} = \frac{C_p}{D}$$

But $C_p = S(I)$ (the additive terms sum to $S(I)$). So the cascade and the cycle equation give IDENTICALLY the same $n_0$.

**This means: the parity constraints $(\star_0), \ldots, (\star_{p-1})$ are AUTOMATICALLY SATISFIED by $n_0 = S(I)/D$, as long as $n_0$ is a positive integer.**

### 4.3 Wait -- that cannot be right

If self-consistency were automatic, then EVERY pattern with $D | S(I)$ would give a valid cycle. But we know computationally that the trivial cycles are the only ones.

**The error in the above reasoning:** The derivation of the cycle equation ASSUMES the parities match $I$. If we start with arbitrary $n_0$ and apply $T$, the actual parities may differ from $I$, so the trajectory formula $n_j = (3^{k_j} n_0 + C_j)/2^j$ may not hold (because $k_j$ counts the ASSUMED odd steps, not the ACTUAL ones).

More precisely: the formula $n_j = (3^{k_j} n_0 + C_j)/2^j$ is valid ONLY IF the actual parities at steps $0, 1, \ldots, j-1$ match the assumed pattern $I$. If any parity differs, the formula breaks down from that point.

So the cascade is: **check at each step $j$ whether the formula still holds**. At step 0, the formula is $n_0 = n_0$ (trivially true). The parity of $n_0$ is either odd or even. If $n_0$ is odd and $0 \in I$, step 0 is consistent; if $n_0$ is even and $0 \notin I$, step 0 is consistent. Otherwise, failure at step 0.

**The subtlety:** $n_0 = S(I)/D$ already encodes the assumption that the pattern is $I$. But this $n_0$ may have the wrong parity for step 0.

### 4.4 The actual constraint

The parity of $n_0$ is determined by $n_0 = S(I)/D$. Since $D$ is odd and $S(I) = 2^{i_1} \cdot S'(I)$ with $S'(I)$ odd:

$$v_2(n_0) = i_1$$

So $n_0$ is odd iff $i_1 = 0$, i.e., iff $0 \in I$. This is CONSISTENT with $b_0 = [0 \in I]$. So step 0 is always consistent!

**Step 1:** $n_1 = T(n_0)$. If $0 \in I$ (odd step), $n_1 = (3n_0+1)/2$. The parity of $n_1$ depends on $n_0 \bmod 4$:
- $n_0 \equiv 1 \pmod{4}$: $n_1 = (3+1)/2 = 2 \Rightarrow$ even.
- $n_0 \equiv 3 \pmod{4}$: $n_1 = (9+1)/2 = 5 \Rightarrow$ odd.

If $0 \notin I$ (even step), $n_1 = n_0/2$, and $n_1$'s parity depends on $n_0 \bmod 4$:
- $n_0 \equiv 0 \pmod{4}$: $n_1 = n_0/2 \equiv 0 \pmod{2}$, even.
- $n_0 \equiv 2 \pmod{4}$: $n_1 = n_0/2 \equiv 1 \pmod{2}$, odd.

The expected parity of $n_1$ is $b_1 = [1 \in I]$. This constrains $n_0 \bmod 4$.

Now, $n_0 = S(I)/D$. What is $n_0 \bmod 4$? Since $D$ is odd, $n_0 \bmod 4 = (S(I)/D) \bmod 4 = S(I) \cdot D^{-1} \bmod 4$. This depends on the specific values of $S(I)$ and $D$.

**The key realization:** For a given pattern $I$, the value $n_0 = S(I)/D$ is a specific integer. Its residue modulo $2^j$ for any $j$ is determined. The parity cascade checks whether these residues are consistent with $I$. This is a nontrivial check because $n_0$ is built from a SUM (via $S(I)$) while the parity cascade is a SEQUENTIAL process.

---

## 5. The Fundamental Theorem of Self-Consistency

### 5.1 Statement

**Theorem (Self-Consistency Equivalence).** Let $I \subseteq \{0, \ldots, p-1\}$ with $|I| = k$, $D = 2^p - 3^k > 0$, and $D \mid S(I)$. Set $n_0 = S(I)/D$. Then the following are equivalent:

(a) The Collatz trajectory from $n_0$ has parity pattern $I$ and $T^p(n_0) = n_0$ (genuine cycle).

(b) For every $j = 0, 1, \ldots, p-1$: the intermediate value $n_j = (3^{k_j} n_0 + C_j)/2^j$ is a positive integer with $n_j \equiv b_j \pmod{2}$.

(c) Condition (b) is equivalent to: $n_0 \bmod 2^p$ equals the value computed by the 2-adic parity cascade from $I$.

**Moreover**, condition (a) is NOT automatically satisfied by condition $D \mid S(I)$. The cycle equation is a NECESSARY condition derived by assuming (a), but (a) is strictly stronger.

### 5.2 Proof sketch

$(a) \Rightarrow (b)$: Immediate from the trajectory formula.

$(b) \Rightarrow (a)$: If all intermediate values are positive integers with correct parities, then the trajectory formula is valid at each step, and $n_p = (3^k n_0 + S(I))/2^p = (3^k n_0 + n_0 D)/2^p = (3^k + D)n_0/2^p = 2^p n_0 / 2^p = n_0$.

$(b) \Leftrightarrow (c)$: The cascade determines $n_0 \bmod 2^{j+1}$ at each step, and (b) is the conjunction of all these being consistent with $n_0 = S(I)/D$.

**Why (a) doesn't follow from $D \mid S(I)$:** The cycle equation guarantees $T^p_I(n_0) = n_0$ where $T_I$ is the map that FORCES pattern $I$. But the actual map $T$ may produce a different pattern, so $T^p(n_0) \neq T^p_I(n_0)$ in general.

### 5.3 The 2-adic characterization

The self-consistency condition can be stated purely 2-adically. Define the 2-adic Collatz operator:

$$\Phi_I: \mathbb{Z}_2 \to \mathbb{Z}_2, \quad \Phi_I(n) = \frac{3^k \cdot n + S(I)}{2^p}$$

This is the "forced" cycle operator. The cycle equation says $\Phi_I(n_0) = n_0$, i.e., $n_0$ is a fixed point of $\Phi_I$ in $\mathbb{Q}$.

The ACTUAL Collatz map on $\mathbb{Z}_2$ is $T(n) = (3n+1)/2$ if $v_2(n) = 0$, $T(n) = n/2$ if $v_2(n) \geq 1$. Define $T^p(n)$ to be $p$ iterations of $T$.

Self-consistency: $T^p(n_0) = \Phi_I(n_0) = n_0$, AND the parity pattern of the orbit $(n_0, T(n_0), \ldots, T^{p-1}(n_0))$ equals $I$.

The 2-adic viewpoint: $n_0$ is the unique fixed point of $\Phi_I$ in $\mathbb{Q}_{>0}$. The parity pattern of the actual orbit from $n_0$ under $T$ is determined by $n_0 \bmod 2, T(n_0) \bmod 2, \ldots$ Matching this with $I$ is a condition on the 2-adic expansion of $n_0$.

---

## 6. Computational Investigation

### 6.1 Setup

The script `/Users/tsuimingleong/Desktop/math/parity_feedback.py` performs exhaustive checks for small $p$. For each $(p, k)$ with $D > 0$, it enumerates all $\binom{p}{k}$ patterns $I$, checks $D \mid S(I)$, and for those that pass, verifies self-consistency by running the actual Collatz trajectory.

### 6.2 Hand computation results

**$p=2, k=1$:** $D = 1$. All patterns $\{0\}$ and $\{1\}$ give $n_0 = 1$ and $n_0 = 2$ respectively. Both are trivial cycles. Both self-consistent. SC rate = 2/2 = 100%.

**$p=4, k=2$:** $D = 7$. Of $\binom{4}{2} = 6$ patterns, exactly 2 have $D \mid S$: $\{0,2\}$ ($n_0 = 1$) and $\{1,3\}$ ($n_0 = 2$). Both are trivial cycles. SC rate = 2/2 = 100%.

**$p=5, k=3$:** $D = 5$. Of $\binom{5}{3} = 10$ patterns, none have $D \mid S$. (No arithmetic solutions at all for this $(p,k)$.)

**$p=6, k=3$:** $D = 37$. Of $\binom{6}{3} = 20$ patterns, exactly 2 have $D \mid S$: $\{0,2,4\}$ ($n_0 = 1$) and $\{1,3,5\}$ ($n_0 = 2$). Both trivial cycles. SC rate = 2/2 = 100%.

**Key observation for small $p$:** For small periods, the divisibility condition $D \mid S(I)$ is already so restrictive (since $D$ is comparable in size to $S$) that only the trivial cycle patterns survive. There are no "arithmetic solutions that fail self-consistency" in this range.

### 6.3 Why non-trivial arithmetic solutions are rare for small $p$

For the cycle equation $n_0 = S(I)/D$ to have a non-trivial solution ($n_0 \geq 2$ for $I \neq$ trivial pattern), we need $S(I) \geq 2D$. Since $D = 2^p - 3^k$ and $S(I) < k \cdot 3^{k-1} \cdot 2^{p-1}$, we need:

$$k \cdot 3^{k-1} \cdot 2^{p-1} > 2 \cdot (2^p - 3^k)$$

For $k \approx 0.631p$ and large $p$, the left side grows like $2^{1.95p}$ while the right grows like $2^{p+1}$, so non-trivial solutions exist. But for small $p$, the ratio $S_{\max}/D$ is small, limiting $n_0$.

### 6.4 Expected results for larger $p$

For $p \geq 10$ with appropriate $(p,k)$ pairs, more patterns will satisfy $D \mid S(I)$ (because $\binom{p}{k}$ grows faster than $D$). Among these, self-consistency will eliminate most. The script computes the exact elimination rate.

**Prediction:** The SC rate (fraction of arithmetic solutions that are self-consistent) should decay roughly as $2^{-cp}$ for some constant $c > 0$, reflecting the $p$-bit parity constraint.

---

## 7. Formalizing the Self-Consistency Constraint Strength

### 7.1 The core counting argument

**Proposition (Parity Feedback Bound).** For fixed $(p, k)$ with $D = 2^p - 3^k > 0$:

(i) The number of patterns $I$ with $D \mid S(I)$ is $\leq \binom{p}{k} / D + O(\binom{p}{k}^{1/2})$ (by equidistribution).

(ii) Among patterns with $D \mid S(I)$, the number that are self-consistent is at most the number of $n_0$ values whose $p$-step Collatz trajectory has exactly $k$ odd steps and returns to $n_0$.

(iii) The number of such $n_0$ values is at most $2^{0.37p + O(\log p)}$ (by the Kolmogorov reduction).

*Proof of (iii):* A $p$-periodic Collatz orbit is determined by $n_0$, and $n_0$ is determined by its trajectory pattern. The trajectory pattern is a binary string of length $p$ with $k$ ones, but among those compatible with a genuine orbit, only $\sim 2^{0.37p}$ are achievable (since each orbit loses $\log_2 3 - 1 \approx 0.585$ bits per odd step, and the net information loss is $(1 - \log_2(3)/2) \cdot p \approx 0.208p$ bits...

Actually, let me be more precise. The Kolmogorov argument from Round 3: the pattern $I$ is determined by $n_0$ (for a genuine cycle). The number of distinct $n_0$ values is bounded by $\max(S)/D \approx 2^{0.9p}/2^{0.05p} = 2^{0.85p}$. But the actual number is much smaller because $n_0$ must satisfy the parity constraints.

A more precise bound: $n_0$ determines the trajectory, and the trajectory determines $I$. The map $n_0 \mapsto I$ is injective on genuine cycles (distinct starting points give distinct patterns, since the cycle is determined by its parity sequence). So the number of self-consistent patterns equals the number of valid $n_0$ values, which equals the number of $p$-periodic orbits of the Collatz map with exactly $k$ odd steps.

### 7.2 The information-theoretic bound

The effective constraint from self-consistency can be quantified as follows:

- **Input:** A pattern $I$ with $\binom{p}{k}$ possibilities.
- **Arithmetic filter:** $D \mid S(I)$ eliminates a factor of $D$, leaving $\binom{p}{k}/D \approx 2^{0.899p}$ patterns.
- **Parity feedback:** Each surviving pattern gives $n_0 = S(I)/D$. The actual trajectory from $n_0$ has a definite pattern $I'$. The condition $I' = I$ is a constraint on $0.949p$ bits.

The question is how many of the $0.949p$ bits are "free" (already determined by $n_0$) versus "constrained" (genuinely independent conditions).

**Key insight:** $n_0$ has $\log_2 n_0$ bits. Since $n_0$ determines $I'$ uniquely, and $I'$ has $0.949p$ bits, we need $\log_2 n_0 \geq 0.949p$ for the map $n_0 \mapsto I'$ to be injective on the image. But $n_0$ can have up to $0.9p$ bits, so the map is generically injective.

The constraint is: $I' = I$ is a $0.949p$-bit condition on a $0.9p$-bit input ($n_0$). But $n_0$ is already determined by $I$ (via $S(I)/D$), so the constraint reduces to: the composition $I \xrightarrow{S/D} n_0 \xrightarrow{\text{trajectory}} I'$ must be the identity.

This composition is a map $\binom{[p]}{k} \to \binom{[p]}{k}$ (restricted to the $\sim 2^{0.899p}$ patterns with $D \mid S$). Self-consistent patterns are fixed points of this map. The number of fixed points of a "random-looking" map on $N$ elements is $\sim 1$ (by Poisson statistics), which would give the desired result.

### 7.3 The random-map heuristic

**Heuristic (Self-Consistency as a Random Map).** Assume the map $\sigma: I \mapsto I' = \text{actual\_parity}(S(I)/D)$ behaves like a random map on the $N \approx 2^{0.899p}$ patterns satisfying $D \mid S(I)$. Then:

- The expected number of fixed points is 1.
- The distribution of the number of fixed points is Poisson(1).
- With probability $1 - 1/e \approx 0.632$, there are no non-trivial fixed points.

**Justification:** The map $I \mapsto I'$ involves two very different operations: (1) the algebraic computation $S(I)/D$ (which depends on exponential sums), and (2) the dynamical iteration of the Collatz map (which is known to behave "pseudo-randomly" for large arguments). The composition should scramble the pattern enough to act like a random map.

**Caveat:** The trivial cycle patterns are fixed points by construction. The heuristic applies to non-trivial patterns.

### 7.4 Why the random-map heuristic is hard to prove

Proving that $\sigma$ behaves like a random map requires showing that the image of $\sigma$ is approximately uniformly distributed over $\binom{[p]}{k}$-subsets (restricted to the arithmetic-compatible ones). This is essentially equivalent to showing that the Collatz map has good mixing properties on the relevant scale -- which is closely related to the original conjecture.

---

## 8. The Carry Perspective on Parity Feedback

### 8.1 How carries encode parity

In the carry analysis of $S(I) = \sum T_j$, the carry sequence $c_0, c_1, \ldots$ is built from the binary additions. The bits of $S(I)$ are:

$$s_r = \left(\sum_{j} b_r(T_j) + c_r\right) \bmod 2$$

with $c_{r+1} = \lfloor(\sum_j b_r(T_j) + c_r)/2\rfloor$.

Now, $S(I) = n_0 \cdot D = n_0 \cdot (2^p - 3^k)$. The lower $p$ bits of $S(I)$ equal $(-n_0 \cdot 3^k) \bmod 2^p$. So:

$$s_r = \text{bit } r \text{ of } (-n_0 \cdot 3^k \bmod 2^p) \quad \text{for } 0 \leq r < p$$

These bits of $S$ determine $n_0 \bmod 2^p$ (since $3^k$ is invertible mod $2^p$).

The parity of $n_j$ depends on $n_0 \bmod 2^{j+1}$. So the first $j+1$ bits of $S(I)$ (determined by the carry cascade through position $j$) encode $n_0 \bmod 2^{j+1}$, which determines $n_j$'s parity.

### 8.2 The carry-parity coupling

**The parity of $n_j$ is encoded in the carry structure of $S(I)$ at bit positions $0, \ldots, j$.**

Specifically:
1. The bits $s_0, \ldots, s_j$ of $S(I)$ determine $n_0 \bmod 2^{j+1}$.
2. These bits are determined by the column sums $\sigma_0, \ldots, \sigma_j$ and carries $c_0, \ldots, c_j$.
3. The column sums depend on which terms $T_m$ are active at positions $0, \ldots, j$.
4. For position $r$, the active terms are those with $L_m \leq r \leq H_m$, i.e., $i_m \leq r \leq i_m + (k-m) \cdot 1.585$.

For self-consistency, the carry pattern at position $j$ must produce the correct parity for $n_j$, which in turn determines whether position $j$ is an odd or even step, which feeds back into the sum $S(I)$.

### 8.3 The feedback loop in carry terms

The feedback loop is:

$$I \xrightarrow{\text{column sums}} \sigma_0, \sigma_1, \ldots \xrightarrow{\text{carry propagation}} c_0, c_1, \ldots \xrightarrow{\text{bits of } S} s_0, s_1, \ldots \xrightarrow{(3^k)^{-1}} n_0 \bmod 2^p \xrightarrow{\text{trajectory}} I'$$

For self-consistency, $I' = I$. Each stage of this pipeline is deterministic, so the composition is a well-defined map $I \mapsto I'$.

**The carry structure mediates the parity feedback.** Changes to $I$ (moving an odd step from position $a$ to position $b$) alter the column sums at positions around $a$ and $b$, which propagate through the carry chain, changing $S(I)$ and hence $n_0$, which changes the trajectory and hence $I'$.

### 8.4 Sensitivity of carries to pattern changes

A key question is: how sensitive is the carry cascade to small changes in $I$?

If the carry cascade is highly sensitive (chaotic), then the map $I \mapsto I'$ is effectively random, supporting the random-map heuristic.

If the carry cascade has low sensitivity (stable), then perturbations of $I$ lead to small perturbations of $I'$, and fixed points might cluster.

**Heuristic analysis:** The carry cascade propagates perturbations over $O(\log k)$ bit positions before the perturbation either dies out or doubles. In the overlap-heavy early terms, perturbations propagate long distances. In the gap regions, perturbations decay. The net effect depends on the balance.

For a "typical" pattern with Sturmian gap structure ($g_j \in \{0, 1\}$), the overlap is dense and carries propagate throughout. A single bit change in $I$ (moving one odd position) affects $O(p)$ bits of $S(I)$, hence $O(p)$ bits of $n_0$, which scrambles the trajectory. This supports high sensitivity and the random-map heuristic.

---

## 9. Symbolic Dynamics and Kneading Theory

### 9.1 The Collatz map as a piecewise-linear map

The compressed Collatz map $T: \mathbb{Z}_{>0} \to \mathbb{Z}_{>0}$ is piecewise-defined:

$$T(n) = \begin{cases} n/2 & n \equiv 0 \pmod{2} \\ (3n+1)/2 & n \equiv 1 \pmod{2} \end{cases}$$

A $p$-periodic orbit $\{n_0, n_1, \ldots, n_{p-1}\}$ has a symbolic itinerary $\omega = (\omega_0, \omega_1, \ldots, \omega_{p-1}) \in \{L, R\}^p$ where $L$ (left, even) and $R$ (right, odd) correspond to the two branches. Here $\omega_j = R$ iff $j \in I$.

### 9.2 The admissibility condition

Not every symbolic sequence is realized by an actual orbit. The **admissibility condition** specifies which sequences correspond to genuine orbits.

For the Collatz map, the admissibility is determined by the parity of $n_j$, which depends on the ARITHMETIC of the previous steps (not just the symbolic dynamics). This is fundamentally different from smooth maps (like quadratic maps), where admissibility is determined by a kneading inequality involving only the symbolic sequence.

### 9.3 Collatz kneading vs. classical kneading

In classical kneading theory (for unimodal maps), a symbolic sequence $\omega$ is admissible iff it satisfies a family of inequalities determined by the kneading invariant. The kneading invariant encodes the symbolic dynamics of the critical point.

For the Collatz map, there is no "critical point" in the usual sense. Instead, the boundary between branches is $n = 0.5$ (not an integer), and the map is defined only on positive integers. The "kneading condition" for Collatz is:

**For each $j$:** $n_j = (3^{k_j} n_0 + C_j) / 2^j$ is a positive integer with the correct parity.

This can be reformulated as: $3^{k_j} n_0 + C_j \equiv b_j \cdot 2^j \pmod{2^{j+1}}$.

Since $3^{k_j}$ is odd, this is: $n_0 \equiv r_j \pmod{2^{j+1}}$ for specific computable $r_j$.

### 9.4 The kneading as a fixed-point equation in 2-adic integers

The self-consistency can be written as a fixed-point equation in $\mathbb{Z}_2$ (2-adic integers). Define $F: \mathbb{Z}_2 \to \mathbb{Z}_2$ by:

$$F(x) = \frac{S(\text{parity\_pattern}(x))}{D}$$

where $\text{parity\_pattern}(x)$ is the set of positions where $T^j(x)$ is odd (for $j = 0, \ldots, p-1$), and $S$ is the cycle sum.

A fixed point $x^* = F(x^*)$ in $\mathbb{Z}_2 \cap \mathbb{Z}_{>0}$ corresponds to a genuine cycle.

**The map $F$ is NOT continuous** on $\mathbb{Z}_2$ because the parity pattern changes discontinuously at every value where some $T^j(x)$ passes through an even/odd boundary. However, $F$ is locally constant on the intervals where the parity pattern is fixed. Each such interval is a residue class modulo $2^p$ (since the parity of $T^j(x)$ depends only on $x \bmod 2^{j+1}$, and all $p$ parities depend on $x \bmod 2^p$).

So the map is: for each residue class $r \bmod 2^p$, compute $I_r = \text{parity\_pattern}(r)$, then $F(r) = S(I_r)/D$. A fixed point requires $F(r) = r$ (as a positive integer).

There are $2^p$ residue classes, each mapping to a specific $n_0 = S(I_r)/D$. For this to be a fixed point, we need $n_0 \equiv r \pmod{2^p}$.

### 9.5 Counting fixed points via the kneading map

**Proposition.** The number of self-consistent patterns is exactly the number of $r \in \{0, 1, \ldots, 2^p - 1\}$ such that:

1. The parity pattern $I_r$ of the orbit from $r$ (computed modulo $2^p$) has exactly $k$ odd steps.
2. $D \mid S(I_r)$.
3. $S(I_r)/D = r$ (as a positive integer).

Or equivalently: $S(I_r) = r \cdot D$, and $I_r$ has exactly $k$ elements.

This reformulation makes it clear that we're looking for fixed points of a specific map on $\{0, \ldots, 2^p - 1\}$. The map is the composition of "compute parity pattern" and "compute $S/D$."

---

## 10. Quantitative Estimates

### 10.1 Expected number of self-consistent patterns

Using the analysis from Section 7, we estimate:

$$\text{Expected \# of self-consistent patterns with } k \text{ odd steps} \leq \min\left(\frac{\binom{p}{k}}{D}, |\{n_0 : n_0 \text{ has a } p\text{-cycle with } k \text{ odd steps}\}|\right)$$

The first bound comes from arithmetic ($D \mid S$). The second comes from the bijection between self-consistent patterns and valid starting values.

If the map $I \mapsto I'$ behaves randomly, the expected number of fixed points among the $\sim \binom{p}{k}/D$ arithmetic solutions is:

$$E[\text{fixed points}] \approx \frac{\binom{p}{k}/D}{\binom{p}{k}} = \frac{1}{D} \approx 2^{-0.05p}$$

This is less than 1 for all $p \geq 1$, suggesting no non-trivial cycles. But this estimate assumes the map is a uniformly random permutation/function, which is too strong.

### 10.2 A more careful estimate

The map $I \mapsto I'$ is NOT uniformly random. Its image is constrained to be the actual parity pattern of SOME positive integer, which excludes most of the $\binom{p}{k}$ patterns.

A better estimate: the number of achievable parity patterns for $n_0$ in the range $[1, \max(S)/D]$ is at most $\max(S)/D \approx 2^{0.9p}$ (one pattern per starting value). Among the $\binom{p}{k}/D \approx 2^{0.899p}$ arithmetic solutions, each maps to one of $\sim 2^{0.9p}$ achievable patterns. The "collision" probability (that the image pattern equals the input pattern) is roughly $1/\binom{p}{k} \approx 2^{-0.949p}$.

So:

$$E[\text{non-trivial fixed points}] \approx 2^{0.899p} \cdot 2^{-0.949p} = 2^{-0.05p} \to 0$$

This matches the simpler estimate and suggests no non-trivial cycles.

### 10.3 What this gives us

The parity feedback constraint, combined with arithmetic divisibility, gives a total expected count of:

$$\binom{p}{k} \cdot \Pr[D | S] \cdot \Pr[\text{SC} | D | S] \approx 2^{0.949p} \cdot 2^{-0.05p} \cdot 2^{-0.949p} = 2^{-0.05p}$$

The factor $\Pr[\text{SC} | D | S] \approx 1/\binom{p}{k} \approx 2^{-0.949p}$ comes from the heuristic that the actual pattern is a random element of $\binom{[p]}{k}$.

**But this heuristic might overclaim.** The actual pattern from $n_0$ is not uniformly random in $\binom{[p]}{k}$. It has specific structure (e.g., the density of odd steps is close to $\log 2 / \log 3$, gaps follow a Sturmian-like pattern for typical starting values). If the actual patterns from different $n_0$ cluster in a specific region of $\binom{[p]}{k}$, the collision probability could be higher.

---

## 11. Interaction with Carry Structure

### 11.1 The joint constraint

The self-consistency and the carry weight identity are not independent. For a self-consistent pattern:

1. **Carry weight identity:** $W_c(I) = \sum s_1(3^m) - s_1(n_0 D)$.
2. **Parity feedback:** The bits of $S(I)$ (determined by carries) encode $n_0$, whose trajectory reproduces $I$.

The carry weight constrains $s_1(n_0 D)$, which constrains $n_0$. The parity feedback further constrains $n_0$ to produce pattern $I$. Together, these are much more restrictive than either alone.

### 11.2 The carry weight as a filter

From the carry analysis: $W_c \approx 0.158 p^2 - 0.815p$ for a typical pattern. The carry weight identity gives $s_1(n_0 D) = \sum s_1(3^m) - W_c \approx 0.396 k^2 - W_c$.

For a self-consistent pattern, $n_0$ is the starting value of a genuine cycle. The Hamming weight $s_1(n_0 D) = s_1(n_0 (2^p - 3^k))$ depends sensitively on $n_0$.

**For the trivial cycle** ($n_0 = 1$): $s_1(D)$ is the Hamming weight of $2^p - 3^k$, which is computable. The carry weight identity holds.

**For a hypothetical non-trivial cycle** ($n_0 \gg 1$): $n_0 D = n_0 \cdot 2^p - n_0 \cdot 3^k$. The Hamming weight of this difference depends on the binary structure of $n_0 \cdot 3^k$. Generically, $s_1(n_0 D) \approx p/2 + (\log_2 n_0)/2$ (half the bits are 1).

Combined with the carry weight identity: $W_c \approx 0.396 k^2 - p/2$. But from the direct computation of carry weight for random patterns: $W_c \approx 0.158 p^2 - p$. The discrepancy between these two estimates ($0.158 p^2$ from direct carry analysis vs. $0.396 k^2 - p/2 \approx 0.158 p^2 - p/2$ from the identity) provides a consistency check.

### 11.3 The carry weight concentration as additional evidence

From the carry analysis: the carry weight $W_c$ for random patterns is concentrated around its mean with standard deviation $O(p)$. For self-consistent patterns, $W_c$ must equal $\sum s_1(3^m) - s_1(n_0 D)$ exactly. Since $s_1(n_0 D)$ can only take $O(p)$ distinct values (it ranges from 1 to $p + O(\log p)$), the carry weight identity eliminates most candidate pairs $(I, n_0)$.

But this alone provides only a factor of $O(p)$ reduction, which is far short of the needed $2^{0.9p}$.

---

## 12. The Critical Question: How Much Does Parity Feedback Actually Constrain?

### 12.1 Three scenarios

**Scenario A (Optimistic): Full $2^{-p}$ constraint.** Each parity step provides an independent binary constraint. The self-consistency rate among arithmetic solutions is $2^{-p}$, giving expected cycles $\sim 2^{-0.05p} \to 0$. This would prove no non-trivial cycles.

**Scenario B (Intermediate): $2^{-cp}$ constraint for some $0 < c < 1$.** The parity constraints are partially correlated but still exponentially constraining. If $c > 0.899$ (so $2^{0.899p} \cdot 2^{-cp} < 1$), this suffices. We need $c > 0.899$.

**Scenario C (Pessimistic): $2^{-o(p)}$ constraint.** The parity constraints are highly correlated, providing only polynomial or subexponential reduction. This is insufficient.

### 12.2 Evidence for Scenario B

The information-theoretic analysis (Section 3.4) gives:
- The pattern $I$ has $0.949p$ bits.
- The cycle equation compresses this to $n_0$ with $\leq 0.9p$ bits.
- Parity feedback requires $I = I'$, a $0.949p$-bit match.
- The "collision probability" is $\sim 2^{-0.949p}$ if the map $I \mapsto I'$ is random.

This gives $c \approx 0.949$, which exceeds $0.899$. The total expected count is $2^{0.899p - 0.949p} = 2^{-0.05p}$.

**But this relies on the random-map assumption.** The actual constraint could be weaker.

### 12.3 A rigorous lower bound on the constraint

Can we PROVE that self-consistency provides at least $2^{-cp}$ reduction for some $c > 0$?

**Partial result:** The first parity constraint (step 0) is automatically satisfied (Section 4.4). The second parity constraint (step 1) eliminates roughly half the patterns (those where $n_0 \bmod 4$ gives the wrong parity for $n_1$). So after 2 steps, we've eliminated a factor of $\sim 2$.

More generally, each step $j$ constrains $n_0 \bmod 2^{j+1}$ given $n_0 \bmod 2^j$. The new bit of $n_0$ is determined by $I$ through the sum $S(I) \bmod 2^{j+1}$. For this bit to match the parity of $n_j$, a specific condition must hold.

**The condition at step $j$:** bit $j$ of $(3^{k_j} \cdot n_0 + C_j)$ must equal $b_j$. Since bit $j$ of $3^{k_j} \cdot n_0$ depends on $n_0 \bmod 2^{j+1}$ (which is already determined by $I$ through the cycle equation), this is a CHECK on whether the forced value agrees with the required value.

How often does this check pass? If the forced value and required value are independent mod 2, then $\Pr[\text{pass}] = 1/2$. But they're NOT independent -- the forced value depends on $S(I) \bmod 2^{j+1}$, which involves the same positions $I$ that determine $b_j$.

### 12.4 The correlation structure

At step $j$, the parity check involves:
- $n_0 \bmod 2^{j+1}$, determined by $S(I) \bmod 2^{j+1} = \sum_{m: i_m \leq j} T_m \bmod 2^{j+1}$ plus carries from terms with $i_m \leq j$.
- $b_j = [j \in I]$, a single bit from the pattern.

The check asks whether a specific function of $\{i_m : i_m \leq j\}$ and the carry cascade through position $j$ equals $b_j$.

For $j$ such that many terms contribute at position $j$ (the overlap-heavy region), the check involves a complex function of many bits of $I$, making it effectively random. For $j$ in a gap region (no term starts near $j$), the check depends mainly on carry propagation from earlier positions, which is already determined -- so the check may be redundant.

**The number of "effectively independent" checks** is roughly the number of positions $j$ where a new term $T_m$ begins (i.e., $j = i_m$ for some $m$). There are $k$ such positions. At each, the contribution of $T_m$ introduces new information that interacts with the carry cascade and the parity requirement.

This gives approximately $k \approx 0.631p$ effectively independent checks, each with probability $\sim 1/2$, yielding a constraint of $\sim 2^{-0.631p}$.

**Combined with $D \mid S$:** Total expected count $\sim 2^{0.949p} \cdot 2^{-0.05p} \cdot 2^{-0.631p} = 2^{0.268p}$.

This is STILL growing, leaving a gap of $2^{0.268p}$. The remaining constraint must come from the GAP positions (the $p - k$ even-step positions).

---

## 13. The Gap Positions and Carry Propagation

### 13.1 Information at gap positions

At a gap position $j \notin I$ (even step), the parity check is: $n_j$ is even. This requires:

$$3^{k_j} \cdot n_0 + C_j \equiv 0 \pmod{2^{j+1}}$$

Since $k_j$ and $C_j$ don't change during a gap (no new odd steps), the carry cascade continues to propagate through the gap using only the tails of earlier terms.

**The parity check at gap positions IS informative** because it constrains the carry propagation. Even though no new term starts, the carry from earlier positions must produce the correct parity.

### 13.2 Carry propagation during gaps

In a gap of length $g_j$ between odd positions $i_j$ and $i_{j+1}$, the column sum at each position involves:
- Tails of terms $T_1, \ldots, T_j$ (those with bit ranges extending past $i_j$).
- The incoming carry from the previous position.

The carry evolves as $c_{r+1} = \lfloor(c_r + \sigma_r)/2\rfloor$ where $\sigma_r$ counts the active term bits.

In the gap, the bits of $S(I)$ at positions $i_j + 1, \ldots, i_{j+1} - 1$ are determined by the carry cascade and the tails of earlier terms. Each of these bits contributes to $n_0 \bmod 2^{r+1}$, and hence to the parity of $n_r$.

**Each gap position provides an additional parity constraint.** The check is whether the carry cascade through the gap produces the correct parity at each position. Since the carry cascade is a deterministic (but complex) function of the earlier bits, these constraints are partially determined by earlier choices.

### 13.3 Effective constraint from gaps

During a gap of length $g_j$, the carry from position $i_j$ propagates through $g_j$ positions. The carry sequence $c_{i_j+1}, \ldots, c_{i_{j+1}}$ is determined by:
- $c_{i_j}$ (the carry entering the gap)
- The tails of terms $T_1, \ldots, T_j$ at positions $i_j+1, \ldots, i_{j+1}-1$

These tails are the bits of $3^{k-1}, 3^{k-2}, \ldots, 3^{k-j}$ at specific offsets, which are FIXED (they don't depend on $I$ -- they depend only on which terms are present, which is determined by $I$ through the positions $i_1, \ldots, i_j$).

So during a gap, the carry cascade is a DETERMINISTIC process given the carry entering the gap. The parity checks at gap positions $r \in (i_j, i_{j+1})$ constrain the carry, which constrains $n_0$.

**However:** since the carry entering the gap is already determined by earlier positions, and the gap carries are deterministic from there, the gap parity checks are ALSO determined by earlier positions. So they don't provide ADDITIONAL constraints beyond those from the odd positions!

Wait -- that's not quite right. The issue is that the sum $S(I)$ and the parity cascade give TWO DIFFERENT computations of $n_0 \bmod 2^r$, and they must agree. The sum computation involves the carry cascade, while the parity cascade is the Collatz trajectory. These are different processes that must produce the same answer.

The gap positions DO provide additional constraints because the Collatz trajectory at gap positions depends on $n_0$ in a way that's NOT captured by the sum $S(I)$. The sum gives $n_0 = S/D$, while the trajectory gives $n_j = T^j(n_0)$. The agreement of these at each step is nontrivial.

---

## 14. The Central Difficulty and Path Forward

### 14.1 Why a proof is hard

The parity feedback analysis reveals a fundamental difficulty: the self-consistency constraint is EQUIVALENT to the existence of a genuine Collatz cycle. Proving that no self-consistent patterns exist is equivalent to proving the Collatz no-cycles conjecture.

The various reductions and estimates in this document do not avoid this equivalence -- they reformulate it in different languages (carry cascades, kneading conditions, fixed-point equations). The value is in identifying the STRUCTURE of the constraint, which may enable new approaches.

### 14.2 What we've learned

1. **The parity feedback is a separate constraint from divisibility.** The condition $D \mid S(I)$ is necessary but not sufficient. Self-consistency is an additional $p$-bit constraint.

2. **The constraint strength depends on the correlation between the sum $S(I)$ and the trajectory.** If these are "effectively independent," the constraint eliminates a factor of $\sim 2^{-0.949p}$, which combined with divisibility gives expected count $\sim 2^{-0.05p} \to 0$.

3. **The carry cascade mediates the feedback.** The bits of $S(I)$ are determined by binary carries, and these same bits determine the trajectory. The carry structure creates long-range correlations that could either help or hinder the proof.

4. **The random-map heuristic gives the right answer.** Heuristically, the expected number of non-trivial cycles is $\sim 2^{-0.05p}$, which is consistent with the Collatz conjecture. Making this rigorous requires proving decorrelation between the sum and trajectory computations.

5. **The information-theoretic gap is $\sim 0.05p$ bits in our favor.** This is a small margin, reflecting the fact that $k \approx p \cdot \log 2 / \log 3$ is very close to the threshold. The proof difficulty is related to this small margin.

### 14.3 Concrete path forward

**Goal:** Prove that for large $p$, no self-consistent non-trivial pattern exists.

**Strategy:** Show that the map $I \mapsto I' = \text{actual\_parity}(S(I)/D)$ has no non-trivial fixed points among the $\sim 2^{0.899p}$ patterns with $D \mid S(I)$.

**Possible approaches:**

**(A) Local expansion.** Show that for any non-trivial $I$ with $D \mid S(I)$, the actual pattern $I'$ differs from $I$ in at least $\Omega(p)$ positions. This would show the map has no "near-fixed points," let alone fixed points.

To prove this: suppose $I$ and $I' = \text{actual\_parity}(S(I)/D)$ agree in positions $0, \ldots, j-1$ but disagree at position $j$. Then the actual trajectory from $S(I)/D$ diverges from the assumed pattern at step $j$. The question is: can the divergence be "corrected" by subsequent steps? If the Collatz map is expanding (which it is, on average, by a factor of $3/2$ per odd step), then a parity error at step $j$ leads to a trajectory that diverges from the assumed one by an amount that grows exponentially. This makes further agreement increasingly unlikely.

**(B) Carry cascade sensitivity.** Show that the carry cascade in $S(I)$ is sensitive to the pattern $I$: changing the pattern at one position changes $S$ by a significant amount (not just in the lowest bits), which changes $n_0$, which changes the trajectory. If the sensitivity is exponential in $p$ (as expected from the expanding dynamics), then the map $I \mapsto I'$ is a "near-permutation" with no fixed points.

**(C) 2-adic contraction.** The operator $\Phi_I(x) = (3^k x + S(I))/2^p$ is a contraction on $\mathbb{Z}_2$ (with Lipschitz constant $3^k/2^p < 1$). Its unique fixed point is $n_0 = S(I)/D$. But we need $n_0$ to be a POSITIVE INTEGER that generates pattern $I$. The contraction means that $n_0$ is robust (small perturbations of $S$ change $n_0$ by small amounts), which doesn't help directly. However, the contraction of $\Phi_I$ combined with the expansion of the Collatz map $T$ creates a tension: $T$ expands orbits while $\Phi_I$ contracts -- this tension may forbid fixed points.

---

## 15. A New Algebraic Identity: The Parity Checksum

### 15.1 Derivation

For a self-consistent pattern, define the **parity checksum**:

$$\Pi(I, n_0) = \sum_{j=0}^{p-1} (-1)^{b_j} \cdot n_j$$

where $n_j = T^j(n_0)$ and $b_j = [j \in I]$.

For a genuine cycle: $n_j$ is odd when $b_j = 1$ and even when $b_j = 0$. So:

$$\Pi = \sum_{j \in I} (-1) \cdot n_j + \sum_{j \notin I} (+1) \cdot n_j = \sum_{j \notin I} n_j - \sum_{j \in I} n_j$$

Using $n_{j+1} = (3n_j + 1)/2$ for $j \in I$ and $n_{j+1} = n_j/2$ for $j \notin I$:

$$\sum_{j=0}^{p-1} n_{j+1} = \sum_{j \in I} \frac{3n_j + 1}{2} + \sum_{j \notin I} \frac{n_j}{2}$$

$$\sum_{j=1}^{p} n_j = \frac{3}{2}\sum_{j \in I} n_j + \frac{k}{2} + \frac{1}{2}\sum_{j \notin I} n_j$$

Since the cycle is periodic: $\sum_{j=0}^{p-1} n_j = \sum_{j=1}^{p} n_j$. Let $A = \sum_{j \in I} n_j$ and $B = \sum_{j \notin I} n_j$. Then:

$$A + B = \frac{3A + k}{2} + \frac{B}{2} = \frac{3A + B + k}{2}$$

$$2A + 2B = 3A + B + k$$

$$B = A + k$$

So $\Pi = B - A = k$. This is a known identity: the sum of trajectory values at even steps minus the sum at odd steps equals $k$ (the number of odd steps).

### 15.2 Generalized checksums

More generally, for any function $f$:

$$\sum_{j=0}^{p-1} f(n_{j+1}) = \sum_{j \in I} f\left(\frac{3n_j+1}{2}\right) + \sum_{j \notin I} f\left(\frac{n_j}{2}\right)$$

For $f(n) = n^2$: this gives a quadratic identity relating $\sum n_j^2$ to sums involving $n_j$ at odd and even steps.

For $f(n) = (-1)^n$: this gives a mod-2 checksum that directly probes the parity structure.

These generalized checksums provide additional constraints that must hold for a self-consistent pattern. Each is a necessary condition that could potentially rule out non-trivial cycles.

---

## 16. Summary and Open Questions

### 16.1 Main results

1. **The self-consistency condition is a genuine constraint** beyond $D \mid S(I)$. It requires that $n_0 = S(I)/D$ generates the trajectory with parity pattern $I$. This is NOT automatic from the cycle equation.

2. **The constraint is equivalent to a fixed-point condition** on the map $I \mapsto I' = \text{actual\_parity}(S(I)/D)$, acting on the $\sim 2^{0.899p}$ patterns satisfying $D \mid S(I)$.

3. **Heuristically, the constraint eliminates $\sim 2^{-0.949p}$ fraction**, giving expected non-trivial cycle count $\sim 2^{-0.05p} \to 0$.

4. **The carry cascade mediates the feedback**, creating a specific mechanism for the interaction between the sum structure and the trajectory dynamics.

5. **The algebraic identity $B - A = k$** (Section 15) provides a necessary checksum condition for cycles.

### 16.2 Open questions

1. **Can the decorrelation between $S(I)/D$ and the trajectory parity be proved?** This is the key step needed to convert the heuristic into a proof.

2. **What is the actual self-consistency failure rate for larger $p$?** The computational script should provide data for $p$ up to 24. If the rate is $\sim 2^{-cp}$ with $c$ near 0.949, the heuristic is confirmed.

3. **Can the carry sensitivity be quantified?** If changing one position in $I$ changes $\Omega(p)$ bits of $n_0$, this supports the random-map heuristic.

4. **Can the expanding property of the Collatz map be used?** The map expands by a factor of $3/2$ on average. Over $p$ steps, a parity error at step $j$ leads to a trajectory divergence of $(3/2)^{p-j}$, which is enormous. Can this expansion be used to prove that self-consistency forces the trivial pattern?

5. **Is there a connection to the spectral gap?** The spectral gap of the affine Collatz operator (proved to be positive for each prime) controls the mixing of the Collatz dynamics. Can this mixing be used to prove decorrelation between $S$ and the trajectory?

### 16.3 Computational verification

The script `/Users/tsuimingleong/Desktop/math/parity_feedback.py` should be run with:

```
/Users/tsuimingleong/Desktop/math/venv/bin/python /Users/tsuimingleong/Desktop/math/parity_feedback.py
```

It will produce:
- Part 3: Exhaustive self-consistency check for $p \leq 22$
- Part 4: First-failure position distribution
- Part 5: Degrees of freedom table
- Part 6: Self-consistency failure rate scaling
- Part 7: Information-theoretic analysis
- Part 8: Carry-parity interaction data
- Part 9: Kneading/cycle search
- Part 10: Detailed modular propagation examples

### 16.4 Relationship to the overall program

This analysis fills in the "parity feedback" gap identified in the carry analysis (Agent C, Round 11, Section 19.4). The missing factor of $2^{0.899p}$ is accounted for by the self-consistency constraint (heuristically $\sim 2^{0.949p}$, with $0.05p$ to spare).

**PATH B (Carry Analysis) status after this work:**
- Carry weight identity: PROVED
- 2-adic cascade: PROVED (determines $n_0$ from $I$)
- Parity feedback: FORMALIZED (this document), HEURISTIC bound obtained
- Total constraint: $2^{0.949p} \cdot 2^{-0.05p} \cdot 2^{-0.949p} = 2^{-0.05p}$ (heuristic)
- **Gap:** Making the decorrelation rigorous ($\sim$ 100% of the remaining difficulty)

The rigorous proof requires establishing that the map $I \mapsto \text{actual\_parity}(S(I)/D)$ has no non-trivial fixed points. This is the equivalent of the Collatz no-cycles conjecture in the carry-analysis framework.

---

## 17. The Contraction-Expansion Duality (Key New Insight)

### 17.1 Two competing dynamics

The self-consistency analysis reveals a fundamental duality at the heart of the Collatz no-cycles problem:

**The contraction:** The operator $\Phi_I(x) = (3^k x + S(I))/2^p$ is a CONTRACTION on $\mathbb{Z}_2$. Its Lipschitz constant is $3^k/2^p < 1$ (since $k < p \log 2/\log 3$). The fixed point $n_0 = S(I)/D$ is unique and STABLE under iteration of $\Phi_I$. Small perturbations of $x$ are contracted toward $n_0$.

**The expansion:** The Collatz map $T(n)$ is EXPANDING on average. Each odd step multiplies by $3/2 > 1$. Over $p$ steps with $k$ odd steps, the expansion factor is $(3/2)^k / 2^{p-k} \cdot 2^p = (3/2)^k$. Wait, that's not right. Let me compute properly.

The derivative of $T^p$ at a periodic point with pattern $I$ is:

$$\frac{d(T^p)}{dn}(n_0) = \frac{3^k}{2^p}$$

Since $3^k/2^p < 1$ (because $D > 0$), the periodic point is ATTRACTING in the real sense! This is the contraction.

But the 2-adic expansion is different. In the 2-adic metric, the map $n \mapsto n/2$ is EXPANDING (by a factor of 2), while $n \mapsto (3n+1)/2$ multiplies the 2-adic absolute value by $|3/2|_2 = 2$. So after $p$ steps, the 2-adic expansion factor is $2^p / 3^k > 1$.

### 17.2 The duality formalized

**In the real metric:** $T^p$ contracts near $n_0$ by factor $3^k/2^p < 1$. The fixed point is stable. This is why the cycle equation has a unique solution.

**In the 2-adic metric:** $T^p$ expands near $n_0$ by factor $2^p/3^k > 1$. The fixed point is UNSTABLE in the 2-adic sense.

**The self-consistency condition lives in the 2-adic world.** The parity of $n_j$ depends on the 2-adic structure (the lowest bit) of $n_j$. The parity cascade determines $n_0 \bmod 2^p$, which is a 2-adic condition. And in the 2-adic metric, the dynamics EXPANDS perturbations.

### 17.3 Implications for self-consistency

The 2-adic expansion means: if $n_0$ is perturbed by $\epsilon$ in the 2-adic metric (i.e., $n_0' = n_0 + \epsilon \cdot 2^t$ for some $t$), then after $j$ steps, the perturbation grows to $\sim (2^p/3^k)^{j/p} \cdot \epsilon$. After $O(p)$ steps, the perturbation reaches the "bit 0" level, causing a parity change.

This means: the parity pattern is SENSITIVE to the 2-adic structure of $n_0$. Two values $n_0$ and $n_0'$ that agree modulo $2^t$ but differ at bit $t$ will produce the same parity pattern for the first $\sim t \cdot k/p$ steps, then diverge.

For a self-consistent pattern: $n_0$ must be precisely the value $S(I)/D$, AND this precise value must generate the exact parity pattern $I$. The 2-adic instability means that "nearby" patterns (those agreeing with $I$ for the first $j$ steps) correspond to $n_0$ values in a 2-adic ball of radius $2^{-j \cdot p/k}$ around $S(I)/D$. Only the exact center of this ball (the precise value $S(I)/D$) can generate pattern $I$.

### 17.4 The instability as an obstruction

**Proposition (2-adic Instability Obstruction).** Let $n_0 = S(I)/D$ for a pattern $I$ with $D \mid S(I)$. Suppose $n_0 > 0$ and the trajectory from $n_0$ agrees with pattern $I$ through step $j-1$ but disagrees at step $j$. Then:

(a) The actual value $n_j = T^j(n_0)$ satisfies $n_j \not\equiv b_j \pmod{2}$.

(b) The trajectory from $n_0$ under the ACTUAL Collatz map produces a different pattern $I'$ with $|I \triangle I'| \geq 1$. In fact, all subsequent parities may differ from $I$.

(c) The actual cycle (if $n_0$ is periodic) has a DIFFERENT pattern from $I$, and hence corresponds to a different $(p', k')$ or a different set of positions.

*Proof.* (a) is the definition of disagreement. (b) follows because once the parity disagrees at step $j$, the trajectory formula $n_{j+1} = (3n_j + 1)/2$ vs. $n_{j+1} = n_j/2$ gives a different $n_{j+1}$, and the perturbation grows by the 2-adic expansion factor. (c) follows because the actual trajectory is determined by $n_0$, not by $I$.

### 17.5 The expansion factor quantified

The 2-adic expansion factor per step is $|2/3|_2 = 2$ for odd steps and $|2|_2 = 2$ for even steps (since division by 2 expands the 2-adic norm by 2). Wait, this needs more care.

For an odd step: $T(n) = (3n+1)/2$. The perturbation: $T(n+\epsilon) - T(n) = 3\epsilon/2$. In the 2-adic metric: $|3\epsilon/2|_2 = |3|_2 \cdot |\epsilon|_2 / |2|_2 = 1 \cdot |\epsilon|_2 / (1/2) = 2|\epsilon|_2$. So the perturbation grows by factor 2.

For an even step: $T(n) = n/2$. The perturbation: $T(n+\epsilon) - T(n) = \epsilon/2$. In the 2-adic metric: $|\epsilon/2|_2 = 2|\epsilon|_2$. Again grows by factor 2.

So EVERY step (odd or even) expands by factor 2 in the 2-adic metric. After $p$ steps: $2^p$. The parity of $n_j$ depends on $|n_j|_2 = |n_0|_2 \cdot 2^j$ roughly (this is approximate because the "+1" terms break linearity).

### 17.6 What this means for the count

The 2-adic expansion by $2^p$ after $p$ steps means: the map from $n_0 \bmod 2^p$ to the parity pattern is a bijection on the $2^p$ residue classes. This is consistent with our earlier observation (Section 9.4) that the parity pattern of $n_0$ is determined by $n_0 \bmod 2^p$.

Since the map is a bijection, there are exactly $\binom{p}{k}$ residue classes (out of $2^p$) that produce patterns with exactly $k$ odd steps. The self-consistency asks: among these $\binom{p}{k}$ residue classes, which ones have $S(I_r)/D \equiv r \pmod{2^p}$ and $S(I_r)/D \leq$ some bound?

The fraction of residues satisfying $S(I_r)/D \equiv r \pmod{2^p}$ is at most $1/D$ (since $S/D$ mod $2^p$ takes each residue class with frequency $\sim 1/D$, as $S$ ranges over $D$ cosets). But this is the arithmetic constraint again.

**The key realization:** The 2-adic expansion means the map $r \mapsto I_r$ is a BIJECTION on residue classes mod $2^p$, and the map $I \mapsto S(I)/D \bmod 2^p$ is well-defined. The self-consistency asks for coincidence of these two maps: $r = S(I_r)/D \bmod 2^p$. Since both maps are "algebraically independent" (one comes from Collatz dynamics, the other from exponential sums), the coincidence should occur with probability $\sim 1/2^p$ per residue class.

But we only need $r \leq S_{\max}/D$, which limits us to $\sim S_{\max}/D$ candidates, and we need $|I_r| = k$, which limits us to $\binom{p}{k}/2^p \cdot 2^p = \binom{p}{k}$ candidates. The expected number of hits is $\binom{p}{k} \cdot (1/2^p) \cdot (\text{something})$... this needs more careful analysis.

Actually, the cleanest formulation: there are $\binom{p}{k}$ residue classes $r$ mod $2^p$ producing patterns with $k$ odd steps. For each, $S(I_r)/D$ is a rational number. The condition $S(I_r)/D \in \mathbb{Z}_{>0}$ with $S(I_r)/D \equiv r \pmod{2^p}$ is one equation in one "unknown" (the residue class $r$). By equidistribution of $S \bmod D$, the first condition ($D | S$) holds for $\sim \binom{p}{k}/D$ residues. The second ($S/D \equiv r \bmod 2^p$) is then automatic from the first (since $S/D$ determines $r$). Wait, that's circular again.

Let me think about this differently. The condition is: $S(I_r) = r \cdot D$ where $I_r$ is the parity pattern of $r$. This is a single equation relating $r$ and $I_r$. Both sides depend on $r$ (the left through $I_r$, the right directly). The question is how many $r$ satisfy this.

If $S(I_r)$ is a "random" function of $r$ (taking values in $[0, S_{\max}]$), and $r \cdot D$ is a linear function, then the expected number of intersections is $\sim S_{\max} / (S_{\max} \cdot D) = 1/D$. This gives expected count $\sim \binom{p}{k}/D$ -- but this is the ARITHMETIC count, not accounting for the constraint that $I_r$ must equal the pattern producing $r$.

The point is: the arithmetic count already incorporates the self-consistency (because we defined $I_r$ as the actual pattern of $r$). The arithmetic count $\binom{p}{k}/D$ is the number of self-consistent patterns!

**Wait -- this contradicts our earlier analysis.** Let me reconsider.

The issue is: we're conflating two different questions.

**Question A:** How many patterns $I$ (freely chosen $k$-subsets) satisfy $D | S(I)$? Answer: $\sim \binom{p}{k}/D$.

**Question B:** Among the patterns from Question A, how many are self-consistent? Answer: this is what we want to know.

**Question C (equivalent to B):** How many $r \in \{1, \ldots, S_{\max}/D\}$ have the property that the actual parity pattern $I_r$ of $r$ satisfies $S(I_r)/D = r$? This is always true by construction (since $n_0 = r$ determines $I_r$, and $S(I_r) = r \cdot D$ is the cycle equation applied with pattern $I_r$). So the answer to C is: all $r$ such that the cycle equation is satisfied.

**The self-consistency is TAUTOLOGICAL from the fixed-point perspective!** If we start with $r$ and compute its actual pattern $I_r$ and then compute $S(I_r)/D$, we get $r$ back (by the cycle equation). But this is only true if $r$ actually has a $p$-periodic orbit with $k$ odd steps.

Actually no, $S(I_r)/D = r$ is NOT automatically true. The cycle equation says: IF $r$ is a starting point of a $p$-cycle with pattern $I_r$, THEN $S(I_r)/D = r$. But the converse is what we need: does $S(I_r)/D = r$ imply $r$ is a cycle starting point?

$S(I_r)/D = r$ means $S(I_r) = r \cdot D = r \cdot (2^p - 3^k)$. Combined with the formula for the forced trajectory $\Phi_{I_r}(r) = (3^k r + S(I_r))/2^p = (3^k r + r \cdot 2^p - r \cdot 3^k)/2^p = r$. So $\Phi_{I_r}(r) = r$, meaning the forced cycle operator returns $r$. But we defined $I_r$ as the ACTUAL pattern of $r$, so the forced operator uses the correct pattern. Therefore $T^p(r) = r$, confirming $r$ is a genuine cycle starting point.

**Conclusion:** $S(I_r)/D = r$ is equivalent to $T^p(r) = r$ (given that $I_r$ is the actual pattern of $r$ with $k$ odd steps). The self-consistency IS the cycle equation, approached from the trajectory side rather than the pattern side.

### 17.7 Resolving the apparent contradiction

The two approaches give the same answer but frame it differently:

**Approach 1 (Pattern-first):** Choose pattern $I$, compute $n_0 = S(I)/D$, check if $n_0$'s actual trajectory has pattern $I$.

**Approach 2 (Trajectory-first):** Choose starting value $r$, compute actual pattern $I_r$, check if $S(I_r)/D = r$.

In Approach 1, the "self-consistency filter" is the additional constraint beyond $D | S$.
In Approach 2, the equation $S(I_r)/D = r$ is automatically satisfied for any $r$ with a $p$-periodic orbit with $k$ odd steps.

The question "how many cycles exist?" is the same in both approaches. In Approach 1, it's the number of self-consistent patterns. In Approach 2, it's the number of $r$ with $p$-periodic orbits having $k$ odd steps.

**The parity feedback constraint in Approach 1 is NOT a separate "filter" on top of the arithmetic constraint.** Instead, it REPLACES the arithmetic constraint with a more refined one. A pattern $I$ corresponds to a cycle iff $I$ is the actual parity pattern of $S(I)/D$. Among the $\binom{p}{k}$ total patterns, this selects exactly the cycle patterns -- there is no intermediate "arithmetic solutions" step.

The arithmetic constraint $D | S(I)$ is WEAKER than self-consistency. It is a necessary condition (every self-consistent pattern satisfies it) but not sufficient (there may be patterns with $D | S$ that are not self-consistent). The "self-consistency rate" measures the gap between necessary and sufficient.

### 17.8 The real question restated

The number of non-trivial $p$-periodic orbits of the Collatz map with $k$ odd steps equals:
- The number of patterns $I$ with $|I| = k$ that are self-consistent, minus 2 (the trivial cycles).

This is bounded above by $\binom{p}{k}/D$ (from the arithmetic necessary condition).

The question is: can we prove a BETTER upper bound? Specifically, can we show the count is 0 for all $p$?

The parity feedback analysis shows that the self-consistent patterns are an exponentially small fraction of the arithmetic solutions (heuristically $\sim 2^{-0.949p}$ additional factor). But making this rigorous requires understanding the map $I \mapsto I' = \text{actual\_pattern}(S(I)/D)$.

---

## 18. A Structural Theorem: The Orbit Expansion Bound

### 18.1 Statement

**Theorem (Orbit Divergence After Parity Mismatch).** Let $I$ be a $k$-subset of $\{0, \ldots, p-1\}$ with $D | S(I)$ and $n_0 = S(I)/D \geq 1$. Let $I'$ be the actual parity pattern of $n_0$ (computed by running the Collatz map from $n_0$). Suppose $I \neq I'$ and let $j_0 = \min\{j : [j \in I] \neq [j \in I']\}$ be the first position of disagreement.

Then:

$$|n_{j_0}^{(I)} - n_{j_0}^{(I')}| = 0 \quad \text{but} \quad |n_{j_0+1}^{(I)} - n_{j_0+1}^{(I')}| = \frac{1}{2}|3n_{j_0} + 1 - n_{j_0}| = \frac{|2n_{j_0} + 1|}{2} = n_{j_0} + \frac{1}{2}$$

Wait, this isn't right either. At step $j_0$, the values $n_{j_0}^{(I)} = n_{j_0}^{(I')} = n_{j_0}$ (they agree up to step $j_0$). But one path applies the odd-step map and the other applies the even-step map. So:

$$|n_{j_0+1}^{(I)} - n_{j_0+1}^{(I')}| = \left|\frac{3n_{j_0}+1}{2} - \frac{n_{j_0}}{2}\right| = \left|\frac{2n_{j_0}+1}{2}\right| = n_{j_0} + \frac{1}{2}$$

or the reverse (even vs. odd). Since $n_{j_0}$ is an integer, this divergence is $\geq 1$.

After the divergence, subsequent steps amplify or reduce the gap. On average, each step multiplies the gap by $3/2$ (for odd steps) or $1/2$ (for even steps). Over the remaining $p - j_0$ steps, the gap grows by a factor of $(3/2)^{k'}/2^{p-j_0-k'} = (3/2)^{k'} \cdot 2^{-(p-j_0-k')}$ where $k'$ is the number of odd steps in positions $j_0+1, \ldots, p-1$.

This analysis shows that a parity mismatch at step $j_0$ leads to a trajectory divergence that is at least $\sim n_{j_0}$ and grows through subsequent odd steps. For the divergent trajectory to "reconverge" to the original cycle, the divergence must be reabsorbed -- which requires very specific cancellations.

### 18.2 Implication

The orbit divergence bound means that self-consistency is extremely fragile: a single parity mismatch leads to a trajectory that is completely different from the assumed one. This supports the heuristic that self-consistency fails with overwhelming probability for non-trivial patterns.

However, turning this into a PROOF of no cycles requires showing that the divergence is never reabsorbed. For the trivial cycle (alternating pattern), the trajectory is 1, 2, 1, 2, ... and any perturbation leads to a different cycle (or divergent trajectory). But for hypothetical non-trivial cycles with large $n_0$, the divergence analysis is more subtle.

---

## Appendix A: Detailed Hand Computation for $p = 6, k = 3$

$D = 64 - 27 = 37$. Patterns with $D \mid S$:

**$I = \{0, 2, 4\}$:** $S = 9 \cdot 1 + 3 \cdot 4 + 1 \cdot 16 = 9 + 12 + 16 = 37$. $n_0 = 1$.
Trajectory: $1 \to 2 \to 1 \to 2 \to 1 \to 2 \to 1$. Parities: odd, even, odd, even, odd, even = $\{0,2,4\}$. Self-consistent.

**$I = \{1, 3, 5\}$:** $S = 9 \cdot 2 + 3 \cdot 8 + 1 \cdot 32 = 18 + 24 + 32 = 74 = 2 \cdot 37$. $n_0 = 2$.
Trajectory: $2 \to 1 \to 2 \to 1 \to 2 \to 1 \to 2$. Parities: even, odd, even, odd, even, odd = $\{1,3,5\}$. Self-consistent.

Both are the trivial cycle (alternating pattern). No non-trivial arithmetic solutions exist for this $(p,k)$.

**Carry analysis for $I = \{0,2,4\}$:**
Terms: $T_1 = 9 = 1001_2$, $T_2 = 12 = 1100_2$, $T_3 = 16 = 10000_2$.

Binary addition:
```
Position:  5 4 3 2 1 0
T_1:       0 0 1 0 0 1
T_2:       0 0 1 1 0 0
T_3:       1 0 0 0 0 0
--------------------------
Sum:       1 0 0 1 0 1  = 37 = 100101_2
Carries:   0 0 1 0 0 0  (carry from pos 2->3: 1+1=2, carry 1)
```

Wait, let me redo: position 2 has $T_1$ bit 2 = 0, $T_2$ bit 2 = 1, $T_3$ bit 2 = 0. Sum = 1, carry = 0.
Position 3: $T_1$ bit 3 = 1, $T_2$ bit 3 = 1, $T_3$ bit 3 = 0, carry in = 0. Sum = 2, bit = 0, carry out = 1.
Position 4: $T_1$ bit 4 = 0, $T_2$ bit 4 = 0, $T_3$ bit 4 = 1, carry in = 1. Sum = 2, bit = 0, carry out = 1.
Position 5: carry in = 1. Sum = 1, bit = 1.

Result: $100101_2 = 37$. Carry weight = 2 (carries at positions 3 and 4).

Carry weight identity check: $\sum s_1(3^m)$ for $m = 0,1,2$: $s_1(1) + s_1(3) + s_1(9) = 1 + 2 + 2 = 5$.
$s_1(n_0 D) = s_1(37) = s_1(100101_2) = 3$. $W_c = 5 - 3 = 2$. Checks out.

---

## Appendix B: Hand-Computed Data for Small $p$

| $p$ | $k$ | $D$ | $\binom{p}{k}$ | $\|D \mid S\|$ | $\|SC\|$ | SC rate | Notes |
|-----|-----|-----|-----------------|-----------------|----------|---------|-------|
| 2 | 1 | 1 | 2 | 2 | 2 | 1.00 | Both trivial |
| 4 | 2 | 7 | 6 | 2 | 2 | 1.00 | Both trivial |
| 5 | 2 | 23 | 10 | 0 | 0 | -- | No solutions |
| 5 | 3 | 5 | 10 | 0 | 0 | -- | No solutions |
| 6 | 3 | 37 | 20 | 2 | 2 | 1.00 | Both trivial |
| 8 | 4 | 175 | 70 | 2 | 2 | 1.00 | Both trivial$^\dagger$ |
| 10 | 5 | 781 | 252 | 2 | 2 | 1.00 | Both trivial$^\dagger$ |

$^\dagger$ Claimed based on the pattern from the carry analysis document (Appendix B), which states all exact solutions for $p \leq 24$ are trivial cycles.

**Key observation:** For all tested $(p,k)$ values, the ONLY patterns satisfying $D \mid S(I)$ are the trivial cycle patterns (alternating $\{0,2,4,\ldots\}$ and $\{1,3,5,\ldots\}$, when $k = p/2$). No non-trivial arithmetic solutions exist in this range, so the self-consistency rate is trivially 100% among arithmetic solutions.

This means the parity feedback constraint is "untested" against non-trivial candidates in the computationally accessible range. Its power will only manifest for larger $p$ where non-trivial arithmetic solutions begin to appear. The computational script `parity_feedback.py` is designed to detect and analyze such cases when they emerge.

---

## Appendix C: Computational Script

The file `/Users/tsuimingleong/Desktop/math/parity_feedback.py` contains a comprehensive computational analysis. Run with:

```bash
/Users/tsuimingleong/Desktop/math/venv/bin/python /Users/tsuimingleong/Desktop/math/parity_feedback.py
```

The script performs:
1. Exhaustive self-consistency check for all $(p,k,I)$ with $D > 0$ and $D \mid S(I)$
2. First-failure-position distribution for non-self-consistent patterns
3. Degrees of freedom analysis (comparing $\binom{p}{k}$, $|D\mid S|$, and $|SC|$)
4. Self-consistency failure rate scaling
5. Information-theoretic analysis (deficit between pattern entropy and $n_0$ entropy)
6. Carry weight comparison between SC and non-SC patterns
7. Forward cycle search from trajectory enumeration
8. Detailed modular propagation examples

**Note:** The script requires Bash access to run. The theoretical analysis in this document does not depend on the computational output.
