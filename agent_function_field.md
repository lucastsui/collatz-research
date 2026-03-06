# Function-Field Lift for the Collatz No-Cycles Problem

*Analysis by Claude Opus 4.6 — 2026-03-06*

---

## 1. Setup and Notation

The Collatz cycle equation: a cycle of period p with k odd steps at positions I = {i₁ < i₂ < ... < i_k} ⊆ {0,...,p-1} gives

    S(I) = Σ_{j=1}^k 3^{k-j} · 2^{i_j} = n₀ · D,    where D = 2^p - 3^k.

**The lift.** Replace 2 → x, 3 → y in the formal expressions:

    D(x,y) = x^p - y^k
    S_I(x,y) = Σ_{j=1}^k y^{k-j} · x^{i_j}

The integer cycle equation is: D(2,3) | S_I(2,3).

**Polynomial non-divisibility (immediate):** In Q[x,y], viewed as polynomials in x with coefficients in Q[y]:
- deg_x(D) = p
- deg_x(S_I) = max(i_j) ≤ p - 1

Since a nonzero polynomial of degree < p cannot be a multiple of a polynomial of degree p (the quotient would need negative degree), we have:

    D(x,y) does NOT divide S_I(x,y) in Q[y][x].

This is trivially free — no deep mathematics needed.

---

## 2. The Specialization Defect: Polynomial Division Analysis

### 2.1. Setup

Perform polynomial long division in Q[y][x]:

    S_I(x,y) = Q(x,y) · D(x,y) + R(x,y)

where deg_x(R) < deg_x(D) = p. Since deg_x(S_I) ≤ p - 1 < p = deg_x(D), the quotient Q = 0 and R = S_I.

**Wait — this is the key observation.** The "remainder" is just S_I itself!

    R(x,y) = S_I(x,y)

This means the polynomial division is trivial: S_I = 0 · D + S_I. The cycle equation D(2,3) | S_I(2,3) is just asking whether the polynomial S_I vanishes modulo D upon specialization, but since S_I IS the remainder, the question is simply: does S_I(2,3) happen to be divisible by D(2,3)?

**This is a negative result for Section A.** The polynomial division approach gives us nothing beyond restating the original problem. The remainder is the original polynomial — there's no cancellation to analyze.

### 2.2. What if we try a different ring?

Instead of dividing in Q[y][x], we could try Q[x,y]/(some ideal). For example, work in Q[x,y]/(x^p - y^k). Then S_I = 0 in this quotient ring iff D | S_I. But at the specialization (2,3), the quotient ring becomes Q ≅ Q[x,y]/(x-2, y-3), and the condition becomes D(2,3) | S_I(2,3) — circular again.

### 2.3. A more productive framing: the resultant

Rather than polynomial division, consider: when does D(x,y) and S_I(x,y) share a common factor over Q̄? This is detected by the resultant.

**Definition.** Res_x(D, S_I) = resultant with respect to x, viewed as polynomials in Q[y][x]. This is a polynomial in y alone. At y = 3:

    Res_x(D, S_I)|_{y=3} = Res_x(x^p - 3^k, S_I(x, 3))

If D(2,3) | S_I(2,3), then x = 2 is a common root of D(x,3) = x^p - 3^k (which vanishes iff 2^p = 3^k, false for p,k > 0) — wait, x = 2 is NOT a root of D(x,3) = x^p - 3^k (since 2^p ≠ 3^k for p,k > 0).

**Correction:** D(2,3) | S_I(2,3) does NOT mean D and S_I share a root at x = 2. It means the INTEGER D(2,3) divides the INTEGER S_I(2,3). These are completely different conditions!

The resultant detects when two polynomials share a COMMON ROOT (as polynomials). The cycle equation asks about integer divisibility at a specific point. The resultant approach is thus not directly applicable.

**Verdict on Section A:** The polynomial division and resultant approaches do not naturally capture integer divisibility. The specialization defect is not a "defect" in the algebraic-geometry sense (common roots) but in the number-theoretic sense (integer divisibility). This is the fundamental obstacle.

---

## 3. Mason-Stothers Analysis (Section B)

### 3.1. The theorem

**Mason-Stothers (1983).** If A, B, C ∈ C[t] are coprime with A + B = C, then:

    max(deg A, deg B, deg C) ≤ deg(rad(ABC)) - 1

where rad(f) = product of distinct irreducible factors.

### 3.2. Attempt to apply it

The cycle equation is S(I) = n₀ · D, i.e., S(I) = n₀ · (2^p - 3^k). This can be written:

    n₀ · 3^k + S(I) = n₀ · 2^p

Set A = n₀ · y^k, B = S_I(x,y), C = n₀ · x^p. Then A + B = C.

**Problem 1: n₀ is not a polynomial.** The value n₀ = S_I(2,3)/D(2,3) is a rational number (an integer, for cycles). It depends on I. There's no natural polynomial "n₀(x,y)" — it's defined only at the specialization point.

**Attempt to fix:** We could formally write n₀(x,y) = S_I(x,y)/D(x,y) as a rational function. Then:

    n₀(x,y) · y^k + S_I(x,y) = n₀(x,y) · x^p

    S_I(x,y) · y^k / D(x,y) + S_I(x,y) = S_I(x,y) · x^p / D(x,y)

    S_I · y^k + S_I · D = S_I · x^p

    S_I · (y^k + D) = S_I · x^p

    S_I · x^p = S_I · x^p  ✓

This is a tautology! The identity n₀ · y^k + S_I = n₀ · x^p becomes trivially true when n₀ = S_I/D, because D = x^p - y^k.

**Problem 2: Mason-Stothers requires polynomials, not rational functions.** Clearing denominators gives a polynomial identity, but it's tautological.

