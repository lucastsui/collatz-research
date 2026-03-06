# Global Lattice Reformulation of Structured Divisibility

*Analysis by Codex -- 2026-03-06*

## 0. Executive Summary

This note records an exact reformulation of

$$
D \mid S(I), \qquad D = a^p - b^k, \qquad S(I) = \sum_{j=1}^k b^{k-j} a^{i_j},
$$

that is global in the modulus $D$ and does not factor $D$ into primes.

Let

$$
F_I(x) := \sum_{j=1}^k b^{k-j} x^{i_j} = \sum_{r=0}^{p-1} c_r x^r,
$$

where $c_r = 0$ unless $r \in I$, and if $r = i_j$ then $c_r = b^{k-j}$.

The main point is:

1. In the rank-$p$ order
   $$
   R := \mathbf{Z}[x]/(x^p - b^k),
   $$
   the divisibility condition is exactly
   $$
   [F_I(x)] \in (x-a)R.
   $$

2. Equivalently, the coefficient vector $c = (c_0,\dots,c_{p-1})^T$ lies in an explicit index-$D$ lattice
   $$
   M_{a,b,p,k}\,\mathbf{Z}^p \subset \mathbf{Z}^p,
   $$
   where $M_{a,b,p,k}$ is a companion-type matrix with determinant $\pm D$.

3. In the Collatz case $(a,b) = (2,3)$, the unique lattice witness $q$ normalizes exactly to the forced branch values:
   $$
   u_{r+1} =
   \begin{cases}
   u_r/2 & r \notin I, \\
   (3u_r+1)/2 & r \in I,
   \end{cases}
   \qquad u_p = u_0.
   $$

So the branch fixed-point equation can be viewed as membership of a sparse geometric vector in one fixed covolume-$D$ lattice, together with a rigid sign/divisibility pattern on the certificate vector.

This does not prove non-divisibility. It is an exact global reformulation native at the scale of $D$.

---

## 1. Setup

Write the indicator of the subset $I$ as

$$
\varepsilon_r := 1_{r \in I}, \qquad 0 \le r \le p-1.
$$

Let

$$
s_r := \sum_{t=r}^{p-1} \varepsilon_t = \#(I \cap \{r,r+1,\dots,p-1\}),
$$

so $s_0 = k$ and $s_p = 0$.

Then the coefficient of $x^r$ in $F_I(x)$ is

$$
c_r = \varepsilon_r\, b^{s_{r+1}}.
$$

Indeed, if $r = i_j$, then the number of selected positions strictly larger than $r$ is $k-j$, so $c_r = b^{k-j} = b^{s_{r+1}}$.

Thus

$$
F_I(x) = \sum_{r=0}^{p-1} \varepsilon_r\, b^{s_{r+1}} x^r.
$$

---

## 2. Exact Ideal-Membership Reformulation

### Theorem 2.1

Let

$$
D = a^p - b^k \ne 0,
\qquad
R = \mathbf{Z}[x]/(x^p - b^k).
$$

For any polynomial $F(x) \in \mathbf{Z}[x]$ with $\deg F < p$, the following are equivalent:

1. $D \mid F(a)$.
2. $F(x) \in (x-a,\;x^p-b^k)$ as an ideal of $\mathbf{Z}[x]$.
3. The class $[F(x)] \in R$ lies in the principal ideal $(x-a)R$.

### Proof

Consider the ring homomorphism

$$
\phi_a : \mathbf{Z}[x] \to \mathbf{Z}/D\mathbf{Z},
\qquad
x \mapsto a \pmod D.
$$

Then

$$
D \mid F(a) \iff \phi_a(F) = 0 \iff F \in \ker \phi_a.
$$

But $\ker \phi_a = (x-a, D)$, since modding out by $(x-a,D)$ forces $x=a$ and then reduces constants mod $D$.

Now

$$
x^p - b^k = (x^p - a^p) + (a^p - b^k)
        = (x-a)\sum_{m=0}^{p-1} a^{p-1-m}x^m + D,
$$

so $x^p - b^k \in (x-a, D)$. Conversely,

$$
D = (x^p - b^k) - (x-a)\sum_{m=0}^{p-1} a^{p-1-m}x^m
$$

lies in $(x-a, x^p-b^k)$. Hence

$$
(x-a, D) = (x-a, x^p-b^k).
$$

This proves $(1) \iff (2)$.

Passing to the quotient $R = \mathbf{Z}[x]/(x^p-b^k)$ turns $(x-a, x^p-b^k)$ into $(x-a)R$, so $(2) \iff (3)$.  QED.

### Corollary 2.2

There is a canonical isomorphism

$$
R/(x-a)R \cong \mathbf{Z}/D\mathbf{Z}.
$$

In particular, the ideal $(x-a)R$ has index $|D|$ inside the rank-$p$ lattice $R \cong \mathbf{Z}^p$.

This is already a genuinely global reformulation: no prime decomposition of $D$ appears anywhere.

---

## 3. Companion Matrix and the Index-$D$ Lattice

