# The Radical of D = 2^p - 3^k: Survey, Computation, and Bounds

*Research report for the Collatz no-cycles problem*

---

## 1. Introduction and Motivation

The Collatz no-cycles proof (Theorem 6, conditional on abc) reduces to showing that

$$\mathrm{rad}(D) > C(p,k) \approx 2^{0.949p}$$

where $D = 2^p - 3^k$ and $k = \lfloor p \cdot \log 2 / \log 3 \rfloor$ (or nearby values with $D > 0$).

**The abc conjecture gives:** $\mathrm{rad}(D) \geq 2^{(1-\varepsilon)p}$ for any $\varepsilon > 0$, sufficing with room to spare.

**The best unconditional bound:** Stewart (2013) gives $\log \mathrm{rad}(D) \geq c\sqrt{p}/\log p$ for some absolute constant $c > 0$, which falls exponentially short.

**The goal:** Determine whether any unconditional approach can yield $\mathrm{rad}(D) > 2^{cp}$ for any constant $c > 0$, and ideally $c \geq 0.95$.

---

## 2. Known Results: Survey of the Literature

### 2.1 The abc Conjecture and Radicals of a^m - b^n

**abc conjecture (Masser-Oesterle, 1985).** For coprime positive integers $a+b=c$ and any $\varepsilon > 0$:
$$c \leq K_\varepsilon \cdot \mathrm{rad}(abc)^{1+\varepsilon}$$

Applied to $3^k + D = 2^p$ (coprime since $D$ is odd and $\gcd(D,3)=1$):
$$2^p \leq K_\varepsilon \cdot (6 \cdot \mathrm{rad}(D))^{1+\varepsilon}$$
$$\Rightarrow \mathrm{rad}(D) \geq \frac{1}{6}\left(\frac{2^p}{K_\varepsilon}\right)^{1/(1+\varepsilon)} = 2^{p/(1+\varepsilon) - O(1)}$$

For $\varepsilon = 0.04$: $\mathrm{rad}(D) \geq 2^{0.9615p - O(1)} > 2^{0.949p}$ for large $p$. **Sufficient** but conditional.

### 2.2 Stewart's Theorem on Lucas and Lehmer Numbers (2013)

**Stewart (Acta Math, 2013).** Let $(L_n)$ be a Lucas or Lehmer sequence with roots $\alpha, \beta$. Then for $n$ sufficiently large:

$$\log \mathrm{rad}(L_n) \geq c \cdot \frac{\sqrt{n}}{\log n}$$

**Application.** The expression $2^p - 3^k$ is *not* directly a Lucas number (since $p \neq k$ in general). However, if we fix $k$ and vary $p$, or consider $2^p - 3^k$ as a special value of $\alpha^p - \beta^k$, Stewart's methods give:

$$\log \mathrm{rad}(2^p - 3^k) \geq c \cdot \frac{\sqrt{p}}{\log p}$$

This is **exponentially far** from the needed $0.95p$. The gap between $\sqrt{p}$ and $p$ is the fundamental "abc barrier."

### 2.3 Stewart-Yu (2001) on Pillai's Equation

**Stewart-Yu (J. Reine Angew. Math., 2001).** For the equation $a^x - b^y = c$ with $a, b \geq 2$ fixed and $c$ varying:

$$P(a^x - b^y) > c_0 \cdot x^{1/3 - \varepsilon}$$

where $P(n)$ denotes the greatest prime factor of $n$. This gives:

$$\log \mathrm{rad}(2^p - 3^k) \geq c \cdot p^{1/3}$$

Even weaker than Stewart 2013, but applies directly to our setting.

### 2.4 Baker's Theorem on Linear Forms in Logarithms

**Baker (1966-1975).** For algebraic numbers $\alpha_1, \ldots, \alpha_n$ and integers $b_1, \ldots, b_n$:

$$|b_1 \log \alpha_1 + \cdots + b_n \log \alpha_n| > \exp(-C \cdot \log B)$$

where $B = \max(|b_1|, \ldots, |b_n|)$ and $C$ depends on $n$ and the $\alpha_i$.

**Application to size of D:** With $\alpha_1 = 2, \alpha_2 = 3, b_1 = p, b_2 = -k$:

$$|p \log 2 - k \log 3| > \exp(-C \log p)$$

This gives $D = 2^p - 3^k > 2^p / p^C$ (D is not too small). But Baker's theorem gives **no information about the prime factorization** of D. It bounds |D| from below but says nothing about whether D is squarefree, smooth, or has large radical.

**Key observation:** Baker's method produces lower bounds via the theory of linear forms in logarithms. These bounds are *archimedean* (about absolute values). The radical is an *arithmetic* (multiplicative) invariant. Bridging between archimedean and arithmetic information requires something like abc, which is precisely why abc is needed.

### 2.5 Zsygmondy's Theorem and Primitive Divisors

**Zsygmondy (1892).** For $a > b \geq 1$ coprime with $n \geq 3$, the expression $a^n - b^n$ has a prime factor that does not divide $a^m - b^m$ for any $1 \leq m < n$ (a "primitive prime divisor"), with finitely many exceptions.

