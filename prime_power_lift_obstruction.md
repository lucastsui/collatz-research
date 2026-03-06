# Prime-Power Lift of the Equidistribution Machinery

*Date: 2026-03-06*

## Goal

Try to replace the squarefree sieve factor `rad(D)` by the full modulus

$$
D = \prod_i q_i^{e_i}
$$

by lifting the block-decomposition / Gauss-sum argument from squarefree moduli
to prime powers.

The outcome is mixed:

1. The naive prime-power lift is false.
2. A corrected local prime-power theorem looks viable.
3. Even if that local theorem is proved, the same block method still cannot
   reach the exponential-size mixed moduli needed to turn `rad(D)` into `D`.

So the local prime-power problem is not the main obstruction. The global
block-size barrier is.

---

## 1. The first obstruction: nonzero Fourier modes need not be units

In the squarefree proof for composite moduli, Step 4 implicitly treats every
nonzero Fourier frequency `t mod M` as if it were invertible mod `M`.
That is harmless for prime moduli, but false for composite moduli and much
more false for prime powers.

For `M = q^e`, define

$$
H_e := \langle 2 \rangle \subset (\mathbf Z/q^e \mathbf Z)^\times,
\qquad
A_e(c) := \sum_{h \in H_e} e\!\left(\frac{c h}{q^e}\right),
\qquad
e(x) := e^{2 \pi i x}.
$$

The squarefree heuristic would suggest a bound of shape

$$
|A_e(c)| \ll q^{e/2}
$$

for all `c not congruent 0 mod q^e`. This is false.

### Counterexample

Take `q = 5`, `e = 3`, so `M = 125`.
Then `ord_{125}(2) = 100`, hence `|H_3| = 100`.
For `c = 25` one gets

$$
A_3(25)
= \sum_{h \in H_3} e\!\left(\frac{25 h}{125}\right)
= \sum_{h \in H_3} e\!\left(\frac{h}{5}\right).
$$

Reduction mod `5` maps `H_3` onto `H_1 = (\mathbf Z/5\mathbf Z)^\times`,
each residue with multiplicity `100 / 4 = 25`. Therefore

$$
A_3(25)
= 25 \sum_{u \in (\mathbf Z/5\mathbf Z)^\times} e\!\left(\frac{u}{5}\right)
= 25(-1),
$$

so

$$
|A_3(25)| = 25 > \sqrt{125}.
$$

Thus the naive `sqrt(q^e)` bound fails already for `(q,e,c) = (5,3,25)`.

The same phenomenon appears systematically when `c` has large `q`-adic
valuation: the additive character drops to a lower conductor and the subgroup
sum acquires a multiplicity factor from the kernel of reduction.

---

## 2. Corrected local structure: reduction to the true conductor

The failure above is not random; it has an exact formula.

For `0 <= a < e`, write

$$
c = q^a u,
\qquad
(u,q)=1,
\qquad
m := e-a.
$$

Let

$$
d_r := |H_r| = \operatorname{ord}_{q^r}(2).
$$

### Proposition 1 (exact conductor reduction)

For `c = q^a u` as above,

$$
A_e(c) = \frac{d_e}{d_m} A_m(u).
$$

#### Proof

The additive character depends only on `h mod q^m`:

$$
e\!\left(\frac{c h}{q^e}\right)
= e\!\left(\frac{u h}{q^m}\right).
$$

Reduction mod `q^m` gives a homomorphism

$$
H_e \to H_m,
$$

whose fibers all have size `d_e / d_m`. Summing fiberwise gives the formula.

So every nonprimitive Fourier mode for `q^e` is exactly a lower-conductor mode
times a multiplicity factor.

---

## 3. Corrected Gauss bound at unit conductor

What remains is to bound `A_m(u)` for `(u,q)=1`.

For odd prime powers, the multiplicative group

$$
G_m := (\mathbf Z/q^m \mathbf Z)^\times
$$

is cyclic of order `phi(q^m) = q^{m-1}(q-1)`.
Expand the indicator of `H_m` in multiplicative characters:

