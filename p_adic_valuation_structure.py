"""
Part 0 Attack: p-adic valuation structure of S(I) mod D.

KEY NEW IDEA: Instead of asking "does D divide S(I)?", ask about the
D-ADIC structure of S(I). Specifically:

S(I) = sum_{j=1}^k 3^{k-j} * 2^{i_j}

This is a sum of k terms. Each term is a {2,3}-smooth number.
D = 2^p - 3^k is their "target divisor".

THE OBSERVATION TO TEST:
In the ring R = Z[x]/(x^p - 3^k), the element F_I(x) = sum 3^{k-j} x^{i_j}
maps to S(I) under x -> 2. The ideal (x-2)R has index D.

F_I lives in a SPECIFIC coset of (x-2)R, determined by S(I) mod D.
The question is: can this coset be the zero coset?

NEW ANGLE: Look at S(I) not just mod D, but mod D AND mod small primes
SIMULTANEOUSLY, using the lattice structure in R.

Specifically: the QUOTIENT n = S(I)/D, if it exists, must satisfy:
- n > 0 (positive starting value)
- n is odd (since i_k < p, the orbit starts at an odd step... wait, not necessarily)
- The BINARY EXPANSION of n*D = S(I) has specific structure

Let me compute: for each (p,k), what are the possible values of S(I) mod D,
and what PATTERNS do the near-zero residues have?

Also: does the GREEDY representation give any insight?
S(I) is a sum of k terms from the set {3^{k-j} * 2^i : 0 <= i <= p-1, 0 <= j <= k-1}.
Each (i,j) pair is used at most once, and the j values must be distinct
(each j from 0 to k-1 appears exactly once).

So S(I) is the sum where the j-th largest position gets weight 3^{k-1-j}.
The LARGEST weight (3^{k-1}) goes to the SMALLEST position.
"""

from itertools import combinations
from math import comb, log, gcd
from collections import Counter, defaultdict

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def binary_weight(n):
    """Number of 1s in binary representation."""
    return bin(n).count('1')

def analyze_residue_structure(p, k):
    """Deep analysis of S(I) mod D residue structure."""
    D = 2**p - 3**k
    if D <= 0:
        return
    C = comb(p, k)

    all_S = []
    residues = defaultdict(list)

    for I in combinations(range(p), k):
        s = S_value(I, k)
        r = s % D
        all_S.append((I, s, r))
        residues[r].append(I)

    # Sort residues by distance from 0
    near_zero = []
    for r, Is in residues.items():
        dist = min(r, D - r)
        near_zero.append((dist, r, Is))
    near_zero.sort()

    print(f"\n{'='*60}")
    print(f"(p,k) = ({p},{k}): D = {D}, C(p,k) = {C}")
    print(f"{'='*60}")

    # How many residues are hit?
    print(f"Distinct residues: {len(residues)}/{D} ({100*len(residues)/D:.1f}%)")
    print(f"Residue 0 hit: {'YES' if 0 in residues else 'NO'}")

    # Show nearest residues to 0
    print(f"\nNearest residues to 0 mod D:")
    for dist, r, Is in near_zero[:8]:
        n_approx = r / D if r < D/2 else -(D-r) / D
        print(f"  r={r} (dist={dist}), count={len(Is)}")
        if len(Is) <= 3:
            for I in Is:
                s = S_value(I, k)
                print(f"    I={I}, S={s}, S/D={s/D:.6f}")

    # KEY TEST: What is the MINIMUM |S(I) mod D| (distance to 0)?
    min_dist = near_zero[0][0]
    print(f"\nMinimum distance to 0: {min_dist}")
    print(f"  As fraction of D: {min_dist/D:.6f}")
    print(f"  log2(min_dist): {log(min_dist+1, 2):.2f}")
    print(f"  log2(D): {log(D, 2):.2f}")

    # STRUCTURE TEST: For the nearest-to-0 residue patterns,
    # what is the SPACING structure of I?
    print(f"\nSpacing analysis of nearest-to-0 patterns:")
    for dist, r, Is in near_zero[:3]:
        for I in Is[:2]:
            I_sorted = sorted(I)
            spacings = [I_sorted[j+1] - I_sorted[j] for j in range(k-1)]
            print(f"  I={I}, spacings={spacings}, sum_spacings={sum(spacings)}")
            # Check: is the spacing "almost uniform"?
            avg_spacing = (p-1) / (k-1) if k > 1 else 0
            deviation = sum((s - avg_spacing)**2 for s in spacings)
            print(f"    avg_spacing={avg_spacing:.2f}, variance={deviation/(k-1):.2f}")

    return near_zero

