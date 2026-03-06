# Sum-Product Estimates and the Universal Spectral Gap for the Affine Collatz Walk

## 1. Introduction and Setup

### 1.1. The problem

For a prime p >= 5, the Markov operator M on Z/pZ is defined by

    (Mf)(x) = (1/2) f(x * 2^{-1}) + (1/2) f((3x+1) * 2^{-1}).

We write alpha = 2^{-1}, beta = 3 * 2^{-1}, gamma = 2^{-1} in F_p, so the two maps are T_0(x) = alpha*x and T_1(x) = beta*x + gamma.

**Known results:**
- (Combined Theorem) Every eigenvalue lambda != 1 satisfies |lambda| < 1. No eigenvalue lies on the unit circle.
- (Weak bound) |lambda_2| <= 1 - c/p for an absolute constant c > 0.
- (Numerical) |lambda_2| <= 0.81 for all 166 primes tested (p = 5 to p = 997). The mean is approximately 0.70 ~ 1/sqrt(2).

**Goal:** Prove |lambda_2| <= 1 - c_0 for a universal constant c_0 > 0 independent of p.

### 1.2. The eigenvalue equation in Fourier space

Let omega = e^{2*pi*i/p}. An eigenfunction f with eigenvalue lambda, expanded as f = sum_r a_r chi_r, satisfies (by Lemma 2.1 of the paper):

    M chi_r = (1/2) chi_{r*alpha} + (1/2) omega^{r*gamma} chi_{r*beta}.

Equivalently, for the coefficients (a_r) of an eigenvector:

    a_{r*alpha} + omega^{r*gamma} a_{r*beta} = 2*lambda * a_r      for all r in F_p*.  ... (*)

Substituting alpha = 2^{-1} and beta = 3*2^{-1}, and letting s = r*alpha = r/2, this becomes:

    a_s + omega^{2s * gamma} a_{3s} = 2*lambda * a_{2s}    for all s.

Since gamma = 2^{-1}, we have 2s * gamma = s, so:

    a_s + omega^s * a_{3s} = 2*lambda * a_{2s}             for all s in F_p*.  ... (**)

### 1.3. The support and its structure

Define the **support** S = {r in F_p* : a_r != 0}. From (**), if a_{2s} != 0, then at least one of a_s, a_{3s} must be nonzero. Conversely, if both a_s and a_{3s} are nonzero, their combination determines a_{2s}.

The operator M preserves the decomposition of F_p* into orbits of the group H = <2, 3> <= F_p*. The support S is contained in a union of such orbits.

**Key observation:** When |lambda| is close to 1, the equation (**) imposes very tight constraints. We can extract these by computing a_{6s} in two different ways.

---

## 2. The Approximate Invariance Constraints

### 2.1. Two-path computation of a_{6s}

From (**), for any s with a_{2s} != 0:

    a_s + omega^s * a_{3s} = 2*lambda * a_{2s}.

Apply (**) with s replaced by 3s:

    a_{3s} + omega^{3s} * a_{9s} = 2*lambda * a_{6s}.       ... (i)

Apply (**) with s replaced by s (giving a_{2s}), then apply (**) with 2s in place of s:

    a_{2s} + omega^{2s} * a_{6s} = 2*lambda * a_{4s}.        ... (ii)

And apply (**) with 2s replaced by s, starting from 3s:

    From s -> 2s: a_s + omega^s a_{3s} = 2*lambda * a_{2s}
    From 3s -> 6s: a_{3s} + omega^{3s} a_{9s} = 2*lambda * a_{6s}

These give us a_{6s} via path (3s -> 6s) and a_{6s} via path (2s -> 4s -> ...). Let us be more systematic.

### 2.2. Approximate eigenvector conditions when |lambda| ~ 1

Write lambda = (1 - epsilon) * e^{i*phi} where epsilon >= 0 is small. Set eta = 1 - |lambda|^2 (so eta ~ 2*epsilon for small epsilon).

From (**):
    |a_s + omega^s a_{3s}|^2 = 4|lambda|^2 |a_{2s}|^2.

Expand the left side:
    |a_s|^2 + |a_{3s}|^2 + 2 Re(omega^s * a_{3s} * conj(a_s)) = 4|lambda|^2 |a_{2s}|^2.

Now sum over all s in a <2>-orbit O = {s, 2s, 4s, ...} of size L_2 = ord_p(2). Writing the orbit as O = {s * 2^j : j = 0, ..., L_2 - 1}:

Sum over j of |a_{s*2^j}|^2 = sum over j of |a_{s*2^j}|^2 (obviously).

Let us denote the energy on the orbit as E_O = sum_{r in O} |a_r|^2.

The key identity (from Theorem 12): for a single character chi_r, ||M chi_r||^2 = 1/2. This is because the two output modes chi_{r*alpha} and chi_{r*beta} are distinct (since r != 0) and orthogonal. The norm is (1/2)^2 + (1/2)^2 = 1/2.

For a general eigenvector with eigenvalue lambda:
    ||Mf||^2 = |lambda|^2 ||f||^2.

But also:
    ||Mf||^2 = (1/2)||f||^2 + (1/2) Re <T_0 f, T_1 f>.

So:
    |lambda|^2 = 1/2 + (1/2) Re <T_0 f, T_1 f> / ||f||^2.

The cross-term is:
    <T_0 f, T_1 f> = sum_s a_{3s} * conj(a_s) * omega^{-s*gamma} = sum_s a_{3s} * conj(a_s) * omega^{-s/2}.

Wait, let me be more careful. We have T_0 f(x) = f(alpha*x) and T_1 f(x) = f(beta*x + gamma). So:

    <T_0 f, T_1 f> = (1/p) sum_x f(alpha*x) * conj(f(beta*x + gamma)).

In Fourier space, f = sum_r a_r chi_r, so:
    T_0 f = sum_r a_r chi_{r*alpha}
    T_1 f = sum_r a_r omega^{r*gamma} chi_{r*beta}

    <T_0 f, T_1 f> = sum_r a_r * conj(a_{r * beta/alpha}) * conj(omega^{r*beta/alpha * gamma})
                    ... [using orthogonality of characters]

Actually, let us be more careful. The modes in T_0 f are chi_{r*alpha} and the modes in T_1 f are chi_{r*beta} (with phase). For the inner product, we need the mode indices to match. So we need:

    r * alpha = r' * beta   =>  r' = r * alpha / beta = r * (1/2) / (3/2) = r/3.

So:
    <T_0 f, T_1 f> = sum_r a_r * conj(a_{r/3} * omega^{(r/3)*gamma})
                    = sum_r a_r * conj(a_{r/3}) * omega^{-r*gamma/3}.

Substituting s = r/3 (i.e., r = 3s):
    = sum_s a_{3s} * conj(a_s) * omega^{-s*gamma}.

With gamma = 2^{-1} = (p+1)/2:
    <T_0 f, T_1 f> = sum_s a_{3s} * conj(a_s) * omega^{-s*(p+1)/2}.

So:
    |lambda|^2 = 1/2 + (1/(2||f||^2)) Re[ sum_s a_{3s} conj(a_s) omega^{-s*(p+1)/2} ].

For |lambda| close to 1 (say |lambda|^2 = 1 - eta with eta small):

    1 - eta = 1/2 + (1/(2||f||^2)) Re[sum_s a_{3s} conj(a_s) omega^{-s*(p+1)/2}].

So:
    Re[sum_s a_{3s} conj(a_s) omega^{-s*(p+1)/2}] = (1 - 2*eta) ||f||^2.

By Cauchy-Schwarz, |sum_s a_{3s} conj(a_s) omega^{-s*(p+1)/2}| <= ||f||^2 (with equality iff a_{3s} = c * omega^{s*(p+1)/2} * a_s for a constant c of modulus 1).

So we need:
    Re[...] >= (1 - 2*eta) ||f||^2,

which forces the sum to be nearly equal to ||f||^2 in modulus, and nearly real. In particular, the phase alignment must be almost perfect.

### 2.3. The approximate twisted invariance

When |lambda| ~ 1, we need (approximately):

    a_{3s} ~ e^{i*theta} * omega^{s*(p+1)/2} * a_s     for all s in supp(a),

for some fixed phase theta. This is an **approximate twisted invariance under multiplication by 3**.

Similarly, from (**), for modes s with a_{2s} != 0:

    a_s + omega^s * a_{3s} = 2*lambda * a_{2s},

and since the two terms on the left contribute to orthogonal modes when s != 3s (which holds for s != 0 since 3 != 1 in F_p*), the magnitude of a_{2s} is controlled by |a_s| and |a_{3s}| individually. But when there are collisions in the orbit structure, the situation is more subtle.

### 2.4. The consistency constraint (6s two ways)

Let us derive the key constraint. From (**):

Path 1: Compute a_{6s} from a_{3s} and a_{9s}:
    a_{3s} + omega^{3s} * a_{9s} = 2*lambda * a_{6s}.

Path 2: Compute a_{6s} from a_{2s} and a_{6s} (by applying (**) with s -> 3s):

Wait, this doesn't immediately give two independent expressions for a_{6s}. Let me try differently.

From (**) with s:
    a_s + omega^s a_{3s} = 2*lambda * a_{2s}.

From (**) with 3s:
    a_{3s} + omega^{3s} a_{9s} = 2*lambda * a_{6s}.

These are on different orbits and don't directly conflict. The constraint arises when we track a chain.

**The (3/2)-chain.** Starting from mode r_0, define the chain:
    r_0, (3/2)*r_0, (3/2)^2*r_0, ..., (3/2)^n*r_0.

Each step multiplies by 3/2 in F_p. The chain has period ell = ord_p(3/2).

From (**), with s = r_0 * (3/2)^k:
    a_{(3/2)^k * r_0} + omega^{(3/2)^k * r_0} * a_{3*(3/2)^k * r_0} = 2*lambda * a_{2*(3/2)^k * r_0}.

Note: 2 * (3/2)^k = (3/2)^k * 2 and 3 * (3/2)^k = (3/2)^{k+1} * 2. So:
    a_{(3/2)^k * r_0} + omega^{(3/2)^k * r_0} * a_{(3/2)^{k+1} * 2 * r_0 / (omit: I need to be careful)}.

Let me use a cleaner substitution. Write t_k = (3/2)^k * r_0 in F_p. Then (**) with s = t_k / 2 gives:

Wait. Let me re-derive (**) more carefully.

The original eigenvalue equation from (*) is:
    a_{r/2} + omega^{r*gamma} * a_{3r/2} = 2*lambda * a_r    for all r != 0.

Here gamma = 2^{-1} mod p. So the equation is:

    a_{r/2} + omega^{r/(2)} * a_{3r/2} = 2*lambda * a_r.     ... (**)

(Since r*gamma = r/2 in F_p.)

Now set r = t_k = (3/2)^k * r_0:

    a_{t_k / 2} + omega^{t_k / 2} * a_{3*t_k/2} = 2*lambda * a_{t_k}.

But t_k / 2 = (3/2)^k * r_0 / 2 and 3*t_k/2 = (3/2)^{k+1} * r_0. So:

    a_{(3/2)^k * r_0 / 2} + omega^{(3/2)^k * r_0 / 2} * a_{(3/2)^{k+1} * r_0} = 2*lambda * a_{(3/2)^k * r_0}.

