# Task: Structured Non-Divisibility for {a,b}-Smooth Sums

## Problem Statement

**Prove or make progress toward:**

Let $a, b \geq 2$ be multiplicatively independent integers (e.g., $a = 2, b = 3$). For integers $p > k \geq 1$ with $a^p > b^k$, define:

$$D = a^p - b^k, \qquad S(I) = \sum_{j=1}^{k} b^{k-j} \cdot a^{i_j}$$

where $I = \{i_1 < i_2 < \cdots < i_k\} \subseteq \{0, 1, \ldots, p-1\}$ is a $k$-element subset.

**Conjecture.** For $k/p$ sufficiently close to $\log a / \log b$ (within $O(p^{-10})$, say) and $p$ sufficiently large, there is no subset $I$ with $D \mid S(I)$.

**Origin.** This is the Collatz no-nontrivial-cycles conjecture in its arithmetic form. A cycle of the compressed Collatz map $T(n) = n/2$ (even) or $(3n+1)/2$ (odd) with period $p$ and $k$ odd steps at positions $I$ exists if and only if $D \mid S(I)$ and $S(I)/D \geq 1$, with $a = 2, b = 3$.

---

## What makes this hard (and what has been tried)

### The 5% margin

$\binom{p}{k} \approx 2^{0.95p}$ candidate subsets. $D \approx 2^p$. Heuristic probability of divisibility: $2^{0.95p} / 2^p = 2^{-0.05p} \to 0$. The conjecture is "barely true" — only a 5% margin separates the number of candidates from the modulus.

### The abc barrier

Every known approach decomposes $D \mid S$ into conditions modulo individual primes $q \mid D$. Per-prime equidistribution is proved:

$$P(q \mid S(I)) = 1/q + O(e^{-cp}) \quad \text{for primes } q \text{ with } \text{ord}_q(a) > \sqrt{q}$$

Combining across primes via sieve gives: $\#\{I : D \mid S\} \lesssim \binom{p}{k} / \text{rad}(D)$. This proves the conjecture IF $\text{rad}(D) > \binom{p}{k}$, which is the abc conjecture applied to $a^p = b^k + D$. Unconditionally, the best known bound is $\log \text{rad}(D) \geq c\sqrt{p}/\log p$ (Stewart 2013), exponentially short of the needed $0.95p$.

**Fourteen rounds of systematic exploration** (spectral gap theory, carry analysis, prime-power sieves, cyclotomic methods, function-field lifts, 2-adic analysis, coupling arguments, thermodynamic formalism) all reduce to the same barrier. See the project map at `map.md` for the full record.

### The meta-theorem (why size-counting always fails)

Any method that treats $S(I)$ and $D$ as "generic" integers of their respective sizes needs to certify that $\sim 2^{0.95p}$ random trials don't hit a target of size $2^p$. Making this rigorous for the specific $S$ and $D$ requires controlling their arithmetic interaction, which is abc. This applies to every framework that doesn't exploit the specific algebraic structure of $S$.

---

## What a solution must exploit

$S(I)$ is NOT a generic integer. It has rigid structure:

### Structural property 1: All terms positive, {a,b}-smooth

$S(I) = \sum b^{k-j} a^{i_j}$ is a sum of $k$ terms, each of the form $b^{\alpha} a^{\beta}$ with $\alpha + \beta < p + k$. All terms are positive (no cancellation). Each term is $\{a,b\}$-smooth.

### Structural property 2: Geometric coefficients

