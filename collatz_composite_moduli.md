# Theorem 5: Equidistribution of S mod M for Composite Moduli

## Statement

**Theorem 5.** Let $M$ be a squarefree positive integer with $\gcd(M, 6) = 1$. Let $d = \mathrm{ord}_M(2)$. If $d > 2\sqrt{M}$, then for $S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$ over uniformly random $k$-element subsets $I \subseteq \{0, \ldots, p-1\}$:

$$\left|P(S \equiv 0 \bmod M) - \frac{1}{M}\right| \leq (M-1) \cdot \exp(-c(M) \cdot p)$$

for an explicit constant $c(M) > 0$.

**Corollary (Independence).** For distinct primes $q_1, \ldots, q_r \geq 5$ with
$\mathrm{lcm}(\mathrm{ord}_{q_i}(2)) > 2\sqrt{q_1 \cdots q_r}$:

$$P(q_1 \mid S \text{ and } \cdots \text{ and } q_r \mid S) = \frac{1}{q_1 \cdots q_r} + O(e^{-cp})$$

*Proof of corollary.* Set $M = q_1 \cdots q_r$ (squarefree, coprime to 6). By CRT, the event $\{M \mid S\}$ is equivalent to $\{q_i \mid S \text{ for all } i\}$, and $P(M \mid S) = 1/M = 1/(q_1 \cdots q_r)$ is equivalent to independence. Note $\mathrm{ord}_M(2) = \mathrm{lcm}(\mathrm{ord}_{q_i}(2))$ by CRT. $\square$

---

## Proof of Theorem 5

The proof follows the same five-step structure as Theorem 4, with one new ingredient: the Gauss sum bound for composite moduli (Lemma 1 below).

### Step 1: Fourier Reduction

By discrete Fourier inversion:

$$P(S \equiv 0 \bmod M) = \frac{1}{M} + \frac{1}{M} \sum_{t=1}^{M-1} \hat\mu(t)$$

where $\hat\mu(t) = \frac{1}{\binom{p}{k}} \sum_{|I|=k} e^{2\pi i t S(I)/M}$.

By the triangle inequality:

$$\left|P(S \equiv 0) - \frac{1}{M}\right| \leq \frac{M-1}{M} \max_{t \neq 0} |\hat\mu(t)|$$

It suffices to show $|\hat\mu(t)| = O(\exp(-c \cdot p))$ for each $t \not\equiv 0 \pmod{M}$.

### Step 2: Block Decomposition

Since $2^d \equiv 1 \pmod{M}$ where $d = \mathrm{ord}_M(2)$, partition $\{0, \ldots, p-1\}$ into $L = \lfloor p/d \rfloor$ complete blocks of size $d$, plus a remainder of size $< d$.

### Step 3: Factorization Given Occupancy

For a fixed block occupancy pattern $\mathbf{r} = (r_1, \ldots, r_L, r_R)$ with $\sum r_\ell + r_R = k$, the entering rank at each block is deterministic: $s_\ell = r_1 + \cdots + r_\ell$. The intra-block selections are independent across blocks, giving:

$$\sum_{\substack{I : \text{occupancy} = \mathbf{r}}} e^{2\pi i t S(I)/M} = \prod_{\ell=1}^{L} B(s_{\ell-1}, r_\ell) \cdot B_R(s_L, r_R)$$

This step is identical to Theorem 4 and does not depend on the modulus.

### Step 4: Character Sum Bound (New Ingredient)

**Lemma 1 (Gauss sum bound for composite moduli).** Let $M = q_1 \cdots q_r$ be squarefree with each $q_i$ prime and $\gcd(M, 6) = 1$. Let $H_M = \langle 2 \rangle \leq (\mathbb{Z}/M\mathbb{Z})^*$ with $|H_M| = d = \mathrm{ord}_M(2)$. For any $c \not\equiv 0 \pmod{M}$:

