# Direction 0C: Motivic / Categorical Structure on {a,b}-Smooth Sums

*Developed 2026-03-06 (Session 7)*

## 0. Goal and Context

**Goal:** Construct an algebraic-geometric or categorical object whose cohomology (or structural invariants) encodes the divisibility $D \mid S(I)$, then use cohomological methods to prove non-divisibility.

**Context:** This is the last concrete direction in Part 0 of the problem decomposition. Directions 0A (non-abelian sieve), 0B (Arakelov theory), and 0D (transversal zero-sum / cascade) have all been explored. 0A and 0B fail outright; 0D reduces to the full conjecture via the Syracuse-Cascade Duality (C7). Direction 0C is the most speculative: it asks whether genuinely new mathematical structure exists on the space of {2,3}-smooth sums.

**The analogy driving 0C:** The Weil conjectures were proved by inventing etale cohomology, which made "number of points on a variety mod $p$" into a topological invariant. Can we similarly make "number of divisible structured sums mod $D$" into a computable invariant?

---

## 1. Toric Geometry of Bi-Smooth Sums

### 1.1. The Two-Variable Formulation

Replace the evaluation $(a,b) = (2,3)$ by formal variables $(u,v)$. Define:

$$F_I(u,v) = \sum_{j=1}^k v^{k-j} u^{i_j}$$

and the "modulus polynomial":

$$G(u,v) = u^p - v^k$$

Then $D = G(2,3)$ and $S(I) = F_I(2,3)$, so:

$$D \mid S(I) \iff G(2,3) \mid F_I(2,3)$$

This is a condition on the **integer evaluation** of two Laurent polynomials at a specific lattice point.

### 1.2. Newton Polygons

The Newton polygon of $G(u,v) = u^p - v^k$ is:

$$\text{Newt}(G) = \text{conv}\{(p,0),\; (0,k)\} \subset \mathbb{R}^2$$

This is a line segment of Euclidean length $\sqrt{p^2 + k^2}$.

The Newton polygon of $F_I(u,v) = \sum_{j=1}^k v^{k-j} u^{i_j}$ is:

$$\text{Newt}(F_I) = \text{conv}\{(i_1, k-1),\; (i_2, k-2),\; \ldots,\; (i_k, 0)\}$$

This is a convex polygon with vertices among the lattice points $(i_j, k-j)$. These points lie roughly along a line of slope $-k/p \approx -\log 2/\log 3$.

**Key observation:** $\text{Newt}(G)$ and $\text{Newt}(F_I)$ have **parallel slopes** (both $\approx -k/p$). The Newton polygon of $F_I$ is approximately a thickened version of the Newton polygon of $G$.

### 1.3. The BKK Mixed Volume

The Bernstein-Kouchnirenko-Khovanskii theorem bounds the number of common zeros of $G$ and $F_I$ in $(\mathbb{C}^*)^2$ by the mixed volume $\text{MV}(\text{Newt}(G), \text{Newt}(F_I))$.

For a segment $S$ and a polygon $P$ in $\mathbb{R}^2$:

$$\text{MV}(S, P) = L(S) \cdot w(P, S^\perp)$$

where $L(S)$ is the length of $S$ and $w(P, S^\perp)$ is the width of $P$ in the direction perpendicular to $S$.

The direction of $\text{Newt}(G)$ is $(-k, p)/\sqrt{p^2+k^2}$. The perpendicular direction is $(p, k)/\sqrt{p^2+k^2}$.

The width of $\text{Newt}(F_I)$ in this direction is:

$$w = \frac{\max_j(p \cdot i_j + k(k-j)) - \min_j(p \cdot i_j + k(k-j))}{\sqrt{p^2 + k^2}}$$

Since $\text{Newt}(G)$ and $\text{Newt}(F_I)$ have nearly parallel slopes, $w$ is small (the polygon $\text{Newt}(F_I)$ is thin in the perpendicular direction).

**Computed values** (from `motivic_verify.py`):

| $(p,k)$ | $\text{MV}$ | Common zeros bound | $\text{Area}(\text{Newt}(F_I))$ |
|----------|-------------|-------------------|-------------------------------|
| $(5,3)$ | 4 | 4 | 0 (line segment) |
| $(7,4)$ | 9 | 9 | 0 (line segment) |
| $(8,5)$ | 12 | 12 | 0 (line segment) |
| $(10,6)$ | 20 | 20 | 0 (line segment) |

Note: For compact positions $I = \{0,1,\ldots,k-1\}$, the vertices $(j, k-1-j)$ lie on the line $x + y = k-1$, so $\text{Newt}(F_I)$ is always a line segment (degenerate polygon). The MV equals $|\det(d_G, d_F)|$ where $d_G, d_F$ are the direction vectors of the two segments.

### 1.4. Why Toric Intersection Theory Doesn't Help

The mixed volume bounds the number of **common zeros** of $G$ and $F_I$ in $(\mathbb{C}^*)^2$. But:

