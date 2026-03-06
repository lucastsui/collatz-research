# Direction 0B: Arithmetic Intersection Theory on R = Z[x]/(x^p - 3^k)

*Developed 2026-03-06 (Session 6)*

## 0. Goal

Prove that no structured coefficient vector $c_I$ lies in the sublattice $(x-2)R$ of covolume $D = 2^p - 3^k$, using height-theoretic methods on the order $R = \mathbb{Z}[x]/(x^p - 3^k)$.

The key insight to exploit: $c_I$ is **sparse** (exactly $k$ nonzero entries out of $p$) with entries that are **descending powers of 3**. A height function that "sees" this sparsity/geometric structure could prove incompatibility with membership in $(x-2)R$.

---

## 1. The Ring R and Its Geometry

### 1.1. Basic Structure

$R = \mathbb{Z}[x]/(x^p - 3^k)$ is a free $\mathbb{Z}$-module of rank $p$ with basis $\{1, x, x^2, \ldots, x^{p-1}\}$.

$R$ is an order in the number field $K = \mathbb{Q}(\alpha)$ where $\alpha = 3^{k/p}$ (the real $p$-th root of $3^k$). Note: $x^p - 3^k$ is irreducible over $\mathbb{Q}$ when $\gcd(p, k) = 1$ (Eisenstein at $p = 3$ doesn't directly apply, but irreducibility follows from the fact that $3^{k/p}$ has degree $p$ over $\mathbb{Q}$ when $\gcd(p,k) = 1$, which holds for all valid Collatz pairs since $p/k \approx \log 3/\log 2$ is irrational).

When $\gcd(p,k) = d > 1$: $x^p - 3^k = (x^{p/d})^d - (3^{k/d})^d$, which factors. In this case $R$ is not a domain. For the Collatz problem, $k/p \approx \log 2/\log 3$, so $\gcd(p,k) = 1$ for all valid pairs with large $p$ (since $\log 2/\log 3$ is irrational). We assume $\gcd(p,k) = 1$ henceforth.

### 1.2. Embeddings

$K = \mathbb{Q}(\alpha)$ has $p$ embeddings into $\mathbb{C}$:
$$\sigma_m : \alpha \mapsto \zeta^m \cdot 3^{k/p}, \qquad m = 0, 1, \ldots, p-1$$
where $\zeta = e^{2\pi i/p}$.

- One real embedding: $\sigma_0(\alpha) = 3^{k/p} \approx 2$ (since $k/p \approx \log 2/\log 3$).
- $(p-1)/2$ pairs of complex embeddings: $\sigma_m, \overline{\sigma_m} = \sigma_{p-m}$.

For $f = \sum_{r=0}^{p-1} a_r x^r \in R$, the image under $\sigma_m$ is:
$$\sigma_m(f) = \sum_{r=0}^{p-1} a_r \cdot \zeta^{mr} \cdot 3^{kr/p}$$

### 1.3. The Minkowski Embedding

The Minkowski embedding $\Phi: R \hookrightarrow \mathbb{R}^p$ sends $f \mapsto (\sigma_0(f), \mathrm{Re}\,\sigma_1(f), \mathrm{Im}\,\sigma_1(f), \ldots)$.

The image is a full-rank lattice $\Lambda_R \subset \mathbb{R}^p$ with covolume:
$$\mathrm{covol}(\Lambda_R) = \frac{1}{2^{(p-1)/2}} |d_K|^{1/2} \cdot [\mathcal{O}_K : R]$$
where $d_K$ is the discriminant of $K$ and $\mathcal{O}_K$ is the maximal order.

The sublattice $(x-2)R$ maps to $\Lambda_{(x-2)R}$ with:
$$[\Lambda_R : \Lambda_{(x-2)R}] = |N_{K/\mathbb{Q}}(\alpha - 2)| = |\alpha^p - 2^p|_{x=\alpha}$$

Wait — we need to be more careful. In $R$, multiplication by $(x-2)$ has norm:
$$N_{R/\mathbb{Z}}(x-2) = \prod_{m=0}^{p-1} (\zeta^m \cdot 3^{k/p} - 2) = \mathrm{Res}(x-2, x^p - 3^k) = 2^p - 3^k = D$$

So $[\Lambda_R : \Lambda_{(x-2)R}] = D$. Correct.

---

## 2. Heights on R

### 2.1. The Canonical Height

For $f \in R$, define the **archimedean height**:
$$h_\infty(f) = \frac{1}{p} \sum_{m=0}^{p-1} \log|\sigma_m(f)|$$

This is the logarithmic Mahler measure of $f$ relative to the number field $K$.

By the product formula, for $f \in R \setminus \{0\}$:
$$h_\infty(f) = \frac{1}{p} \log |N_{K/\mathbb{Q}}(f)| - \frac{1}{p} \sum_{\mathfrak{p}} v_\mathfrak{p}(f) \log N\mathfrak{p}$$

### 2.2. The Structured Height

For the Collatz problem, we need a height that captures the **sparsity** of $c_I$.

**Definition.** For $f = \sum_{r=0}^{p-1} a_r x^r \in R$, define:
$$H_{\mathrm{sparse}}(f) = \#\{r : a_r \neq 0\}$$
(the support size, or Hamming weight of the coefficient vector).

For the Collatz vector $F_I(x) = \sum_{r \in I} 3^{s_{r+1}} x^r$:
$$H_{\mathrm{sparse}}(F_I) = k$$

### 2.3. The Key Height Inequality (TARGET)

**Target Theorem (0B).** There exists a function $h^*: R \to \mathbb{R}$ such that:
1. For all $f \in (x-2)R$ with $f \neq 0$: $h^*(f) \geq \phi(D)$ for some function $\phi$ with $\phi(D) \to \infty$.
2. For all structured vectors $F_I$: $h^*(F_I) \leq \psi(p,k)$ for some function $\psi$.
3. $\phi(D) > \psi(p,k)$ for all valid $(p,k)$ with $p$ large.

If such $h^*$ exists, then $F_I \notin (x-2)R$, proving Part 1.

---

## 3. Height of Elements in (x-2)R

### 3.1. Lower Bound via Norm

If $f = (x-2) \cdot g$ for $g \in R$, then:
$$N_{K/\mathbb{Q}}(f) = N_{K/\mathbb{Q}}(x-2) \cdot N_{K/\mathbb{Q}}(g) = D \cdot N_{K/\mathbb{Q}}(g)$$

Since $g \in R \setminus \{0\}$ implies $N_{K/\mathbb{Q}}(g) \in \mathbb{Z} \setminus \{0\}$, we get:
$$|N_{K/\mathbb{Q}}(f)| \geq D$$

In terms of height:
$$h_\infty(f) = \frac{1}{p} \log|N_{K/\mathbb{Q}}(f)| \geq \frac{1}{p} \log D \approx \frac{p - k \log_2 3}{p} \log 2 \approx 0.05 \log 2 \approx 0.035$$

This gives a **constant** lower bound on $h_\infty(f)$ for $f \in (x-2)R$.

### 3.2. Upper Bound for F_I

$$|N_{K/\mathbb{Q}}(F_I)| = \prod_{m=0}^{p-1} |\sigma_m(F_I)|$$

Each $\sigma_m(F_I) = \sum_{r \in I} 3^{s_{r+1}} \cdot \zeta^{mr} \cdot 3^{kr/p}$.

For $m = 0$: $\sigma_0(F_I) = \sum_{r \in I} 3^{s_{r+1}} \cdot 3^{kr/p} = S(I) / 2^{i_1}$ (approximately, up to the substitution $\alpha = 3^{k/p} \approx 2$).

Actually, $\sigma_0(F_I) = F_I(3^{k/p}) = \sum_{r \in I} 3^{s_{r+1}} \cdot 3^{kr/p}$. Since $s_{r+1}$ counts the number of elements of $I$ strictly above $r$, this is $\sum_{j=0}^{k-1} 3^{k-1-j} \cdot 3^{ki_{j+1}/p}$. Note $3^{k/p} \approx 2$, so $\sigma_0(F_I) \approx S(I) = \sum 3^{k-1-j} \cdot 2^{i_{j+1}}$.

For the height:
$$h_\infty(F_I) = \frac{1}{p} \sum_{m=0}^{p-1} \log|\sigma_m(F_I)|$$

**Upper bound:** By Jensen's inequality and the triangle inequality:
$$|\sigma_m(F_I)| \leq \sum_{r \in I} 3^{s_{r+1}} \cdot 3^{kr/p} \leq k \cdot 3^{k-1} \cdot 3^{k(p-1)/p} < k \cdot 3^{2k}$$

So $h_\infty(F_I) \leq \log(k \cdot 3^{2k}) = \log k + 2k \log 3 \approx 2k \log 3 \approx 1.26p$.

This is too weak: the lower bound $0.035$ is dwarfed by the upper bound $1.26p$.

### 3.3. The Norm Approach Fails

The norm $|N(f)| \geq D$ for $f \in (x-2)R$ gives only:
$$h_\infty(f) \geq \frac{\log D}{p} \approx 0.035$$

But $F_I$ has $h_\infty(F_I) \gg 1$, so this cannot exclude $F_I$ from $(x-2)R$.

**Diagnosis:** The norm is too coarse. It captures the SIZE of $f$ but not its STRUCTURE. A generic element of $(x-2)R$ with norm $\geq D$ can have very large archimedean height (just multiply by a large $g$). The height inequality goes in the wrong direction.

---

## 4. Refined Height: The Quotient Height

### 4.1. Setup

If $F_I = (x-2) \cdot Q_I$ in $R$, then $Q_I$ is the certificate sequence from the global lattice reformulation (agent_global_lattice.md, Section 4).

The key constraint is on $Q_I$, not on $F_I$. Specifically:
- $Q_I$ has all negative coefficients (Proposition 4.1 in agent_global_lattice.md)
- $q_{p-1} = -n$ where $n = S(I)/D$
- The differences $q_{r-1} - 2q_r$ follow the specific pattern $\{0, 1, 3, 9, \ldots, 3^{k-1}\}$

### 4.2. Height of Q_I

Since $F_I = (x-2) Q_I$:
$$h_\infty(F_I) = h_\infty(x-2) + h_\infty(Q_I) + \text{error}$$
(the "error" is from the fact that $h_\infty$ is not exactly additive for non-unit elements in a non-UFD).

More precisely:
$$\frac{1}{p} \log|N(F_I)| = \frac{1}{p} \log D + \frac{1}{p} \log|N(Q_I)|$$

So:
$$\frac{1}{p} \log|N(Q_I)| = \frac{1}{p} \log|N(F_I)| - \frac{1}{p} \log D$$

### 4.3. Bounding N(Q_I) from the Certificate Structure

The certificate $Q_I$ has coefficients $q_0, \ldots, q_{p-1}$ all negative, with $q_{p-1} = -n$.

From the recurrence $q_{r-1} = 2q_r + c_r$ (where $c_r \in \{0, 3^{k-1}, 3^{k-2}, \ldots, 1\}$):
$$|q_r| \approx n \cdot 2^{p-1-r} - \sum_{m=r+1}^{p-1} c_m \cdot 2^{m-r-1}$$

The largest coefficient is $|q_0| \approx n \cdot 2^{p-1}$.

The norm $|N(Q_I)| = \prod_m |\sigma_m(Q_I)|$.

For $m = 0$: $\sigma_0(Q_I) = Q_I(3^{k/p}) \approx Q_I(2)$. But $F_I(2) = S(I) = nD$, and $F_I(x) = (x-2)Q_I(x)$, so... $F_I(2) = 0 \cdot Q_I(2)$. This is a problem — the evaluation at $x = 2$ is degenerate because $(x-2)$ vanishes there.

Wait: $\sigma_0(\alpha) = 3^{k/p} \neq 2$ (they're close but not equal, since $3^{k/p} \neq 2$ for $k/p$ irrational). So:

$$\sigma_0(F_I) = (\sigma_0(\alpha) - 2) \cdot \sigma_0(Q_I) = (3^{k/p} - 2) \cdot \sigma_0(Q_I)$$

Since $3^{k/p} \approx 2$ with $3^{k/p} - 2 \approx (k \log 3 - p \log 2) \cdot 2/p \approx \log(D/\text{power}) / p$... Let me be more precise.

$3^{k/p} = 2 \cdot 3^{k/p}/2 = 2 \cdot \exp((k \log 3 - p \log 2)/p) = 2(1 + (k \log 3 - p \log 2)/p + O(1/p^2))$.

Now $k \log 3 - p \log 2 = \log(3^k/2^p) = \log(1 - D/2^p) \approx -D/2^p$ for $D \ll 2^p$.

So $3^{k/p} - 2 \approx -2D/(p \cdot 2^p) = -D/(p \cdot 2^{p-1})$.

This is exponentially small! $|3^{k/p} - 2| \approx D/p 2^{p-1}$.

For $m \neq 0$: $|\sigma_m(\alpha) - 2| = |\zeta^m \cdot 3^{k/p} - 2|$. Since $|\zeta^m \cdot 3^{k/p}| \approx 2$ and $\zeta^m \neq 1$, this is $\approx 2|1 - \zeta^m| \approx 4\pi m/p$ (for small $m$). So these are $O(1)$, not small.

### 4.4. The Archimedean Asymmetry

The product $\prod_{m=0}^{p-1} |\sigma_m(\alpha) - 2| = |N_{K/\mathbb{Q}}(\alpha - 2)| = D$.

But the factors are wildly asymmetric:
- $|\sigma_0(\alpha) - 2| \approx D/(p \cdot 2^{p-1})$ (exponentially small)
- $|\sigma_m(\alpha) - 2| \approx |2\zeta^m - 2| = 2|1-\zeta^m| \approx 4\sin(\pi m/p)$ for $m \neq 0$

Product of the $m \neq 0$ factors:
$$\prod_{m=1}^{p-1} |\zeta^m \cdot 3^{k/p} - 2| \approx \prod_{m=1}^{p-1} 2|1 - \zeta^m| \cdot (3^{k/p}/2)^? $$

Actually: $\prod_{m=0}^{p-1} (x - \zeta^m \cdot 3^{k/p}) = x^p - 3^k$. Setting $x = 2$: $\prod_{m=0}^{p-1} (2 - \zeta^m \cdot 3^{k/p}) = 2^p - 3^k = D$.

So $\prod_{m=1}^{p-1} |2 - \zeta^m \cdot 3^{k/p}| = D / |2 - 3^{k/p}| \approx D / (D/(p \cdot 2^{p-1})) = p \cdot 2^{p-1}$.

This means the "non-degenerate" embeddings of $(x-2)$ have product $\approx p \cdot 2^{p-1}$, exponentially large. The single "near-degenerate" embedding $\sigma_0$ has value $\approx D/(p \cdot 2^{p-1})$, exponentially small.

### 4.5. Consequences for $Q_I$

From $\sigma_m(F_I) = \sigma_m(x-2) \cdot \sigma_m(Q_I)$:

$$\sigma_m(Q_I) = \frac{\sigma_m(F_I)}{\sigma_m(x-2)}$$

For $m = 0$:
$$\sigma_0(Q_I) = \frac{\sigma_0(F_I)}{3^{k/p} - 2} \approx \frac{S(I)}{D/(p \cdot 2^{p-1})} = \frac{nD \cdot p \cdot 2^{p-1}}{D} = n \cdot p \cdot 2^{p-1}$$

So $|\sigma_0(Q_I)| \approx n \cdot p \cdot 2^{p-1}$ — exponentially large.

For $m \neq 0$:
$$|\sigma_m(Q_I)| = \frac{|\sigma_m(F_I)|}{|\sigma_m(x-2)|}$$

$|\sigma_m(F_I)| = |\sum_{r \in I} 3^{s_{r+1}} \zeta^{mr} 3^{kr/p}|$. This is a sum of $k$ terms of size $\leq 3^{2k} \approx 4^p$. By cancellation in the roots of unity, typically $|\sigma_m(F_I)| \approx 3^k \sqrt{k}$ (random walk estimate).

$|\sigma_m(x-2)| = |2 - \zeta^m \cdot 3^{k/p}| \approx 2|1-\zeta^m|$ for $3^{k/p} \approx 2$.

So for generic $m$: $|\sigma_m(Q_I)| \approx 3^k \sqrt{k} / (4\pi m/p) \approx 2^p \sqrt{k} p / (4\pi m)$.

### 4.6. The Height of Q_I

$$h_\infty(Q_I) = \frac{1}{p} \sum_m \log|\sigma_m(Q_I)|$$

The dominant contribution is from $m = 0$:
$$\frac{1}{p} \log(n \cdot p \cdot 2^{p-1}) \approx \frac{1}{p}(\log n + \log p + (p-1)\log 2) \approx \log 2$$

So $h_\infty(Q_I) \approx \log 2 + O(\log p / p)$.

This is a **constant** independent of $p$ (approximately).

---

## 5. The Successive Minima Approach

### 5.1. Idea

Instead of comparing heights of individual elements, compare the **successive minima** of the lattice $(x-2)R$ (under some norm/height) with the "height" of $F_I$.

The $i$-th successive minimum $\lambda_i$ of a lattice $\Lambda$ w.r.t. a convex body $B$ is the smallest $\lambda$ such that $\lambda B \cap \Lambda$ contains $i$ linearly independent vectors.

### 5.2. The Sup-Norm on Coefficient Vectors

For $f = \sum a_r x^r$, define $\|f\|_\infty = \max_r |a_r|$.

For $F_I$: $\|F_I\|_\infty = 3^{k-1}$ (the largest coefficient).

For elements of $(x-2)R$: if $f = (x-2)g$ where $g = \sum q_r x^r$, then:
$$a_r = q_{r-1} - 2q_r + 3^k q_{p-1} \delta_{r,0}$$
(from the companion matrix).

The first successive minimum $\lambda_1$ of $(x-2)R$ w.r.t. $\|\cdot\|_\infty$ is the smallest $\|f\|_\infty$ achievable by a nonzero $f \in (x-2)R$.

### 5.3. Lower Bound on $\lambda_1$

By Minkowski's theorem: $\lambda_1^p \leq 2^p \cdot D / V_p$ where $V_p$ is the volume of the unit ball in the $\|\cdot\|_\infty$ norm ($V_p = 2^p$). So $\lambda_1 \leq D^{1/p} \approx 2$.

This gives an **upper** bound on $\lambda_1$, not a lower bound. And it's too small to be useful.

### 5.4. Better: The Euclidean Norm

Use $\|f\|_2 = (\sum |a_r|^2)^{1/2}$.

For $F_I$: $\|F_I\|_2 = (\sum_{j=0}^{k-1} 3^{2(k-1-j)})^{1/2} = ((3^{2k}-1)/8)^{1/2} \approx 3^k/\sqrt{8} \approx 2^{0.63p}/\sqrt{8}$.

For the lattice $(x-2)R$: by Minkowski, $\lambda_1 \leq (2D)^{1/p} \cdot c_p \leq C$ (a constant).

So the first minimum is $O(1)$, while $\|F_I\| \approx 2^{0.63p}$. There's no contradiction from successive minima — the lattice contains short vectors, and $F_I$ is very long.

**Diagnosis:** Successive minima in coefficient space cannot help because $(x-2)R$ contains vectors much shorter than $F_I$. The question is whether $F_I$ specifically (with its particular structure) lies in the lattice, not whether short vectors do.

---

## 6. The Theta Function / Lattice Point Counting Approach

### 6.1. Setup

The theta function of the lattice $\Lambda = (x-2)R$ (embedded via Minkowski into $\mathbb{R}^p$) is:

$$\Theta_\Lambda(\tau) = \sum_{f \in \Lambda} e^{-\pi \tau \|f\|^2}$$

where $\|f\|$ is the Euclidean norm in the Minkowski embedding.

By Poisson summation:
$$\Theta_\Lambda(\tau) = \frac{1}{D \cdot \tau^{p/2}} \Theta_{\Lambda^*}(1/\tau)$$

where $\Lambda^* = (x-2)^{-1} R^*$ is the dual lattice (with $R^* = $ trace dual).

### 6.2. Individual Lattice Point Detection

We want to know whether a specific point $v = \Phi(F_I)$ lies in $\Lambda$. This is a single lattice point detection problem, not a counting problem.

The indicator function of $\Lambda$ can be written:
$$\mathbf{1}_\Lambda(v) = \frac{1}{D} \sum_{\chi \in R/\Lambda} \chi(v)$$

where the sum is over the $D$ characters of the quotient group $R/(x-2)R \cong \mathbb{Z}/D\mathbb{Z}$.

This is just the Fourier test for divisibility: $\mathbf{1}_\Lambda(v) = 1$ iff $D | F_I(2) = S(I)$.

We've come full circle — the lattice point detection is exactly the divisibility condition, just rephrased.

---

## 7. The Arakelov Intersection Number

### 7.1. Arithmetic Intersection on Spec(R)

Think of $R = \mathbb{Z}[x]/(x^p - 3^k)$ as the ring of global sections of an arithmetic curve $\mathcal{X} = \mathrm{Spec}(R)$ (an affine arithmetic scheme of relative dimension 0 over $\mathrm{Spec}(\mathbb{Z})$).

Two elements $f, g \in R$ define "arithmetic divisors." Their intersection number is:
$$\langle f, g \rangle = \sum_\mathfrak{p} v_\mathfrak{p}(f) \cdot v_\mathfrak{p}(g) \cdot \log N\mathfrak{p} + \sum_m \log|\sigma_m(f)| \cdot \log|\sigma_m(g)|$$

Wait — this isn't quite right. The Arakelov intersection theory is developed for **arithmetic surfaces** (2-dimensional schemes over $\mathbb{Z}$), not for $\mathrm{Spec}(R)$ which is 1-dimensional.

### 7.2. The Correct Setting: Arithmetic Surface from R

To apply Arakelov theory, we need a 2-dimensional object. Consider:

$$\mathcal{X} = \mathrm{Spec}(\mathbb{Z}[x,y]/(y - x^p + 3^k)) \cong \mathrm{Spec}(\mathbb{Z}[x]) \cong \mathbb{A}^1_\mathbb{Z}$$

This is not helpful. The standard Arakelov setup needs a proper arithmetic surface $\mathcal{X} \to \mathrm{Spec}(\mathbb{Z})$ where the generic fiber is a smooth curve.

**Alternative:** Consider the projective completion. Let $\mathcal{C}$ be the smooth projective curve over $\mathbb{Q}$ defined by $y^p = 3^k$ (a constant — this is degenerate) or better: the "Fermat-like" curve $Y^p = X^p - 3^k Z^p$ (but this is the hyperplane $Y^p + 3^k Z^p = X^p$, a Fermat hypersurface).

Actually, the most natural arithmetic surface here is:

$$\mathcal{X} = \mathrm{Proj}(\mathbb{Z}[X, Y]/(X^p - 3^k Y^p - Z^p \cdot D))$$

But this is getting contrived. Let me think differently.

### 7.3. Heights of Ideals (Faltings-Style)

For an order $R$ in a number field $K$, and ideals $I, J \subset R$, Faltings' height machinery gives heights of the quotients $R/I$:

$$h_F(R/I) = -\log \mathrm{covol}(I) + \frac{1}{2} \sum_m \log|\sigma_m(g)|$$

where $g$ is a generator of $I$ in $K$.

For the principal ideal $(x-2)R$:
$$h_F(R/(x-2)R) \propto \log D + \text{archimedean contribution}$$

And for the ideal generated by $F_I$:
$$h_F(R/F_I R) \propto \log|N(F_I)| + \text{archimedean terms}$$

The membership $F_I \in (x-2)R$ is equivalent to $(x-2)R \supseteq F_I \cdot R$... no, that's not right either. $F_I \in (x-2)R$ means $F_I$ is in the ideal, not that the ideals are ordered.

---

## 8. A New Approach: The Coefficient Entropy

### 8.1. Motivation

Heights in the Minkowski embedding don't help because they measure the SIZE of $f$ (which is too coarse). We need something that measures the SHAPE of the coefficient vector.

**Key structural difference between $F_I$ and generic elements of $(x-2)R$:**

$F_I$ has:
- Exactly $k$ nonzero coefficients (sparsity $k/p \approx 0.63$)
- Nonzero coefficients are all powers of 3 (multiplicatively structured)
- The powers of 3 are strictly decreasing: $3^{k-1}, 3^{k-2}, \ldots, 1$

A generic element $f = (x-2)g \in (x-2)R$ has:
- Typically ALL $p$ coefficients nonzero
- Coefficients are "random-looking" integers

### 8.2. Entropy of Coefficient Vectors

Define the **normalized coefficient entropy** of $f = \sum a_r x^r \in R$:
$$E(f) = -\sum_{r=0}^{p-1} \frac{|a_r|}{\|f\|_1} \log \frac{|a_r|}{\|f\|_1}$$
where $\|f\|_1 = \sum |a_r|$.

For $F_I$: the nonzero coefficients are $3^{k-1}, 3^{k-2}, \ldots, 3, 1$, so $\|F_I\|_1 = (3^k - 1)/2$.
$$E(F_I) = -\sum_{j=0}^{k-1} \frac{3^j}{(3^k-1)/2} \log \frac{3^j}{(3^k-1)/2}$$

The dominant term is $3^{k-1}/(3^k-1)/2 \approx 2/3$. So $E(F_I) \approx H(2/3, 2/9, 2/27, \ldots)$ where $H$ is the Shannon entropy. This converges to a constant $\approx 0.92$ (units: nats).

For a generic element of $(x-2)R$: all $p$ coefficients nonzero, roughly equal in magnitude. $E \approx \log p$.

So $E(F_I) \approx 0.92$ while $E(\text{generic}) \approx \log p$. The structured vectors have **much lower entropy**.

### 8.3. Can We Prove E(f) > constant for all f in (x-2)R?

If we could show $E(f) \geq c \log p$ for all nonzero $f \in (x-2)R$, then $F_I$ (with $E(F_I) = O(1)$) could not lie in $(x-2)R$.

**Unfortunately, this is false.** The element $(x-2) \cdot x^m \in (x-2)R$ has coefficient vector with only 2 or 3 nonzero entries ($x^{m+1} - 2x^m$, plus possibly a wraparound from $x^p = 3^k$). Its entropy is $O(1)$.

So the lattice $(x-2)R$ contains elements with low coefficient entropy. The entropy approach fails as stated.

---

## 9. The $b$-Adic Valuation Profile

### 9.1. Idea

The coefficients of $F_I$ are powers of 3. Define the **3-adic valuation profile**:
$$V(F_I) = (v_3(a_0), v_3(a_1), \ldots, v_3(a_{p-1}))$$

For $F_I$: the nonzero entries have $v_3$ values $k-1, k-2, \ldots, 0$ (one of each), and the zero entries have $v_3 = \infty$.

For $(x-2)g \in (x-2)R$: the coefficient $a_r = q_{r-1} - 2q_r$ (plus wraparound). If $g$ is "generic," the $v_3$ of $a_r$ is typically 0 (since $q_{r-1} - 2q_r$ is generically coprime to 3).

### 9.2. A 3-Adic Height on R

In the Collatz case, $x^p \equiv 3^k$ in $R$, so 3 has a specific ideal factorization in $R$.

Since $x^p = 3^k$, the element $x$ satisfies $v_3(x^p) = k$, suggesting $v_3(x) = k/p$ in a "fractional valuation" sense. More precisely, if $\mathfrak{q}$ is the unique prime of $R$ above 3 (if it's unique), then $v_\mathfrak{q}(x) = k/e$ where $e$ is the ramification index.

The ideal $(3) = (x^p/3^{k-1}) \cdot (3^{k-1}/x^{p-?})$... this gets complicated. Let me think about it differently.

### 9.3. The Prime (3) in R

In $R = \mathbb{Z}[x]/(x^p - 3^k)$, reduce modulo 3:
$$R/3R = \mathbb{F}_3[x]/(x^p) = \mathbb{F}_3[x]/(x^p)$$

So $(3) = \mathfrak{q}^p$ where $\mathfrak{q} = (3, x)$ is the unique prime above 3, totally ramified with $e = p$, $f = 1$.

The $\mathfrak{q}$-adic valuation: $v_\mathfrak{q}(3) = p$, $v_\mathfrak{q}(x) = k$ (from $x^p = 3^k$, so $p \cdot v_\mathfrak{q}(x) = k \cdot v_\mathfrak{q}(3) = kp$, giving $v_\mathfrak{q}(x) = k$).

For $F_I = \sum_{r \in I} 3^{s_{r+1}} x^r$:
$$v_\mathfrak{q}(3^{s_{r+1}} x^r) = p \cdot s_{r+1} + k \cdot r$$

So:
$$v_\mathfrak{q}(F_I) = \min_{r \in I} (p \cdot s_{r+1} + k \cdot r)$$

Since $s_{r+1} = k - j - 1$ when $r = i_{j+1}$ (the $(j+1)$-th selected position):
$$p \cdot s_{i_{j+1}+1} + k \cdot i_{j+1} = p(k-j-1) + k \cdot i_{j+1}$$

For $j = k-1$ (last position): $p \cdot 0 + k \cdot i_k = k \cdot i_k$.
For $j = 0$ (first position): $p(k-1) + k \cdot i_1$.

The minimum is at $j = k-1$: $v_\mathfrak{q}(F_I) = k \cdot i_k \leq k(p-1)$.

### 9.4. q-Adic Valuation of Elements in (x-2)R

For $f = (x-2)g \in (x-2)R$:
$$v_\mathfrak{q}(f) = v_\mathfrak{q}(x-2) + v_\mathfrak{q}(g)$$

Now $v_\mathfrak{q}(x-2) = \min(v_\mathfrak{q}(x), v_\mathfrak{q}(2)) = \min(k, 0) = 0$ (since $\gcd(2,3) = 1$, $v_\mathfrak{q}(2) = 0$, and $v_\mathfrak{q}(x) = k > 0$).

Wait: $v_\mathfrak{q}(2) = 0$ because 2 is a unit in $R_\mathfrak{q}$ (since $\mathfrak{q}$ lies over 3, not 2). And $v_\mathfrak{q}(x) = k$. So $v_\mathfrak{q}(x - 2) = \min(k, 0) = 0$.

Therefore $v_\mathfrak{q}(f) = v_\mathfrak{q}(g) \geq 0$ for $f \in (x-2)R$.

This gives no constraint beyond $v_\mathfrak{q}(F_I) \geq 0$, which is always satisfied.

### 9.5. The Prime (2) in R

$R/2R = \mathbb{F}_2[x]/(x^p - 3^k) = \mathbb{F}_2[x]/(x^p - 1)$ (since $3^k \equiv 1 \pmod{2}$).

$x^p - 1$ factors over $\mathbb{F}_2$ according to the cyclotomic factorization modulo 2. If $p$ is prime (which it need not be for the Collatz problem): $x^p - 1 = (x-1)(x^{p-1} + x^{p-2} + \cdots + 1)$. The second factor may or may not be irreducible over $\mathbb{F}_2$.

The element $(x-2) \equiv (x-0) = x$ in $R/2R$. So $(x-2) \equiv x \pmod{2}$.

In $R/2R = \mathbb{F}_2[x]/(x^p-1)$: the image of $(x-2)$ is $x$, which is a unit (since $x^p = 1$, so $x^{-1} = x^{p-1}$).

Therefore $(x-2)R + 2R = R$, meaning the ideal $(x-2)R$ is coprime to 2. This is consistent with $D = 2^p - 3^k$ being odd.

---

## 10. Intersection Theory: The Fundamental Idea

### 10.1. Two Divisors on Spec(R)

Think of $R$ as the coordinate ring of an arithmetic scheme. The element $F_I$ defines a "horizontal" divisor, and $(x-2)$ defines another. Their "intersection" at a prime $\mathfrak{p}$ counts the common vanishing:

$$i_\mathfrak{p}(F_I, x-2) = \dim_{\mathbb{F}_\mathfrak{p}} R_\mathfrak{p}/(F_I, x-2)R_\mathfrak{p}$$

Summing over all primes:
$$\langle F_I, x-2 \rangle_{\mathrm{fin}} = \sum_\mathfrak{p} i_\mathfrak{p}(F_I, x-2) \cdot \log N\mathfrak{p}$$

This finite intersection number is essentially $\log|R/(F_I, x-2)R| = \log|\gcd(N(F_I), D)|$ (approximately).

If $D | S(I) = F_I(2)$, then $(F_I, x-2)$ generates an ideal of index at least $D$ in $R$, so $\langle F_I, x-2 \rangle_\mathrm{fin} \geq \log D \approx 0.05p \log 2$.

If $D \nmid S(I)$, the intersection is smaller.

### 10.2. Arakelov Extension

In Arakelov theory, one adds archimedean contributions:
$$\langle F_I, x-2 \rangle_{\mathrm{Ar}} = \langle F_I, x-2 \rangle_{\mathrm{fin}} + \sum_{m=0}^{p-1} g_m(\sigma_m(F_I), \sigma_m(x-2))$$

where $g_m$ is a Green's function at the embedding $\sigma_m$.

The idea: if $\langle F_I, x-2 \rangle_\mathrm{Ar}$ is bounded by some universal function of $(p,k)$, and $\langle F_I, x-2 \rangle_\mathrm{fin} \geq \log D$ is required for divisibility, then the archimedean part must compensate. If it can't, we get a contradiction.

### 10.3. Computing the Archimedean Contribution

At embedding $\sigma_m$:
$$\sigma_m(F_I) = \sum_{r \in I} 3^{s_{r+1}} \zeta^{mr} 3^{kr/p}$$
$$\sigma_m(x-2) = \zeta^m 3^{k/p} - 2$$

The "Green's function" term should be:
$$g_m = -\log|\sigma_m(F_I)| - \log|\sigma_m(x-2)| + \text{correction}$$

(In the Arakelov formalism for arithmetic surfaces, $g$ is the Arakelov-Green function of the Riemann surface at the fiber. For a 0-dimensional fiber, it degenerates to something simpler.)

For our 1-dimensional $R$, the Arakelov height of the "point" $F_I$ relative to the "divisor" $(x-2)$ is essentially:
$$\hat{h}_{(x-2)}(F_I) = \frac{1}{p}(\langle F_I, x-2 \rangle_\mathrm{fin} + \sum_m \log^+ |\sigma_m(F_I / (x-2))|)$$

But $F_I / (x-2) = Q_I$ (when divisibility holds), and we computed $h_\infty(Q_I) \approx \log 2$.

### 10.4. The Arithmetic Bezout Inequality

**Theorem (Arithmetic Bezout, simplified).** For elements $f, g$ in a number ring $R$ of degree $p$ over $\mathbb{Z}$:
$$\langle f, g \rangle_\mathrm{fin} \leq p \cdot h(f) \cdot h(g) + O(p \log p)$$

For $f = F_I$, $g = x-2$:
- $h(F_I) \approx k \log 3 \approx 0.63p \log 3$
- $h(x-2) = \log 2$

So: $\langle F_I, x-2 \rangle_\mathrm{fin} \leq 0.63p^2 \log 3 \cdot \log 2 + O(p \log p) \approx 0.48 p^2$.

The divisibility requires $\langle F_I, x-2 \rangle_\mathrm{fin} \geq \log D \approx 0.05p$.

Since $0.05p \ll 0.48p^2$, the Bezout inequality is **far from tight** and gives no contradiction.

---

## 11. New Idea: The Resultant Height

### 11.1. The Key Object

Define $\rho(n, p, k) = \mathrm{Res}(F_I(x), x^p - 3^k) = N_{R/\mathbb{Z}}(F_I)$.

This is the norm of $F_I$ in $R$, equal to:
$$\rho = \prod_{m=0}^{p-1} F_I(\zeta^m \cdot 3^{k/p})$$

If $D | S(I) = F_I(2)$, then $(x-2) | F_I$ in $R$, so $D | \rho$.

### 11.2. Bounding ρ from the Structure of F_I

$F_I(x) = \sum_{r \in I} 3^{s_{r+1}} x^r$ is a polynomial of degree $\leq p-1$ with $k$ terms.

**Upper bound on ρ:** By Mahler's inequality:
$$|N(F_I)| \leq \prod_m |F_I(\zeta^m \cdot 3^{k/p})| \leq \prod_m \|F_I\|_1 \cdot \max(1, |\zeta^m \cdot 3^{k/p}|)^{p-1}$$

Since $|\zeta^m \cdot 3^{k/p}| = 3^{k/p} \approx 2$:
$$|\rho| \leq (\|F_I\|_1)^p \cdot 2^{p(p-1)} \approx (3^k/2)^p \cdot 2^{p^2}$$

This is astronomically large and useless.

**Better upper bound:** By the Bombieri norm / Beauzamy-Enflo inequality, or more directly:

$|F_I(\zeta^m \cdot 3^{k/p})|^2 = |\sum_{r \in I} 3^{s_{r+1}} \zeta^{mr} 3^{kr/p}|^2 \leq k \sum_{r \in I} 3^{2s_{r+1}} \cdot 3^{2kr/p}$ (Cauchy-Schwarz)

$= k \sum_{j=0}^{k-1} 3^{2(k-1-j)} \cdot 3^{2k i_{j+1}/p} \leq k^2 \cdot 3^{2k} \cdot 3^{2k}$

So $|F_I(\zeta^m \cdot 3^{k/p})| \leq k \cdot 3^{2k}$ and $|\rho| \leq (k \cdot 3^{2k})^p$.

For divisibility: $D | \rho$ requires $|\rho| \geq D \approx 2^p$. Since $(k \cdot 3^{2k})^p \gg 2^p$, there's no contradiction.

### 11.3. Exploiting Cancellation in the Product

The product $\rho = \prod_m F_I(\zeta^m \cdot 3^{k/p})$ involves terms with roots of unity, so there's cancellation.

Actually, $\rho$ is always an integer (it's the norm of an algebraic integer). And:
$$\rho = \mathrm{Res}(F_I(x), x^p - 3^k) = (-1)^{pk} \cdot 3^{k \cdot \deg F_I} \cdot \prod_{r \in I} (\text{something involving the roots of } F_I)$$

This is getting complicated without leading anywhere new.

---

## 12. The Core Obstruction and a Genuine New Direction

### 12.1. Why Classical Arakelov Fails

Classical Arakelov theory gives height bounds that are either:
- Too weak (Bezout: quadratic in $p$, but we only need linear)
- In the wrong direction (norm bounds give lower bounds on $(x-2)R$ elements that are too small)

The fundamental issue: Arakelov theory bounds SIZES (norms, heights), but the Collatz non-divisibility is about STRUCTURE. The lattice $(x-2)R$ contains elements of all sizes, so no size-based bound can exclude $F_I$.

### 12.2. What COULD Work: Slope Inequality

In Arakelov geometry, the **slope** of a lattice (or more generally, a Hermitian vector bundle on an arithmetic curve) is:
$$\mu(\Lambda) = -\frac{\log \mathrm{covol}(\Lambda)}{\mathrm{rank}(\Lambda)}$$

For a sublattice $\Lambda' \subset \Lambda$, the slope decreases:
$$\mu(\Lambda') \leq \mu(\Lambda) + \text{correction}$$

**The analogy for our problem:**

Consider the "filtration" of $R$ by the ideals $\mathfrak{q}^j = (3, x)^j$:
$$R \supset \mathfrak{q} \supset \mathfrak{q}^2 \supset \cdots$$

The element $F_I$ has a specific $\mathfrak{q}$-adic profile (from Section 9.3).

The ideal $(x-2)R$ intersected with this filtration gives:
$$(x-2)R \cap \mathfrak{q}^j$$

If the $\mathfrak{q}$-adic profile of $F_I$ is incompatible with any element of $(x-2)R$ at the same $\mathfrak{q}$-adic level, that would give non-membership.

### 12.3. The Slope Filtration of (x-2)R

**Proposition.** For each $j \geq 0$:
$$(x-2)R \cap \mathfrak{q}^j = (x-2) \cdot (R \cap (x-2)^{-1}\mathfrak{q}^j)$$

Since $v_\mathfrak{q}(x-2) = 0$ (computed in 9.4), we have $(x-2)^{-1}\mathfrak{q}^j$ is well-defined in $K$, and:
$$(x-2)R \cap \mathfrak{q}^j = (x-2) \cdot \mathfrak{q}^j$$

(Since $x-2$ is a $\mathfrak{q}$-adic unit.)

So the $\mathfrak{q}$-adic filtration of $(x-2)R$ is just the shift of the $\mathfrak{q}$-adic filtration of $R$. The filtration gives no new information.

### 12.4. A Genuinely New Construction: The Bi-Filtered Height

**Definition.** For $f \in R$, define the **bi-filtered invariant**:
$$\beta(f) = v_\mathfrak{q}(f) \cdot h_\infty(f) - p \cdot v_\mathfrak{p}(f) \cdot h_\mathfrak{q}(f)$$

where $\mathfrak{p}$ is a prime above 2...

Actually, this is getting too ad hoc. Let me step back and think about what's genuinely possible.

---

## 13. Honest Assessment

### 13.1. What We've Established

1. $R = \mathbb{Z}[x]/(x^p - 3^k)$ is a well-defined order in a degree-$p$ number field.
2. The membership $F_I \in (x-2)R$ is an exact reformulation of $D | S(I)$.
3. The Minkowski embedding maps $R$ to a lattice in $\mathbb{R}^p$ and $(x-2)R$ to a sublattice of index $D$.
4. Classical height bounds (norm, Bezout, successive minima) are all too weak to exclude $F_I$.
5. The archimedean structure has a striking asymmetry: $\sigma_0(x-2) \approx 0$ while other $\sigma_m(x-2) = O(1)$.
6. The $\mathfrak{q}$-adic structure ($\mathfrak{q}$ above 3) gives $v_\mathfrak{q}(x-2) = 0$, so the 3-adic filtration doesn't help.

### 13.2. The Gap

No standard tool in arithmetic geometry produces a height inequality of the form "structured sparse elements can't lie in $(x-2)R$." The fundamental reason:

$(x-2)R$ contains elements of ALL types — sparse, dense, large, small. The membership is a LINEAR condition (lattice membership), so it doesn't constrain the "shape" of elements, only their residue class modulo the sublattice.

### 13.3. What Would Be Needed

A height or invariant that:
1. Is NOT linear (so it can distinguish between residue classes of the quotient $R/(x-2)R$)
2. Captures the MULTIPLICATIVE structure of the coefficients (powers of 3)
3. Interacts with the ideal $(x-2)R$ in a way that creates a contradiction

The only candidate I see: a **non-linear** functional on $R$ that combines the additive lattice structure with the multiplicative structure of the coefficients. This would be genuinely new mathematics — no existing framework provides this.

### 13.4. Comparison with Map.md Assessment

The original assessment in map.md was:
> CHALLENGE: Arakelov theory is developed for arithmetic surfaces and abelian varieties, not for orders like Z[x]/(x^p - b^k).

This is confirmed. The deeper issue isn't just that the theory hasn't been developed for these orders — it's that height-based methods are inherently too coarse for this problem, because membership in $(x-2)R$ is a LINEAR (lattice) condition that doesn't constrain heights or shapes.

---

## 14. Residual Idea: Embedding-Specific Constraints

### 14.1. The Near-Degenerate Embedding

At $\sigma_0$: $\sigma_0(\alpha) = 3^{k/p} \approx 2$, so $\sigma_0(x-2) \approx 0$.

If $F_I = (x-2)Q_I$, then:
$$\sigma_0(Q_I) = \frac{\sigma_0(F_I)}{\sigma_0(x-2)} \approx \frac{S(I)}{3^{k/p} - 2}$$

This is a huge number ($\approx n \cdot p \cdot 2^{p-1}$). All the "mass" of $Q_I$ is concentrated at the near-degenerate embedding.

**Consequence:** $Q_I$ is extremely anisotropic in the Minkowski embedding — its $\sigma_0$ component is exponentially larger than the others.

### 14.2. Does This Constrain Q_I?

For $Q_I$ to have integer coefficients, all its Minkowski coordinates must be compatible. The extreme anisotropy at $\sigma_0$ means:

$$q_r \approx -\frac{\sigma_0(Q_I)}{p} \approx -\frac{n \cdot 2^{p-1}}{1}$$

(The coefficient vector is dominated by the $\sigma_0$ contribution.)

But we already know this from the explicit formula: $q_r \approx -n \cdot 2^{p-1-r}$.

The integrality of $Q_I$ is automatically satisfied whenever $D | S(I)$ (by the algebraic setup). So the anisotropy is a feature of the problem, not a contradiction.

### 14.3. Conclusion for 0B

The arithmetic intersection theory approach on $R = \mathbb{Z}[x]/(x^p - 3^k)$ does NOT yield a path to proving Part 1. The fundamental obstruction is:

> **Membership in $(x-2)R$ is a linear (lattice) condition. Height-based methods measure sizes, not residue classes. No height can distinguish between elements of different residue classes in $R/(x-2)R \cong \mathbb{Z}/D\mathbb{Z}$.**

This is the same barrier we've seen before in different guise: the problem requires distinguishing a SPECIFIC residue (0) from the $D-1$ others, which is a number-theoretic question at scale $D$, not a geometric question about the lattice.

**Status: 0B → EXPLORED, does not escape the barriers.**

The Arakelov/height approach would work if there were a NON-LINEAR relation between $F_I$ and $(x-2)R$ — e.g., if we needed $F_I^2 \in (x-2)R$ or $N(F_I) \in (x-2)R$. But the condition is simply $F_I \in (x-2)R$, which is linear.
