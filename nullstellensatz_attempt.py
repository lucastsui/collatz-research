"""
PROOF ATTEMPT: Use the Combinatorial Nullstellensatz to prove 0 ∉ R.

Alon's Combinatorial Nullstellensatz (1999):
Let f ∈ F[x_1,...,x_n], let S_1,...,S_n ⊆ F with |S_i| > deg_{x_i}(f).
If the coefficient of x_1^{t_1} ... x_n^{t_n} in f is nonzero (where
t_i = |S_i| - 1 and deg f = sum t_i), then there exist s_i ∈ S_i
with f(s_1,...,s_n) ≠ 0.

For our problem: we want to show that the weighted sum
    W(x_1,...,x_k) = w_0*x_0 + w_1*x_1 + ... + w_{k-1}*x_{k-1}
is NEVER ≡ 0 mod D when (x_0,...,x_{k-1}) is a transversal.

But the Nullstellensatz shows existence of a NONZERO evaluation,
not that ALL evaluations are nonzero.

DIFFERENT APPROACH: Consider the polynomial
    P(x_0,...,x_{k-1}) = W(x_0,...,x_{k-1})^{D-1} - 1

By Fermat's little theorem (for D prime):
- If W ≢ 0 mod D: P = 0 (i.e., W^{D-1} = 1)
- If W ≡ 0 mod D: P = -1

So P = 0 iff W ≠ 0, and P = -1 iff W = 0.

We want to show P is NEVER -1 on transversals. Equivalently,
P + 1 is NEVER 0 on transversals.

This means: show the polynomial Q = W^{D-1} has no zero on the set
of transversals. Since W^{D-1} = 0 iff W = 0 (in F_D), this is
equivalent to W having no zero on transversals.

ALTERNATIVELY: Consider the PERMANENT approach.
The number of zero-sum transversals is:
    N_0 = (1/D) * sum_{t=0}^{D-1} sum_{transversals} omega^{t*W}
where omega = e^{2*pi*i/D}.

The inner sum over transversals of omega^{t*W} is a CHARACTER SUM
evaluated on the transversal set.

For t = 0: inner sum = C(p,k) * k! (number of ordered transversals...
hmm, need to be more careful).

Actually, let's think about it more precisely.

An ORDERED transversal is a k-tuple (r_0, ..., r_{k-1}) with all
r_j ∈ {0,...,p-1} and all distinct. There are p!/(p-k)! such tuples.

The weighted sum for tuple (r_0,...,r_{k-1}) is:
    W = sum_{j=0}^{k-1} 3^{k-1-j} * 2^{r_j}

For the COLLATZ CONVENTION: we restrict to r_0 < r_1 < ... < r_{k-1}
(sorted positions). There are C(p,k) such tuples.

For the UNRESTRICTED ordered case: any permutation of positions.
There are p!/(p-k)! tuples.

N_0 (number of zero-sum sorted transversals) = (1/D) * sum_{t=0}^{D-1}
    sum_{I, |I|=k} omega^{t * S(I)}

where the inner sum is:
    F(t) = sum_{|I|=k} omega^{t * S(I)/D}

But S(I) = sum 3^{k-j} * 2^{i_j}. So:
    F(t) = sum_{i_1<...<i_k} prod_{j=1}^k omega^{t * 3^{k-j} * 2^{i_j}}
         = sum_{i_1<...<i_k} prod_{j=1}^k gamma_j^{2^{i_j}}

where gamma_j = omega^{t * 3^{k-j}}.

F(t) is the k-th ELEMENTARY SYMMETRIC POLYNOMIAL of the values
{gamma_j^{2^r} : r = 0,...,p-1}... no wait, the gamma_j depend on j.

Hmm, it's more complicated because the base changes with j.

Actually, let me reconsider. The sorted transversal sum:
F(t) = sum_{i_1<...<i_k} prod_{j=1}^k omega^{t * 3^{k-j} * 2^{i_j}}

This is NOT a standard elementary symmetric polynomial because the
"variable" at position j depends on both j (via 3^{k-j}) and i_j (via 2^{i_j}).

Let's define: for each position r and weight class j, the "phase" is
    phi(j, r) = omega^{t * 3^{k-1-j} * 2^r}

Then:
    F(t) = sum_{transversals (r_0,...,r_{k-1}) sorted} prod_{j=0}^{k-1} phi(j, r_j)

This is a SUM OVER MATCHINGS in a bipartite graph (weight classes × positions)
weighted by products of phases. This IS a permanent-like quantity.

Specifically, let M be the k × p matrix with entries M[j][r] = phi(j, r).
Then:
    F(t) = sum_{sorted transversals} prod M[j][r_j]

For sorted transversals (r_0 < ... < r_{k-1}), this is related to
the permanent of a k × p submatrix.

The key quantity is N_0 = (1/D) * sum_{t=0}^{D-1} F(t).

If we can show N_0 = 0 (no zero-sum sorted transversals), that proves
the conjecture.

For t = 0: phi(j,r) = 1 for all j,r. So F(0) = C(p,k) (number of sorted transversals).

For t ≠ 0: F(t) involves cancellations among the phases.

N_0 = C(p,k)/D + (1/D) * sum_{t=1}^{D-1} F(t).

For the conjecture: N_0 = 0. So sum_{t=1}^{D-1} F(t) = -C(p,k).

This means the character sum part exactly cancels the main term.

Can we compute |F(t)| for t ≠ 0?

If |F(t)| ≤ C(p,k)/(D-1) for all t ≠ 0, then:
    |sum_{t=1}^{D-1} F(t)| ≤ (D-1) * C(p,k)/(D-1) = C(p,k)
and |N_0 - C(p,k)/D| ≤ C(p,k)/D.

This gives N_0 ∈ [0, 2*C(p,k)/D], which for C(p,k) < D means
N_0 < 2. Since N_0 is a non-negative integer, N_0 ∈ {0, 1}.
This doesn't prove N_0 = 0.

We'd need |F(t)| < C(p,k)/D for the exact cancellation.
This is exactly the equidistribution problem that we already solved
(Theorem 4) for individual primes! But here we need it for D itself
(which is the whole problem).

So this approach also hits the abc barrier in disguise.

HOWEVER: the character sum F(t) for the SORTED transversal might be
smaller than for the unsorted case (because of the sorting constraint).
The sorting constraint creates cancellations.

Let me compute F(t) numerically for small cases and see.
"""

