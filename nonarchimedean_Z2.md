# Direction 6g-xi: Non-Archimedean Dynamics on $\mathbb{Z}_2$

*Developed 2026-03-06 (Session 8)*

## 0. Executive Summary

We analyze the Collatz map $T$ as a continuous dynamical system on the 2-adic integers $\mathbb{Z}_2$. The main results:

1. **Shift conjugacy** (known): $T: \mathbb{Z}_2 \to \mathbb{Z}_2$ is topologically conjugate to the full one-sided shift $\sigma: \{0,1\}^{\mathbb{N}} \to \{0,1\}^{\mathbb{N}}$ via the coding map $\Phi(n) = (\text{parity sequence of } n)$.

2. **2-adic repulsion** (known, but map.md entry had wrong sign): Every periodic orbit is **repelling** in $\mathbb{Z}_2$ with Lyapunov exponent $\log_2 |3^k/2^p|_2 = p > 0$. The map.md entry incorrectly said "attracting" — the *archimedean* Lyapunov exponent $\log_2(3^k/2^p) < 0$ (contracting in $\mathbb{R}$), but the *2-adic* Lyapunov exponent is $+p$ (repelling in $\mathbb{Z}_2$).

3. **Self-consistency is automatic**: For each periodic parity pattern $\varepsilon$ of period $p$, there is a unique $n(\varepsilon) \in \mathbb{Z}_2$ whose parity sequence under $T$ is exactly $\varepsilon$. The "cycle condition" reduces to the single arithmetic constraint $n(\varepsilon) \in \mathbb{Z}_{>0}$, equivalently $D \mid S(\varepsilon)$.

4. **p-adic Fatou/Julia theory does not apply**: $T$ is piecewise-affine, not analytic. On each piece, $T^p$ is a single repelling affine map — the Julia set is everything, there are no Fatou components, and the no-wandering-domain theorem (Benedetto, Rivera-Letelier) is vacuous.

5. **The archimedean/non-archimedean mismatch**: The question "is $n(\varepsilon)$ a positive integer?" is an archimedean condition, invisible to the 2-adic topology. This is the same barrier encountered in all other directions, expressed in non-archimedean language.

**Status: Direction 6g-xi provides correct structural insights but FAILS to escape the fundamental barriers.**

---

## 1. The Collatz Map on $\mathbb{Z}_2$

### 1.1. Definition and Continuity

The 2-adic integers $\mathbb{Z}_2$ are the completion of $\mathbb{Z}$ with respect to the 2-adic absolute value $|n|_2 = 2^{-v_2(n)}$. Elements of $\mathbb{Z}_2$ can be written as formal power series $n = \sum_{i=0}^{\infty} b_i 2^i$ with $b_i \in \{0,1\}$.

The Collatz map $T: \mathbb{Z}_2 \to \mathbb{Z}_2$ is:

$$T(n) = \begin{cases} n/2 & \text{if } n \in 2\mathbb{Z}_2 \\ (3n+1)/2 & \text{if } n \in 1 + 2\mathbb{Z}_2 \end{cases}$$

This is well-defined and continuous on $\mathbb{Z}_2$:
- The sets $2\mathbb{Z}_2$ and $1 + 2\mathbb{Z}_2$ are clopen (open and closed).
- On $2\mathbb{Z}_2$: $T(n) = n/2$ is a contraction with $|T(n)|_2 \leq 2|n|_2$.
- On $1 + 2\mathbb{Z}_2$: $T(n) = (3n+1)/2$. Since $n$ is odd, $3n+1$ is even, so $T(n) \in \mathbb{Z}_2$. The map $n \mapsto (3n+1)/2$ is affine with slope $3/2$; in the 2-adic metric, $|3/2|_2 = 2$, so this branch is expanding by factor 2.

### 1.2. The Piecewise-Affine Structure

$T$ is piecewise-affine with two branches. The $p$-fold iterate $T^p$, restricted to a fixed parity pattern $\varepsilon = (\varepsilon_0, \ldots, \varepsilon_{p-1}) \in \{0,1\}^p$ (where $\varepsilon_i$ records the parity at step $i$), is a single affine map:

$$T^p(n) = \frac{3^k}{2^p} n + c(\varepsilon)$$

where $k = \sum \varepsilon_i$ is the number of odd steps and $c(\varepsilon)$ depends on the pattern $\varepsilon$.

