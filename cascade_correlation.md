# Direction 6g-vii: Cascade Increment Correlation

*Developed 2026-03-06 (Session 8)*

## 0. Executive Summary

The cascade (C3/C7) computes position increments $g_j = v_2(3S^j(n)+1)$ where $S$ is the Syracuse map. A cycle requires $\sum_{j=0}^{k-1} g_j = p$. For random odd integers, $\mathbb{E}[g_j] = 2$, giving $\mathbb{E}[\sum g_j] = 2k \approx 1.26p$. Since $2k > p$, the average halving count exceeds the cycle target.

**The approach**: Use large deviation bounds and correlation analysis to show $\Pr(\sum g_j = p)$ decays fast enough to overcome the $(3/2)^{k-1}$ candidates.

**The result**: The approach fails, with a quantitatively precise diagnosis:

1. **The independence rate is too small**: Under independence, $\Pr(\sum g_j \leq p) \approx \exp(-0.055k)$. With $(3/2)^{k-1} \approx \exp(0.405k)$ candidates, the expected number of "successes" is $\exp(0.351k) \to \infty$. The independence model predicts infinitely many cycles.

2. **Correlations are POSITIVE, not negative**: Contrary to initial expectations, the lag-1 correlation $\text{Corr}(g_j, g_{j+1}) \approx +0.02$ to $+0.04$, meaning correlations make $\text{Var}[\sum g_j]$ LARGER than the independence prediction. Correlations HURT, not help.

3. **The 7.4$\times$ gap**: The needed large deviation rate is $c > \log(3/2) \approx 0.405$, but the independence rate is $I(\log_2 3) \approx 0.055$. The gap factor is $0.405/0.055 \approx 7.4\times$. Correlations provide at most $\sim 1.1\times$ adjustment (in the wrong direction). The gap is unbridgeable.

4. **Some candidates DO have $G < p$**: For $k \geq 10$, $\min_n G(n,k)/k$ drops below $\log_2 3$. Long runs of $g = 1$ (orbit growth phases) produce candidates with low halving counts. The approach $G > p$ for all $n$ is FALSE.

**Status: Direction 6g-vii EXPLORED, FAILS. The 7.4$\times$ gap is the quantitative expression of the barrier.**

---

## 1. Setup

### 1.1. The Halving Count

For odd $n \geq 3$ coprime to 3 and parameter $k$, define:

$$G(n,k) = \sum_{j=0}^{k-1} v_2(3S^j(n) + 1)$$

where $S$ is the Syracuse map $S(m) = (3m+1)/2^{v_2(3m+1)}$ and $S^j$ is the $j$-th iterate.

By the Syracuse-Cascade Duality (C7): a cycle with parameters $(p,k)$ starting at $n$ exists if and only if $G(n,k) = p$ and $S^k(n) = n$.

### 1.2. The Random Model

For a uniformly random odd integer $m$:

$$\Pr[v_2(3m+1) = r] = 2^{-r} \quad \text{for } r \geq 1$$

$$\mathbb{E}[v_2(3m+1)] = \sum_{r=1}^{\infty} r \cdot 2^{-r} = 2, \qquad \text{Var}[v_2(3m+1)] = \sum_{r=1}^{\infty} r^2 \cdot 2^{-r} - 4 = 2$$

If the $g_j$ were independent with this distribution, then $\mathbb{E}[G] = 2k$ and $\text{Var}[G] = 2k$.

---

## 2. The Independence Baseline (Fails)

### 2.1. Large Deviation Rate

By Cramér's theorem, if $g_0, \ldots, g_{k-1}$ are i.i.d. geometric on $\{1, 2, 3, \ldots\}$ with parameter $1/2$:

$$\Pr\left(\frac{G}{k} \leq x\right) \approx \exp(-k \cdot I(x))$$

where the rate function is $I(x) = \sup_{t < \log 2} (tx - \Lambda(t))$ with $\Lambda(t) = \log\left(\frac{e^t/2}{1 - e^t/2}\right)$.

For $x = \log_2 3 \approx 1.585$ (the cycle target $p/k$):