1. **We need evaluation, not common zeros.** The condition $D \mid F_I(2,3)$ asks about the VALUE of $F_I$ at a SPECIFIC POINT $(2,3)$, not about whether $G$ and $F_I$ share a zero.

2. **$(2,3)$ is not on the curve $G = 0$.** Since $G(2,3) = D \neq 0$, the point $(2,3)$ does NOT lie on $\{G = 0\}$. The local intersection multiplicity at $(2,3)$ is therefore 0.

3. **The divisibility is an arithmetic condition, not geometric.** $D \mid F_I(2,3)$ says the integer $F_I(2,3)$ is divisible by the integer $G(2,3)$. This is a single Diophantine condition, not a condition about a variety.

**The fundamental disconnect:** Toric intersection theory computes how curves intersect IN the torus $(\mathbb{C}^*)^2$. The Collatz condition is about integer divisibility AT a single lattice point. These are completely different questions.

---

## 2. Log-Geometric Structure

### 2.1. The {2,3}-Smooth Monoid

The set $\{2^a \cdot 3^b : a, b \geq 0\}$ forms the free commutative monoid $M = \mathbb{N}^2$ under the map $(a,b) \mapsto 2^a \cdot 3^b$. This is a sharp, fine, saturated (fs) monoid in the sense of Kato.

A **log structure** on $\text{Spec}(\mathbb{Z})$ is a monoid homomorphism $M \to \mathbb{Z}$ together with compatibility data. The canonical log structure associated to $\{2,3\}$ maps $(a,b) \mapsto 2^a \cdot 3^b$.

### 2.2. The Collatz Sum in Log-Geometric Language

Each term of $S(I) = \sum_{j=1}^k 3^{k-j} \cdot 2^{i_j}$ is an element of the image of $M$ in $\mathbb{Z}$:

$$s_j = 2^{i_j} \cdot 3^{k-j} = \alpha(i_j, k-j) \qquad \text{where } \alpha: M \to \mathbb{Z}$$

The Collatz sum $S(I)$ is a sum of $k$ such images. In the log world, sums are NOT natural operations (the log structure is multiplicative). The ADDITION of smooth numbers is what breaks the log-geometric structure.

### 2.3. Why Log Geometry Doesn't Help

**The key obstruction:** Log geometry captures the **multiplicative** structure of the monoid $M$, but the Collatz sum involves **addition**. The transition from multiplicative to additive structure is exactly where the difficulty lies.

Concretely:
- Log geometry can encode: $2^a \cdot 3^b$ divides $2^c \cdot 3^d$ (iff $a \leq c$ and $b \leq d$).
- Log geometry CANNOT naturally encode: $2^{a_1} \cdot 3^{b_1} + 2^{a_2} \cdot 3^{b_2}$ is divisible by $D$.

The divisibility of a **sum** of smooth numbers is an arithmetic condition that lives outside the log structure.

---

## 3. The Zeta Function Question

### 3.1. What a "Collatz Zeta Function" Would Need

