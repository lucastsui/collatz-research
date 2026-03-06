"""
PROOF ATTEMPT: Modular Rearrangement Inequality

Core idea: The anti-sorted sum S(I) = sum 3^{k-j} * 2^{i_j} with i_1<...<i_k
satisfies S(I) ≡ -2^{i_1} * 3^{k-1} mod (3*2^{i_1} + ... terms).

But more precisely: let's work in Z/DZ and use the TELESCOPING structure.

KEY ALGEBRAIC IDENTITY:
S(I) = sum_{j=1}^k 3^{k-j} * 2^{i_j}
     = 3^{k-1} * 2^{i_1} + sum_{j=2}^k 3^{k-j} * 2^{i_j}
     = 3^{k-1} * 2^{i_1} + 3 * sum_{j=2}^k 3^{k-j-1} * 2^{i_j} + (terms...)

Actually, let me try a TELESCOPING approach:
Define T_m = sum_{j=m}^k 3^{k-j} * 2^{i_j} for m = 1,...,k, and T_{k+1} = 0.
Then T_m = 3^{k-m} * 2^{i_m} + T_{m+1}.
And S(I) = T_1.

In Z/DZ where D = 2^p - 3^k:
T_1 = S(I).

Now: T_m = 3^{k-m} * 2^{i_m} + T_{m+1}.
So T_m / 3^{k-m} = 2^{i_m} + T_{m+1} / 3^{k-m}.
But T_{m+1} / 3^{k-m} = T_{m+1} / (3 * 3^{k-m-1}).

This gives a continued-fraction-like structure.

ALTERNATIVE: Factor out common powers.
S(I) = 3^{k-1}(2^{i_1} + (1/3) * 2^{i_2} + ... + (1/3^{k-1}) * 2^{i_k})

In Z/DZ, 1/3 = 3^{-1} mod D. Since gcd(3, D) = 1, this is well-defined.

Let gamma = 2/3 mod D. Then:
S(I)/3^{k-1} = 2^{i_1} + gamma * 2^{i_2-1} * 3 + ...

Hmm, let me try yet another decomposition.

DECOMPOSITION BY GAPS:
Let g_j = i_{j+1} - i_j - 1 for j = 1,...,k-1 (gap minus 1, so g_j >= 0).
And let i_1 = a (first position), i_k = b (last position).
Then b - a = (k-1) + sum g_j.

S(I) = 3^{k-1} * 2^a + 3^{k-2} * 2^{a+1+g_1} + 3^{k-3} * 2^{a+2+g_1+g_2} + ...
     = 2^a * (3^{k-1} + 3^{k-2} * 2^{1+g_1} + 3^{k-3} * 2^{2+g_1+g_2} + ...)
     = 2^a * sum_{j=0}^{k-1} 3^{k-1-j} * 2^{j + sum_{m=1}^{j} g_m}
     = 2^a * sum_{j=0}^{k-1} 3^{k-1-j} * 2^j * 2^{G_j}
where G_j = sum_{m=1}^j g_m (with G_0 = 0).

So S(I) = 2^a * sum_{j=0}^{k-1} (2/3)^j * 3^{k-1} * 2^{G_j}
         = 2^a * 3^{k-1} * sum_{j=0}^{k-1} gamma^j * 2^{G_j}
where gamma = 2/3 mod D.

Denote: Sigma = sum_{j=0}^{k-1} gamma^j * 2^{G_j} mod D.
Then S(I) ≡ 2^a * 3^{k-1} * Sigma mod D.

Since gcd(2^a * 3^{k-1}, D) = 1: D | S(I) iff D | Sigma.

So the problem reduces to: Sigma ≡ 0 mod D, where
Sigma = sum_{j=0}^{k-1} gamma^j * alpha^{G_j}
with alpha = 2, gamma = 2/3 = 2 * 3^{-1} mod D,
and G_0 = 0 <= G_1 <= ... <= G_{k-1} (non-decreasing non-negative integers
with G_{k-1} <= p - k).

Note: gamma * alpha = (2/3) * 2 = 4/3 mod D. And gamma^j * alpha^{G_j} =
(2/3)^j * 2^{G_j} = 2^{j+G_j} / 3^j.

So Sigma = sum 2^{j+G_j} / 3^j = sum (2^{1+G_j/j})^j / 3^j ... no that's wrong.

Sigma = sum_{j=0}^{k-1} 2^{j+G_j} * 3^{-j} mod D.

Setting h_j = j + G_j = j + (sum_{m=1}^j g_m):
h_j = j + sum_{m=1}^j g_m = sum_{m=1}^j (1 + g_m) = sum_{m=1}^j (i_{m+1} - i_m) = i_{j+1} - i_1.
Wait: h_0 = 0. h_1 = 1 + g_1 = i_2 - i_1. h_j = i_{j+1} - i_1.

So Sigma = sum_{j=0}^{k-1} 2^{i_{j+1} - a} * 3^{-j} where a = i_1.
         = sum_{j=0}^{k-1} 2^{i_{j+1}} * 2^{-a} * 3^{-j}
         = (1/2^a) * sum_{j=0}^{k-1} 2^{i_{j+1}} * 3^{-j}

Which gives S(I) = 2^a * 3^{k-1} * (1/2^a) * sum 2^{i_{j+1}} * 3^{-j}
                 = 3^{k-1} * sum_{j=0}^{k-1} 2^{i_{j+1}} / 3^j
                 = sum_{j=0}^{k-1} 3^{k-1-j} * 2^{i_{j+1}}
                 = sum_{j=1}^k 3^{k-j} * 2^{i_j}. ✓ (Circular.)

OK so the gap decomposition doesn't immediately help. Let me try a different
approach: look at the problem in the QUOTIENT RING.

THE KEY APPROACH: Work in R = Z[x]/(x^p - 3^k) and use the NORM.

Actually, let me try something completely different.

APPROACH: THE RESULTANT/DISCRIMINANT

F_I(x) = sum 3^{k-j} * x^{i_j} has k terms. In R = Z[x]/(x^p - 3^k):
D | F_I(2) iff F_I ∈ (x-2)R.

If F_I ∈ (x-2)R, then F_I = (x-2) * Q_I where Q_I ∈ R.

Taking norms: N(F_I) = N(x-2) * N(Q_I) = D * N(Q_I).

N(Q_I) must be a positive integer (since Q_I has all-negative coefficients
after normalization, but the norm is a product of complex conjugates).

The key: N(F_I) = prod_{m=0}^{p-1} F_I(omega_m) where omega_m = 3^{k/p} * zeta^m.

Can we compute N(F_I) mod small primes and get a contradiction?

For instance: N(F_I) mod 2.

F_I(omega_m) = sum 3^{k-j} * omega_m^{i_j}.

The product N(F_I) = prod_m F_I(omega_m).

In Z (not mod anything): N(F_I) is a specific integer. If N(F_I) is ODD
and D is ODD, then N(Q_I) = N(F_I)/D might still be an integer. But if
we could show v_q(N(F_I)) < v_q(D) for some prime q, that would give
D ∤ N(F_I), hence F_I ∉ (x-2)R.

Let me compute N(F_I) for small cases and check.
"""

