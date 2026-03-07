# k=5 Collatz Cycle Equation: Complete Analysis

## The Equation

For k=5, n=5, the Collatz cycle equation is:

$$2^{a_0} + 3 \cdot 2^{a_1} + 9 \cdot 2^{a_2} + 27 \cdot 2^{a_3} + 81 = 5(2^p - 243)$$

**Constraints:** $p \geq 8$, $a_0 > a_1 > a_2 > a_3 \geq 1$, $a_0 \leq p-1$.

Equivalently (subtracting 81 from both sides):

$$2^{a_0} + 3 \cdot 2^{a_1} + 9 \cdot 2^{a_2} + 27 \cdot 2^{a_3} = 5 \cdot 2^p - 1296$$

---

## Result

**Theorem.** The k=5 equation has **no solutions**.

---

## Proof

### Step 1: Size Bound

The maximum LHS occurs at $(a_0, a_1, a_2, a_3) = (p-1, p-2, p-3, p-4)$:

$$\text{max LHS} = 2^{p-1} + 3 \cdot 2^{p-2} + 9 \cdot 2^{p-3} + 27 \cdot 2^{p-4} + 81 = \frac{65}{16} \cdot 2^p + 81$$

The RHS is $5 \cdot 2^p - 1215$.

For no solution: $\frac{65}{16} \cdot 2^p + 81 < 5 \cdot 2^p - 1215$, which gives $2^p > \frac{1296 \cdot 16}{15} = 1382.4$, i.e., $p \geq 11$.

**Conclusion:** Only $p \in \{8, 9, 10\}$ are possible from size considerations alone.

Verification:

| p  | max LHS | RHS   | Feasible? |
|----|---------|-------|-----------|
| 8  | 1121    | 65    | Yes (but RHS < min LHS after modular constraints) |
| 9  | 2161    | 1345  | Yes       |
| 10 | 4241    | 3905  | Yes       |
| 11 | 8401    | 9025  | **No**    |

### Step 2: Modular Cascade

We apply a sequence of modular constraints, each one pinning down the next exponent.

#### Mod 8

- $1296 \equiv 0 \pmod{8}$, and $5 \cdot 2^p \equiv 0 \pmod{8}$ for $p \geq 3$, so RHS $\equiv 0 \pmod{8}$.
- LHS mod 8 contributions:
  - $a_3 = 1$: $27 \cdot 2 = 54 \equiv 6$; $a_3 = 2$: $27 \cdot 4 = 108 \equiv 4$; $a_3 \geq 3$: $\equiv 0$.
  - $a_2 = 2$: $9 \cdot 4 = 36 \equiv 4$; $a_2 \geq 3$: $\equiv 0$.
  - All other terms $\equiv 0$ for $a_1 \geq 3$, $a_0 \geq 4$.
- Checking: $a_3 \in \{1,2\}$ always gives LHS $\not\equiv 0$. **Must have $a_3 \geq 3$.**

#### Mod 16

- $1296 \equiv 0 \pmod{16}$, RHS $\equiv 0$.
- $a_3 = 3$: $27 \cdot 8 = 216 \equiv 8 \pmod{16}$. ELIMINATED.
- **Must have $a_3 \geq 4$.**

#### Mod 32

- $1296 \equiv 16 \pmod{32}$, RHS $\equiv 16 \pmod{32}$.
- $a_3 = 4$: $27 \cdot 16 = 432 \equiv 16 \pmod{32}$. MATCHES.
- $a_3 \geq 5$: $27 \cdot 2^{a_3} \equiv 0 \pmod{32}$. LHS $\equiv 0 \neq 16$. ELIMINATED.
- **$a_3 = 4$ exactly.**

#### Mod 64

- $1296 \equiv 16 \pmod{64}$, RHS $\equiv 48 \pmod{64}$.
- With $a_3 = 4$: $432 \equiv 48 \pmod{64}$.
- $a_2 = 5$: $9 \cdot 32 = 288 \equiv 32$. LHS $\equiv 48 + 32 = 80 \equiv 16$. ELIMINATED.
- $a_2 \geq 6$: additional term $\equiv 0$. LHS $\equiv 48$. MATCHES.
- **$a_2 \geq 6$.**

#### Mod 128

