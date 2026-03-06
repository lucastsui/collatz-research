# Bourgain-Gamburd Expansion for the Affine Collatz Walk: Analysis and Obstructions

**Date:** 2026-03-05

**Problem:** Prove that the second-largest eigenvalue of the Markov operator
$$
(Mf)(x) = \tfrac{1}{2}f(x \cdot 2^{-1}) + \tfrac{1}{2}f((3x+1) \cdot 2^{-1})
$$
on $\mathbb{Z}/p\mathbb{Z}$ satisfies $|\lambda_2| \leq 1 - c$ for a universal constant $c > 0$.

---

## 1. The Standard Bourgain-Gamburd Machine

### 1.1. Statement (Bourgain-Gamburd 2008, Tao's formulation)

**Theorem (B-G Expansion Machine).** Let $G$ be a finite group, $S \subset G$ a symmetric generating set, and $\mu = \frac{1}{|S|}\sum_{s \in S} \delta_s$ the uniform measure on $S$. Let $M$ be the associated Markov operator. Suppose:

1. **(Quasirandomness)** $G$ is $D$-quasirandom: every nontrivial irreducible representation of $G$ has dimension $\geq D$.
2. **(Product theorem)** There exist $\delta, \epsilon > 0$ such that for any $K$-approximate subgroup $A \subset G$ with $|G|^\delta \leq |A| \leq |G|^{1-\delta}$, we have $|A \cdot A \cdot A| \geq |A|^{1+\epsilon}$ (unless $A$ generates a proper subgroup).
3. **(Non-concentration)** For some $n_0 = O(\log |G|)$, the convolution power $\mu^{(n_0)}$ satisfies $\mu^{(n_0)}(H) \leq |H|^{-\eta}$ for any proper subgroup $H < G$, where $\eta > 0$.

Then the Cayley graph $\mathrm{Cay}(G, S)$ is an $\epsilon'$-expander, i.e., $|\lambda_2(M)| \leq 1 - \epsilon'$ for some $\epsilon' = \epsilon'(\delta, \epsilon, \eta, D) > 0$ independent of $|G|$.

**Key references:**
- Bourgain-Gamburd, "Uniform expansion bounds for Cayley graphs of SL_2(F_p)", *Annals of Math.* 167 (2008), 625-642.
- Tao, *Expansion in finite simple groups of Lie type*, GSM 164, AMS, 2015. See especially Chapter 4.
- Breuillard, "Approximate groups and the Bourgain-Gamburd machine", PCMI 2012 Lecture Notes.

### 1.2. How the machine works

The proof has three phases:

**Phase 1 (Initial flattening via non-concentration).** Using the non-concentration hypothesis, one shows that after $O(\log |G|)$ steps, the walk measure $\mu^{(n)}$ does not concentrate on any proper subgroup. This gives an initial bound $\|\mu^{(n)}\|_2^2 \leq |G|^{-\sigma}$ for some small $\sigma > 0$.

**Phase 2 (L^2 flattening via product theorem).** This is the core step. The *Balog-Szemeredi-Gowers lemma* converts L^2 information about $\mu^{(n)}$ into combinatorial set-growth information. Specifically, if $\|\mu^{(n)}\|_2^2 \gg |G|^{-1+\alpha}$, then the support of $\mu^{(n)}$ contains an approximate subgroup $A$ with $|A| \approx |G|^\alpha$. The *product theorem* then guarantees $|A^3| \gg |A|^{1+\epsilon}$, which forces the L^2 norm of $\mu^{(2n)}$ to drop: $\|\mu^{(2n)}\|_2^2 \leq |G|^{-\sigma'} \|\mu^{(n)}\|_2^2$ for some $\sigma' > 0$. Iterating: after $O(\log |G|)$ further convolutions, $\|\mu^{(N)}\|_2^2 \leq C |G|^{-1}$.

**Phase 3 (Quasirandomness smoothing).** Once $\mu^{(N)}$ is almost flat in L^2, quasirandomness finishes the job. For a $D$-quasirandom group, $\|\mu^{(N+1)}\|_2^2 \leq \|\mu^{(N)}\|_2^2 / D$ for the non-trivial Fourier components. With $D \geq |G|^\gamma$, a few more steps reach near-uniform distribution.

### 1.3. The critical role of quasirandomness

In Phase 3, the lower bound $D$ on representation dimensions is essential. It provides the "last mile" of mixing: once the L^2 norm is moderately small, quasirandomness forces rapid convergence to uniform. Without quasirandomness, the machine stalls -- the walk can concentrate on low-dimensional representations.

---

## 2. Why the Standard Machine Fails for Aff(F_p)

### 2.1. The affine group is solvable and non-quasirandom

Our random walk lives on $\mathbb{Z}/p\mathbb{Z}$, but the natural algebraic setting is the affine group:
$$
\mathrm{Aff}(\mathbb{F}_p) = \mathbb{F}_p^* \ltimes \mathbb{F}_p = \left\{ \begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} : a \in \mathbb{F}_p^*, b \in \mathbb{F}_p \right\}
$$

The two generators of our walk are:
$$
g_0 = \begin{pmatrix} 2^{-1} & 0 \\ 0 & 1 \end{pmatrix}, \qquad g_1 = \begin{pmatrix} 3 \cdot 2^{-1} & 2^{-1} \\ 0 & 1 \end{pmatrix}
$$

The group $\mathrm{Aff}(\mathbb{F}_p)$ has order $p(p-1)$ and is **solvable** (in fact metabelian: the derived subgroup is the translation subgroup $\mathbb{F}_p$, which is abelian).

**The representation theory of $\mathrm{Aff}(\mathbb{F}_p)$ (Conrad):**

The group has $p$ conjugacy classes and hence $p$ irreducible representations:
- **$(p-1)$ one-dimensional representations:** For each homomorphism $\chi : \mathbb{F}_p^* \to \mathbb{C}^*$, the map $(a, b) \mapsto \chi(a)$ gives a one-dimensional representation. These factor through the quotient $\mathrm{Aff}(\mathbb{F}_p) \twoheadrightarrow \mathbb{F}_p^*$.
- **One $(p-1)$-dimensional representation:** The "standard" representation on the space of functions $\{f : \mathbb{F}_p \to \mathbb{C} : \sum f = 0\}$ via $(g \cdot f)(x) = f(g^{-1}(x))$.

