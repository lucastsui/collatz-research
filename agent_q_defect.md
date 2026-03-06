# The q-Certificate Defect Identity

*Analysis by Codex -- 2026-03-06*

## 0. Executive Summary

This note does not prove that the `q`-certificate constraints are inconsistent.
What it does give is an exact identity that isolates where the near-critical
slack

$$
\Delta := p \log 2 - k \log 3 = \log\!\left(\frac{2^p}{3^k}\right) > 0
$$

actually lives.

Assume there is a strictly negative integer sequence

$$
q_0,\dots,q_{p-1}
$$

with

$$
q_{r-1} - 2 q_r = \varepsilon_r 3^{s_{r+1}},
\qquad
q_{-1} := -n 3^k,
$$

where $\varepsilon_r = 1_{r \in I}$, $s_r = \sum_{t=r}^{p-1} \varepsilon_t$, and

$$
3^{s_{r+1}} \mid q_r
\qquad
(0 \le r \le p-1).
$$

Then after normalization

$$
u_0 := n,
\qquad
u_{r+1} := -\frac{q_r}{3^{s_{r+1}}},
$$

the sequence $u_0,\dots,u_p=u_0$ is a genuine positive integer period-$p$
orbit of the compressed Collatz map with parity pattern $\varepsilon$:

$$
u_{r+1} =
\begin{cases}
u_r/2 & \varepsilon_r = 0, \\
(3u_r+1)/2 & \varepsilon_r = 1.
\end{cases}
$$

The main new point is the exact defect variable

$$
E_r := \Delta_r + \log\!\left(\frac{u_r}{n}\right),
\qquad
\Delta_r := r \log 2 - t_r \log 3,
\qquad
t_r := \sum_{j=0}^{r-1} \varepsilon_j.
$$

It satisfies:

1. `Band constraint`:
   $$
   0 \le E_r \le \Delta
   \qquad
   (0 \le r \le p).
   $$

2. `Exact evolution`:
   $$
   E_{r+1} - E_r =
   \begin{cases}
   0 & \varepsilon_r = 0, \\
   \log\!\left(1 + \frac{1}{3u_r}\right) & \varepsilon_r = 1.
   \end{cases}
   $$

3. `Telescoping identity`:
   $$
   \Delta
   =
   \sum_{r \in I} \log\!\left(1 + \frac{1}{3u_r}\right).
   $$

So the entire failure of exact criticality is concentrated in tiny positive
jumps at the odd steps, and nowhere else.

This gives a concrete Target C reformulation:

> To rule out the `q`-certificate, it is enough to show that no positive
> period-$p$ orbit can decompose $\Delta$ into the special atoms
> $\log(1 + 1/(3u_r))$ coming from its odd values.

---

## 1. From the q-Certificate to a Genuine Collatz Orbit

Define

$$
u_0 := n,
\qquad
u_{r+1} := -\frac{q_r}{3^{s_{r+1}}}
\qquad
(0 \le r \le p-1).
$$

Because $q_r < 0$ and $3^{s_{r+1}} \mid q_r$, every $u_r$ is a positive
integer.

Substitute

$$
q_{r-1} = -3^{s_r} u_r,
\qquad
q_r = -3^{s_{r+1}} u_{r+1},
\qquad
s_r = \varepsilon_r + s_{r+1}
$$

into

$$
q_{r-1} - 2 q_r = \varepsilon_r 3^{s_{r+1}}.
$$

This gives

$$
-3^{s_r} u_r + 2 \cdot 3^{s_{r+1}} u_{r+1}
=
\varepsilon_r 3^{s_{r+1}},
$$

hence

$$
2u_{r+1} = 3^{\varepsilon_r} u_r + \varepsilon_r.
$$

So:

$$
u_{r+1} =
\begin{cases}
u_r/2 & \varepsilon_r = 0, \\
(3u_r+1)/2 & \varepsilon_r = 1.
\end{cases}
$$

In particular, parity is automatic:

$$
\varepsilon_r = 0 \Rightarrow u_r \equiv 0 \pmod 2,
\qquad
\varepsilon_r = 1 \Rightarrow u_r \equiv 1 \pmod 2.
$$

Also $q_{p-1} = -n$, so $u_p = n = u_0$.

Therefore the full feasibility problem for `(a)+(b)+(c)` is exactly the
existence of a genuine positive integer period-$p$ Collatz orbit.

---

## 2. A Monotone Scaled q-Sequence

Define the scaled variables

$$
x_r := -\frac{q_r}{2^{p-1-r}}
\qquad
(0 \le r \le p-1),
$$

and also

$$
x_{-1} := \frac{n3^k}{2^p}.
$$

Divide the recurrence by $2^{p-r}$:

$$
\frac{-q_{r-1}}{2^{p-r}}
=
\frac{-q_r}{2^{p-1-r}}
-
\varepsilon_r \frac{3^{s_{r+1}}}{2^{p-r}}.
$$

So

$$
x_{r-1}
=
x_r - \varepsilon_r \frac{3^{s_{r+1}}}{2^{p-r}}.
$$

Hence

$$
x_{-1} \le x_r \le x_{p-1},
$$

that is,

$$
\frac{n3^k}{2^p} \le x_r \le n.
$$

Now use

