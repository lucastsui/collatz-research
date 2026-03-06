"""
Gap analysis for Transversal Zero-Sum Exclusion.

Key insight: D is odd, so D | S(I) iff D | C(g) where C(g) = S(I)/2^{i_1}
depends only on the gap vector. WLOG i_1 = 0.
"""
from itertools import combinations
from math import comb, log, gcd

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def analyze(p, k):
    D = 2**p - 3**k
    if D <= 0:
        return None

    min_dist = D
    closest = None
    residues = set()
    near_misses = []

    for I in combinations(range(p), k):
        if I[0] != 0:
            continue
        S = S_value(I, k)
        r = S % D
        residues.add(r)
        dist = min(r, D - r)
        if dist < min_dist:
            min_dist = dist
            closest = I
        if dist <= 5:
            gaps = tuple(I[j+1] - I[j] - 1 for j in range(k-1))
            near_misses.append((I, gaps, S, r, dist))

    # Verify WLOG: check a non-zero-start subset
    for I in combinations(range(p), k):
        if I[0] == 0:
            continue
        S = S_value(I, k)
        r = S % D
        # S = 2^{i_1} * C(g), so S%D should equal (2^{i_1} * C(g)) % D
        I_shifted = tuple(x - I[0] for x in I)
        C = S_value(I_shifted, k)
        assert S == (2**I[0]) * C, f"Factor check failed for {I}"
        assert (S % D == 0) == (C % D == 0), f"WLOG check failed for {I}"
        break  # just check one

    print(f"(p,k)=({p},{k}), D={D}, subsets(i1=0)={comb(p-1,k-1)}, "
          f"|R|={len(residues)}, 0∈R={0 in residues}, "
          f"min_dist={min_dist}, min_dist/D={min_dist/D:.4f}")

    if near_misses:
        near_misses.sort(key=lambda x: x[4])
        for I, gaps, S, r, dist in near_misses[:5]:
            print(f"  near-miss: I={I}, gaps={gaps}, S%D={r}, dist={dist}")

    return min_dist, D

print("=== Gap Analysis: Minimum distance to 0 ===\n")
results = []
for p in [5, 7, 8, 10, 12, 13, 15, 16, 17, 18]:
    k = round(p * log(2) / log(3))
    D = 2**p - 3**k
    if D <= 0 or k < 3:
        continue
    res = analyze(p, k)
    if res:
        results.append((p, k, res[0], res[1]))

print("\n=== Summary: min distance vs D ===")
print(f"{'p':>4} {'k':>4} {'D':>10} {'min_dist':>10} {'ratio':>10}")
for p, k, md, D in results:
    print(f"{p:4d} {k:4d} {D:10d} {md:10d} {md/D:10.6f}")
