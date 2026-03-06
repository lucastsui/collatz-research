"""
THE MISSING RESIDUE IDENTITY

For prime D with C(p,k) > D: the restricted sumset R has |R| = D-1,
and the only missing residue is 0.

If this always holds, then the missing residue is:
    missing = sum_{r=0}^{D-1} r  -  sum_{I, |I|=k} S(I) mod D

Since sum_{r=0}^{D-1} r = D(D-1)/2 ≡ 0 mod D (for D odd prime):
    missing ≡ -sum_I S(I) mod D

For missing = 0: need D | sum_I S(I).

FORMULA:
sum_I S(I) = sum_{j=1}^k sum_{r=0}^{p-1} 3^{k-j} * 2^r * C(r, j-1) * C(p-1-r, k-j)

This is a SPECIFIC NUMBER. The question: does D = 2^p - 3^k always divide it?

If YES: this is a new algebraic identity, and it proves that for the
"dense" regime (C > D), the ONLY missing residue is 0 — which is exactly
the no-cycles statement.

Even for C < D: the sum formula might have a specific residue mod D that
constrains which residues can be missing.
"""

from itertools import combinations
from math import comb, log

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def compute_sum_formula(p, k):
    """Compute sum_I S(I) using the explicit formula."""
    total = 0
    for j in range(1, k+1):
        for r in range(p):
            coeff = 3**(k-j) * 2**r
            count = comb(r, j-1) * comb(p-1-r, k-j)
            total += coeff * count
    return total

def compute_sum_direct(p, k):
    """Compute sum_I S(I) by brute force."""
    total = 0
    for I in combinations(range(p), k):
        total += S_value(I, k)
    return total

def test_missing_residue_identity(p, k):
    D = 2**p - 3**k
    if D <= 0:
        return

    C = comb(p, k)

    # Compute sum_I S(I)
    total = compute_sum_direct(p, k)
    total_formula = compute_sum_formula(p, k)
    assert total == total_formula, f"Formula mismatch: {total} vs {total_formula}"

    # Check divisibility
    remainder = total % D
    divisible = (remainder == 0)

    # The "missing residue" (if we hit exactly D-1 residues)
    # = D*(D-1)/2 - total mod D  (for D odd)
    if D % 2 == 1:
        missing = (D * (D-1) // 2 - total) % D
    else:
        missing = None

    # Count unique residues
    if C <= 500000:
        residues = set()
        for I in combinations(range(p), k):
            residues.add(S_value(I, k) % D)
        num_residues = len(residues)
        zero_in_R = 0 in residues
    else:
        num_residues = None
        zero_in_R = None

    print(f"\n(p,k)=({p},{k}): D={D}, C={C}")
    print(f"  sum_I S(I) = {total}")
    print(f"  sum mod D = {remainder}")
    print(f"  D | sum: {divisible}")

    if D % 2 == 1:
        print(f"  'Missing residue' = {missing}")

    if num_residues is not None:
        print(f"  |R| = {num_residues}/{D}")
        print(f"  0 in R: {zero_in_R}")
        if num_residues == D - 1 and not zero_in_R:
            print(f"  >>> EXACTLY 0 is missing! <<<")

    # Additional: what is sum_I S(I) in terms of D?
    print(f"  sum / D = {total / D:.2f}")

    return divisible, total, remainder

print("="*70)
print("THE MISSING RESIDUE IDENTITY")
print("Does D | sum_I S(I)?")
print("="*70)

for p in range(5, 25):
    k = round(p * log(2) / log(3))
    if k >= p or k < 1:
        continue
    D = 2**p - 3**k
    if D <= 0:
        continue
    test_missing_residue_identity(p, k)

print("\n" + "="*70)
print("DEEPER: Factor structure of sum_I S(I)")
print("="*70)

for p in [5, 7, 8, 10, 13]:
    k = round(p * log(2) / log(3))
    D = 2**p - 3**k
    if D <= 0:
        continue

    total = compute_sum_formula(p, k)
    C = comb(p, k)

    # Factor total
    rem = total
    factor_D = 0
    while rem % D == 0 and rem > 0:
        rem //= D
        factor_D += 1

    print(f"\n(p,k)=({p},{k}): D={D}")
    print(f"  sum = {total}")
    print(f"  v_D(sum) = {factor_D} (sum = D^{factor_D} * {total // D**factor_D if factor_D > 0 else total})")

    # Also check: sum_I S(I) = C(p,k) * (average S(I))
    avg = total / C
    print(f"  Average S(I) = {avg:.2f}")
    print(f"  Average S/D = {avg/D:.4f}")

    # IDENTITY: average = sum_{j=1}^k 3^{k-j} * (weighted average of 2^r)
    # The weighted average of 2^r with weight C(r,j-1)*C(p-1-r,k-j)/C(p,k)
    # is the expected value of 2^{X_j} where X_j ~ Hypergeometric(p, j-1, k).
    # Actually it's: E[2^{i_j}] = sum_r 2^r * P(r = j-th order stat of Unif{0..p-1})