The domain of this branch is the clopen set $\{n \in \mathbb{Z}_2 : T^i(n) \bmod 2 = \varepsilon_i \text{ for all } i\}$, which is a coset of $2^p \mathbb{Z}_2$ (i.e., a "2-adic ball" of radius $2^{-p}$).

**Number of valid branches**: Not all $2^p$ patterns give $D > 0$. Among the $2^p$ patterns, those with $k$ ones require $D = 2^p - 3^k > 0$, i.e., $k < p \log_2 3 \approx 0.63p$. Verified: $T^5$ has 26 valid branches (of 32), $T^7$ has 99 (of 128), $T^{10}$ has 848 (of 1024).

---

## 2. Conjugacy with the Full Shift

### 2.1. The Coding Map

Define $\Phi: \mathbb{Z}_2 \to \{0,1\}^{\mathbb{N}}$ by:

$$\Phi(n) = (n \bmod 2, \; T(n) \bmod 2, \; T^2(n) \bmod 2, \; \ldots)$$

**Theorem (Shift Conjugacy).** $\Phi$ is a homeomorphism from $\mathbb{Z}_2$ to $\{0,1\}^{\mathbb{N}}$ (with the product topology), and $\Phi \circ T = \sigma \circ \Phi$, where $\sigma$ is the left shift.

*Proof sketch.* Injectivity: The parity of $n$ determines $n \bmod 2$. Each subsequent parity $\varepsilon_i$ determines one additional bit of $n \bmod 2^{i+1}$ (via the inverse branch: if $\varepsilon_i = 0$, apply $n \mapsto 2n$; if $\varepsilon_i = 1$, apply $n \mapsto (2n-1)/3$). So $\Phi(n) = \Phi(m)$ implies $n \equiv m \pmod{2^p}$ for all $p$, hence $n = m$.

Surjectivity: Given any sequence $\varepsilon \in \{0,1\}^{\mathbb{N}}$, the consistent residues $n \bmod 2^p$ form a nested sequence of nonempty cosets, whose intersection is a unique $n \in \mathbb{Z}_2$.

Continuity: Both $\Phi$ and $\Phi^{-1}$ are continuous (the first $p$ symbols of $\Phi(n)$ depend only on $n \bmod 2^p$).

Conjugacy: $\Phi(T(n))_i = T^{i+1}(n) \bmod 2 = \Phi(n)_{i+1} = \sigma(\Phi(n))_i$. $\square$

**Verified computationally** for all $n \bmod 2^p$ with $p \leq 8$.

### 2.2. Consequences

Since $T \cong \sigma$ (full one-sided shift on two symbols):
- **Topological entropy**: $h_{\text{top}}(T) = \log 2$.
- **Dense periodic orbits**: Periodic points of $T$ are dense in $\mathbb{Z}_2$.
- **Topological transitivity**: $T$ has a dense orbit in $\mathbb{Z}_2$.
- **Periodic orbit count**: $T$ has exactly $2^p$ fixed points of period dividing $p$ (one per binary string of length $p$).

The shift conjugacy is the cleanest possible statement: $T$ on $\mathbb{Z}_2$ has **maximal topological complexity**.

---

## 3. Periodic Orbits and the Cycle Formula

### 3.1. Classification

For a periodic parity pattern $\varepsilon = (\varepsilon_0, \ldots, \varepsilon_{p-1})$ with $k$ ones and $D = 2^p - 3^k > 0$, the unique periodic point is:

$$n(\varepsilon) = \frac{S(\varepsilon)}{D}, \qquad S(\varepsilon) = \sum_{j=0}^{k-1} 3^{k-1-j} \cdot 2^{i_{j+1}}$$

where $i_1 < i_2 < \cdots < i_k$ are the positions of the ones in $\varepsilon$.

This is a rational number with odd denominator $D$, hence $n(\varepsilon) \in \mathbb{Z}_2$ always. It is a positive integer if and only if:
1. $D \mid S(\varepsilon)$ (integrality), and
2. $S(\varepsilon)/D > 0$ (positivity — automatic since $S > 0$ and $D > 0$).

So **the cycle condition reduces to the single divisibility $D \mid S(\varepsilon)$**.

### 3.2. Self-Consistency is Automatic