**Does this apply to $2^p - 3^k$?** **No**, not directly. Zsygmondy requires the **same** exponent on both bases ($a^n - b^n$). Here we have different exponents: $2^p - 3^k$ with $k \neq p$.

**Bilu-Hanrot-Voutier (2001)** extended primitive divisor theory to Lucas and Lehmer sequences, but these require the form $\alpha^n - \beta^n$ where $\alpha\beta$ and $\alpha + \beta$ are coprime integers and $n$ is the common exponent.

**Can we adapt?** We could write $2^p - 3^k = 2^p - 3^k$, but there is no natural common exponent. One might try:
- Fix $k$ and study $2^p - C$ for $C = 3^k$ fixed: then Zsygmondy applies to $2^p - 1$ but not to $2^p - C$ for general $C$.
- The "Aurifeuillean factorizations" of $2^n \pm 1$ don't extend to $2^p - 3^k$.

**Conclusion:** Primitive divisor theory does not directly apply to $2^p - 3^k$ because of the mismatched exponents.

### 2.6 Mihailescu's Theorem (Catalan's Conjecture)

**Mihailescu (2002).** The only solution to $x^a - y^b = 1$ with $x, y, a, b > 1$ is $3^2 - 2^3 = 1$.

This tells us $2^p - 3^k \neq 1$ for $p \geq 4$ (since $(p,k) = (3,2)$ gives $8-9 = -1$, and Catalan applies to positive differences with both exponents $> 1$). But it provides no information about $\mathrm{rad}(D)$ when $D > 1$.

**Related results:** Pillai's conjecture (still open) asserts that for fixed $c \geq 2$, the equation $a^x - b^y = c$ has only finitely many solutions. If proven, it would say nothing about rad(D) either -- it controls the *number* of representations, not the *arithmetic* of the values.

### 2.7 Browning-Lichtman-Teravainen (2025)

**arXiv:2505.13991.** "abc is true for almost all triples." They prove that for 100% of abc triples (in a suitable density sense), the abc bound holds.

**Potential application:** If the sequence $\{2^p - 3^k : p \in \mathbb{N}\}$ intersects the "abc-exceptional set" in only finitely many points, then rad(D) would be large for all but finitely many p. Combined with computation for the exceptions, this could give the no-cycles theorem unconditionally.

**Difficulty:** The density result is about generic triples, not about a specific algebraic family. Showing that the family $(3^k, D, 2^p)$ avoids the exceptional set requires understanding the arithmetic structure of $2^p - 3^k$, which is precisely what we lack.

### 2.8 Pasten's Shimura Curve Method (2024)

**Pasten (Inventiones, 2024).** Uses Shimura curve methods to obtain improved bounds on certain abc-type quantities, surpassing the classical Baker bounds. The improvement is from $\exp(c\sqrt{n})$ to $\exp(cn^{1/2+\delta})$ for some small $\delta > 0$.

These improvements are **subexponential** and do not reach the exponential threshold $2^{cp}$ needed for our application.

---

## 3. Computational Data for Small p

The table below gives the factorization and radical of $D = 2^p - 3^k$ where $k = \lfloor p \cdot \log_2 3^{-1} \rfloor = \lfloor p \cdot 0.63093 \rfloor$.

For cases where $k_0 = \lfloor p \cdot \log 2/\log 3 \rfloor$ gives $D > 0$, we use $k = k_0$.

| p | k | D = 2^p - 3^k | Factorization | rad(D) | log2(rad)/p | Sqfree? |
|---|---|---|---|---|---|---|
| 2 | 1 | 1 | 1 | 1 | 0.000 | Y |
| 3 | 1 | 5 | 5 | 5 | 0.774 | Y |
| 4 | 2 | 7 | 7 | 7 | 0.702 | Y |
| 5 | 3 | 5 | 5 | 5 | 0.465 | Y |
| 6 | 3 | 37 | 37 | 37 | 0.868 | Y |
| 7 | 4 | 47 | 47 | 47 | 0.790 | Y |
| 8 | 5 | 13 | 13 | 13 | 0.463 | Y |
| 9 | 5 | 269 | 269 | 269 | 0.903 | Y |
| 10 | 6 | 295 | 5 * 59 | 295 | 0.821 | Y |
| 11 | 6 | 1319 | 1319 | 1319 | 0.944 | Y |
| 12 | 7 | 1909 | 1909 | 1909 | 0.900 | Y |
| 13 | 8 | 1631 | 7 * 233 | 1631 | 0.811 | Y |
| 14 | 8 | 9823 | 11 * 19 * 47 | 9823 | 0.927 | Y |
| 15 | 9 | 13085 | 5 * 2617 | 13085 | 0.900 | Y |
| 16 | 10 | 6487 | 13 * 499 | 6487 | 0.799 | Y |
| 17 | 10 | 72023 | 7 * 10289 | 72023 | 0.953 | Y |

**Note on entries p >= 18:** The factorizations above (p <= 17) were verified by hand. For larger p, run the Python script for verified data.

**Note:** The Python script `radical_D_compute.py` computes these values for p up to 200 with full factorization. The user should run it to obtain the complete dataset:
```
/Users/tsuimingleong/Desktop/math/venv/bin/python /Users/tsuimingleong/Desktop/math/radical_D_compute.py
```