**Problem 3: Two-variable Mason-Stothers.** The standard Mason-Stothers is for ONE variable. There is a multi-variable analogue (the abc theorem for function fields of curves), but it requires the polynomials to live in k[t] for a single variable t.

### 3.3. Attempting a one-variable reduction

Fix y = 3 (or let y be a function of x). Then:
- D(x) = x^p - 3^k (a polynomial in x)
- S_I(x) = Σ_{j=1}^k 3^{k-j} · x^{i_j} (a polynomial in x)
- n₀(x) = S_I(x)/D(x) (a rational function)

For Mason-Stothers, we need a polynomial identity A + B = C with coprime polynomials.

Write: S_I(x) = n₀(x) · D(x). This is a divisibility statement in C[x], NOT an additive identity.

Alternatively, consider the identity D + (- D) = 0 — useless.

Consider: S_I(x) + (n₀ · 3^k) = n₀ · x^p. Here n₀ is a number (when y = 3 is fixed), not a polynomial. So this is:

    A(x) = S_I(x),  B = n₀ · 3^k (constant),  C(x) = n₀ · x^p

These ARE polynomials (B is a constant polynomial)! Mason-Stothers gives:

    max(deg A, deg B, deg C) ≤ deg(rad(ABC)) - 1

But:
- deg A = max(i_j) ≤ p - 1
- deg B = 0
- deg C = p
- max = p

rad(ABC): A = S_I(x) has ≤ p - 1 distinct roots. B is constant (no roots as polynomial). C = n₀ · x^p has one root: x = 0.

So rad(ABC) = rad(S_I(x)) · x, which has degree at most p - 1 + 1 = p (if S_I has p - 1 distinct roots).

Mason-Stothers: p ≤ p - 1. This is FALSE — contradiction!

**Wait — let me re-examine.** The identity A + B = C requires these to be COPRIME polynomials. But we're assuming S_I(x) + n₀ · 3^k = n₀ · x^p, and we need gcd(A, B, C) = 1 (pairwise coprime, technically gcd of any two = 1).

Actually, B = n₀ · 3^k is a NONZERO constant. It is coprime to any polynomial (gcd with any polynomial is a constant, which divides out). And gcd(A, C) = gcd(S_I(x), n₀ · x^p).

If S_I(0) = 3^{k-1} · x^0 term (when i₁ = 0), so S_I(0) = 3^{k-1} ≠ 0 in this case, meaning x ∤ S_I. Then gcd(S_I, x^p) = 1 in C[x].

If i₁ > 0 (no odd step at position 0), then S_I(0) = 0. In fact x^{i₁} | S_I(x), so gcd(S_I, x^p) = x^{i₁}.

So the coprimality condition may fail. Divide out: let S_I(x) = x^{i₁} · S̃_I(x). Then:

    x^{i₁} · S̃_I(x) + n₀ · 3^k = n₀ · x^p

This is NOT of the form A + B = C with coprime A, C, because x^{i₁} | A but x ∤ B (B is constant ≠ 0), so actually gcd(A, C) = x^{i₁} but gcd(B, A) = 1 and gcd(B, C) = 1. Wait — pairwise coprimality requires gcd(A,C) = 1.

The standard Mason-Stothers doesn't require pairwise coprimality of A, B, C — it requires gcd(A, B, C) = 1 (some formulations) or pairwise coprime (some formulations). Let me use the standard form:

**Mason-Stothers (precise form).** If a + b + c = 0 with a, b, c ∈ C[t], gcd(a,b,c) = 1, not all constant, then:

    max(deg a, deg b, deg c) ≤ deg(rad(abc)) - 1

Set a = S_I(x), b = n₀ · 3^k, c = -n₀ · x^p. Then a + b + c = 0 (assuming the cycle equation holds). gcd(a, b, c) = gcd(S_I, n₀ · 3^k, n₀ · x^p).

Since b is constant and nonzero: gcd(a, b, c) = gcd(S_I, n₀ · x^p, n₀ · 3^k). This is gcd of a polynomial with two constants (one nonzero), which is 1 (up to units). ✓

Now: max(deg a, deg b, deg c) = max(p-1, 0, p) = p.

rad(abc) = rad(S_I(x) · n₀ · 3^k · (-n₀) · x^p) = rad(S_I(x) · x^p) = rad(S_I(x)) · x (if x ∤ S̃_I) or just rad(S_I(x)) (if x | S_I, then x is already a factor of S_I).

Let r = number of distinct roots of S_I · x^p. We have:
- x^p contributes root x = 0
- S_I has degree max(i_j) ≤ p - 1, so at most p - 1 roots

If 0 is not a root of S_I: deg(rad(abc)) ≤ p - 1 + 1 = p. Mason-Stothers requires p ≤ p - 1. **CONTRADICTION!**

If 0 IS a root of S_I: deg(rad(abc)) ≤ p - 1 (roots of S_I already include 0). Mason-Stothers requires p ≤ p - 1 - 1 = p - 2. **Also a contradiction!**

### 3.4. What does this contradiction mean?

**It means the identity S_I(x) + n₀ · 3^k = n₀ · x^p CANNOT HOLD as a polynomial identity in C[x].**

Wait — of course it can't. S_I(x) is a fixed polynomial (with coefficients involving powers of 3), and n₀ is a specific integer. The equation S_I(x) + n₀ · 3^k = n₀ · x^p would require S_I(x) = n₀ · (x^p - 3^k) = n₀ · D(x), i.e., D(x) | S_I(x) in C[x]. But deg S_I < deg D = p, so this is impossible (unless S_I = 0, which is excluded for k ≥ 1).

**So we've shown something trivially true: D(x) ∤ S_I(x) as polynomials. Mason-Stothers just confirms this fact.**