A natural question: if we define $n(\varepsilon)$ by the formula above, does $n(\varepsilon)$ actually have parity sequence $\varepsilon$? **Yes, by construction**: $n(\varepsilon)$ is the unique element of $\mathbb{Z}_2$ with $\Phi(n(\varepsilon)) = \bar{\varepsilon}$ (the periodic extension of $\varepsilon$). The self-consistency equation "$\varepsilon(n) = \varepsilon$" is not an additional constraint — it is the definition of $n(\varepsilon)$.

**Verified computationally**: For all valid patterns with $p \leq 8$, the parity sequence of $n(\varepsilon) \bmod 2^p$ matches $\varepsilon$ exactly (100% consistency).

This means there is **no additional dynamical constraint** beyond the arithmetic condition $D \mid S(\varepsilon)$.

---

## 4. The 2-Adic Lyapunov Exponent

### 4.1. Correction of the Map Entry

The map.md entry for 6g-xi stated: "Lyapunov exponent: $\log_2(3^k/2^p) < 0$ → orbits ATTRACTING in $\mathbb{Z}_2$."

**This is wrong.** The quantity $\log_2(3^k/2^p) < 0$ is the *archimedean* (real) Lyapunov exponent, measuring behavior in $\mathbb{R}$. In the 2-adic metric:

$$\left|\frac{3^k}{2^p}\right|_2 = \frac{|3^k|_2}{|2^p|_2} = \frac{1}{2^{-p}} = 2^p$$

The **2-adic Lyapunov exponent** is $\lambda_2 = \log_2(2^p) = p > 0$.

### 4.2. Repulsion

Since $|dT^p/dn|_2 = 2^p > 1$, the fixed point $n(\varepsilon)$ is **repelling** in $\mathbb{Z}_2$:

$$|T^p(n) - n(\varepsilon)|_2 = 2^p \cdot |n - n(\varepsilon)|_2$$

for all $n$ in the same piece as $n(\varepsilon)$.

This means nearby 2-adic integers are pushed **away** from the cycle point. The "basin of repulsion" grows: a ball of radius $r$ around $n(\varepsilon)$ maps to a ball of radius $2^p \cdot r$.

### 4.3. The Archimedean Contrast

| Property | Archimedean ($\mathbb{R}$) | 2-Adic ($\mathbb{Z}_2$) |
|---|---|---|
| Slope of $T^p$ | $3^k/2^p < 1$ | $\|3^k/2^p\|_2 = 2^p$ |
| Lyapunov exponent | $k\log 3 - p\log 2 < 0$ | $p > 0$ |
| Fixed point behavior | Attracting | Repelling |
| Basin | Neighborhood in $\mathbb{R}$ | Empty (measure 0) |

The real and 2-adic behaviors are **opposite**: cycles attract in $\mathbb{R}$ but repel in $\mathbb{Z}_2$. This is a manifestation of the product formula: $|3^k/2^p|_\infty \cdot |3^k/2^p|_2 = (3^k/2^p) \cdot 2^p = 3^k$.

---

## 5. The 2-Adic Expansion of Cycle Points

### 5.1. Structure

For $n(\varepsilon) = S(\varepsilon)/D$ with $D$ odd, the 2-adic expansion of $n(\varepsilon)$ is:
- **Finite** (terminating) iff $D \mid S(\varepsilon)$, i.e., $n(\varepsilon) \in \mathbb{Z}_{\geq 0}$.
- **Eventually periodic** with period dividing $\operatorname{ord}_D(2)$ otherwise.

Here $\operatorname{ord}_D(2)$ is the multiplicative order of 2 modulo $D$.

### 5.2. Computational Results

| $(p,k)$ | $D$ | $\operatorname{ord}_D(2)$ | 2-adic period |
|---|---|---|---|
| $(5,3)$ | 5 | 4 | 4 |
| $(7,4)$ | 47 | 23 | 23 |
| $(8,5)$ | 13 | 12 | 12 |

For non-integer cycle points, the 2-adic expansion is eventually periodic with the predicted period. This means $n(\varepsilon)$ cycles through a fixed set of residues modulo $2^m$ as $m$ grows — it never "settles down" to a finite expansion (which would indicate integrality).

---

## 6. The Distance to Integrality

### 6.1. The 2-Adic Defect