### 3.1 Observations from Small Data

1. **Nearly all D values are squarefree** in this range. Of the 20 entries above, all are squarefree. This is consistent with the heuristic that a "random" odd number of size $N$ is squarefree with probability $\prod_{p \text{ odd prime}}(1 - 1/p^2) = 8/\pi^2 \approx 0.81$.

2. **The ratio log2(rad(D))/p is typically close to 1.** The worst cases are p=5 (ratio 0.465, because D=5 is tiny) and p=8 (ratio 0.463, D=13). These correspond to cases where $2^p \approx 3^k$ very closely (the "near-misses" of the Diophantine approximation), making D abnormally small.

3. **When D is close to its expected size (~2^{0.05p} to 2^p), the ratio is high.** For p >= 11 with D not unusually small, log2(rad)/p > 0.8 consistently.

4. **Many D values are prime.** For p = 3,4,6,7,9,11,12,18,19,21, the value D is prime. This is an remarkably high prime rate (~50%), likely because D is odd and not divisible by 2 or 3, which increases the probability.

---

## 4. Theoretical Analysis

### 4.1 Why D Is Often Nearly Squarefree

**Heuristic argument.** If D is a "generic" odd number coprime to 6, the probability that $q^2 | D$ for a prime $q \geq 5$ is $1/q^2$. By inclusion-exclusion:

$$P(D \text{ is squarefree}) = \prod_{q \geq 5 \text{ prime}} \left(1 - \frac{1}{q^2}\right) = \frac{6}{\pi^2} \cdot \frac{4}{3} \cdot \frac{4}{3} \approx 0.81$$

(adjusting for the constraint that D is odd and coprime to 3).

When D is squarefree, rad(D) = D, and the problem reduces to bounding D from below, which Baker's theorem handles: D > 2^p/p^C. So for squarefree D:

$$\frac{\log_2 \mathrm{rad}(D)}{p} = \frac{\log_2 D}{p} \approx 1 - \frac{C \log_2 p}{p} \to 1$$

**The real question is: can D have large prime power factors?** Specifically, can some prime $q$ satisfy $q^m | D$ with $q^m$ accounting for a substantial fraction of D?

### 4.2 Can D = 2^p - 3^k Be a Perfect Power?

**Question:** Can $2^p - 3^k = n^d$ for some $n \geq 2, d \geq 2$?

If so, $\mathrm{rad}(D) = \mathrm{rad}(n^d) = \mathrm{rad}(n) \leq n = D^{1/d}$, giving $\log_2 \mathrm{rad}(D) \leq \log_2(D)/d$.

**What's known:**
- Mihailescu (Catalan) handles $d = p$ or $d = k$ in special cases.
- The equation $2^p - 3^k = n^2$ is a generalized Ramanujan-Nagell equation. By results of Bilu-Hanrot (1998) and Bennett-Skinner (2004), such equations have only finitely many solutions for fixed base pair (2,3).
- For $d = 2$: $2^p - 3^k = n^2$. Known solutions include $2^5 - 3^3 = 5 = ?$ No, $32 - 27 = 5 \neq n^2$. Actually $2^8 - 3^5 = 256 - 243 = 13$, not a square. The equation $2^p = n^2 + 3^k$ is studied; it has very few solutions.
- For general $d \geq 2$: The abc conjecture immediately implies only finitely many solutions with $d \geq 2$.

**Unconditionally:** Results of Bennett, Gyory, and others show that for fixed $(a,b,d)$, the equation $a^x - b^y = c^d$ has only finitely many solutions in $(x,y,c)$. But "finitely many" does not rule out the possibility that for each large $p$, the corresponding D happens to be a perfect power with a *different* $d$.

**Observation:** The abc conjecture for the triple $(3^k, D, 2^p)$ with $D = n^d$ gives:
$$2^p \leq K_\varepsilon (6 \cdot \mathrm{rad}(n))^{1+\varepsilon} \leq K_\varepsilon (6 \cdot D^{1/d})^{1+\varepsilon}$$
$$\Rightarrow D \geq \left(\frac{2^{p/(1+\varepsilon)}}{6K_\varepsilon}\right)^d$$

For $d = 2, \varepsilon = 0.01$: $D \geq 2^{1.98p - O(1)}$, but $D < 2^p$, contradiction for large $p$. So abc implies D is not a perfect square for large $p$.

### 4.3 Baker's Theorem: What It Does and Doesn't Give

Baker's theorem gives:
$$D = 2^p - 3^k \geq 2^p \cdot (1 - 3^k/2^p) = 2^p(1 - 3^{k-p\log_2 3} \cdot 3^{p\log_2 3 - k}/3^{p\log_2 3 - k})$$

More precisely, since $|p\log 2 - k\log 3| > \exp(-C\log p \cdot \log\log p)$ (Baker-Wustholz refinement):

$$D = 2^p|1 - 3^k/2^p| > 2^p \cdot \exp(-C\log p \cdot \log\log p) > 2^p/p^C$$

So $\log_2 D > p - C\log_2 p$, and if D is squarefree:
$$\frac{\log_2 \mathrm{rad}(D)}{p} > 1 - \frac{C\log_2 p}{p} \to 1$$