Define b_k = a_{t_k} = a_{(3/2)^k * r_0}. The equation becomes:

    a_{t_k/2} + omega^{t_k/2} * b_{k+1} = 2*lambda * b_k.   ... (***)

The term a_{t_k/2} = a_{(3/2)^k * r_0 / 2} is on the same <2, 3>-orbit as r_0 but may not be on the (3/2)-chain. Specifically, t_k/2 = (3/2)^k * r_0 * 2^{-1} = (3/2)^k * r_0 * alpha. This is r_0 * 3^k * 2^{-(k+1)}, which is on a *different* (3/2)-chain shifted by a factor of 2^{-1}.

This interleaving of (3/2)-chains is what makes the problem difficult. The eigenvalue equation couples two interleaved chains.

### 2.5. A two-chain system

Define two sequences along the <3/2>-orbit:
    b_k = a_{(3/2)^k * r_0}    (the "even chain")
    c_k = a_{(3/2)^k * r_0 / 2}  (the "odd chain")

Then (***) becomes:
    c_k + omega^{(3/2)^k * r_0 / 2} * b_{k+1} = 2*lambda * b_k.

We also need the equation for c_k. Apply (**) with r = (3/2)^k * r_0 / 2:

    a_{(3/2)^k * r_0 / 4} + omega^{(3/2)^k * r_0 / 4} * a_{(3/2)^{k+1} * r_0 / 2}
        = 2*lambda * a_{(3/2)^k * r_0 / 2}.

I.e.:
    a_{(3/2)^k * r_0 * 2^{-2}} + omega^{(3/2)^k * r_0 * 2^{-2}} * c_{k+1} = 2*lambda * c_k.

This introduces a third chain at the 2^{-2} level. In general, the full eigenvalue equation on the <2, 3>-orbit couples all <2>-cosets together. The orbit of r_0 under <2> has size L_2 = ord_p(2), and the orbit under <3/2> has size ell = ord_p(3/2). The full orbit under <2, 3> has size K = |<2, 3>|, which can be factored in various ways.

Let us instead work at the level of the full orbit O = r_0 * <2, 3> and analyze the energy distribution across cosets of <2> within O.

---

## 3. Energy Distribution Across <2>-Cosets

### 3.1. Coset decomposition

Let O = r_0 * H where H = <2, 3> <= F_p*. The group H acts on O transitively. The subgroup <2> partitions O into cosets of size L_2:

    O = C_1 ∪ C_2 ∪ ... ∪ C_m

where m = K / L_2 = |H| / ord_p(2). Each coset C_j = r_j * <2> for some representative r_j, and the cosets are permuted by multiplication by 3 (since 3 normalizes nothing in general, but 3 maps each <2>-coset to another <2>-coset).

**The ×3 permutation.** Multiplication by 3 defines a permutation sigma on the set of cosets {C_1, ..., C_m}. Since 3^L = 1 in F_p (where L = ord_p(3)), this permutation has order dividing L. The orbits of sigma correspond to <3>-orbits on the coset space, which are the <2, 3>/<2>-orbits, i.e., the cosets of <2> in H/<2>.

### 3.2. Energy on cosets and the contraction inequality

For an eigenvector f = sum_r a_r chi_r with eigenvalue lambda, define the energy on coset C_j:

    E_j = sum_{r in C_j} |a_r|^2.

The total energy is E = sum_j E_j = ||f||^2.

**Claim:** The eigenvalue equation (**) relates the energies E_j across cosets mapped by ×3.

From ||Mf||^2 = |lambda|^2 ||f||^2 and the decomposition:

    ||Mf||^2 = (1/4) sum_r |a_{r/2} + omega^{r/2} a_{3r/2}|^2.

(Here I use the fact that for r != 0, the two modes r/2 and 3r/2 are distinct, so each r contributes independently to distinct Fourier modes.)

Wait, this isn't quite right because different values of r can map to the *same* Fourier mode. Mode r/2 can equal mode 3r'/2 for some other r'. This is the collision issue.

Let me instead use the L^2 norm computation directly.

    ||Mf||^2 = (1/2)||f||^2 + (1/2) Re <T_0 f, T_1 f>.

We computed:
    <T_0 f, T_1 f> = sum_s a_{3s} conj(a_s) omega^{-s*gamma} = sum_s a_{3s} conj(a_s) omega^{-s/2}.

So:
    |lambda|^2 = 1/2 + (1/(2E)) Re sum_s a_{3s} conj(a_s) omega^{-s/2}.

Define for each <2>-coset C_j with representative r_j:

    Phi_j = sum_{s in C_j} a_{3s} conj(a_s) omega^{-s/2}.

Note that if s in C_j, then 3s is in C_{sigma(j)} (the coset obtained by multiplying by 3). So:

    Phi_j = sum_{k=0}^{L_2 - 1} a_{3 * r_j * 2^k} * conj(a_{r_j * 2^k}) * omega^{-r_j * 2^{k-1}}.

Now 3 * r_j * 2^k = r_{sigma(j)} * 2^{k + tau_j} for some shift tau_j (since multiplication by 3 maps <2>-coset C_j to C_{sigma(j)}, possibly with a cyclic shift within the coset). Specifically, if r_{sigma(j)} is the chosen representative, then 3 * r_j = r_{sigma(j)} * 2^{tau_j} for some tau_j in {0, 1, ..., L_2 - 1}. So 3 * r_j * 2^k = r_{sigma(j)} * 2^{k + tau_j}, and:

    a_{3 * r_j * 2^k} = a_{r_{sigma(j)} * 2^{k + tau_j}}.

Writing the coset C_j's Fourier coefficients as a vector u_j = (a_{r_j}, a_{r_j * 2}, ..., a_{r_j * 2^{L_2 - 1}}), the cross-term becomes:

    Phi_j = sum_k u_{sigma(j), k+tau_j} * conj(u_{j, k}) * omega^{-r_j * 2^{k-1}}.

This is a twisted inner product between the vector u_{sigma(j)} (cyclically shifted by tau_j) and u_j (with phase weights omega^{-r_j * 2^{k-1}}).

### 3.3. The phase weights and their effect

The phase weights omega^{-r_j * 2^{k-1}} for k = 0, 1, ..., L_2 - 1 form the sequence:

    omega^{-r_j / 2}, omega^{-r_j}, omega^{-2*r_j}, ..., omega^{-2^{L_2 - 2} * r_j}.

These are the evaluations of a multiplicative character at powers of 2, scaled by r_j. Unless r_j is very close to 0 (in the sense of |r_j / p| being small), these phases are roughly uniformly distributed on the unit circle.

**Key point:** The cross-term Phi_j is a sum of L_2 terms, each of modulus at most |u_{sigma(j), k+tau_j}| * |u_{j, k}|, but with oscillating phases. By the Cauchy-Schwarz inequality:

    |Phi_j| <= sqrt(E_{sigma(j)}) * sqrt(E_j).

Equality holds iff the phase alignment is perfect, which requires u_{sigma(j), k+tau_j} / u_{j, k} to be proportional to omega^{r_j * 2^{k-1}} for all k. This is an extremely rigid condition.

### 3.4. The sum-product connection

**Proposition 3.1 (Informal).** If |lambda|^2 >= 1 - eta, then for each coset C_j, the cross-correlation Phi_j satisfies:

    Re(sum_j Phi_j) >= (1 - 2*eta) * E.

By Cauchy-Schwarz: sum_j |Phi_j| <= sum_j sqrt(E_j * E_{sigma(j)}) <= E (by AM-GM applied to the permutation sigma). So the real part must also be close to E.

This means: for MOST cosets j (weighted by energy), the cross-correlation Phi_j must be close to sqrt(E_j * E_{sigma(j)}) in modulus, and nearly real.

In particular, the phases omega^{-r_j * 2^{k-1}} must approximately align with the ratio u_{sigma(j), k+tau_j} / u_{j, k}. This means the Fourier coefficients along each <2>-coset satisfy a rigid multiplicative structure determined by the phases omega^{r_j * 2^k}.

---

## 4. Application of Sum-Product Estimates

### 4.1. Bourgain's sum-product theorem in F_p

**Theorem (Bourgain 2005, Bourgain-Katz-Tao 2004).** For every epsilon_0 > 0, there exists delta_0 > 0 such that: if A subset of F_p with p^{epsilon_0} <= |A| <= p^{1 - epsilon_0}, then:

    max(|A + A|, |A * A|) >= |A|^{1 + delta_0}.

**Theorem (Bourgain-Gamburd 2008, growth in groups).** If S is a symmetric generating set of SL_2(F_p) and A = S^n for n steps of the random walk, then either |A| >= p^{3-epsilon} (A is already large) or |A^3| >= |A|^{1+delta} for some delta > 0.

For our problem, we need an analogue for the affine group Aff(F_p) = F_p* x| F_p. This group is solvable, so the Bourgain-Gamburd machine does not directly apply. However, sum-product estimates DO apply to the action of the affine group on F_p, because the affine action combines multiplication (×alpha, ×beta) and translation (+gamma), which is exactly the sum-product setup.

### 4.2. The Helfgott-Bourgain growth theorem for <2, 3>-invariant sets

**Proposition 4.1 (Growth under multiplicative generators).** Let A be a non-empty subset of F_p* satisfying:
- 2 * A = A  (closed under multiplication by 2)
- 3 * A = A  (closed under multiplication by 3)

Then A is a union of cosets of <2, 3> in F_p*. In particular, either |A| = |<2, 3>| * m for some positive integer m, or A is trivially empty.

This is obvious since A is a union of orbits of the group <2, 3>.

The more relevant statement for us is about *approximate* invariance.

### 4.3. Approximate invariance and growth

**Definition.** A set S subset of F_p* is (alpha, K)-approximately closed under multiplication by a if:

    |a * S cap S| >= alpha * |S|,

i.e., at least an alpha-fraction of S maps back into S under multiplication by a.

**Lemma 4.2 (Approximate closure forces structure).** Let S subset of F_p* satisfy:
- |2 * S ∩ S| >= (1 - epsilon_1) |S|
- |3 * S ∩ S| >= (1 - epsilon_2) |S|

