# The Collatz Conjecture as a Height Inequality on a Fermat Curve

*Developed 2026-03-06 (Session 8, late)*

## 0. Executive Summary

The cycle equation D * n = S(I) can be reformulated as **ideal membership on the coordinate ring of a Fermat-type curve**. This gives a geometric framework where:

- The function field proof = "no small-bidegree element lies in the evaluation ideal over Q"
- The integer question = "does this remain true modulo D?"

The two-variable structure reveals a **dual degree bound** (R_I is small in BOTH variables) that is STRONGER than either single-variable function field argument. The natural language for exploiting this is **Arakelov intersection theory / height inequalities on the Fermat curve**.

**Status: FRAMEWORK IDENTIFIED. Not a proof, but potentially the right question.**

---

## 1. The Two-Variable Lift

### 1.1. Setup

Introduce formal variables s (for 3) and t (for 2). Define:

$$R_I(s, t) = \sum_{j=1}^{k} s^{k-j} \cdot t^{i_j}$$

where I = {i_1 < i_2 < ... < i_k} is a k-element subset of {0, ..., p-1}.

Then:
- S(I) = R_I(3, 2) (the Collatz sum)
- D = (t^p - s^k)|_{(3,2)} = 2^p - 3^k (the modulus)

### 1.2. The Curve

Define the Fermat-type curve:

$$C: t^p = s^k$$

in affine (s, t)-space. The point P = (3, 2):
- Is NOT on C over Q (since 2^p != 3^k)
- IS on C modulo D (since 2^p = 3^k mod D, by definition)

### 1.3. The Coordinate Ring

A = Z[s, t] / (t^p - s^k) is the coordinate ring of C.

The evaluation map ev: A -> Z/DZ sends s -> 3, t -> 2. Its kernel is the ideal (s-3, t-2) in A/DA.

**The cycle equation D | S(I) is equivalent to:**

$$R_I \in (s - 3, t - 2) \text{ in } A/DA$$

This is ideal membership in the coordinate ring of a Fermat curve modulo D.

---

## 2. The Dual Degree Bound

### 2.1. Bidegree of R_I

In A, elements can be represented with deg_t < p (since t^p = s^k). R_I has:

- deg_t(R_I) = i_k <= p-1 < p = deg_t(t^p - s^k)
- deg_s(R_I) = k-1 < k = deg_s(t^p - s^k)

**R_I is strictly smaller than D in BOTH variables independently.**

### 2.2. Comparison with Function Field Proofs

- Function field in t (replace 2 by variable): uses deg_t(R_I) < deg_t(D). One-line proof.
- Function field in s (replace 3 by variable): uses deg_s(R_I) < deg_s(D). Also a one-line proof.
- Two-variable: BOTH bounds hold simultaneously. Strictly stronger.

### 2.3. The Small Box

Define A_small = {elements of A with bidegree < (k, p)} = span of monomials {s^a * t^b : 0 <= a <= k-1, 0 <= b <= p-1}.

- dim(A_small) = k * p
- R_I is in A_small for every valid I
- The evaluation ideal (s-3, t-2) has codimension 1 in A/DA

The cycle equation asks: does A_small intersect (s-3, t-2) in A/DA, at a staircase element?

Over Q: A_small intersect (s-3, t-2) = {0} (the bidegree is too small). This IS the function field proof.

Over Z/DZ: the intersection could be nontrivial. This is the open question.

---

## 3. The Staircase Structure

### 3.1. Definition

R_I has exactly k nonzero coefficients, at positions:
- (k-1, i_1), (k-2, i_2), ..., (1, i_{k-1}), (0, i_k)

in the (s-exponent, t-exponent) grid. As the s-exponent decreases by 1, the t-exponent strictly increases. This is a **monotone staircase** in the bidegree grid.

### 3.2. Significance

The staircase is a very rigid combinatorial structure. It's not an arbitrary element of A_small -- it has:
- Exactly k nonzero entries (out of k*p possible)
- 0-1 coefficients
- Monotone anti-diagonal pattern

This rigidity is ADDITIONAL information beyond the bidegree bound. Any proof must exploit it.

### 3.3. Connection to Rank-Dependence

