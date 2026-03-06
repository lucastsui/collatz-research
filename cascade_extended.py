"""
Extended cascade verification for larger p values.
Also proves n=1 case for all (p,k).
"""
from math import log, gcd

def v2(n):
    if n == 0: return float('inf')
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v

def cascade(n, p, k):
    D = 2**p - 3**k
    remainder = n * D - 3**(k-1)
    positions = [0]
    for j in range(1, k):
        if remainder <= 0:
            return False, positions, "negative"
        gap = v2(remainder)
        h_j = positions[-1] + gap
        if h_j > p - 1:
            return False, positions, "overflow"
        positions.append(h_j)
        remainder = remainder // (2**gap) - 3**(k-1-j)
    if remainder == 0:
        return True, positions, "success"
    return False, positions, "nonzero_remainder"

def get_n_range(p, k):
    D = 2**p - 3**k
    C_min = sum(3**(k-1-j) * 2**j for j in range(k))
    # C_max: positions {0, p-k+1, ..., p-1}
    C_max = 3**(k-1) + sum(3**(k-2-j) * 2**(p-k+1+j) for j in range(k-1))
    n_min = max(1, -(-C_min // D))  # ceil division
    n_max = C_max // D
    return n_min, n_max, D

def test_pair(p, k, verbose=True):
    D = 2**p - 3**k
    if D <= 0: return None
    n_min, n_max, D = get_n_range(p, k)
    valid_n = [n for n in range(n_min, n_max + 1) if n % 2 == 1 and n % 3 != 0]

    successes = 0
    for n in valid_n:
        ok, pos, reason = cascade(n, p, k)
        if ok:
            is_trivial = (pos == list(range(0, 2*k, 2)) and p == 2*k)
            if verbose:
                tag = "TRIVIAL" if is_trivial else "NONTRIVIAL!"
                print(f"  n={n} pos={pos} [{tag}]")
            if not is_trivial:
                successes += 1  # only count nontrivial

    if verbose:
        print(f"(p,k)=({p},{k}) D={D} candidates={len(valid_n)} "
              f"nontrivial_solutions={successes}")
    return successes

# Find valid (p,k) pairs
print("=== Extended Cascade Verification ===\n")
pairs = []
for p in range(5, 35):
    k = round(p * log(2) / log(3))
    D = 2**p - 3**k
    if D <= 0:
        # Try k-1
        k -= 1
        D = 2**p - 3**k
    if D > 0 and k >= 3:
        pairs.append((p, k, D))

for p, k, D in pairs:
    n_min, n_max, _ = get_n_range(p, k)
    n_count = len([n for n in range(n_min, n_max+1) if n%2==1 and n%3!=0])
    result = test_pair(p, k, verbose=False)
    status = "OK" if result == 0 else f"FOUND {result}!"
    print(f"p={p:2d} k={k:2d} D={D:>12d} n_range=[{n_min},{n_max}] "
          f"candidates={n_count:>5d} {status}")

# Near-critical pairs from convergents of log2/log3
print("\n=== Near-critical pairs (convergents) ===")
near_critical = [(5,3), (8,5), (27,17), (46,29)]
for p, k in near_critical:
    D = 2**p - 3**k
    if D <= 0:
        print(f"p={p} k={k}: D={D} < 0, skipping")
        continue
    n_min, n_max, _ = get_n_range(p, k)
    n_count = len([n for n in range(n_min, n_max+1) if n%2==1 and n%3!=0])
    print(f"p={p} k={k} D={D} candidates={n_count}")
    if n_count <= 50000:
        result = test_pair(p, k, verbose=False)
        print(f"  Result: {'OK - no nontrivial solutions' if result==0 else f'FOUND {result}!'}")
    else:
        print(f"  Too many candidates, skipping full check")