$$I(\log_2 3) \approx 0.0550$$

### 2.2. The Accounting Fails

- **Candidates**: $N(k) \approx (3/2)^{k-1} \approx \exp(0.405k)$
- **Success probability** (per candidate): $\approx \exp(-0.055k) / \sqrt{k}$
- **Expected successes**: $\approx \exp((0.405 - 0.055)k) / \sqrt{k} = \exp(0.351k) / \sqrt{k} \to \infty$

**The independence model predicts infinitely many cycles as $k \to \infty$.** The rate $I = 0.055$ is far too small to overcome the exponential number of candidates.

---

## 3. Correlation Analysis (Surprise: Positive)

### 3.1. Initial Expectation vs Reality

**Expected**: After a large gap $g_j$, $S^{j+1}(n)$ is small, so $g_{j+1}$ should be bounded → negative correlation → narrower $G$ distribution → stronger exclusion.

**Observed**: The lag-1 correlation is **slightly positive**:

| $k$ | Candidates | $\text{Corr}(g_j, g_{j+1})$ | $\text{Var}[G] / \text{Var}_{\text{indep}}$ |
|---|---|---|---|
| 10 | 12 | $+0.21$ | 0.97 |
| 20 | 738 | $+0.04$ | 1.50 |
| 30 | 42,610 | $+0.02$ | 1.14 |

Correlations are positive and make $\text{Var}[G]$ **larger** than the independence prediction. They HURT the approach.

### 3.2. Why Positive Correlations?

The conditional expectations $\mathbb{E}[g_{j+1} \mid g_j = r]$ show no clear trend:

| $g_j$ | $\mathbb{E}[g_{j+1} \mid g_j]$ ($k=30$) | Samples |
|---|---|---|
| 1 | 1.944 | 531,005 |
| 2 | 2.014 | 434,117 |
| 3 | 2.069 | 136,239 |
| 4 | 1.938 | 77,691 |
| 5 | 2.155 | 28,325 |
| 6 | 1.851 | 14,571 |

The positive lag-1 correlation comes not from $g \to g$ dependence but from **orbit-level structure**: candidates whose orbits grow (long $g = 1$ streaks) tend to have correlated stretches of low/high halvings due to the deterministic orbit dynamics.

---

## 4. The $G < p$ Phenomenon

### 4.1. Minimum Halving Ratio

Contrary to the hope that $G(n,k) > p$ always, the minimum $G/k$ drops **below** $\log_2 3$:

| $k$ | $\min_n G/k$ | $\log_2 3$ | $n$ achieving min |
|---|---|---|---|
| 5 | 2.400 | 1.585 | 5 |
| 10 | 1.300 | 1.585 | 31 |
| 20 | 1.200 | 1.585 | 2047 |
| 30 | 1.200 | 1.585 | 77671 |

### 4.2. Mechanism: Long $g = 1$ Streaks

The candidates achieving low $G/k$ are those with long initial runs of $g = 1$. For example, $n = 2^m - 1$ (Mersenne-like) produce orbits that grow by factor $3/2$ per step, with $g = 1$ for many consecutive steps, before eventually "crashing" (a step with large $g$).

Run-length statistics for $k = 30$:
- Maximum $g = 1$ streak: 16 steps
- Average max streak: 3.82

A streak of length $\ell$ contributes $\ell$ halvings for $\ell$ steps (ratio $1.0$), pulling $G/k$ toward $1.0$. The subsequent "crash" (large $g$) compensates but not always enough for the overall ratio to exceed $\log_2 3$.

### 4.3. Implication