For non-integer $n(\varepsilon) = S/D$, write $S = qD + r$ with $0 < r < D$. Then:

$$|n(\varepsilon) - q|_2 = |r/D|_2 = |r|_2 = 2^{-v_2(r)}$$

The quantity $v_2(S \bmod D)$ measures how 2-adically close $n(\varepsilon)$ is to the nearest integer.

### 6.2. Distribution

| $(p,k)$ | $D$ | $v_2 = 0$ | $v_2 = 1$ | $v_2 = 2$ | $v_2 = 3$ | $v_2 = \infty$ (integer) |
|---|---|---|---|---|---|---|
| $(5,3)$ | 5 | 60% | 10% | 30% | — | 0 |
| $(7,4)$ | 47 | 51% | 34% | 9% | 3% | 0 |
| $(8,5)$ | 13 | 50% | 27% | 18% | 5% | 0 |
| $(10,6)$ | 295 | 52% | 23% | 14% | 8% | 0 |

The distribution shows a roughly geometric decay: $\Pr[v_2 = m] \approx 2^{-m-1}$ for $m \geq 0$. This is consistent with $S \bmod D$ being "pseudo-random" modulo 2, with no special tendency toward $v_2 = \infty$ (exact divisibility).

---

## 7. Why p-Adic Dynamics Theorems Don't Apply

### 7.1. The Analytic vs Piecewise Obstruction

The deep theorems of non-archimedean dynamics — Fatou/Julia theory, no-wandering-domain (Benedetto), classification of periodic Fatou components (Rivera-Letelier) — require the map to be a **single analytic function** (power series, polynomial, or rational function) on $\mathbb{P}^1(\mathbb{C}_p)$.

The Collatz map $T$ is:
- Affine on each of the two clopen sets $2\mathbb{Z}_2$ and $1+2\mathbb{Z}_2$.
- **Not given by a single power series** on all of $\mathbb{Z}_2$.
- The "derivative" jumps: $|T'|_2 = 2^{-1}$ on even integers, $|T'|_2 = 2$ on odd integers.

Therefore, the entire framework of p-adic analytic dynamics is **inapplicable**.

### 7.2. What the Julia Set Would Be

On each piece of $T^p$ (one per valid parity pattern), the map is affine with $|dT^p/dn|_2 = 2^p > 1$. For an affine map $f(z) = az + b$ with $|a|_p > 1$, the "Julia set" is all of $\mathbb{C}_p$ (the map is uniformly expanding). So:

- There are **no Fatou components** on any piece.
- The no-wandering-domain theorem is **vacuously true**.
- The classification of periodic Fatou components is **empty**.

### 7.3. The Shift Captures Everything

The shift conjugacy $T \cong \sigma$ already provides the complete topological description of $T$ on $\mathbb{Z}_2$. Any theorem about the **topology** or **dynamics** of $T$ on $\mathbb{Z}_2$ is equivalent to a statement about the full shift, which is completely understood. The remaining question — which periodic orbits correspond to positive integers — is **arithmetic**, not dynamical.

---

## 8. The Archimedean/Non-Archimedean Mismatch

### 8.1. The Product Formula Perspective

For a rational number $n = S(\varepsilon)/D$, the product formula gives:

$$|n|_\infty \cdot \prod_{q \text{ prime}} |n|_q = 1$$

This relates the archimedean size to the product of all non-archimedean sizes. But this is just the fundamental theorem of arithmetic in disguise — it doesn't provide new constraints.

### 8.2. Why This is the Same Barrier

The question "is $n(\varepsilon) \in \mathbb{Z}_{>0}$?" decomposes as:

| Condition | Nature | Tool |
|---|---|---|
| $n(\varepsilon) \in \mathbb{Z}_2$ | 2-adic | Automatic ($D$ is odd) |
| $n(\varepsilon) \in \mathbb{Z}_q$ for all $q$ | $q$-adic | Requires $q \nmid D$ or $q \mid S$ |
| $n(\varepsilon) > 0$ | Archimedean | Size bounds |
| $D \mid S(\varepsilon)$ | All non-arch simultaneously | **The unsolved problem** |

The 2-adic dynamics approach handles the first row trivially and has nothing to say about the last row. The divisibility $D \mid S(\varepsilon)$ is simultaneously a condition at all primes dividing $D$ — it is the **global** (rational integer) question that no single completion can resolve.

