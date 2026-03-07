# Direction 6g-viii: Prime-D Sieve Completion + Composite-D Descent

*Developed 2026-03-06 (Session 8)*

## 0. Executive Summary

Direction 6g-viii separates the Collatz no-cycles problem into two cases based on the primality of $D = 2^p - 3^k$:

- **Prime $D$** (~6-10% of valid $(p,k)$ pairs): The sieve has only one prime to work with: $D$ itself. Theorem 4's block decomposition requires $\operatorname{ord}_D(2) \leq p$ AND $\operatorname{ord}_D(2) > 2\sqrt{D}$. Since $\sqrt{D} \approx 2^{p/2} \gg p$, these conditions are simultaneously impossible for $p \geq 5$. The sieve at modulus $D$ is provably vacuous.

- **Composite $D$** (~90%+): The sieve works if enough prime factors of $D$ are "handleable." Computationally, the handleable fraction is often below 90%, and the smallest largest-prime-factor ratio drops to 0.18. Proving a large prime factor exists for all $D = 2^p - 3^k$ reduces to a specific (weaker-than-abc) conjecture.

**Status: Direction 6g-viii EXPLORED, FAILS. Both sub-problems are blocked.**

---

## 1. Setup and Motivation

### 1.1. The Sieve Approach (Review)

From Theorems 4-5 and the sieve framework: if we can show
$$\frac{\binom{p}{k}}{\operatorname{rad}(D)} \to 0$$
then no cycles exist for large $p$. This requires $\operatorname{rad}(D) > \binom{p}{k} \approx 2^{0.95p}$.

The idea of 6g-viii: split into cases based on $D$'s factorization.

### 1.2. The Two Cases