$$
1_{H_m}(x)
= \frac{d_m}{\varphi(q^m)}
   \sum_{\chi : \chi|_{H_m}=1} \chi(x).
$$

Hence

$$
A_m(u)
= \frac{d_m}{\varphi(q^m)}
   \sum_{\chi : \chi|_{H_m}=1} \tau_m(\chi,u),
$$

where

$$
\tau_m(\chi,u)
:=
\sum_{x \in G_m} \chi(x) e\!\left(\frac{u x}{q^m}\right).
$$

For `u` a unit mod `q^m`, standard Gauss-sum theory gives:

- if `chi` is primitive mod `q^m`, then `|tau_m(chi,u)| = q^{m/2}`;
- if `chi` is nonprincipal and imprimitive mod `q^m`, then `tau_m(chi,u) = 0`;
- for the principal character, `tau_m(chi_0,u)` is a Ramanujan sum, so
  `|tau_m(chi_0,u)| <= 1 <= q^{m/2}`.

Therefore:

### Proposition 2 (unit-frequency bound)

For `(u,q)=1`,

$$
|A_m(u)| \le q^{m/2}.
$$

#### Proof

Primitive characters contribute size exactly `q^{m/2}`; the principal
character contributes at most `1`; and every other imprimitive character
contributes `0`. There are at most `phi(q^m) / d_m` characters trivial on
`H_m`, so

$$
|A_m(u)|
\le
\frac{d_m}{\varphi(q^m)}
\cdot
\frac{\varphi(q^m)}{d_m}
\cdot q^{m/2}
= q^{m/2}.
$$

Combining Propositions 1 and 2 gives:

### Corollary 3

If `v_q(c)=a` and `m=e-a`, then

$$
|A_e(c)| \le \frac{d_e}{d_m} q^{m/2},
\qquad
\frac{|A_e(c)|}{d_e} \le \frac{q^{m/2}}{d_m}.
$$

So the normalized loss for a `q^e`-Fourier mode is controlled by the order of
`2` at the true conductor `q^m`, not at the ambient modulus `q^e`.

---

## 4. Proof attempt: fixed prime-power equidistribution

This suggests the following corrected local theorem.

### Theorem candidate

Fix an odd prime power `q^e` with `q >= 5` and `gcd(q,6)=1`.
Assume

$$
d_m = \operatorname{ord}_{q^m}(2) > q^{m/2}
\qquad
\text{for every } 1 \le m \le e.
$$

Then the block-decomposition argument proving Theorem 4 should extend to
modulus `q^e` and give

$$
\left| \mathbf P(S \equiv 0 \bmod q^e) - \frac{1}{q^e} \right|
\le C_{q,e} e^{-c_{q,e} p}.
$$

### Sketch

For a fixed occupancy pattern, the block factor with one selected index is

$$
B_{q^e}(s,1;t)
=
\sum_{j=0}^{d_e-1}
e\!\left(\frac{t \, 3^{k-s-1} 2^j}{q^e}\right).
$$

If the Fourier frequency `t` has `q`-adic valuation `a`, then by Corollary 3
the normalized block factor satisfies

$$
\frac{|B_{q^e}(s,1;t)|}{d_e}
\le
\frac{q^{m/2}}{d_m}
\le
\rho_{q,e}
< 1,
\qquad
m=e-a,
$$

where

$$
\rho_{q,e} := \max_{1 \le m \le e} \frac{q^{m/2}}{d_m}.
$$

Once `rho_{q,e} < 1`, the rest of the proof is the same as for prime moduli:
blocks with one selected element occur with positive density, and concentration
of the occupancy profile gives exponential decay in `p`.

### What this does achieve

It gives a plausible local replacement of the squarefree factor `1/q`
by the prime-power factor `1/q^e`.

### Numerical support

Exact DP counts for small `(p,k)` already look compatible with this.
For example:

- `(p,k)=(15,9)`, mod `125`: count at residue `0` is `41`, expectation is
  `5005 / 125 = 40.04`;