The real question is about the specialization at x = 2. Mason-Stothers gives a polynomial-level statement; it says nothing about values at specific points.

### 3.5. Attempting to extract information from Mason-Stothers about the specialization

Can we relate the polynomial identity to the specialization? Consider:

    S_I(x) = n₀ · (x^p - 3^k) + E(x)

where E(x) = S_I(x) - n₀ · (x^p - 3^k). This is a polynomial of degree p (from the -n₀ · x^p term... wait, but deg S_I ≤ p - 1). So:

    E(x) = S_I(x) - n₀ · x^p + n₀ · 3^k

    deg(E) = p (from the -n₀ · x^p term)

    E(2) = S_I(2) - n₀ · 2^p + n₀ · 3^k = S_I(2) - n₀ · D(2) ... wait, D(2) = 2^p - 3^k.

    E(2) = S(I) - n₀ · (2^p - 3^k) = S(I) - n₀ · D = 0    (by the cycle equation)

So the cycle equation is: E(x) vanishes at x = 2, where E(x) = S_I(x) - n₀ · (x^p - 3^k).

E is a polynomial of degree p with leading coefficient -n₀. Its roots are determined by the equation S_I(x) = n₀ · (x^p - 3^k). The cycle equation says x = 2 is one such root.

Can Mason-Stothers constrain the roots of E? Not directly — Mason-Stothers is about relationships between coprime polynomials, not about the roots of a single polynomial.

### 3.6. Verdict on Mason-Stothers (Direct Application)

**Mason-Stothers confirms polynomial non-divisibility (which was already trivial from degree comparison) but does NOT constrain integer divisibility at the specialization point x = 2.**

The fundamental issue: Mason-Stothers is a statement about polynomials as formal objects. It says deg(rad(ABC)) is large relative to deg(A), deg(B), deg(C). But it says NOTHING about the values rad(A(2)·B(2)·C(2)) or about divisibility at a point.

This is the core obstruction for the entire function-field approach.

---

## 4. One-Variable Specialization Along a Curve (Section C)

### 4.1. The idea

Instead of specializing at a point (x,y) = (2,3), parameterize a curve through (2,3) and apply Mason-Stothers to the restricted polynomials.

**Natural choice:** y = x^α where α = log 3/log 2 ≈ 1.585. Then (2, 2^α) = (2, 3). But α is irrational, so y = x^α is not a polynomial relation.

**Alternative:** y = x + 1 (a line through (2,3)). Then:
- D(x) = x^p - (x+1)^k
- S_I(x) = Σ (x+1)^{k-j} · x^{i_j}

These are polynomials in x. The cycle equation becomes D(2) | S_I(2).

Mason-Stothers applies to polynomial identities, not to divisibility at a point. Same obstruction as before.

### 4.2. Puiseux series approach

Set y = x^α with α = log₂ 3. Then:
- D(x) = x^p - x^{αk}
- S_I(x) = Σ x^{α(k-j) + i_j}

These are "generalized polynomials" (Puiseux monomials). They live in C{{x^{1/N}}} for large N.

Mason-Stothers does not apply to Puiseux series — it requires polynomials. One could try to clear denominators in the exponents by substituting x = t^N, but then the degrees blow up by a factor of N, and the radical would also grow, making the bound vacuous.

### 4.3. Rational approximation approach

Take α = a/b ∈ Q close to log₂ 3 and set y = x^{a/b}. Substitute x = t^b, y = t^a. Then:
- D(t) = t^{bp} - t^{ak}
- S_I(t) = Σ t^{a(k-j) + b·i_j}

Now Mason-Stothers applies (these are polynomials in t). But the cycle equation becomes D(2^{1/b}) | S_I(2^{1/b}), which is about specialization at a specific (irrational) point. Same obstruction.

Moreover, 3 = 2^α ≈ 2^{a/b}, so 3^b ≈ 2^a. The approximation error means D(2^{1/b}) ≠ 2^p - 3^k; instead D(2^{1/b}) = 2^p - 2^{ak/b} ≠ 2^p - 3^k.

**Verdict:** One-variable specializations along curves do not escape the fundamental problem: Mason-Stothers constrains polynomial identities, not point evaluations.

---

## 5. Resultant Analysis (Section D)

### 5.1. Computing the resultant

Res_x(D, S_I) where D = x^p - y^k and S_I = Σ y^{k-j} · x^{i_j}.

By the property of resultants: Res_x(D, S_I) = Π_{α: D(α,y)=0} S_I(α, y), where the product is over all roots of D in x (with multiplicity).

D(x,y) = x^p - y^k = 0 has roots x = ζ^m · y^{k/p} where ζ = e^{2πi/p} and m = 0, 1, ..., p-1 (in the algebraic closure).

So:
    Res_x(D, S_I) = Π_{m=0}^{p-1} S_I(ζ^m · y^{k/p}, y)

    = Π_{m=0}^{p-1} Σ_{j=1}^k y^{k-j} · (ζ^m · y^{k/p})^{i_j}

    = Π_{m=0}^{p-1} Σ_{j=1}^k ζ^{m·i_j} · y^{k-j + k·i_j/p}

This is a product of p sums, each evaluated at a p-th root of unity times y^{k/p}. The exponents of y are fractional (involving k/p), so the resultant lives in C[y^{1/p}], not C[y].

Actually, let me compute this more carefully. The resultant Res_x(x^p - y^k, S_I(x,y)) is a polynomial in y. We can compute it as:

    Res_x(x^p - y^k, S_I(x,y)) = Π_{ω^p = y^k} S_I(ω, y)

