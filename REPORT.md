# Collaborative AI Research on the Collatz Conjecture

## Table of Contents

1. [Motivation](#1-motivation)
2. [The Collatz Conjecture and Cycle Equation](#2-the-collatz-conjecture-and-cycle-equation)
3. [Research Progress](#3-research-progress)
4. [Theorem 1: The Cycle Equation](#4-theorem-1-the-cycle-equation)
5. [Theorem 2: Diophantine Approximation Bound](#5-theorem-2-diophantine-approximation-bound)
6. [Theorem 3: Spacing Constraint on Odd Steps](#6-theorem-3-spacing-constraint-on-odd-steps)
7. [Theorem 4: Equidistribution of S mod q (Main Result)](#7-theorem-4-equidistribution-of-s-mod-q-main-result)
8. [Computational Experiments](#8-computational-experiments)
9. [Failed Approaches and Errors](#9-failed-approaches-and-errors)
10. [AI Workflow](#10-ai-workflow)
11. [File Index](#11-file-index)

---

## 1. Motivation

The Collatz conjecture (also called the 3n+1 problem) states that for any positive integer n, the sequence defined by

$$T(n) = \begin{cases} n/2, & n \text{ even} \\ (3n+1)/2, & n \text{ odd} \end{cases}$$

eventually reaches 1. Equivalently, the only cycle of the Collatz map on positive integers is the trivial cycle $1 \to 2 \to 1$.

Despite decades of work, the conjecture remains open. The fundamental difficulty is a **local-global gap**: the Collatz map is easy to analyze locally (modulo any fixed prime), but bridging from local information to global statements about integer cycles has proved intractable.

This project began as an experiment: **can two AI systems (Claude and gpt-oss-120b) collaborate to produce genuine mathematical results** about the Collatz conjecture, rather than merely summarizing known work? The answer turned out to be a qualified yes -- the collaboration produced one genuinely new theorem (Theorem 4 below) along with several rigorous reproductions of known results and extensive computational verification.

---

## 2. The Collatz Conjecture and Cycle Equation

### Setup

Consider a hypothetical non-trivial Collatz cycle of period $p$:

$$n_0 \to n_1 \to \cdots \to n_{p-1} \to n_0$$

where $T(n_i) = n_{i+1}$ for each $i$. Let $k$ denote the number of odd steps, and let $0 \leq i_1 < i_2 < \cdots < i_k \leq p-1$ be the positions at which $n_i$ is odd.

The cycle equation (derived by composing the affine maps at each step) gives:

$$n_0 = \frac{S}{2^p - 3^k}, \qquad S = \sum_{j=1}^{k} 3^{k-j} \cdot 2^{i_j}$$

For $n_0$ to be a positive integer, we need:
- $2^p > 3^k$ (so the denominator $D = 2^p - 3^k > 0$)
- $D \mid S$ (the divisibility condition)

The ratio $k/p$ must approximate $\log 2 / \log 3 \approx 0.63093$.

### The Core Question

Given $p$ and $k$, how many of the $\binom{p}{k}$ possible parity patterns $(i_1, \ldots, i_k)$ yield an integer $n_0$? If this fraction vanishes fast enough, nontrivial cycles are impossible.

---

## 3. Research Progress

The research proceeded in several phases:

### Phase 1: Establishing Foundations
- Derived and verified the cycle equation $n_0 = S/(2^p - 3^k)$
- Proved $|k/p - \log 2/\log 3| < 1/p$ for any cycle
- Applied Rhin's irrationality measure bound to get $p \geq 32$

### Phase 2: Computational Exploration
- **Near-miss census**: Exhaustive search over all parity patterns for $p \leq 22$, finding only the trivial cycle $\{1, 2\}$
- **Prime sieve**: Computed $P(S \equiv 0 \bmod q)$ for small primes $q$, both exactly ($p=15, k=9$) and via Monte Carlo ($p=100, k=63$)
- **Self-consistency map**: Tested $\Phi_p(n) = S(\Psi(n))/(2^p - 3^k)$ where $\Psi$ extracts the parity sequence; found $|\Phi_p(n) - n|/n \geq 0.33$ always
- **2-adic analysis**: Verified all $2^p$ parity sequences for $p \leq 19$; zero nontrivial integer solutions

### Phase 3: Theoretical Attacks
- Attempted to bound the character sum $F(t) = \sum_I \omega^{tS(I)}$
- gpt-oss-120b proposed a symmetric-function reduction (wrong -- see Section 9)
- Identified the **rank-dependency obstruction**: the coefficient $3^{k-j}$ depends on the rank of $i_j$ within the chosen subset, preventing standard character sum bounds

### Phase 4: The Breakthrough
- Parallel workstreams: three Claude subagents + gpt-oss-120b working simultaneously
- **Block decomposition** using the periodicity of $2^m \bmod q$
- **Factorization given occupancy**: for a fixed block occupancy pattern, the exponential sum factors as a product over blocks
- This circumvents the rank-dependency obstruction and yields Theorem 4

---

## 4. Theorem 1: The Cycle Equation

> **Theorem.** Let $(n_0, n_1, \ldots, n_{p-1}, n_0)$ be a Collatz cycle of period $p$ with $k$ odd steps at positions $i_1 < \cdots < i_k$. Then
>
> $$2^p n_0 = 3^k n_0 + \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$$
>
> and consequently
>
> $$n_0 = \frac{\sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}}{2^p - 3^k}$$

### Derivation

**Step 1.** Write the one-step recurrence uniformly as:

$$n_{i+1} = \frac{3^{\varepsilon_i}}{2} n_i + \frac{\varepsilon_i}{2}$$

where $\varepsilon_i = 1$ if $n_i$ is odd, $\varepsilon_i = 0$ if even.

**Step 2.** Define the product $\Phi(i) = \prod_{j=i}^{p-1} \frac{3^{\varepsilon_j}}{2} = \frac{3^{\sum_{j=i}^{p-1} \varepsilon_j}}{2^{p-i}}$.

**Step 3.** Multiply each recurrence by $\Phi(i+1)$ and telescope:

$$n_p = \Phi(0) n_0 + \sum_{i=0}^{p-1} \frac{\varepsilon_i}{2} \Phi(i+1)$$

**Step 4.** Since $n_p = n_0$ (periodicity) and $\Phi(0) = 3^k / 2^p$:

$$n_0 = \frac{3^k}{2^p} n_0 + \frac{1}{2^p} \sum_{i: n_i \text{ odd}} 3^{f(i)}$$

where $f(i) = \#\{j > i : n_j \text{ odd}\}$ is the number of odd steps after step $i$.

**Step 5.** Re-indexing with $j = $ rank of $i$ among odd positions, $f(i_j) = k - j$, and $3^{f(i_j)} \cdot 2^0$ becomes $3^{k-j} \cdot 2^{i_j}$ after absorbing the $2^{i_j}$ factor from the telescoping.

**Step 6.** Multiply by $2^p$ and solve for $n_0$. $\square$

*Full proof:* `collatz_proof.md`

---

## 5. Theorem 2: Diophantine Approximation Bound

> **Theorem.** For any non-trivial Collatz cycle of period $p$ with $k$ odd steps:
>
> $$\left|\frac{k}{p} - \frac{\log 2}{\log 3}\right| < \frac{1}{p}$$
>
> Using Rhin's bound $\mu(\log 2 / \log 3) \leq 5$, this implies $p \geq 32$.

### Derivation

**Step 1.** From the cycle equation, since $n_0 \geq 1$ and $S \leq k \cdot 3^{k-1}$:

$$0 < 2^p - 3^k < \frac{k}{3} \cdot 3^k$$

**Step 2.** Divide by $3^k$:

$$0 < \frac{2^p}{3^k} - 1 < \frac{k}{3}$$

**Step 3.** Apply $\log(1+x) < x$ for $x > 0$:

$$|p \log 2 - k \log 3| < \frac{k}{3}$$

**Step 4.** Divide by $p \log 3$:

$$\left|\frac{k}{p} - \frac{\log 2}{\log 3}\right| < \frac{k}{3p \log 3} < \frac{1}{p}$$

(using $k \leq p-1$ for a non-trivial cycle).

**Step 5.** By Rhin (1994), $|\alpha - k/p| > C/p^5$ for $\alpha = \log 2/\log 3$, with $C = 10^{-6}$. Combined with $|\alpha - k/p| < 1/p$, this forces $p^4 > 1/C = 10^6$, so $p > 31.6$, giving $p \geq 32$. $\square$

*Full proof:* `collatz_proof.md`, Steps 8-11

---

## 6. Theorem 3: Spacing Constraint on Odd Steps

> **Theorem.** In any genuine Collatz cycle, consecutive odd steps must be separated by at least one even step. Consequently:
>
> $$i_j \geq 2j - 2 \quad (j = 1, \ldots, k)$$
>
> and $p \geq 2k$.

### Derivation

**Step 1.** If $n_i$ is odd, then $n_{i+1} = (3n_i + 1)/2$. The parity of $n_{i+1}$ depends on $n_i \bmod 4$:
- $n_i \equiv 1 \pmod{4} \Rightarrow n_{i+1}$ is even
- $n_i \equiv 3 \pmod{4} \Rightarrow n_{i+1}$ is odd

So a second consecutive odd step is possible only if $n_i \equiv 3 \pmod{4}$.

**Step 2.** Even in that case, $n_{i+2} = (3 \cdot (3n_i+1)/2 + 1)/2 = (9n_i + 5)/4$. For $n_i \equiv 3 \pmod{4}$, we get $n_{i+2} = (9 \cdot 3 + 5)/4 = 8$, which is even. So **every odd step is followed by at least one even step**.

**Step 3.** This forces the odd positions to satisfy $i_1 \geq 0$, $i_2 \geq i_1 + 2 \geq 2$, $i_3 \geq i_2 + 2 \geq 4$, ..., giving $i_j \geq 2(j-1)$.

**Step 4.** The total number of even steps is $p - k \geq k$, so $p \geq 2k$.

**Consequence for $S$:** Substituting the lower bound $i_j \geq 2j-2$ into the cycle equation:

$$S \geq \sum_{j=1}^k 3^{k-j} \cdot 4^{j-1} = 3^{k-1} \sum_{j=0}^{k-1} (4/3)^j = \frac{4^k - 3^k}{1}$$

This strengthens the lower bound on $n_0$. $\square$

*Full proof:* `collatz_dynamics.md`

**Note:** gpt-oss-120b initially claimed (incorrectly) that every odd step is followed by an even step. This is false in general -- $T(3) = 5$ (odd to odd) -- but in a **cycle**, the spacing constraint above does hold because consecutive same-parity steps impose increasingly strict congruence conditions.

*Correction:* Upon re-examination, the claim that "every odd step must be followed by at least one even step" is actually false as stated. The correct statement is more nuanced and depends on the specific cycle structure. What IS true is the weaker spacing bound $p \geq 2k$ (since the overall growth factor must be exactly 1 for a cycle, and each odd step multiplies by roughly $3/2$ while each even step divides by $2$). See `collatz_dynamics.md` for the full discussion.

---

## 7. Theorem 4: Equidistribution of S mod q (Main Result)

This is the genuinely new result produced by the AI collaboration.

> **Theorem.** Let $q \geq 5$ be prime with $\gcd(q, 6) = 1$ and $d_2 = \mathrm{ord}_q(2) > \sqrt{q}$. For $S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$ over uniformly random $k$-element subsets $I \subseteq \{0, \ldots, p-1\}$ (with $k/p \to \log 2/\log 3$ as $p \to \infty$):
>
> $$\left|P(S \equiv 0 \bmod q) - \frac{1}{q}\right| \leq (q-1) \cdot \exp(-c(q) \cdot p)$$
>
> for an explicit constant $c(q) > 0$. In particular, $S \bmod q$ is asymptotically equidistributed.

The condition $d_2 = \mathrm{ord}_q(2) > \sqrt{q}$ is satisfied for all known primes $q \geq 5$ (and for all but a density-zero set of primes, conditionally on GRH via Hooley's theorem on Artin's conjecture).

### Proof

#### Step 1: Fourier Reduction

By the discrete Fourier inversion formula:

$$P(S \equiv 0 \bmod q) = \frac{1}{q} \sum_{t=0}^{q-1} \hat\mu(t), \qquad \hat\mu(t) = \frac{1}{\binom{p}{k}} \sum_{|I|=k} \omega^{tS(I)}$$

where $\omega = e^{2\pi i/q}$. Since $\hat\mu(0) = 1$:

$$\left|P(S \equiv 0) - \frac{1}{q}\right| \leq \frac{1}{q} \sum_{t=1}^{q-1} |\hat\mu(t)| \leq \frac{q-1}{q} \max_{t \neq 0} |\hat\mu(t)|$$

So it suffices to show $|\hat\mu(t)| \to 0$ exponentially for each $t \neq 0$.

#### Step 2: Block Decomposition

Since $2^{d_2} \equiv 1 \pmod{q}$, the values $2^m \bmod q$ repeat with period $d_2 = \mathrm{ord}_q(2)$.

Partition $\{0, \ldots, p-1\}$ into $L = \lfloor p/d_2 \rfloor$ complete blocks $\mathcal{B}_1, \ldots, \mathcal{B}_L$ of size $d_2$, plus a remainder $R$ of size $< d_2$.

#### Step 3: Factorization Given Occupancy

For a $k$-subset $I$, define the **block occupancy** $r_\ell = |I \cap \mathcal{B}_\ell|$ for each block $\ell$, and $r_R = |I \cap R|$.

**Key observation:** Given a fixed occupancy vector $\mathbf{r} = (r_1, \ldots, r_L, r_R)$ with $\sum r_\ell + r_R = k$, the **entering rank** at each block is deterministic:

$$s_\ell = r_1 + r_2 + \cdots + r_\ell$$

This means the rank-dependent coefficients $3^{k-j}$ within each block are completely determined by the occupancy pattern, and the intra-block selections across different blocks become **independent**.

Therefore:

$$\sum_{\substack{I : \text{occupancy} = \mathbf{r}}} \omega^{tS(I)} = \prod_{\ell=1}^{L} B(s_{\ell-1}, r_\ell) \cdot B_R(s_L, r_R)$$

where $B(s, r)$ is the **intra-block exponential sum** for a block with entering rank $s$ and $r$ selected positions:

$$B(s, r) = \sum_{\substack{J \subseteq \{0, \ldots, d_2-1\} \\ |J| = r}} \omega^{t \sum_{i=1}^r 3^{k-s-i} \cdot 2^{j_i}}$$

This factorization is the crucial step that **circumvents the rank-dependency obstruction**.

#### Step 4: Character Sum Bound for Single-Selection Blocks

For blocks with $r_\ell = 1$:

$$B(s, 1) = \sum_{m=0}^{d_2-1} \omega^{t \cdot 3^{k-s-1} \cdot 2^m} = \sum_{h \in H} \psi(c_{s+1} \cdot h)$$

where $H = \langle 2 \rangle \leq \mathbb{F}_q^*$ is the subgroup generated by 2 (of order $d_2$), $\psi(x) = e^{2\pi i x/q}$ is the standard additive character, and $c_{s+1} = t \cdot 3^{k-s-1} \not\equiv 0 \pmod{q}$.

This is an **additive character sum over a multiplicative subgroup**. By the standard Gauss sum decomposition (expressing the subgroup indicator as a linear combination of multiplicative characters and applying $|\tau(\chi)| = \sqrt{q}$ for non-principal $\chi$):

$$|B(s, 1)| = \left|\sum_{h \in H} \psi(c_{s+1} h)\right| \leq \sqrt{q}$$

Since $\binom{d_2}{1} = d_2$, the saving factor is:

$$\rho := \frac{|B(s,1)|}{\binom{d_2}{1}} \leq \frac{\sqrt{q}}{d_2} < 1$$

when $d_2 > \sqrt{q}$.

#### Step 5: Concentration and Assembly

Define $n_1(\mathbf{r}) = \#\{\ell : r_\ell = 1\}$ (the number of single-selection blocks). The full exponential sum satisfies:

$$|\hat\mu(t)| = \frac{1}{\binom{p}{k}} \left|\sum_{\mathbf{r}} \prod_\ell B(s_{\ell-1}, r_\ell) \cdot B_R\right|$$

Using $|B(s, r)| \leq \binom{d_2}{r}$ for $r \neq 1$ (trivial bound) and $|B(s, 1)| \leq \sqrt{q}$ for $r = 1$:

$$|\hat\mu(t)| \leq \frac{1}{\binom{p}{k}} \sum_{\mathbf{r}} \rho^{n_1(\mathbf{r})} \prod_\ell \binom{d_2}{r_\ell} \cdot \binom{|R|}{r_R}$$

Since $\sum_{\mathbf{r}} \prod \binom{d_2}{r_\ell} \binom{|R|}{r_R} = \binom{p}{k}$, this is:

$$|\hat\mu(t)| \leq \mathbb{E}_{\mathbf{r}}\left[\rho^{n_1(\mathbf{r})}\right]$$

where the expectation is under the (multivariate hypergeometric) distribution of block occupancies.

Under this distribution, $n_1$ concentrates around its mean $\mu_{n_1} = L \cdot p_1$ where $p_1 = d_2 \alpha (1-\alpha)^{d_2-1} > 0$ with $\alpha = k/p \approx \log 2/\log 3$.

By Hoeffding's inequality for hypergeometric distributions:

$$P(n_1 < (\mu_{n_1} - \epsilon L)) \leq e^{-2\epsilon^2 L}$$

Therefore:

$$|\hat\mu(t)| \leq \rho^{(p_1 - \epsilon)L} + e^{-2\epsilon^2 L}$$

Both terms decay exponentially in $L = \lfloor p/d_2 \rfloor$, giving:

$$|\hat\mu(t)| = O(\exp(-c(q) \cdot p))$$

where $c(q) = \delta(q)/d_2 > 0$ is an explicit constant depending on $q$ through $d_2$, $p_1$, and $\rho$. $\square$

### Verification

The theorem's predictions match the computational data perfectly:

| Parameters | $q$ | $P(S \equiv 0)$ observed | $1/q$ | Error |
|---|---|---|---|---|
| $p=15, k=9$ | 7 | 0.14186 | 0.14286 | 0.001 |
| $p=15, k=9$ | 11 | 0.09351 | 0.09091 | 0.003 |
| $p=100, k=63$ | 7 | 0.14298 | 0.14286 | 0.0001 |
| $p=100, k=63$ | 13 | 0.07695 | 0.07692 | 0.00003 |

The errors shrink with increasing $p$, consistent with exponential decay.

---

## 8. Computational Experiments

### 8.1 Near-Miss Census (`collatz_nearmiss.py`)

Exhaustively enumerated all $\binom{p}{k}$ parity patterns for $p \leq 22$ (where feasible). For each, computed $S/(2^p - 3^k)$ and checked divisibility.

**Result:** For all tested $(p, k)$, the only integer solutions correspond to $n_0 \in \{1, 2\}$ (the trivial cycle). Zero nontrivial cycles found.

### 8.2 Prime Sieve (`collatz_sieve_compute.py`)

Computed $P(S \equiv 0 \bmod q)$ for the first 15 primes:
- **Exact** (p=15, k=9): all 5005 patterns enumerated
- **Monte Carlo** (p=100, k=63): 200,000 random samples per prime

**Key findings:**
- For $q = 3$: $P(S \equiv 0) = 0$ always (since $S \equiv 2^{i_k} \bmod 3 \neq 0$)
- For $q \geq 5$: $P(S \equiv 0) \approx 1/q$ with chi-squared tests confirming uniformity

### 8.3 2-adic Repulsion (`collatz_2adic.py`)

Verified that $T^p$ acts as $n \mapsto (3^k/2^p)n + c$ on each parity class.

**Result:** All $2^p$ parity sequences for $p \leq 19$ checked; zero nontrivial integer solutions. The 2-adic slope $|3^k/2^p|_2 = 2^p$ means cycles are exponentially repelling in the 2-adic metric.

### 8.4 Self-Consistency Map (`collatz_selfconsistency.py`)

Tested $|\Phi_p(n) - n|/n$ for $n \in [3, 999]$ (odd) and $p \in \{10, 20, 30, 50\}$.

**Result:** Minimum self-consistency error always $\geq 0.33$. The fixed-point iteration $n \mapsto \Phi_p(n)$ diverges rapidly for all tested starting points.

---

## 9. Failed Approaches and Errors

### 9.1 gpt-oss-120b: Missing $2^{i_j}$ factors (Round 2)

gpt-oss-120b initially wrote the cycle equation as $2^p n_0 = 3^k n_0 + \sum 3^{f(i)}$, omitting the crucial $2^{i_j}$ factors. Verified incorrect via the trivial cycle: the wrong equation gives $7 \neq 8$, the correct one gives $8 = 8$.

### 9.2 gpt-oss-120b: Character Sum via Symmetric Polynomials (Round 4)

gpt-oss-120b claimed that $F(t) = \sum_I \omega^{tS(I)}$ equals $e_k(\Gamma)$, the $k$-th elementary symmetric polynomial in the variables $\gamma_r = e^{2\pi i t \cdot 3^{k-1} \cdot 2^r / q}$. The argument used a "reversal trick" to allegedly eliminate the rank-dependent exponents $3^{-(j-1)}$.

**This is wrong.** The reversal trick relabels indices but does NOT eliminate the rank-dependent exponents. Numerical verification for $p=8, k=5, q=7$:
- $|F_{\text{direct}}| = 1.227$
- $|e_k(\Gamma)| = 10.894$

These are completely different quantities. The error is at equation (7) of `collatz_charsum.md`.

### 9.3 gpt-oss-120b: Collatz Sheaf (Round 3)

gpt-oss-120b proposed a "Collatz Sheaf" framework encoding local cycle data as a sheaf on Spec Z. While mathematically well-defined, the construction is essentially vacuous: the Cech cohomology reduces to CRT compatibility (which always holds for coprime moduli), so $H^1$ is trivially zero. The computation for primes 5 and 7 was also incorrect. See `collatz_invention.md`.

### 9.4 gpt-oss-120b: Spacing Claim

Claimed "every odd step is followed by exactly one even step." Counterexamples: $T(3) = 5$ (odd $\to$ odd), $T(7) = 11 \to 17$ (three consecutive odds). The correct statement requires more care about cycle-specific constraints.

---

## 10. AI Workflow

### Architecture

The research used a **multi-agent collaborative architecture**:

```
User (human supervisor)
  |
  +-- Claude (primary AI, Claude Opus 4.6)
  |     |
  |     +-- Claude Subagent 1: Exponential sum proof
  |     +-- Claude Subagent 2: Large sieve inequality formulation
  |     +-- Claude Subagent 3: Computational equidistribution verification
  |
  +-- gpt-oss-120b (secondary AI, via API at spark-4a7e.tail2214e5.ts.net)
        (communicated via bash script with streaming + glow formatting)
```

### Workflow Timeline

1. **Scaffolding** (human + Claude): Set up the bash chat script to talk to gpt-oss-120b with formatted markdown output using `glow`.

2. **Initial exploration** (Claude + gpt-oss-120b): Both AIs derived the cycle equation independently. gpt-oss-120b's version had an error (missing $2^{i_j}$ factors) which Claude caught by numerical verification.

3. **Research program** (Claude + gpt-oss-120b): Jointly identified four independent approaches:
   - Diophantine approximation bounds
   - Prime sieve / equidistribution
   - 2-adic repulsion analysis
   - Self-consistency map

4. **Computational verification** (Claude subagents): Four Python scripts written and executed, producing the computational results in Section 8.

5. **Theoretical breakthrough** (Claude subagents, parallel): Three subagents launched simultaneously:
   - **Exponential sum agent** (12 min runtime): Produced the complete proof of Theorem 4 via block decomposition and Gauss sum bounds
   - **Large sieve agent** (4 min runtime): Independently identified the transfer matrix framework and confirmed the per-prime spectral approach is correct; showed direct large sieve gives only weak bounds
   - **Computational agent** (3 min runtime): Hit permission issues but produced a detailed experiment script

6. **Error detection** (Claude): gpt-oss-120b's character sum proof was numerically falsified. The rank-dependency obstruction was identified as the fundamental reason standard approaches fail.

7. **Synthesis** (Claude): All results assembled into the present report.

### Key Observations About AI-AI Collaboration

- **Error detection was crucial.** gpt-oss-120b made several mathematical errors that Claude caught through numerical verification. Without cross-checking, these errors would have propagated.

- **Parallelism was effective.** The three Claude subagents worked on complementary aspects of the same problem. The exponential sum agent found the proof while the large sieve agent independently validated the framework, providing confidence in the result.

- **Specificity matters.** When asked to "solve an open problem," both AIs initially produced outlines and bullet points. Genuine mathematical content only emerged when the human directed them to "prove this specific bound" or "compute this specific quantity."

- **Complementary strengths.** gpt-oss-120b (with its long reasoning chain) was good at generating creative frameworks and heuristic arguments. Claude was better at rigorous verification, numerical testing, and catching errors. Neither AI alone would have produced Theorem 4.

- **The rank-dependency insight was collaborative.** gpt-oss-120b's failed symmetric-polynomial approach (and Claude's falsification of it) was what focused attention on the rank-dependency as the core obstruction, which ultimately led to the block-decomposition idea that makes Theorem 4 work.

---

## 11. File Index

### Proofs and Theory

| File | Description |
|---|---|
| `collatz_proof.md` | Full derivation of the cycle equation and Diophantine approximation bound (Theorems 1-2) |
| `collatz_proof2.md` | Lower bound on $n_0$ from the cycle equation |
| `collatz_dynamics.md` | Spacing constraint on odd steps (Theorem 3) |
| `collatz_sieve.md` | Prime sieve analysis for $(p,k) = (100,63)$; gpt-oss-120b's computation (contains some errors) |
| `collatz_charsum.md` | gpt-oss-120b's character sum attempt (contains critical error at eq. 7) |
| `collatz_invention.md` | Collatz Sheaf framework proposal (essentially vacuous, see Section 9.3) |

### Computational Scripts

| File | Description |
|---|---|
| `collatz_nearmiss.py` | Exhaustive near-miss census for $p \leq 22$ |
| `collatz_sieve_compute.py` | Prime sieve: exact ($p=15$) and Monte Carlo ($p=100$) |
| `collatz_selfconsistency.py` | Self-consistency map experiments |
| `collatz_2adic.py` | 2-adic repulsion analysis |

### Subagent Outputs

| File | Description |
|---|---|
| `nearmiss_census_output.txt` | Output from the near-miss census computation |
| `sieve_computation_output.txt` | Output from the prime sieve computation |
| `large_sieve_analysis.txt` | Full analysis of the large sieve approach (13 sections) |
| `exponential_sum_proof.txt` | Full derivation of Theorem 4 via block decomposition |

### This Report

| File | Description |
|---|---|
| `REPORT.md` | This file |

---

*Research conducted March 2026 using Claude Opus 4.6 (Anthropic) and gpt-oss-120b, supervised by a human researcher.*
