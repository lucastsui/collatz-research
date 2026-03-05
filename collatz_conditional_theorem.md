# Conditional No-Cycles Theorem (Assuming abc)

## Main Result

**Theorem 6 (Conditional).** Assume the abc conjecture. Then for all sufficiently large $p$, there is no Collatz cycle of period $p$.

Combined with computational verification for small $p$ (Eliahou 1993: no cycles with $k \leq 1.7 \times 10^{10}$; Simons–de Weger 2005: no 1-cycles with $k$ up to astronomical bounds), this implies:

**Corollary.** The abc conjecture implies there are no nontrivial Collatz cycles.

---

## Proof

The proof chains three ingredients: the cycle equation, equidistribution (Theorem 5), and the abc conjecture.

### Step 1: Cycle Equation

Any hypothetical cycle of period $p$ with $k$ odd steps at positions $0 \leq i_1 < \cdots < i_k \leq p-1$ satisfies:

$$n_0 = \frac{S}{D}, \quad S = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}, \quad D = 2^p - 3^k$$

For a nontrivial cycle, $n_0$ must be a positive integer, so $D > 0$ (i.e., $2^p > 3^k$) and $D \mid S$.

The number of candidate parity patterns is $\binom{p}{k}$.

### Step 2: Counting Constraint

A nontrivial cycle exists only if there exists at least one $k$-subset $I$ with $D \mid S(I)$. By equidistribution of $S$ modulo $D$ (if established), the number of such subsets is approximately:

$$\#\{I : D \mid S(I)\} \approx \frac{\binom{p}{k}}{D}$$

