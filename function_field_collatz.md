# The Function Field Collatz Analogy and the Ostrowski Obstruction

*Developed 2026-03-06 (Session 8)*

## 0. Executive Summary

The Collatz cycle equation has a natural analogue over function fields $\mathbb{F}_q[t]$, where it is **trivially unsolvable** by degree comparison. This gives a one-line proof of "no cycles" over function fields. The proof does not lift to $\mathbb{Z}$ because of Ostrowski's theorem: no non-archimedean absolute value on $\mathbb{Q}$ can have $|2| > 1$.

This analysis identifies the **precise mathematical obstruction** to proving the integer Collatz conjecture: the need for an absolute value that is simultaneously ultrametric (to bound the degree of sums) and has $|2| > 1$ (to create the degree gap). Over $\mathbb{F}_q(t)$, the place at infinity provides this. Over $\mathbb{Q}$, Ostrowski says it cannot exist.

A proof of the integer Collatz conjecture would need to circumvent Ostrowski — either by working in a larger ring, by replacing absolute values with a different structure, or by finding a completely different proof strategy.

---

## 1. The Function Field Collatz

### 1.1. Setup

Let $\mathbb{F}_q$ be a finite field, $\alpha \in \mathbb{F}_q^*$ with $\alpha \neq 1$. Define the function field analogues:

| Integer Collatz | Function Field Collatz |
|---|---|
| Base $a = 2$ | Uniformizer $t$ |
| Multiplier $b = 3$ | Constant $\alpha \in \mathbb{F}_q^*$ |
| "Even" = $2 \mid n$ | "$t$ divides $f$" |
| "Odd" = $2 \nmid n$ | $f(0) \neq 0$ |
| $D = 2^p - 3^k$ | $D = t^p - \alpha^k$ |
| $S(I) = \sum 3^{k-j} \cdot 2^{i_j}$ | $S(I) = \sum \alpha^{k-j} \cdot t^{i_j}$ |

The cycle equation over $\mathbb{F}_q[t]$: does $D \mid S(I)$ for some $k$-subset $I = \{i_1 < \ldots < i_k\} \subseteq \{0, \ldots, p-1\}$?

### 1.2. The One-Line Proof

**Theorem (Function Field Collatz).** For all valid $(p,k)$ and all $k$-subsets $I \subseteq \{0, \ldots, p-1\}$: $D \nmid S(I)$ in $\mathbb{F}_q[t]$.

*Proof.*
$$\deg(S(I)) = \max_j\, i_j = i_k \leq p - 1 < p = \deg(D)$$
Since $S(I) \neq 0$ (it has $k$ distinct monomials $t^{i_j}$ with nonzero coefficients $\alpha^{k-j}$) and $\deg(S) < \deg(D)$, divisibility $D \mid S$ is impossible. $\square$

### 1.3. Why It Works

The degree function on $\mathbb{F}_q[t]$ satisfies three properties simultaneously:

**(A) Ultrametric inequality:** $\deg(f + g) \leq \max(\deg f, \deg g)$

**(B) Degree gap:** Each term $\alpha^{k-j} \cdot t^{i_j}$ has $\deg = i_j \leq p-1$, so $\deg(S) \leq p-1 < p = \deg(D)$. The coefficient $\alpha^{k-j} \in \mathbb{F}_q^*$ has degree 0 — **constants are free**.

**(C) Divisibility constraint:** If $f \mid g$ in $\mathbb{F}_q[t]$ with $g \neq 0$, then $\deg(f) \leq \deg(g)$.

From (A)+(B): $\deg(S) \leq p-1$.
From (C)+(D|S): $\deg(D) \leq \deg(S)$, i.e., $p \leq \deg(S)$.
Combined: $p \leq p - 1$. Contradiction.

---

## 2. Why It Doesn't Lift to $\mathbb{Z}$

### 2.1. The Coefficient Problem

Over $\mathbb{Z}$: the "coefficients" $3^{k-j}$ are NOT free. They have size $\approx 3^k \approx 2^{0.631 \cdot 1.585 \cdot p} \approx 2^p \approx D$.

The term $3^{k-j} \cdot 2^{i_j}$ has $\log_2 \approx i_j + (k-j) \cdot \log_2 3$. For $j=1$ with $i_1 \geq 1$:

$$\log_2(\text{term}_1) \geq 1 + (k-1)\log_2 3 \approx 1 + p - 1.585 \approx p$$

Individual terms of $S(I)$ can **exceed** $D$ in size. Over $\mathbb{F}_q[t]$, this never happens because constants have degree 0. Over $\mathbb{Z}$, the "constants" ($3^{k-j}$) are exponentially large.

### 2.2. The Ostrowski Obstruction

To lift the function field proof, we would need a "degree" function $\delta: \mathbb{Z} \to \mathbb{R}$ satisfying:

**(A)** Ultrametric: $\delta(\sum a_i) \leq \max_i \delta(a_i)$

**(B)** Gap: $\delta(3^{k-j} \cdot 2^{i_j}) \leq p - 1$ and $\delta(D) = p$. This requires $\delta$ to "see" only the power of 2, treating $3^{k-j}$ as invisible.

**(C)** Divisibility: $d \mid n$ implies $\delta(d) \leq \delta(n)$

Condition (B) requires $\delta(2) = c > 1$ (so $\delta(2^{i_j}) = c^{i_j}$ grows with $i_j$) and $\delta(3) = 1$ (so $3^{k-j}$ is invisible).

Condition (A) requires $\delta$ to be non-archimedean.

**Ostrowski's Theorem** (1916): Every non-trivial absolute value on $\mathbb{Q}$ is equivalent to either the archimedean absolute value $|\cdot|_\infty$ or a $p$-adic absolute value $|\cdot|_p$.

For any non-archimedean absolute value on $\mathbb{Q}$:
$$|2| = |1 + 1| \leq \max(|1|, |1|) = 1$$

Therefore $|2| \leq 1$, contradicting $\delta(2) > 1$.

**The function field proof requires a non-archimedean absolute value with $|2| > 1$ and $|3| = 1$. Ostrowski says this cannot exist on $\mathbb{Q}$.**

### 2.3. The Gap-Constraint Dichotomy

Over $\mathbb{Q}$, two natural measures capture different halves of the proof:

| Measure | Gap ($\delta(S) < \delta(D)$)? | Constraint ($D \mid S \Rightarrow \delta(D) \leq \delta(S)$)? |
|---|---|---|
| $\log\|\cdot\|$ (archimedean) | NO: $\log S \approx 2p > p \approx \log D$ | YES: $d \mid n \Rightarrow \|d\| \leq \|n\|$ |
| $v_2$ (2-adic, "bottom") | NO: $v_2(S) = i_1 \geq 0 = v_2(D)$ | YES: $d \mid n \Rightarrow v_2(d) \leq v_2(n)$ |
| Highest bit ("top") | YES: highest bit of terms $\leq p - 1 < p$ | NO: highest bit of $S$ can exceed highest bit of $D$ via carries |
| Function field degree | YES: $\deg(S) \leq p - 1 < p = \deg(D)$ | YES: $f \mid g \Rightarrow \deg f \leq \deg g$ |

**The "top" measure gives the gap but not the constraint. The "bottom" measure gives the constraint but not the gap. No single measure on $\mathbb{Q}$ gives both.**

The function field degree gives both because it combines the ultrametric property (bounding the top) with multiplicativity (ensuring divisibility respects the measure).

---

## 3. The Precise Breaking Point

### 3.1. Specialization

The function field $\mathbb{F}_q(t)$ has a "place at infinity" $|\cdot|_\infty$ where:
- $|t|_\infty = q > 1$ (the uniformizer has absolute value $> 1$)
- $|\alpha|_\infty = 1$ for all $\alpha \in \mathbb{F}_q^*$ (constants have absolute value 1)
- The absolute value is **ultrametric**

When we "specialize" $t \to 2$ (to pass from $\mathbb{F}_q[t]$ to $\mathbb{Z}$), the place at infinity maps to the archimedean absolute value on $\mathbb{Q}$:
- $|2|_\infty = 2 > 1$ (preserved)
- $|3|_\infty = 3 \neq 1$ (**NOT preserved** — constants are no longer "free")
- The absolute value is **NOT ultrametric** (broken)

**Two things break simultaneously:**
1. The ultrametric property (needed for $\deg(\text{sum}) \leq \max$)
2. The invisibility of $3$ (needed for the degree gap)

