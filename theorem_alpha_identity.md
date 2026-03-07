# Theorem: The Alpha Identity

*Proved 2026-03-06 (Session 8)*

## Statement

**Theorem.** Let $n \geq 1$ be odd, and suppose the Syracuse orbit of $n$ reaches 1 in $t$ steps: $n = n_0, n_1 = S(n_0), \ldots, n_t = 1$, with halvings $h_m = v_2(3n_m + 1)$ and total halvings $A = \sum_{m=0}^{t-1} h_m$.

Define the cascade walk: $w_0 = 1$, $w_m = 3 w_{m-1} + 2^{A_m}$ where $A_m = \sum_{i=0}^{m-1} h_i$.

Then:
$$w_t = 4 \cdot 2^A - 3^{t+1} \cdot n$$

Equivalently: $\alpha := w_t - 4 \cdot 2^A = -3^{t+1} \cdot n$.

## Proof

Define $S = 3^t(3n + 1) + \sum_{i=1}^{t} 3^{t-i} \cdot 2^{A_i}$.

**Claim:** $S = 4 \cdot 2^A$.

*Proof of claim by telescoping.* At each step, use $3n_m + 1 = n_{m+1} \cdot 2^{h_m}$:

- $S = 3^t \cdot n_1 \cdot 2^{A_1} + \sum_{i=1}^{t} 3^{t-i} \cdot 2^{A_i}$
- $= 3^{t-1} \cdot 2^{A_1} \cdot (3n_1 + 1) + \sum_{i=2}^{t} 3^{t-i} \cdot 2^{A_i}$
- $= 3^{t-1} \cdot n_2 \cdot 2^{A_2} + \sum_{i=2}^{t} 3^{t-i} \cdot 2^{A_i}$
- Continue peeling: at step $j$, obtain $3^{t-j} \cdot n_{j+1} \cdot 2^{A_{j+1}} + \sum_{i=j+1}^{t} 3^{t-i} \cdot 2^{A_i}$
- At step $t-1$: $3^1 \cdot n_t \cdot 2^{A_t} + 3^0 \cdot 2^{A_t} = 3 \cdot 2^A + 2^A = 4 \cdot 2^A$. $\square$

But also: $S = 3^t(3n+1) + \sum_{i=1}^{t} 3^{t-i} \cdot 2^{A_i} = 3^{t+1} n + 3^t + \sum_{i=1}^{t} 3^{t-i} \cdot 2^{A_i} = 3^{t+1} n + w_t$.

Therefore: $w_t + 3^{t+1} n = 4 \cdot 2^A$, giving $w_t - 4 \cdot 2^A = -3^{t+1} n$. $\square$

## Consequence for Collatz No-Cycles

For $k > t$: the cascade walk continues with periodic halvings $h = 2$ (since the orbit has reached 1). The pinned sum becomes:

$$\text{ps}(k) = \alpha \cdot 3^{k-1-t} + 2^{A+2} \cdot 4^{k-1-t}$$

Since $\alpha = -3^{t+1} n$:

$$\text{ps}(k) \equiv 2^{A+2} \cdot 4^{k-1-t} \pmod{n}$$

This is **always nonzero** mod $n$ (since $n$ is odd, $\gcd(2^{A+2}, n) = 1$, and $4^{k-1-t}$ is a unit mod $n$).

**Therefore:** For any $n$ that reaches 1 under Syracuse, and for any $k > t$: $\text{ps}(k) \not\equiv 0 \pmod{n}$. Since $\text{ps}(k) = 0 \bmod n$ is necessary for a cycle of length $k$ with starting value $n$, no such cycle exists.

Combined with the Steiner bound ($n < (3/2)^{k-1}$) and computational Collatz verification (all $n < 2^{68}$ reach 1):

**No nontrivial Collatz cycle exists with $n < 2^{68}$.**

## Significance

The identity $\alpha = -3^{t+1} n$ is the precise algebraic content of the "self-referentiality" of the Collatz cycle equation. It says: the cascade-pinned sum and the power-of-2 reference differ by exactly $3^{t+1}$ times the starting value $n$. The factor of $n$ in $\alpha$ is what prevents $n$ from dividing the pinned sum — the starting value "knows" about itself through the cascade structure.

This reduces the Collatz no-cycles problem to the Collatz convergence problem: if every $n < N$ reaches 1, then no cycle with starting value $< N$ exists.