Take the standard $\mathbf{Z}$-basis $1,x,\dots,x^{p-1}$ of $R$.

Let

$$
Q(x) = q_0 + q_1 x + \cdots + q_{p-1}x^{p-1}.
$$

In $R$ we have

$$
(x-a)Q(x) \equiv
(-a q_0 + b^k q_{p-1})
+ \sum_{r=1}^{p-1} (q_{r-1} - a q_r)x^r.
$$

Therefore the matrix of multiplication by $(x-a)$ on this basis is

$$
M_{a,b,p,k} =
\begin{pmatrix}
-a & 0 & 0 & \cdots & 0 & b^k \\
1  & -a & 0 & \cdots & 0 & 0 \\
0  & 1  & -a & \cdots & 0 & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
0 & 0 & 0 & \cdots & -a & 0 \\
0 & 0 & 0 & \cdots & 1 & -a
\end{pmatrix}.
$$

If $c = (c_0,\dots,c_{p-1})^T$ is the coefficient vector of $F(x)$, then

$$
[F(x)] \in (x-a)R
\iff
\exists\, q \in \mathbf{Z}^p \text{ such that } M_{a,b,p,k} q = c.
$$

So divisibility becomes an exact lattice-membership question.

### Proposition 3.1

$$
\det M_{a,b,p,k} = (-1)^p(a^p - b^k) = (-1)^p D.
$$

### Proof

This is the norm/resultant identity

$$
\det M_{a,b,p,k}
=
N_{R/\mathbf{Z}}(x-a)
=
(-1)^p \operatorname{Res}_x(x-a,\;x^p-b^k)
=
(-1)^p(a^p-b^k).
$$

Equivalently, one can verify it by induction on $p$.  QED.

### Corollary 3.2

For any $F(x)$ of degree $< p$, the following are equivalent:

1. $D \mid F(a)$.
2. The rational linear system $M_{a,b,p,k} q = c$ has an integer solution.
3. The unique rational solution belongs to $\mathbf{Z}^p$.

Thus the divisibility problem is exactly the integrality of one explicit rank-$p$ linear solve whose determinant is $\pm D$.

---

## 4. Exact Polynomial Identity and the Certificate Sequence

Apply the previous section to $F = F_I$.

If $D \mid F_I(a)$, write

$$
n := \frac{F_I(a)}{D} \in \mathbf{Z}.
$$

Then there is a unique $Q_I(x) = \sum_{r=0}^{p-1} q_r x^r \in \mathbf{Z}[x]$ such that

$$
F_I(x) = n(x^p-b^k) + (x-a)Q_I(x),
$$

because the $x^p$-coefficient must cancel and $\deg F_I < p$.

Comparing coefficients gives the exact recurrence

$$
q_{p-1} = -n,
$$

$$
c_0 = -a q_0 - n b^k,
$$

and for $1 \le r \le p-1$,

$$
c_r = q_{r-1} - a q_r.
$$

Equivalently,

$$
q_{r-1} = a q_r + c_r \qquad (1 \le r \le p-1).
$$

This sequence $q_0,\dots,q_{p-1}$ is the unique integer certificate of divisibility.

### Proposition 4.1

For $0 \le r \le p-1$,

$$
q_r
=
-\frac{
\sum_{m=0}^{r} c_m a^{p-1-r+m}
+
b^k \sum_{m=r+1}^{p-1} c_m a^{m-r-1}
}{D}.
$$

In particular, if $D>0$ and all $c_m \ge 0$ with not all $c_m=0$, then

$$
q_r < 0 \qquad \text{for every } r.
$$

### Proof

From $q_{p-1}=-n$ and $q_{r-1}=a q_r + c_r$ for $r \ge 1$, we get

$$
q_r = -a^{p-1-r}n + \sum_{m=r+1}^{p-1} a^{m-r-1}c_m.
$$

Substitute

$$
n = \frac{F_I(a)}{D} = \frac{\sum_{m=0}^{p-1} c_m a^m}{D}
$$

and simplify. The sign claim is immediate from the displayed formula because every term in the numerator is nonnegative and at least one is positive.  QED.

### Structural Corollary 4.2

If $D \mid S(I)$, write $n=S(I)/D$ and let $q_0,\dots,q_{p-1}$ be the certificate sequence above. Define also

$$
q_{-1} := -n b^k.
$$

Then there is a unique strictly negative extended integer sequence

$$
q_{-1},q_0,\dots,q_{p-1}
$$

such that

$$
q_{r-1} - a q_r \in \{0,\; b^0,\; b^1,\;\dots,\; b^{k-1}\}
$$

for every $0 \le r \le p-1$, and the nonzero values occur exactly at the positions in $I$, in the strict order

$$
b^{k-1},\; b^{k-2},\;\dots,\;1.
$$

In the Collatz case this becomes:

$$
q_{r-1} - 2 q_r \in \{0,1,3,9,\dots,3^{k-1}\},
$$

with the nonzero differences appearing exactly at the odd-step positions, and in strictly descending powers of $3$.