Both are consequences of the same structural fact: over $\mathbb{Z}$, there is no completion where $2$ and $3$ play asymmetric roles with the right properties.

### 3.2. The Role of $\log_2 3$ Being Irrational

Over $\mathbb{F}_q[t]$: the "irrationality" of $t$ relative to $\alpha$ is absolute — $t$ and $\alpha$ live in different "worlds" (the polynomial variable vs the coefficient field). The degree function perfectly separates them.

Over $\mathbb{Z}$: $\log_2 3$ is irrational (proved by antiquity), meaning $2^a \neq 3^b$ for any positive integers $a, b$. But $2$ and $3$ live in the **same** ring ($\mathbb{Z}$), so no absolute value can fully separate them. The irrationality of $\log_2 3$ prevents exact cancellation ($2^p \neq 3^k$) but doesn't prevent approximate equality ($2^p \approx 3^k$), which is what makes $D$ small relative to its terms.

---

## 4. What Would Circumvent Ostrowski

### 4.1. Extend the Ring

Ostrowski applies to $\mathbb{Q}$. If we embed $\mathbb{Z}$ into a larger ring $R$ where:
- $R$ admits a non-archimedean absolute value $|\cdot|_R$ with $|2|_R > 1$ and $|3|_R = 1$
- The divisibility $D \mid S$ in $\mathbb{Z}$ lifts to a divisibility in $R$
- The degree gap $\delta(S) < \delta(D)$ holds in $R$

Then the function field proof would work in $R$.

**Candidates:**
- **$\mathbb{Z}[[x]]$ with $x = 2$**: Power series ring. Has a "degree" (order of vanishing), but this is $v_2$, which gives $|2| < 1$.
- **$\mathbb{F}_1$-geometry**: If $\mathbb{Z}$ could be viewed as $\mathbb{F}_1[t]$ (polynomials over the "field with one element"), it would have a natural degree function. But $\mathbb{F}_1$-geometry is incomplete and the notion of "degree" is not established.
- **Non-standard models**: In a non-standard extension ${}^*\mathbb{Z}$, there might be non-standard absolute values. But transfer principle would prevent new results about standard integers.

### 4.2. Replace Absolute Values with a Filtration

Instead of an absolute value, define a **filtration** on $\mathbb{Z}$-modules that captures the "smooth degree":

$$F^n = \{m \in \mathbb{Z} : m = \sum_{i \leq n} c_i \cdot 2^i \cdot 3^{d_i} \text{ for some } c_i, d_i\}$$

This is the set of integers expressible as smooth sums with $2$-exponents $\leq n$. Then:
- $S(I) \in F^{p-1}$ (since all terms have $2$-exponent $\leq i_k \leq p-1$)
- $D \notin F^{p-1}$ (since $D = 2^p - 3^k$ requires $2$-exponent $p$)

If $D \mid S(I)$ and $S(I) \in F^{p-1}$, does this force $D \in F^{p-1}$? NOT necessarily — $D \mid S$ means $S = n_0 D$, and $n_0 D$ being in $F^{p-1}$ doesn't force $D \in F^{p-1}$.

The filtration approach fails because multiplication by $n_0$ can "move" elements between filtration levels. This is the same as the carrying problem: $n_0 \cdot D$ can have lower "smooth degree" than $D$ itself.

### 4.3. Find a Different Proof Structure

The function field proof has the structure: **degree comparison**. The integer proof might need a completely different structure that achieves the same effect without using an absolute value. Possible approaches:

1. **Cohomological obstruction**: Define a cohomology theory for smooth sums where $H^1 \neq 0$ implies no divisibility. The function field proof would correspond to $H^0$ (sections of a line bundle of negative degree = empty).

2. **Intersection theory**: View $S(I)$ and $D$ as "divisors" on some arithmetic surface. Their intersection number might be computable and incompatible with $D \mid S$.

3. **Automata-theoretic**: The function field degree corresponds to "string length" in the automaton reading $t$-adic digits. An analogue for integers might use the Cobham-Semenov theorem on multi-base recognizability.

4. **$\mathbb{F}_1$-algebraic geometry**: Develop the theory of $\text{Spec}(\mathbb{Z})$ as a "curve over $\mathbb{F}_1$" far enough that a degree function and Riemann-Roch theorem become available.

---

## 5. The Philosophical Point