- $1296 \equiv 16 \pmod{128}$, RHS $\equiv 112 \pmod{128}$.
- $a_3 = 4$: $432 \equiv 48 \pmod{128}$.
- $a_2 = 6$: $576 \equiv 64 \pmod{128}$. LHS $\equiv 48 + 64 = 112$. MATCHES.
- $a_2 \geq 7$: $\equiv 0$. LHS $\equiv 48 \neq 112$. ELIMINATED.
- **$a_2 = 6$ exactly.**

#### Reduced Equation

With $a_3 = 4$, $a_2 = 6$ fixed:

$$2^{a_0} + 3 \cdot 2^{a_1} = 5 \cdot 2^p - 2304$$

#### Mod 256

- $2304 \equiv 0 \pmod{256}$, RHS $\equiv 0$.
- $a_1 = 7$: $3 \cdot 128 = 384 \equiv 128$. ELIMINATED.
- **$a_1 \geq 8$.**

#### Mod 512

- $2304 \equiv 256 \pmod{512}$, RHS $\equiv 256$.
- $a_1 = 8$: $3 \cdot 256 = 768 \equiv 256$. MATCHES.
- $a_1 \geq 9$: $\equiv 0 \neq 256$. ELIMINATED.
- **$a_1 = 8$ exactly.**

### Step 3: Final Equation

With $a_3 = 4$, $a_2 = 6$, $a_1 = 8$:

$$2^{a_0} = 5 \cdot 2^p - 3072 = 5 \cdot 2^p - 3 \cdot 2^{10}$$

Constraints: $a_0 \geq 9$, $a_0 \leq p - 1$.

### Step 4: Case Analysis

**For $p \leq 9$:** $5 \cdot 2^p - 3072 \leq 5 \cdot 512 - 3072 = -512 < 0$. Impossible.

**For $p = 10$:** $5 \cdot 1024 - 3072 = 2048 = 2^{11}$. So $a_0 = 11$. But $a_0 \leq p - 1 = 9$. Contradiction.

**For $p = 11$:** $5 \cdot 2048 - 3072 = 7168 = 7 \cdot 1024$. Not a power of 2 (since 7 is odd and $\neq 1$).

**For $p \geq 12$:** Factor out $2^{10}$:

$$2^{a_0} = 2^{10}(5 \cdot 2^{p-10} - 3)$$

So $a_0 \geq 10$ and $2^{a_0 - 10} = 5 \cdot 2^{p-10} - 3$.

The RHS must be a power of 2: $5 \cdot 2^{p-10} - 3 = 2^m$.

Rearranging: $5 \cdot 2^{p-10} = 2^m + 3$.

For $p \geq 12$: $p - 10 \geq 2$, so LHS $\equiv 0 \pmod{4}$.

For $m \geq 2$: $2^m + 3 \equiv 3 \pmod{4}$. Contradiction.

For $m = 1$: $2^m + 3 = 5$, giving $p = 10$. Contradicts $p \geq 12$.

For $m = 0$: $2^m + 3 = 4$, giving $5 \cdot 2^{p-10} = 4$. Impossible (LHS divisible by 5, RHS is not).

**No solution exists for any $p$. $\blacksquare$**

---

## Summary Table: Modular Cascade

| Modulus | Constraint Derived | Effect |
|---------|-------------------|--------|
| 8       | $a_3 \geq 3$     | Eliminates $a_3 \in \{1, 2\}$ |
| 16      | $a_3 \geq 4$     | Eliminates $a_3 = 3$ |
| 32      | $a_3 = 4$        | Pins $a_3$ exactly |
| 64      | $a_2 \geq 6$     | Eliminates $a_2 = 5$ |
| 128     | $a_2 = 6$        | Pins $a_2$ exactly |
| 256     | $a_1 \geq 8$     | Eliminates $a_1 = 7$ |
| 512     | $a_1 = 8$        | Pins $a_1$ exactly |

After pinning $(a_3, a_2, a_1) = (4, 6, 8)$, the residual equation $2^{a_0} = 5 \cdot 2^p - 3 \cdot 2^{10}$ has no solution due to a mod 4 obstruction for $p \geq 12$, and explicit case checks for $p \leq 11$.

## Computational Verification

Exhaustive brute-force search over $p \in [8, 40]$ with all valid $(a_0, a_1, a_2, a_3)$ confirms: **zero solutions**.

Script: `solve_k5.py`