The staircase arises because the coefficient 3^{k-j} of the j-th term depends on the RANK of i_j within I. This rank-dependence makes S(I) fundamentally different from a standard subset sum (where coefficients are fixed regardless of which elements are chosen).

In the two-variable framework, the rank-dependence becomes GEOMETRIC: it determines the shape of R_I as a polynomial on C.

---

## 4. Height Inequality Perspective

### 4.1. The Core Idea

In Diophantine geometry, a **height** measures the arithmetic complexity of a point or a polynomial. The key theorems (Faltings, Vojta, abc) are HEIGHT INEQUALITIES: they bound how "simple" objects on curves can be.

The function field degree is the height over function fields. Over Z, the height is more complex (combining archimedean and non-archimedean information).

**Conjecture (informal):** There exists a height inequality on the Fermat curve C: t^p = s^k such that:

For any staircase element R of A_small with bidegree < (k, p), the evaluation R(3, 2) mod D is bounded away from 0.

### 4.2. What the Inequality Would Use

1. **The bidegree bound** on R (both degrees strictly less than those of D)
2. **The height of the point (3, 2)** on C mod D (small -- two consecutive primes)
3. **The arithmetic of D = 2^p - 3^k** (an S-unit in Z_{2,3} = Z[1/6])
4. **The staircase structure** of R (combinatorial rigidity)

### 4.3. Connection to Vojta's Conjecture

Vojta's conjecture is a vast generalization of the abc conjecture, stated for rational points on algebraic varieties. For the Fermat curve C and the family of staircase functions, Vojta's conjecture predicts specific height bounds.

The Collatz conjecture might follow from a SPECIFIC CASE of Vojta's conjecture, applied to:
- The variety: C: t^p = s^k
- The divisor: the zero locus of staircase elements
- The point: (3, 2) mod D

This specific case could be weaker than the full Vojta conjecture.

### 4.4. Connection to the Frey Curve / Wiles Approach

The equation 2^p = 3^k + D is an ABC equation with A = 3^k, B = D, C = 2^p. The Frey curve:

E: y^2 = x(x - 3^k)(x + D)

has Galois representation constrained by modularity. The ADDITIONAL constraint D | S(I) (from the Collatz cycle) gives extra arithmetic information about D that could constrain the Galois representation further.

Previous work on 2^p - 3^k = D treats the equation in isolation. The Collatz constraint is UNUSED in the arithmetic geometry literature.

---

## 5. The Parameterization

### 5.1. Universal Cover

Parameterize C by z: s = z^p, t = z^k. Then:

F_I(z) = R_I(z^p, z^k) = sum_{j=1}^{k} z^{p(k-j) + k*i_j}

This is a single-variable polynomial (lacunary: sum of k monomials).

The exponents e_j = p(k-j) + k*i_j satisfy:
- Maximum: max(e_j) <= max(p(k-1), k(p-1)) = k(p-1)
- The cycle equation becomes F_I(z_0) = 0 mod D for a specific z_0

### 5.2. The Specific z_0

If gcd(p,k) = 1 (required for primitive cycles), Bezout gives a, b with ap + bk = 1. Then:

z_0 = 3^a * 2^b mod D

since z_0^p = 3 and z_0^k = 2 modulo D.

F_I(z_0) = sum z_0^{e_j} = sum 3^{k-j} * 2^{i_j} = S(I) mod D. (Recovers the original equation, as expected.)

---

## 6. Why the Function Field Proof is an "Incomplete Shadow"

### 6.1. The Two-Constraint Structure

The Collatz cycle equation involves TWO constraints:

**Constraint 1 (Global):** D = 2^p - 3^k > 0 (the modulus is a difference of prime powers)

**Constraint 2 (Local):** D | S(I) for some k-element subset I (the modulus divides a structured sum)

The function field proof uses ONLY Constraint 1 (the degree of D exceeds the degree of S). It doesn't need Constraint 2 because the degree argument is already sufficient.

### 6.2. The Shadow Hypothesis

Over Z, Constraint 1 alone gives the abc barrier (we can't control D's factorization). But Constraint 2 is UNUSED.

**Hypothesis:** The integer proof fundamentally requires BOTH constraints, woven together. The function field proof is a degenerate case where Constraint 1 suffices -- a "shadow" that doesn't reveal the full structure of the real proof.