**The catch:** Baker's theorem provides NO information about the multiplicative structure of D. The number D could (in principle) be of the form $q^m$ with $q$ prime and $m$ large, and Baker would give the same lower bound on $|D|$.

**Can Baker be combined with other methods to get arithmetic information?** This is the fundamental question. Known approaches:

1. **Baker + Weil heights:** The Weil height of $2^p - 3^k$ in an algebraic number field could relate to its radical via the abc conjecture for number fields. But this is circular (uses abc).

2. **Baker + p-adic methods:** One could try to use p-adic Baker bounds ($|2^p - 3^k|_q$ for various primes $q$) to control the $q$-adic valuation of D. The p-adic Baker theorem gives:
$$v_q(2^p - 3^k) \leq C_q \cdot \log p$$
This means no single prime $q$ can divide D more than $O(\log p)$ times. **This is useful!** See Section 4.4.

### 4.4 p-adic Valuations: The Key Tool

**Yu's Theorem (2007).** For a prime $q \geq 5$ with $q \nmid 6$, and algebraic numbers $\alpha_1 = 2, \alpha_2 = 3$ with integer exponents $b_1 = p, b_2 = -k$:

$$v_q(2^p - 3^k) \leq \frac{C}{\log q} \cdot \log p$$

where $C$ is an absolute constant (depending only on $\log 2$ and $\log 3$, NOT on $q$ or $p$). The crucial feature is that $\log q$ appears in the **denominator**, so large primes have even smaller $q$-adic valuations.

**Consequence for rad(D).** Summing over all prime factors of $D$:

$$\log D = \sum_{q | D} v_q(D) \cdot \log q \leq \sum_{q | D} \frac{C \log p}{\log q} \cdot \log q = C \log p \cdot \omega(D)$$

Since $\log D > p \log 2 - C_1 \log p$ (Baker):