**Consequence:** $\mathrm{Aff}(\mathbb{F}_p)$ has $(p-1)$ one-dimensional representations. Its quasirandomness constant $D = 1$, the worst possible value. The Bourgain-Gamburd machine's Phase 3 (quasirandomness smoothing) **completely fails**.

This is not a mere technicality. The one-dimensional representations correspond to the multiplicative characters of $\mathbb{F}_p^*$, and they form a concrete obstruction: the walk can concentrate energy on these low-dimensional Fourier modes.

### 2.2. What this failure means concretely

The projection $\pi : \mathrm{Aff}(\mathbb{F}_p) \to \mathbb{F}_p^*$ (dropping the translation) sends our walk to the purely **multiplicative** random walk $x \mapsto 2^{-1}x$ or $3 \cdot 2^{-1}x$ on $\mathbb{F}_p^*$. The one-dimensional representations of $\mathrm{Aff}(\mathbb{F}_p)$ are precisely the characters that see only this multiplicative projection.

As we have established numerically, the multiplicative walk has spectral gap $\approx 0$ (at most $O(1/p)$). So the projection to one-dimensional representations has almost no mixing. The "+1" translation -- which the one-dimensional representations are blind to -- is the entire source of mixing.

This means:
- **Phase 3 is useless:** After flattening in Phases 1-2, the one-dimensional Fourier modes remain unmixed. We cannot appeal to quasirandomness to finish.
- **The walk on $\mathrm{Aff}(\mathbb{F}_p)$ itself does NOT have a constant spectral gap** in general (the multiplicative part decays as $O(1/p)$). The constant spectral gap is a phenomenon specific to the **quotient** action on $\mathbb{F}_p$ (the translation component).

### 2.3. The walk on $\mathbb{F}_p$ vs. the walk on $\mathrm{Aff}(\mathbb{F}_p)$

This is a subtle but crucial distinction. Our operator $M$ acts on $L^2(\mathbb{F}_p)$, not on $L^2(\mathrm{Aff}(\mathbb{F}_p))$. The space $L^2(\mathbb{F}_p)$ decomposes under the action of $\mathrm{Aff}(\mathbb{F}_p)$ as:
$$
L^2(\mathbb{F}_p) = \mathbb{C} \cdot \mathbf{1} \oplus V_{p-1}
$$
where $V_{p-1}$ is the unique $(p-1)$-dimensional irreducible representation. The one-dimensional representations of $\mathrm{Aff}(\mathbb{F}_p)$ do **not** appear in $L^2(\mathbb{F}_p)$.

This is the key structural advantage: **our walk acts on a space where the only representation present is the $(p-1)$-dimensional one**, precisely the "good" quasirandom-like representation. The one-dimensional representations are invisible.

However, we cannot directly plug this into the B-G machine because:
1. The machine works for the full Cayley graph (all representations), not a single representation.
2. While $V_{p-1}$ is a single irreducible, its dimension is $p-1$, which is **large** -- this is encouraging from the quasirandomness perspective, but the machine needs this for **all** irreducible representations simultaneously.

---

## 3. The Lindenstrauss-Varju Theorem

### 3.1. The main result

**Theorem (Lindenstrauss-Varju, 2014/2016).** Let $p$ be a prime, and let $\mu$ be a probability measure on the affine group $\mathrm{Aff}(\mathbb{F}_p) = \mathbb{F}_p^* \ltimes \mathbb{F}_p$. Let $\pi : \mathrm{Aff}(\mathbb{F}_p) \to \mathbb{F}_p^*$ be the natural projection, and let $\bar{\mu} = \pi_* \mu$ be the pushed-forward measure on $\mathbb{F}_p^*$.

Suppose:
- The support of $\mu$ generates $\mathrm{Aff}(\mathbb{F}_p)$ as a group.
- The pushed-forward measure $\bar{\mu}$ on $\mathbb{F}_p^*$ has a spectral gap: $\|\bar{\mu}^{(n)} * f\|_2 \leq \rho^n \|f\|_2$ for all $f \perp \mathbf{1}$, for some $\rho < 1$.

Then the spectral gap of $\mu$ on $\mathrm{Aff}(\mathbb{F}_p)$ can be bounded in terms of $\rho$ and $\|\mu\|$, with the bound being independent of $p$.

**More precisely:** The spectral gap of the random walk on $\mathbb{F}_p$ (the translation component, i.e., the action on the $(p-1)$-dimensional representation) can be estimated in terms of the spectral gap of the projected walk on $\mathbb{F}_p^*$.

**Reference:** Lindenstrauss and Varju, "Spectral gap in the group of affine transformations over prime fields," *Ann. Fac. Sci. Toulouse Math.* 25 (2016), no. 5, 969-993. arXiv: 1409.3564.

### 3.2. Why L-V doesn't immediately solve our problem

The L-V theorem is designed for the setting where:
- The generators include a **generic** element of $\mathrm{SL}_d(\mathbb{F}_p)$ acting on $\mathbb{F}_p^d$, so the projected walk on the linear part ($\mathrm{SL}_d(\mathbb{F}_p)$) already has a spectral gap (by Bourgain-Gamburd for semisimple groups).
- The translation part then inherits a spectral gap from the linear part's spectral gap.

**In our setting:** The linear part is not $\mathrm{SL}_d(\mathbb{F}_p)$ but a **subgroup** of $\mathbb{F}_p^*$ (the group $\langle 2^{-1}, 3 \cdot 2^{-1} \rangle = \langle 2, 3 \rangle \leq \mathbb{F}_p^*$). The group $\mathbb{F}_p^*$ is **abelian**, so the projected walk on $\mathbb{F}_p^*$ is a random walk on an abelian group. Its spectral gap is:
$$
\text{gap}_{\text{mult}} = 1 - \max_{\chi \neq \chi_0} \left| \tfrac{1}{2}\chi(2^{-1}) + \tfrac{1}{2}\chi(3 \cdot 2^{-1}) \right|
$$

For a character $\chi$ of $\mathbb{F}_p^*$ of order $d$:
$$
\left| \tfrac{1}{2}\chi(2^{-1}) + \tfrac{1}{2}\chi(3 \cdot 2^{-1}) \right| = \left| \tfrac{1}{2}(\chi(\alpha) + \chi(\beta)) \right| = \left| \cos\left(\frac{\pi (a_\chi - b_\chi)}{d}\right) \right|
$$
where $a_\chi, b_\chi$ are the discrete logarithms of $\alpha, \beta$ in the cyclic group.