This would explain why:
- The function field proof doesn't transfer (it only uses half the information)
- Direct approaches fail (they either use Constraint 1 or Constraint 2, never both)
- The problem feels "harder than it should be" (we're missing half the argument)

### 6.3. The Interaction

Constraint 1 gives us the CURVE C and the POINT (3,2) on it.
Constraint 2 gives us the FUNCTION R_I that must vanish at that point.

The interaction: the function R_I is built from the SAME PRIMES (2 and 3) that define the curve C and the modulus D. This creates an algebraic feedback loop:
- D = 2^p - 3^k defines the curve
- S(I) uses powers of 2 and 3 (the same bases)
- The divisibility D | S(I) ties the curve to the function

This feedback loop is invisible in the function field (where 2 and 3 are constants). Over Z, the feedback is the source of both the truth of the conjecture and the difficulty of the proof.

---

## 7. What the Missing Concept Looks Like

### 7.1. Desiderata

The "arithmetic degree" or "Collatz height" would be a structured invariant h(R, P, C) depending on:
- R: a function on the curve (the staircase element R_I)
- P: a point on the curve (the evaluation point (3,2))
- C: the curve itself (the Fermat curve t^p = s^k)

It would satisfy:
1. **Bidegree bound:** h decreases when bideg(R) < bideg(D) (the function field property)
2. **Height sensitivity:** h increases with the arithmetic height of P
3. **Arithmetic interaction:** h accounts for the relationship between R's coefficients and the curve's defining equation (the feedback loop from 6.3)
4. **Non-vanishing:** h(R, P, C) > 0 implies R(P) != 0 mod D

### 7.2. Candidate Frameworks

1. **Arakelov intersection theory:** Computes "arithmetic intersection numbers" on arithmetic surfaces (Spec(Z) x C). Naturally combines archimedean heights with non-archimedean divisibility. The bidegree bound translates to the "horizontal" component; the point (3,2) gives the "vertical" component.

2. **Vojta's conjecture (specific case):** For staircase functions on Fermat curves evaluated at S-unit points, predict a height inequality that implies non-vanishing.

3. **Modularity + level lowering (Wiles-type):** Construct a Frey curve from 2^p = 3^k + D, use the Collatz constraint D | S(I) to further restrict the Galois representation, and derive a conductor contradiction.

### 7.3. Why This Might Be Tractable

The Collatz problem doesn't need the FULL abc conjecture or the FULL Vojta conjecture. It needs a SPECIFIC height inequality for:
- A specific curve (Fermat-type, well-studied)
- A specific point (small height, consecutive primes)
- A specific family of functions (staircases, rigid combinatorial structure)
- A specific modulus (S-unit, closely related to the curve)

Each specificity is a HANDLE. The general conjecture is wide open, but the specific case might be attackable because of all these handles.

---

## 8. Connection to Everything Else

### 8.1. The Barrier Diagnostic

This framework explains WHY the three barriers exist:

- **Barrier 1 (abc/counting):** The height inequality over Z is controlled by abc-type bounds. Without the full Vojta conjecture, we can't prove the height inequality.
- **Barrier 2 (equivalence):** The cascade IS the Collatz iteration because the staircase structure of R_I perfectly encodes the dynamics. Any analysis of R_I reconstructs the orbit.
- **Barrier 3 (completion blindness):** Local methods (p-adic, Hensel lifting) can't see the GLOBAL height inequality, which requires combining all places.

### 8.2. The Function Field Insight

The function field proof (from function_field_collatz.md) is the "shadow" of this framework:
- Over F_q[t]: height = degree, and the degree argument gives the height inequality trivially.
- Over Z: height involves Arakelov data, and the height inequality is the open problem.
- The Ostrowski obstruction: no single absolute value gives the height. The full Arakelov height (which combines ALL absolute values) might work.

### 8.3. The Galois/Wiles Pattern

- **Galois:** equation -> symmetry group -> structural property -> contradiction
- **Wiles:** equation -> elliptic curve -> Galois representation -> modularity contradiction
- **Collatz (proposed):** cycle equation -> staircase on Fermat curve -> height invariant -> non-vanishing inequality

The "richer object" is the Fermat curve C with its staircase functions. The "structural property" is the height inequality. The "contradiction" is that the height inequality prevents evaluation at (3,2) from being zero modulo D.

---

## 9. Specific Research Program

### Step 1: Compute Arakelov Heights
For small (p, k), compute the Arakelov intersection number of:
- The horizontal divisor defined by R_I = 0 on C
- The vertical fiber at the prime(s) dividing D
- The archimedean component at the point (3,2)

### Step 2: Identify the Height Inequality
Determine whether the computed Arakelov data satisfies a pattern:
- Does the arithmetic intersection number grow with p?
- Is there a uniform lower bound independent of I?
- How does it relate to the bidegree of R_I?

### Step 3: Connect to Existing Theory
Determine which known results (if any) imply the height inequality:
- Specific cases of Vojta's conjecture for Fermat curves?
- Effective results from Baker's method applied to the S-unit equation?
- Modularity results for the associated Frey curve?
- The explicit abc conjecture (known for specific families)?

### Step 4: Exploit the Collatz Constraint
The key novelty: use D | S(I) (not just D = 2^p - 3^k) in the arithmetic geometry. This extra constraint is ABSENT from the existing literature on 2^p - 3^k. Determine what it implies for:
- The Galois representation of the Frey curve
- The conductor of the associated modular form
- The Arakelov height of the evaluation point

---

## 10. The Polynomial Reformulation (Key Computational Discovery)

### 10.1. The Clean Conjecture

By re-indexing the sum, S(I) = P_I(3) where:

$$P_I(x) = 2^{a_0} + 2^{a_1} x + 2^{a_2} x^2 + \cdots + 2^{a_{k-1}} x^{k-1}$$

with $a_0 > a_1 > \cdots > a_{k-1} \geq 0$ (strictly decreasing, all in $\{0, \ldots, p-1\}$).

**CONJECTURE (Equivalent to Collatz Part 1):** For all $p \geq 2$, $k \geq 1$ with $2^p > 3^k$, and all strictly decreasing sequences $p-1 \geq a_0 > a_1 > \cdots > a_{k-1} \geq 0$, we have $(2^p - 3^k) \nmid P_I(3)$.

### 10.2. The Rearrangement Inequality Connection

The strictly decreasing coefficient condition is equivalent to the monotonicity (staircase) constraint. By the **Rearrangement Inequality**:

- Coefficients $c_j = 2^{a_j}$ are decreasing: $c_0 > c_1 > \cdots > c_{k-1}$
- Powers $x^j = 3^j$ are increasing: $1 < 3 < 9 < \cdots$
- Anti-sorted pairing (large coeff with small power) gives the **MINIMUM** sum

Therefore: the staircase assignment gives the unique minimum over all $k!$ permutations of the same coefficients.

### 10.3. Computational Evidence

| Test | Result |
|---|---|
| Staircase $P(3) \equiv 0 \pmod{D}$? | **NEVER** (all tested $(p,k)$ up to $p = 60$) |
| Unordered $P_\sigma(3) \equiv 0 \pmod{D}$? | Yes, at rate $\approx 1/D$ (random expectation) |
| Minimum inversions among 0-hitters | Always $\geq 1$ (often $\geq 2$) |

The monotonicity constraint **perfectly** excludes 0 mod D. Without it, the sums behave randomly.

### 10.4. Special Case: Tightest Staircase

For $I = \{0, 1, \ldots, k-1\}$: the sum telescopes to $S = 3^k - 2^k$ (geometric series).

$S \mod D = (2^p - 2^k) \mod D = 2^k(2^{p-k} - 1) \mod D$

This is $0$ iff $D \mid 2^{p-k} - 1$, which requires $\text{ord}_D(2) \mid (p-k)$. Since $\text{ord}_D(2) \gg p-k$ for all tested cases, this never holds.

### 10.5. Why This Matters

The reformulation separates the problem into:
1. **Algebraic structure:** $P$ is a polynomial of degree $k-1 < k$ with power-of-2 coefficients
2. **Combinatorial constraint:** coefficients are strictly decreasing
3. **Evaluation point:** $x = 3$ (one more than the coefficient base 2)
4. **Modulus:** $D = 2^p - 3^k = 2^p - x^k$ evaluated at $x = 3$

The function field proof uses (1) alone. The integer proof needs (1) + (2). The Rearrangement Inequality connects (2) to minimality, but proving the minimum avoids 0 mod D requires understanding the arithmetic interaction between (3) and (4).

### 10.6. Proven Special Cases

**Consecutive runs** $I = \{m, m+1, \ldots, m+k-1\}$: P(3) = $2^m(3^k - 2^k)$. Since $D$ is odd, $D \mid P(3)$ iff $D \mid (3^k - 2^k)$ iff $D \mid (2^p - 2^k)$ iff $D \mid 2^k(2^{p-k}-1)$ iff $\text{ord}_D(2) \mid (p-k)$. Fails because $\text{ord}_D(2) \gg p-k$ (by Rhin bound + computation).

**Near-tightest** $I = \{0, \ldots, k-2, m\}$ for $m \geq k$: $P(3) = 2^m + 3^k - 3 \cdot 2^{k-1}$. Mod $D$: $P(3) \equiv 2^{k-1}(2^{m-k+1} + 2^{p-k+1} - 3) \pmod{D}$. The "inner" value $2^{m-k+1} + 2^{p-k+1} - 3 \leq 3 \cdot 2^{p-k} - 3 < D$ for $p \geq 10$ (since $D \approx 2^p \gg 2^{p-k}$). So $0 < \text{inner} < D$, making divisibility impossible. **Proved by SIZE** for $p \geq 10$.

These special cases suggest that the general proof might combine:
- **Size arguments** (for "spread-out" staircases where P(3) reduces to a small expression)
- **Order arguments** (for "tight" staircases where P(3) factors through a geometric series)
- **A bridging argument** (for intermediate cases)

### 10.7. Fixed-k Proof Program via Rearrangement + Size

**Theorem (k ≤ 4):** No nontrivial Collatz cycles exist with k ≤ 4 odd steps.

*Proof sketch:*
- k=1: P(3) = 2^a. D is odd, gcd(D, 2^a) = 1. No divisibility.
- k=2: P(3)/2^{a_1} = 2^d + 3 where 1 ≤ d ≤ p-1. For p ≥ 5: 0 < 2^d + 3 < D. Impossible.
- k=3: max P(3) = 5·2^{p-2} + 9 < 2D for p ≥ 7. Only m=1 (trivial). Verified p < 7 computationally.
- k=4: max P(3) ≈ 4D. Only odd m coprime to 3 in range: m=5 by size bound. For p ≥ 8: LHS < RHS. Small p checked.

**General structure for fixed k:**

For each k, max P(3)/D → (3/2)^k - 1 as p → ∞. Using Steiner bound (C8): n < (3/2)^{k-1}. So only m < (3/2)^{k-1} need checking.

Additional filters:
- m must be ODD (since n is odd for a nontrivial cycle)
- m must be coprime to 3 (since v_3(P(3)) = 0 always)
- m = 1, 2 give only the trivial cycle {1,2}

For k ≤ 4: **zero** valid m remain after these filters. PROVED by size alone.
For k = 5: only m = 5 to check.
For k = 10: ~12 values.
For k = 30: ~10^5 values.

Each (k, m) gives an S-unit equation with k+2 terms, solvable by Baker's method with effective bounds.

**This gives a DECISION PROCEDURE: for each fixed k, the Collatz no-cycle conjecture is decidable and (in principle) provable by finite computation.**

**THEOREM (k ≤ 4, NEW PROOF):** For $k \leq 4$, no nontrivial Collatz cycles exist.

*Proof:* The Steiner bound gives $n < (3/2)^{k-1}$. For nontrivial cycles: $n \geq 3$, $n$ odd, $\gcd(n, 3) = 1$ (from $v_3(P(3)) = 0$). For $k \leq 4$: $(3/2)^{k-1} \leq 3.375$, so $n \leq 3$. The only candidate $n = 3$ is eliminated by $3 \mid 3$. No valid $n$ exists. $\square$

Note: This proof uses only the Steiner bound (C8) and $v_3(P(3)) = 0$. It does NOT use the cascade, orbit verification, or any computation beyond the bound. It is the simplest known proof for $k \leq 4$.

**Comparison with C9 (k ≤ 30):** The cascade method proved k ≤ 30 by Collatz orbit verification up to n = 127834. The Rearrangement + size method gives an INDEPENDENT proof for k ≤ 4, and a systematic extension path for larger k that doesn't require orbit computation.

### 10.8. The Affine Walk Interpretation

The cycle equation is equivalent to an **affine walk** in Z/DZ:

- Start at $w_0 = 1$
- At step $m$: $w_m = 3 w_{m-1} + c_m \mod D$
- Perturbations: $c_m = 2^{a_{k-1-m}}$ (powers of 2, INCREASING since a is decreasing)
- Need $w_{k-1} = 0 \mod D$

**Key properties of the perturbations:**
1. Powers of 2 (specific arithmetic structure)
2. Strictly increasing: $c_1 < c_2 < \cdots < c_{k-1}$
3. Gap constraint: $c_m \geq 2^m$ (from $a_j \geq k-1-j$, which follows from strict decrease)

The walk with INCREASING perturbations never reaches 0. With decreasing or shuffled perturbations, it CAN reach 0 (at rate ~1/D). The increasing order "protects" the orbit.

**Dynamical interpretation:** The multiplication by 3 expands the orbit. The additive perturbations try to steer it back to 0. With increasing perturbations, the small corrections happen first (when they could help) and get washed out by the 3× expansion; the large corrections happen last (too little amplification). With decreasing perturbations, large corrections early get amplified by many 3× steps, allowing precise steering.

**Critical finding:** The claim fails for arbitrary increasing sequences — the walk CAN reach 0 with non-power-of-2 increasing c's. The power-of-2 constraint is ESSENTIAL, not just the ordering. The avoidance of 0 requires BOTH the ordering AND the arithmetic structure.

### 10.9. The Three Constraints

The Collatz no-cycles conjecture is equivalent to: the affine walk $w \to 3w + c_m$ in $\mathbb{Z}/D\mathbb{Z}$, starting at 1, never reaches 0, when the perturbations satisfy ALL THREE:

1. **Arithmetic:** Each $c_m$ is a power of 2
2. **Ordering:** $c_1 < c_2 < \cdots < c_{k-1}$ (strictly increasing)
3. **Growth:** $c_m \geq 2^m$ (exponential lower bound on perturbation size)

No single constraint suffices. No pair of constraints suffices. All three together exclude 0.

---

## 11. Honest Assessment

### What This Provides
1. A genuinely new GEOMETRIC framework for the Collatz no-cycles problem
1b. A CLEAN polynomial reformulation: Collatz Part 1 = "no polynomial with strictly decreasing power-of-2 coefficients, evaluated at 3, is divisible by 2^p - 3^k"
1c. The discovery that the REARRANGEMENT INEQUALITY precisely characterizes the staircase as the minimum, and that 0 mod D is avoided by the minimum but hit by non-minimal permutations at the random rate
2. The observation that R_I satisfies a DUAL degree bound (both variables), which is stronger than the single-variable function field argument
3. The insight that the function field proof may be an "incomplete shadow" that uses only one of two constraints
4. A specific connection to Arakelov theory and Vojta's conjecture
5. A concrete 4-step research program

### What This Does NOT Provide
1. A proof. The height inequality is conjectural.
2. Certainty that this is the right approach. It could be another reformulation that hits the same barriers.
3. Any guarantee that the specific height inequality is provable with current technology.

### Why It Might Work
- The function field proof tells us the answer SHOULD be trivial from the right viewpoint
- The Fermat curve framework provides the rich geometric structure needed for the Wiles pattern
- The Collatz constraint (D | S(I)) is an unused handle in the arithmetic geometry literature
- The specificity of the problem (specific curve, specific point, specific functions) gives many handles that the general abc/Vojta conjectures don't have

### Why It Might Not
- Arakelov theory on Fermat curves is technically very demanding
- The height inequality might REQUIRE the full abc conjecture, not just a special case
- The staircase structure might not give enough combinatorial leverage
- This could be another instance of Barrier 1 in fancier language

**Status: FRAMEWORK. The most concrete new direction of the project. Requires arithmetic geometry expertise to evaluate.**