For y = 3: the roots of x^p = 3^k are x = 3^{k/p} · ζ^m (complex numbers). Only the real positive root x = 3^{k/p} ≈ 2 (since k/p ≈ log 2/log 3) is close to x = 2.

The resultant Res_x(x^p - 3^k, S_I(x, 3)) = Π_{m=0}^{p-1} S_I(3^{k/p} · ζ^m, 3).

If this resultant equals 0, then S_I and D share a common root (over C). But D(2,3) = 2^p - 3^k ≠ 0 (since log₂ 3 is irrational). So x = 2 is NOT a root of D(x,3). The cycle equation D(2,3) | S_I(2,3) does NOT require that D and S_I share a common root.

**Key insight:** Integer divisibility (D(2,3) | S_I(2,3)) is fundamentally different from algebraic divisibility (D | S_I as polynomials or sharing a common root). The resultant detects the latter, not the former.

### 5.2. Norm form interpretation

There is one connection worth noting. Define:

    N_D(S_I) := Res_x(D, S_I) / (leading coeff of D in x)^{deg_x S_I}

This is the "norm" of S_I modulo D. In the ring R = Q[y][x]/(D), the norm of S_I is the product of all conjugates:

    N(S_I) = Π_{α: D(α)=0} S_I(α)

By properties of norms: D | S_I in Q[y][x] iff N(S_I) = 0. Since D ∤ S_I, we know N(S_I) ≠ 0 as a polynomial in y.

At the specialization y = 3: N(S_I)|_{y=3} = Π_{α^p = 3^k} S_I(α, 3).

The cycle equation D(2,3) | S_I(2,3) does NOT require N(S_I)|_{y=3} = 0 (since 2 is not a root of x^p - 3^k).

**Verdict on Section D:** Resultants detect common roots of polynomials, not integer divisibility at specific points. Not directly applicable.

---

## 6. The Wronskian Approach (Section E)

### 6.1. Setup

Mason-Stothers is proved via the Wronskian. For polynomials f, g ∈ C[t]:

    W(f, g) = f'g - fg'

If f, g are coprime: W ≠ 0, and deg W ≤ deg f + deg g - 1.

### 6.2. Application attempt

Consider f(x) = S_I(x, 3) and g(x) = D(x, 3) = x^p - 3^k as polynomials in x.

    W(f, g) = S_I'(x,3) · (x^p - 3^k) - S_I(x,3) · p·x^{p-1}

Are f and g coprime? D(x,3) = x^p - 3^k = Π_{m=0}^{p-1} (x - 3^{k/p} ζ^m). S_I(x,3) = Σ 3^{k-j} x^{i_j}, which is a polynomial of degree ≤ p - 1. For generic I, gcd(f, g) = 1.

If coprime: deg W = deg S_I' + deg D - 1 = (max(i_j) - 1) + p - 1 = max(i_j) + p - 2 ≤ 2p - 3.

Alternatively, deg W = deg(S_I' · D - S_I · pxp-1) ≤ max(max(i_j) - 1 + p, max(i_j) + p - 1) = max(i_j) + p - 1 ≤ 2p - 2.

This gives valid bounds on the Wronskian, but I don't see how to connect it to the integer divisibility question at x = 2.

The Wronskian W(2) = S_I'(2,3) · D(2,3) - S_I(2,3) · p · 2^{p-1}.

If D(2,3) | S_I(2,3), then: W(2) = S_I'(2,3) · D - n₀ · D · p · 2^{p-1} = D · (S_I'(2,3) - n₀ · p · 2^{p-1}).

So W(2) is divisible by D. This constrains W(2) to be large. Meanwhile, W is a polynomial of degree ≤ 2p - 2, so |W(2)| ≤ C · 2^{2p-2} for some C depending on coefficients.

This gives: |D| ≤ |W(2)|/|S_I'(2,3) - n₀ · p · 2^{p-1}| ≤ C · 2^{2p-2} / |S_I' - n₀ · p · 2^{p-1}|.

Not useful unless we can bound the denominator from below.

**Verdict:** The Wronskian gives degree bounds on polynomial identities but does not constrain integer evaluations in a useful way.

---

## 7. Explicit Computations (Section F)

Without computational tools, I'll work through the smallest meaningful case by hand.

### 7.1. Case p = 5, k = 3

D(2,3) = 2^5 - 3^3 = 32 - 27 = 5.

Admissible patterns I = {i₁, i₂, i₃} ⊆ {0,1,2,3,4} with |I| = 3:

There are C(5,3) = 10 patterns. For each:

S(I) = 3² · 2^{i₁} + 3¹ · 2^{i₂} + 3⁰ · 2^{i₃} = 9 · 2^{i₁} + 3 · 2^{i₂} + 2^{i₃}

| I | S(I) | S mod 5 | n₀ = S/5? |
|---|---|---|---|
| {0,1,2} | 9·1 + 3·2 + 4 = 19 | 4 | - |
| {0,1,3} | 9·1 + 3·2 + 8 = 23 | 3 | - |
| {0,1,4} | 9·1 + 3·2 + 16 = 31 | 1 | - |
| {0,2,3} | 9·1 + 3·4 + 8 = 29 | 4 | - |
| {0,2,4} | 9·1 + 3·4 + 16 = 37 | 2 | - |
| {0,3,4} | 9·1 + 3·8 + 16 = 49 | 4 | - |
| {1,2,3} | 9·2 + 3·4 + 8 = 38 | 3 | - |
| {1,2,4} | 9·2 + 3·4 + 16 = 46 | 1 | - |
| {1,3,4} | 9·2 + 3·8 + 16 = 58 | 3 | - |
| {2,3,4} | 9·4 + 3·8 + 16 = 76 | 1 | - |

**No S(I) is divisible by 5.** No cycle for p = 5, k = 3.