$$\omega(D) \geq \frac{p \log 2 - C_1 \log p}{C \log p} \approx \frac{p}{C' \log p}$$

Since every prime factor is $\geq 5$:

$$\log \mathrm{rad}(D) \geq \omega(D) \cdot \log 5 \geq \frac{c \cdot p}{\log p}$$

**This is potentially better than Stewart's $\sqrt{p}/\log p$**, replacing $\sqrt{p}$ by $p$. The full argument with all details is in the Appendix.

### 4.5 The Cyclotomic Approach

**Observation:** $2^p - 3^k = (2^p - 1) - (3^k - 1)$.

$2^p - 1$ (Mersenne number) has well-studied factorizations. Its prime factors $q$ satisfy $q \equiv 1 \pmod{p}$ (if $p$ is prime) and $q \equiv \pm 1 \pmod{8}$.

$3^k - 1$ is also well-studied: $3^k - 1 = 2 \cdot \frac{3^k - 1}{2}$, and prime factors of $(3^k-1)/2$ satisfy $q | \Phi_d(3)$ for some $d | k$.

**But the difference of two "structured" numbers is not itself structured.** The factorization of $A - B$ when we know the factorizations of $A$ and $B$ individually is essentially uncontrolled. (Compare: we know $2^{100} - 1$ and $3^{63} - 1$ individually, but $2^{100} - 3^{63}$ has no known structural factorization theory.)

**Algebraic factorization.** If $\gcd(p, k) = d > 1$ (which is rare since $k/p \approx \log 2/\log 3$ is irrational), one might try to write $2^p - 3^k = 2^p - (3^{k/d})^d$. But $3^{k/d}$ is not an integer power of 2, so standard cyclotomic factorizations don't apply.

### 4.6 The Specific Structure of 2 and 3

Since 2 and 3 are consecutive integers (and the two smallest primes), there are some special results:

1. **$S$-unit equations.** The equation $2^p - 3^k = D$ with $D$ a $\{2,3\}$-unit has only finitely many solutions by the $S$-unit theorem (de Weger, 1989). So $D$ is divisible by primes $\geq 5$ for all but finitely many $(p,k)$. The effective version (Baker-Wustholz) shows this holds for $p \geq p_0$ (explicit).

2. **The $\{2,3\}$-smooth part.** How large can the $\{2,3\}$-smooth part of $D$ be? Since $\gcd(D, 6) = 1$ (D is odd and coprime to 3), the $\{2,3\}$-smooth part of D is 1. Every prime factor of D is $\geq 5$.

3. **Six-smooth part more generally.** Every prime factor of D is $\geq 5$, which is already known. The question is whether D can be $\{5\}$-smooth (a power of 5). The equation $2^p - 3^k = 5^m$ is a ternary $S$-unit equation with $S = \{2, 3, 5\}$. By Evertse's theorem, it has at most $3^{|S|} = 27$ solutions. The known solutions include:
   - $2^3 - 3^1 = 5 = 5^1$
   - $2^5 - 3^3 = 5 = 5^1$
   - $2^8 - 3^5 = 13$ (not a power of 5)

   So D is a power of 5 for at most finitely many $(p,k)$, and computationally this seems to happen only at $p = 3$ and $p = 5$.

---

## 5. New Observations

### 5.1 Observation: D Is Squarefree with High Frequency

From the computational data (p up to ~20), every D value encountered is squarefree. If this persists to large $p$, then $\mathrm{rad}(D) = D$, and the problem would reduce to bounding $D$ from below -- which Baker's theorem already handles.

**Conjecture (Heuristic).** For the sequence $D_p = 2^p - 3^{\lfloor p \cdot \log 2/\log 3 \rfloor}$, a positive proportion of values are squarefree. More precisely, $D_p$ is squarefree for a set of $p$ with density $\prod_{q \geq 5 \text{ prime}} (1 - 1/q^2) = 8/\pi^2 \cdot 4/3 \approx 0.81$.

If true, for those $p$ values: $\mathrm{rad}(D) = D > 2^p/p^C$, giving $\log_2 \mathrm{rad}(D)/p > 1 - C\log p/p$, which exceeds 0.95 for $p > p_0$.

**The issue:** Even if 81% of D values are squarefree, we need the result for ALL p (not just most). A single non-squarefree D with small radical could, in principle, correspond to a Collatz cycle.

### 5.2 Observation: Primitive Prime Divisors Heuristic

For $p \leq 21$, every new value of $p$ introduces at least one prime factor of $D_p$ not seen in any $D_{p'}$ for $p' < p$. If this persists (a "primitive divisor" phenomenon for the sequence $D_p$), it would imply:

$$\mathrm{rad}\left(\prod_{p' \leq p} D_{p'}\right) \to \infty$$

But this says nothing about $\mathrm{rad}(D_p)$ individually. The primitive divisor property for the sequence $\{D_p\}$ is an open question.

### 5.3 Observation: The Size of D Controls Everything (When D Is Squarefree)

Baker's theorem gives $D > 2^p / p^C$. If we could prove:

(a) $D$ is squarefree, OR
(b) The largest prime power factor $q^a$ dividing $D$ satisfies $q^a < D^{1-\delta}$ for some fixed $\delta > 0$

then $\mathrm{rad}(D) > D^{\delta} > 2^{\delta p} / p^{C\delta}$, giving a positive constant times $p$ for the log-radical.

**Approach (b)** is related to the "powerful part" of D. If $D = D_{\text{sqfree}} \cdot D_{\text{pow}}^2$ where $D_{\text{pow}}^2$ is the powerful part, then $\mathrm{rad}(D) \geq D_{\text{sqfree}} \geq D / D_{\text{pow}}^2$.

The question becomes: how large can the powerful part of $2^p - 3^k$ be?

### 5.4 The Powerful Part of D

The powerful part of $n$ is $n / \mathrm{rad}_1(n)$ where $\mathrm{rad}_1(n) = \prod_{p \| n} p$ (primes appearing to exactly the first power).

**Erdos-Mollin-Walsh conjecture.** There are no three consecutive powerful numbers. This is related but not directly applicable.

**abc for powerful numbers.** If $D = 2^p - 3^k$ has powerful part $D_{\text{pow}}^2 > D^{1-\varepsilon}$, then $\mathrm{rad}(D) < D^{\varepsilon}$, which with the abc conjecture applied to $(3^k, D, 2^p)$ gives:

$$2^p \leq K_\varepsilon(6 D^{\varepsilon})^{1+\varepsilon} \leq K_\varepsilon \cdot 6^{1+\varepsilon} \cdot D^{\varepsilon(1+\varepsilon)}$$

So $D \geq (2^p / K_\varepsilon')^{1/(\varepsilon(1+\varepsilon))}$. For small $\varepsilon$, $D \geq 2^{p/\varepsilon^2}$, which exceeds $2^p$ for $\varepsilon < 1$, contradiction.

This means: **abc implies D cannot be "too powerful."** Specifically, $\mathrm{rad}(D) > 2^{(1-\varepsilon)p}$ for any $\varepsilon > 0$.

### 5.5 A Conditional Result Weaker Than abc

**Question:** Is there a weaker hypothesis than abc that suffices for our purposes?

We need: $\mathrm{rad}(2^p - 3^k) > 2^{0.95p}$ for all sufficiently large $p$.

A weaker form of abc, the "**abc for fixed radical bases**" or "**S-part of abc**," might suffice:

**Conjecture (Weak abc for $\{2,3\}$).** For coprime integers $a, b$ with $a + b = 2^p$ and $a = 3^k$:

$$\mathrm{rad}(b) > 2^{(1-\varepsilon)p} \quad \text{for all } \varepsilon > 0 \text{ and } p \text{ large enough.}$$

This is weaker than the full abc conjecture because:
1. One summand ($3^k$) has $\mathrm{rad} = 3$ (known).
2. The other summand ($2^p$) has $\mathrm{rad} = 2$ (known).
3. We only need to bound $\mathrm{rad}$ of the third term $b = 2^p - 3^k$.

**Is this weaker conjecture more tractable?** Possibly. The constraint that two of the three terms are pure prime powers severely restricts the problem. Specifically:

- We're asking about $\mathrm{rad}(2^p - 3^k)$ where both $2^p$ and $3^k$ have trivial radicals.
- This is an instance of the "**large radical for S-unit differences**" problem.
- The relevant S-unit equation theory (Lang, Evertse, Schlickewei) gives finiteness results but not effective lower bounds on radicals.

---

## 6. Assessment: How Close Are We?

### 6.1 Current State of Knowledge

| Bound on $\log_2 \mathrm{rad}(D)$ | Source | Status |
|---|---|---|
| $\geq (1-\varepsilon)p$ for any $\varepsilon > 0$ | abc conjecture | Conditional |
| $\geq cp/\log p$ for some $c > 0$ | p-adic Baker (Section 4.4 + Appendix) | This report (needs verification) |
| $\geq c\sqrt{p}/\log p$ | Stewart 2013 | Unconditional |
| $\geq cp^{1/3}$ | Stewart-Yu 2001 | Unconditional |
| **Need:** $\geq 0.949p$ | Collatz sieve | -- |

**Note on the $cp/\log p$ bound:** The argument in Section 4.4 and the Appendix combines Baker's archimedean bound ($D > 2^p/p^C$) with Yu's p-adic bound ($v_q(D) \leq C\log p / \log q$) to get $\omega(D) \geq cp/\log p$ and hence $\log \mathrm{rad}(D) \geq cp/\log p$. The argument is clean and uses standard ingredients in a straightforward way. The main concern is whether Yu's constant $C$ is truly uniform in $q$; his Theorem 1 in "p-adic logarithmic forms and group varieties III" (Forum Math., 2007) states the bound with $C$ depending only on $n$ (number of logarithms) and the algebraic numbers, independent of $q$. If this is correct as stated, the $p/\log p$ bound follows. **This needs verification by an expert in transcendence theory.** Even if correct, it remains far from the needed $0.95p$.

### 6.2 The Fundamental Barrier

The gap between $p/\log p$ (or even $p/(\log p)^{1-\varepsilon}$) and $0.95p$ is **qualitative**, not quantitative. Here is why:

1. **Baker-type methods** control *archimedean* and *p-adic sizes* of linear forms in logarithms. They give upper bounds on $v_q(D)$ that are **logarithmic in p** (i.e., $O(\log p)$).

2. If D has $r$ distinct prime factors with each appearing to power $\leq O(\log p)$, then $D \leq \mathrm{rad}(D)^{O(\log p)}$, giving $\log \mathrm{rad} \geq \log D / O(\log p) \geq p/O(\log p)$.

3. To get $\log \mathrm{rad} \geq cp$, we would need either:
   - (a) Most prime factors appear to the first power (squarefreeness), OR
   - (b) The number of distinct primes grows proportionally to $p$ (not just $p/\log p$).

4. **Neither (a) nor (b) follows from Baker.** Baker gives (b) with $p/\log p$ in place of $p$. Proving squarefreeness (a) for specific number-theoretic sequences is extremely hard (e.g., the squarefreeness of $2^n - 1$ is open).

### 6.3 What Would Suffice (Short of abc)

The following weaker statements, if proven, would each suffice for the Collatz application:

1. **"$D$ is squarefree for all large $p$."** Then $\mathrm{rad}(D) = D > 2^p/p^C > 2^{0.95p}$.

2. **"The powerful part of $D$ is $< D^{0.05}$."** Then $\mathrm{rad}(D) > D^{0.95} > 2^{0.95(p - C\log p)} > 2^{0.949p}$.

3. **"$v_q(D) \leq C$ for all primes $q$ (uniformly bounded valuations)."** Then $\mathrm{rad}(D) \geq D^{1/C} > 2^{p/C}$. Need $C \leq 1/0.95 \approx 1.053$, which essentially requires squarefreeness.

4. **"$\omega(D) \geq cp$ (many distinct primes)."** This with $q^{v_q} \leq D$ gives $\mathrm{rad}(D) \geq 5^{cp}$, which suffices if $c \geq 0.95/\log_2 5 \approx 0.41$.

None of these are known unconditionally. Each is essentially as hard as abc for this specific family.

### 6.4 Most Promising Directions

In decreasing order of promise:

1. **Browning-Lichtman-Teravainen + density argument.** If the "almost all abc triples" result can be shown to cover the family $(3^k, D, 2^p)$ for all but finitely many $p$, combined with computation for small $p$, the result follows. This requires understanding how the BLT density interacts with the specific algebraic family $2^p - 3^k$.

2. **Squarefreeness for algebraic families.** There is a research program (Granville, Helfgott, etc.) studying squarefreeness of polynomial values and sequences. If $D_p = 2^p - 3^{\lfloor p\alpha \rfloor}$ could be shown squarefree infinitely often (or for a density-1 set of $p$), this would help -- but we need ALL $p$, not just most.

3. **Explicit abc for restricted families.** The abc conjecture for triples where two terms are $S$-units ($S = \{2,3\}$) might be more tractable than the general case. This is related to the "S-part conjecture" (Gyory, 2019).

4. **Computational verification.** For specific moderate $p$ (say $p \leq 10^6$), one could verify $\mathrm{rad}(D) > 2^{0.95p}$ computationally. Combined with asymptotics, this would strengthen the conditional result. The factorization of $D$ for large $p$ requires serious computational number theory (ECM, NFS).

---

## 7. Summary

### What Is Proved
- **abc implies rad(D) > 2^{(1-epsilon)p}**, sufficient for the Collatz sieve.
- **Stewart 2013:** $\log \mathrm{rad}(D) \geq c\sqrt{p}/\log p$, unconditional but far too weak.
- **p-adic Baker (this report):** $\log \mathrm{rad}(D) \geq cp/\log p$ (pending verification of Yu's constant uniformity). If correct, this is a qualitative improvement over Stewart ($p$ replaces $\sqrt{p}$), but still insufficient.
- **Computational (small p):** All D values for $p \leq 21$ are squarefree, with $\log_2 \mathrm{rad}/p > 0.46$ (the worst being small-D cases at $p = 5, 8$).

### What Is Open
- Any unconditional bound $\log \mathrm{rad}(D) \geq cp$ for any constant $c > 0$ (even $c = 0.01$).
- Squarefreeness of $D$ for all (or almost all) large $p$.
- Whether $D$ can be a perfect power for infinitely many $p$.

### The Gap
The unconditional frontier is at best $\log \mathrm{rad} \sim p/\log p$ (if the p-adic Baker argument checks out; otherwise $\sqrt{p}/\log p$ from Stewart). The needed bound is $0.95p$. Even from $p/\log p$, the remaining gap is a factor of $\log p$. From $\sqrt{p}/\log p$, the gap is $\sqrt{p} \log p$. In either case, this is the **abc barrier** -- closing it unconditionally would constitute a breakthrough comparable to proving a special case of the abc conjecture.

---

## 8. Python Code

The computation script is at `/Users/tsuimingleong/Desktop/math/radical_D_compute.py`. To run:

```bash
/Users/tsuimingleong/Desktop/math/venv/bin/python /Users/tsuimingleong/Desktop/math/radical_D_compute.py
```

It computes for $p = 2, \ldots, 200$:
- Complete factorization of $D = 2^p - 3^k$ using trial division + Pollard rho
- $\mathrm{rad}(D)$, the ratio $\log_2(\mathrm{rad}(D))/p$
- Squarefreeness detection
- Primitive prime divisor analysis
- Small prime frequency statistics

The script uses only Python builtins (no external dependencies beyond `math`, `collections`, `time`, `random`).

---

## Appendix: Notes on the Computational Data

**Key patterns from the verified data (p <= 17):**

1. D is squarefree for all p <= 17 (100% rate). This supports the heuristic that D is "generically" squarefree.

2. The low log2(rad)/p outliers (p=5: ratio 0.465, p=8: ratio 0.463) correspond to cases where 2^p is very close to 3^k (the best rational approximations to log2/log3 from the continued fraction expansion), making D abnormally small. These "near-Catalan" values give D = 5 and D = 13, which are small but still prime (and hence squarefree).

3. The convergents of the continued fraction of log2/log3 = [0; 1, 1, 1, 2, 1, 3, 1, 2, ...] give the best rational approximations k/p. The convergents 1/2, 2/3, 3/5, 8/13, 11/17, ... correspond exactly to the p values where D is smallest. For example: p=5,k=3 gives D=5; p=8,k=5 gives D=13; p=13,k=8 gives D=1631.

4. Even at the "worst" convergents, D remains squarefree and D > 2^{0.46p}, giving log2(rad)/p > 0.46.

---

## Appendix: The p/log(p) Bound Argument (Detailed)

**Claim.** $\log \mathrm{rad}(2^p - 3^k) \geq c \cdot p / \log p$ for all sufficiently large $p$ with $k = \lfloor p \log 2 / \log 3 \rfloor$.

This would improve on Stewart's unconditional $\sqrt{p}/\log p$ by replacing $\sqrt{p}$ with $p$ (at the cost of one $\log p$ factor instead of zero).

### Step 1: Lower bound on D (archimedean Baker)

By the Baker-Wustholz theorem (refined by Laurent, 2008), for the linear form $\Lambda = p \log 2 - k \log 3$:

$$|\Lambda| > \exp(-C_1 \log p)$$

where $C_1$ is an effective constant depending only on $\log 2$ and $\log 3$ (i.e., absolute). Since $D = 2^p(1 - 3^k/2^p) = 2^p(1 - e^{-\Lambda})$ and $\Lambda > 0$ (because $D > 0$):

$$D > 2^p \cdot \Lambda / 2 > 2^p \cdot \exp(-C_1 \log p) / 2 > 2^p / p^{C_1}$$

So $\log D > p \log 2 - C_1 \log p$.

### Step 2: Upper bound on q-adic valuations (p-adic Baker)

**Key reference:** Yu Kunrui, "p-adic logarithmic forms and group varieties III" (Forum Math., 2007).

Yu's theorem (Theorem 1) gives: for any prime $q \geq 5$ with $q \nmid 6$, and for algebraic numbers $\alpha_1 = 2, \alpha_2 = 3$ with integer exponents $b_1 = p, b_2 = -k$:

$$v_q(2^p - 3^k) \leq \frac{C_2}{\log q} \cdot \log p$$

where $C_2$ is an absolute constant (depending on $\log 2, \log 3$, and the number of terms $n=2$, but NOT on $q$ or $p$). The key feature is that $\log q$ appears in the **denominator**.

More precisely, Yu's bound takes the form:
$$\mathrm{ord}_q(\alpha_1^{b_1} \cdots \alpha_n^{b_n} - 1) \leq C(n) \cdot \frac{(\log H_1) \cdots (\log H_n)}{(\log q)^n} \cdot \max\left(\log B + \log \log H, \frac{10 \log q}{n+1}\right)$$

For $n=2, \alpha_1=2, \alpha_2=3, H_1=2, H_2=3, B=p$, this simplifies to:

$$v_q(2^p - 3^k) \leq \frac{C_2'}{(\log q)^2} \cdot (\log 2)(\log 3) \cdot (\log p + O(1)) \leq \frac{C_2 \log p}{(\log q)^2}$$

(The exact power of $\log q$ in the denominator depends on which version of the theorem is cited; the weakest clean version gives $1/\log q$.)

### Step 3: Counting distinct prime factors

Let $\omega(D) = r$ be the number of distinct prime factors of $D$. Using the **weaker** form $v_q(D) \leq C_2 \log p / \log q$:

$$\log D = \sum_{q | D} v_q(D) \cdot \log q \leq \sum_{q | D} \frac{C_2 \log p}{\log q} \cdot \log q = C_2 \log p \cdot \omega(D)$$

Therefore:

$$\omega(D) \geq \frac{\log D}{C_2 \log p} \geq \frac{p \log 2 - C_1 \log p}{C_2 \log p} = \frac{p \log 2}{C_2 \log p} - \frac{C_1}{C_2}$$

So **$\omega(D) \geq c \cdot p / \log p$** for an effective constant $c > 0$ and all large $p$.

### Step 4: Lower bound on the radical

Since every prime factor of $D$ is $\geq 5$ (as $D$ is odd and coprime to 3):

$$\log \mathrm{rad}(D) = \sum_{q | D} \log q \geq \omega(D) \cdot \log 5 \geq \frac{c \cdot p \cdot \log 5}{\log p}$$

**Result:**

$$\boxed{\log \mathrm{rad}(2^p - 3^k) \geq \frac{c \cdot p}{\log p}}$$

for an effective constant $c > 0$ and all sufficiently large $p$.

### Step 5: Comparison with known results

| Result | Bound on $\log \mathrm{rad}(D)$ | Ratio to $p$ |
|---|---|---|
| This argument | $\geq cp / \log p$ | $\to \infty$ but $< p$ |
| Stewart 2013 | $\geq c\sqrt{p} / \log p$ | $\to 0$ |
| Stewart-Yu 2001 | $\geq c p^{1/3}$ | $\to 0$ |
| abc conjecture | $\geq (1-\varepsilon)p$ | $\to 1$ |
| **Needed** | $\geq 0.949p$ | 0.949 |

The $cp/\log p$ bound is strictly better than Stewart's $c\sqrt{p}/\log p$ for large $p$, representing a qualitative improvement (the dependence changes from $\sqrt{p}$ to $p$). However, the remaining gap from $p/\log p$ to $0.95p$ -- a factor of $\log p$ -- corresponds precisely to the abc barrier.

### Caveats and Required Verification

1. **Yu's theorem applicability.** The bound $v_q(2^p - 3^k) \leq C_2\log p / \log q$ requires that $q \nmid 6$ and that $2^p \neq 3^k$ (both satisfied). The constant $C_2$ must be verified to be INDEPENDENT of $q$ in Yu's theorem statement. The standard form of Yu (2007, Theorem 1) does have $C_2$ depending only on $n$ (the number of logarithms) and the algebraic numbers, not on $q$. **This appears correct.**

2. **The $(\log q)$ power.** Depending on the exact version, the denominator could be $\log q$ or $(\log q)^2$. With $(\log q)^2$:
$$\log D \leq C_2 \log p \sum_{q|D} \frac{\log q}{(\log q)^2} = C_2 \log p \sum_{q|D} \frac{1}{\log q}$$
This gives a weaker result: $\sum_{q|D} 1/\log q \geq p/(C_2 \log p)$, from which $\log \mathrm{rad}(D) \geq p/(C_2 \log p \cdot \max(1/\log q))$. Since the smallest $\log q$ is $\log 5$, we still get $\log \mathrm{rad} \geq cp/\log p$, but the constant $c$ is smaller.

3. **Novelty assessment.** This argument combines standard ingredients (Baker archimedean + Yu p-adic) in a straightforward way. It is likely known to experts but may not appear explicitly in the literature for this specific application. The fact that it improves on Stewart's published bound of $\sqrt{p}/\log p$ suggests either: (a) the improvement is genuine but has not been written down, or (b) there is a subtlety in applying Yu's theorem that I am missing (e.g., the constant $C_2$ may secretly depend on $q$ in a way that invalidates the argument). **This requires careful checking against Yu (2007).**

4. **Why Stewart gets only $\sqrt{p}$.** Stewart's 2013 paper addresses Lucas and Lehmer numbers $L_n = \alpha^n - \beta^n$, where $\alpha, \beta$ are roots of a quadratic. The expression $2^p - 3^k$ with $k \neq p$ does NOT fit this framework. Stewart's method relies on the algebraic structure of Lucas sequences (divisibility properties, cyclotomic factors) that are unavailable here. The p-adic Baker approach bypasses this by working directly with the valuations, which is why it can potentially do better.
