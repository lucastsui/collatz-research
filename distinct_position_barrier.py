"""
THE DISTINCT-POSITION BARRIER

Critical discovery: S(I) = sum 3^{k-j} * 2^{i_j} mod D can ALWAYS achieve
residue 0 if we allow repeated positions (unrestricted sumset), but the
distinct-position constraint (I is a k-SUBSET) prevents 0 from being hit.

For small D (cases where C(p,k) > D): 0 is the ONLY residue excluded
by the distinct-position constraint!

This means the framework should be:
PROVE THAT THE TRANSVERSAL CONSTRAINT (distinct positions) PREVENTS
ZERO-SUM IN THE WEIGHTED GEOMETRIC PROGRESSION.

This is a problem in additive combinatorics + transversal theory.
"""

from itertools import combinations
from math import comb, log, gcd
from collections import Counter

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def unrestricted_sumset(p, k, D):
    """
    Compute the unrestricted sumset A_0 + A_1 + ... + A_{k-1} mod D,
    where A_j = {3^{k-1-j} * 2^i mod D : i = 0, ..., p-1}.
    (No distinct-position constraint.)
    """
    current = {0}
    for j in range(k):
        coeff = pow(3, k-1-j, D)
        Aj = set()
        for i in range(p):
            Aj.add((coeff * pow(2, i, D)) % D)
        new = set()
        for s in current:
            for a in Aj:
                new.add((s + a) % D)
        current = new
    return current

def restricted_sumset(p, k, D):
    """
    Compute the restricted sumset (distinct positions): choose k positions
    i_1 < ... < i_k from {0,...,p-1}, compute sum 3^{k-j} * 2^{i_j} mod D.
    """
    result = set()
    for I in combinations(range(p), k):
        s = S_value(I, k)
        result.add(s % D)
    return result

def test_distinction(p, k):
    D = 2**p - 3**k
    if D <= 0:
        return None
    C = comb(p, k)

    U = unrestricted_sumset(p, k, D)

    # For small enough cases, compute restricted too
    if C <= 200000:
        R = restricted_sumset(p, k, D)
    else:
        R = None

    print(f"\n(p,k)=({p},{k}): D={D}, C={C}, C/D={C/D:.3f}")
    print(f"  Unrestricted sumset: |U|={len(U)}/{D} ({100*len(U)/D:.1f}%)")
    print(f"  0 in U: {0 in U}")

    if R is not None:
        print(f"  Restricted sumset: |R|={len(R)}/{D} ({100*len(R)/D:.1f}%)")
        print(f"  0 in R: {0 in R}")
        diff = U - R
        print(f"  U \\ R (unrestricted only): {len(diff)} residues")
        if len(diff) <= 20:
            print(f"    {sorted(diff)}")
        print(f"  0 in (U \\ R): {0 in diff}")

        # KEY: is 0 ALWAYS in U \ R?
        if 0 in U and 0 not in R:
            print(f"  >>> 0 excluded by distinct-position constraint! <<<")

            if len(diff) == 1:
                print(f"  >>> 0 is the ONLY excluded residue! <<<")
    else:
        print(f"  Restricted sumset: (too large to enumerate)")

    return (0 in U, R is not None and 0 not in R if R else None)

print("="*70)
print("THE DISTINCT-POSITION BARRIER")
print("Does the unrestricted sumset contain 0? Always?")
print("Does the restricted sumset exclude 0? Always?")
print("="*70)

results = []
for p in range(5, 23):
    k = round(p * log(2) / log(3))
    if k >= p or k < 1:
        continue
    D = 2**p - 3**k
    if D <= 0:
        continue
    result = test_distinction(p, k)
    if result:
        results.append((p, k, D, result))

print("\n" + "="*70)
print("SUMMARY")
print("="*70)
print(f"{'p':>3} {'k':>3} {'D':>10} {'0∈U':>5} {'0∉R':>5}")
for p, k, D, (in_U, not_in_R) in results:
    r_str = str(not_in_R) if not_in_R is not None else "N/A"
    print(f"{p:>3} {k:>3} {D:>10} {str(in_U):>5} {r_str:>5}")

print("\n" + "="*70)
print("DEEPER: WHY does the distinct-position constraint exclude 0?")
print("="*70)

# For small cases, find the UNRESTRICTED zero-sum solutions
# and check if they ALL require repeated positions
for p in [5, 7, 8]:
    k = round(p * log(2) / log(3))
    D = 2**p - 3**k
    if D <= 0:
        continue

    print(f"\n(p,k)=({p},{k}), D={D}")
    print("Unrestricted zero-sum solutions (allowing repeated positions):")

    # Find all tuples (i_0, ..., i_{k-1}) with sum ≡ 0 mod D
    # where i_j ∈ {0,...,p-1} (allowing repeats)
    zero_sum_count = 0
    has_repeat_count = 0
    distinct_count = 0
    example_repeats = []

    from itertools import product as cartesian_product
    for positions in cartesian_product(range(p), repeat=k):
        s = sum(3**(k-j-1) * 2**positions[j] for j in range(k))
        if s % D == 0:
            zero_sum_count += 1
            if len(set(positions)) < k:
                has_repeat_count += 1
                if len(example_repeats) < 5:
                    example_repeats.append(positions)
            else:
                distinct_count += 1

    print(f"  Total zero-sum tuples: {zero_sum_count}")
    print(f"  With repeated positions: {has_repeat_count}")
    print(f"  With ALL distinct positions: {distinct_count}")

    if distinct_count == 0 and has_repeat_count > 0:
        print(f"  >>> ALL zero-sum solutions require repeated positions! <<<")

    print(f"  Example solutions with repeats:")
    for pos in example_repeats[:5]:
        s = sum(3**(k-j-1) * 2**pos[j] for j in range(k))
        repeats = [i for i in range(p) if sum(1 for x in pos if x == i) > 1]
        print(f"    positions={pos}, S={s}, n=S/D={s//D}, repeated: {repeats}")