Now let's examine the polynomial structure. S_I(x,y) for I = {0,1,2}:

    S_I = y² · x⁰ + y¹ · x¹ + y⁰ · x² = y² + xy + x²

    D = x⁵ - y³

S_I(2,3) = 9 + 6 + 4 = 19. D(2,3) = 5. 5 ∤ 19. ✓

For I = {0,3,4}: S_I = y² + y·x³ + x⁴ = y² + x³y + x⁴.
S_I(2,3) = 9 + 24 + 16 = 49. D(2,3) = 5. 5 ∤ 49. (49 = 9·5 + 4). ✓

### 7.2. Case p = 7, k = 4

D(2,3) = 128 - 81 = 47.

S(I) = 27 · 2^{i₁} + 9 · 2^{i₂} + 3 · 2^{i₃} + 2^{i₄}, I ⊂ {0,...,6}, |I| = 4.

C(7,4) = 35 patterns. Let me check a few:

I = {0,1,2,3}: S = 27 + 18 + 12 + 8 = 65. 65 mod 47 = 18. ✗
I = {0,1,2,4}: S = 27 + 18 + 12 + 16 = 73. 73 mod 47 = 26. ✗
I = {0,1,2,5}: S = 27 + 18 + 12 + 32 = 89. 89 mod 47 = 42. ✗
I = {0,1,2,6}: S = 27 + 18 + 12 + 64 = 121. 121 mod 47 = 27. ✗
I = {0,1,3,4}: S = 27 + 18 + 24 + 16 = 85. 85 mod 47 = 38. ✗
I = {0,1,3,5}: S = 27 + 18 + 24 + 32 = 101. 101 mod 47 = 7. ✗
I = {0,1,3,6}: S = 27 + 18 + 24 + 64 = 133. 133 mod 47 = 39. ✗
I = {0,1,4,5}: S = 27 + 18 + 48 + 32 = 125. 125 mod 47: 125 - 2·47 = 31. ✗
I = {0,1,4,6}: S = 27 + 18 + 48 + 64 = 157. 157 - 3·47 = 16. ✗
I = {0,1,5,6}: S = 27 + 18 + 96 + 64 = 205. 205 - 4·47 = 17. ✗
I = {0,2,3,4}: S = 27 + 36 + 24 + 16 = 103. 103 - 2·47 = 9. ✗
I = {0,2,3,5}: S = 27 + 36 + 24 + 32 = 119. 119 - 2·47 = 25. ✗
I = {0,2,3,6}: S = 27 + 36 + 24 + 64 = 151. 151 - 3·47 = 10. ✗
I = {0,2,4,5}: S = 27 + 36 + 48 + 32 = 143. 143 - 3·47 = 2. ✗
I = {0,2,4,6}: S = 27 + 36 + 48 + 64 = 175. 175 - 3·47 = 34. ✗
I = {0,2,5,6}: S = 27 + 36 + 96 + 64 = 223. 223 - 4·47 = 35. ✗
I = {0,3,4,5}: S = 27 + 72 + 48 + 32 = 179. 179 - 3·47 = 38. ✗
I = {0,3,4,6}: S = 27 + 72 + 48 + 64 = 211. 211 - 4·47 = 23. ✗
I = {0,3,5,6}: S = 27 + 72 + 96 + 64 = 259. 259 - 5·47 = 24. ✗
I = {0,4,5,6}: S = 27 + 144 + 96 + 64 = 331. 331 - 7·47 = 2. ✗
I = {1,2,3,4}: S = 54 + 36 + 24 + 16 = 130. 130 - 2·47 = 36. ✗
I = {1,2,3,5}: S = 54 + 36 + 24 + 32 = 146. 146 - 3·47 = 5. ✗
I = {1,2,3,6}: S = 54 + 36 + 24 + 64 = 178. 178 - 3·47 = 37. ✗
I = {1,2,4,5}: S = 54 + 36 + 48 + 32 = 170. 170 - 3·47 = 29. ✗
I = {1,2,4,6}: S = 54 + 36 + 48 + 64 = 202. 202 - 4·47 = 14. ✗
I = {1,2,5,6}: S = 54 + 36 + 96 + 64 = 250. 250 - 5·47 = 15. ✗
I = {1,3,4,5}: S = 54 + 72 + 48 + 32 = 206. 206 - 4·47 = 18. ✗
I = {1,3,4,6}: S = 54 + 72 + 48 + 64 = 238. 238 - 5·47 = 3. ✗
I = {1,3,5,6}: S = 54 + 72 + 96 + 64 = 286. 286 - 6·47 = 4. ✗
I = {1,4,5,6}: S = 54 + 144 + 96 + 64 = 358. 358 - 7·47 = 29. ✗
I = {2,3,4,5}: S = 108 + 72 + 48 + 32 = 260. 260 - 5·47 = 25. ✗
I = {2,3,4,6}: S = 108 + 72 + 48 + 64 = 292. 292 - 6·47 = 10. ✗
I = {2,3,5,6}: S = 108 + 72 + 96 + 64 = 340. 340 - 7·47 = 11. ✗
I = {2,4,5,6}: S = 108 + 144 + 96 + 64 = 412. 412 - 8·47 = 36. ✗
I = {3,4,5,6}: S = 216 + 144 + 96 + 64 = 520. 520 - 11·47 = 3. ✗

**No S(I) is divisible by 47.** No cycle for p = 7, k = 4.

### 7.3. Observations from explicit computation

1. The residues S(I) mod D appear to be roughly uniformly distributed over {0,...,D-1} \ {0}, consistent with Theorem 4's equidistribution.

2. For p = 5, k = 3: D = 5, C(5,3) = 10. Heuristic: 10/5 = 2 expected hits. We got 0 — mild deviation.