import numpy as np
from itertools import combinations
from math import comb, log, gcd
from functools import reduce

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def compute_norm_FI(I, k, p):
    """Compute N(F_I) = prod_{m=0}^{p-1} F_I(omega_m)
    where omega_m = 3^{k/p} * exp(2*pi*i*m/p)."""
    I_sorted = sorted(I)
    base = 3**(k/p)
    product = 1.0 + 0j
    for m in range(p):
        omega = base * np.exp(2j * np.pi * m / p)
        val = sum(3**(k-j-1) * omega**I_sorted[j] for j in range(k))
        product *= val
    return product

def compute_norm_exact(I, k, p):
    """Compute N(F_I) using resultant (more numerically stable).
    N(F_I) = Res(F_I, x^p - 3^k) / leading_coeff^{deg}.
    For our polynomial F_I of degree < p, this is just the product
    of F_I evaluated at all roots of x^p = 3^k.
    The result should be an integer.
    """
    return compute_norm_FI(I, k, p)

def factorize(n):
    if n <= 1:
        return {}
    factors = {}
    d = 2
    while d * d <= abs(n):
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if abs(n) > 1:
        factors[abs(n)] = factors.get(abs(n), 0) + 1
    return factors

def analyze_norm(p, k):
    D = 2**p - 3**k
    if D <= 0:
        return

    print(f"\n{'='*60}")
    print(f"(p,k)=({p},{k}), D={D}")
    print(f"{'='*60}")

    D_factors = factorize(D)
    print(f"D = {' * '.join(f'{p}^{e}' if e > 1 else str(p) for p, e in sorted(D_factors.items()))}")

    for I in combinations(range(p), k):
        s = S_value(I, k)
        r = s % D

        norm = compute_norm_exact(I, k, p)
        norm_real = round(norm.real)
        norm_int = norm_real

        # Check N(F_I) mod D
        if abs(norm_int) > 0:
            n_mod_D = norm_int % D
            divisible = (n_mod_D == 0)
        else:
            divisible = True

        if r <= 2 or r >= D - 2:  # Near zero residues
            print(f"  I={I}, S={s}, S mod D={r}")
            print(f"    N(F_I) ≈ {norm_real:.0f}, N mod D = {n_mod_D}")
            print(f"    D | N(F_I): {divisible}, D | S(I): {r == 0}")

            if divisible and r != 0:
                print(f"    *** D | N but D ∤ S: norm condition is WEAKER ***")
            if not divisible and r == 0:
                print(f"    *** D ∤ N but D | S: CONTRADICTION (impossible) ***")
            if not divisible and r != 0:
                print(f"    *** D ∤ N and D ∤ S: norm PROVES non-divisibility ***")

analyze_norm(5, 3)
analyze_norm(7, 4)

# For p=5, k=3: Let me also check if N(F_I) mod D has a pattern
print("\n" + "="*60)
print("FULL NORM ANALYSIS: (5,3)")
print("="*60)

p, k = 5, 3
D = 2**p - 3**k

for I in combinations(range(p), k):
    s = S_value(I, k)
    r = s % D
    norm = compute_norm_exact(I, k, p)
    norm_int = round(norm.real)
    n_mod_D = norm_int % D

    print(f"  I={I}, S={s}, S%D={r}, N≈{norm_int}, N%D={n_mod_D}, D|N={n_mod_D==0}")

print("\n" + "="*60)
print("FULL NORM ANALYSIS: (7,4)")
print("="*60)

p, k = 7, 4
D = 2**p - 3**k

for I in combinations(range(p), k):
    s = S_value(I, k)
    r = s % D
    norm = compute_norm_exact(I, k, p)
    norm_int = round(norm.real)
    n_mod_D = norm_int % D if abs(norm_int) > 0 else 0

    if r <= 5 or r >= D - 5 or n_mod_D == 0:
        print(f"  I={I}, S={s}, S%D={r}, N≈{norm_int}, N%D={n_mod_D}")