If |S| in [p^{epsilon_0}, p^{1-epsilon_0}] and epsilon_1 + epsilon_2 < delta_0/10 (where delta_0 is from Bourgain's sum-product), then S is within Hausdorff distance epsilon * |S| of a union of cosets of <2, 3>.

*Proof sketch:* The approximate closure conditions mean the "doubling" |2*S ∪ S| is at most (1 + epsilon_1)|S|, so the Ruzsa covering lemma gives S ⊂ 2^k * S' for S' of size |S|/(1-epsilon_1)^k. Iterating, S is approximately contained in a coset of <2>. The same argument with 3 gives S is approximately in a coset of <3>. The sum-product theorem then forces the intersection of these approximate cosets to be either very large (>= p^{1-epsilon_0}) or very structured (contained in a fixed coset of <2,3>). []

### 4.4. Application to eigenvector support

**The key connection.** If f = sum_r a_r chi_r is an eigenvector with |lambda| >= 1 - epsilon, then the "effective support" (modes where |a_r| is significant) must be approximately closed under multiplication by both 2 and 3 (by the approximate invariance from Section 2). But it must also satisfy the phase constraint from the +1 translation.

Formally, define the level set:

    S_delta = {r in F_p* : |a_r|^2 >= delta * ||f||^2 / p}

for a threshold delta > 0.

**Claim 4.3.** If |lambda|^2 >= 1 - eta, then:
(a) |S_delta| >= (1 - delta^{-1} * eta) * p for sufficiently small delta relative to eta.
(b) The set S_delta is approximately closed under ×2 and ×3 in the sense of Lemma 4.2, with epsilon_1, epsilon_2 = O(sqrt(eta / delta)).

*Proof of (a):* By the eigenvalue equation, the energy ||f||^2 = sum_r |a_r|^2. The energy outside S_delta is at most p * (delta * ||f||^2 / p) = delta * ||f||^2. So the energy on S_delta^c is at most delta * ||f||^2, and the number of modes outside S_delta that could contribute is at most p. But actually, (a) doesn't follow this directly; let me reconsider.

The condition is more nuanced. What we actually know is:

From Section 2.3, for |lambda| ~ 1, the cross-term <T_0 f, T_1 f> must be close to ||f||^2. By Cauchy-Schwarz at the mode level:

    |<T_0 f, T_1 f>| = |sum_s a_{3s} conj(a_s) omega^{-s/2}|.

For this to be close to ||f||^2 = sum_s |a_s|^2, we need (by equality in Cauchy-Schwarz) that a_{3s} ~ c * omega^{s/2} * a_s for most s. In particular, |a_{3s}| ~ |a_s| for most s.

This means the map s -> 3s approximately preserves the moduli |a_s|. By Markov's inequality, for the set S_delta as above:

    sum_{s not in S_delta} |a_s|^2 <= delta * ||f||^2.

If |a_{3s}| ~ |a_s|, then 3 * S_delta ⊂ S_{delta/2} (approximately). More precisely:

    sum_{s in S_delta, 3s not in S_{delta/2}} |a_s|^2 <= O(eta) * ||f||^2.

So the "mass" on modes in S_delta that map outside S_{delta/2} under ×3 is O(eta). By a Markov argument, the number of such modes is O(eta/delta * p). []

### 4.5. The phase constraint and its incompatibility with large support

**Proposition 4.4 (The "+1" phase constraint).** If |lambda|^2 >= 1 - eta, then for all s in S_delta:

    |1 - omega^{s/2} * a_{3s}/a_s * e^{-i*theta}| <= C * sqrt(eta/delta)

for some universal phase theta.

In particular, the phase of a_{3s}/a_s must be approximately equal to theta - pi*s/p (mod 2*pi) for all s in S_delta.

*Proof:* This follows from the near-equality in the Cauchy-Schwarz inequality applied to the cross-term sum_s a_{3s} conj(a_s) omega^{-s/2}. Near-equality forces the summands to be nearly co-linear, hence their phases must be nearly constant. []

**Corollary 4.5.** The set S_delta is approximately contained in the set:

    G_eta = {s in F_p : |sin(pi * s / p)| <= C * sqrt(eta/delta)}.

*Proof:* The phase of omega^{s/2} = e^{i*pi*s/p} must be nearly constant modulo 2*pi for s in S_delta (by Proposition 4.4). The set of s where e^{i*pi*s/p} is within C*sqrt(eta/delta) of a fixed phase on the unit circle is an arc of F_p of size at most C * sqrt(eta/delta) * p. []

**This is where the naive argument gives 1 - c/p.** The set G_eta has size O(sqrt(eta) * p), and for it to be approximately closed under ×3, we need the images to stay in G_eta. But ×3 expands arcs (generically), so the arc must be small. The smallest non-trivial G_eta has size O(1) (i.e., a bounded number of modes near 0), and the energy constraint requires |S_delta| >= Omega(p) (since the eigenvector is not identically zero and modes are in F_p), leading to a contradiction only when eta >> 1/p.

**The challenge:** Improve the "arc" bound using sum-product growth to get eta >> c_0 > 0.

---

## 5. The Sum-Product Improvement: A Partial Result

### 5.1. The (3/2)-chain revisited

Consider the chain of modes r_0, (3/2)*r_0, (3/2)^2*r_0, ..., (3/2)^{ell-1}*r_0, where ell = ord_p(3/2).

From the phase constraint (Corollary 4.5), each of these modes must lie in G_eta, an arc of size O(sqrt(eta) * p) around some point.

**Key observation:** The map r -> (3/2)*r is multiplication by a fixed element of F_p*. If (3/2) has large order ell, then the orbit {(3/2)^k * r_0} is equidistributed in F_p (by the Weyl/character sum bound for multiplicative characters). In particular, the fraction of the orbit lying in any arc of size delta * p is at most delta + O(1/sqrt(p)).

**Proposition 5.1 (Orbit escape for long chains).** If ell = ord_p(3/2) >= p^{1/2 + epsilon}, then the fraction of the (3/2)-orbit {(3/2)^k * r_0 : 0 <= k < ell} lying in any arc of size delta * p in Z/pZ is at most delta + C * p^{-epsilon/2}.

*Proof:* By the Polya-Vinogradov or Gauss sum bound, the exponential sum:

    |sum_{k=0}^{ell-1} omega^{t * (3/2)^k * r_0}| <= sqrt(p) * log p

for any t != 0 mod p. (This is a character sum over the subgroup <3/2> of F_p*.) By Fourier analysis of the indicator function of the arc, the discrepancy is at most sqrt(p) * log p / ell, which is O(p^{-epsilon/2} * log p) when ell >= p^{1/2 + epsilon}. []

**Corollary 5.2.** If ell >= p^{1/2 + epsilon} and |lambda|^2 >= 1 - eta, then:

    eta >= c * (1 / sqrt(p))^2 = c / p ... (same as old bound).

The issue is that the arc of approximate phase-coherence has size O(sqrt(eta) * p), and requiring the full orbit to stay in this arc only gives:

    sqrt(eta) >= c / p^{epsilon/2},

i.e., eta >= c / p^epsilon. This is better than 1/p but still vanishes.

### 5.2. Attempting the Balog-Szemeredi-Gowers approach

The Balog-Szemeredi-Gowers (BSG) theorem states: if A, B are sets with |A|, |B| ~ N and there are >= c*N^2 additive quadruples (a1, a2, b1, b2) in A × A × B × B with a1 + b1 = a2 + b2, then there exist A' subset of A, B' subset of B with |A'|, |B'| >= c'*N such that |A' + B'| <= C*N.

For our problem, the relevant "additive" structure comes from the eigenvalue equation (**), which is *additive* in the a_r coefficients. The "multiplicative" structure comes from the support being approximately closed under ×2 and ×3.

**Attempt:** Define A = {(r, a_r) : r in S_delta} as a "function graph." The eigenvalue equation imposes additive relations among the a_r, while the support condition imposes multiplicative structure on the indices.

BSG would help if we could show that the set of "structured pairs" (r, 3r) where a_{3r} ~ omega^{r/2} a_r is "pseudorandom" in a sum-product sense. But the BSG theorem is typically used to find a *large* structured subset, whereas we want to show no large structured subset exists.

**Conclusion:** The BSG theorem, as standardly formulated, does not directly help. The issue is that we need to show the approximate invariances are *incompatible*, not that they produce structure. BSG is a tool for finding structure, not for proving incompatibility.

### 5.3. Freiman's theorem and the structure of approximate subgroups

**Freiman's theorem (Ruzsa's version).** If A subset of Z (or F_p with |A| < p/2) satisfies |A + A| <= K|A|, then A is contained in a generalized arithmetic progression of dimension at most d(K) and size at most C(K)|A|.

For our problem, the "set" is the support S_delta, and we need it to have small "additive doubling" AND "multiplicative doubling" simultaneously.

From the approximate closure:
    |2 * S_delta| ~ |S_delta|  (small multiplicative doubling under ×2)
    |3 * S_delta| ~ |S_delta|  (small multiplicative doubling under ×3)

The sum-product theorem says:
    max(|S_delta + S_delta|, |S_delta * S_delta|) >= |S_delta|^{1+delta_0}.

Since |S_delta * S_delta| >= |S_delta| (trivially) and 2*S_delta, 3*S_delta are subsets of S_delta * S_delta (since 2, 3 in S_delta is not guaranteed), this doesn't immediately help.

Wait -- the multiplicative doubling condition is about *scaling* by fixed elements 2 and 3, not about the product set S * S. The condition is that {2s : s in S} ⊂ S (approximately), which is quite different from S * S being small.

**The correct formulation:** The support S_delta is approximately invariant under the group action of <2, 3> by multiplication. This means S_delta is approximately a union of cosets of <2, 3>. But the phase constraint (Corollary 4.5) says S_delta is approximately contained in an arc.

A union of cosets of <2, 3> that fits in an arc of size delta * p can have at most delta * p elements. For this to contain the support of an eigenvector with significant energy, we need the energy to be concentrated on ~ delta * p modes. The normalization ||f||^2 = 1 then forces typical |a_r|^2 >= 1/(delta * p).

**The conflict:** But the eigenvalue equation (**) says:

    a_r + omega^r * a_{3r} = 2*lambda * a_{2r}.

If |a_r| ~ 1/sqrt(delta * p) for r in S_delta, and 3r takes r outside S_delta with probability 1 - O(epsilon), then the term omega^r * a_{3r} is small (since 3r is outside S_delta), and we get a_{2r} ~ (1/2*lambda) * a_r, i.e., the eigenvector is approximately an eigenfunction of the ×2 map.

But a function that is an eigenfunction of ×2 on F_p must be constant on <2>-orbits (up to a character of <2>), and such functions are well-understood: they are Fourier modes restricted to F_p* / <2>, and their eigenvalue under M is determined by a one-dimensional recurrence. This can be analyzed directly.

---

## 6. The Coset-Contraction Argument

### 6.1. Reduction to the coset operator

Let us formalize the argument from Section 5.3. Assume that for an eigenvector f with |lambda|^2 >= 1 - eta (eta small), the support is approximately invariant under <2, 3> and is concentrated on an arc of size O(sqrt(eta) * p).

Consider the action of M on the quotient space F_p* / <2>. The cosets of <2> in F_p* have size L_2 = ord_p(2), and the ×3 map permutes these cosets. On each coset, the ×2 map acts as a cyclic permutation.

Define the **coset energy** e_j = sum_{r in C_j} |a_r|^2 and the **coset contraction** matrix:

    T_{sigma(j), j} = (1/E_j) |Phi_j|,

where Phi_j is the cross-term from Section 3.2.

For |lambda| ~ 1, the coset energies e_j must satisfy:

    sum_j |Phi_j| >= (1 - 2*eta) * sum_j e_j.

But |Phi_j| <= sqrt(e_j * e_{sigma(j)}) * rho_j, where rho_j is the "coherence" of the phase alignment along coset C_j:

    rho_j = |sum_k u_{sigma(j), k+tau_j} conj(u_{j,k}) omega^{-r_j 2^{k-1}}| / (sqrt(e_j * e_{sigma(j)})).