**The problem:** When $\langle 2, 3 \rangle$ is a proper subgroup of $\mathbb{F}_p^*$, the characters of $\mathbb{F}_p^*$ that are trivial on $\langle 2, 3 \rangle$ achieve $|\hat{\bar{\mu}}(\chi)| = 1$, so **the multiplicative spectral gap is zero**. Even when $\langle 2, 3 \rangle = \mathbb{F}_p^*$, the gap is at most $O(1/p)$.

The L-V theorem can only give a spectral gap for the full walk that is at most as good as the multiplicative gap. So L-V gives at best $O(1/p)$, which is what we already proved.

### 3.3. The essential structural mismatch

The L-V approach works by "reducing to the linear part": if the linear part mixes well, the affine part follows. But in our problem, the linear part does NOT mix well -- it is a random walk on an abelian group. The mixing comes entirely from the **interplay** between the linear and translation parts. L-V's reduction goes in the wrong direction for us.

---

## 4. The Product Theorem for the Affine Group

### 4.1. Helfgott-Murphy-Rudnev-Shkredov classification

**Theorem (Rudnev-Shkredov, 2019; cf. Helfgott 2008, Murphy 2017).** Let $A \subset \mathrm{Aff}(\mathbb{F}_p)$ with $A = A^{-1}$ and $|A^3| \leq K|A|$. Then at least one of the following holds:

(a) If $1 < |A| \leq (1+\epsilon)p$: the projection $\pi(A)$ satisfies $|\pi(A)| \leq 2K^4$.

(b) If $|A| > (1+\epsilon)p$: we have $|\pi(A)| = O_\epsilon(K^3 |A|/p)$. Moreover, for $|A| > 4p$, $A^8 \supseteq U$ (where $U = \{(1, b) : b \in \mathbb{F}_p\}$ is the translation subgroup).

**Interpretation:** A slowly growing subset of $\mathrm{Aff}(\mathbb{F}_p)$ must have a small projection to $\mathbb{F}_p^*$ -- it is essentially "trapped near a coset of the translation subgroup $U$." Growth in $\mathrm{Aff}(\mathbb{F}_p)$ is equivalent (up to constants) to the **sum-product phenomenon**: if a subset has small multiplicative doubling, it must have small additive doubling, and vice versa.

**Reference:** Rudnev and Shkredov, "On growth rate in SL_2(F_p), the affine group and sum-product type implications," *Mathematika* 68 (2022), 39-70. arXiv: 1812.01671.

### 4.2. The product theorem applied to our walk

Our generators are $g_0 = (2^{-1}, 0)$ and $g_1 = (3 \cdot 2^{-1}, 2^{-1})$ in $\mathrm{Aff}(\mathbb{F}_p)$. Their projections to $\mathbb{F}_p^*$ are $\alpha = 2^{-1}$ and $\beta = 3 \cdot 2^{-1}$.

The group generated by $\{g_0, g_1\}$ is all of $\mathrm{Aff}(\mathbb{F}_p)$ (we proved this as Lemma 3.8 in the paper). In particular:
- The multiplicative projections generate $\langle \alpha, \beta \rangle = \langle 2, 3 \rangle \leq \mathbb{F}_p^*$.
- The translation part is nontrivial ($g_1$ has translation component $2^{-1} \neq 0$).

After $n$ steps, the support of $\mu^{(n)}$ in $\mathrm{Aff}(\mathbb{F}_p)$ has multiplicative projections in $\langle 2, 3 \rangle$ (which may be all of $\mathbb{F}_p^*$ or a proper subgroup). The product theorem tells us that if this support is an approximate subgroup that doesn't grow, it must be concentrated near a coset of $U$.

However, the product theorem alone does not give a spectral gap. It gives a combinatorial growth statement, which needs to be fed into a **flattening** argument (Phases 1-2 of B-G). The problem is Phase 3 (quasirandomness), which fails for our solvable group.

---

## 5. Attempting a Modified Expansion Argument

### 5.1. The Golsefidy-Varju perfectness criterion

**Theorem (Salehi Golsefidy-Varju, 2012).** Let $\Gamma \leq \mathrm{GL}_d(\mathbb{Q})$ be a finitely generated subgroup, and let $G = \overline{\Gamma}^{\mathrm{Zar}}$ be its Zariski closure. The Cayley graphs of $\pi_q(\Gamma)$ form a family of expanders as $q$ ranges over square-free integers with large prime divisors **if and only if** the connected component $G^0$ is **perfect** (i.e., $[G^0, G^0] = G^0$; equivalently, $G^0$ has no nontrivial abelian quotients).

**Reference:** Salehi Golsefidy and Varju, "Expansion in perfect groups," *Geom. Funct. Anal.* 22 (2012), 1832-1891.

**Application to our setting:** The Zariski closure of the group generated by $g_0, g_1$ inside $\mathrm{GL}_2$ is the full affine group $\mathrm{Aff}_1 = \mathbb{G}_m \ltimes \mathbb{G}_a$, which has connected component $\mathrm{Aff}_1^0 = \mathrm{Aff}_1$. The derived subgroup is $[\mathrm{Aff}_1, \mathrm{Aff}_1] = \mathbb{G}_a$ (the translation subgroup), and $\mathrm{Aff}_1 / \mathbb{G}_a \cong \mathbb{G}_m$ is abelian.

**Therefore $\mathrm{Aff}_1$ is NOT perfect.** The Golsefidy-Varju theorem predicts that the Cayley graphs of $\mathrm{Aff}(\mathbb{F}_p)$ do NOT form a family of expanders as $p \to \infty$.

**But wait -- this is about the walk on $\mathrm{Aff}(\mathbb{F}_p)$, not on $\mathbb{F}_p$.** The failure of expansion in $\mathrm{Aff}(\mathbb{F}_p)$ does not immediately imply failure of constant spectral gap for the induced action on $\mathbb{F}_p$. The abelian quotient $\mathbb{F}_p^*$ absorbs the non-expansion, while the action on $\mathbb{F}_p$ (which corresponds to the single large irreducible representation) may still have a constant spectral gap.

### 5.2. Restriction to the $(p-1)$-dimensional representation

Our operator $M$ acts on $L_0^2(\mathbb{F}_p}) = V_{p-1}$, the unique $(p-1)$-dimensional irreducible representation of $\mathrm{Aff}(\mathbb{F}_p)$. The relevant spectral gap is:
$$
\lambda_2 = \max_{f \perp \mathbf{1}} \frac{\|Mf\|_2}{\|f\|_2} = \| M |_{V_{p-1}} \|_{\mathrm{op}}
$$

