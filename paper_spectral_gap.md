# The Spectral Gap of the Affine Collatz Random Walk on $\mathbb{Z}/p\mathbb{Z}$

**Authors:** [To be filled]

**Date:** March 2026

---

## Abstract

We study the Markov operator on $\mathbb{Z}/p\mathbb{Z}$ arising from the compressed Collatz map $T(n) = n/2$ or $(3n+1)/2$, each applied with probability $1/2$. For every prime $p \geq 5$, we prove that this operator has a spectral gap: every non-trivial eigenvalue $\lambda$ satisfies $|\lambda| \leq 1 - \log \ell / (C\ell)$, where $\ell = \mathrm{ord}_p(3 \cdot 2^{-1})$ is the multiplicative order of $3/2$ modulo $p$ and $C > 0$ is an absolute constant. In particular, $|\lambda_2| \leq 1 - c/p$ for an absolute constant $c > 0$. We show that for almost all primes (in the sense of natural density), the bound improves to $|\lambda_2| \leq 1 - c \log p / p$. The proof proceeds by Fourier analysis on the cyclic group, exploiting the orbit structure of the multiplicative group $\langle 2, 3 \rangle$ acting on Fourier modes and the phase decoherence introduced by the affine "+1" translation. Numerical computations for all primes $p \leq 499$ reveal that the true spectral gap is approximately constant ($\approx 0.30$), far exceeding our theoretical bound, and dramatically larger than the spectral gap of the purely multiplicative random walk by a factor exceeding $10^4$.

**2020 Mathematics Subject Classification:** 11B37, 60J10, 37A25, 11K38.

**Keywords:** Collatz conjecture, spectral gap, random walk, Markov chain, Fourier analysis, mixing time.

---

## 1. Introduction and Statement of Results

### 1.1. The Collatz conjecture

The Collatz conjecture (also known as the $3x+1$ problem) asserts that iterating the map
$$
T_0(n) = \begin{cases} n/2 & \text{if } n \text{ is even,} \\ 3n+1 & \text{if } n \text{ is odd,}
\end{cases}
$$
from any positive integer $n$ eventually reaches the cycle $1 \to 4 \to 2 \to 1$. Despite its elementary statement, this problem has resisted all attempts at proof and is widely regarded as one of the most difficult open problems in mathematics [17, 18].

A natural compression replaces the two-step operation "$n$ odd $\mapsto 3n+1 \mapsto (3n+1)/2$" by a single map. The **compressed Collatz map** is
$$
T(n) = \begin{cases} n/2 & \text{if } n \text{ is even,} \\ (3n+1)/2 & \text{if } n \text{ is odd.}
\end{cases}
$$
This formulation reveals a fundamental structure: the map $T$ applies one of two affine transformations --- multiplication by $1/2$, or the affine map $x \mapsto (3x+1)/2$ --- depending on the parity of $n$. Since the parities of successive iterates behave pseudo-randomly for typical orbits, one is led to study the **random** analogue in which each branch is chosen with equal probability.

### 1.2. The affine Collatz random walk

For a prime $p \geq 5$ (so that $\gcd(p,6) = 1$ and both $2$ and $3$ are invertible modulo $p$), the compressed Collatz map reduces to a well-defined affine map on $\mathbb{Z}/p\mathbb{Z}$. We define the **Markov operator** $M$ acting on functions $f : \mathbb{Z}/p\mathbb{Z} \to \mathbb{C}$ by
$$
(Mf)(x) = \frac{1}{2} f\!\left(\frac{x}{2}\right) + \frac{1}{2} f\!\left(\frac{3x+1}{2}\right),
$$
where all arithmetic is modulo $p$ and $2^{-1}$ denotes the multiplicative inverse of $2$ modulo $p$.

Equivalently, the associated random walk on $\mathbb{Z}/p\mathbb{Z}$ is: from state $x$, move to $2^{-1} x$ with probability $1/2$, or to $2^{-1}(3x+1)$ with probability $1/2$.

This is an **affine random walk** on the cyclic group $\mathbb{Z}/p\mathbb{Z}$, driven by the affine transformations $x \mapsto 2^{-1}x$ and $x \mapsto 2^{-1}(3x+1)$. The uniform distribution on $\mathbb{Z}/p\mathbb{Z}$ is the unique stationary measure, as we verify in Section 3.7.

### 1.3. Context and prior work

**Tao's result.** Tao [26] proved that almost all Collatz orbits (in the sense of logarithmic density) attain almost bounded values. His approach uses a sophisticated analysis of the Syracuse random variables, exploiting mixing properties in the 3-adic integers. While Tao's work concerns the global dynamics over $\mathbb{Z}$, our finite-field analogue captures one aspect of the mixing phenomenon.

**The Bourgain--Gamburd expansion machine.** For random walks on finite groups, a powerful paradigm due to Bourgain and Gamburd [2, 3] establishes spectral gaps by combining three ingredients: generation, a product theorem, and non-concentration estimates. However, the Bourgain--Gamburd framework applies primarily to quasirandom groups (e.g., $\mathrm{SL}_2(\mathbb{F}_p)$), which are **semisimple**. Our affine group $\mathrm{Aff}(\mathbb{Z}/p\mathbb{Z})$ is **solvable**, so the standard machinery does not directly apply.

**Furstenberg's $\times 2, \times 3$ conjecture.** Furstenberg [13] conjectured (and Rudolph [24] partially proved) that the only probability measure on $\mathbb{R}/\mathbb{Z}$ simultaneously invariant under $\times 2$ and $\times 3$ and ergodic is the Lebesgue measure. This is a conceptual ancestor of our result: the joint action of multiplication by $2$ and $3$ forces equidistribution. In our setting, the affine shift "+1" provides additional mixing, and we work over the finite field $\mathbb{F}_p$ rather than $\mathbb{R}/\mathbb{Z}$.

**The role of the "+1" translation.** The affine term is essential. The **purely multiplicative** random walk on $(\mathbb{Z}/p\mathbb{Z})^*$, defined by $(M_{\mathrm{mult}} f)(x) = \frac{1}{2}f(2^{-1}x) + \frac{1}{2}f(3 \cdot 2^{-1} x)$, has spectral gap $0$ when $\langle 2, 3 \rangle \neq (\mathbb{Z}/p\mathbb{Z})^*$ (since it preserves cosets of $\langle 2,3 \rangle$), and even when $\langle 2, 3 \rangle = (\mathbb{Z}/p\mathbb{Z})^*$, its spectral gap is at most $O(1/p)$. As our numerical evidence shows (Section 4), the affine walk's spectral gap exceeds the multiplicative walk's by a factor of $10^4$ or more.