This is a rigid certificate condition native at the full modulus $D$.

---

## 5. Normalization to the Forced Branch Orbit

Now specialize to the structured coefficients

$$
c_r = \varepsilon_r\, b^{s_{r+1}}.
$$

Define

$$
u_0 := n = \frac{F_I(a)}{D},
$$

and for $1 \le r \le p$,

$$
u_r := -\frac{q_{r-1}}{b^{s_r}}.
$$

Since $q_{p-1} = -n$ and $s_p = 0$, we have

$$
u_p = -q_{p-1} = n = u_0.
$$

### Theorem 5.1

For every $0 \le r \le p-1$,

$$
a u_{r+1} = b^{\varepsilon_r} u_r + \varepsilon_r.
$$

Equivalently,

$$
u_{r+1} =
\begin{cases}
u_r/a & \text{if } \varepsilon_r = 0, \\
(b u_r + 1)/a & \text{if } \varepsilon_r = 1.
\end{cases}
$$

Thus the normalized certificate sequence is exactly the period-$p$
fixed point of the affine branch composition determined by $I$.
In the Collatz case, it becomes a genuine orbit only after the extra
parity self-consistency checks are verified.

### Proof

For $1 \le r \le p-1$, substitute

$$
q_{r-1} = -b^{s_r}u_r,
\qquad
q_r = -b^{s_{r+1}}u_{r+1},
\qquad
c_r = \varepsilon_r b^{s_{r+1}}
$$

into $c_r = q_{r-1} - a q_r$:

$$
\varepsilon_r b^{s_{r+1}}
=
-b^{s_r}u_r + a b^{s_{r+1}}u_{r+1}.
$$

Since $s_r = \varepsilon_r + s_{r+1}$, divide by $b^{s_{r+1}}$ to obtain

$$
\varepsilon_r = -b^{\varepsilon_r}u_r + a u_{r+1},
$$

which rearranges to

$$
a u_{r+1} = b^{\varepsilon_r}u_r + \varepsilon_r.
$$

For $r=0$, the same calculation uses the constant-term identity

$$
c_0 = -a q_0 - n b^k
$$

and $s_0 = k = \varepsilon_0 + s_1$, giving the same formula.  QED.

### Interpretation

The certificate vector $q$ is not an arbitrary lattice witness.
After dividing by the exact remaining power of $b$, it becomes the forced branch fixed point attached to $I$.

So the divisibility problem can be read in two equivalent coordinates:

1. A linear index-$D$ lattice-membership problem in rank $p$.
2. The nonlinear branch-fixed-point equation for the compressed map.

This recovers the known equivalence with the branch cycle equation, but now from a single global linear algebra package.

---

## 6. Norm and Resultant Viewpoint

The core object here is the principal ideal $(x-a)R \subset R$.

Its index is

$$
[R : (x-a)R] = |N_{R/\mathbf{Z}}(x-a)| = |a^p - b^k| = |D|.
$$

Equivalently,

$$
N_{R/\mathbf{Z}}(x-a) = (-1)^p \operatorname{Res}_x(x-a,\;x^p-b^k).
$$

So the conjecture may be restated as:

> No coefficient vector coming from a structured geometric pattern $I$
> lies in the index-$D$ sublattice $(x-a)R$ once $k/p \approx \log a / \log b$
> and $p$ is large.

This is genuinely "native at scale $D$": the modulus appears as a single lattice covolume, not as a product of local prime conditions.

---

## 7. Honest Assessment

This note does **not** bypass the main barrier by itself. It is an exact reformulation, not a proof.

What it gives:

1. A global, non-sieved model of the problem:
   $$
   c_I \in M_{a,b,p,k}\mathbf{Z}^p,
   \qquad
   |\det M_{a,b,p,k}| = D.
   $$

2. A rigid certificate sequence $q$ with three simultaneous properties:
   - strict negativity,
   - sparse geometric differences $q_{r-1} - a q_r$,
   - exact divisibility by the trailing powers $b^{s_r}$.

3. An exact bridge between the linear algebra and the forced dynamics:
   after normalization, the certificate sequence is the branch-fixed-point sequence attached to $I$.

Why this might still matter:

The lattice here is not generic. The target vectors are also not generic.
The vector $c_I$ has one nonzero per selected position, and those nonzero entries are forced to be

$$
b^{k-1}, b^{k-2}, \dots, 1
$$

in rank order. Simultaneously, the witness vector $q$ must satisfy sign and trailing-$b$ divisibility conditions that are far stronger than ordinary lattice membership.

So a plausible Target C program is:

1. treat $D \mid S(I)$ as the existence of a negative integer certificate $q$;
2. exploit the exact pattern
   $$
   q_{r-1} - a q_r = \varepsilon_r b^{s_{r+1}};
   $$
3. prove that no such certificate can exist when $k/p$ is near $\log a / \log b$.

At present I do not see such a contradiction, but this is the cleanest exact global formulation I know that stays at modulus scale $D$ and does not decompose $D$ into primes.