import numpy as np
from itertools import combinations
from math import comb, log

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def compute_character_sums(p, k):
    """Compute F(t) = sum_{|I|=k} omega^{t*S(I)/D} for t = 0,...,D-1."""
    D = 2**p - 3**k
    if D <= 0:
        return

    C = comb(p, k)
    omega = np.exp(2j * np.pi / D)

    all_S = []
    for I in combinations(range(p), k):
        all_S.append(S_value(I, k))

    print(f"\n(p,k)=({p},{k}), D={D}, C={C}")

    # Compute F(t) for all t
    F = np.zeros(D, dtype=complex)
    for t in range(D):
        F[t] = sum(omega**(t * s) for s in all_S)

    # N_0 = (1/D) * sum F(t)
    N0 = np.sum(F) / D
    print(f"  N_0 = {N0.real:.6f} + {N0.imag:.6f}i")
    print(f"  (should be 0 if no zero-sum sorted transversals)")

    # |F(t)| for t ≠ 0
    magnitudes = [abs(F[t]) for t in range(1, D)]
    print(f"  max |F(t)| for t≠0: {max(magnitudes):.4f}")
    print(f"  avg |F(t)| for t≠0: {np.mean(magnitudes):.4f}")
    print(f"  F(0) = C = {C}")
    print(f"  C/D = {C/D:.4f}")
    print(f"  max|F|/C = {max(magnitudes)/C:.4f}")

    # The critical ratio: if max|F(t)|/C < 1/(D-1), then N_0 < 2C/D
    critical_ratio = max(magnitudes) / C
    threshold = 1 / (D - 1) if D > 1 else float('inf')
    print(f"  Critical ratio: {critical_ratio:.6f}")
    print(f"  Threshold for N_0 < 2: {threshold:.6f}")
    print(f"  Below threshold: {critical_ratio < threshold}")

    # DEEPER: How does |F(t)| depend on t?
    # For the equidistribution-type bound, |F(t)| should be ≈ √C
    sqrt_C = np.sqrt(C)
    print(f"  sqrt(C) = {sqrt_C:.2f}")
    print(f"  max|F|/sqrt(C) = {max(magnitudes)/sqrt_C:.4f}")

    # Count how many t have |F(t)| > C/D
    large_count = sum(1 for m in magnitudes if m > C / D)
    print(f"  |F(t)| > C/D for {large_count}/{D-1} values of t")

    # UNSORTED CHARACTER SUM (for comparison)
    # For unsorted tuples, the character sum is a PRODUCT:
    # G(t) = prod_{j=0}^{k-1} sum_{r=0}^{p-1} omega^{t * 3^{k-1-j} * 2^r}
    # (when positions can repeat)
    G = np.ones(D, dtype=complex)
    for j in range(k):
        for t_val in range(D):
            inner = sum(omega**(t_val * pow(3, k-1-j) * pow(2, r)) for r in range(p))
            # This is slow, let me just compute for a few t values
            pass  # Skip for now

    return F

# Run for small cases
for p in [5, 7, 8, 10]:
    k = round(p * log(2) / log(3))
    if 0 < k < p and 2**p - 3**k > 0:
        compute_character_sums(p, k)