The coefficient of $a^{i_j}$ is $b^{k-j}$, which depends on the RANK of $i_j$ among the selected positions. The weights form a geometric progression $b^{k-1}, b^{k-2}, \ldots, b, 1$. After the reversal $j \to k+1-j$, rank-dependence is removed: $S(I) = \sum_{j=1}^k b^{j-1} a^{i'_j}$ with $i'_1 > \cdots > i'_k$.

### Structural property 3: Elementary symmetric function

(Proved in this project, file `collatz_charsum.md`.) For Fourier analysis modulo a prime $q$:

$$F(t) = \sum_{|I|=k} e^{2\pi i t S(I)/q} = e_k(\gamma_0, \ldots, \gamma_{p-1})$$

where $\gamma_r = e^{2\pi i t b^{k-1} a^r / q}$ and $e_k$ is the $k$-th elementary symmetric polynomial. This gives the Weil-type bound $|F(t)| \leq \binom{p}{k} q^{-1/2}$, which is the equidistribution theorem.

### Structural property 4: The divisor has matching structure

$D = a^p - b^k$ is itself a difference of $\{a,b\}$-smooth numbers. The cycle equation says: "an $\{a,b\}$-smooth sum with geometric weights is divisible by an $\{a,b\}$-smooth difference." Both sides live in the multiplicative world of $\langle a, b \rangle$.

### Structural property 5: Dynamical origin

$S(I)/D = n_0$ is the starting value of an actual orbit of the map $T$. The positions $I$ encode which steps are odd. The divisibility is not an arbitrary number-theoretic coincidence — it's the closure condition of a dynamical orbit.

---

## The precise mathematical task

**Find a technique that proves a quantitative non-vanishing of $S(I) \bmod D$ using the structure of $S$, without decomposing $D$ into prime factors.**

More formally, prove one of:

### Target A (ideal): Non-divisibility theorem

For all $p \geq p_0$ and all $k$-element subsets $I \subset \{0, \ldots, p-1\}$ with $k = \lfloor p \log 2 / \log 3 \rfloor$: $D \nmid S(I)$ where $D = 2^p - 3^k$.

### Target B (strong partial): Non-vanishing lower bound

For all nontrivial $I$: $|S(I) \bmod D| \geq D^{1-\varepsilon}$ for some $\varepsilon < 1$. (This would show $S(I)/D$ is not an integer for large $p$.)

### Target C (useful partial): Structural incompatibility

Prove a structural theorem of the form: "If $\sum b^{k-j} a^{i_j} \equiv 0 \pmod{a^p - b^k}$, then the subset $I$ must satisfy [some impossible condition]." The impossible condition could be number-theoretic (e.g., requiring specific congruences that $I$ can't satisfy) or combinatorial (e.g., requiring a spacing pattern incompatible with $k/p \approx \log a/\log b$).

### Target D (new framework): Effective S-unit non-divisibility

Prove: for $S$-units $x_1, \ldots, x_k \in \langle a, b \rangle$ with geometric structure ($x_j = b^{k-j} a^{i_j}$, positions ordered), the sum $\sum x_j$ has $\text{ord}_D(\sum x_j) = 0$, where $D = a^p - b^k$. This would be a new type of result in the theory of $S$-unit equations — an effective non-vanishing modulo a specific modulus, rather than the traditional finiteness of solutions.

---

## Known results and tools that come closest

| Result | What it gives | Why it falls short |
|---|---|---|
| Baker's theorem (linear forms in logarithms) | $\|S\| \geq \exp(-C p^{1/2} \log p)$ (archimedean) | Archimedean bound, not $D$-adic. Gap: $\sqrt{p}$ vs $p$. |
| Subspace Theorem (Schmidt-Schlickewei) | Finiteness of $S$-unit equation solutions | Ineffective. Can't exclude specific solutions. |
| Corvaja-Zannier (2004) | $\#\{x : (x^p - b^k) \mid f(x)\}$ is finite | Ineffective (Thue-Siegel-Roth type). |
| Equidistribution mod $q$ (Theorem 4) | $P(q \mid S) = 1/q + O(e^{-cp})$ per prime $q$ | Can't combine: needs $\text{rad}(D)$ large (abc). |
| BGK character sums (Theorem 17) | Constant spectral gap for density-1 primes | Spectral gap ≠ no-cycles (still needs sieve). |
| Mason-Stothers (function-field abc) | $D(x,y) \nmid S_I(x,y)$ in $\mathbb{Z}[x,y]$ | Polynomial non-div doesn't imply integer non-div. |
| Mihailescu (Catalan's conjecture) | $2^p - 3^k = 1$ only for $(p,k) = (3,2)$ | Requires $D = 1$. For $D \gg 1$: class group absorbs constraints. |
| Carry Weight Identity (this project) | $W_c = \sum s_1(3^m) - s_1(n_0 D) = \Theta(p^2)$ | Equivalent to cycle equation (no new constraint). |

## What a solution would look like

It would be a proof that operates **natively at the scale of $D$** (exponential in $p$) without decomposing into primes. It would use the fact that $S(I)$ is a structured sum (geometric weights, ordered positions, $\{a,b\}$-smooth terms) rather than a generic integer. And it would establish that this structure is **incompatible** with divisibility by $D = a^p - b^k$.

The closest analogy in known mathematics: Mihailescu's proof that $2^p - 3^k \neq 1$ for $(p,k) \neq (3,2)$. That proof works at exponential scale by using the cyclotomic factorization of $a^p - b^k$ in $\mathbb{Q}(\zeta_p, b^{1/p})$ and forcing the factors to be units — but this technique fails when $D \gg 1$ because the factors are no longer units.

A solution to our problem would likely require a new algebraic or analytic framework that can handle "divisibility of structured sums by large smooth differences" — a capability that does not currently exist in the mathematical literature.

---

## Project context

This task emerges from a systematic multi-session research project on the Collatz conjecture. The full project (including 17 proved theorems, 20+ agent analyses, and a complete record of all approaches tried) is at:

- Problem decomposition map: `map.md`
- All theorems with proofs: `theorems_and_proofs.md`
- Agent analyses: `agent_*.md`
- Session log: `session_log.md`

The project has exhausted all known mathematical frameworks (spectral theory, sieve theory, algebraic number theory, $p$-adic analysis, carry analysis, thermodynamic formalism, polynomial methods). Every approach reduces to the same barrier. This task — finding a structure-exploiting method — is identified as the **true frontier** of the problem.
