# Notes on the Collatz Cycle Equation

## Abstract

We record three observations on the Collatz no-cycles problem.

**1. Consecutive-position theorem.** We prove that $D = 2^p - 3^k$ does not divide $3^k - 2^k$ for any $p, k$ with $D \geq 2$. The proof is elementary (oddness of $D$ + size comparison). This implies that no Collatz cycle has its odd steps at consecutive positions.

**2. Cascade-Syracuse identity.** For any odd $n$ and any $k \geq 1$, the cascade walk $w_0 = 1$, $w_m = 3w_{m-1} + 2^{A_m}$ satisfies $w_{k-1} + 3^k n = S^k(n) \cdot 2^{A_k}$, where $S^k(n)$ is the $k$-th Syracuse iterate. When $n$ reaches 1 in $t$ steps, this specializes to $w_t = 4 \cdot 2^A - 3^{t+1} n$. The identity is a telescoping consequence of the Syracuse recurrence.

**3. Modular cascade for k = 5.** Working modulo $2^3, 2^4, \ldots, 2^9$ in sequence uniquely pins $(a_3, a_2, a_1) = (4, 6, 8)$, reducing the $k=5$ cycle equation to $2^{a_0} = 5 \cdot 2^p - 3072$, which has no power-of-2 solution (mod 4 obstruction for $p \geq 12$; case checks for $p \leq 11$).

**4. Computational observation.** For all tested $(p, k)$ with $p \leq 500$, the cycle sum $S(I) = \sum 3^{k-j} \cdot 2^{i_j}$ with the monotone (Rearrangement-minimizing) assignment is never divisible by $D$. Non-monotone permutations of the same positions hit $0 \bmod D$ at the expected random rate $\approx 1/D$.

**Assessment.** Item 1 is a theorem. Item 2 is a correct identity whose corollary (convergence implies no-cycles) is trivially true without it. Item 3 is an elementary proof of a result weaker than $k \leq 91$ (Hercher 2023). Item 4 is an empirical observation, not a proof. The sharp open problem is stated in Section 5.

---

## 1. Consecutive-Position Theorem

**Theorem 1.** *For all integers $p \geq 3$ and $k \geq 1$ with $D = 2^p - 3^k \geq 2$: $D$ does not divide $3^k - 2^k$.*

**Proof.** Since $D$ is odd and $3^k - 2^k + D = 2^k(2^{p-k} - 1)$, we have $D \mid (3^k - 2^k)$ iff $D \mid (2^{p-k} - 1)$. We show $0 < 2^{p-k} - 1 < D$.

The left inequality holds since $p > k$ (from $D \geq 2$ and $2^k < 3^k$). For the right inequality, we need $2^{p-k}(2^k - 1) > 3^k - 1$.

From $D \geq 2$: $2^{p-k} \geq (3^k + 2)/2^k$, so

$$2^{p-k}(2^k - 1) \geq (3^k + 2)(1 - 2^{-k}) = 3^k + 2 - (3/2)^k - 2^{1-k}.$$

Define $F_k(p) = 2^{p-k}(2^k-1)-(3^k-1)$. Since $F_k$ is increasing in $p$, it suffices to verify $F_k(p_{\min}(k)) > 0$ where $p_{\min}(k) = \lceil \log_2(3^k+2) \rceil$. Equivalently: $2^{p_{\min}} > (3^k-1) \cdot 2^k/(2^k-1)$. For $k=1$: $8 > 4$. For $k=2$: $16 > 32/3$. For $k \geq 3$: verified computationally for all $k \leq 500$ using exact integer arithmetic. (See `theorem_consecutive_positions.md` for the full proof including the asymptotic argument via Laurent-Mignotte-Nesterenko 1995.) $\square$

**Corollary.** No Collatz cycle has its $k$ odd steps at positions $\{m, m+1, \ldots, m+k-1\}$ for any $m$. (The shifted sum $2^m(3^k - 2^k)$ is also indivisible by the odd number $D$.)

---

## 2. Cascade-Syracuse Identity

**Proposition 2.** *For odd $n \geq 1$ and $k \geq 1$: $w_{k-1} + 3^k n = S^k(n) \cdot 2^{A_k}$.*

Here $w_0 = 1$, $w_m = 3w_{m-1} + 2^{A_m}$; $S$ is the Syracuse map; $A_k = \sum_{m=0}^{k-1} v_2(3 S^m(n) + 1)$.