To bound this, we need to show that the random walk, restricted to this specific representation, mixes rapidly. The dimension of $V_{p-1}$ is $p-1$, which grows with $p$ -- so from the perspective of a single representation, we have a "quasirandomness constant" of $D = p-1$, which is excellent.

**Proposed approach:** Combine:
1. Product theorem for $\mathrm{Aff}(\mathbb{F}_p)$ (Section 4.1) to get combinatorial growth.
2. The L^2 flattening lemma restricted to $V_{p-1}$.
3. The large dimension $\dim V_{p-1} = p-1$ as a substitute for quasirandomness in Phase 3.

### 5.3. The L^2 flattening restricted to $V_{p-1}$

The key quantity is the L^2 norm of $\mu^{(n)}$ restricted to $V_{p-1}$:
$$
\| \mu^{(n)} |_{V_{p-1}} \|_2^2 = \sum_{r \neq 0} |\hat{\mu}^{(n)}(r)|^2
$$
where $\hat{\mu}^{(n)}(r) = \frac{1}{p}\sum_{x} \mu^{(n)}(x) \omega^{-rx}$ are the Fourier coefficients.

From Theorem 12 (single-character contraction), we know:
$$
\| M \chi_r \|_2^2 = \frac{1}{2} \qquad \text{for all } r \neq 0.
$$

This means each Fourier mode individually contracts by $1/\sqrt{2}$ per step. If modes did not interfere, we would get $\| M^n |_{V_{p-1}} \|_{\mathrm{op}} \leq (1/\sqrt{2})^n$, giving the constant spectral gap $1 - 1/\sqrt{2} \approx 0.293$.

**The obstruction:** Modes DO interfere. $M\chi_r = \frac{1}{2}\chi_{r\alpha} + \frac{1}{2}\omega^{r\gamma}\chi_{r\beta}$ couples different Fourier modes. For a superposition $f = \sum a_r \chi_r$, the cross-term $\langle T_0 f, T_1 f \rangle$ can add constructively, potentially canceling the contraction.

### 5.4. The cross-term and sum-product structure

From the analysis in our paper:
$$
\|Mf\|_2^2 = \frac{1}{2}\|f\|_2^2 + \frac{1}{2}\mathrm{Re}\langle T_0 f, T_1 f \rangle
$$
where $\langle T_0 f, T_1 f \rangle = \sum_{s \in \mathbb{F}_p^*} a_{3s} \overline{a_s} \omega^{-s\gamma}$ (summing over modes $s$ with $3s$ defined in $\mathbb{F}_p^*$).

For $|\langle T_0 f, T_1 f\rangle|$ to be close to $\|f\|_2^2$, we need:
$$
\left| \sum_{s} a_{3s} \overline{a_s} \omega^{-s\gamma} \right| \approx \sum_s |a_s|^2
$$

This requires:
1. $|a_{3s}| \approx |a_s|$ for all $s$ (energy is roughly constant on $\langle 3 \rangle$-orbits).
2. $\arg(a_{3s}/a_s) \approx s\gamma + c$ (phases align with the "+1" translation).

**This is a sum-product type constraint:** The amplitude profile $|a_s|$ must be invariant under $\times 3$ (a multiplicative structure), while the phase profile must linearly track $s$ (an additive structure). Satisfying both simultaneously is "non-generic" -- this is the sum-product phenomenon at work.

---

## 6. A Proposed Proof Strategy

### 6.1. Overview

We propose a three-step approach that bypasses the quasirandomness failure:

**Step 1 (Non-concentration on affine subgroups).** Show that $\mu^{(n)}$ does not concentrate on any proper affine subgroup of the action on $\mathbb{F}_p$ (i.e., any coset $aH + b$ for proper $H \leq \mathbb{F}_p^*$).

**Step 2 (Flattening via sum-product).** Use the product theorem for $\mathrm{Aff}(\mathbb{F}_p)$ and the Balog-Szemeredi-Gowers lemma to show L^2 flattening of $\mu^{(n)}$ restricted to $V_{p-1}$.

**Step 3 (Dimension-based smoothing).** Instead of quasirandomness (which would give smoothing via $D$ over all representations), use the fact that $V_{p-1}$ has dimension $p-1$ to complete the mixing, replacing Phase 3 of B-G.

### 6.2. Step 1: Non-concentration

**Proposition (Non-concentration).** For any $n \geq C \log p$ and any proper coset $aH + b \subsetneq \mathbb{F}_p$ (where $H \leq \mathbb{F}_p^*$, $|H| \leq (p-1)/2$):
$$
\mu^{(n)}(aH + b) \leq |aH + b|^{-\eta}
$$
for some $\eta > 0$ depending on the generators.

**Proof sketch (standard argument).** After $n$ steps, the walk from $x_0 = 0$ reaches $x_n = \sum_{i : b_i = 1} \gamma \prod_{j > i} m_{b_j}$, which is a sum of random products. The key is the **escape from proper subgroups** property: the walk cannot be trapped in a coset because the translation $\gamma = 2^{-1}$ combined with the multiplicative action generates all of $\mathbb{F}_p$ (Lemma 3.8 of our paper).

More precisely, if the walk concentrated on $aH + b$, then $T_1(aH + b) \subseteq aH + b$ and $T_0(aH + b) \subseteq aH + b$. The condition $T_0(aH + b) \subseteq aH + b$ means $2^{-1}(aH + b) \subseteq aH + b$, i.e., $aH + b$ is invariant under $\times 2^{-1}$, which forces $H \supseteq \langle 2 \rangle$. The condition $T_1(aH + b) \subseteq aH + b$ additionally requires $3 \cdot 2^{-1}(aH + b) + 2^{-1} \subseteq aH + b$, which (with the multiplicative invariance) forces $H \supseteq \langle 2, 3 \rangle$. If $\langle 2, 3 \rangle = \mathbb{F}_p^*$, no proper coset is invariant.

When $\langle 2, 3 \rangle$ is a proper subgroup, the walk IS invariant on orbits $r \langle 2, 3 \rangle$ under the multiplicative part, but the translation breaks this invariance -- the "+1" moves points between different orbits. Quantifying this requires more care.

**This step is achievable** using standard arguments (Eskin-Mozes-Oh escape from subvarieties, or direct computation).

### 6.3. Step 2: L^2 flattening

This is the most challenging step. We need to show:

