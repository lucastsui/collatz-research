# Attack on 6g-iii: Quantitative ×2 ×3 Rigidity

*Analysis -- 2026-03-06*

## 0. Executive Summary

**Result: the direct application of Furstenberg-Rudolph ×2 ×3 rigidity to Collatz cycles FAILS.** The failure is structural, not technical: the cycle measure is atomic (finitely supported on rationals), which is an explicitly allowed case in the rigidity classification. This note documents why, identifies what survives, and proposes a modified approach.

---

## 1. The Furstenberg-Rudolph Theorem (what it actually says)

**Furstenberg's conjecture (1967):** The only Borel probability measures on $\mathbb{R}/\mathbb{Z}$ that are invariant under both $\times 2: x \mapsto 2x \bmod 1$ and $\times 3: x \mapsto 3x \bmod 1$ are:
- Lebesgue measure, and
- measures supported on finite orbits of rationals (atomic measures).

**Rudolph (1990):** Proved for ergodic $\times 2$-invariant measures with $h_\mu(\times 2) > 0$ (positive entropy): if also $\times 3$-invariant, then $\mu$ is Lebesgue.

**Johnson (1992), Host (1995):** Extended to zero-entropy case under additional assumptions. The full conjecture remains open but all results agree: atomic measures on rationals are ALLOWED.

### Why this matters for Collatz

A period-$p$ Collatz cycle $u_0, \ldots, u_{p-1}$ defines an atomic measure
$$
\mu_p = \frac{1}{p} \sum_{r=0}^{p-1} \delta_{u_r/D}
$$
on $\mathbb{Q}$, which can be projected to $\mathbb{R}/\mathbb{Z}$.

This measure is:
- Finitely supported (on $p$ rational points)
- Has zero entropy
- Is atomic

All three properties place $\mu_p$ squarely in the "allowed" category of Furstenberg's conjecture. **No version of ×2 ×3 rigidity will rule it out based on the measure type alone.**

---

## 2. The Invariance Problem (why the connection is indirect)

The Collatz cycle measure $\mu_p$ is $T$-invariant (invariant under the compressed Collatz map), NOT $\times 2$-invariant or $\times 3$-invariant.

The compressed Collatz map acts as:
- $T(n) = n/2$ at even steps ($\times 2^{-1}$, a pure multiplicative operation)
- $T(n) = (3n+1)/2$ at odd steps ($\times 3 \times 2^{-1}$ plus a "+1" correction)

So $T$ involves both $\times 2$ and $\times 3$, but in a **piecewise** and **affine** (not linear) way. The "+1" at odd steps breaks multiplicative structure.

### Approximate invariance?

For large orbit values $u_r \gg 1/\Delta$, the "+1" correction is relatively small:
$$
\frac{3u_r + 1}{2} = \frac{3}{2} u_r \cdot \left(1 + \frac{1}{3u_r}\right).
$$

The relative perturbation is $1/(3u_r) \approx \Delta/k \approx p^{-10}$. So the odd step is "$O(p^{-10})$-approximately $\times (3/2)$."

But "approximate invariance" of a measure under $\times 2$ or $\times 3$ requires the PUSHFORWARD to be close to the original measure. For $\mu_p$:
$$
(\times 2)_* \mu_p = \frac{1}{p} \sum_{r=0}^{p-1} \delta_{2u_r/D}.
$$

The points $2u_r/D$ are NOT the same as $u_r/D$ in general (the orbit is $T$-invariant, not $\times 2$-invariant). At even steps, $2u_r = u_{r-1}$ (the previous value), but at odd steps, $2u_r = 3u_{r-1} + 1 \neq u_{r-1}$ in general.

So $\mu_p$ is not even approximately $\times 2$-invariant in the usual measure-theoretic sense.

---

## 3. The Dual Action on $(\mathbb{Z}/D\mathbb{Z})^*$ (what does survive)

Although the measure-theoretic approach fails, the ALGEBRAIC structure is real.

Since $D = 2^p - 3^k$, we have $2^p \equiv 3^k \pmod{D}$, so the subgroup $\langle 2, 3 \rangle \subset (\mathbb{Z}/D\mathbb{Z})^*$ satisfies:
$$
2^p = 3^k \quad \text{in } (\mathbb{Z}/D\mathbb{Z})^*.
$$