The Weil conjecture analogy requires:
1. A **varying parameter** $q$ (like the field size $\mathbb{F}_q$)
2. A **counting function** $N(q)$ (like $\#X(\mathbb{F}_q)$)
3. A **generating series** $Z(t) = \exp(\sum N(q) t^n/n)$
4. A **cohomological interpretation** $Z(t) = \prod P_i(t)^{(-1)^{i+1}}$

For Collatz, the "counting function" is $N(p,k) = \#\{I : D \mid S(I)\}$, which we want to show equals 0.

### 3.2. The Partition Function

Define:

$$Z(s; p, k) = \sum_{|I|=k} |S(I)|^{-s}$$

This is the "thermodynamic partition function" (already identified in direction 6e of the map). At $s = 0$: $Z(0) = \binom{p}{k}$. As $s \to \infty$: $Z(s) \to |S_{\min}|^{-s}$.

The critical observation: the "pressure" $P(s) = \frac{1}{p} \log Z(s)$ satisfies:
- $P(0) \approx H(k/p) \approx 0.95$ (the entropy)
- $P(1) \approx P(0) - \log 2 \approx -0.05$ (since $|S(I)|/D \approx 1$ on average)

The phase transition at $s^* < 1$ where $P(s^*) = 0$ marks the boundary between "many large contributions" and "exponentially few contributions."

### 3.3. Why There's No Functional Equation

A functional equation $Z(s) = \epsilon \cdot A^{s-1/2} \cdot Z(1-s)$ would encode deep symmetry. For Weil zeta functions, this comes from Poincare duality on the variety.

For the Collatz partition function:
- There's no underlying variety with duality.
- The sum $S(I)$ has no multiplicative structure (it's a SUM of smooth numbers, not a product).
- The weights $3^{k-j}$ break any permutation symmetry that might give a functional equation.

**Verified computationally:** $Z(s; p, k)$ has no discernible functional equation for any tested $(p,k)$.

### 3.4. The Weil Analogy Breaks Down

The deepest reason the Weil analogy fails:

| Weil Conjectures | Collatz |
|------------------|---------|
| Count $\#X(\mathbb{F}_q)$ as $q$ varies | Count $\#\{I : D \mid S(I)\}$ for fixed $(p,k)$ |
| $q$ varies continuously (prime powers) | No natural varying parameter |
| Zeta function is a rational function of $t$ | No zeta function at all |
| Frobenius endomorphism provides symmetry | No analogous symmetry |
| Cohomology $H^i(X, \mathbb{Q}_\ell)$ is finite-dim | No cohomology theory available |
| Point count = alternating trace of Frobenius | No trace formula |

**The missing ingredient is the VARYING PARAMETER.** In the Weil setting, varying $q = p^n$ provides a whole family of counting problems, and the zeta function encodes the entire family. For Collatz, each $(p,k)$ is an isolated problem with no natural deformation parameter.

One might try varying $p$ (keeping $k/p$ near $\log 2/\log 3$). But:
- $p$ is an integer, not a continuous parameter.
- The structure of $D = 2^p - 3^k$ changes discontinuously with $p$.
- The limiting behavior as $p \to \infty$ (via continued fraction convergents of $\log_2 3$) gives the full Collatz conjecture (C7-C8), not a simplification.

---

## 4. Tropical Geometry

### 4.1. Tropicalization of Key Polynomials

The tropicalization of a polynomial $f = \sum a_\alpha x^\alpha$ (over a non-archimedean field with valuation $v$) is:

$$\text{trop}(f)(w) = \min_\alpha (v(a_\alpha) + \alpha \cdot w)$$

For $F_I(u,v) = \sum v^{k-j} u^{i_j}$ with the 2-adic valuation $v_2$:

$$\text{trop}_2(F_I)(w_1, w_2) = \min_j (i_j w_1 + (k-j) w_2)$$

(since $v_2(1) = 0$ for all coefficients, which are powers of 3).

For $G(u,v) = u^p - v^k$:

$$\text{trop}_2(G)(w_1, w_2) = \min(p w_1, k w_2)$$

### 4.2. Tropical Intersection

The tropical curves $\text{trop}(G) = 0$ and $\text{trop}(F_I) = 0$ are piecewise-linear objects in $\mathbb{R}^2$. Their intersection number equals the classical intersection number (by Mikhalkin's correspondence theorem, for curves in toric surfaces).

The tropical curve of $G$: $\min(pw_1, kw_2) = \min(pw_1, kw_2)$, which is the "corner locus" where $pw_1 = kw_2$, i.e., $w_2/w_1 = p/k$. This is a single ray.

Evaluating at the "valuation point" of $(2,3)$: $v_2(2) = 1$, $v_2(3) = 0$, giving $(w_1, w_2) = (1, 0)$. Then $\text{trop}_2(G)(1,0) = \min(p, 0) = 0$, and $\text{trop}_2(F_I)(1,0) = \min_j(i_j) = i_1$.

### 4.3. What Tropicalization Captures and Misses

**Captures:**
- $v_2(S(I)) = i_1$ (the 2-adic valuation of $S(I)$ is determined by the smallest position). This is just Theorem C1 (WLOG $i_1 = 0$).
- $v_3(S(I)) = 0$ (the last term $2^{i_k}$ has no factor of 3).

**Misses:**
- The divisibility $D \mid S(I)$ is about the $D$-adic valuation, not the 2-adic or 3-adic valuation. Since $D$ is typically prime or has large prime factors, this information is invisible to the tropicalizations at 2 and 3.
- Tropical geometry works with **leading terms** (min/max of valuations). The Collatz divisibility condition is about **exact cancellation** in the sum, which is a sub-leading effect invisible to the tropical world.

**Diagnosis:** Tropicalization loses too much information. It captures the coarsest arithmetic (valuations at small primes) but misses the fine arithmetic (divisibility by the large modulus $D$).

---

## 5. $\mathbb{F}_1$-Geometry and $\lambda$-Rings

### 5.1. The Smooth Monoid as an $\mathbb{F}_1$-Scheme

In Borger's framework, an $\mathbb{F}_1$-algebra is a $\lambda$-ring: a commutative ring with "Frobenius lifts" $\psi_p$ for each prime $p$.

The $\{2,3\}$-smooth monoid $M = \{2^a 3^b\}$ is a monoid under multiplication. Over $\mathbb{F}_1$, it corresponds to the "affine toric scheme" $\text{Spec}(\mathbb{F}_1[M])$.

Base change to $\mathbb{Z}$ gives $\text{Spec}(\mathbb{Z}[M]) = \text{Spec}(\mathbb{Z}[x^{\pm 1}, y^{\pm 1}])$ where $x = 2, y = 3$.

### 5.2. Frobenius Lifts and the Collatz Map

In a $\lambda$-ring, the Frobenius at $p$ acts as $\psi_p(n) = n^p$ on elements. On $\mathbb{Z}$:
- $\psi_2(n) = n^2$ (not $2n$)
- $\psi_3(n) = n^3$ (not $3n$)

The Collatz map $T(n) = n/2$ or $(3n+1)/2$ involves **multiplication** by $3/2$ and **addition** of $1/2$. The multiplicative part ($\times 3/2$) is related to the ratio $\psi_3/\psi_2$ in the $\lambda$-ring. But the additive part ($+1/2$) breaks the $\lambda$-ring structure.

### 5.3. The "+1" Obstruction

The Collatz map mixes two operations:
- **Multiplication** by smooth numbers ($\times 2$, $\times 3$) -- this is compatible with $\mathbb{F}_1$-structure.
- **Addition** of $+1$ -- this is NOT compatible with $\mathbb{F}_1$-structure.

The "$+1$" is what makes Collatz hard. Without it ($n \mapsto 3n/2$, which is purely multiplicative), the dynamics would be trivially understood via the independence of $\log 2$ and $\log 3$ over $\mathbb{Q}$.

In $\lambda$-ring language: the Collatz map is a **perturbation** of a $\lambda$-ring endomorphism by an additive term. The perturbation takes us outside the $\mathbb{F}_1$-world.

### 5.4. Why $\mathbb{F}_1$-Methods Don't Help

The $\mathbb{F}_1$-framework is designed for:
- Counting points on varieties via zeta functions (Kurokawa, Soule, Connes-Consani).
- Understanding the "arithmetic" of multiplicative structures.

The Collatz problem involves an additive perturbation ($+1$) that is invisible to the $\mathbb{F}_1$-framework. This is the same obstruction as in log geometry (Section 2): the difficulty lives in the ADDITION of smooth numbers.

---

## 6. Configuration Space Cohomology

### 6.1. The Configuration Space

The space of ordered $k$-subsets of $\{0, \ldots, p-1\}$ is:

$$\text{Conf}_k = \{(i_1, \ldots, i_k) : 0 \leq i_1 < i_2 < \cdots < i_k \leq p-1\}$$

This is a finite set of size $\binom{p}{k}$. As a topological space (discrete topology), it has trivial cohomology: $H^0 = \mathbb{Z}^{\binom{p}{k}}$, $H^i = 0$ for $i \geq 1$.

### 6.2. The Sum Map

The Collatz sum defines a function:

$$S: \text{Conf}_k \to \mathbb{Z}/D\mathbb{Z}, \qquad I \mapsto S(I) \bmod D$$

The fiber $S^{-1}(0)$ is the set of "Collatz cycles." We want to show $S^{-1}(0) = \emptyset$.

### 6.3. Continuous Embedding

Embed $\text{Conf}_k$ in the continuous ordered configuration space:

$$\widetilde{\text{Conf}}_k = \{(x_1, \ldots, x_k) \in \mathbb{R}^k : 0 \leq x_1 < x_2 < \cdots < x_k \leq p-1\}$$

This is a $k$-dimensional simplex. The continuous extension of $S$ is:

$$\widetilde{S}(x_1, \ldots, x_k) = \sum_{j=1}^k 3^{k-j} \cdot 2^{x_j}$$

This is a smooth function with $\widetilde{S} > 0$ everywhere (all terms positive). The level sets $\widetilde{S}^{-1}(nD)$ for $n \geq 1$ are smooth hypersurfaces in $\widetilde{\text{Conf}}_k$.

### 6.4. Curvature and Integer Points

The Hessian of $\widetilde{S}$ at a point $(x_1, \ldots, x_k)$ is diagonal:

$$\frac{\partial^2 \widetilde{S}}{\partial x_j^2} = 3^{k-j} \cdot (\log 2)^2 \cdot 2^{x_j}$$

The Gaussian curvature of the level surface $\widetilde{S} = c$ is:

$$K \propto \prod_{j=1}^k 3^{k-j} \cdot 2^{x_j}$$

For typical points: $K \approx 3^{k(k-1)/2} \cdot 2^{\sum x_j} \approx 3^{k^2/2} \cdot 2^{kp/2}$ -- exponentially large.

**The determinant method** (Heath-Brown, Salberger) bounds integer points on hypersurfaces:

$$\#\{I \in \mathbb{Z}^k : \widetilde{S}(I) = c\} \leq C \cdot K^{-1/(k-1)}$$

For our curvature: $K^{-1/(k-1)} \approx 2^{-p/2}$, which would give $< 1$ integer point. This seems promising!

**But there are two fatal problems:**

1. **The determinant method is for polynomial hypersurfaces, not exponential ones.** The function $\widetilde{S}$ involves $2^{x_j}$, which is exponential, not polynomial. The method requires bounded degree, and our "degree" is effectively $\infty$.

2. **Even for polynomial surfaces, the method gives UPPER BOUNDS that depend on the degree.** For a degree-$d$ surface in $\mathbb{R}^k$, the bound is $O(B^{k-2+\epsilon} d^{O(1)})$. Our "degree" grows with $p$, so the bound blows up.

3. **We're not asking about a SINGLE level set.** The condition $D \mid S(I)$ means $S(I) \in \{D, 2D, 3D, \ldots\}$ -- infinitely many level sets. Even if each level set has few integer points, the union could have many.

---

## 7. Derived Categories and the Divisibility Exact Sequence

### 7.1. The Fundamental Short Exact Sequence

In the order $R = \mathbb{Z}[x]/(x^p - 3^k)$, the multiplication-by-$(x-2)$ map gives:

$$0 \to R \xrightarrow{\times(x-2)} R \to R/(x-2)R \to 0$$

Since $R/(x-2)R \cong \mathbb{Z}/D\mathbb{Z}$ (Corollary 2.2 of agent_global_lattice.md), this is:

$$0 \to R \xrightarrow{\times(x-2)} R \to \mathbb{Z}/D\mathbb{Z} \to 0$$

The condition $F_I \in (x-2)R$ is equivalent to the image of $F_I$ in the quotient $\mathbb{Z}/D\mathbb{Z}$ being zero.

### 7.2. The Derived Perspective

In the derived category $D^b(\text{Mod}_R)$, the exact sequence gives a distinguished triangle:

$$R \to R \to \mathbb{Z}/D\mathbb{Z} \to R[1]$$

The connecting homomorphism $\delta: \mathbb{Z}/D\mathbb{Z} \to R[1] = \text{Ext}^1_R(\mathbb{Z}/D\mathbb{Z}, R)$ measures "how far" elements of $\mathbb{Z}/D\mathbb{Z}$ are from lifting to $R$.

But every element of $\mathbb{Z}/D\mathbb{Z}$ lifts to $R$ (since $R \to \mathbb{Z}/D\mathbb{Z}$ is surjective). The connecting homomorphism classifies the different lifts, not whether a lift exists.

### 7.3. Ext Groups

$$\text{Ext}^1_R(\mathbb{Z}/D\mathbb{Z}, R) = R/(x-2)R = \mathbb{Z}/D\mathbb{Z}$$

This is just saying the obstruction to uniqueness of the lift is $D$-periodic -- which is the divisibility condition again.

### 7.4. Why the Derived Category Doesn't Help

The derived category of $R$-modules is too algebraic. It encodes:
- Linear algebra over $R$
- Ideal structure of $R$
- Extensions and deformations

But the Collatz condition is about a SPECIFIC element $F_I$ (with its structured coefficient pattern) being in a SPECIFIC ideal $(x-2)R$. The derived category treats all elements of $R$ equally -- it cannot distinguish the structured $F_I$ from a generic element.

**The core issue (same as 0B):** Membership in an ideal is a LINEAR condition. Derived categories are built from linear algebra. No amount of homological machinery can distinguish between elements of the same residue class.

---

## 8. Galois Representations and L-Functions

### 8.1. The Galois Group of $x^p - 3^k$

For $p$ prime with $\gcd(p,k) = 1$, the polynomial $x^p - 3^k$ is irreducible over $\mathbb{Q}$, and its splitting field $L$ has Galois group:

$$\text{Gal}(L/\mathbb{Q}) \cong \mathbb{Z}/p\mathbb{Z} \rtimes (\mathbb{Z}/p\mathbb{Z})^* \cong \text{Aff}(\mathbb{F}_p)$$

of order $p(p-1)$. The automorphisms are:
- $\alpha \mapsto \zeta \alpha$ (cyclic of order $p$), $\zeta$ a primitive $p$-th root of unity
- $\zeta \mapsto \zeta^a$ for $a \in (\mathbb{Z}/p\mathbb{Z})^*$ (order $p-1$)

### 8.2. The Norm as a Galois-Equivariant Function

$N_{K/\mathbb{Q}}(F_I) = \prod_{m=0}^{p-1} \sigma_m(F_I)$, where $\sigma_m(\alpha) = \zeta^m \alpha$.

The norm is Galois-invariant and satisfies: $D \mid S(I) \implies D \mid N(F_I)$.

But the converse is false in general (the norm is too coarse). And even when $D \mid N(F_I)$, this doesn't help because we already showed (arakelov_0B.md, Section 11) that $|N(F_I)| \gg D$ for any nonzero $F_I$.

### 8.3. Artin L-Functions

The Artin $L$-function associated to the representation $\rho: \text{Gal}(L/\mathbb{Q}) \to GL_p(\mathbb{C})$ is:

$$L(s, \rho) = \prod_q \det(I - \rho(\text{Frob}_q) q^{-s})^{-1}$$

This encodes how primes split in $L$. But it does NOT encode divisibility of specific elements $F_I$ by the ideal $(x-2)$.

**Why:** $L$-functions capture the GLOBAL arithmetic of the number field (distribution of primes, class numbers, regulators). The Collatz condition is about a SPECIFIC principal ideal and a SPECIFIC element -- this is local information that $L$-functions don't see.

---

## 9. The Scheme $X_D$ and Point Counting

### 9.1. Can We Build a Variety Whose Points ARE the Cycles?

The most direct approach: construct a variety $X_D$ over $\mathbb{Z}$ such that:

$$\#X_D(\mathbb{Z}) = \#\{I : D \mid S(I)\}$$

Then show $\#X_D(\mathbb{Z}) = 0$ using geometric methods.

**Attempt 1: The affine scheme.** Define the system of equations:

$$\sum_{j=1}^k 3^{k-j} \cdot 2^{x_j} = n \cdot D, \qquad 0 \leq x_1 < x_2 < \cdots < x_k \leq p-1, \qquad n \in \mathbb{Z}_{>0}$$

The variables are $(x_1, \ldots, x_k, n)$. But $2^{x_j}$ is an EXPONENTIAL function of $x_j$, not a polynomial. This is not an algebraic variety.

**Attempt 2: Replace exponentials with new variables.** Set $y_j = 2^{x_j}$. Then $y_j \in \{1, 2, 4, \ldots, 2^{p-1}\}$ and the equation becomes:

$$\sum_{j=1}^k 3^{k-j} y_j = n D$$

with constraints: each $y_j$ is a power of 2, $y_1 < y_2 < \cdots < y_k$, all $y_j \leq 2^{p-1}$.

The equation $\sum 3^{k-j} y_j = nD$ IS linear in the $y_j$. But the constraint "$y_j$ is a power of 2" is not algebraic (in the classical sense). Over any ring, the set $\{2^0, 2^1, \ldots\}$ is not the zero set of polynomial equations.

**Attempt 3: Use multiplicative group structure.** The powers of 2 form the cyclic group $\langle 2 \rangle$ inside $\mathbb{Z}$. In the multiplicative group scheme $\mathbb{G}_m$, the $n$-torsion points $\mu_n$ are algebraic. But the orbit $\{2^m\}$ is not a torsion subgroup (it's infinite).

In $\mathbb{G}_m(\mathbb{Z}) = \{-1, 1\}$, the only units are $\pm 1$. The elements $\{2^m\}$ are not units; they live in $\mathbb{Z}$ but not in $\mathbb{G}_m(\mathbb{Z})$.

### 9.2. The Fundamental Obstruction

**There is no algebraic variety whose integer points are exactly the Collatz cycle parameters.**

The reason: the Collatz sum $S(I) = \sum 3^{k-j} \cdot 2^{i_j}$ involves EXPONENTIALS $2^{i_j}$. The set of positions $\{i_j\}$ parameterizes points on an exponential curve, not an algebraic curve. The transition from algebraic to exponential is where algebro-geometric methods lose their grip.

This is the same obstruction that appears in transcendence theory: the values of the exponential function at algebraic points are generically transcendental (Hermite-Lindemann), so exponential Diophantine equations are fundamentally harder than polynomial ones.

### 9.3. Comparison with Weil/Faltings

| Method | Object | Point count | Tools |
|--------|--------|-------------|-------|
| Weil conjectures | Variety $X/\mathbb{F}_q$ | $\#X(\mathbb{F}_q)$ | Etale cohomology |
| Faltings | Curve $C/\mathbb{Q}$, $g \geq 2$ | $\#C(\mathbb{Q})$ finite | Arakelov theory + Hodge |
| Collatz | NOT a variety | $\#\{I : D \mid S(I)\}$ | ??? |

The Collatz "space" is NOT a variety because the constraints involve exponentials. Without a variety, there is no:
- Cohomology theory to compute
- Frobenius endomorphism to take traces of
- Poincare duality to give functional equations
- Comparison theorems (de Rham, etale, crystalline) to exploit

---

## 10. The Exponential-Algebraic Divide

### 10.1. The Deepest Diagnosis

Every approach in Sections 1-9 fails for the same root cause:

> **The Collatz divisibility condition involves EXPONENTIAL functions ($2^{i_j}$, $3^{k-j}$), but all existing cohomological/motivic methods work with ALGEBRAIC (polynomial) objects.**

The divide between exponential and algebraic is a fundamental boundary in mathematics:

| Algebraic world | Exponential world |
|----------------|-------------------|
| Polynomial equations | Exponential Diophantine equations |
| Algebraic varieties | Exponential varieties (not a standard notion) |
| Weil conjectures, etale cohomology | Nothing analogous |
| Baker's theorem (LOWER bounds) | Collatz (needs IMPOSSIBILITY) |
| Effective Mordell (open for genus $\geq 2$) | Effective Skolem (open) |
| Faltings' theorem (finiteness) | Corvaja-Zannier (finiteness, ineffective) |

### 10.2. The Polynomial Reformulation Trap

One might try to "polynomialize" the problem:
- Replace $2^{i_j}$ by a new variable $y_j$ with the constraint $y_j \in \{1, 2, 4, \ldots, 2^{p-1}\}$.
- The linear equation $\sum 3^{k-j} y_j = nD$ defines a hyperplane.
- The constraint $y_j \in \{2^m\}$ defines a "digital" subset of $\mathbb{Z}^k$.

The number of integer points on the hyperplane intersected with the "digital" set is EXACTLY the Collatz cycle count. But the "digital" set $\{2^0, 2^1, \ldots, 2^{p-1}\}^k$ is:
- Not an algebraic variety
- Not a semialgebraic set (in the polynomial sense)
- A set with multiplicative structure but no additive structure

The intersection of a linear hyperplane with a multiplicatively-structured set is the SAME problem as the original Collatz divisibility. No reduction achieved.

### 10.3. The S-Unit Equation Connection

The Collatz equation $\sum_{j=1}^k 3^{k-j} \cdot 2^{i_j} = n(2^p - 3^k)$ is an **S-unit equation** with $S = \{2, 3\}$:

$$\text{(sum of $k$ $S$-units)} = n \cdot (\text{$S$-unit difference})$$

The Evertse-Schlickewei theorem gives finiteness of solutions for FIXED $k$. But $k \sim 0.63p$ grows with $p$, so finiteness breaks down. The bound on the number of solutions is $C(k)$, which is a tower of exponentials in $k$.

This is the closest existing framework, and it gives FINITENESS for fixed $k$ but nothing for growing $k$. Making it effective (quantitative) for growing $k$ is an open problem in Diophantine approximation.

---

## 11. Positive Residue: What a Working Framework Would Need

### 11.1. Requirements

A "motivic" framework that works for Collatz would need to:

1. **Handle exponentials:** Treat $2^x$ and $3^y$ as coherent objects, not just evaluate them at integers.

2. **Encode divisibility at composite moduli:** The modulus $D = 2^p - 3^k$ is composite and varies. The framework must handle divisibility by $D$ without decomposing $D$ into primes (else: abc barrier).

3. **Exploit the ordering constraint:** The positions $i_1 < \cdots < i_k$ must be distinct and ordered, with monotone weight assignment. This combinatorial constraint must be "seen" by the cohomology.

4. **Be effective:** It must give quantitative bounds, not just finiteness.

5. **Work for growing $k$:** The number of terms $k \sim 0.63p \to \infty$ with $p$.

### 11.2. The Closest Existing Theory: O-Minimal Structures

The theory of **o-minimal structures** (Wilkie, van den Dries) provides a framework for "tame" geometry that includes exponential functions. Key results:

- Wilkie (1996): The structure $\mathbb{R}_{\exp} = (\mathbb{R}, +, \times, \exp)$ is o-minimal.
- Pila-Wilkie (2006): Rational points on definable sets in o-minimal structures are sparse.

**The Pila-Wilkie theorem** bounds the number of rational points of height $\leq H$ on a "transcendental" definable set: $\#\{(x,y) \in X(\mathbb{Q}) : H(x,y) \leq H\} \leq C_\epsilon H^\epsilon$.

**Application attempt:** Define $X \subset \mathbb{R}^{k+1}$ by:

$$X = \{(x_1, \ldots, x_k, n) : \sum 3^{k-j} \cdot 2^{x_j} = n(2^p - 3^k), \; 0 \leq x_1 < \cdots < x_k \leq p-1\}$$

This is definable in $\mathbb{R}_{\exp}$. The integer points are exactly the Collatz cycles. By Pila-Wilkie, the number of such points of height $\leq H$ is $O(H^\epsilon)$.

**Problem:** The height bound $H$ here is exponential in $p$ (since the coordinates are $\leq p$ but the equation involves $2^p$). So the Pila-Wilkie bound gives $O(2^{\epsilon p})$, which is vacuous.

**Sharper versions** (Pila, 2011; Habegger-Pila, 2016) give better bounds for special definable sets. But the Collatz set has $k \to \infty$ variables, which defeats these methods (the implicit constants grow with dimension).

### 11.3. The Missing Mathematics

What would a working "motivic theory for exponential sums" look like?

**Axiom 1 (Exponential Cohomology).** For each $S$-unit equation $\sum a_i \cdot \prod_{p \in S} p^{x_{i,p}} = 0$, there exists a finite-dimensional vector space $H^*(X_S)$ whose dimension is controlled by the number of terms.

**Axiom 2 (Frobenius Action).** There exists an endomorphism $\Phi$ on $H^*$ such that the number of solutions is $|\text{tr}(\Phi|_{H^i})|$ (alternating trace formula).

**Axiom 3 (Weight Bound).** The eigenvalues of $\Phi$ satisfy $|\lambda| \leq C^{k}$ where $C$ is absolute and $k$ is the number of terms.

**Axiom 4 (Effectiveness).** The trace formula is effective: one can COMPUTE $\text{tr}(\Phi)$ and show it's 0.

No such theory exists today. Axiom 1 alone would be a major advance in arithmetic geometry. Together, these axioms would solve not just Collatz but a wide class of exponential Diophantine problems.

---

## 12. Computational Verification

### 12.1. Mixed Volumes

Verified by `motivic_verify.py`: the BKK mixed volume $\text{MV}(\text{Newt}(G), \text{Newt}(F_I))$ is $O(pk)$ for all test cases. This bounds the number of common zeros in $(\mathbb{C}^*)^2$, but is irrelevant to the integer divisibility condition (Section 1.4).

### 12.2. Norm Factorization

$N(F_I) = \prod_{m=0}^{p-1} F_I(\zeta^m \cdot 3^{k/p})$ is always divisible by $D$ when $D \mid S(I)$ (tautological). The cofactor $N(F_I)/D = N(Q_I)$ is a large integer with no special factorization pattern.

### 12.3. Partition Function

$Z(s; p, k) = \sum_{|I|=k} |S(I)|^{-s}$ has:
- $Z(0) = \binom{p}{k}$
- $Z(s)$ is smooth, decreasing, with no functional equation
- No rational structure visible in the coefficients

### 12.4. Tropical Valuations

For all test cases: $v_2(S(I)) = i_1$ and $v_3(S(I)) = 0$, confirming the tropical computation (Section 4.2). No additional information extracted.

---

## 13. Honest Assessment

### 13.1. Summary of Failures

| Approach | Core obstruction |
|----------|-----------------|
| Toric geometry | Evaluates at a point, not common zeros |
| Log geometry | Addition of smooth numbers breaks log structure |
| Zeta function | No varying parameter, no functional equation |
| Tropical geometry | Loses fine arithmetic (divisibility by $D$) |
| $\mathbb{F}_1$-geometry | "+1" perturbation breaks multiplicative structure |
| Configuration space | Discrete set, trivial cohomology |
| Derived categories | Ideal membership is linear, no distinguished $F_I$ |
| Galois representations | Encode field arithmetic, not element-level divisibility |
| Determinant method | Requires polynomial, not exponential, hypersurface |
| Pila-Wilkie | Dimension and height too large |

### 13.2. The Root Cause

All approaches fail because:

> **The Collatz divisibility condition $D \mid S(I)$ lives at the INTERSECTION of the exponential world ($2^{i_j}$, $3^{k-j}$) and the algebraic world (divisibility by $D = 2^p - 3^k$). Existing cohomological/motivic methods handle one world or the other, but not their intersection.**

Specifically:
- **Algebraic geometry** handles polynomial equations but not exponential ones.
- **Transcendence theory** handles exponential expressions but gives only BOUNDS (Baker), not IMPOSSIBILITY.
- **O-minimal geometry** handles exponential definable sets but with bounds too weak for growing dimension.
- **Additive combinatorics** handles structured sums but not at exponential moduli.

### 13.3. What Would Constitute a Breakthrough

A genuinely new framework would:
1. Treat the exponential-algebraic hybrid structure of $S(I)$ natively (not by reduction to one world or the other).
2. Produce a COMPUTABLE INVARIANT that detects divisibility.
3. Show this invariant is nonzero for all valid $(p,k)$ with large $p$.

This would be a contribution to mathematics far beyond the Collatz conjecture. It would provide new tools for exponential Diophantine equations, $S$-unit equations with growing number of terms, and the general problem of "arithmetic on exponential varieties."

### 13.4. Difficulty Assessment

**Direction 0C: EXPLORED, FAILS at the foundational level.**

Unlike 0A (circularity) and 0B (linearity), the failure of 0C is not a technical limitation but a **missing foundation**: the mathematical framework needed to handle exponential-algebraic hybrids at composite moduli DOES NOT EXIST. Building it would be comparable in scope to building etale cohomology (a multi-decade, multi-person program).

---

## 14. Final Status of Part 0

With 0C explored, ALL four Part 0 directions have been investigated:

| Direction | Status | Core obstruction |
|-----------|--------|-----------------|
| 0A: Non-abelian sieve | Circular | Anti-correlation = conjecture |
| 0B: Arakelov theory | Linear obstruction | Heights can't detect residue classes |
| 0C: Motivic/categorical | Missing foundation | No exponential-algebraic cohomology exists |
| 0D: Transversal zero-sum | Equivalent to conjecture | Cascade IS the Syracuse iteration (C7) |

**The diagnosis across all four directions is consistent:** the Collatz no-cycles conjecture requires mathematics that does not yet exist. The existing toolkit (algebraic geometry, number theory, combinatorics, dynamics) provides only tools that either:
- Work at polynomial scale but need exponential scale (abc barrier), or
- Work at exponential scale but are equivalent to the conjecture (equivalence barrier).

A proof would require bridging the gap between polynomial-scale tools and exponential-scale targets -- which is precisely the content of the abc conjecture for the specific family $2^p - 3^k$.