3. For p = 7, k = 4: D = 47, C(7,4) = 35. Heuristic: 35/47 ≈ 0.74 expected hits. We got 0 — consistent.

4. The polynomial structure (S_I as polynomial in x,y) does not visibly constrain the residues beyond what's already captured by equidistribution.

---

## 8. The Fundamental Obstruction (Honest Assessment)

### 8.1. Why the function-field lift doesn't work directly

The function-field approach has a clean idea: abc is a THEOREM for polynomials, so lift the Collatz equation to the polynomial ring and exploit it. But there is a **fundamental disconnect** between polynomial algebra and integer evaluation:

**Polynomial non-divisibility ≠ Integer non-divisibility at a point.**

Specifically:
1. D(x,y) ∤ S_I(x,y) in Q[x,y] — trivially true from degree comparison.
2. D(2,3) | S_I(2,3) — the cycle equation we want to disprove.

Statement (1) says NOTHING about statement (2). The specialization map Q[x,y] → Q, f(x,y) ↦ f(2,3), is a ring homomorphism. It sends the non-divisibility D ∤ S_I to the statement that S_I(2,3) ∉ D(2,3) · Q — but wait, every integer is in D(2,3) · Q (since Q is a field). The integrality condition (that n₀ must be a POSITIVE INTEGER) is invisible to the polynomial ring.

**The issue is that Z is not a field.** In Q, every nonzero element divides every other. In Z, divisibility is nontrivial. The polynomial ring Q[x,y] maps to Q under specialization, where divisibility is trivial. To get integer divisibility, we'd need to work in Z[x,y] → Z, but Z[x,y] doesn't have unique factorization in the sense needed for Mason-Stothers.

### 8.2. Can we bridge the gap?

Here are three ideas for bridging the polynomial/integer gap, with honest assessments:

**Idea 1: Height bounds.** In arithmetic geometry, the connection between polynomial statements and integer statements goes through HEIGHT theory. The abc conjecture for integers IS the analogue of Mason-Stothers via the dictionary:

    degree ↔ log(height)
    rad(f) ↔ log(rad(n))

But this analogy is exactly what GIVES the abc conjecture — and the abc conjecture is unproved! The function-field lift reduces to: "use the polynomial abc theorem to prove the integer abc conjecture." This is a known open problem (the "abc over Z" problem). Mochizuki claims a proof via inter-universal Teichmuller theory, but this is not accepted by the mathematical community.

**Idea 2: Global function fields.** Instead of Q[x,y] (polynomials over Q), work in F_q[t] (polynomials over a finite field). The abc theorem for F_q[t] is Mason-Stothers. But the Collatz equation lives over Z, not over F_q[t]. To connect them, one would need a "function field analogue of the Collatz conjecture" and then transfer the result to Z via some comparison theorem. No such comparison theorem exists in general.

**Idea 3: Deformation theory.** Consider the family of equations D(2+ε, 3+δ) | S_I(2+ε, 3+δ) parameterized by (ε,δ). At the polynomial level (ε,δ formal), this family has no solutions. The integer solution (if it exists) is a single point (ε,δ) = (0,0). One could try to show that the "solution variety" is empty, hence has no integer points. But the "solution variety" is defined by the equation S_I(x,y) ≡ 0 mod (x^p - y^k), which is a congruence condition, not a polynomial equation. It doesn't define a variety in the usual sense.

### 8.3. What WOULD make this approach work?

For the function-field lift to prove anything about Collatz cycles, one would need:

1. **A specialization bound:** A theorem of the form "if D ∤ S in Q[x,y], then D(2,3) ∤ S(2,3) provided [some condition on degrees and heights]." Such theorems exist in limited form (e.g., the Hilbert irreducibility theorem says that if f(x,y) is irreducible in Q[x,y], then f(a,y) is irreducible for "most" a ∈ Z). But divisibility is not irreducibility, and we need a specific point (2,3), not "most" points.

2. **An effective abc for integers:** If the abc conjecture were proved (even in weak effective form), the Collatz no-cycles result would follow by Theorem 6. The function-field lift is essentially trying to "transfer" the polynomial abc theorem to the integer setting, which IS the abc conjecture.

3. **A structural constraint on S_I(2,3) mod D(2,3):** Some algebraic identity that forces S_I(2,3) to avoid 0 mod D(2,3). The polynomial structure of S_I (its degree, its coefficients) would need to imply something about its residue at (2,3). I don't see how to extract such a constraint without already solving the abc-type problem.

---

## 9. Alternative: The Normic Approach

### 9.1. A different use of the polynomial ring

Instead of trying to use Mason-Stothers, consider the NORM in the ring extension Q[x]/(x^p - 3^k) over Q.

In this ring, x is a root of x^p - 3^k, so x^p = 3^k. The norm of an element f(x) is:

    N(f) = Π_{m=0}^{p-1} f(ζ^m · 3^{k/p})

where ζ = e^{2πi/p}.

For f = S_I(x,3) = Σ 3^{k-j} x^{i_j}:

    N(S_I) = Π_{m=0}^{p-1} Σ_{j=1}^k 3^{k-j} · (ζ^m · 3^{k/p})^{i_j}

    = Π_{m=0}^{p-1} Σ_{j=1}^k 3^{k-j + k·i_j/p} · ζ^{m·i_j}

This is related to the DFT of the sequence {3^{k-j + k·i_j/p}} at frequencies given by the pattern I.

Key property: N(S_I) ∈ Q (and in fact ∈ Z up to bounded denominators), since the norm of an algebraic integer is an integer.

**The cycle equation S_I(2,3) = n₀ · D(2,3) implies:**

