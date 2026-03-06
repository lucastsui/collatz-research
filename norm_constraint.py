"""
Explore the norm constraint for Collatz cycle non-divisibility.

Key idea: If D | F_I(2) where F_I(x) = sum 3^{k-j} x^{i_j},
then in R = Z[x]/(x^p - 3^k), F_I = (x-2) Q_I.

The NORM gives: N(F_I) = D * N(Q_I).

N(F_I) = prod_{j=0}^{p-1} F_I(zeta_j) where zeta_j^p = 3^k.

Question: does the integrality of N(Q_I) = N(F_I)/D give usable constraints?

Also: investigate the elementary symmetric polynomial at composite modulus.
Does e_k at composite roots show anti-correlation vs product of primes?
"""

from itertools import combinations
from math import comb, log, gcd
import numpy as np

def S_value(I, k, p):
    """Compute S(I) = sum_{j=1}^k 3^{k-j} * 2^{i_j}"""
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def compute_norm_FI(I, k, p):
    """Compute N(F_I) = prod_{j=0}^{p-1} F_I(zeta_j) where zeta_j = 3^{k/p} * e^{2*pi*i*j/p}"""
    I_sorted = sorted(I)
    base = 3**(k/p)
    product = 1.0 + 0j
    for j in range(p):
        zeta = base * np.exp(2j * np.pi * j / p)
        val = sum(3**(k-m-1) * zeta**I_sorted[m] for m in range(len(I_sorted)))
        product *= val
    return product

def analyze_case(p, k):
    D = 2**p - 3**k
    if D <= 0:
        print(f"  D = {D} <= 0, skipping")
        return

    C = comb(p, k)
    print(f"\n(p,k) = ({p},{k}): D = {D}, C(p,k) = {C}, C/D = {C/D:.4f}")

    residues = {}
    divisible_count = 0
    norms = []

    for I in combinations(range(p), k):
        s = S_value(I, k, p)
        r = s % D
        residues[r] = residues.get(r, 0) + 1
        if r == 0:
            divisible_count += 1
            n = s // D
            print(f"  DIVISIBLE: I={I}, S={s}, n={n}")

        # Compute norm (expensive, only for small cases)
        if p <= 12:
            norm = compute_norm_FI(I, k, p)
            norm_real = norm.real
            norms.append((I, s, r, norm_real))

    print(f"  Residues hitting 0: {divisible_count} out of {C}")
    print(f"  Expected (uniform): {C/D:.2f}")
    print(f"  Distinct residues: {len(residues)} out of {D}")

    if residues.get(0, 0) == 0:
        print(f"  ** 0 is AVOIDED **")

    # Check norm constraints for divisible cases
    if p <= 12 and norms:
        print(f"\n  Norm analysis (N(F_I) and N(F_I)/D):")
        for I, s, r, norm_r in norms[:5]:  # show first 5
            if abs(norm_r) > 1e-10:
                ratio = norm_r / D
                print(f"    I={I}: S={s} mod D={r}, |N(F_I)|={abs(norm_r):.2f}, N/D={ratio:.2f}")

def check_anticorrelation(p, k):
    """Check if divisibility by q1*q2 shows anti-correlation vs product."""
    D = 2**p - 3**k
    if D <= 0:
        return

    # Find small prime factors of D
    factors = []
    d = D
    for q in range(2, min(1000, d)):
        if d % q == 0:
            factors.append(q)
            while d % q == 0:
                d //= q
    if d > 1:
        factors.append(d)

    if len(factors) < 2:
        print(f"\n(p,k)=({p},{k}): D={D} has {len(factors)} prime factor(s): {factors}")
        print(f"  Need at least 2 factors for anti-correlation test")
        return

    q1, q2 = factors[0], factors[1]
    Q = q1 * q2
    C = comb(p, k)

    count_q1 = 0
    count_q2 = 0
    count_Q = 0
    total = C

    for I in combinations(range(p), k):
        s = S_value(I, k, p)
        if s % q1 == 0:
            count_q1 += 1
        if s % q2 == 0:
            count_q2 += 1
        if s % Q == 0:
            count_Q += 1

    p_q1 = count_q1 / total
    p_q2 = count_q2 / total
    p_Q = count_Q / total
    p_product = p_q1 * p_q2

    print(f"\n(p,k)=({p},{k}): D={D}, factors={factors}")
    print(f"  q1={q1}: P(q1|S) = {count_q1}/{total} = {p_q1:.4f} (expected 1/{q1} = {1/q1:.4f})")
    print(f"  q2={q2}: P(q2|S) = {count_q2}/{total} = {p_q2:.4f} (expected 1/{q2} = {1/q2:.4f})")
    print(f"  Q={Q}: P(Q|S) = {count_Q}/{total} = {p_Q:.6f}")
    print(f"  Product: P(q1)*P(q2) = {p_product:.6f}")
    print(f"  Ratio: P(Q)/(P(q1)*P(q2)) = {p_Q/p_product:.4f}" if p_product > 0 else "  Product = 0")
    if p_Q < p_product:
        print(f"  ** ANTI-CORRELATION detected! **")
    elif p_Q > p_product:
        print(f"  Positive correlation")
    else:
        print(f"  Independent")

print("=" * 60)
print("PART 1: Non-divisibility and norm analysis")
print("=" * 60)

for p in range(5, 20):
    k = round(p * log(2) / log(3))
    if k >= p or k < 1:
        continue
    analyze_case(p, k)

print("\n" + "=" * 60)
print("PART 2: Anti-correlation test")
print("=" * 60)

for p in range(5, 22):
    k = round(p * log(2) / log(3))
    if k >= p or k < 1:
        continue
    D = 2**p - 3**k
    if D <= 0:
        continue
    check_anticorrelation(p, k)
