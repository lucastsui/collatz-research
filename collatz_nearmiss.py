"""
Near-miss census for Collatz cycles.
For each (p, k) pair with k/p near log2/log3,
enumerate parity patterns and check how close S/(2^p - 3^k) is to an integer.
"""
from itertools import combinations
from math import log, gcd
import sys

def compute_S(odd_positions, k):
    """Compute S = sum_{j=1}^{k} 3^{k-j} * 2^{i_j}"""
    S = 0
    for j_idx, i_j in enumerate(odd_positions):
        j = j_idx + 1
        S += pow(3, k - j) * pow(2, i_j)
    return S

def analyze_pk(p, k):
    """For given (p,k), enumerate all C(p,k) parity patterns and find near-misses."""
    denom = pow(2, p) - pow(3, k)
    if denom <= 0:
        return None
    
    best_remainder = denom  # worst case
    best_pattern = None
    best_n0 = None
    exact_count = 0
    total = 0
    near_misses = []  # (remainder/denom ratio, n0_approx, pattern)
    
    for odd_pos in combinations(range(p), k):
        total += 1
        S = compute_S(odd_pos, k)
        remainder = S % denom
        
        if remainder == 0:
            n0 = S // denom
            if n0 > 0:
                exact_count += 1
                near_misses.append((0.0, n0, odd_pos))
        else:
            # How close to an integer? min(remainder, denom-remainder) / denom
            closeness = min(remainder, denom - remainder) / denom
            if closeness < 0.01:  # within 1% of an integer
                n0_approx = round(S / denom)
                near_misses.append((closeness, n0_approx, odd_pos))
        
        if remainder < best_remainder:
            best_remainder = remainder
            best_pattern = odd_pos
            if remainder == 0:
                best_n0 = S // denom
    
    return {
        'p': p, 'k': k, 'denom': denom,
        'total_patterns': total,
        'exact_solutions': exact_count,
        'best_remainder_ratio': best_remainder / denom,
        'best_pattern': best_pattern,
        'best_n0': best_n0,
        'near_misses': sorted(near_misses)[:10]
    }

print("=== Collatz Near-Miss Census ===\n")
print(f"Target ratio k/p = log(2)/log(3) = {log(2)/log(3):.6f}\n")

target = log(2) / log(3)

for p in range(2, 30):
    # For each p, find k values where k/p is closest to log2/log3
    k_ideal = p * target
    for k in range(max(1, int(k_ideal) - 1), min(p, int(k_ideal) + 2)):
        if pow(2, p) <= pow(3, k):
            continue
        
        # Skip if C(p,k) is too large (> 1M)
        from math import comb
        if comb(p, k) > 500000:
            print(f"p={p:2d}, k={k:2d}: C(p,k)={comb(p,k):>10,} -- skipping (too large)")
            continue
        
        result = analyze_pk(p, k)
        if result is None:
            continue
        
        ratio = k/p
        print(f"p={p:2d}, k={k:2d} (k/p={ratio:.4f}), "
              f"denom={result['denom']:>12,}, "
              f"patterns={result['total_patterns']:>8,}, "
              f"exact={result['exact_solutions']}, "
              f"best_rem_ratio={result['best_remainder_ratio']:.6f}")
        
        if result['exact_solutions'] > 0:
            for closeness, n0, pattern in result['near_misses']:
                if closeness == 0:
                    # Verify this is a real cycle
                    print(f"  *** EXACT SOLUTION: n0={n0}, pattern={pattern}")
                    # Verify
                    n = n0
                    for i in range(p):
                        if i in pattern:
                            assert n % 2 == 1, f"Step {i}: expected odd, got {n}"
                            n = (3*n + 1) // 2
                        else:
                            assert n % 2 == 0, f"Step {i}: expected even, got {n}"
                            n = n // 2
                    if n == n0:
                        print(f"      VERIFIED CYCLE! n0={n0}")
                    else:
                        print(f"      Algebraic solution but NOT a valid cycle (n={n} != n0={n0})")
                        print(f"      (parity pattern doesn't match actual parities)")

print("\n=== Distribution of best remainder ratios ===")
print("(How close the nearest pattern gets to an integer solution)\n")

import collections
buckets = collections.Counter()
for p in range(2, 24):
    k_ideal = p * target
    for k in range(max(1, int(k_ideal) - 1), min(p, int(k_ideal) + 2)):
        if pow(2, p) <= pow(3, k):
            continue
        from math import comb
        if comb(p, k) > 200000:
            continue
        result = analyze_pk(p, k)
        if result and result['exact_solutions'] == 0:
            r = result['best_remainder_ratio']
            if r < 0.001: buckets['< 0.001'] += 1
            elif r < 0.01: buckets['< 0.01'] += 1
            elif r < 0.1: buckets['< 0.1'] += 1
            else: buckets['>= 0.1'] += 1

for bucket in ['< 0.001', '< 0.01', '< 0.1', '>= 0.1']:
    print(f"  {bucket}: {buckets.get(bucket, 0)}")