The function field Collatz is **trivially** true — a one-line proof by degree comparison. This suggests the integer Collatz might also be "trivially" true from the right viewpoint. The difficulty is not in the problem but in the **absence of a language** that makes the trivial argument expressible over $\mathbb{Z}$.

Every hard number theory problem that was eventually solved followed this pattern:
- **FLT for regular primes** (Kummer 1850): trivial once ideal theory exists
- **Mordell conjecture** (Faltings 1983): follows from "heights on abelian varieties decrease under isogeny" — a structural fact invisible without the right framework
- **FLT** (Wiles 1995): follows from "the Frey curve can't be modular" — obvious once modularity lifting exists

The Collatz conjecture might follow from: "smooth sums of degree $< p$ can't be divisible by a smooth difference of degree $p$" — obvious once the right "degree" exists over $\mathbb{Z}$.

**The problem is not that the Collatz conjecture is hard. The problem is that we don't have a degree function on $\mathbb{Z}$ that treats 2 and 3 asymmetrically while remaining ultrametric. Building one is the missing mathematics.**

---

## 6. Connection to the Barrier Diagnostic

The Ostrowski obstruction is the **deepest formulation** of the barriers:

- **Barrier 1 (abc/size-counting)**: The archimedean absolute value gives the divisibility constraint but not the gap. To get the gap, we'd need $\operatorname{rad}(D)$ bounds, which is abc.

- **Barrier 2 (equivalence)**: Any reformulation that preserves the full structure of $D \mid S(I)$ inherits the Ostrowski obstruction. The function field proof works by LOSING information (replacing integers with polynomials), but the specific information lost (the size of coefficients) is exactly what makes the problem hard.

- **Barrier 3 (completion blindness)**: No single completion of $\mathbb{Q}$ provides both the gap and the constraint. The archimedean completion gives the constraint; the function field analogue gives the gap; no completion gives both.

The Ostrowski obstruction unifies all three barriers: **they are all consequences of the fact that $\mathbb{Q}$ has exactly one archimedean place, and that place is not ultrametric.**

---

## 7. Specific Conjectures for Future Work

### Conjecture A (Smooth Degree Conjecture)
There exists a function $\delta: \mathbb{Z}_{>0} \to \mathbb{R}_{\geq 0}$ and a constant $C > 0$ such that:
1. For all $\{2,3\}$-smooth sums $S = \sum c_i \cdot 2^{a_i} \cdot 3^{b_i}$ with $k$ terms: $\delta(S) \leq \max_i a_i + C \log k$
2. For all $d, n \in \mathbb{Z}_{>0}$ with $d \mid n$: $\delta(d) \leq \delta(n) + C$
3. $\delta(2^p - 3^k) \geq p - C$ for all valid $(p,k)$

If such $\delta$ exists with $C < 1/2$, then the Collatz conjecture follows for large $p$.

### Conjecture B (Filtered Divisibility)
For $D = 2^p - 3^k$ and $S(I) = \sum 3^{k-j} 2^{i_j}$ with $i_k \leq p-1$:

$$v_2(S(I)) + \lfloor \log_2(S(I)/2^{v_2(S(I))}) \rfloor < 2p - 1$$

but if $D \mid S(I)$, then $v_2(S(I)) + \lfloor \log_2(S(I)/2^{v_2(S(I))}) \rfloor \geq 2p - O(\log p)$.

(This would combine the "bottom" and "top" measures into a single constraint.)

### Conjecture C ($\mathbb{F}_1$-Degree)
There exists a "degree" on $\mathbb{Z}$ (in the sense of $\mathbb{F}_1$-geometry) such that:
- $\deg(2^a \cdot 3^b) = a$ (powers of 3 are "units")
- $\deg$ satisfies a Riemann-Roch theorem for $\text{Spec}(\mathbb{Z})$
- The "line bundle" $\mathcal{O}(D)$ for $D = 2^p - 3^k$ has $\deg = p$
- The "space of global sections" of $\mathcal{O}(D)$ with $\deg \leq p-1$ does not contain $S(I)$

This would make the Collatz conjecture a statement about vanishing of cohomology of a line bundle on $\text{Spec}(\mathbb{Z})$ — the arithmetic analogue of "$H^0(\mathcal{O}(D-1)) = 0$ when $\deg(D-1) < 0$" over function fields.