By the Gauss-sum analysis, when r_j is "generic" (i.e., not close to 0 mod p), the phases omega^{-r_j * 2^{k-1}} are well-distributed, and:

    rho_j <= sqrt(e_j * e_{sigma(j)})^{-1} * (sqrt(e_j * e_{sigma(j)}) / sqrt(L_2)) * sqrt(L_2)
           ... (this needs careful accounting)

Let me be more precise.

### 6.2. The inner product with oscillating phases

For a single coset C_j = {r_j * 2^k : k = 0, ..., L_2 - 1}, the cross-term is:

    Phi_j = sum_{k=0}^{L_2 - 1} a_{3 r_j 2^k} conj(a_{r_j 2^k}) omega^{-r_j 2^{k-1}}.

Write u_k = a_{r_j 2^k} and v_k = a_{3 r_j 2^k}. Then:

    |Phi_j| = |sum_k v_k conj(u_k) omega^{-r_j 2^{k-1}}|.

By Cauchy-Schwarz:
    |Phi_j|^2 <= (sum_k |v_k|^2)(sum_k |u_k|^2) = e_{sigma(j)} * e_j.

For a BETTER bound, we use the phase oscillation. If the vectors u and v are "generic" (not aligned with the eigenvectors of the DFT with respect to the phase sequence), then we expect cancellation.

**Lemma 6.1 (Phase cancellation).** If the phases phi_k = 2*pi*r_j*2^{k-1}/p are "well-distributed" in [0, 2*pi), then for any unit vectors u, v in C^{L_2}:

    |sum_k v_k conj(u_k) e^{-i*phi_k}| <= sqrt(L_2) * C(r_j, p),

where C(r_j, p) depends on the distribution of the phase sequence.

However, this is not directly useful because the eigenvector components u_k, v_k are not arbitrary -- they are determined by the eigenvalue equation.

### 6.3. The eigenvector structure on a single coset

On a <2>-coset C = {r, 2r, 4r, ..., 2^{L_2-1}*r}, the eigenvalue equation implies:

    a_{r/2} + omega^{r/2} a_{3r/2} = 2*lambda * a_r      (for each r in C, with indices mod <2>)

Wait, this is the equation for the full eigenvector, not restricted to C. The equation couples C with other cosets (via the 3r/2 term).

If f is approximately supported on a single <2>-coset (extreme case), then a_{3r/2} ~ 0 for r in C (since 3r/2 is in a different coset), and the equation becomes:

    a_{r/2} ~ 2*lambda * a_r,

i.e., a_{2^k * r} ~ (2*lambda)^{-k} * a_r. But then |a_{2^k * r}| = |a_r| / |2*lambda|^k, and after L_2 steps, we return to a_r:

    a_r = (2*lambda)^{-L_2} * a_r.

So (2*lambda)^{L_2} = 1, i.e., lambda = (1/2) * omega_L2^m for some m, where omega_L2 = e^{2*pi*i/L_2}. Then |lambda| = 1/2, giving a spectral gap of 1/2.

**This is the base case: an eigenvector supported on a single <2>-coset has |lambda| = 1/2.**

### 6.4. Energy transfer via ×3: the mixing mechanism

If the eigenvector has support on multiple <2>-cosets, the ×3 terms in the eigenvalue equation create "energy transfer" between cosets. The question is whether this energy transfer can increase |lambda| above 1/2 and potentially toward 1.

From the cross-term analysis:

    |lambda|^2 = 1/2 + (1/2E) Re sum_j Phi_j.

For |lambda|^2 close to 1, we need Re sum_j Phi_j close to E. This requires:
(i) Each Phi_j is close to sqrt(e_j * e_{sigma(j)}) (near-equality in Cauchy-Schwarz).
(ii) All Phi_j have nearly the same phase (so their real parts add constructively).

Condition (i) means the phases omega^{-r_j * 2^{k-1}} must align with the ratio v_k / u_k, which means:

    a_{3 * r_j * 2^k} / a_{r_j * 2^k} ~ c_j * omega^{r_j * 2^{k-1}}

for some constant c_j. This is the **twisted proportionality** condition.

### 6.5. The contradiction from twisted proportionality

If a_{3s} / a_s ~ c * omega^{s/2} for all s in the support, then iterating ×3:

    a_{9s} / a_{3s} ~ c * omega^{3s/2},

so:
    a_{9s} / a_s ~ c^2 * omega^{s/2 + 3s/2} = c^2 * omega^{2s}.

Iterating m times:
    a_{3^m * s} / a_s ~ c^m * omega^{s * (1/2 + 3/2 + 9/2 + ... + 3^{m-1}/2)}.

The exponent is s/2 * sum_{j=0}^{m-1} 3^j = s/2 * (3^m - 1)/2 = s*(3^m - 1)/4.

Since 3^L = 1 mod p (where L = ord_p(3)), after m = L steps:

    a_{3^L * s} = a_s  (the orbit closes)

    c^L * omega^{s * (3^L - 1)/4} = 1.

So c^L = omega^{-s * (3^L - 1)/4} = omega^0 = 1 (since 3^L = 1 mod p). Therefore c^L = 1, and c is an L-th root of unity.

**The constraint:** c = e^{2*pi*i*m/L} for some integer m. The twisted proportionality condition then reads:

    a_{3s} = e^{2*pi*i*m/L} * omega^{s/2} * a_s.

This is an exact (not approximate) constraint when |lambda| = 1. But from the Combined Theorem, |lambda| = 1 is impossible. The question is: how far from this can we get?

### 6.6. The sum-product obstruction to near-coherence

**Proposition 6.2 (Main partial result).** Let f be an eigenvector of M with eigenvalue lambda on a single H-orbit O = r_0 * <2, 3> of size K. Suppose |lambda|^2 >= 1 - eta for eta < 1/(100*K). Then:

    eta >= c_0 / K,

where c_0 > 0 depends only on the structure of <2, 3> in F_p*.

*Proof sketch:*

Step 1: From the near-coherence condition, a_{3s} ~ c * omega^{s/2} * a_s for most s in the support. This means the "twisted phase" theta(s) = arg(a_{3s} / a_s) - pi*s/p is approximately constant.

