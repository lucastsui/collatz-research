"""
MONOTONE WEIGHT BARRIER: The deeper structure.

We discovered: zero-sum requires repeated positions. But actually, the
unrestricted case has 11 zero-sum solutions with DISTINCT positions for (5,3).
These use non-monotone weight assignments.

So the true barrier is: the MONOTONE weight-position coupling
(largest 3-weight to smallest 2-position) prevents zero-sum.

Let me verify: for zero-sum solutions with distinct positions but non-monotone
assignment, what is the relationship between the weight ordering and position ordering?

HYPOTHESIS: Every zero-sum solution with distinct positions requires at
least one "inversion" where a larger weight is assigned to a larger position
(violating the anti-sorted/monotone convention).
"""

from itertools import combinations, permutations
from math import comb, log
from collections import Counter

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def weighted_sum(positions, k):
    """Compute sum 3^{k-1-j} * 2^{positions[j]} for j=0,...,k-1.
    Here positions[j] is the position assigned to weight class j.
    Weight class 0 has weight 3^{k-1} (largest).
    """
    return sum(3**(k-1-j) * 2**positions[j] for j in range(k))

def count_inversions(positions):
    """Count inversions: pairs (i,j) with i < j but positions[i] > positions[j].
    For the Collatz convention, positions should be INCREASING (0 inversions).
    """
    inv = 0
    k = len(positions)
    for i in range(k):
        for j in range(i+1, k):
            if positions[i] > positions[j]:
                inv += 1
    return inv

def analyze_zero_sum_inversions(p, k):
    """For all zero-sum solutions with distinct positions,
    what is the minimum number of inversions?"""
    D = 2**p - 3**k
    if D <= 0:
        return

    print(f"\n{'='*70}")
    print(f"(p,k) = ({p},{k}), D = {D}")
    print(f"{'='*70}")

    # Find ALL zero-sum weight assignments with distinct positions
    # positions is a k-tuple from {0,...,p-1} with all distinct entries
    zero_sum = []
    for positions in permutations(range(p), k):
        s = weighted_sum(positions, k)
        if s % D == 0:
            inv = count_inversions(positions)
            n = s // D
            zero_sum.append((inv, positions, n))

    zero_sum.sort()

    print(f"Total zero-sum distinct-position tuples: {len(zero_sum)}")

    if not zero_sum:
        # No zero-sum even with permuted weights!
        # This would be a much stronger statement
        # Check: is this because there are no zero-sum solutions at all?
        print("  >>> NO zero-sum solutions even with permuted weights! <<<")
        # Verify with unrestricted
        from itertools import product as cartesian_product
        count = 0
        for pos in cartesian_product(range(p), repeat=k):
            s = weighted_sum(pos, k)
            if s % D == 0:
                count += 1
        print(f"  Unrestricted zero-sum count: {count}")
        return

    # Minimum inversions
    min_inv = zero_sum[0][0]
    print(f"Minimum inversions for zero-sum: {min_inv}")

    if min_inv == 0:
        print("  WARNING: zero-sum with 0 inversions (sorted positions)!")
        for inv, pos, n in zero_sum:
            if inv == 0:
                print(f"    positions={pos}, n={n}")
    else:
        print(f"  >>> All zero-sum solutions require ≥ {min_inv} inversion(s) <<<")

    # Distribution of inversions
    inv_dist = Counter(inv for inv, _, _ in zero_sum)
    max_possible_inv = k * (k-1) // 2
    print(f"\nInversion distribution (max possible = {max_possible_inv}):")
    for inv in sorted(inv_dist.keys()):
        print(f"  {inv} inversions: {inv_dist[inv]} solutions")

    # Show examples
    print(f"\nExamples with fewest inversions ({min_inv}):")
    for inv, pos, n in zero_sum[:5]:
        if inv == min_inv:
            pos_set = set(pos)
            # What would the Collatz-sorted sum be?
            sorted_pos = tuple(sorted(pos))
            collatz_sum = S_value(sorted_pos, k)
            collatz_r = collatz_sum % D
            print(f"  pos={pos}, n={n}, inversions={inv}")
            print(f"    As sorted subset: {sorted_pos}")
            print(f"    Collatz sum: {collatz_sum}, mod D: {collatz_r}")

    # KEY TEST: For each SUBSET (unordered), how many permutations give zero-sum?
    print(f"\nSubset analysis:")
    subset_zero_counts = Counter()
    for inv, pos, n in zero_sum:
        subset = tuple(sorted(pos))
        subset_zero_counts[subset] += 1

    print(f"  Subsets with ≥1 zero-sum permutation: {len(subset_zero_counts)}")
    for subset, count in sorted(subset_zero_counts.items(), key=lambda x: -x[1])[:5]:
        collatz_sum = S_value(subset, k)
        collatz_r = collatz_sum % D
        print(f"    {subset}: {count} zero-sum perms, Collatz S={collatz_sum}, S mod D={collatz_r}")

print("="*70)
print("MONOTONE WEIGHT BARRIER ANALYSIS")
print("="*70)

for p in [5, 7, 8, 10]:
    k = round(p * log(2) / log(3))
    if 0 < k < p and 2**p - 3**k > 0:
        analyze_zero_sum_inversions(p, k)

# For p=10, permutations(range(10), 6) has 10*9*8*7*6*5 = 151200 elements
# This might take a while but should be feasible
print("\n\n" + "="*70)
print("CRITICAL TEST: Does the inversion barrier grow with p?")
print("="*70)

# For each p, compute the minimum number of inversions needed for zero-sum
for p in [5, 7, 8]:
    k = round(p * log(2) / log(3))
    D = 2**p - 3**k
    if D <= 0:
        continue

    min_inv = float('inf')
    count = 0
    for positions in permutations(range(p), k):
        s = weighted_sum(positions, k)
        if s % D == 0:
            inv = count_inversions(positions)
            min_inv = min(min_inv, inv)
            count += 1

    if count > 0:
        print(f"(p,k)=({p},{k}), D={D}: min_inversions={min_inv}, total_zero_sum={count}")
    else:
        print(f"(p,k)=({p},{k}), D={D}: NO zero-sum with distinct positions and permuted weights")