### 8.3. Connection to Other Directions

| Direction | What it sees | What it misses |
|---|---|---|
| 0A (sieve/counting) | Archimedean: $C(p,k)/D \to 0$ | Non-arch: correlations between $q \mid S$ events |
| 0B (Arakelov) | Both via heights | Lattice membership is linear — heights too coarse |
| 0C (motivic) | Algebraic structure | Exponential functions $2^{i_j}$ are not algebraic |
| 6g-xi (2-adic) | Non-arch: shift conjugacy, repulsion | Archimedean: positivity, integrality |

All four directions illuminate different facets of the same obstacle: the Collatz cycle condition spans the archimedean/non-archimedean divide, and no existing framework works across this divide.

---

## 9. Positive Residue: What Does Work

Despite the overall failure, the 2-adic perspective provides genuine structural clarity:

**Insight 1: Clean separation.** The shift conjugacy completely solves the dynamical question ("classify all periodic orbits in $\mathbb{Z}_2$") and reduces the conjecture to a pure arithmetic question ("for which patterns does $D \mid S$?"). This is a genuine simplification.

**Insight 2: Isolation of cycles.** The 2-adic repulsion (factor $2^p$) means that if a positive integer cycle exists, it is an **isolated** point — there is no continuous family of nearby cycles. Each potential cycle is individually specified by its parity pattern.

**Insight 3: The defect distribution.** The roughly geometric decay of $\Pr[v_2(S \bmod D) = m]$ suggests that $S \bmod D$ behaves "pseudo-randomly" with respect to powers of 2. This is consistent with the heuristic that $D \mid S$ occurs with probability $\sim 1/D \sim 2^{-0.05p} \to 0$.

**Insight 4: Complementary completions.** The archimedean and 2-adic Lyapunov exponents are opposite in sign (attracting vs repelling). A proof strategy that could exploit this complementarity — using archimedean contraction together with 2-adic repulsion to bound the set of possible integer cycle points — would be genuinely novel. But no such strategy currently exists.

---

## 10. Computational Verification Summary

| Check | Result |
|---|---|
| Shift conjugacy $\Phi$ bijective mod $2^p$ | Verified for $p \leq 8$ |
| Shift conjugacy $\Phi \circ T = \sigma \circ \Phi$ | Verified for $p \leq 7$ (100% of residues) |
| Self-consistency of $n(\varepsilon)$ | 100% for $p \leq 8$ |
| 2-adic repulsion $\|T^p - n_0\|_2 = 2^p\|n - n_0\|_2$ | Verified for $(p,k) \in \{(5,3),(7,4),(8,5),(10,6)\}$ |
| 2-adic expansion period = $\operatorname{ord}_D(2)$ | Verified for $(5,3), (7,4), (8,5)$ |
| $v_2(S \bmod D)$ distribution | Geometric decay confirmed |
| Nontrivial positive integer cycles | 0 found (all tested cases) |

---

## 11. Final Assessment

### What 6g-xi is

A correct and illuminating reformulation of the Collatz cycle problem in the language of 2-adic dynamics. The shift conjugacy and repulsion are genuine mathematical facts that provide structural insight.

### What 6g-xi is not

A path to proving Part 1. The 2-adic topology is blind to the positivity/integrality condition that distinguishes the Collatz conjecture from the trivially true statement "periodic orbits exist in $\mathbb{Z}_2$." All tools from p-adic analytic dynamics (Fatou/Julia theory, no-wandering-domain) are inapplicable because $T$ is piecewise, not analytic.

### The deeper lesson

Direction 6g-xi represents the fourth instance of a recurring pattern in this project:

> **Every completion of $\mathbb{Q}$ sees part of the Collatz cycle condition, but no single completion sees all of it.**

The Collatz conjecture, at its core, is a statement about the intersection of $\mathbb{Z}_{>0}$ with a specific subset of $\mathbb{Z}_2$ (the preimage of periodic sequences under the coding map $\Phi$). Since $\mathbb{Z}_{>0}$ is simultaneously archimedean (bounded, positive) and non-archimedean (integer), any proof must work across completions.

### Status

**Direction 6g-xi: EXPLORED, FAILS as standalone approach. Core insights (shift conjugacy, repulsion, self-consistency automatic) are valid and recorded. No path to Part 1.**