**Case 1: $D$ is prime.** Then $\operatorname{rad}(D) = D \approx 2^p > 2^{0.95p}$, so the first moment gives $\mathbb{E}[\#] \approx 2^{-0.05p} \to 0$. The sieve "morally works" — but we need to make it rigorous.

**Case 2: $D$ is composite.** Need the product of handleable primes to exceed $2^{0.95p}$.

---

## 2. Prime D: The Block Decomposition Impossibility

### 2.1. Theorem 4 Requirements

Theorem 4 applies to a prime $q$ when $d = \operatorname{ord}_q(2) > 2\sqrt{q}$. It works by partitioning $\{0, \ldots, p-1\}$ into $L = \lfloor p/d \rfloor$ blocks of size $d$, with Gauss sum saving $\rho = \sqrt{q}/d < 1$ per single-selection block.

For $q = D$ (prime), $d = \operatorname{ord}_D(2)$:

**Condition A**: $d \leq p$ (for $L \geq 1$ blocks)
**Condition B**: $d > 2\sqrt{D}$ (for Gauss saving $\rho < 1$)

### 2.2. The Impossibility Proof

**Claim**: For $p \geq 5$, conditions (A) and (B) cannot hold simultaneously when $D = 2^p - 3^k$.

*Proof.* Conditions (A) + (B) require $p \geq d > 2\sqrt{D}$, hence $p > 2\sqrt{D}$, i.e., $p^2 > 4D$.

Since $D = 2^p - 3^k > 0$ and $3^k < 2^p$, we have $D \geq 1$. More precisely, $D > 2^p/p^{10.6}$ by the Rhin bound (Theorem 1). So:

$$p^2 > 4D > 4 \cdot 2^p / p^{10.6}$$

This requires $p^{12.6} > 4 \cdot 2^p$, which fails for $p \geq 47$ (since $2^p$ grows exponentially while $p^{12.6}$ grows polynomially).

For small $p$: direct computation shows that for ALL prime $D = 2^p - 3^k$ with $p \geq 5$ (except the trivial $D = 5$ at $(p,k) = (5,3)$), $\operatorname{ord}_D(2) > p$, giving $L = 0$ blocks. In fact, $\operatorname{ord}_D(2)$ is typically close to $D - 1$ (the maximal order). $\square$

### 2.3. Computational Verification

For all prime $D$ with $D \leq 10^{10}$ arising from valid $(p,k)$ with $p \leq 60$:

| $(p,k)$ | $D$ | $\operatorname{ord}_D(2)$ | $L = \lfloor p/d \rfloor$ | $\rho = \sqrt{D}/d$ |
|---|---|---|---|---|
| (5,3) | 5 | 4 | 1 | 0.500 |
| (5,1) | 29 | 28 | 0 | 0.179 |
| (6,1) | 61 | 60 | 0 | 0.117 |
| (8,5) | 13 | 12 | 0 | 0.250 |
| (9,4) | 431 | 43 | 0 | 0.465 |
| (10,1) | 1021 | 340 | 0 | 0.091 |
| (16,5) | 65293 | 65292 | 0 | 0.004 |
| (20,1) | 1048573 | 1048572 | 0 | 0.001 |

**Every prime $D > 5$ gives $L = 0$ blocks.** The saving factor $\rho < 1$ is irrelevant — there are zero blocks to apply it to.

### 2.4. Why Other Character Sum Approaches Also Fail

Even without the block decomposition, the character sum $F(t) = \sum_{|I|=k} e(tS(I)/D)$ satisfies:
- By Parseval: $\sum_{t=0}^{D-1} |F(t)|^2 = D \cdot \binom{p}{k}$
- The count: $\#\{I : D | S(I)\} = \binom{p}{k}/D + (1/D) \sum_{t=1}^{D-1} F(t)$
- By Cauchy-Schwarz: $\left|\sum_{t \geq 1} F(t)\right| \leq \sqrt{D \cdot \sum |F(t)|^2} = D \cdot \sqrt{\binom{p}{k}}$

For the count to be 0: need $\left|\sum F(t)\right| < \binom{p}{k}$. But:

$$\frac{D \sqrt{\binom{p}{k}}}{\binom{p}{k}} = \frac{D}{\sqrt{\binom{p}{k}}} \approx \frac{2^p}{2^{0.475p}} = 2^{0.525p} \to \infty$$

The Cauchy-Schwarz bound exceeds the target by a factor of $2^{0.525p}$. Square-root cancellation is exponentially insufficient.

---

## 3. Equidistribution Confirmed (Small Cases)

Despite the inability to PROVE equidistribution, computation confirms it for small $(p,k)$:

For all 50+ prime $D$ tested with $C(p,k) \leq 10^7$:
- $S(I) \bmod D$ is equidistributed (CV $\leq 0.35$)
- $\#\{I : D | S(I)\} = 0$ in 48/50 cases
- The two exceptions ($\#\{D|S\} = 2$) occur at $(6,3)$ with $D = 37$ and $(14,7)$ with $D = 14197$, where $\mathbb{E}[\#] = 0.54$ and $0.24$ respectively — close to the threshold

The heuristic $\mathbb{E}[\#] \approx \binom{p}{k}/D < 1$ is accurate. The problem is entirely about PROVING it.

---

## 4. Composite D: Factorization Analysis

### 4.1. Primality Statistics

| $p$ range | Prime $D$ / Total | Percentage |
|---|---|---|
| $[5, 30]$ | 54 / 274 | 19.7% |
| $[31, 60]$ | 64 / 846 | 7.6% |
| $[61, 100]$ | 84 / 2012 | 4.2% |

**Correction**: The initial estimate "~50% of $D$ are prime" was wrong. Only 6-10% of valid $(p,k)$ pairs give prime $D$, and the fraction decreases with $p$. Most pairs have small $k$ (far from the critical ratio $k/p \approx \log 2/\log 3$), giving large $D$ that are usually composite.

### 4.2. Largest Prime Factor

For 945 composite $D$ with $p \leq 60$ (all fully factored):
- Mean $\log_2(\text{lpf}) / \log_2(D) = 0.564$
- Min ratio: **0.183** at $(p,k) = (48,18)$ with $D = 7 \cdot 13^2 \cdot 61 \cdot 139 \cdot 229 \cdot 283 \cdot 433$
- Max ratio: 0.961

Many composite $D$ have largest prime factor well below $D^{0.95}$:
- Ratio $< 0.5$: abundant (hundreds of cases)
- Ratio $< 0.3$: multiple cases (e.g., $(60,30)$, $(60,12)$, $(54,6)$, $(48,18)$)

**This kills the naive sieve for composite $D$**: the product of handleable primes can be far smaller than $\binom{p}{k}$ when $D$ has many small factors.

### 4.3. Handleable Fraction

A prime $q | D$ is "handleable" if $\operatorname{ord}_q(2) > 2\sqrt{q}$ (Theorem 4 condition). The handleable fraction $= \sum_{\text{handleable } q | D} e_q \log q / \log D$.

Many composite $D$ have handleable fraction **below 0.90**:
- $(7,1)$: $D = 5^3$, handleable = 0.00 (single prime, small order)
- $(7,2)$: $D = 7 \cdot 17$, handleable = 0.00
- $(12,4)$: $D = 5 \cdot 11 \cdot 73$, handleable = 0.29
- $(14,6)$: $D = 5 \cdot 31 \cdot 101$, handleable = 0.48

The sieve needs handleable fraction $> 0.95$ (since $\binom{p}{k}/D \approx 2^{-0.05p}$, we need the handleable part to cover all but the 5% margin). Falling below this threshold means the sieve bound exceeds 1.

---

## 5. The Scale Gap (Unified Diagnosis)

### 5.1. Why Both Cases Fail

The fundamental issue is the **exponential scale gap** between $p$ (the number of positions) and $D \approx 2^p$ (the divisibility modulus).

**For prime $D$**: The block decomposition uses blocks of size $d = \operatorname{ord}_D(2)$, giving $L = p/d$ blocks. Since $D \approx 2^p$, even the smallest useful $d$ (at least $2\sqrt{D} = 2^{p/2+1}$) gives $L = p/2^{p/2+1} \approx 0$. The "resolution" of the block method is $\sim p$ positions, but the modulus is $\sim 2^p$.

**For composite $D$**: Each prime $q | D$ with $\operatorname{ord}_q(2) = d_q$ gives blocks of size $d_q$ and $L_q = p/d_q$ blocks. The sieve combines information from multiple primes. But the total "information" extracted is bounded by $\sum_q \log(1/\rho_q) \cdot L_q$, where $\rho_q = \sqrt{q}/d_q$ is the saving factor. For the sieve to work, this must exceed $\log \binom{p}{k} \approx 0.95p \log 2$. Each prime $q$ contributes at most $\log q$ to the total. So we need the product of handleable primes to exceed $2^{0.95p}$.

### 5.2. Connection to Barrier 1

The scale gap is the same barrier as **Barrier 1 (abc/size-counting)** from the barrier diagnostic:

- The sieve needs $\operatorname{rad}(D) > 2^{0.95p}$
- This is a specific case of the abc conjecture for $3^k + D = 2^p$
- The existing best unconditional bound (Stewart 2013) gives $\log \operatorname{rad}(D) \geq c\sqrt{p}/\log p$, far below the needed $0.95p \log 2$

Direction 6g-viii does NOT escape Barrier 1. It merely reformulates it as:
- **Prime $D$**: "prove equidistribution of $S$ mod $D$ when $D \approx 2^p$" (impossible with block decomposition)
- **Composite $D$**: "prove $D$ always has a large prime factor" (a specific abc-type conjecture)

---

## 6. What Would Be Needed

### 6.1. For Prime D

A method to bound $\#\{I : D | S(I)\}$ that does NOT use the block decomposition. This would require:
- Character sum cancellation beyond square-root: $|F(t)| \ll \binom{p}{k}^{1/2 - \delta}$ for some $\delta > 0$
- Or a completely different approach to equidistribution at exponential moduli
- The structural constraint $2^p \equiv 3^k \pmod{D}$ is the only "handle," but it doesn't help

### 6.2. For Composite D

Either:
- **(a)** Prove that $\max_{q | D} q > 2^{0.95p}$ for all valid $(p,k)$ — a specific large-prime-factor conjecture for $2^p - 3^k$
- **(b)** Prove that the product of handleable primes exceeds $2^{0.95p}$ — weaker, but still requires that most of $D$'s mass comes from primes with large multiplicative order of 2

Both require input from Diophantine approximation / abc theory that is currently unavailable.

---

## 7. Honest Assessment

### What 6g-viii Provides

1. **Clean case separation**: The prime/composite split is the correct way to organize the problem. Different tools apply to each case.

2. **The block decomposition impossibility**: For $p \geq 5$, Theorem 4 PROVABLY cannot work at modulus $q = D$. This is not a technical gap — it's a theorem. The conditions $d \leq p$ and $d > 2\sqrt{D}$ are contradictory.

3. **Corrected primality estimate**: $D$ is prime for only ~6-10% of pairs, not ~50%. The primality rate decreases with $p$.

4. **Quantitative factorization data**: The minimum largest-prime-factor ratio drops to 0.18, showing that some $D$ have very dispersed factorizations. The sieve cannot automatically handle these.

5. **The scale gap as a unifying diagnosis**: Both cases fail for the same reason — the gap between $p$ (number of positions) and $D \approx 2^p$ (modulus) is exponential, and no tool bridges this gap.

### What 6g-viii Cannot Provide

A proof of Part 1. The direction reduces the problem to two open sub-problems, both of which are blocked by the abc barrier (Barrier 1).

### Status

**Direction 6g-viii: EXPLORED, FAILS. Blocked at the exponential scale gap (= abc barrier in sieve language).**

---

## 8. Connection to Previous Work

6g-viii is the FINAL direction from the Session 7 brainstorm. With this analysis complete:

| Direction | Status | Barrier |
|---|---|---|
| 6g-vi (carry automaton) | Predicted fail (Q4) | Equivalence |
| 6g-vii (cascade correlation) | Explored, fails | 7.4× gap (abc in cascade language) |
| **6g-viii (prime-D sieve)** | **Explored, fails** | **Scale gap (abc in sieve language)** |
| 6g-ix (CSP) | Predicted fail (Q4) | Equivalence |
| 6g-x (induction on k) | Predicted fail (Q4) | Equivalence |
| 6g-xi (2-adic dynamics) | Explored, fails | Archimedean/non-arch. mismatch |

All six directions are now closed. The barrier diagnostic correctly predicted the failures of 6g-vi, ix, x, and the two "ambiguous" directions (6g-vii, viii) also failed with quantitative diagnoses.

**The project's conclusion stands**: No existing mathematical framework can prove Part 1 of the Collatz conjecture. New mathematics is required.