**Claim.** For some $n = O(\log p)$:
$$
\| \mu^{(n)} |_{V_{p-1}} \|_2^2 \leq C p^{-1}
$$

The standard B-G approach uses the Balog-Szemeredi-Gowers lemma: if $\|\mu^{(n)}\|_2^2$ is large, then $\mu^{(n)}$ is supported on an approximate subgroup. The product theorem then guarantees growth, contradicting the assumption.

**For our specific representation $V_{p-1}$:** The L^2 norm restricted to $V_{p-1}$ is:
$$
\| \mu^{(n)} |_{V_{p-1}} \|_2^2 = \sum_{r=1}^{p-1} |\hat{\mu}^{(n)}(r)|^2
$$

If this is large (say $\geq p^{-1+\alpha}$), then the mass of $\mu^{(n)}$ on $\mathbb{F}_p$ is "concentrated." The Fourier support $\{r : |\hat{\mu}^{(n)}(r)| \geq \tau\}$ forms a set $S$ with $|S| \cdot \tau^2 \leq 1$ and $|S| \tau^2 \geq p^{-1+\alpha}$.

However, $S$ is a subset of $\mathbb{F}_p^*$, not a subgroup of $\mathrm{Aff}(\mathbb{F}_p)$. The connection between the Fourier concentration of $\mu^{(n)}$ on $\mathbb{F}_p$ and the approximate subgroup structure in $\mathrm{Aff}(\mathbb{F}_p)$ is not immediate.

**The key technical challenge:** We need a variant of the B-G flattening argument that works within a single representation, using the product theorem for $\mathrm{Aff}(\mathbb{F}_p)$ to constrain the Fourier structure of $\mu^{(n)}$ on $\mathbb{F}_p$.

### 6.4. Step 3: Dimension-based smoothing