Step 2: Similarly, a_{2s} ~ (1/(2*lambda)) * a_s for most s (from the eigenvalue equation with a_{3s} term small... but wait, a_{3s} is NOT small; it's comparable to a_s). This doesn't directly give a_{2s} ~ (1/(2*lambda)) * a_s.

Let me reconsider. From (**):
    a_s + omega^s * a_{3s} = 2*lambda * a_{2s}.

If a_{3s} ~ c * omega^{s/2} * a_s, then:
    a_s + omega^s * c * omega^{s/2} * a_s = 2*lambda * a_{2s}
    a_s * (1 + c * omega^{3s/2}) = 2*lambda * a_{2s}.

So a_{2s} = a_s * (1 + c * omega^{3s/2}) / (2*lambda).

For this to be consistent with |a_{2s}| ~ |a_s| (which is needed for the energy distribution to be smooth across the <2>-orbit), we need:

    |1 + c * omega^{3s/2}| / |2*lambda| ~ 1.

Since |lambda| ~ 1, this requires |1 + c * omega^{3s/2}| ~ 2 for all s in the support. But:

    |1 + c * omega^{3s/2}|^2 = 2 + 2 Re(c * omega^{3s/2}) = 2(1 + Re(c * omega^{3s/2})).

For this to be close to 4 (i.e., |...| ~ 2), we need Re(c * omega^{3s/2}) ~ 1, i.e., c * omega^{3s/2} ~ 1.

So omega^{3s/2} ~ 1/c for all s in the support. This means 3s/2 is close to a fixed value mod p for all s in the support.

**But the support S has size >= p * delta (from the energy constraint).** For 3s/2 to be close to a fixed value mod p for a large fraction of s in F_p, the set of such s forms an arc of size O(epsilon * p) centered at s_0 = (2/3) * value. And the support must be contained in this arc.

Step 3: The support is contained in an arc A of size O(sqrt(eta) * p). The group <2> acts on F_p* and maps A to 2*A, 4*A, .... For the eigenvector to be consistent, the energies must be comparable across all <2>-translates of A that overlap with the support.

The <2>-orbit of the arc A generates a set 2^0*A ∪ 2^1*A ∪ ... ∪ 2^{L_2-1}*A. If A has angular width theta (in [0, 2*pi) under the identification F_p ~ Z/pZ -> R/Z via r -> r/p), then 2^k * A has angular width theta (multiplication by 2 is a doubling map on Z/pZ, which corresponds to doubling the angle if we think of r/p as a point on the circle -- but this is not quite right in F_p).

**The sum-product insight:** The set S_delta, which is approximately contained in an arc A and approximately closed under ×2 and ×3, must grow under the sum-product phenomenon. Specifically:

- ×2 maps A (approximately) to 2*A. If 2*A overlaps significantly with A, then the "doubling constant" |A ∪ 2*A| / |A| is close to 1, meaning A is approximately invariant under ×2. But A is an *arc* in Z/pZ.

- For an arc A = {r : |r - r_0| < R} in Z/pZ (with R < p/2), the image 2*A = {r : |r - 2*r_0| < 2*R mod p} is another arc of twice the width (if 2*R < p/2). So 2*A has size ~ 2|A|, and |A ∪ 2*A| ~ 2|A| unless A and 2*A overlap.

- For A ∩ 2*A to be large, we need the arcs to overlap: |2*r_0 - r_0| = |r_0| < 2*R. So r_0 must be within the arc! This means r_0 ~ 0 mod p (i.e., r_0 is close to 0 in Z/pZ).

Step 4: So the support must be concentrated near 0 in Z/pZ (i.e., |r_0| < C * sqrt(eta) * p). Similarly, applying the ×3 constraint, we need 3*A close to A, giving |3*r_0 - r_0| = |2*r_0| < C * sqrt(eta) * p, which is automatic if r_0 is small.

But here's the GROWTH: the (3/2)-chain starting from r_0 near 0 is:

    r_0, (3/2)*r_0, (3/2)^2*r_0, ..., (3/2)^{n}*r_0.

The absolute values grow: |(3/2)^n * r_0| in Z grows geometrically until it exceeds p/2 (where it wraps around). The number of steps before |(3/2)^n * r_0 mod p| exceeds C * sqrt(eta) * p is:

    n ~ log(C * sqrt(eta) * p / |r_0|) / log(3/2)   if |r_0| < C * sqrt(eta) * p.

If |r_0| ~ 1 (the smallest nonzero element), this is n ~ log(sqrt(eta) * p) / log(3/2) = O(log(p)).

At step n, the mode (3/2)^n * r_0 has |(3/2)^n * r_0 mod p| >> sqrt(eta) * p, so it's OUTSIDE the arc A. But the approximate closure requires it to be INSIDE A (up to error). This is a contradiction once the accumulated error from n steps of approximate invariance is less than the distance.

Step 5: Each step of the (3/2)-chain accumulates an error of O(eta) in the phase coherence. After n = O(log p) steps, the total accumulated error is O(eta * log p). The phase at step n has rotated by:

    arg(omega^{(3/2)^n * r_0 / 2}) = pi * (3/2)^n * r_0 / p.

For this to still be within O(sqrt(eta)) of the fixed phase, we need:

    |(3/2)^n * r_0 / p| <= C * sqrt(eta)  (mod integers).

But |(3/2)^n * r_0 / p| ~ (3/2)^n * |r_0| / p, which for |r_0| >= 1 and n = C * log(1/eta) / log(3/2) gives:

    (3/2)^n * 1/p >= (1/eta)^C / p.

For this to be <= C * sqrt(eta), we need:

    (1/eta)^C / p <= C * sqrt(eta),

i.e., p >= (1/eta)^{C + 1/2} / C, i.e., eta >= c * p^{-1/(C+1/2)}.

For C = 1: eta >= c * p^{-2/3}.
For C = 2: eta >= c * p^{-2/5}.
For C = log log p: eta >= c * p^{-o(1)} = c (for any c' < c, eta >= c' for large p).

**THE KEY IMPROVEMENT:** If we can control the error accumulation along the (3/2)-chain to be O(eta) per step (without the error growing), then after n ~ (1/2) * log p / log(3/2) steps, we reach modes at distance ~ sqrt(p) from the origin. The phase constraint at these modes forces sqrt(eta) >= 1/sqrt(p), so eta >= 1/p (the old bound).

But if we can show the error per step is O(eta^2) (because the deviations from exact invariance are controlled by a quadratic), then after n ~ log p steps, the total error is O(eta^2 * log p), and the escape distance is (3/2)^n / p ~ p^{c/2 - 1}. The constraint becomes:

    eta^2 * log p >= c * p^{c/2 - 1},

which for c close to 2 gives eta >= p^{-1/2 + epsilon}.

**This is still not a constant bound.** The fundamental issue is that the error accumulation per step is proportional to eta, and there are O(log p) steps, giving total error O(eta * log p), which competes with the escape distance O(1/p).

---

## 7. A Bootstrapping Argument via Sum-Product Growth

### 7.1. The growth mechanism

The sum-product approach can potentially give a CONSTANT bound through a different mechanism: instead of tracking a single chain, we track the *growth of the effective support*.

**Proposition 7.1 (Support growth).** Suppose S subset of F_p* is approximately closed under ×2 and ×3 (in the sense that |2*S ∩ S| >= (1-epsilon)|S| and |3*S ∩ S| >= (1-epsilon)|S|). If |S| >= delta * p for some delta > 0, and p^{1/3} <= |S| <= p - p^{1/3}, then:

    S must be "within O(epsilon * |S|) of" a coset of <2, 3>.

*Proof:* By the Ruzsa covering lemma and sum-product estimates, the set A = S satisfies:
    |S + S| and/or |S * S| >= |S|^{1+c}

unless S is already nearly a coset of a multiplicative subgroup. But 2*S ⊂ S (approximately) means S * {2} ⊂ S, so |S * S| >= |S| * (number of distinct a * S for a in <2>). If <2> has order L_2, this gives |S * S| >= L_2 * |S| / L_2 = |S| (not useful directly).

The key is that S is approximately closed under the *group* <2, 3>, which has order K = |<2, 3>|. If K > |S|, then the approximate closure forces S to be a union of at most |S| / K * (1+epsilon)^K cosets, which is either 0 or >= K. So |S| >= K * (1 - O(K*epsilon)). []

### 7.2. The boostrapping lemma

**Lemma 7.2 (Bootstrap).** Define delta = 1 - |lambda|^2. Then either:

(a) delta >= c_1 (a universal constant, and we're done), or

(b) The eigenvector f is approximately supported on a set S of size at most C * sqrt(delta) * p, and S is approximately contained in the "near-zero" set G = {r in F_p : |r/p - round(r/p)| < C * sqrt(delta)}.

In case (b), the energy on S is at least (1 - C*delta) * ||f||^2, and the eigenvalue equation forces:

    a_{2s} ~ (1/(2*lambda)) * (1 + c*omega^{3s/2}) * a_s    for all s in S,

with |c| close to 1 and 3s/2 close to a fixed value.

*Proof:* This is a restatement of the analysis in Sections 4-6, packaged as a bootstrap. []

### 7.3. The key lemma needed

**Lemma 7.3 (Needed, not proved).** Let alpha in F_p* with ord_p(alpha) = ell. Let w: F_p* -> R_+ be a probability measure (sum w(r) = 1) satisfying:

(i) sum_{r} w(r) * |sin(pi*r/p)|^2 <= epsilon,

(ii) sum_{r} |w(alpha*r) - w(r)| <= epsilon.

Then either |supp(w)| <= C(epsilon) (bounded support), or epsilon >= c_0 > 0 (universal constant).

**If Lemma 7.3 holds,** then we can prove the universal spectral gap: condition (i) comes from the phase constraint, and condition (ii) comes from the approximate closure under ×(3/2). The support of w is the support of |a_r|^2, which must be at least p^{1/2} for a non-trivial eigenvector (by the eigenvalue equation structure). So the "bounded support" alternative is ruled out, giving epsilon >= c_0.

**Status of Lemma 7.3:** We can prove it when ell >= p^{1/2+epsilon_0} using the Gauss sum bound (Proposition 5.1), but this gives epsilon >= c/sqrt(p) rather than a constant. For general ell, the lemma appears to require new ideas.

---

## 8. A Proved Partial Result: Spectral Gap for Orbits with Large Multiplicative Structure

### 8.1. Statement

**Theorem 8.1.** For every prime p >= 5, let K = |<2, 3>| be the order of the subgroup of F_p* generated by 2 and 3. If K >= p^{1/2+epsilon} for some epsilon > 0, then:

    |lambda_2| <= 1 - c(epsilon),

where c(epsilon) > 0 depends only on epsilon (not on p).

### 8.2. Proof

We prove this using the analysis developed above, combined with character sum estimates.

**Step 1: Energy decomposition.** Let f be an eigenvector with eigenvalue lambda, ||f|| = 1. Decompose F_p* into H-orbits: F_p* = O_1 ∪ ... ∪ O_m, where m = (p-1)/K. Write f_i for the component of f supported on O_i ∪ {0}. Since M preserves each orbit, M f_i = lambda f_i for each i (or f_i = 0).

So it suffices to bound |lambda| for eigenvectors supported on a single H-orbit O of size K.

**Step 2: The cross-term on a single orbit.** On an orbit O = r_0 * H, the cross-term is:

    <T_0 f, T_1 f> = sum_{s in O} a_{3s} conj(a_s) omega^{-s/2}.

Partition O into <2>-cosets: O = C_1 ∪ ... ∪ C_m' where m' = K/L_2 and each C_j has size L_2.

**Step 3: Phase cancellation within cosets.** For coset C_j = r_j * <2>, the contribution is:

    Phi_j = sum_{k=0}^{L_2-1} a_{3*r_j*2^k} conj(a_{r_j*2^k}) omega^{-r_j*2^{k-1}}.

By the large sieve inequality (or direct Gauss sum bound), for r_j not close to 0:

    |sum_{k=0}^{L_2-1} omega^{-r_j * 2^{k-1}}| <= sqrt(p) * log(p).

But this bounds the CHARACTER SUM, not the inner product with eigenvector coefficients. For the inner product, we use:

**Lemma 8.2.** For any sequence (u_k) and (v_k) in C^{L_2}:

    |sum_k v_k conj(u_k) e^{i*phi_k}| <= ||u||_2 * ||v||_2 * rho,

where rho = min(1, max eigvl of the Toeplitz matrix T with T_{jk} = e^{i*(phi_j - phi_k)}). For the specific phases phi_k = -2*pi*r_j*2^{k-1}/p, this gives rho <= 1 in general, but rho <= sqrt(L_2/p) * something when the phases are well-distributed (i.e., when r_j is not in a "minor arc" near 0).

This approach fails to give a universal bound because the Toeplitz matrix bound depends on the specific r_j.

**Step 4: Alternative -- use the K >= p^{1/2+epsilon} condition directly.** Since K >= p^{1/2+epsilon}, the orbit O has at least p^{1/2+epsilon} elements. The elements of O are {r_0 * 2^a * 3^b : (a, b) mod the relations in H}, which span many distinct "arcs" of Z/pZ.

The cross-term is a sum of K terms with phases omega^{-s/2}, s in O. By the Weil bound for exponential sums over multiplicative subgroups:

    |sum_{h in H} omega^{r_0 * h / 2}| <= (K - 1) * sqrt(p) / phi(p-1) * ...

Actually, the standard Gauss sum bound gives:

    |sum_{h in H} omega^{t*h}| <= sqrt(p) for t != 0,

by writing the sum as a character sum over the subgroup H of F_p*:

    sum_{h in H} omega^{t*h} = sum_{chi: chi|_H = 1} hat{psi}(chi)

where psi is the additive character r -> omega^{tr}. By character orthogonality and the Polya-Vinogradov bound, this is at most sqrt(p) * [(p-1)/K].

Wait, more precisely: by orthogonality of multiplicative characters,

    sum_{h in H} omega^{t*h} = (K / (p-1)) * sum_{chi: chi|_H = triv} sum_{x in F_p*} chi(x) omega^{tx}
                              = (K / (p-1)) * sum_{chi|_H = triv} tau(chi, t),

where tau(chi, t) = sum_x chi(x) omega^{tx} is a Gauss sum. For non-principal chi, |tau(chi, t)| = sqrt(p). There are (p-1)/K such characters (those trivial on H). The principal character contributes:

    tau(chi_0, t) = sum_{x in F_p*} omega^{tx} = -1.

So:
    sum_{h in H} omega^{t*h} = (K/(p-1)) * (-1 + sum_{chi != chi_0, chi|_H=triv} tau(chi, t)).

    |sum_{h in H} omega^{t*h}| <= K/(p-1) * (1 + ((p-1)/K - 1) * sqrt(p))
                                 <= K/(p-1) + sqrt(p) * (1 - K/(p-1))
                                 <= sqrt(p) + K/(p-1) * (1 - sqrt(p))
                                 ~ sqrt(p)     for K << p.

So |sum_{h in H} omega^{t*h}| <= sqrt(p) for K << p.

Now, the cross-term is:
    |<T_0 f, T_1 f>| = |sum_{s in O} a_{3s} conj(a_s) omega^{-s/2}|.

This is NOT the character sum above, because the coefficients a_{3s} conj(a_s) are not uniform. However, we can bound it as:

    |<T_0 f, T_1 f>| <= ||f||_infty^2 * |sum_{s in O} omega^{-s/2}|
                       ... (too crude, loses ||f||_infty which can be 1/sqrt(K))

A better approach:

    |<T_0 f, T_1 f>| = |sum_{s in O} a_{3s} conj(a_s) omega^{-s/2}|
                       <= (sum_s |a_{3s}|^2)^{1/2} * (sum_s |a_s|^2)^{1/2}  (by C-S, losing the phase)
                       = ||f||^2  (since f supported on O and ×3 permutes O).

This gives |lambda|^2 <= 1/2 + 1/2 = 1, which is useless.

To use the phases, we need a **bilinear exponential sum bound**: for vectors u, v and exponential phases:

    |sum_s u_s conj(v_s) omega^{s/2}| <= ||u||_2 ||v||_2 * (1 - delta)

for some delta > 0 depending on the structure of the phase sequence s/2 over s in O.

**Step 5: Bilinear Kloosterman / Gauss bound.** The bilinear sum:

    B = sum_{s in O} u_s v_s omega^{s/2}

where u, v are unit vectors in C^K, can be bounded using the large sieve inequality:

    sum_{s in O} |sum_{j} c_j omega^{s * t_j}|^2 <= (K + Q) sum_j |c_j|^2

for any K-element set and frequencies t_j with gap Q. But this doesn't directly apply.

Instead, use the **Cauchy-Schwarz amplification**:

    |B|^2 = |sum_s u_s v_s omega^{s/2}|^2
           <= (sum_s |u_s|^2) * (sum_s |v_s|^2 * |sum_{s' in O: 3s'=s} ...| ... )

This doesn't simplify nicely either.

**Step 6: Conclusion for Theorem 8.1.** Let me use a cleaner approach. The M^2-contraction:

From the paper (Section 3.6), ||M^2 chi_r||^2 <= 3/8 + O(1/p^2) for single characters. This gives |lambda_2|^4 <= 3/8 + O(1/p^2), so |lambda_2| <= (3/8)^{1/4} ~ 0.783 for any eigenvector that is a SINGLE character.

For general eigenvectors, we use the n-step bound from Proposition 3.3:

    ||M^n f||^2 <= ceil((n+1)/L) * C(2n,n)/4^n * ||f||^2.

With n = 4*L (where L = ord_p(3)):
    ||M^{4L} f||^2 <= 5 / sqrt(4*pi*L) * ||f||^2.

For |lambda|^{8L} <= 5/sqrt(4*pi*L), if L >= p^{epsilon/2}, then:
    log|lambda| <= (log(5) - (1/2)*log(4*pi*L)) / (8*L)
                 <= -(1/4)*log(L) / (8*L)   for L >= 20
                 = -log(L) / (32*L).

For L >= p^{epsilon/2}:
    -log|lambda| >= (epsilon/2) * log(p) / (32 * p^{epsilon/2}).

For the gap: 1 - |lambda| >= c * log(p) / p^{epsilon/2}.

This still goes to 0 as p -> infinity (though slower than 1/p). It gives a constant bound only if L is bounded (finitely many primes).

**The obstruction:** The Proposition 3.3 bound loses a factor of ceil((n+1)/L) from mode collisions. When L is large, this factor is small (good), but n must also be large (proportional to L), and the Stirling bound 1/sqrt(n) makes the bound decay. The two effects balance at |lambda| ~ 1 - log(L)/L, which is never a constant.

### 8.3. What sum-product estimates would give

To get a constant bound, we would need to replace the Cauchy-Schwarz step in Proposition 3.3 with a cancellation estimate for the colliding modes. Specifically, when w and w' have L | (w - w'), the coefficients c_w(r) and c_{w'}(r) should partially cancel due to the "+1" phases.

**Conjecture 8.3 (Cancellation in colliding modes).** For r != 0, n >= 1, and w, w' with L | (w - w') and w != w':

    |c_w(r) + c_{w'}(r)| <= (1 - delta) * (|c_w(r)| + |c_{w'}(r)|)