- `(p,k)=(18,11)`, mod `125`: count at residue `0` is `256`, expectation is
  `31824 / 125 = 254.592`;
- `(p,k)=(18,11)`, mod `121`: count at residue `0` is `267`, expectation is
  `31824 / 121 = 263.008`.

This does not prove the theorem, but it supports the corrected local picture.

---

## 5. What the remaining obstruction actually is

The local prime-power theorem above does not automatically replace `rad(D)` by
`D`, but the reason is narrower than "one must prove equidistribution at the
full modulus `D`."

Write

$$
D = \prod_i q_i^{e_i}.
$$

By CRT, for each parity pattern `I` one has the exact event identity

$$
D \mid S(I)
\iff
q_i^{e_i} \mid S(I) \text{ for every } i.
$$

What CRT does **not** give, by itself, is exact factorization of
probabilities:

$$
\mathbf P(D \mid S)
=
\mathbf P\!\left(\bigcap_i \{q_i^{e_i} \mid S\}\right),
$$

not automatically

$$
\prod_i \mathbf P(q_i^{e_i} \mid S).
$$

So some independence / sieve input is still needed. But once a local theorem is
available for each prime power, that combination problem is conceptually much
less severe than asking for block decomposition directly at modulus `D`.

The real remaining difficulty is this:

### Large individual prime powers can be unhandleable

The local prime-power proof for modulus `q^e` uses blocks of length

$$
d_{q^e} := \operatorname{ord}_{q^e}(2).
$$

To get any complete blocks at all, one needs

$$
d_{q^e} \le p.
$$

If a prime factor `q^e || D` has

$$
\operatorname{ord}_{q^e}(2) > p,
$$

then the block method gives zero complete blocks for that individual modulus,
so the local equidistribution theorem does not apply there.

This is already possible for a single large prime factor `q | D` with `q > p`.
In that case `ord_q(2)` can easily exceed `p`, and the obstruction appears
before any issue of combining different moduli.

### The arithmetic subproblem

Suppose one proves the local prime-power theorem for every **handleable** prime
power divisor `q^e || D`, meaning those with `ord_{q^e}(2) <= p` and
`ord_{q^m}(2) > q^{m/2}` for all `m <= e`.

Then the remaining question is:

> Does the product of the handleable prime powers dividing `D` already exceed
> the combinatorial count `\binom{p}{k} \asymp 2^{0.949p}`?

Equivalently, can one show that the complementary **unhandleable part**

$$
D_{\mathrm{bad}}
:=
\prod_{q^e \parallel D \,:\, \operatorname{ord}_{q^e}(2) > p} q^e
$$

is always too small to matter?

That is a specific arithmetic question about the factorization of

$$
D = 2^p - 3^k,
$$

and it is weaker than a full `abc`-strength statement on `rad(D)`. It isolates
the real obstruction at the current level of the method: not the CRT
combination itself, but the possible presence of large prime powers whose order
modulus is too large for the block decomposition to see.

### Revised conclusion

Lifting from squarefree moduli to prime powers still matters. It repairs the
local density from `1/q` to `1/q^e` for every handleable prime power. What it
does **not** settle is whether enough of `D` is made from such handleable prime
powers to push the solution count below `1`.

---

## 6. Bottom line

There is a real local theorem to prove:

- prime-power equidistribution mod fixed `q^e` looks viable, after correcting
  for nonprimitive Fourier modes by reducing to their true conductor.

But there is also a real global obstruction:

- one must control the portion of `D` coming from prime powers `q^e` with
  `\operatorname{ord}_{q^e}(2) > p`, since those are invisible to the current
  block method.

So the research target should be separated into two distinct tasks:

1. **Local task:** prove the fixed-`q^e` theorem above cleanly.
2. **Global task:** prove that the product of the locally handleable prime
   powers dividing `D` is already large enough, or else develop a different
   method for the unhandleable prime powers.

Without (2), prime-power lifting improves the local story but does not close
the Collatz counting argument.