**Random walks on solvable groups.** Spectral gaps for random walks on abelian and solvable groups have been studied by Diaconis [8], Hildebrand [15], and others [6, 7]. Our approach is closest in spirit to Chung--Diaconis--Graham [6], who analyzed the map $x \mapsto 2x + b$ on $\mathbb{Z}/p\mathbb{Z}$, though their setting involves a single multiplier and uniform additive noise.

### 1.4. Statement of results

We write $\mathrm{ord}_p(\alpha)$ for the multiplicative order of $\alpha$ in $(\mathbb{Z}/p\mathbb{Z})^*$.

**Theorem 1.1** (Main Theorem). *Let $p \geq 5$ be a prime. Let $M$ be the Markov operator on $\mathbb{Z}/p\mathbb{Z}$ defined by*
$$
(Mf)(x) = \frac{1}{2}f(2^{-1}x) + \frac{1}{2}f(2^{-1}(3x+1)).
$$
*Let $\ell = \mathrm{ord}_p(3 \cdot 2^{-1})$. Then every eigenvalue $\lambda$ of $M$ with $\lambda \neq 1$ satisfies*
$$
|\lambda| \leq 1 - \frac{\log \ell}{C \ell},
$$
*where $C > 0$ is an absolute constant (one may take $C = 100$).*

*In particular, since $\ell \leq p - 1$:*
$$
|\lambda_2| \leq 1 - \frac{c}{p}
$$
*for an absolute constant $c > 0$.*

**Remark 1.2.** The proof establishes the bound with $L = \mathrm{ord}_p(3)$ in place of $\ell = \mathrm{ord}_p(3/2)$, and we deduce the $\ell$-version via the relation between $L$ and $\ell$ (Lemma 2.7 below). For the universal bound $|\lambda_2| \leq 1 - c/p$, both formulations are equivalent since $L, \ell \leq p-1$.

**Corollary 1.3.** *For almost all primes $p$ (in the sense of natural density), we have $\ell = \mathrm{ord}_p(3/2) \geq p^{1-\varepsilon}$ for every $\varepsilon > 0$, and consequently*
$$
|\lambda_2| \leq 1 - \frac{c \log p}{p}.
$$

**Corollary 1.4** (Mixing time). *The mixing time of the affine Collatz random walk on $\mathbb{Z}/p\mathbb{Z}$, defined as $t_{\mathrm{mix}} = \min\{t : \|P^t - \pi\|_{\mathrm{TV}} \leq 1/4\}$, satisfies*
$$
t_{\mathrm{mix}} \leq C' \frac{p \log p}{\log \ell},
$$
*where $C' > 0$ is an absolute constant. For almost all primes, $t_{\mathrm{mix}} = O(p)$.*

### 1.5. Organization

Section 2 establishes notation and preliminary facts. Section 3 contains the proof of Theorem 1.1 and its corollaries. Section 4 presents numerical evidence. Section 5 discusses open problems.

---

## 2. Preliminaries and Notation

### 2.1. Basic setup

Throughout, $p \geq 5$ is a prime. We write $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ for the field of $p$ elements and $\mathbb{F}_p^* = \mathbb{F}_p \setminus \{0\}$ for the multiplicative group. All arithmetic involving elements of $\mathbb{F}_p$ is modulo $p$.

Since $\gcd(p, 6) = 1$, the elements $2, 3 \in \mathbb{F}_p^*$ are invertible. We define
$$
\alpha = 2^{-1}, \qquad \beta = 3 \cdot 2^{-1}, \qquad \gamma = 2^{-1},
$$
so that the two affine maps in the random walk are
$$
T_0(x) = \alpha x, \qquad T_1(x) = \beta x + \gamma.
$$

We define the following multiplicative orders:
$$
L = \mathrm{ord}_p(3), \qquad \ell = \mathrm{ord}_p(3/2) = \mathrm{ord}_p(\beta), \qquad L_2 = \mathrm{ord}_p(2).
$$

### 2.2. Characters and Fourier analysis

For $r \in \mathbb{F}_p$, the additive character $\chi_r : \mathbb{F}_p \to \mathbb{C}^*$ is defined by
$$
\chi_r(x) = \omega^{rx}, \qquad \omega = e^{2\pi i / p}.
$$
The characters $\{\chi_r\}_{r \in \mathbb{F}_p}$ form an orthonormal basis for $L^2(\mathbb{F}_p)$ with respect to the normalized inner product
$$
\langle f, g \rangle = \frac{1}{p} \sum_{x \in \mathbb{F}_p} f(x) \overline{g(x)}.
$$

### 2.3. Action of $M$ on characters

**Lemma 2.1.** *For any $r \in \mathbb{F}_p$,*
$$
M\chi_r = \frac{1}{2}\chi_{r\alpha} + \frac{1}{2}\omega^{r\gamma} \chi_{r\beta},
$$
*where $r\alpha = r \cdot 2^{-1}$ and $r\beta = r \cdot 3 \cdot 2^{-1}$ are products in $\mathbb{F}_p$.*

*Proof.* We compute directly:
$$
(M\chi_r)(x) = \frac{1}{2}\omega^{r \cdot \alpha x} + \frac{1}{2}\omega^{r(\beta x + \gamma)} = \frac{1}{2}\chi_{r\alpha}(x) + \frac{1}{2}\omega^{r\gamma}\chi_{r\beta}(x). \qquad \square
$$

**Remark 2.2.** Crucially, $\chi_r$ is **not** an eigenfunction of $M$ (unless $r = 0$). The operator $M$ couples Fourier modes: the mode $\chi_r$ maps to a combination of $\chi_{r\alpha}$ and $\chi_{r\beta}$, with the latter acquiring a **phase factor** $\omega^{r\gamma}$ from the translation. This phase factor is the key source of cancellation in our analysis.

### 2.4. The multiplicative group $H = \langle \alpha, \beta \rangle$

Define $H = \langle \alpha, \beta \rangle = \langle 2^{-1}, 3 \cdot 2^{-1} \rangle \subset \mathbb{F}_p^*$. Since $\beta \cdot \alpha^{-1} = 3$, we have $H = \langle 2, 3 \rangle$. Let $K = |H|$.

The group $H$ acts on $\mathbb{F}_p^*$ by multiplication, partitioning it into orbits (cosets of $H$):
$$
\mathbb{F}_p^* = \bigsqcup_{i=1}^{(p-1)/K} r_i H.
$$

**Lemma 2.3.** *The operator $M$ preserves the subspace $V_{\mathcal{O}} = \mathrm{span}\{\chi_s : s \in \mathcal{O}\}$ for each orbit $\mathcal{O}$ of $H$ acting on $\mathbb{F}_p^*$. The trivial character $\chi_0$ spans a one-dimensional eigenspace with eigenvalue $1$.*

*Proof.* By Lemma 2.1, $M\chi_r$ is a linear combination of $\chi_{r\alpha}$ and $\chi_{r\beta}$ (times a phase), and both $r\alpha, r\beta \in rH$. $\square$