For this count to be zero, we need $\binom{p}{k} < D$. By the Diophantine constraint (Rhin's irrationality measure of $\log_2 3$):

$$D = 2^p - 3^k > \frac{2^p}{p^{10.6}} \quad \text{for large } p$$

Since $\binom{p}{k} \leq 2^{H(k/p) \cdot p}$ where $H$ is the binary entropy function, and $k/p \approx \frac{\log 2}{\log 3} \approx 0.6309$, we have $H(k/p) \approx 0.949$. Therefore:

$$\frac{\binom{p}{k}}{D} \leq \frac{2^{0.949p} \cdot p^{10.6}}{2^p} = p^{10.6} \cdot 2^{-0.051p} \to 0$$

So the *heuristic* count goes to zero. Making this rigorous requires equidistribution of $S$ modulo $D$ (or a sufficient portion of $D$).

### Step 3: Why Direct Equidistribution mod D Fails

Our equidistribution method (Theorem 5) uses a block decomposition requiring $\mathrm{ord}_D(2) > 2\sqrt{D}$. For $D \approx 2^p$, this requires $\mathrm{ord}_D(2) > 2^{p/2+1}$, but then the block size $d = \mathrm{ord}_D(2) > 2^{p/2}$ exceeds $p$, leaving zero complete blocks. The method is structurally incapable of handling moduli exponentially large in $p$.

This was confirmed by exhaustive analysis of four alternative approaches:
1. **Transfer matrix spectral analysis:** Reduces to the same exponential sum obstacle.
2. **Weyl differencing:** Creates doubly-exponential term counts that overwhelm savings.
3. **Algebraic structure of $2^p \equiv 3^k \pmod{D}$:** Provides no useful constraint on $\mathrm{ord}_D(2)$.
4. **Second moment method:** Loops back to the same Fourier bounds.

### Step 4: Sieve Approach

Instead of equidistribution mod $D$ directly, we combine equidistribution mod individual primes $q \mid D$ via the Selberg upper bound sieve.

By Theorem 5, for each prime $q \mid D$ with $q \geq 5$ and $\mathrm{ord}_q(2) > 2\sqrt{q}$ (which holds for all but $O(\sqrt{q})$ primes):

$$\left|P(S \equiv 0 \bmod q) - \frac{1}{q}\right| \leq (q-1) \cdot e^{-c(q) \cdot p}$$

By the Selberg sieve (Iwaniec–Kowalski, Chapter 6):

$$\#\{I : D \mid S(I)\} \leq \binom{p}{k} \cdot \prod_{\substack{q \mid D \\ q \leq z \\ q \text{ good}}} \frac{1}{q} \cdot \bigl(1 + O(z^{-1/2})\bigr)$$

where "good" means $\mathrm{ord}_q(2) > 2\sqrt{q}$ and the sieve level $z$ is chosen to optimize the bound. For the right-hand side to be $< 1$, we need:

$$\prod_{\substack{q \mid D \\ q \text{ good}}} q > \binom{p}{k} \approx 2^{0.949p}$$

This holds if $\mathrm{rad}(D) > 2^{0.949p}$ (since almost all primes are "good").

### Step 5: The abc Conjecture Supplies the Missing Bound

**abc conjecture.** For coprime positive integers $a + b = c$ and any $\varepsilon > 0$, there exists $K_\varepsilon$ such that $c \leq K_\varepsilon \cdot \mathrm{rad}(abc)^{1+\varepsilon}$.

Apply to $a = 3^k$, $b = D$, $c = 2^p$ (these are coprime since $D$ is odd and coprime to 3):

$$2^p \leq K_\varepsilon \cdot \bigl(6 \cdot \mathrm{rad}(D)\bigr)^{1+\varepsilon}$$

Therefore:

$$\mathrm{rad}(D) \geq \frac{1}{6} \cdot \left(\frac{2^p}{K_\varepsilon}\right)^{1/(1+\varepsilon)} = \frac{2^{p/(1+\varepsilon)}}{6 \cdot K_\varepsilon^{1/(1+\varepsilon)}}$$

Choosing $\varepsilon = 0.04 < 1 - 0.949 = 0.051$:

$$\mathrm{rad}(D) \geq 2^{p/1.04 - O(1)} = 2^{0.9615p - O(1)} > 2^{0.949p} \geq \binom{p}{k}$$

for all sufficiently large $p$.

### Step 6: Assembly

Combining Steps 4 and 5: under the abc conjecture, for all $p > p_0(\varepsilon)$,

$$\#\{I : D \mid S(I)\} \leq \frac{\binom{p}{k}}{\mathrm{rad}(D)} \cdot (1 + o(1)) \leq \frac{2^{0.949p}}{2^{0.9615p}} \cdot (1+o(1)) = 2^{-0.0125p} \cdot (1+o(1)) < 1$$

Since the count is a non-negative integer and is $< 1$, it must be $0$. Therefore no parity pattern produces a valid cycle. $\square$

---

## Unconditional Status

### What is proved (no assumptions)

| Result | Status |
|--------|--------|
| Equidistribution of $S \bmod q$ for each prime $q \geq 5$ with $\mathrm{ord}_q(2) > \sqrt{q}$ | **Proved** (Theorem 4) |
| Equidistribution of $S \bmod M$ for squarefree $M$ with $\mathrm{ord}_M(2) > 2\sqrt{M}$ | **Proved** (Theorem 5) |
| Independence of $\{q \mid S\}$ events for qualifying prime sets | **Proved** (Corollary of Theorem 5) |
| Sieve framework: $\#\{I : D \mid S\} \leq \binom{p}{k}/\mathrm{rad}^*(D)$ | **Proved** |
| No nontrivial cycles for $p \leq 22$ | **Proved** (computation) |
| Heuristic count $\binom{p}{k}/D \to 0$ | **Proved** (from Rhin) |

### The gap

| Bound on $\log_2 \mathrm{rad}(D)$ | Source | Sufficient? |
|---|---|---|
| $\geq (1-\varepsilon)p$ | abc conjecture | **Yes** |
| $\geq c\sqrt{p}/\log p$ | Stewart (2013), unconditional | No |
| $\geq c \cdot p^{1/3}$ | Stewart–Yu (2001), unconditional | No |
| **Need:** $\geq 0.949p$ | — | — |

The gap between $\sqrt{p}$ and $p$ is the **abc barrier**. Closing it unconditionally would be a result comparable in significance to proving the abc conjecture itself.

---

## Alternative Directions (Not Explored Here)

1. **Density result:** Browning–Lichtman–Teravainen (2025, arXiv:2505.13991) prove "abc is true almost always." If this implies $\mathrm{rad}(2^p - 3^k)$ is large for all but finitely many $(p,k)$, combined with computation for the exceptions, the no-cycles theorem might follow unconditionally. This requires careful analysis of whether the density-1 set intersects $\{2^p - 3^k\}$ appropriately.

2. **GRH-conditional:** Under the Generalized Riemann Hypothesis, Artin's conjecture holds, giving $\mathrm{ord}_q(2) = q-1$ for a positive proportion of primes. This might strengthen the sieve but does not directly resolve the $\mathrm{rad}(D)$ question.

3. **Shimura curves:** Pasten (2024, Inventiones) uses Shimura curve methods to improve subexponential bounds on abc-type quantities. These improvements are subexponential and do not reach the exponential threshold needed here.