$$
u_{r+1}
=
\frac{-q_r}{3^{s_{r+1}}}
=
x_r \frac{2^{p-1-r}}{3^{s_{r+1}}}.
$$

Since $s_{r+1} = k - t_{r+1}$, we obtain:

### Proposition 2.1

For every $0 \le r \le p$,

$$
n \frac{3^{t_r}}{2^r}
\le
u_r
\le
n \frac{2^{p-r}}{3^{k-t_r}}.
$$

Equivalently,

$$
n e^{-\Delta_r}
\le
u_r
\le
n e^{\Delta - \Delta_r}.
$$

This is an exact global consequence of the `q`-recurrence. No prime
factorization of $D$ appears.

---

## 3. The Defect Variable

Define

$$
E_r := \Delta_r + \log\!\left(\frac{u_r}{n}\right).
$$

By Proposition 2.1:

### Corollary 3.1

For all $0 \le r \le p$,

$$
0 \le E_r \le \Delta.
$$

So the entire orbit stays inside a logarithmic strip of width exactly
$\Delta = \log(2^p/3^k)$.

Now compute its stepwise evolution.

If $\varepsilon_r = 0$, then

$$
\Delta_{r+1} - \Delta_r = \log 2,
\qquad
\log\!\left(\frac{u_{r+1}}{u_r}\right) = -\log 2,
$$

so

$$
E_{r+1} - E_r = 0.
$$

If $\varepsilon_r = 1$, then

$$
\Delta_{r+1} - \Delta_r = \log 2 - \log 3,
$$

and

$$
\log\!\left(\frac{u_{r+1}}{u_r}\right)
=
\log\!\left(\frac{3u_r+1}{2u_r}\right),
$$

so

$$
E_{r+1} - E_r
=
\log 2 - \log 3 + \log\!\left(\frac{3u_r+1}{2u_r}\right)
=
\log\!\left(1 + \frac{1}{3u_r}\right).
$$

Therefore:

### Theorem 3.2 (Exact Defect Evolution)

For every $0 \le r \le p-1$,

$$
E_{r+1} - E_r =
\begin{cases}
0 & \varepsilon_r = 0, \\
\log\!\left(1 + \frac{1}{3u_r}\right) & \varepsilon_r = 1.
\end{cases}
$$

In particular, $E_r$ is monotone nondecreasing, constant on even steps, and
gains all of its mass at odd steps.

Since $E_0 = 0$ and $E_p = \Delta$, we get:

### Corollary 3.3 (Defect Identity)

$$
\Delta
=
\sum_{r \in I} \log\!\left(1 + \frac{1}{3u_r}\right).
$$

If $y_1,\dots,y_k$ are the odd values in one period, this is

$$
\Delta
=
\sum_{j=1}^k \log\!\left(1 + \frac{1}{3y_j}\right).
$$

This is the cleanest exact formula I know for where the near-critical slack is
stored.

---

## 4. Immediate Consequences

### Corollary 4.1 (Uniform Lower Bound for Odd Values)

For every odd position $r \in I$,

$$
\log\!\left(1 + \frac{1}{3u_r}\right) \le \Delta,
$$

hence

$$
u_r \ge \frac{1}{3(e^\Delta - 1)}.
$$

So if

$$
\left|\frac{k}{p} - \frac{\log 2}{\log 3}\right| \le C p^{-10},
$$

then

$$
\Delta = p \log 2 - k \log 3 = O(p^{-9}),
$$

and every odd value satisfies

$$
u_r \gg p^9.
$$

This holds uniformly over the whole period.

### Corollary 4.2 (Harmonic-Mean Form)

Using $\log(1+x) \le x$,

$$
\Delta
\le
\frac13 \sum_{r \in I} \frac{1}{u_r}.
$$

So any independent lower bound on the reciprocal sum of the odd values would
immediately force a lower bound on $\Delta$.

This is a plausible attack point: near-resonant cycles would require the odd
values to be so large that their reciprocal mass drops to $O(\Delta)$.

### Corollary 4.3 (Almost-Multiplicative Rigidity)

For every $r$ there exists $\theta_r \in [0,\Delta]$ such that

$$
u_r = n \exp(-\Delta_r + \theta_r).
$$

So the orbit value at time $r$ is determined by the prefix discrepancy

$$
\Delta_r = r \log 2 - t_r \log 3
$$

up to a multiplicative factor in $[1,e^\Delta]$.

When $\Delta$ is tiny, the whole orbit is pinned very close to the purely
multiplicative model $n 3^{t_r}/2^r$.

---

## 5. Assessment

This does not yet prove inconsistency of the `q`-certificate.

But it clarifies the exact shape of any possible counterexample:

1. The `q`-problem is not merely a lattice-feasibility problem. Under the full
   divisibility constraints it is exactly a genuine Collatz cycle.
2. The deviation from the critical multiplier $3^k/2^p = 1$ is encoded by a
   monotone defect process $E_r$ that only jumps at odd steps.
3. The total defect is
   $$
   \Delta = \sum_{r \in I} \log\!\left(1 + \frac{1}{3u_r}\right),
   $$
   so near-resonant cycles force every odd value to be uniformly large.

What would be needed next is an independent argument showing that a nontrivial
periodic orbit cannot have odd values large enough, or reciprocals sparse
enough, to realize this decomposition of $\Delta$.

That is a concrete reformulation of the open subtask.