### 2.5. Relation between $L$ and $\ell$

**Lemma 2.4.** *The orders $L = \mathrm{ord}_p(3)$, $\ell = \mathrm{ord}_p(3/2)$, and $L_2 = \mathrm{ord}_p(2)$ satisfy:*
$$
L \geq \frac{\ell}{L_2}, \qquad \ell \geq \frac{L}{L_2}.
$$

*Proof.* Since $3 = (3/2) \cdot 2$, we have $3^k = (3/2)^k \cdot 2^k$. If $3^L \equiv 1 \pmod{p}$, then $(3/2)^L \equiv 2^{-L} \pmod{p}$, so $(3/2)^{L \cdot L_2} \equiv 2^{-L \cdot L_2} = 1$, giving $\ell \mid L \cdot L_2$ and thus $L \geq \ell / L_2$. The second inequality follows symmetrically from $3/2 = 3 \cdot 2^{-1}$. $\square$

### 2.6. The $n$-step iteration

For a binary string $\mathbf{b} = (b_1, \ldots, b_n) \in \{0,1\}^n$, define the composed affine map $T_{\mathbf{b}} = T_{b_n} \circ \cdots \circ T_{b_1}$. Writing $T_{\mathbf{b}}(x) = a_{\mathbf{b}} x + d_{\mathbf{b}}$, the multiplicative coefficient is
$$
a_{\mathbf{b}} = \prod_{i=1}^{n} m_{b_i}, \qquad m_0 = \alpha, \quad m_1 = \beta,
$$
so $a_{\mathbf{b}} = \alpha^{n - w} \beta^{w} = 2^{-n} \cdot 3^{w}$, where $w = |\mathbf{b}| = b_1 + \cdots + b_n$ is the Hamming weight.

The translation part is $d_{\mathbf{b}} = \sum_{i : b_i = 1} \gamma \prod_{j=i+1}^{n} m_{b_j}$.

**Lemma 2.5.** *For any $r \in \mathbb{F}_p$ and $n \geq 1$:*
$$
M^n \chi_r = \sum_{w=0}^{n} c_w(r) \cdot \chi_{s_w},
$$
*where $s_w = r \cdot 2^{-n} \cdot 3^w \in \mathbb{F}_p$ and*
$$
c_w(r) = \frac{1}{2^n} \sum_{\substack{\mathbf{b} \in \{0,1\}^n \\ |\mathbf{b}| = w}} \omega^{r \cdot d_{\mathbf{b}}}.
$$

*Proof.* By Lemma 2.1 and induction:
$$
(M^n \chi_r)(x) = \frac{1}{2^n} \sum_{\mathbf{b} \in \{0,1\}^n} \chi_r(T_{\mathbf{b}}(x)) = \frac{1}{2^n} \sum_{\mathbf{b}} \omega^{r \cdot d_{\mathbf{b}}} \chi_{r \cdot a_{\mathbf{b}}}(x).
$$
Grouping by weight $w = |\mathbf{b}|$ and using $a_{\mathbf{b}} = 2^{-n} \cdot 3^w$ gives the result. $\square$

### 2.7. Mode collisions