The orbit values $u_0, \ldots, u_{p-1}$ satisfy (from the affine orbit equation):
$$
u_r = \frac{3^{t_r}}{2^r} n + \beta_r
$$
where $t_r = \#(I \cap \{0, \ldots, r-1\})$ and $\beta_r$ is a specific rational number with denominator $2^r$.

Modulo $D$:
$$
u_r \equiv 3^{t_r} \cdot 2^{-r} \cdot n + \beta_r \pmod{D}.
$$

The multiplicative part $3^{t_r} \cdot 2^{-r}$ traces out a path in $\langle 2, 3 \rangle \subset (\mathbb{Z}/D\mathbb{Z})^*$. After $p$ steps, the net multiplication is $3^k \cdot 2^{-p} \equiv 1 \pmod{D}$, as required for the orbit to close.

### The Weyl sum

Define the Weyl sum at frequency $h \in (\mathbb{Z}/D\mathbb{Z})^*$:
$$
W(h) = \frac{1}{p} \sum_{r=0}^{p-1} e\!\left(\frac{h u_r}{D}\right).
$$

Substituting $u_r = 3^{t_r} 2^{-r} n + \beta_r$:
$$
W(h) = \frac{1}{p} \sum_{r=0}^{p-1} e\!\left(\frac{h_r n}{D}\right) \cdot e\!\left(\frac{h \beta_r}{D}\right)
$$
where $h_r = h \cdot 3^{t_r} \cdot 2^{-r} \bmod D$.

The frequencies $h_r$ form the **dual orbit** of $h$ under the $\langle 2, 3 \rangle$ action on $(\mathbb{Z}/D\mathbb{Z})^*$.

**Key question:** How do the frequencies $h_r$ distribute in $(\mathbb{Z}/D\mathbb{Z})^*$?

If $\langle 2, 3 \rangle = (\mathbb{Z}/D\mathbb{Z})^*$ (i.e., 2 and 3 generate the full group), then the dual orbit visits many residue classes, giving cancellation in $W(h)$.

But understanding $\langle 2, 3 \rangle \bmod D$ requires understanding the group structure of $(\mathbb{Z}/D\mathbb{Z})^*$, which decomposes by CRT into prime factors of $D$. **This is the sieve approach in disguise.**

---

## 4. The Discrepancy Walk and Irrationality of $\log 2/\log 3$

The most promising angle uses the irrationality of $\log 2/\log 3$ directly, not through a known theorem.

### Setup

For a Collatz cycle with parity sequence $\varepsilon_0, \ldots, \varepsilon_{p-1}$, define:
$$
\Delta_r = r \log 2 - t_r \log 3, \qquad t_r = \sum_{j=0}^{r-1} \varepsilon_j.
$$

The walk $\Delta_r$ starts at 0 and ends at $\Delta = p \log 2 - k \log 3 > 0$.

Each step is:
$$
\Delta_{r+1} - \Delta_r = \begin{cases} \log 2 \approx 0.693 & \text{if } \varepsilon_r = 0, \\ \log 2 - \log 3 \approx -0.405 & \text{if } \varepsilon_r = 1. \end{cases}
$$

From the defect identity (agent_q_defect.md, Corollary 3.1), the **defect variable**
$$
E_r = \Delta_r + \log(u_r/n) \in [0, \Delta]
$$
is confined to a band of width $\Delta$.

### The irrationality constraint

The orbit values satisfy $u_r = n e^{-\Delta_r + E_r}$, so:
$$
\log u_r = \log n - \Delta_r + E_r = \log n - (r \log 2 - t_r \log 3) + E_r.
$$

Since $u_r$ must be a positive integer:
$$
e^{-\Delta_r + E_r} = u_r / n \in \mathbb{Q}_{>0}.
$$

Now $\Delta_r = r \log 2 - t_r \log 3$, so:
$$
e^{-r \log 2 + t_r \log 3 + E_r} = u_r/n,
$$
i.e.,
$$
\frac{3^{t_r}}{2^r} \cdot e^{E_r} = \frac{u_r}{n}.
$$

Since the left side involves $e^{E_r}$ and the right side is rational, we need:
$$
e^{E_r} = \frac{u_r \cdot 2^r}{n \cdot 3^{t_r}}.
$$