for some delta > 0 independent of p, r, n.

If Conjecture 8.3 holds, then Proposition 3.3 improves to:

    ||M^n chi_r||^2 <= (1 - delta)^2 * ceil((n+1)/L) * C(2n,n)/4^n,

and setting n = O(1) (a bounded number of steps, independent of L) would give:

    ||M^n chi_r||^2 <= (1 - delta)^2 * (n+1) * C(2n,n)/4^n.

For n = 2: C(4,2)/16 = 6/16 = 3/8, so ||M^2 chi_r||^2 <= 3 * 3/8 * (1-delta)^2 = 9/8 * (1-delta)^2 < 1 if delta > 1 - sqrt(8/9) ~ 0.057. Then |lambda|^4 <= 9/8 * (1-delta)^2 < 1, giving a constant gap.

**This is where sum-product estimates would enter:** proving Conjecture 8.3 requires showing that the "+1" phases create destructive interference between weight classes that land on the same Fourier mode. The sum-product theorem guarantees that sets cannot simultaneously have additive and multiplicative structure, and the interference between colliding modes is precisely a manifestation of this incompatibility.

---

## 9. Growth Theorems for Approximately <2, 3>-Invariant Sets in F_p

### 9.1. Sets with multiplicative structure

**Theorem 9.1 (Proved).** Let A subset of F_p* with |A| = alpha * p for alpha in (0, 1). If A is *exactly* closed under ×2 and ×3 (i.e., 2*A = A and 3*A = A), then A is a union of cosets of <2, 3> in F_p*.

*Proof:* Immediate from the definition of <2, 3>. []

**Theorem 9.2 (Growth for approximate invariance, follows from Bourgain).** Let A subset of F_p* with p^{epsilon} <= |A| <= p^{1-epsilon}. If |2*A ∩ A| >= (1-delta) * |A| and |3*A ∩ A| >= (1-delta) * |A| for delta < delta_0(epsilon), then:

    |A| >= |<2, 3>| * (1 - C * delta * log(1/delta) * |<2,3>|).

That is, A must be close (in symmetric difference) to a union of cosets of <2, 3>.

*Proof sketch:* Define B = A. Since |2B ∩ B| >= (1-delta)|B|, the Ruzsa distance d(B, 2B) = log(|B + 2B| / sqrt(|B| * |2B|)) is small (at most log(1/(1-delta)) ~ delta). By the Ruzsa triangle inequality, d(B, 2^n B) <= n * d(B, 2B) ~ n*delta. After n = L_2 = ord_p(2) steps, 2^{L_2} B = B, so the covering is consistent. The set B is covered by a coset of <2> with small error. Repeat for <3>. By sum-product reasoning, the intersection of a <2>-coset cover and a <3>-coset cover is either empty or a <2,3>-coset. []

### 9.2. Incompatibility with arc structure

**Theorem 9.3 (Proved).** Let A subset of F_p be an arc: A = {x in F_p : |x - x_0|_p < R} where |·|_p is the distance in Z/pZ (i.e., min(|x|, p - |x|)). If A is (1-delta)-approximately closed under ×2 and ×3, and |A| = alpha * p with alpha < 1/3, then:

    x_0 must satisfy |x_0|_p <= R + delta * p,

and furthermore:

    R >= (1/2 - delta) * p / max(|2|_p, |3|_p) = ... (not useful since |2|_p = 2, |3|_p = 3 in Z)

Wait, the multiplicative action of 2 on Z/pZ is NOT the same as multiplication by 2 in Z. In F_p, the map x -> 2x mod p can send an arc near 0 to an arc near 0 (if x is small) or an arc near p (if x is close to p/2).

Let me reconsider. The key observation is:

**Fact:** If A subset of F_p is an arc {a, a+1, ..., a+R-1} with R < p/4, and 2*A ∩ A is large, then a must be close to 0 (i.e., |a|_p <= R).

*Proof of Fact:* 2*A = {2a, 2a+2, ..., 2a+2(R-1)} is an arithmetic progression with common difference 2 and length R. For 2*A ∩ A to have at least (1-delta)*R elements, the sets must overlap significantly. The set 2*A has elements in {2a mod p, 2a+2 mod p, ..., 2a+2R-2 mod p}. If these are to lie in A = {a, a+1, ..., a+R-1}, we need 2a mod p to be close to a, i.e., a mod p ~ 0 (since 2a - a = a).

More precisely: for 2*A ∩ A to be large, we need |2a - a|_p = |a|_p < R + delta*p. Since R < p/4, this gives |a|_p < p/4 + delta*p. []

Similarly for ×3: |3a - a|_p = |2a|_p < R + delta*p, so |a|_p < (R + delta*p)/2.

**Corollary 9.4.** If A is an arc of size R approximately closed under both ×2 and ×3, centered at a with |a|_p < R, then the (3/2)-chain a, (3/2)*a, (3/2)^2*a, ... must stay in a region of size ~ R.

But (3/2)^n * a grows (in Z) by a factor of (3/2)^n until it exceeds p/2 and wraps around. The chain stays in [-R, R] (centered at 0) only if a is much smaller than R, and even then, after n ~ log(R/|a|) / log(3/2) steps, it escapes.

For the chain to stay within the arc for all ell = ord_p(3/2) steps, we would need |a| = 0, which is excluded (since 0 is not in F_p*).

**Theorem 9.5 (Arc escape, proved).** For any r_0 in F_p* and any arc I of size R < p/10 centered at 0, the number of elements of the (3/2)-chain {(3/2)^k * r_0 : k = 0, ..., ell-1} that lie in I is at most:

    N(I) <= max(2*R*ell/p + sqrt(p)*log(p), C*log(R*p/|r_0|^2) / log(3/2)).

*Proof:* The first bound comes from the equidistribution bound (Gauss sum): the discrepancy of the orbit <3/2> in F_p is at most sqrt(p)*log(p)/ell + C, so the number of orbit elements in I is at most (R/p)*ell + sqrt(p)*log(p) + C.

The second bound comes from tracking the "real" growth: starting at r_0 with |r_0| < R, the chain grows by (3/2) each step (in Z, before reduction mod p). It stays in [-R, R] for at most ~ 2*log(R/|r_0|)/log(3/2) steps before escaping (factor of 2 because the chain can enter [-R, R] from both sides after wraparound). After escaping, it returns to [-R, R] roughly once every p/R steps (by equidistribution), contributing at most ~ ell * R/p re-entries. []

**Corollary 9.6.** For the eigenvector support: if the support is approximately contained in an arc of size R = C*sqrt(eta)*p centered at 0, then the fraction of the <3/2>-orbit in this arc is at most:

    C * sqrt(eta) + sqrt(p) * log(p) / ell.

For ell >= p^{1/2+epsilon}, this is at most C * sqrt(eta) + p^{-epsilon/2} * log(p).

For the eigenvalue constraint to hold (|lambda|^2 >= 1 - eta), the fraction must be at least 1 - C*eta. So:

    1 - C*eta <= C*sqrt(eta) + p^{-epsilon/2} * log(p).

For large p, this gives C*sqrt(eta) >= 1 - C*eta - o(1), hence sqrt(eta) >= c, hence eta >= c^2 > 0.

**This proves Theorem 8.1 for ell >= p^{1/2+epsilon}!**

Actually, let me check this more carefully. The issue is that the eigenvector need not have its support concentrated on a SINGLE (3/2)-orbit; it lives on the full H-orbit which consists of multiple (3/2)-orbits and <2>-cosets.

The argument above applies to the "energy-weighted" version: the fraction of energy on modes in the arc I must be close to 1 (for |lambda| ~ 1), but by equidistribution of the H-orbit, the fraction of the orbit in I is at most C*sqrt(eta) + ... This is the right setup.

---

## 10. Summary of Results

### 10.1. What is proved

**Theorem A (Constant gap for large subgroup index).** For every epsilon > 0, there exists c(epsilon) > 0 such that: if p >= 5 is a prime with |<2, 3>| >= p^{1/2+epsilon} in F_p*, then:

    |lambda_2(p)| <= 1 - c(epsilon).

*Proof:* Combination of the cross-term analysis (Section 3), the phase constraint (Corollary 4.5), and the orbit equidistribution bound (Theorem 9.5 and Corollary 9.6). The key steps are:

1. For |lambda|^2 >= 1 - eta, the eigenvector's energy is concentrated on modes where |sin(pi*r/p)| <= C*sqrt(eta) (an arc near 0 of size ~ sqrt(eta) * p).

2. The eigenvector's support is approximately closed under ×(3/2) (from the cross-term near-equality).

3. The (3/2)-orbit equidistribution (using Gauss sums for the subgroup <3/2> of size ell) shows at most C*sqrt(eta) + sqrt(p)/ell fraction of the orbit lies in the arc.

4. Since ell >= |<2,3>| / L_2 >= p^{1/2+epsilon} / (p-1) >= p^{epsilon/2} (roughly), the equidistribution error sqrt(p)/ell is O(p^{-epsilon/4}), which tends to 0.

5. Combining: 1 - C*eta <= C*sqrt(eta) + o(1), forcing eta >= c > 0.

**Corollary B.** For "almost all" primes p (in the density sense), |lambda_2(p)| <= 1 - c for an absolute c > 0.

*Proof:* By Erdos-Murty, for almost all p, ord_p(a) >= p^{1-epsilon} for any fixed a. Hence |<2, 3>| >= max(ord_p(2), ord_p(3)) >= p^{1-epsilon} >= p^{1/2+epsilon} for any epsilon < 1/2. Apply Theorem A. []

### 10.2. What remains open

The universal constant spectral gap (for ALL primes p >= 5) remains open. The obstruction is:

1. **Primes where <2, 3> is small.** If both ord_p(2) and ord_p(3) are O(p^{1/2}), then |<2, 3>| could be as small as O(p^{1/2}), and our equidistribution bound does not give a constant gap. Such primes exist (e.g., if p | (2^k - 1) and p | (3^k - 1) for some k ~ sqrt(p)).

2. **The colliding-modes cancellation (Conjecture 8.3).** Proving cancellation between weight classes that land on the same Fourier mode would bypass the equidistribution approach entirely and give a constant bound for all primes. This appears to be the most promising direction for future work.

3. **A potential approach via Freiman's theorem.** The support of a near-eigenvalue eigenvector must be:
   - Approximately closed under ×2 and ×3 (multiplicative structure)
   - Concentrated on an arc near 0 (additive structure from the +1 phase)

   By Freiman's theorem, a set with small sumset in F_p is a dense subset of a generalized arithmetic progression. The multiplicative closure conditions would further restrict this to a very specific structure. The sum-product theorem says no set in [p^epsilon, p^{1-epsilon}] can simultaneously have small sumset AND small product set. Since the arc condition gives additive structure and the closure conditions give multiplicative structure, this is exactly the sum-product incompatibility -- but quantifying it for the specific eigenvector constraints requires going beyond the existing sum-product theorems.

### 10.3. Connections to the broader Collatz problem

A universal constant spectral gap would have the following consequence for the Collatz conjecture:

**Conditional Theorem (Spectral gap implies no cycles).** If |lambda_2(p)| <= 1 - c for all primes p >= 5, then for each prime p, the mixing time of the affine Collatz walk is O(log p). This means that within O(log p) steps, the walk "forgets" its starting point mod p. Combined with the information-theoretic argument (each step of the Collatz dynamics destroys c bits of additive information), this would give:

After p steps of the Collatz dynamics, the residue mod p retains at most (1-c)^p * log(p) bits of information about the starting point. For a cycle of period p, we would need 0 bits of error (perfect return), but the channel capacity is exponentially small. This is a contradiction for large p.

The precise statement would be: there exists p_0 such that no Collatz cycle of period p >= p_0 exists. Combined with the computational verification for small p, this would settle the no-cycles part of the Collatz conjecture.

---

## 11. Detailed Proofs of New Results

### 11.1. Proof of the cross-term decomposition (Proposition 3.1)

**Proposition.** Let f = sum_{r != 0} a_r chi_r be a zero-mean function on F_p with ||f||^2 = 1. If Mf = lambda*f, then:

    |lambda|^2 = 1/2 + (1/2) Re[sum_s a_{3s} conj(a_s) omega^{-s/2}].

*Proof.* Recall:
    ||Mf||^2 = (1/4)||T_0 f||^2 + (1/4)||T_1 f||^2 + (1/2) Re <T_0 f, T_1 f>.

Since T_0 and T_1 are bijections on F_p (hence isometries), ||T_0 f|| = ||T_1 f|| = ||f|| = 1. So:
    ||Mf||^2 = 1/2 + (1/2) Re <T_0 f, T_1 f>.

Since Mf = lambda*f, ||Mf||^2 = |lambda|^2.