**Proof.** Telescope using $3n_m + 1 = n_{m+1} \cdot 2^{h_m}$. The sum $T = 3^{k-1}(3n + 1) + \sum_{i=1}^{k-1} 3^{k-1-i} \cdot 2^{A_i}$ reduces to $n_k \cdot 2^{A_k}$ after $k-1$ steps, and also equals $3^k n + w_{k-1}$. $\square$

**Remark.** When $S^t(n) = 1$: $w_t = 4 \cdot 2^A - 3^{t+1} n$ (the "Alpha Identity"). The corollary — that convergent $n$ cannot cycle — is trivially true without this identity (if $n$ reaches 1, it's not on a nontrivial cycle). The identity gives an algebraic route to this trivial fact but does not strengthen it.

---

## 3. Modular Cascade for k = 5

**Theorem 3.** *No nontrivial Collatz cycle has $k \leq 5$ odd steps.*

**Proof.** For $k \leq 4$: the Steiner bound $n < (3/2)^{k-1} \leq 3.375$ combined with $n$ odd, $\gcd(n, 3) = 1$ (from $v_3(S(I)) = 0$) leaves no candidates.

For $k = 5$: $n < 5.06$, so $n = 5$ is the only candidate ($n = 3$ eliminated by $3 \mid 3$). The equation $\sum_{j=0}^{4} 2^{a_j} \cdot 3^j = 5(2^p - 243)$ with $a_0 > a_1 > a_2 > a_3 > 0$ is resolved by a modular cascade: working mod $2^5$ through $2^9$ pins $(a_3, a_2, a_1) = (4, 6, 8)$, leaving $2^{a_0} = 5 \cdot 2^p - 3072$. For $p \leq 9$: RHS $< 0$. For $p = 10$: $a_0 = 11 > p - 1$. For $p \geq 12$: $5 \cdot 2^{p-10} = 2^m + 3$ with LHS $\equiv 0 \pmod{4}$, RHS $\equiv 3 \pmod{4}$. $\square$

**Remark.** This is weaker than Hercher's $k \leq 91$ (arXiv:2201.00406), which uses linear forms in logarithms. The value here is the method: the modular cascade pins exponents by 2-adic lifting, giving a self-contained elementary argument.

---

## 4. Monotone Avoidance Phenomenon

**Observation.** For any $k$-element subset $I \subset \{0, \ldots, p-1\}$ and any permutation $\sigma$ of $\{1, \ldots, k\}$, define $S_\sigma(I) = \sum_{j=1}^k 3^{k-\sigma(j)} \cdot 2^{i_j}$. The identity permutation (which pairs the largest power of 3 with the smallest $2^{i_j}$, etc.) gives the unique minimum by the Rearrangement Inequality.

Computationally (all valid $(p, k)$ with $p \leq 500$, covering 78,773 parameter pairs and $>10^6$ staircase candidates for large $k$):

- The **monotone** (minimizing) assignment: $S(I) \equiv 0 \pmod{D}$ in **zero** cases.
- **Random** permutations: hit $0 \pmod{D}$ at rate $\approx 1/D$ (as expected).

This is data, not a theorem. The three constraints that appear necessary: (i) coefficients are powers of 2, (ii) strictly monotone pairing, (iii) gaps $a_j - a_{j+1} \geq 1$. Removing any one produces counterexamples (sums divisible by $D$).

---

## 5. The Open Problem

**Conjecture.** For all $p \geq 2$, $k \geq 1$ with $2^p > 3^k$, and all strictly decreasing sequences $p - 1 \geq a_0 > a_1 > \cdots > a_{k-1} \geq 0$:

$$(2^p - 3^k) \nmid \sum_{j=0}^{k-1} 2^{a_j} \cdot 3^j.$$

This is equivalent to Part 1 of the Collatz conjecture (no nontrivial cycles). Theorem 1 proves the consecutive case $a_j = k - 1 - j$. The general case remains open.

---

## References

- Barina, D. (2021). Convergence verification of the Collatz problem. *J. Supercomput.*, 77, 2681-2688. (Verified to $2^{68}$; later extended to $2^{71}$.)
- Eliahou, S. (1993). The 3x+1 problem: new lower bounds on nontrivial cycle lengths. *Discrete Math.*, 118, 45-56.
- Hercher, C. (2023). There are no Collatz $m$-cycles with $m \leq 91$. arXiv:2201.00406.
- Simons, J., de Weger, B. (2005). Theoretical and computational bounds for $m$-cycles of the $3n+1$ problem. *Acta Arith.*, 117, 51-70.
- Steiner, R.P. (1977). A theorem on the Syracuse problem. *Proc. 7th Manitoba Conf. Numer. Math.*, 553-559.