If Step 2 succeeds in bringing $\|\mu^{(n)}\|_{V_{p-1}}$ to the level $C p^{-1}$, then:
$$
|\hat{\mu}^{(n)}(r)|^2 \leq C p^{-1} \quad \text{for all } r
$$
which means $|\hat{\mu}^{(n)}(r)| \leq C^{1/2} p^{-1/2}$. Since $M$ contracts each Fourier mode by at most factor 1 (it's a contraction on $L^2$):
$$
|\hat{\mu}^{(n+k)}(r)| \leq |\hat{\mu}^{(n)}(r)|
$$

But we need something stronger: the spectral gap tells us that $|\hat{\mu}^{(n+k)}(r)| \leq |\lambda_2|^k \cdot |\hat{\mu}^{(n)}(r)|$, which is circular (we're trying to bound $|\lambda_2|$).

**Alternative:** Use the single-character contraction (Theorem 12). Once $\mu^{(n)}$ is expressed in the Fourier basis, each mode contracts by $1/\sqrt{2}$ per step -- but only if the modes don't interfere. The cross-terms introduce the difficulty.

However, once the L^2 norm is at level $O(p^{-1})$, the coefficients $a_r$ are all small ($|a_r| \leq C^{1/2} p^{-1/2}$), and the sum-product constraint from Section 5.4 becomes:
$$
\left| \sum_s a_{3s} \overline{a_s} \omega^{-s\gamma} \right| \leq \left(\sum_s |a_{3s}|^2\right)^{1/2} \left(\sum_s |a_s|^2\right)^{1/2} = \|f\|_2^2
$$

This is just Cauchy-Schwarz and gives no improvement. We need to exploit the phases $\omega^{-s\gamma}$ for cancellation.

---

## 7. The Key Technical Obstruction

### 7.1. Identifying the precise difficulty

The entire proof attempt reduces to the following:

**Core Lemma (Unproved).** Let $f = \sum_{r=1}^{p-1} a_r \chi_r$ with $\|f\|_2 = 1$. Then:
$$
\left| \sum_{s \in \mathbb{F}_p^*} a_{3s} \overline{a_s} \omega^{-s\gamma} \right| \leq 1 - c
$$
for a universal constant $c > 0$ (where $\gamma = 2^{-1}$).

**Equivalently:** $|\langle T_0 f, T_1 f \rangle| \leq 1 - c$ for all unit vectors $f \perp \mathbf{1}$, which immediately gives $\|Mf\|_2^2 \leq 1 - c/2$.

### 7.2. Why this is hard

The sum $\sum_s a_{3s} \overline{a_s} \omega^{-s\gamma}$ is a **bilinear exponential sum** with structured coefficients. For it to be close to $\sum |a_s|^2 = 1$, we need:

(i) $|a_{3s}| \approx |a_s|$ (the amplitude profile is nearly $\times 3$-invariant).
(ii) $\arg(a_{3s} / a_s) \approx s\gamma$ (the phase tracks the additive character).

Condition (i) means the spectral measure $|a_s|^2$ is approximately invariant under $\times 3$. Condition (ii) means the phase of $a_s$ is approximately a linear function of $s$, modulo the $\times 3$ action.

**The connection to Furstenberg's conjecture:** Condition (i) is reminiscent of measures on $\mathbb{R}/\mathbb{Z}$ invariant under $\times 3$ (Furstenberg's conjecture concerns measures simultaneously invariant under $\times 2$ and $\times 3$). The operator $M$ already makes the walk $\times 2$-equivariant (via $T_0$), so if $|a_s|^2$ were also $\times 3$-invariant, we would have a doubly-invariant measure. Furstenberg's conjecture (proved by Shmerkin 2019 in a measure-theoretic sense) says such measures are very constrained.

However, condition (ii) adds a phase constraint that goes beyond Furstenberg. Moreover, we need an explicit quantitative bound, not just a qualitative statement.

### 7.3. Partial results and what they suggest

**What we know:**
1. For **single Fourier modes** $f = \chi_r$: $|\langle T_0 \chi_r, T_1 \chi_r \rangle| = 0$ (orthogonal modes), so $\|M\chi_r\|^2 = 1/2$. The Core Lemma holds with $c = 1/2$.

2. For **orbit-constant functions** (f constant on $\langle 2 \rangle$-orbits): $|\langle T_0 f, T_1 f \rangle|$ can approach $\|f\|^2$ for some primes (Mersenne primes show this). But our Combined Theorem proves it can never actually equal $\|f\|^2$ (no unit-circle eigenvalues).

3. Numerically, $|\lambda_2| \approx 0.70$ for all primes tested. This suggests the Core Lemma holds with $c \approx 0.02$ (since $\|Mf\|^2 \leq 0.70^2 \approx 0.49 = 1/2 + (-0.01)$, meaning the cross-term is at most $\approx -0.02$... actually, let's be more precise: $0.70^2 = 0.49$, and $\|Mf\|^2 = 0.5 + 0.5 \cdot \text{Re}\langle T_0 f, T_1 f\rangle$, so $0.49 = 0.5 + 0.5 x$ gives $x = -0.02$. So we need $\text{Re}\langle T_0 f, T_1 f\rangle \leq 1 - 0.02$ at the operator level).

Actually this is wrong -- $|\lambda_2|^2 = 0.49$ is the eigenvalue squared, but $\|Mf\|^2 \leq |\lambda_2|^2 \|f\|^2$ only for eigenvectors, not for all $f$. The operator norm of $M$ on $V_{p-1}$ may be larger than $|\lambda_2|$.

### 7.4. A sum-product approach to the Core Lemma

**Strategy:** Show that conditions (i) and (ii) from Section 7.2 are incompatible using sum-product estimates.

If $|a_{3s}| \approx |a_s|$ for most $s$, then $\mathrm{supp}(|a_s|^2)$ is approximately $\times 3$-invariant. Combined with the constraint $\|f\|_2 = 1$, the support has $\sum |a_s|^2 = 1$, so the mass is spread over a set $S = \{s : |a_s| \geq \tau\}$ with $|S| \leq 1/\tau^2$.

If $S$ is approximately $\times 3$-invariant ($3S \approx S$), this is a strong structural constraint. By the sum-product theorem (Bourgain-Katz-Tao):

**Theorem (BKT).** For $A \subset \mathbb{F}_p$ with $|A| \leq p^{1-\delta}$: $|A + A| + |A \cdot A| \geq |A|^{1+\epsilon}$ for $\epsilon = \epsilon(\delta) > 0$.

If $3S \subset S$ and $|S| \leq p^{1-\delta}$, then $|S \cdot S| \leq |S|$ (since $S$ is closed under $\times 3$ and $S \subset \langle 3 \rangle \cdot S_0$ for some small $S_0$). The BKT theorem then implies $|S + S| \geq |S|^{1+\epsilon}$. Now condition (ii) requires the phases to track an additive character, which is compatible with additive structure. So there may be no contradiction from sum-product alone.

**The difficulty:** Conditions (i) and (ii) together might actually be satisfiable on a set of the right structure. The sum-product theorem constrains sets, but the coefficients $a_s$ are complex numbers with both amplitudes and phases. The interaction between amplitude ($\times 3$-invariance) and phase (additive character) may or may not be incompatible.

---

## 8. Alternative Approaches Worth Investigating

### 8.1. The Chung-Diaconis-Graham analogy

Chung, Diaconis, and Graham (1987) proved that the random walk $X_{n+1} = 2X_n + b_n \pmod{p}$ (where $b_n \in \{-1, 0, 1\}$ uniformly) mixes in $O(\log p \log \log p)$ steps for almost all odd $p$.

**Key insight from CDG:** The mixing time depends on the entropy of the corresponding Bernoulli convolution. Specifically, the mixing time is $(c + o(1)) \log_2 p$ where $c = \log 2 / h$ and $h$ is the entropy of the self-similar measure associated with the IFS $x \mapsto x/2 \pm 1/(2p)$.

**For our walk:** The IFS is $x \mapsto x/2$ and $x \mapsto (3x+1)/(2p)$, which is NOT a self-similar IFS in the classical sense (the contraction ratios differ: $1/2$ vs $3/2$). However, for the purpose of mixing on $\mathbb{F}_p$, the relevant quantity is the "effective entropy rate" per step.

The CDG result is proven via **Fourier analysis** (bounding $|\hat{\mu}^{(n)}(r)|$ for each $r$), not via B-G expansion. Their bound:
$$
|\hat{\mu}^{(n)}(r)| = \prod_{k=0}^{n-1} \left| \frac{1}{3}(1 + 2\cos(2\pi r \cdot 2^k / p)) \right|
$$
decays exponentially because the angles $2\pi r \cdot 2^k / p$ equidistribute (for most $r$ and $p$).

**For our walk:** The analogous product would be:
$$
|\hat{\mu}^{(n)}(r)| \leq \prod_{k} \left| \frac{1}{2}(1 + \omega^{r_k \gamma}) \right|
$$
where $r_k$ is the mode at step $k$. But because $M$ couples modes (it's not diagonal in Fourier space), this product formula doesn't hold. The coupling is the fundamental difficulty.

### 8.2. Self-similar measures and entropy

The walk on $\mathbb{F}_p$ is the finite-field analogue of the iterated function system:
$$
x \mapsto \frac{x}{2} \quad \text{or} \quad x \mapsto \frac{3x+1}{2}
$$
on $\mathbb{R}$, each with probability $1/2$. The stationary measure $\nu$ on $\mathbb{R}$ (if it exists as a probability measure, which it doesn't since the IFS is expanding in one branch) is a self-affine measure.

The **Bernoulli convolution** perspective: consider the random variable $Y = \sum_{k=0}^{\infty} b_k \prod_{j=0}^{k-1} m_{b_j}^{-1} \cdot \gamma$, where $b_k \in \{0, 1\}$ and $m_0 = 1/2, m_1 = 3/2$. This is an infinite random product of affine maps, and its distribution is a generalized Bernoulli convolution.

By Hochman's theorem on self-similar measures (2014), such measures have dimension equal to the minimum of 1 and $h / \chi$, where $h$ is the entropy and $\chi$ is the Lyapunov exponent, **provided there are no exact overlaps**. In our case, $h = \log 2$ (entropy of the fair coin) and $\chi = \frac{1}{2}(\log 2 + \log(3/2)) = \frac{1}{2}\log 3$. So $h/\chi = 2\log 2/\log 3 \approx 1.26 > 1$, meaning the measure should be absolutely continuous on $\mathbb{R}$.

This suggests that the finite-field walk should equidistribute rapidly (the "analytic" dimension exceeds 1), which is consistent with a constant spectral gap. However, translating this heuristic into a rigorous proof for $\mathbb{F}_p$ requires controlling the discrepancy between the real-line IFS and its mod-$p$ reduction.

### 8.3. Direct L^2 flattening via additive combinatorics

Instead of going through the B-G machine, one could try to prove L^2 flattening directly using the specific structure of our walk.

**Proposition (Two-step contraction).** For each $r \neq 0$:
$$
\|M^2 \chi_r\|_2^2 \leq \frac{3}{8} + O(1/p^2) < \frac{1}{2}
$$

This was established in our analysis (phase decoherence in $M^2$). The improvement from $1/2$ (one-step) to $3/8$ (two-step) comes from the phases $\omega^{r\gamma}$ providing cancellation in the cross-terms between the two steps.

**The obstruction for superpositions:** While $\|M^2 \chi_r\|^2 \leq 3/8$ for individual characters, for general $f = \sum a_r \chi_r$, we have $\|M^2 f\|^2$ depending on cross-terms between different $r$. The operator norm of $M^2$ on $V_{p-1}$ involves controlling all these cross-terms simultaneously.

**A potential approach:** Show that the operator norm of $M^k$ on $V_{p-1}$ satisfies:
$$
\|M^k\|_{\mathrm{op}}^2 \leq \frac{1}{2} + \frac{1}{2} \cdot \rho(k)
$$
where $\rho(k) \to 0$ as $k \to \infty$ at a rate **independent of $p$**. The quantity $\rho(k)$ measures the worst-case cross-term alignment, and the claim is that after $O(1)$ steps, the phases from "+1" decorrelate the cross-terms.

The difficulty: $\rho(k)$ involves sums of the form $\sum_{s \in S_k} a_s \overline{a_{s'}} \omega^{s \cdot \text{(translation term)}}$, where $S_k$ is a complicated set determined by the $k$-step orbit structure. Controlling these for arbitrary coefficients $a_s$ requires exponential sum estimates that depend on the arithmetic of $p$.

---

## 9. Assessment and Remaining Gaps

### 9.1. Summary of what the literature provides

| Tool | What it gives | Limitation for our problem |
|------|--------------|---------------------------|
| Bourgain-Gamburd machine | Constant spectral gap for quasirandom groups | $\mathrm{Aff}(\mathbb{F}_p)$ is NOT quasirandom (has $p-1$ one-dimensional reps) |
| Lindenstrauss-Varju | Spectral gap for $\mathbb{F}_p^d \rtimes \mathrm{SL}_d(\mathbb{F}_p)$ from the linear part's gap | Our linear part ($\mathbb{F}_p^*$) has gap $O(1/p)$, giving only $O(1/p)$ for the affine part |
| Golsefidy-Varju (perfectness) | Expansion iff Zariski closure is perfect | $\mathrm{Aff}_1$ is NOT perfect; predicts failure for the walk on $\mathrm{Aff}(\mathbb{F}_p)$ (but NOT for the action on $\mathbb{F}_p$) |
| Product theorem for $\mathrm{Aff}(\mathbb{F}_p)$ | Slowly growing sets have small multiplicative projection | Gives combinatorial growth, but needs quasirandomness for Phase 3 |
| CDG mixing for $x \mapsto 2x + b$ | $O(\log p)$ mixing for a related affine walk | Different walk structure (additive noise $b \in \{-1,0,1\}$ vs. our specific "+1") |
| Single-character contraction (Theorem 12) | $\|M\chi_r\|^2 = 1/2$ for all $r \neq 0$ | Does not extend to superpositions (cross-terms) |
| No unit-circle eigenvalues (Combined Thm) | $|\lambda_2| < 1$ for each $p$ | No uniformity in $p$; purely qualitative |

### 9.2. The precise technical gap

The proof attempt stalls at the following point:

**The needed estimate (Core Lemma, restated):** For the operator $M$ on $V_{p-1} \subset L^2(\mathbb{F}_p)$:
$$
\|M\|_{\mathrm{op}} \leq 1 - c \quad \text{for a universal } c > 0.
$$

Equivalently, for all $f \in V_{p-1}$ with $\|f\| = 1$:
$$
\mathrm{Re}\langle T_0 f, T_1 f \rangle \leq 1 - 2c.
$$

**What would suffice:** Any ONE of the following:

(A) **Sum-product for phases:** Show that for any unit vector $(a_s)_{s \in \mathbb{F}_p^*}$, the bilinear sum $|\sum_s a_{3s} \bar{a}_s \omega^{-s\gamma}| \leq 1 - c$. This requires mixing between the multiplicative structure ($\times 3$ permutation of indices) and the additive phase ($\omega^{-s\gamma}$). Existing sum-product estimates (BKT, Garaev) handle sets, not arbitrary complex coefficients.

(B) **Multi-step flattening:** Show that $\|M^k\|_{\mathrm{op}} \leq (1 - c)^k$ for some fixed $k$ independent of $p$. This would follow from a $k$-step version of the cross-term analysis, requiring that the accumulated phases from $k$ applications of "+1" provide enough cancellation. The difficulty grows with $k$ because the orbit structure becomes more complicated.

(C) **Spectral gap of the Bernoulli convolution operator:** Identify the "limiting operator" as $p \to \infty$ (on $L^2(\mathbb{R}/\mathbb{Z})$ or an adelic space) and show it has spectral radius $< 1$ on the non-constant subspace. Then transfer the spectral gap back to $\mathbb{F}_p$ for $p$ large. For small $p$, verify computationally.

### 9.3. Approaches NOT yet tried

1. **Hochman's theorem on entropy of self-similar measures:** The entropy $h > \chi/2$ condition (which is satisfied for our IFS) implies absolute continuity of the stationary measure on $\mathbb{R}$. Can this be adapted to give a spectral gap bound on $\mathbb{F}_p$?

2. **Varjú's work on Bernoulli convolutions:** Varjú (2019) proved that $\nu_\lambda$ is absolutely continuous for a.e. $\lambda \in (1/2, 1)$, using entropy methods. Our walk corresponds to a parameter $\lambda$ that varies with $p$ (the contraction ratio of the IFS modulo $p$).

3. **Additive energy bounds:** Instead of controlling the bilinear sum directly, bound the additive energy $E^+(S) = |\{(a,b,c,d) \in S^4 : a+b = c+d\}|$ of the level sets of $|a_s|^2$. If the energy is small (which the $\times 3$ invariance combined with additive phase should force), then the bilinear sum is bounded.

4. **Transfer to $\mathbb{R}/\mathbb{Z}$:** Study the operator $(Mf)(x) = \frac{1}{2}f(x/2) + \frac{1}{2}f((3x+1)/2)$ on $L^2(\mathbb{R}/\mathbb{Z})$. If this operator has spectral radius $\rho < 1$ on $L_0^2$, then for large enough $p$, the finite-field version inherits $|\lambda_2| \leq \rho + o(1)$.

5. **Representation-theoretic B-G for a single large representation:** Develop a variant of the B-G machine that works for a SINGLE high-dimensional representation, using its dimension as the quasirandomness constant. This would require adapting the flattening argument to work within a single representation space rather than over the entire group algebra.

---

## 10. Conclusion

### 10.1. What the Bourgain-Gamburd framework tells us

The B-G expansion machine, in its standard form, does not apply to our problem because the affine group $\mathrm{Aff}(\mathbb{F}_p)$ is solvable and far from quasirandom. The most relevant existing results are:

- **Lindenstrauss-Varju (2016):** Reduces the affine spectral gap to the linear part's spectral gap. In our case, the linear part has gap $O(1/p)$, so this gives only our existing weak bound.
- **Golsefidy-Varju (2012):** The perfectness criterion predicts non-expansion for $\mathrm{Aff}(\mathbb{F}_p)$ as a family, but this does not preclude a constant spectral gap for the action on $\mathbb{F}_p$ (which involves only the unique large representation).
- **Product theorem for $\mathrm{Aff}(\mathbb{F}_p)$ (Helfgott-Rudnev-Shkredov):** Provides the combinatorial Phase 2 ingredient, but cannot be deployed without a Phase 3 substitute.

### 10.2. The true nature of the problem

The constant spectral gap, if it exists, arises from the interaction of:
- **Multiplicative dynamics** ($\times 2$ and $\times 3$ on Fourier modes)
- **Additive phases** (the "+1" translation contributing phases $\omega^{r\gamma}$)
- **The sum-product phenomenon** (these two structures cannot simultaneously be exploited by an eigenvector)

The problem sits at the intersection of:
- Spectral theory of random walks on solvable groups
- Sum-product estimates over finite fields
- Self-similar measures and Bernoulli convolutions
- Furstenberg's $\times 2, \times 3$ conjecture

No existing theorem in the literature directly gives the desired result. The most promising approaches are:
1. **(Approach C, Section 9.3)** Transferring spectral gap from the real-line operator to $\mathbb{F}_p$.
2. **(Approach E, Section 9.3)** Developing a single-representation variant of B-G using dimension $p-1$ as a substitute for quasirandomness.
3. **(Direct)** Proving the Core Lemma (Section 7.1) via additive combinatorics / sum-product estimates for bilinear forms.

### 10.3. Recommended next steps

1. **Study the real-line operator** $(Mf)(x) = \frac{1}{2}f(x/2) + \frac{1}{2}f((3x+1)/2)$ on $L^2(\mathbb{R}/\mathbb{Z})$. Compute its spectral radius numerically. If $\rho < 1$, this provides the "target" spectral gap and suggests a transfer argument.

2. **Develop bilinear sum-product estimates:** Prove that $|\sum_s a_{3s} \bar{a}_s \omega^{-s\gamma}| \leq (1 - c)\sum |a_s|^2$ for arbitrary complex coefficients, using the non-commutativity of addition and multiplication in $\mathbb{F}_p$. This is a strengthening of the classical sum-product estimate to bilinear forms with phases.

3. **Multi-step operator norm:** Compute $\|M^k\|_{\mathrm{op}}$ for $k = 2, 3, 4$ analytically (not just for single characters but for all of $V_{p-1}$). If $\|M^2\|_{\mathrm{op}} < 1 - c$ uniformly, the problem is solved with two steps.

4. **Explore entropy methods:** Apply Hochman-Varjú entropy techniques for self-similar measures to the finite-field setting. The entropy rate $h/\chi = 2\log 2/\log 3 > 1$ suggests absolute continuity (constant spectral gap), but making this rigorous requires new tools.

---

## References

- [BG08] J. Bourgain, A. Gamburd, "Uniform expansion bounds for Cayley graphs of SL_2(F_p)," *Ann. Math.* 167 (2008), 625-642. [Link](https://annals.math.princeton.edu/wp-content/uploads/annals-v167-n2-p07.pdf)
- [BKT04] J. Bourgain, N. Katz, T. Tao, "A sum-product estimate in finite fields, and applications," *GAFA* 14 (2004), 27-57. [arXiv:math/0301343](https://arxiv.org/abs/math/0301343)
- [BGS10] J. Bourgain, A. Gamburd, P. Sarnak, "Affine linear sieve, expanders, and sum-product," *Invent. Math.* 179 (2010), 559-644. [Link](https://link.springer.com/article/10.1007/s00222-009-0225-3)
- [BGT11] E. Breuillard, B. Green, T. Tao, "Approximate subgroups of linear groups," *GAFA* 21 (2011), 774-819. [Link](https://link.springer.com/article/10.1007/s00039-011-0122-y)
- [Br12] E. Breuillard, "Approximate groups and the Bourgain-Gamburd machine," PCMI 2012 Lecture Notes. [PDF](https://www.math.utah.edu/pcmi12/lecture_notes/breuillard4.pdf)
- [CDG87] F. Chung, P. Diaconis, R. Graham, "Random walks arising in random number generation," *Ann. Probab.* 15 (1987), 1148-1165. [Link](https://projecteuclid.org/euclid.aop/1176992088)
- [Con] K. Conrad, "Representations of Aff(F_q) and Heis(F_q)," expository note. [PDF](https://kconrad.math.uconn.edu/blurbs/grouptheory/affineheisrep.pdf)
- [GV12] A. Salehi Golsefidy, P. Varju, "Expansion in perfect groups," *GAFA* 22 (2012), 1832-1891. [arXiv:1108.4900](https://arxiv.org/abs/1108.4900)
- [LV16] E. Lindenstrauss, P. Varju, "Spectral gap in the group of affine transformations over prime fields," *Ann. Fac. Sci. Toulouse Math.* 25 (2016), 969-993. [arXiv:1409.3564](https://arxiv.org/abs/1409.3564)
- [RS22] M. Rudnev, I. Shkredov, "On growth rate in SL_2(F_p), the affine group and sum-product type implications," *Mathematika* 68 (2022), 39-70. [arXiv:1812.01671](https://arxiv.org/abs/1812.01671)
- [Tao15] T. Tao, *Expansion in finite simple groups of Lie type*, GSM 164, AMS, 2015. [Blog notes](https://terrytao.wordpress.com/2012/01/13/254b-notes-4-the-bourgain-gamburd-expansion-machine/)
- [Var19] P. Varju, "On the dimension of Bernoulli convolutions for all transcendental parameters," *Ann. Math.* 189 (2019), 1001-1011.