This is automatic (it defines $E_r$). But the constraint $E_r \in [0, \Delta]$ means:
$$
1 \leq \frac{u_r \cdot 2^r}{n \cdot 3^{t_r}} \leq e^\Delta = \frac{2^p}{3^k}.
$$

Equivalently:
$$
n \cdot 3^{t_r} \leq u_r \cdot 2^r \leq n \cdot 2^{p-r+r} \cdot 3^{t_r-k}...
$$

Wait, let me just state it cleanly:
$$
\frac{n \cdot 3^{t_r}}{2^r} \leq u_r \leq \frac{n \cdot 2^{p-r}}{3^{k-t_r}}.
$$

This is Proposition 2.1 from agent_q_defect.md. The ratio upper/lower is exactly $2^p/3^k = e^\Delta$.

### What irrationality of $\log 2/\log 3$ forces

The discrepancy $\Delta_r = r \log 2 - t_r \log 3$ depends on how the partial sums $t_r$ track the "ideal" value $r \cdot \log 2/\log 3$.

By the three-distance theorem, for the optimal placement (Kronecker sequence), the values $\{r \cdot \log 2/\log 3 \bmod 1 : r = 0, \ldots, p-1\}$ partition $[0,1)$ into gaps of at most 3 distinct lengths. The minimum gap is $\sim 1/p$ (or $\sim 1/q$ where $q$ is a CF denominator).

For the Collatz parity sequence, the placement of odd steps is NOT the Kronecker sequence — it's determined by the orbit dynamics. But the defect variable $E_r$ confines the placement to within $\Delta$ of the "ideal" template.

**The question:** Does the irrationality of $\log 2/\log 3$, combined with the integrality of orbit values and the narrow band $[0, \Delta]$ for the defect, force a contradiction?

---

## 5. A Concrete Obstruction Attempt

### The inter-step constraint

Between two consecutive odd steps at positions $r$ and $r'$ (with $m = r' - r - 1$ even steps in between), the orbit evolves as:

After the odd step at $r$: $u_{r+1} = (3u_r + 1)/2$.
After $m$ even steps: $u_{r'+1-1} = u_{r+1}/2^m = (3u_r + 1)/2^{m+1}$.
At position $r'$: $u_{r'} = (3u_r + 1)/2^{m+1}$ must be odd.

So $v_2(3u_r + 1) = m + 1$ exactly (the 2-adic valuation).

Denote the gaps between consecutive odd steps as $g_1, g_2, \ldots, g_k$ (where $g_j = r_{j+1} - r_j$ for $j < k$ and $g_k = p - r_k + r_1$, wrapping around). Each $g_j \geq 1$ and $\sum g_j = p$.

The 2-adic constraint: at the $j$-th odd step with value $y_j$:
$$
v_2(3y_j + 1) = g_j.
$$

So:
$$
3y_j + 1 \equiv 0 \pmod{2^{g_j}}, \qquad 3y_j + 1 \not\equiv 0 \pmod{2^{g_j+1}}.
$$

The first condition: $y_j \equiv -3^{-1} \pmod{2^{g_j}}$, i.e., $y_j \equiv (2^{g_j} - 1)/3 \cdot (-1) \ldots$

More carefully: $3y_j \equiv -1 \pmod{2^{g_j}}$, so $y_j \equiv -3^{-1} \pmod{2^{g_j}}$.

Since $3^{-1} \bmod 2^n$ follows the pattern: $3^{-1} \equiv 1 \bmod 2$, $3^{-1} \equiv 3 \bmod 8$, $3^{-1} \equiv 11 \bmod 16$, etc. (the 2-adic expansion of $-1/3$ is $\ldots 10101011_2$).

So $y_j \equiv -3^{-1} \equiv \ldots 01010101_2 \pmod{2^{g_j}}$ (the 2-adic expansion of $1/3$, which is $\sum_{i=0}^\infty 2^{2i} / 3 = \ldots 01010101_2$).

This is a rigid 2-adic constraint on each odd orbit value.

### The 3-adic constraint

From Section 1 of agent_q_defect.md: after each odd step, $u_{r+1} = (3u_r + 1)/2$. Since $3u_r + 1 \equiv 1 \pmod{3}$, the value $u_{r+1}$ satisfies $v_3(u_{r+1}) = 0$. After subsequent even steps, $v_3$ is preserved. So **all orbit values have $v_3 = 0$** (not divisible by 3).