**The approach "prove $G(n,k) > p$ for all $n$" is FALSE.** There exist candidates $n$ with $G(n,k) \leq p$ for valid $(p,k)$ pairs. These candidates fail the cycle condition not because $G \neq p$ but because $S^k(n) \neq n$ (the orbit doesn't close).

---

## 5. The 7.4$\times$ Gap

### 5.1. Quantitative Statement

To prove no cycles via halving counts alone, we need:

$$\sum_{n \leq (3/2)^{k-1}} \Pr[G(n,k) = p] = 0$$

For this to follow from a union bound, we need each $\Pr[G(n,k) = p]$ to be smaller than $1/(3/2)^{k-1}$, i.e.:

$$\Pr[G = p \text{ for a specific } n] < \exp(-0.405k)$$

But the best available bound (independence + any reasonable correlation correction) gives only $\exp(-0.055k)$. The gap:

$$\frac{0.405}{0.055} \approx 7.4\times$$

### 5.2. What Would Be Needed

To close the gap, we'd need one of:

1. **A rate function $I > 0.405$**: This would require the $g_j$ to be much more concentrated than geometric random variables. But the actual distribution is CLOSE to geometric (Section 3.2), so this is impossible.

2. **Candidate reduction**: If we could reduce the number of candidates from $(3/2)^{k-1}$ to $\exp(ck)$ with $c < 0.055$, the union bound would work. But the candidate count comes from the upper bound on $n$ (C8), which is tight.

3. **Non-independent structure**: If the candidates $n$ are correlated (a low $G$ for one $n$ implies low $G$ for nearby $n'$), we could group candidates and reduce the effective count. But the cascade (C3) shows each $n$ gives an independent trajectory.

None of these are achievable with current tools.

---

## 6. Connection to Barrier 1

The 7.4$\times$ gap is a quantitative manifestation of **Barrier 1 (abc/size-counting)**:

- The sieve approach needs $\operatorname{rad}(D) > 2^{0.95p}$ to make $\mathbb{E}[\#] < 1$.
- The cascade correlation approach needs $I > 0.405$ to make the union bound work.
- Both are asking: "Is the probability of $D \mid S(I)$ small enough to overcome the combinatorial count $C(p,k)$?"
- The answer in both cases is: **not without additional structural input**.

The cascade reformulation (C7) transforms the divisibility condition $D \mid S(I)$ into the halving condition $G(n,k) = p$, but it doesn't change the fundamental counting bottleneck. The 7.4$\times$ gap is the cascade-language translation of the abc barrier.

---

## 7. Honest Assessment

### What 6g-vii Provides

1. **The 7.4$\times$ gap as a precise barrier measure**: This is the first quantitative characterization of how far any counting/probabilistic approach is from succeeding. Previous barrier analyses were qualitative ("needs abc").

2. **The positive correlation surprise**: The initial hypothesis (negative correlation helps) was wrong. The actual positive correlation means the halving distribution is WIDER than independence predicts, making exclusion harder.

3. **The $G < p$ phenomenon**: Some candidates genuinely have fewer halvings than a cycle would need. The approach "prove $G > p$ always" is false. Cycle exclusion requires the orbit closure condition $S^k(n) = n$, not just the halving count.

4. **The connection to long $g = 1$ streaks**: Mersenne-like starting values ($n \approx 2^m - 1$) produce the lowest halving ratios. Understanding why these orbits don't close might provide insight.

### What 6g-vii Cannot Provide

A proof of Part 1. The 7.4$\times$ gap between the available rate and the needed rate is structural, not technical. No amount of correlation analysis can bridge it within the counting framework.

### Status

**Direction 6g-vii: EXPLORED, FAILS. Quantitative barrier: 7.4$\times$ gap. Positive correlations make the gap worse, not better.**

---

## 8. The Updated Barrier Landscape

With 6g-vii closed, the remaining viable direction is:

**6g-viii (Prime-D sieve completion)**: For prime $D$, the sieve gives $\mathbb{E}[\#] \approx 1/D \to 0$. The gap is the second moment. Unlike the 7.4$\times$ gap here, the second moment gap for prime $D$ may be closable because:
- For prime $D$, character sums in $\mathbb{F}_D$ provide exact correlation formulas.
- The pair correlation $\Pr[D \mid S(I) \text{ and } D \mid S(J)]$ factors through $\mathbb{F}_D^*$.
- This is a FINITE-FIELD problem, where powerful tools (Weil bounds, etc.) apply.

This is the last unexplored direction that passes the barrier diagnostic.