The "evaluation norm" at x = 2 satisfies |S_I(2,3)|^p ≈ |N(S_I)| (very roughly, up to conjugate factors).

But this doesn't quite work because x = 2 is not a root of D(x,3). The norm computation above uses the roots of D, not x = 2.

### 9.2. Connection to the resultant

Actually, Res_x(D, S_I)|_{y=3} = (-1)^{p·deg S_I} · N(S_I) (up to leading coefficients).

We showed in Section 5 that the resultant doesn't directly constrain integer divisibility.

**Verdict:** The normic approach provides interesting algebraic quantities but doesn't escape the fundamental obstruction.

---

## 10. A More Promising Direction: Effective Specialization Bounds

### 10.1. The Corvaja-Zannier approach

Corvaja and Zannier (2002, 2004) proved effective results on how often D(n) | S(n) can hold for polynomials D, S ∈ Z[x] and integer arguments n. Their results use the Subspace Theorem (Schmidt).

**Theorem (Corvaja-Zannier, 2004).** Let f, g ∈ Z[x] with deg f > deg g ≥ 0 and f irreducible. Then the set {n ∈ Z : f(n) | g(n)} is finite.

This is for ONE variable. In our setting: fix y = 3. Then D(x) = x^p - 3^k and S_I(x) = Σ 3^{k-j} · x^{i_j}. We have deg D = p > max(i_j) = deg S_I.

**If D were irreducible over Q:** Corvaja-Zannier would give: {x ∈ Z : D(x) | S_I(x)} is finite.

**Is D(x) = x^p - 3^k irreducible over Q?** By the criterion for x^n - a: x^p - 3^k is irreducible over Q iff 3^k is not a perfect p-th power. Since p ≥ 5 and k < p (with k/p ≈ log₂ 3 ≈ 0.63), 3^k is a p-th power only if p | k. Since k < p and k ≥ 1: p ∤ k (as k < p). So 3^k is NOT a p-th power, and x^p - 3^k is irreducible over Q by Eisenstein-like criteria (specifically, by the theorem on x^n - a being irreducible when a is not a perfect d-th power for any d | n with d > 1).

Actually, for x^n - a to be irreducible over Q, we need: a is not a perfect q-th power for any prime q | n, AND a ≠ -4b⁴ when 4 | n. Since n = p is an odd prime, we only need 3^k not a p-th power, which holds as argued.

**So x^p - 3^k IS irreducible over Q.** Corvaja-Zannier applies!

**Corvaja-Zannier gives:** Only finitely many integers x have D(x) | S_I(x).

**But we need more:** We need x = 2 to NOT be one of those finitely many exceptions.

The Corvaja-Zannier theorem is INEFFECTIVE in general (it uses the Subspace Theorem, which is ineffective). But for SPECIFIC polynomials, one can sometimes make it effective.

### 10.2. Effective bounds for x^p - a | g(x)

Consider: when does (x^p - a) | g(x) for x ∈ Z, where g has degree < p?

If x^p - a | g(x) as integers, then |g(x)| ≥ |x^p - a| or g(x) = 0.