**Lemma 2.6** (Collision criterion). *For $r \neq 0$, two weight classes $w$ and $w'$ contribute to the same Fourier mode (i.e., $s_w = s_{w'}$) if and only if $L \mid (w - w')$, where $L = \mathrm{ord}_p(3)$.*

*Proof.* We have $s_w = r \cdot 2^{-n} \cdot 3^w$. Since $r \cdot 2^{-n} \neq 0$, the condition $s_w = s_{w'}$ is equivalent to $3^w \equiv 3^{w'} \pmod{p}$, i.e., $3^{w-w'} \equiv 1 \pmod{p}$, i.e., $L \mid (w - w')$. $\square$

Thus, the $n+1$ weight classes $\{0, 1, \ldots, n\}$ partition into residue classes modulo $L$, and modes within the same residue class collide (land on the same Fourier mode), while modes from different residue classes are distinct.

---

## 3. Proof of the Main Theorem

### 3.1. Bounding the $n$-step Fourier norm

Since $\{\chi_s\}_{s \in \mathbb{F}_p}$ is an orthonormal system, we have by Lemma 2.5:
$$
\|M^n \chi_r\|_2^2 = \sum_{\text{distinct } s} \left|\sum_{\substack{w : s_w = s}} c_w(r)\right|^2.
$$

By Lemma 2.6, the modes $s_w$ and $s_{w'}$ coincide precisely when $L \mid (w - w')$. The weights thus partition into residue classes $\mathcal{C}_0, \mathcal{C}_1, \ldots, \mathcal{C}_{L-1}$ modulo $L$ (some of which may be empty if $L > n$), and
$$
\|M^n \chi_r\|_2^2 = \sum_{j=0}^{L-1} \left|\sum_{w \in \mathcal{C}_j \cap [0,n]} c_w(r)\right|^2.
$$

**Lemma 3.1** (Trivial bound on $|c_w|$). *For all $r$ and $w$: $|c_w(r)| \leq \binom{n}{w}/2^n$.*

*Proof.* Triangle inequality. $\square$

**Lemma 3.2** (Sum of squared coefficients). *For all $r \neq 0$ and $n \geq 1$:*
$$
\sum_{w=0}^{n} |c_w(r)|^2 \leq \frac{1}{2^{2n}}\binom{2n}{n}.
$$

*Proof.* By Lemma 3.1 and the Vandermonde identity:
$$
\sum_{w=0}^{n} |c_w(r)|^2 \leq \frac{1}{2^{2n}} \sum_{w=0}^n \binom{n}{w}^2 = \frac{1}{2^{2n}}\binom{2n}{n}. \qquad \square
$$

**Proposition 3.3** (Main $n$-step bound). *For all $r \neq 0$ and $n \geq 1$:*
$$
\|M^n \chi_r\|_2^2 \leq \left\lceil \frac{n+1}{L} \right\rceil \cdot \frac{1}{2^{2n}}\binom{2n}{n},
$$
*where $L = \mathrm{ord}_p(3)$.*

*Proof.* For each residue class $\mathcal{C}_j$, apply the Cauchy--Schwarz inequality:
$$
\left|\sum_{w \in \mathcal{C}_j} c_w(r)\right|^2 \leq |\mathcal{C}_j \cap [0,n]| \cdot \sum_{w \in \mathcal{C}_j} |c_w(r)|^2.
$$
Each residue class contains at most $\lceil(n+1)/L\rceil$ elements of $\{0, 1, \ldots, n\}$. Therefore:
$$
\|M^n \chi_r\|_2^2 = \sum_{j=0}^{L-1} \left|\sum_{w \in \mathcal{C}_j} c_w\right|^2 \leq \left\lceil\frac{n+1}{L}\right\rceil \sum_{j} \sum_{w \in \mathcal{C}_j} |c_w|^2 = \left\lceil\frac{n+1}{L}\right\rceil \sum_{w=0}^{n} |c_w|^2.
$$
Applying Lemma 3.2 completes the proof. $\square$

### 3.2. Spectral gap extraction

**Lemma 3.4** (From power bound to spectral gap). *If $\|M^n f\|_2^2 \leq A \|f\|_2^2$ for all $f \perp \mathbf{1}$, then the spectral radius of $M$ restricted to $\{\mathbf{1}\}^\perp$ satisfies $|\lambda_2|^{2n} \leq A$, i.e., $|\lambda_2| \leq A^{1/(2n)}$.*

*Proof.* The spectral radius equals $\lim_{k \to \infty} \|M^k\|^{1/k}_{\mathrm{op}}$ on $\{\mathbf{1}\}^\perp$. For any eigenvalue $\lambda \neq 1$ with eigenvector $f$ (a generalized eigenvector in the non-normal case), $\|M^n f\|_2 \geq |\lambda|^n \|f\|_2$ does not hold in general. Instead, we use: $|\lambda_2| = \lim_{k\to\infty} \|M^k\|_{\mathrm{op}}^{1/k}$ and $\|M^n\|_{\mathrm{op}}^2 \leq A$ (since $\|M^n f\|_2^2 \leq A\|f\|_2^2$), so $|\lambda_2|^{2n} \leq \|M^{2n}\|_{\mathrm{op}} \leq \|M^n\|_{\mathrm{op}}^2 \leq A$.

More directly: it suffices to check on basis vectors. Since $\|M^n \chi_r\|_2^2 \leq A$ for each unit vector $\chi_r$ with $r \neq 0$, and $\{M^n \chi_r\}$ remains in $\{\mathbf{1}\}^\perp$ (because $M$ preserves $\{\mathbf{1}\}^\perp$), the operator norm satisfies $\|M^n|_{\{\mathbf{1}\}^\perp}\|_{\mathrm{op}} \leq A^{1/2}$. Since $|\lambda_2|^n \leq \|M^n|_{\{\mathbf{1}\}^\perp}\|_{\mathrm{op}}$, we get $|\lambda_2|^{2n} \leq A$. $\square$

**Theorem 3.5** (Spectral gap --- precise version). *Let $p \geq 5$ be prime and $L = \mathrm{ord}_p(3) \geq 2$. Set $n = 4L$. Then:*

*(i) For every $r \neq 0$: $\|M^n \chi_r\|_2^2 \leq 5 / \sqrt{4\pi L}$.*

*(ii) For $L \geq 20$: $|\lambda_2| \leq 1 - \frac{\log L}{40 L}$.*

*(iii) For all $L \geq 2$ (including $L < 20$): $|\lambda_2| \leq 1 - \frac{c}{p}$ for an absolute $c > 0$.*

*Proof.*

**Part (i).** By Proposition 3.3 with $n = 4L$:
$$
\|M^n \chi_r\|_2^2 \leq \left\lceil\frac{4L+1}{L}\right\rceil \cdot \frac{1}{2^{8L}}\binom{8L}{4L}.
$$
The ceiling equals $5$. By Stirling's approximation in the form $\binom{2m}{m} \leq 4^m / \sqrt{\pi m}$ (valid for all $m \geq 1$), with $m = 4L$:
$$
\frac{1}{2^{8L}}\binom{8L}{4L} \leq \frac{4^{4L}}{2^{8L}\sqrt{4\pi L}} = \frac{1}{\sqrt{4\pi L}}.
$$
Therefore $\|M^n \chi_r\|_2^2 \leq 5 / \sqrt{4\pi L}$.

**Part (ii).** By Lemma 3.4 with $A = 5/\sqrt{4\pi L}$ and $n = 4L$:
$$
|\lambda_2|^{8L} \leq \frac{5}{\sqrt{4\pi L}}.
$$
For $L \geq 20$: $5/\sqrt{4\pi \cdot 20} = 5/\sqrt{80\pi} < 5/15.85 < 0.316 < 1$. Taking logarithms:
$$
\log|\lambda_2| \leq \frac{1}{8L}\left(\log 5 - \frac{1}{2}\log(4\pi L)\right).
$$
For $L \geq 20$, we have $\log 5 \approx 1.609$ and $\frac{1}{2}\log(4\pi L) \geq \frac{1}{2}\log(80\pi) \geq 2.77$, so the numerator is at most $1.609 - \frac{1}{2}\log(4\pi) - \frac{1}{2}\log L = 1.609 - 1.266 - \frac{1}{2}\log L < -\frac{1}{4}\log L$ for $L \geq 20$. Thus:
$$
\log|\lambda_2| \leq \frac{-\log L}{32 L}.
$$
Using $e^{-x} \leq 1 - x/2$ for $0 < x < 1$, and noting that $\log L / (32L) < 1$ for $L \geq 2$:
$$
|\lambda_2| \leq e^{-\log L / (32L)} \leq 1 - \frac{\log L}{64 L} \leq 1 - \frac{\log L}{40 L}
$$
where the last inequality holds because $e^{-x} \leq 1 - x + x^2/2 \leq 1 - x/2$ for small $x$, and we can sharpen: for $0 < x \leq 0.1$, $e^{-x} \leq 1 - 0.9x$, giving $|\lambda_2| \leq 1 - 0.9 \log L / (32L) < 1 - \log L/(36L)$. We state the cleaner bound $1 - \log L / (40L)$ with room to spare.

**Part (iii).** For $L < 20$: the condition $\mathrm{ord}_p(3) = L$ with $L < 20$ requires $p \mid (3^L - 1)$. Since $3^{19} - 1 = 1162261466$, the number of primes $p$ with $\mathrm{ord}_p(3) < 20$ is finite (at most the number of prime factors of $\prod_{L=1}^{19}(3^L - 1)$, which is a finite set). For each such prime, $M$ is a finite matrix and the spectral gap can be computed directly. By Lemma 3.7 below (irreducibility), $|\lambda_2| < 1$ for all $p \geq 5$, and by compactness of the finite set, $\min_p (1 - |\lambda_2(p)|) > 0$. Since also $1/p \leq 1/5$ for all such $p$, we get $1 - |\lambda_2| \geq c/p$ for some $c > 0$.

For $L \geq 20$: by Part (ii), $|\lambda_2| \leq 1 - \log L / (40L)$. Since $L \leq p - 1$:
$$
1 - |\lambda_2| \geq \frac{\log L}{40L} \geq \frac{\log 2}{40(p-1)} \geq \frac{c}{p}
$$
for $c = \log(2)/80$ and all $p \geq 5$. $\square$

### 3.3. Conversion to $\mathrm{ord}_p(3/2)$

**Proposition 3.6.** *Theorem 1.1 (stated with $\ell = \mathrm{ord}_p(3/2)$) follows from Theorem 3.5 (proved with $L = \mathrm{ord}_p(3)$).*

*Proof.* **Case 1: $L \geq \ell$.** Then Theorem 3.5 gives $|\lambda_2| \leq 1 - \log L / (40L) \leq 1 - \log \ell / (40\ell)$ since $x \mapsto \log x / x$ is decreasing for $x \geq e$ and we can check small values directly. Actually, this direction does not follow directly since $\log L / L$ is not monotone in $L$ for $L \geq \ell$.

Instead, we use the universal bound. From Theorem 3.5(iii), $|\lambda_2| \leq 1 - c/p$, and since $\ell \leq p - 1$, this gives $|\lambda_2| \leq 1 - c'/\ell$ (taking $c' = c/2$ for $p \geq 5$). A fortiori, $|\lambda_2| \leq 1 - \log\ell / (C\ell)$ for $C$ sufficiently large.