$$\left|\sum_{h \in H_M} e^{2\pi i ch/M}\right| \leq 2\sqrt{M}$$

*Proof.* Write $\psi(x) = e^{2\pi i x/M}$. By orthogonality of multiplicative characters of $(\mathbb{Z}/M\mathbb{Z})^*$:

$$\sum_{h \in H_M} \psi(ch) = \frac{d}{\phi(M)} \sum_{\substack{\chi \bmod M \\ \chi|_{H_M} = 1}} \bar\chi(c) \cdot \tau(\chi)$$

where $\tau(\chi) = \sum_{x \in (\mathbb{Z}/M\mathbb{Z})^*} \chi(x) \psi(x)$ is the Gauss sum.

**Claim:** For squarefree $M = q_1 \cdots q_r$, Gauss sums are multiplicative:

$$\tau(\chi) = \prod_{i=1}^{r} \tau(\chi_i)$$

where $\chi = \chi_1 \otimes \cdots \otimes \chi_r$ under the CRT isomorphism $(\mathbb{Z}/M\mathbb{Z})^* \cong \prod (\mathbb{Z}/q_i\mathbb{Z})^*$.

*Proof of claim.* Under CRT, write $x \leftrightarrow (x_1, \ldots, x_r)$, so $\chi(x) = \prod \chi_i(x_i)$. The additive character also factors: $\psi(x) = e^{2\pi i x/M} = \prod_{i=1}^r e^{2\pi i x_i \bar{Q}_i / q_i}$ where $Q_i = M/q_i$ and $\bar{Q}_i = Q_i^{-1} \bmod q_i$. Since the CRT map is a bijection on units:

$$\tau(\chi) = \sum_{x \in (\mathbb{Z}/M\mathbb{Z})^*} \prod_i \chi_i(x_i) \cdot e^{2\pi i x_i \bar{Q}_i / q_i} = \prod_{i=1}^r \sum_{x_i \in (\mathbb{Z}/q_i\mathbb{Z})^*} \chi_i(x_i) \cdot e^{2\pi i x_i \bar{Q}_i / q_i} = \prod_i \tau(\chi_i, \psi_{q_i}^{\bar{Q}_i})$$

For each factor, $\psi_{q_i}^{\bar{Q}_i}$ is a non-trivial additive character of $\mathbb{Z}/q_i\mathbb{Z}$ (since $\bar{Q}_i \not\equiv 0$), and $|\tau(\chi_i, \psi_{q_i}^{\bar{Q}_i})| = \sqrt{q_i}$ for non-principal $\chi_i$ (standard result for Gauss sums over finite fields). For the principal character $\chi_{0,i}$, $|\tau(\chi_{0,i}, \psi_{q_i}^{\bar{Q}_i})| = 1$ (the Ramanujan sum $c_{q_i}(\bar{Q}_i) = \mu(q_i) = -1$). $\square$

**Bounding the sum.** The set of characters $\chi$ trivial on $H_M$ has order $\phi(M)/d$.

- For the principal character $\chi_0$: $|\tau(\chi_0)| = |\prod_i \mu(q_i)| = 1$.
- For any non-principal $\chi$: $|\tau(\chi)| = \prod_{i: \chi_i \neq \chi_0} \sqrt{q_i} \leq \sqrt{M}$.

Therefore:

$$\left|\sum_{h \in H_M} \psi(ch)\right| \leq \frac{d}{\phi(M)} \left(1 + \left(\frac{\phi(M)}{d} - 1\right) \sqrt{M}\right) = \frac{d}{\phi(M)} + \left(1 - \frac{d}{\phi(M)}\right)\sqrt{M}$$

Since $d/\phi(M) \leq 1$ and $\sqrt{M} \geq 1$, this is $\leq 1 + \sqrt{M} \leq 2\sqrt{M}$. $\square$

**Application to blocks.** For $r_\ell = 1$ blocks:

$$|B(s, 1)| = \left|\sum_{j=0}^{d-1} e^{2\pi i c_{s+1} \cdot 2^j / M}\right| \leq 2\sqrt{M}$$

where $c_{s+1} = t \cdot 3^{k-s-1} \not\equiv 0 \pmod{M}$ (since $\gcd(t \cdot 3^{k-s-1}, M) = 1$ when $\gcd(M, 6) = 1$ and $t \not\equiv 0$).

The saving factor is:

$$\rho = \frac{2\sqrt{M}}{d} < 1 \qquad \text{when } d > 2\sqrt{M}$$

### Step 5: Concentration and Assembly

Identical to Theorem 4. The number of single-selection blocks $n_1$ concentrates around $p_1 L > 0$ under the hypergeometric distribution. By Hoeffding:

$$|\hat\mu(t)| \leq \rho^{(p_1 - \epsilon)L} + e^{-2\epsilon^2 L}$$

Both terms decay exponentially in $L \sim p/d$, giving $|\hat\mu(t)| = O(\exp(-c(M) \cdot p))$. $\square$

---

## Condition Verification

The condition $d = \mathrm{ord}_M(2) > 2\sqrt{M}$ must be verified for each composite $M$.

For $M = q_1 q_2$ (product of two primes): $d = \mathrm{lcm}(\mathrm{ord}_{q_1}(2), \mathrm{ord}_{q_2}(2))$.

| $q_1$ | $q_2$ | $d_1$ | $d_2$ | $d = \mathrm{lcm}$ | $2\sqrt{M}$ | Condition? |
|--------|--------|--------|--------|---------------------|--------------|------------|
| 5      | 7      | 4      | 3      | 12                  | 11.83        | Yes (barely) |
| 5      | 11     | 4      | 10     | 20                  | 14.83        | Yes |
| 5      | 13     | 4      | 12     | 12                  | 16.12        | **No** |
| 7      | 11     | 3      | 10     | 30                  | 17.55        | Yes |
| 7      | 13     | 3      | 12     | 12                  | 19.08        | **No** |
| 11     | 13     | 10     | 12     | 60                  | 23.92        | Yes |
| 5      | 17     | 4      | 8      | 8                   | 18.44        | **No** |
| 5      | 19     | 4      | 18     | 36                  | 19.49        | Yes |

Note: Some pairs fail the condition (e.g., $\{5, 13\}$ where $\mathrm{lcm}(4, 12) = 12 < 16.12$). For these pairs, the proof does not apply and independence is not established by this method.

---

## Implications for Collatz Cycles

### What Theorem 5 gives us

For any finite set of primes satisfying the lcm condition, the events $\{q_i \mid S\}$ are asymptotically independent. The sieve product $\prod 1/q_i$ correctly estimates the probability of simultaneous divisibility.

### The remaining gap

To prove no nontrivial cycles exist, we need:

$$\text{Expected solutions} = \frac{\binom{p}{k}}{D} \to 0$$

where $D = 2^p - 3^k$. This is equivalent to showing $D > \binom{p}{k}$, which holds since $D \sim 2^p$ while $\binom{p}{k} \sim 2^{0.95p}$.

But making this rigorous requires equidistribution of $S$ modulo $D$ itself (or at least modulo $\mathrm{rad}(D)$), which needs $\mathrm{ord}_D(2) > 2\sqrt{D}$. Since $D \sim 2^p$, this requires $\mathrm{ord}_D(2) > 2^{p/2+1}$, a condition we cannot verify in general.

**Conditional result (assuming abc):** The abc conjecture implies $\mathrm{rad}(D) \geq D^{1-\epsilon}/6$, which combined with Theorem 5 (applied to the radical) would give the no-cycles result.

**Unconditional:** Stewart-Yu (2001) gives $\log \mathrm{rad}(D) \geq c \cdot p^{1/3}$, far short of the needed $\log \mathrm{rad}(D) \geq 0.66p$.