Combined with the 2-adic constraint: each odd value $y_j$ satisfies:
- $y_j \equiv 1 \pmod{2}$ (odd)
- $y_j \not\equiv 0 \pmod{3}$
- $y_j \equiv -3^{-1} \pmod{2^{g_j}}$ (2-adic pattern from the gap)

### The recurrence

The consecutive odd values are linked:
$$
y_{j+1} = \frac{3y_j + 1}{2^{g_j}}.
$$

This is exact: after the odd step $(3y_j + 1)/2$, followed by $g_j - 1$ even steps (dividing by $2^{g_j-1}$), we get $y_{j+1} = (3y_j + 1)/2^{g_j}$.

Closure: $y_{k+1} = y_1$. So:
$$
y_1 = \frac{3y_k + 1}{2^{g_k}} = \frac{3(\frac{3y_{k-1}+1}{2^{g_{k-1}}})+1}{2^{g_k}} = \ldots
$$

The full composition gives:
$$
y_1 = \frac{3^k}{2^p} y_1 + \frac{S'}{2^p}
$$
where $S'$ encodes the accumulated "+1" corrections. This gives $y_1 (1 - 3^k/2^p) = S'/2^p$, i.e., $y_1 = S'/(2^p - 3^k) = S'/D$.

Which is the cycle equation again. No new information.

---

## 6. What Would a Working ×2 ×3 Approach Look Like?

The direct Furstenberg-Rudolph connection fails because:
1. The cycle measure is atomic (allowed by the theorem)
2. The cycle measure is T-invariant, not ×2- or ×3-invariant
3. The algebraic structure mod D reduces to the sieve via CRT

But here is what a MODIFIED approach might exploit:

### 6.1 The "simultaneous Diophantine" angle

The orbit values $u_0, \ldots, u_{p-1}$ are positive integers that simultaneously satisfy:
- **2-adic constraints**: $v_2(3y_j + 1) = g_j$ for each odd value
- **Archimedean constraints**: $u_r = n \cdot e^{-\Delta_r + E_r}$ with $E_r \in [0, \Delta]$
- **Integrality**: $u_r \in \mathbb{Z}_{>0}$

The 2-adic constraints pin the odd values to specific residue classes mod $2^{g_j}$. The archimedean constraints pin them to a narrow multiplicative band. The irrationality of $\log 2/\log 3$ means these two sets of constraints are "incommensurable" — the 2-adic structure and the archimedean structure are controlled by different aspects of the number system.

**Concrete question:** Is there a simultaneous Diophantine approximation result that says: an integer $y$ satisfying both
$$
y \equiv c \pmod{2^g} \qquad \text{and} \qquad A \leq y \leq A(1 + \delta)
$$
requires $g \lesssim \log(1/\delta) / \log 2$?

Yes — trivially! The number of integers in $[A, A(1+\delta)]$ is $\sim A\delta$. Among these, the fraction with $y \equiv c \bmod 2^g$ is $\sim 1/2^g$. So the expected count is $A\delta/2^g$. For a solution to exist, we need $A\delta \gtrsim 2^g$, i.e., $g \lesssim \log(A\delta)$.

For the Collatz cycle: $A \sim n$, $\delta \sim \Delta \sim p^{-9}$ (for near-resonant cycles), $g_j \geq 1$, and we need the average gap to be $\bar{g} = p/k \approx 1/0.63 \approx 1.585$.

The condition $n \cdot \Delta \gtrsim 2^{g_j}$ gives $g_j \lesssim \log(n\Delta)$. Since $n\Delta \approx n/p^9$, and $n \geq 1$, this gives $g_j \lesssim \log n - 9 \log p$. For $n \gg p^9$ (which is required for all odd values to be positive), this is consistent.

But we need ALL $k$ gaps $g_j$ to simultaneously have solutions. The total constraint is:
$$
\sum_{j=1}^k g_j = p, \qquad \prod_{j=1}^k 2^{g_j} = 2^p.
$$

And for each gap, we need an odd value $y_j$ in the intersection of a residue class mod $2^{g_j}$ and an interval of length $\sim n\Delta$. Since $n\Delta$ can be large (no a priori upper bound on $n$), this doesn't immediately give a contradiction.

### 6.2 The "reciprocal sum" constraint

From the defect identity:
$$
\Delta = \sum_{j=1}^k \log\!\left(1 + \frac{1}{3y_j}\right) \approx \frac{1}{3} \sum_{j=1}^k \frac{1}{y_j}.
$$

Combined with the recurrence $y_{j+1} = (3y_j + 1)/2^{g_j}$:

If the gaps $g_j$ are mostly small (close to 1-2), then $y_{j+1} \approx (3/2^{g_j}) y_j$, so the sequence $y_j$ has multiplicative growth/decay $\sim 3/2^{g_j}$ per step. For $g_j = 1$: growth $3/2 = 1.5$. For $g_j = 2$: decay $3/4 = 0.75$. Average: $3^k/2^p \approx 1$.

The reciprocal sum: if $y_j \sim n$ for all $j$ (the orbit values are all similar in size), then:
$$
\frac{1}{3} \sum \frac{1}{y_j} \approx \frac{k}{3n} \approx \frac{0.63p}{3n} = \frac{0.21p}{n}.
$$
Setting this equal to $\Delta \approx p^{-9}$: $n \approx 0.21 p^{10}$.

So near-resonant cycles would have $n \sim p^{10}$ — not astronomically large, just polynomial in $p$.

But then $D = 2^p - 3^k \approx 2^p \cdot \Delta \approx 2^p / p^9$. And $S(I) = nD \approx p^{10} \cdot 2^p / p^9 = p \cdot 2^p$. This is consistent with $S(I) \leq k \cdot 3^{k-1} \cdot 2^{p-1} \sim 2^p$ for large $p$... actually $p \cdot 2^p > 2^p$, so there might be a contradiction here.

Wait: $S(I) = \sum_{j=1}^k 3^{k-j} 2^{i_j}$. The maximum value of $S(I)$ occurs when $i_j = p-k+j-1$ (choosing the largest exponents):
$$
S_{\max} = \sum_{j=1}^k 3^{k-j} 2^{p-k+j-1} = 2^{p-k-1} \sum_{j=1}^k (2/3)^{-j+k} \cdot 3^0 \ldots
$$

Hmm, let me compute $S_{\max}$ more carefully:
$$
S_{\max} \leq \sum_{j=1}^k 3^{k-1} \cdot 2^{p-1} = k \cdot 3^{k-1} \cdot 2^{p-1}.
$$
No, that's wrong — each term has a different power of 3. The maximum is:
$$
S_{\max} = \sum_{j=1}^k 3^{k-j} 2^{p-k+j-1} = 2^{p-k-1} \sum_{j=1}^k (2 \cdot 3)^{j-1} \cdot 3^{k-1}...
$$

Let me just bound it differently. The largest single term is $3^{k-1} \cdot 2^{p-1}$ (when $j=1$ and $i_1 = p-1$). But we can't have $i_1 = p-1$ and also have $i_2 = p-1$. More carefully:
$$
S(I) \leq 3^{k-1}(2^{p-1} + 2^{p-2} + \cdots + 2^0) < 3^{k-1} \cdot 2^p.
$$

Since $3^{k-1} \approx 3^k/3 \approx 2^p/3$:
$$
S(I) < \frac{2^{2p}}{3}.
$$

And $S(I) = nD \approx n \cdot 2^p$. So $n < 2^p/3$, which is a very weak constraint.

So $n \sim p^{10}$ is easily accommodated. No contradiction here.

---

## 7. Negative Result and Honest Assessment

### What fails

1. **Furstenberg-Rudolph doesn't apply**: the cycle measure is atomic, which is allowed.
2. **Approximate invariance is meaningless**: $\mu_p$ is not approximately $\times 2$-invariant in any useful sense.
3. **The dual action mod $D$** reduces to the sieve via CRT decomposition.
4. **Simultaneous Diophantine constraints** (2-adic + archimedean) don't give a contradiction because $n$ can be polynomially large in $p$, and the constraints are compatible.
5. **The recurrence $y_{j+1} = (3y_j+1)/2^{g_j}$** combined with the defect identity is exactly the cycle equation — no new information.

### What survives

The irrationality of $\log 2/\log 3$ IS the fundamental reason Collatz cycles are rare. It forces:
- The discrepancy walk $\Delta_r$ to wander
- The orbit values to compensate via the "+1" corrections
- The compensation budget is exactly $\Delta$

But turning "rare" into "impossible" requires a quantitative leap that no known tool provides.

### The real gap

The cycle equation is a SINGLE equation: $D \mid S(I)$. It has $\binom{p}{k} \approx 2^{0.95p}$ candidates and the modulus is $D \approx 2^p$. The expected number of solutions is $2^{-0.05p} \to 0$.

To prove no solutions exist, we need to show the $2^{0.95p}$ residues $S(I) \bmod D$ (as $I$ ranges over $k$-subsets) are all nonzero. This is a statement about the distribution of a specific set of integers modulo a specific modulus. No known technique handles this at exponential scale without factoring the modulus.

---

## 8. A Modified Approach (speculative)

The one angle that hasn't been fully explored:

**The joint distribution of $S(I) \bmod 2^p$ and $S(I) \bmod 3^k$ simultaneously.**

Since $\gcd(2^p, 3^k) = 1$ and $D = 2^p - 3^k$, the CRT gives:
$$
D \mid S(I) \iff S(I) \equiv 0 \pmod{D} \iff \begin{cases} S(I) \equiv 0 \pmod{\gcd(D, 2^p)} \\ S(I) \equiv 0 \pmod{\gcd(D, 3^k)} \end{cases}
$$

But $\gcd(D, 2^p) = \gcd(2^p - 3^k, 2^p) = \gcd(3^k, 2^p) = 1$ and similarly $\gcd(D, 3^k) = 1$. So this CRT decomposition is trivial.

However, we CAN write:
$$
S(I) \equiv 0 \pmod{D} \implies S(I) \equiv 0 \pmod{2^p - 3^k}.
$$

In the ring $\mathbb{Z}/2^p\mathbb{Z}$: $D \equiv -3^k$, so $S(I) \equiv 0 \pmod{-3^k}$ in $\mathbb{Z}/2^p\mathbb{Z}$, i.e., $3^k \mid S(I)$ in $\mathbb{Z}/2^p\mathbb{Z}$.

Similarly in $\mathbb{Z}/3^k\mathbb{Z}$: $D \equiv 2^p$, so $2^p \mid S(I)$ in $\mathbb{Z}/3^k\mathbb{Z}$.

This gives two conditions:
1. $S(I) \equiv 0 \pmod{3^k}$ as an integer mod $2^p$ (i.e., $v_3(S(I) \bmod 2^p) \geq k$... but this doesn't quite make sense since $S(I) \bmod 2^p$ might not be divisible by 3 at all).

Actually, let me be more precise. The condition $D \mid S(I)$ means $S(I) = nD = n(2^p - 3^k)$ for some positive integer $n$. So:
$$
S(I) \equiv -n \cdot 3^k \pmod{2^p}, \qquad S(I) \equiv n \cdot 2^p \pmod{3^k}.
$$

From the second: $n \equiv S(I) \cdot (2^p)^{-1} \pmod{3^k}$, where $(2^p)^{-1}$ exists mod $3^k$ since $\gcd(2, 3) = 1$.

From the first: $n \equiv -S(I) \cdot (3^k)^{-1} \pmod{2^p}$.

These determine $n$ modulo $\text{lcm}(2^p, 3^k) = 2^p \cdot 3^k$. Since $n < 2^p/3$ (from the bound on $S(I)$), $n$ is uniquely determined — which is just saying the cycle equation has a unique rational solution $n = S(I)/D$.

So this decomposition also gives nothing new.

---

## 9. Conclusion

**6g-iii (Quantitative ×2 ×3 rigidity) does not work as a direct approach to Collatz cycles.** The failure is not technical but structural:

- The Furstenberg-Rudolph classification explicitly allows atomic measures (which is what cycle measures are).
- The Collatz map is $T$-invariant, not $\times 2$- or $\times 3$-invariant, and the approximate invariance is too weak.
- Every algebraic decomposition (mod $D$, mod $2^p$, mod $3^k$) either reduces to the sieve or gives trivial information.

**Revised status of 6g-iii**: Should be marked as **explored, fails** with the caveat that a deeply modified version (not currently conceivable) might still work.

The fundamental problem remains: proving non-divisibility at exponential scale without factoring the modulus. The ×2 ×3 framework, despite its thematic appeal, does not provide a path to this.