def test_greedy_bound(p, k):
    """
    Test: can we show S(I) mod D != 0 by a GREEDY argument?

    S(I) = 3^{k-1} * 2^{i_1} + 3^{k-2} * 2^{i_2} + ... + 2^{i_k}

    The LARGEST term is 3^{k-1} * 2^{i_1}. If i_1 is large, this term
    dominates. The divisibility D | S requires a very specific cancellation
    between the terms.

    Can we bound how close the partial sums can get to a multiple of D?
    """
    D = 2**p - 3**k
    if D <= 0:
        return

    print(f"\n--- Greedy analysis for (p,k)=({p},{k}), D={D} ---")

    # For each I, compute the partial sums and their residues mod D
    best_approach = None
    best_final_dist = D

    for I in combinations(range(p), k):
        I_sorted = sorted(I)
        partial_sums = []
        s = 0
        for j in range(k):
            s += 3**(k-j-1) * 2**I_sorted[j]
            partial_sums.append(s % D)

        final_r = partial_sums[-1]
        dist = min(final_r, D - final_r)
        if dist < best_final_dist:
            best_final_dist = dist
            best_approach = (I, partial_sums)

    if best_approach:
        I, ps = best_approach
        print(f"  Closest to 0: I={I}")
        print(f"  Partial sums mod D: {ps}")
        print(f"  Final distance: {best_final_dist}")

def test_carry_propagation(p, k):
    """
    NEW TEST: When we compute S(I) in binary, the carries propagate.
    S(I) = sum 3^{k-j} * 2^{i_j}.

    Each term 3^{k-j} * 2^{i_j} has binary weight = binary_weight(3^{k-j}).
    The sum's binary weight depends on carry propagation.

    D = 2^p - 3^k. In binary, D = 1000...0 - binary(3^k).

    For D | S: S = n*D. The binary representation of n*D has specific structure
    determined by n and D.

    KEY: n*D = n*2^p - n*3^k. The binary weight of n*D depends on n.
    But S(I) is a sum of {2,3}-smooth terms with specific positions.
    """
    D = 2**p - 3**k
    if D <= 0:
        return

    print(f"\n--- Binary structure for (p,k)=({p},{k}), D={D} ---")
    print(f"  D in binary: {bin(D)}")
    print(f"  binary_weight(D) = {binary_weight(D)}")
    print(f"  3^k = {3**k}, binary: {bin(3**k)}")
    print(f"  binary_weight(3^k) = {binary_weight(3**k)}")

    # For small n, compute binary weight of n*D
    print(f"\n  Binary weight of n*D:")
    for n in range(1, min(20, 2**p // D + 1)):
        nD = n * D
        print(f"    n={n}: n*D={nD}, bw(n*D)={binary_weight(nD)}, bits={nD.bit_length()}")

    # For each I, compute binary weight of S(I) and compare
    bw_dist = Counter()
    for I in combinations(range(p), k):
        s = S_value(I, k)
        bw = binary_weight(s)
        bw_dist[bw] += 1

    print(f"\n  Binary weight distribution of S(I):")
    for bw in sorted(bw_dist.keys()):
        if bw_dist[bw] > 0:
            print(f"    bw={bw}: count={bw_dist[bw]}")

# Run analyses
for p in [5, 7, 8, 10, 13]:
    k = round(p * log(2) / log(3))
    if 0 < k < p and 2**p - 3**k > 0:
        analyze_residue_structure(p, k)

print("\n" + "="*60)
print("GREEDY ANALYSIS")
print("="*60)

for p in [5, 7, 8]:
    k = round(p * log(2) / log(3))
    if 0 < k < p and 2**p - 3**k > 0:
        test_greedy_bound(p, k)

print("\n" + "="*60)
print("BINARY STRUCTURE ANALYSIS")
print("="*60)

for p in [5, 7, 8, 10]:
    k = round(p * log(2) / log(3))
    if 0 < k < p and 2**p - 3**k > 0:
        test_carry_propagation(p, k)