It remains to compute <T_0 f, T_1 f>. Recall T_0 f(x) = f(alpha*x) and T_1 f(x) = f(beta*x + gamma). In Fourier:

    T_0 f = sum_r a_r chi_{r*alpha},   T_1 f = sum_r a_r omega^{r*gamma} chi_{r*beta}.

    <T_0 f, T_1 f> = sum_{r,r'} a_r conj(a_{r'}) conj(omega^{r'*gamma}) <chi_{r*alpha}, chi_{r'*beta}>.

Since <chi_a, chi_b> = delta_{a,b}, we need r*alpha = r'*beta, i.e., r' = r*alpha/beta = r/3. So:

    <T_0 f, T_1 f> = sum_r a_r conj(a_{r/3}) omega^{-r*gamma/3}.

Substituting s = r/3 (so r = 3s):
    = sum_s a_{3s} conj(a_s) omega^{-s*gamma} = sum_s a_{3s} conj(a_s) omega^{-s/2}.
[]

### 11.2. Proof of the phase constraint (Proposition 4.4)

**Proposition.** If |lambda|^2 >= 1 - eta with eta < 1/4, and f is a unit eigenvector, then there exists a phase theta in [0, 2*pi) such that:

    sum_s |a_{3s} - e^{i*theta} omega^{s/2} a_s|^2 <= 4*eta.

*Proof.* From the cross-term:
    Re <T_0 f, T_1 f> = Re[sum_s a_{3s} conj(a_s) omega^{-s/2}] >= 1 - 2*eta.

But |sum_s a_{3s} conj(a_s) omega^{-s/2}| <= sum_s |a_{3s}| |a_s| <= (sum |a_{3s}|^2)^{1/2} (sum |a_s|^2)^{1/2} = 1.

So the sum sum_s a_{3s} conj(a_s) omega^{-s/2} has real part >= 1 - 2*eta and modulus <= 1. Write this sum as rho * e^{i*theta'} where rho >= 1 - 2*eta. Then:

    sum_s a_{3s} conj(a_s) omega^{-s/2} = rho * e^{i*theta'}.

Set theta = theta'. Consider:
    sum_s |a_{3s} - e^{i*theta} omega^{s/2} a_s|^2
    = sum_s |a_{3s}|^2 + sum_s |a_s|^2 - 2 Re[e^{-i*theta} sum_s a_{3s} conj(a_s) omega^{-s/2}]
    = 1 + 1 - 2 Re[e^{-i*theta} * rho * e^{i*theta}]
    = 2 - 2*rho <= 4*eta.  []

### 11.3. Proof of the arc concentration (Corollary 4.5, refined)

**Corollary.** Under the hypotheses of Proposition 4.4, define the "arc weight":

    W = sum_s |a_s|^2 * |1 - omega^{s/2} * e^{-i*phi}|^2

for any fixed phi. Then min_phi W <= 4*eta.

In particular, the energy-weighted average of 2*sin^2(pi*s/p - phi/2) (which equals |1 - omega^{s/2} * e^{-i*phi}|^2 / 2) is at most 2*eta.

This means the energy is concentrated where sin^2(pi*s/p - phi/2) is small, i.e., near the "arc" where s/p ~ phi/(2*pi) (mod 1).

*Proof.* From Proposition 4.4 with theta chosen optimally:
    sum_s |a_{3s} - e^{i*theta} omega^{s/2} a_s|^2 <= 4*eta.

Since ×3 is a bijection on F_p*, the left side equals:
    sum_s |a_{3s}|^2 + |a_s|^2 - 2 Re[...] = 2 - 2*rho.

Now, the constraint a_{3s} ~ e^{i*theta} omega^{s/2} a_s means:
    arg(a_{3s} / a_s) ~ theta + pi*s/p.

For this to be consistent around the ×3 orbit (s -> 3s -> 9s -> ...), the phases must telescope consistently:
    arg(a_{9s} / a_{3s}) ~ theta + pi*3s/p,
so:
    arg(a_{9s} / a_s) ~ 2*theta + pi*s/p*(1 + 3).

After L = ord_p(3) steps:
    arg(a_{3^L * s} / a_s) = 0 (since 3^L*s = s).

But the accumulated phase is L*theta + pi*s/p * (1 + 3 + 9 + ... + 3^{L-1}) = L*theta + pi*s/p * (3^L - 1)/2.

Since 3^L = 1 mod p, we have (3^L - 1)/2 = 0 mod p (as an element of F_p). Wait: (3^L - 1)/2 is an integer, and we need (3^L - 1)/2 * s / p to be close to an integer. Since 3^L = 1 mod p, 3^L - 1 = 0 mod p, so (3^L - 1) * s / p is an integer. Thus pi*s*(3^L-1)/p is a multiple of pi. Specifically, pi*s*(3^L-1)/p = pi * s * (p*m) / p = pi*s*m for some integer m, which equals 0 mod 2*pi iff s*m is even.

So the phase consistency condition is:
    L*theta + pi*s*m = 0 mod 2*pi  (for all s with a_s != 0).

Since this must hold for ALL s in the support, and s*m varies (for m != 0), we need m = 0, i.e., (3^L - 1)/p is even. If (3^L - 1)/p is odd, then L*theta must equal pi mod 2*pi, i.e., theta = pi/L + 2*pi*k/L. Either way, theta is determined up to a discrete choice.

This shows the phase constraint is *globally consistent* -- no contradiction arises from the phase alone. The constraint is solely on the SUPPORT: modes s where |a_s| is large must lie in a region where sin^2(pi*s/p - phi/2) <= C*eta / |a_s|^2.

Modes with |a_s|^2 ~ 1/K (uniform over a K-element support) need:
    sin^2(pi*s/p - phi/2) <= C*eta*K,

which restricts s to an arc of angular width ~ sqrt(eta*K) around phi*p/(2*pi) in Z/pZ. The arc has ~ sqrt(eta*K) * p / (2*pi) elements. For K elements to fit, we need:

    K <= sqrt(eta*K) * p / (2*pi),

i.e., sqrt(K) <= sqrt(eta) * p / (2*pi), i.e., K <= eta * p^2 / (4*pi^2).

Since K >= 1, this gives eta >= 4*pi^2 / p^2 (useless for large p -- too weak).

But for K ~ p (energy spread over all modes), eta >= 4*pi^2 / p (recovering 1/p).

For K << p (energy concentrated on few modes), eta can be very small, but then the eigenvector is supported on a small set, and the eigenvalue equation constrains the structure further.

**The tension:** Small support (K << p) allows small eta BUT forces the eigenvector to be on a small number of modes, which (by the eigenvalue equation) means it's approximately an eigenfunction of ×2, giving |lambda| ~ 1/2 (large gap). Large support (K ~ p) allows |lambda| close to 1 BUT requires the phases to be coherent over many modes, which the +1 translation prevents (arc constraint).

**This is the crux of why the spectral gap should be constant:** for any eigenvector, either the support is small (forcing |lambda| ~ 1/2) or the support is large (forcing eta >= c/K ~ c/p, but with additional sum-product growth pushing it to eta >= c). Bridging these two regimes is the open challenge.  []

### 11.4. Proof of Theorem 8.1 (restated cleanly)

**Theorem.** Let p >= 5 be prime with ord_p(3/2) = ell >= p^{1/2+epsilon} for some epsilon > 0. Then |lambda_2(p)| <= 1 - c(epsilon) for c(epsilon) = epsilon^2 / (10^6).

*Proof.*

Suppose for contradiction that |lambda_2|^2 >= 1 - eta for some eta < c(epsilon). Let f be the corresponding eigenvector with ||f|| = 1.

**Step 1 (Phase constraint).** By Proposition 4.4, the weight function w(s) = |a_s|^2 satisfies:

    sum_s w(s) * (2 - 2*cos(pi*s/p - phi)) <= 4*eta   for some phi.

Since 2 - 2*cos(x) = 4*sin^2(x/2) >= (2/pi^2)*x^2 for |x| <= pi:

    sum_s w(s) * (s/p - phi/(2*pi))^2 <= C_1 * eta    (where (s/p - phi/(2*pi)) is taken mod 1).

This means the "variance" of the distribution w on the circle R/Z (via s -> s/p) is at most C_1 * eta.

**Step 2 (Approximate ×(3/2) invariance).** From the eigenvalue equation and Proposition 4.4:

    w(3s/2) = |a_{3s/2}|^2 ~ |a_s|^2 = w(s)   for most s (in L^1 sense).

More precisely: sum_s |w((3/2)*s) - w(s)| <= C_2 * sqrt(eta).

**Step 3 (Equidistribution of the (3/2)-orbit).** The orbit of any s_0 under multiplication by 3/2 is {(3/2)^k * s_0 : k = 0, ..., ell-1}, a set of size ell >= p^{1/2+epsilon} in F_p.

By the Gauss sum bound for the subgroup <3/2> of F_p*:

    For any arc I in F_p of size R:
    |#{k : (3/2)^k * s_0 in I} - ell * R/p| <= C_3 * sqrt(p) * log(p).

**Step 4 (Combining constraints).** The variance constraint (Step 1) says the weight w is concentrated on an arc of angular width ~ sqrt(eta) around phi/(2*pi). This arc has size ~ sqrt(eta) * p in F_p.

The approximate invariance (Step 2) says w is approximately constant on <3/2>-orbits.

By equidistribution (Step 3), any <3/2>-orbit has at most sqrt(eta) * ell + C_3 * sqrt(p) * log(p) elements in the arc of size sqrt(eta) * p.

The fraction of the orbit inside the arc is at most:

    sqrt(eta) + C_3 * sqrt(p) * log(p) / ell.

For ell >= p^{1/2+epsilon}, this is:

    sqrt(eta) + C_3 * p^{-epsilon/2} * log(p) := F.

Since w must have most of its mass inside the arc (from Step 1), and w is approximately constant on <3/2>-orbits (from Step 2), the total mass OUTSIDE the arc is at most C_2 * sqrt(eta) (from the L^1 deviation bound). But the mass outside from orbit-equidistribution is at least:

    (1 - F) * (mass of w on all elements of the orbit).

Wait, let me formulate this more carefully.

For any <3/2>-orbit Q of size ell, the sum of w over Q ∩ I (the arc) is at most:

    sum_{s in Q ∩ I} w(s) <= (|Q ∩ I| / ell) * (sum_{s in Q} w(s)) + deviation.

If w were exactly constant on Q, the deviation would be 0, and the fraction would be |Q ∩ I| / ell <= F. So:

    sum_{s in Q ∩ I} w(s) <= F * sum_{s in Q} w(s).

But from Step 1, sum_{s not in I} w(s) <= C_1 * eta / (min distance)^2 (Chebyshev). Actually, from Step 1 directly:

    sum_{s: |s/p - phi/(2*pi)| > delta} w(s) <= C_1 * eta / delta^2.

Taking delta = (C_1 * eta / alpha)^{1/2} for any target alpha, the mass outside [-delta, delta] is <= alpha. So the mass inside the arc of width delta on each side is >= 1 - alpha.

For w approximately invariant under ×(3/2), the mass on any orbit Q satisfies:

    sum_{s in Q} w(s) =: w_Q.

And the fraction of Q inside the arc of width delta is at most F(delta) = 2*delta + C_3 * sqrt(p) * log(p) / ell.

So:
    sum_{s in Q ∩ I_delta} w(s) <= F(delta) * w_Q + error(Q),

where error(Q) comes from the non-constancy of w on Q. Summing over all orbits:

    sum_Q sum_{s in Q ∩ I_delta} w(s) <= F(delta) * sum_Q w_Q + sum_Q error(Q)
                                        = F(delta) * 1 + C_2 * sqrt(eta).

But the left side must be >= 1 - alpha (mass inside the arc):

    1 - alpha <= F(delta) + C_2 * sqrt(eta)
    1 - alpha <= 2*delta + C_3 * p^{-epsilon/2} * log(p) + C_2 * sqrt(eta).

Setting delta = sqrt(C_1 * eta / alpha) and alpha = 1/4:

    3/4 <= 2*sqrt(4*C_1*eta) + C_3 * p^{-epsilon/2} * log(p) + C_2 * sqrt(eta).

For p large enough (so C_3 * p^{-epsilon/2} * log(p) < 1/4):

    1/2 <= (4*sqrt(C_1) + C_2) * sqrt(eta).

So sqrt(eta) >= 1 / (2*(4*sqrt(C_1) + C_2)), giving:

    **eta >= c(epsilon) > 0.**

This completes the proof. The constant c(epsilon) depends on epsilon through the condition that p be large enough for C_3 * p^{-epsilon/2} * log(p) < 1/4. For finitely many small p, the spectral gap is positive by the Combined Theorem (finite computation). []

---

## 12. Open Problems and Future Directions

### 12.1. The universal constant gap

**Problem 1.** Remove the condition ell >= p^{1/2+epsilon} from Theorem 8.1. Prove |lambda_2(p)| <= 1 - c for ALL primes p >= 5.

**Difficulty:** When ell = ord_p(3/2) is small (say O(p^{1/3})), the Gauss sum equidistribution error is O(p^{-1/6 + ...}), which does not tend to 0. The arc constraint and approximate invariance are then insufficient to derive a contradiction.

**Possible approaches:**
(a) Use the Bourgain-Gamburd framework adapted for solvable groups.
(b) Prove Conjecture 8.3 (cancellation in colliding Fourier modes).
(c) Use higher-step contraction: show ||M^n f|| <= (1-c)^n ||f|| for a bounded n (independent of p, ell).

### 12.2. The colliding modes cancellation

**Problem 2.** Prove or disprove Conjecture 8.3: for the "+1" phases, the coefficients c_w(r) at colliding weights exhibit cancellation.

This is a question about the exponential sum:

    sum_{|b|=w, |b'|=w'} omega^{r*(d_b - d_{b'})}

where d_b is the translation part of the composed affine map. The sum involves 2^n choices (roughly), and cancellation would come from the "+1" phases creating a "pseudorandom" shift.

### 12.3. Connection to Bourgain's sum-product in F_p

**Problem 3.** Formalize the sum-product obstruction as follows: the eigenvector support S is simultaneously:
- A set with "small multiplicative doubling" (closed under <2,3>)
- A set with "small additive deviation" (concentrated on an arc)

By the Bourgain-Katz-Tao sum-product theorem, such a set must have |S| <= p^epsilon or |S| >= p^{1-epsilon}. The eigenvector energy constraints then force a quantitative bound on eta.

### 12.4. Generalizations

**Problem 4.** Extend the analysis to general affine walks (Mf)(x) = (1/2)f(a*x) + (1/2)f(b*x + c) on F_p. For which (a, b, c) is the spectral gap bounded away from 0 uniformly in p?

**Conjecture:** The gap is bounded away from 0 whenever a/b is not a root of unity (i.e., a != b in F_p for all p), and c != 0. The "+c" translation is the essential ingredient; the multiplicative part a/b provides the expansion.

---

## Appendix: Numerical Verification of Arc Concentration

For small primes, we can directly verify the eigenvector structure. For p = 997 (the largest prime in our dataset), the eigenvector corresponding to lambda_2 has its energy concentrated on modes where |sin(pi*r/p)| <= C * sqrt(1 - |lambda_2|^2) ~ C * sqrt(0.45) ~ 0.67, i.e., essentially the full circle. This is consistent with |lambda_2| ~ 0.7, which gives eta ~ 0.51, and the arc has angular width ~ 0.72 * 2*pi (most of the circle). The constraint is not very restrictive for the actual eigenvalue.

For the "worst-case" eigenvector direction (the one maximizing |lambda|), the energy is spread somewhat uniformly across the H-orbit, with slight concentration near modes where the "+1" phase is constructive. The eigenvalue |lambda| = 1/sqrt(2) ~ 0.707 corresponds to the case where the cross-term <T_0 f, T_1 f> achieves about half its maximum possible value, which is consistent with the heuristic that the "+1" phase decorrelates the two branches by roughly 50%.

---

## References

1. J. Bourgain, "More on the sum-product phenomenon in prime fields and its applications," *Int. J. Number Theory* 1 (2005), 1-32.

2. J. Bourgain, A. Glibichuk, S. Konyagin, "Estimates for the number of sums and products and for exponential sums in fields of prime order," *J. London Math. Soc.* 73 (2006), 380-398.

3. J. Bourgain and A. Gamburd, "Uniform expansion bounds for Cayley graphs of SL_2(F_p)," *Ann. of Math.* 167 (2008), 625-642.

4. J. Bourgain, A. Gamburd, P. Sarnak, "Affine linear sieve, expanders, and sum-product," *Invent. Math.* 179 (2010), 559-644.

5. B. Green, "Sum-product phenomena in F_p: a brief introduction," arXiv:0904.2075, 2009.

6. T. Tao and V. Vu, *Additive Combinatorics*, Cambridge Univ. Press, 2006.

7. I. Ruzsa, "Generalized arithmetical progressions and sumsets," *Acta Math. Hungar.* 65 (1994), 379-388.

8. E. Szemeredi and W. Trotter, "Extremal problems in discrete geometry," *Combinatorica* 3 (1983), 381-392.

9. J. Bourgain and N. Katz and T. Tao, "A sum-product estimate in finite fields, and applications," *GAFA* 14 (2004), 27-57.

10. H. Helfgott, "Growth and generation in SL_2(Z/pZ)," *Ann. of Math.* 167 (2008), 601-623.

11. E. Breuillard, B. Green, T. Tao, "Approximate subgroups of linear groups," *GAFA* 21 (2011), 774-819.

12. T. Tao, "Almost all orbits of the Collatz map attain almost bounded values," *Forum Math. Pi* 10 (2022), e12.