For x = 2: |g(2)| = S_I(2,3) ≤ S_max = Σ 3^{k-j} · 2^{p-k+j-1} < 2^p (by Theorem 2's discussion). And |D(2)| = |2^p - 3^k| = D.

For D | S_I(2,3): we need S_I(2,3) = n₀ · D with n₀ ≥ 1. So S_I(2,3) ≥ D, i.e., Σ 3^{k-j} · 2^{i_j} ≥ 2^p - 3^k.

This is the existing lower bound on n₀ — nothing new.

### 10.3. Could we use Corvaja-Zannier for TWO variables?

Corvaja-Zannier also have results for the two-variable case (studying when f(m,n) | g(m,n) for (m,n) ∈ Z²). These involve the unit equation and are related to the Subspace Theorem.

For a FIXED point (2,3), this gives nothing — we need the result for ALL (m,n), not for one specific pair.

**Verdict:** Corvaja-Zannier gives finiteness but not effectiveness. The specific point (2,3) cannot be excluded by these general methods without additional input.

---

## 11. Synthesis: What Works, What Doesn't, and Where the Real Hope Is

### 11.1. What definitely doesn't work

1. **Direct polynomial division:** S_I has smaller degree than D, so the remainder IS S_I. No information gained.

2. **Direct Mason-Stothers application:** Confirms polynomial non-divisibility (trivially known). Says nothing about integer evaluation.

3. **Resultant/norm approach:** Detects common roots of polynomials, not integer divisibility.

4. **One-variable specializations along curves:** Same obstruction as direct Mason-Stothers — polynomial statement doesn't constrain point evaluation.

5. **Wronskian bounds:** Give polynomial degree relations, not integer divisibility constraints.

### 11.2. What partially works

1. **Corvaja-Zannier:** Shows D(x) | S_I(x) for only finitely many x (using irreducibility of x^p - 3^k). But ineffective — can't exclude x = 2 specifically.

2. **The normic viewpoint:** Provides a framework for thinking about the problem (S_I in Q[x]/(x^p - 3^k)), but doesn't yield bounds.

3. **Explicit computation:** Confirms no cycles for small (p,k), consistent with equidistribution theory. But this was already known.

### 11.3. The real obstruction (and where hope might lie)

The function-field lift fails because:

    **Polynomial algebra over Q → Integer arithmetic over Z**

is a "forgetful" map. Polynomial non-divisibility is about DEGREES; integer divisibility is about VALUES. Degrees are preserved by the ring structure; values depend on the specific arithmetic of (2,3).

The one setting where polynomial algebra DOES constrain integer values is **number fields and algebraic integers**. The norm N_{K/Q}(α) of an algebraic integer α ∈ O_K is a nonzero integer if α ≠ 0. This is an arithmetic consequence of the polynomial structure of the minimal polynomial.

**The most promising direction for future work:**

Consider S_I as an element of the ring of integers O_K of the number field K = Q(3^{1/p}). In this ring:

    S_I = Σ 3^{k-j} · 2^{i_j} = Σ (3^{1/p})^{p(k-j)} · 2^{i_j}

Setting α = 3^{1/p}, this becomes a polynomial in α with integer coefficients evaluated at specific powers. The element 2^p - 3^k = 2^p - α^{pk} ∈ Z is a rational integer.

The divisibility D | S_I in Z is equivalent to S_I/D ∈ Z, which is a much stronger condition than S_I/D ∈ O_K (since Z ⊂ O_K). The norm N(S_I) is divisible by N(D)^{v_D(S_I)} = D^p (since D ∈ Z has norm D^p in K = Q(α) of degree p).

**Key arithmetic constraint:**

If D | S_I in Z, then D^p | N_{K/Q}(S_I).

N(S_I) = Π_{m=0}^{p-1} S_I(ζ^m · 3^{1/p}) where ζ = e^{2πi/p}.

Each conjugate S_I(ζ^m · 3^{1/p}) = Σ 3^{k-j} · (ζ^m · 3^{1/p})^{... wait, S_I involves 2^{i_j}, not α^{i_j}.

Actually, S_I = Σ 3^{k-j} · 2^{i_j} is a RATIONAL INTEGER. It doesn't live in K = Q(3^{1/p}) in any interesting way — it's already in Q. Its norm is S_I^p. The condition D | S_I gives D^p | S_I^p, which is just (D | S_I)^p — tautological.

**The issue:** S_I and D are both rational integers. Embedding them in a number field doesn't add structure because they're both in the base field Q.

To make the number field approach work, we'd need to FACTOR D or S_I in O_K. For example, x^p - 3^k = Π (x - ζ^m · 3^{k/p}) in Q(ζ, 3^{1/p}). Then D = 2^p - 3^k = Π (2 - ζ^m · 3^{k/p}). The factorization of D in O_K involves the primes above 2.

This connects to the theory of cyclotomic fields and Kummer extensions, which is exactly where Mihailescu's proof of the Catalan conjecture (x^p - y^q = 1) operates. Indeed, the Catalan conjecture is the case S_I = D (i.e., n₀ = 1) of our equation.

**The Catalan connection is the deepest structural insight of this analysis.** Mihailescu proved 2^p - 3^k = 1 has no solution with p,k ≥ 2 (except 3² - 2³ = 1). His proof uses:
- Cyclotomic field Q(ζ_p)
- Factorization of x^p - 1 in Q(ζ_p)[x]
- Stickelberger's theorem on ideal class group annihilation
- Thaine's theorem on circular units

Could these tools be adapted to show 2^p - 3^k ∤ S_I for arbitrary S_I of the Collatz form? This would require extending Mihailescu's methods from "x^p - y^q = 1" to "x^p - y^q | f(x,y)" for specific f. This is a significant generalization but at least operates in the right algebraic framework.

---

## 12. Summary and Recommendations

### What was investigated:

| Section | Approach | Result |
|---|---|---|
| A | Polynomial division & specialization defect | Trivial: remainder = S_I itself. No info gained. |
| B | Mason-Stothers (direct) | Confirms polynomial non-divisibility (trivially known). No integer consequence. |
| C | One-variable specialization along curves | Same obstruction: polynomial ≠ integer. |
| D | Resultants | Detect common roots, not integer divisibility. |
| E | Wronskian | Degree bounds, not value bounds. |
| F | Explicit computation (p=5,k=3; p=7,k=4) | No cycles found. Consistent with equidistribution. |

### The fundamental obstruction:

**Mason-Stothers (polynomial abc) does not imply integer abc.** The function-field lift fails at the specialization step: going from the polynomial ring Q[x,y] to the integers Z at the point (2,3) loses all the algebraic structure that Mason-Stothers exploits.

### What IS genuinely promising:

1. **Corvaja-Zannier (Section 10):** The irreducibility of x^p - 3^k, combined with the Subspace Theorem, gives finiteness of solutions to D(x) | S_I(x). Making this effective for x = 2 would solve the problem. This requires deepening the Subspace Theorem, which is a known hard problem.

2. **Mihailescu/Catalan methods (Section 11.3):** The cycle equation is a generalization of the Catalan equation. Mihailescu's cyclotomic methods (Stickelberger, Thaine) might extend to the "x^p - y^k | S_I" setting. This is the most algebraically natural direction.

3. **The normic constraint D^p | N(S_I) in an appropriate number field** might give nontrivial bounds when computed in Q(ζ_p, 3^{1/p}). This connects to the arithmetic of Fermat-type equations in cyclotomic fields.

### Honest overall assessment:

The function-field lift, as initially conceived (use Mason-Stothers to bypass the abc conjecture), **does not work**. The gap between polynomial abc and integer abc is precisely the gap between function fields and number fields — one of the deepest divides in mathematics.

However, the investigation reveals a more promising algebraic direction: the **Catalan/Mihailescu connection**. The Collatz cycle equation is structurally similar to the Catalan equation, and Mihailescu's proof technique (cyclotomic fields + ideal class group theory) is the only known method that proves x^p - y^q ∈ {0, ±1} is impossible for large exponents. Extending these methods to "x^p - y^q | f(x,y) for specific structured f" is a concrete and well-defined mathematical challenge.

This should be the focus of Sub-problem D going forward: **not Mason-Stothers, but Mihailescu-style cyclotomic methods applied to the divisibility D | S_I.**