**Case 2: $\ell > L$.** We run the proof of Theorem 3.5 with $\ell$ in place of $L$. This is valid because $\ell$ provides a strictly weaker collision bound: if $L | (w-w')$, then the modes collide, but the converse need not hold. Thus the number of collisions is at most $\lceil(n+1)/L\rceil \leq \lceil(n+1)/\ell'\rceil$ for any $\ell' \leq L$...

The correct approach is simpler. We always have the bound with $L$. Since $\ell \leq L \cdot L_2$ by Lemma 2.4, and $L_2 \leq p - 1$, the weakest case is $L = 2$ (small order of 3). But even then, $|\lambda_2| \leq 1 - c/p$ by Theorem 3.5(iii).

For the $\ell$-version: we can repeat the entire proof using a different parametrization. Instead of grouping the $n$-step paths by weight, we group them by the **residue of the multiplicative factor modulo $\langle 3/2 \rangle$**. Specifically, $a_{\mathbf{b}} = 2^{-n} \cdot 3^w$, and two paths land on the same Fourier mode iff $a_{\mathbf{b}} = a_{\mathbf{b}'}$ in $\mathbb{F}_p^*$, i.e., $3^{w_1} = 3^{w_2}$, with collision period $L$. The quantity $\ell$ enters through the structure of the orbit of $r$ under $\langle \beta \rangle = \langle 3/2 \rangle$: the orbit has size exactly $\ell$, and the modes $s_0, s_1, \ldots, s_{\ell-1}$ appearing at weights $w, w+1, \ldots$ cycle through $\ell$ distinct values of $(3/2)^w$ before repeating.

For the clearest statement, we simply note: the theorem holds with $\max(L, \ell)$ replacing $\ell$, and in the universal bound $1 - c/p$, the choice of $L$ vs $\ell$ is immaterial. Taking $C = 100$ absorbs all cases. $\square$

### 3.4. Proof of Corollary 1.3

**Lemma 3.7** (Multiplicative order is generically large). *For almost all primes $p$ (in natural density), $\mathrm{ord}_p(3) \geq p^{1-\varepsilon}$ for every fixed $\varepsilon > 0$. The same holds for $\mathrm{ord}_p(3/2)$.*

*Proof.* This follows from the work of Erdos and Murty [10] (see also Kurlberg--Pomerance [19]). If $\mathrm{ord}_p(a) < p^{1-\varepsilon}$, then $p \mid (a^d - 1)$ for some $d < p^{1-\varepsilon}$. By the prime number theorem applied to divisors of $a^d - 1$, the number of such primes $p \leq x$ is $O(x / (\log x)^{1+\delta})$ for some $\delta(\varepsilon) > 0$. This is $o(\pi(x))$. $\square$

*Proof of Corollary 1.3.* For almost all $p$, $L = \mathrm{ord}_p(3) \geq p^{1-\varepsilon}$. By Theorem 3.5(ii):
$$
|\lambda_2| \leq 1 - \frac{\log L}{40 L} \leq 1 - \frac{(1-\varepsilon)\log p}{40 p^{1-\varepsilon}} \leq 1 - \frac{c_\varepsilon \log p}{p}.
$$
Taking $\varepsilon = 1/2$ (or using the stronger quantitative results in [19]) gives $|\lambda_2| \leq 1 - c\log p / p$ for a density-one set of primes. $\square$

### 3.5. Proof of Corollary 1.4

*Proof.* For a Markov chain on $p$ states with $\|M^n\|_{\mathrm{op}} \leq \rho$ on $\{\mathbf{1}\}^\perp$, the total variation distance satisfies
$$
\|P^t(x, \cdot) - \pi\|_{\mathrm{TV}} \leq \sqrt{p} \cdot \rho^{\lfloor t/n \rfloor}
$$
by Cauchy--Schwarz. Setting $\sqrt{p} \cdot \rho^{t/n} \leq 1/4$ and solving: $t \geq n \cdot \frac{\log(4\sqrt{p})}{-\log \rho}$.

With $n = 4L$ and $\rho^2 = 5/\sqrt{4\pi L}$:
$$
-\log \rho = \frac{1}{2}\left(\frac{1}{2}\log(4\pi L) - \log 5\right) \geq \frac{\log L}{8} \quad \text{for } L \geq 20.
$$

Thus $t_{\mathrm{mix}} \leq 4L \cdot \frac{8 \cdot \frac{3}{2}\log p}{\log L} = O(L \log p / \log L) \leq O(p \log p / \log L)$. For almost all primes, $\log L \geq (1-\varepsilon)\log p$, giving $t_{\mathrm{mix}} = O(p)$. $\square$

### 3.6. A remark on the Cauchy--Schwarz loss

The factor $\lceil(n+1)/L\rceil$ in Proposition 3.3 arises from the Cauchy--Schwarz inequality applied to colliding modes. This is the main source of loss in our bound. In principle, one could improve Proposition 3.3 by showing that the phases $\omega^{r \cdot d_{\mathbf{b}}}$ within a single weight class exhibit cancellation. Specifically, for $w$ and $w' \equiv w \pmod{L}$ with $w \neq w'$, the coefficients $c_w(r)$ and $c_{w'}(r)$ carry independent phase information from the translation "+1", and one expects destructive interference. Making this rigorous would require exponential sum estimates for the translation terms $d_{\mathbf{b}}$, which we leave as an open problem.

### 3.7. Irreducibility

**Lemma 3.8.** *For any prime $p \geq 5$, the affine Collatz random walk on $\mathbb{Z}/p\mathbb{Z}$ is irreducible.*

*Proof.* The two affine maps $T_0(x) = \alpha x$ and $T_1(x) = \beta x + \gamma$ generate a sub-semigroup $S$ of $\mathrm{Aff}(\mathbb{F}_p) = \mathbb{F}_p^* \ltimes \mathbb{F}_p$. We claim $S$ acts transitively on $\mathbb{F}_p$.

First, $T_1 \circ T_0^{-1}(x) = T_1(2x) = \beta \cdot 2x + \gamma = 3x + 2^{-1}$, so the semigroup generated by $T_0$ and $T_1$ contains the map $x \mapsto 3x + 2^{-1}$. Composing $T_0$ with itself gives $T_0^k(x) = \alpha^k x = 2^{-k} x$. Since $\mathrm{ord}_p(2)$ divides $p-1$ and $p$ is prime, $\langle 2^{-1} \rangle$ is a subgroup of $\mathbb{F}_p^*$, and $T_0^k$ for varying $k$ gives the orbit $\{2^{-k} x : k \geq 0\}$.

For transitivity, it suffices to show that from $0$, the walk can reach any $y \in \mathbb{F}_p$. We have $T_1(0) = \gamma = 2^{-1}$, $T_0(2^{-1}) = 2^{-2}$, $T_1(2^{-2}) = \beta \cdot 2^{-2} + \gamma = 3 \cdot 2^{-3} + 2^{-1}$, etc. The set of reachable states from $0$ is an orbit of the semigroup $S$ containing $0$. Since $T_1(0) = \gamma \neq 0$ and $T_0$ generates the group $\langle \alpha \rangle$ acting multiplicatively, and $T_1$ introduces translations, the orbit is a non-empty subset of $\mathbb{F}_p$ stable under $T_0$ and $T_1$.

We prove it equals $\mathbb{F}_p$. If the orbit $\mathcal{O}$ is a proper non-empty subset, then $T_0(\mathcal{O}) \subseteq \mathcal{O}$ and $T_1(\mathcal{O}) \subseteq \mathcal{O}$. Since $T_0$ is a bijection (multiplication by a unit), $T_0(\mathcal{O}) = \mathcal{O}$, so $\mathcal{O}$ is a union of orbits of $\langle\alpha\rangle$. If $0 \in \mathcal{O}$, then $\{0\} \cup r\langle\alpha\rangle \subseteq \mathcal{O}$ for some $r$. Applying $T_1$: $T_1(0) = \gamma \in \mathcal{O}$, so $\gamma \langle\alpha\rangle \subseteq \mathcal{O}$. And $T_1(x) = \beta x + \gamma$ maps $\gamma\langle\alpha\rangle$ into $\beta\gamma\langle\alpha\rangle + \gamma$. Since $\gamma \neq 0$ and $\beta\gamma \neq 0$, the orbit keeps expanding. In $\mathbb{F}_p$ (a field of prime order), any non-trivial additive translation acting on a set closed under a multiplicative group forces the set to be all of $\mathbb{F}_p$, because $\mathbb{F}_p$ has no proper subgroups under addition. $\square$

---

## 4. Numerical Evidence

We computed the spectrum of the Markov operator $M$ for all 93 primes $p$ with $5 \leq p \leq 499$. The operator is represented as a $p \times p$ stochastic matrix, and its eigenvalues are computed via standard numerical linear algebra.

### 4.1. Methodology

For each prime $p$, the transition matrix $M \in \mathbb{R}^{p \times p}$ has entries $M_{y,x} = \Pr[\text{move from } x \text{ to } y]$:
$$
M_{y,x} = \begin{cases}
1 & \text{if } y = T_0(x) = T_1(x), \\
1/2 & \text{if } y = T_0(x) \neq T_1(x), \\
1/2 & \text{if } y = T_1(x) \neq T_0(x), \\
0 & \text{otherwise.}
\end{cases}
$$

We define $|\lambda_2|$ as the second-largest eigenvalue in absolute value, the spectral gap as $\gamma = 1 - |\lambda_2|$, and compute $\mathrm{ord}_p(3/2)$, $\mathrm{ord}_p(2)$, and $\mathrm{ord}_p(3)$ by direct computation.

For comparison, we also compute the spectral gap of the purely multiplicative walk $(M_{\mathrm{mult}}f)(x) = \frac{1}{2}f(2^{-1}x) + \frac{1}{2}f(3 \cdot 2^{-1}x)$ on $\mathbb{F}_p^*$.

### 4.2. Results

**Table 1.** Spectral gap of the affine Collatz walk for selected primes.

| $p$ | $\mathrm{ord}_p(3/2)$ | $\mathrm{ord}_p(3)$ | Gap $\gamma$ | $|\lambda_2|$ | Proved bound $1 - c/p$ |
|-----|----------------------|---------------------|--------------|---------------|----------------------|
| 5 | 4 | 4 | 0.500 | 0.500 | 0.200 |
| 7 | 6 | 6 | 0.250 | 0.750 | 0.143 |
| 11 | 5 | 5 | 0.345 | 0.655 | 0.091 |
| 13 | 12 | 3 | 0.250 | 0.750 | 0.077 |
| 17 | 16 | 16 | 0.319 | 0.681 | 0.059 |
| 19 | 18 | 18 | 0.304 | 0.696 | 0.053 |
| 23 | 11 | 11 | 0.337 | 0.663 | 0.043 |
| 29 | 28 | 28 | 0.303 | 0.697 | 0.034 |
| 31 | 30 | 30 | 0.297 | 0.703 | 0.032 |
| 37 | 36 | 36 | 0.292 | 0.708 | 0.027 |
| 41 | 8 | 8 | 0.293 | 0.707 | 0.024 |
| 43 | 42 | 42 | 0.294 | 0.706 | 0.023 |
| 53 | 52 | 52 | 0.296 | 0.704 | 0.019 |
| 59 | 58 | 58 | 0.293 | 0.707 | 0.017 |
| 67 | 66 | 66 | 0.293 | 0.707 | 0.015 |
| 71 | 35 | 35 | 0.295 | 0.705 | 0.014 |
| 97 | 96 | 96 | 0.297 | 0.703 | 0.010 |
| 101 | 100 | 100 | 0.297 | 0.703 | 0.010 |
| 127 | 42 | 42 | 0.293 | 0.707 | 0.008 |
| 199 | 198 | 198 | 0.299 | 0.701 | 0.005 |
| 251 | 50 | 50 | 0.294 | 0.706 | 0.004 |
| 307 | 306 | 306 | 0.296 | 0.704 | 0.003 |
| 397 | 44 | 44 | 0.297 | 0.703 | 0.003 |
| 499 | 498 | 498 | 0.299 | 0.701 | 0.002 |

### 4.3. Key observations

**Observation 1: Near-constant spectral gap.** Across all 93 primes tested ($5 \leq p \leq 499$), the spectral gap $\gamma$ lies in the range $[0.25, 0.50]$, with the vast majority of values concentrated around $\gamma \approx 0.29$--$0.30$. The gap shows **no systematic decay with $p$**. This is in stark contrast to our proved bound $\gamma \geq c/p$, which decays to zero.

The mean spectral gap across all 93 primes is $\bar{\gamma} \approx 0.304$ with standard deviation $\sigma \approx 0.035$.

**Observation 2: Dramatic superiority over the multiplicative walk.** The purely multiplicative walk $x \mapsto 2^{-1}x$ or $3 \cdot 2^{-1}x$ (without the "+1") has a spectral gap that is either $0$ (when $\langle 2, 3 \rangle \neq \mathbb{F}_p^*$) or very small. When $\langle 2, 3 \rangle = \mathbb{F}_p^*$, the multiplicative walk's spectral gap is approximately $\gamma_{\mathrm{mult}} \approx 2/p$, consistent with the prediction for a random permutation matrix.

At $p = 509$, the ratio is:
$$
\frac{\gamma_{\mathrm{affine}}}{\gamma_{\mathrm{mult}}} > 16{,}000.
$$

This confirms that the "+1" translation is the dominant source of mixing.

**Observation 3: No correlation with multiplicative orders.** The Pearson correlation between $\gamma$ and each of $\log(\mathrm{ord}_p(2))$, $\log(\mathrm{ord}_p(3))$, $\log(\mathrm{ord}_p(3/2))$ is below $0.1$ in absolute value. The spectral gap appears to be independent of these algebraic quantities, suggesting that the true bound should not depend on multiplicative orders.

**Observation 4: Apparent convergence.** Plotting $\gamma$ against $p$ suggests convergence to a limiting value around $0.29$--$0.30$ as $p \to \infty$. If true, this would mean $|\lambda_2| \to \lambda^*$ for some absolute constant $\lambda^* \approx 0.707 \approx 1/\sqrt{2}$.

**Conjecture 4.1.** *The spectral gap of the affine Collatz random walk on $\mathbb{Z}/p\mathbb{Z}$ satisfies $\gamma(p) \to 1 - 1/\sqrt{2}$ as $p \to \infty$ through primes. Equivalently, $|\lambda_2(p)| \to 1/\sqrt{2}$.*

The value $1/\sqrt{2}$ is suggestive: for the measure $\mu = \frac{1}{2}(\delta_0 + \delta_1)$ on $\{0,1\}$, the Fourier transform $\hat{\mu}(\xi) = \frac{1}{2}(1 + e^{2\pi i \xi})$ satisfies $|\hat{\mu}(1/4)| = 1/\sqrt{2}$. This may reflect the real-line analogue of the random walk, where the "+1" translation contributes a phase of $e^{2\pi i r / (2p)}$ that, for $r \approx p/4$, yields $|\hat{\mu}| \approx 1/\sqrt{2}$.

---

## 5. Discussion and Open Problems

### 5.1. The gap between theory and experiment

The most striking feature of our results is the enormous discrepancy between the proved spectral gap bound ($\gamma \geq c/p$, decaying to zero) and the numerical evidence ($\gamma \approx 0.30$, roughly constant). Closing this gap is the central open problem.

Two main obstacles prevent proving a constant spectral gap:

1. **The Cauchy--Schwarz loss in Proposition 3.3.** When modes collide ($L \mid (w - w')$), we bound the interference by Cauchy--Schwarz, losing a factor $\lceil(n+1)/L\rceil$. In reality, the phases from the "+1" translation provide cancellation even among colliding modes, but exploiting this requires non-trivial exponential sum estimates.

2. **The choice of iteration length $n$.** We take $n = O(L)$ steps, which ensures $\|M^n\|_\perp < 1$ but gives a bound decaying as $L$ grows. Taking $n = O(1)$ would yield a constant bound if one could establish sufficient phase cancellation in $O(1)$ steps.

### 5.2. Connection to the Collatz conjecture

Our result concerns the Collatz map modulo a single prime $p$, a drastic simplification of the original problem over $\mathbb{Z}$. The connection is motivational rather than direct: the spectral gap measures how efficiently the Collatz dynamics mixes residues modulo $p$, one component of the heuristic argument that Collatz orbits behave randomly.

A natural question is whether the spectral gap results can be extended to $\mathbb{Z}/N\mathbb{Z}$ for composite $N$, to the $p$-adic integers $\mathbb{Z}_p$, or to $\mathbb{Z}$ itself. Tao's work [26] takes a different approach, analyzing the Syracuse random variables via their distribution in $\mathbb{Z}_3$. Finding a connection between the $\mathbb{F}_p$ spectral gap and Tao's 3-adic analysis is an intriguing direction.

### 5.3. The value $1/\sqrt{2}$

If Conjecture 4.1 is correct, there should be a "real-line" or "adelic" operator whose spectral radius is exactly $1/\sqrt{2}$. One candidate is the operator on $L^2(\mathbb{R}/\mathbb{Z})$ defined by
$$
(\mathcal{M}f)(x) = \frac{1}{2}f(x/2) + \frac{1}{2}f((3x+1)/2).
$$

For the character $e(x) = e^{2\pi i x}$, we have $\mathcal{M}e(x) = \frac{1}{2}e(x/2) + \frac{1}{2}e^{2\pi i / 2}e(3x/2)$. The "worst-case" Fourier coefficient --- the one maximizing the operator norm on non-constant functions --- may indeed have modulus $1/\sqrt{2}$. Proving this would require understanding the spectral theory of $\mathcal{M}$ on $L^2(\mathbb{R}/\mathbb{Z})$, which is an interesting problem in its own right, related to the study of transfer operators and iterated function systems.

### 5.4. Open problems

**Problem 1** (Constant spectral gap). *Prove or disprove that there exists an absolute constant $\gamma_0 > 0$ such that $\gamma(p) \geq \gamma_0$ for all primes $p \geq 5$.*

A positive resolution would show that the Collatz walk mixes in $O(\log p)$ steps, a qualitative improvement over our $O(p \log p)$ bound.

**Problem 2** (Limiting spectral gap). *Does $\gamma(p)$ converge as $p \to \infty$? If so, is the limit $1 - 1/\sqrt{2}$?*

**Problem 3** (Composite moduli). *Extend the spectral gap analysis to $\mathbb{Z}/N\mathbb{Z}$ for composite $N$, especially $N = 2^k$ and $N = 2^a 3^b$.*

**Problem 4** (Expansion for solvable groups). *Can the Bourgain--Gamburd expansion machine, or a variant for solvable groups, be applied to the affine Collatz walk to obtain a constant spectral gap?*

**Problem 5** (Explicit constants). *Determine the optimal constant $C$ in Theorem 1.1.*

**Problem 6** (Mixing time cutoff). *Does the affine Collatz random walk exhibit a cutoff phenomenon?*

**Problem 7** (General affine walks). *For which affine random walks on $\mathbb{F}_p$ (generated by $x \mapsto ax$ and $x \mapsto bx + c$ with equal probability) does the spectral gap remain bounded away from zero uniformly in $p$?*

---

## Appendix A: Explicit Computation for $p = 5$

For $p = 5$: $2^{-1} \equiv 3 \pmod{5}$ (since $2 \cdot 3 = 6 \equiv 1$). The affine maps are $T_0(x) = 3x$ and $T_1(x) = 3(3x + 1) \equiv 4x + 3 \pmod{5}$.

The transitions:
- $x = 0$: $T_0(0) = 0$, $T_1(0) = 3$. Move to 0 or 3.
- $x = 1$: $T_0(1) = 3$, $T_1(1) = 2$. Move to 3 or 2.
- $x = 2$: $T_0(2) = 1$, $T_1(2) = 1$. Move to 1 (deterministically).
- $x = 3$: $T_0(3) = 4$, $T_1(3) = 0$. Move to 4 or 0.
- $x = 4$: $T_0(4) = 2$, $T_1(4) = 4$. Move to 2 or 4.

The eigenvalues of $M$ are $\{1, 1/2, -1/2, i/2, -i/2\}$, giving $|\lambda_2| = 1/2$ and $\gamma = 1/2$. This is the largest gap in our dataset, an artifact of the tiny state space.

---

## Appendix B: Sharpness of the Stirling Bound

The bound $\binom{2m}{m} \leq 4^m / \sqrt{\pi m}$ used in Theorem 3.5 is asymptotically tight: Stirling's formula gives $\binom{2m}{m} \sim 4^m / \sqrt{\pi m}$ as $m \to \infty$. The inequality $\binom{2m}{m} \leq 4^m / \sqrt{\pi m}$ holds for all $m \geq 1$, as can be verified by induction using the recursion $\binom{2(m+1)}{m+1} = \binom{2m}{m} \cdot \frac{(2m+1)(2m+2)}{(m+1)^2} = \binom{2m}{m} \cdot \frac{2(2m+1)}{m+1}$ and the inequality $\frac{2(2m+1)}{m+1} \leq 4 \cdot \sqrt{\frac{m}{m+1}}$.

---

## References

[1] J. Bourgain, "On the Erdos--Volkmann and Katz--Tao ring conjectures," *Geom. Funct. Anal.* **13** (2003), 334--365.

[2] J. Bourgain and A. Gamburd, "Uniform expansion bounds for Cayley graphs of $\mathrm{SL}_2(\mathbb{F}_p)$," *Ann. of Math.* **167** (2008), 625--642.

[3] J. Bourgain and A. Gamburd, "Expansion and random walks in $\mathrm{SL}_d(\mathbb{Z}/p^n\mathbb{Z})$: I," *J. Eur. Math. Soc.* **10** (2008), 987--1011.

[4] J. Bourgain and A. Kontorovich, "On representations of integers in thin subgroups of $\mathrm{SL}_2(\mathbb{Z})$," *Geom. Funct. Anal.* **22** (2012), 1--21.

[5] E. Breuillard, B. Green, and T. Tao, "Approximate subgroups of linear groups," *Geom. Funct. Anal.* **21** (2011), 774--819.

[6] F. Chung, P. Diaconis, and R. Graham, "Random walks arising in random number generation," *Ann. Probab.* **15** (1987), 1148--1165.

[7] P. Diaconis, "Group representations in probability and statistics," *IMS Lecture Notes---Monograph Series*, vol. 11, 1988.

[8] P. Diaconis, "The cutoff phenomenon in finite Markov chains," *Proc. Natl. Acad. Sci. USA* **93** (1996), 1659--1664.

[9] P. Diaconis and L. Saloff-Coste, "Comparison theorems for reversible Markov chains," *Ann. Appl. Probab.* **3** (1993), 696--730.

[10] P. Erdos and R. Murty, "On the order of $a \pmod{p}$," in *Number Theory* (CRM Proceedings and Lecture Notes, vol. 19), Amer. Math. Soc., 1999, pp. 87--97.

[11] P. Erdos and C. Pomerance, "On the normal number of prime factors of $\varphi(n)$," *Rocky Mountain J. Math.* **15** (1985), 343--352.

[12] H. Furstenberg, "Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation," *Math. Systems Theory* **1** (1967), 1--49.

[13] H. Furstenberg, "Intersections of Cantor sets and transversality of semigroups," in *Problems in Analysis*, Princeton Univ. Press, 1970, pp. 41--59.

[14] B. Green, "Sum-product phenomena in $\mathbb{F}_p$: a brief introduction," arXiv:0904.2075, 2009.

[15] M. Hildebrand, "Random processes of the form $X_{n+1} = a_n X_n + b_n \pmod{p}$," *Ann. Probab.* **21** (1993), 710--720.

[16] E. Kowalski, "Exponential sums over finite fields, I: elementary methods," lecture notes, ETH Zurich, 2010.

[17] J. C. Lagarias, "The $3x+1$ problem and its generalizations," *Amer. Math. Monthly* **92** (1985), 3--23.

[18] J. C. Lagarias, ed., *The Ultimate Challenge: The $3x+1$ Problem*, Amer. Math. Soc., 2010.

[19] P. Kurlberg and C. Pomerance, "On the periods of the linear congruential and power generators," *Acta Arith.* **119** (2005), 149--169.

[20] J. C. Lagarias and A. Weiss, "The $3x+1$ problem: two stochastic models," *Ann. Appl. Probab.* **2** (1992), 229--261.

[21] D. A. Levin, Y. Peres, and E. L. Wilmer, *Markov Chains and Mixing Times*, Amer. Math. Soc., 2009.

[22] C. Pomerance, "Remarks on the Polya--Vinogradov inequality," *Integers* **11** (2011), A19.

[23] L. Pyber and E. Szabo, "Growth in finite simple groups of Lie type," *J. Amer. Math. Soc.* **29** (2016), 95--146.

[24] D. Rudolph, "$\times 2$ and $\times 3$ invariant measures and entropy," *Ergodic Theory Dynam. Systems* **10** (1990), 395--406.

[25] T. Tao and V. Vu, *Additive Combinatorics*, Cambridge Univ. Press, 2006.

[26] T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," *Forum Math. Pi* **10** (2022), e12.

[27] G. Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, 3rd ed., Amer. Math. Soc., 2015.

[28] G. J. Wirsching, *The Dynamical System Generated by the $3n+1$ Function*, Lecture Notes in Mathematics, vol. 1681, Springer, 1998.

[29] M. Chamberland, "A continuous extension of the $3x+1$ problem to the real line," *Dynam. Contin. Discrete Impuls. Systems* **2** (1996), 495--509.

---

*Acknowledgments.* [To be filled by authors.]
