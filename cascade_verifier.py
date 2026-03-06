"""
2-adic cascade verifier for Transversal Zero-Sum Exclusion.

Key insight: Given n, the positions h_0=0, h_1, h_2, ... are UNIQUELY
determined by the 2-adic valuations at each step.

For C = nD with C = sum 3^{k-1-j} * 2^{h_j}:
  T_0 = nD - 3^{k-1}
  h_1 = v_2(T_0)
  T_1 = T_0/2^{h_1} - 3^{k-2}
  h_2 - h_1 = v_2(T_1)
  ...

The cascade succeeds iff all h_j are in range and the final remainder is 0.
"""
from math import log, gcd

def v2(n):
    """2-adic valuation of n."""
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v

def cascade(n, p, k):
    """Run the 2-adic cascade for starting value n.
    Returns (success, positions, fail_reason)."""
    D = 2**p - 3**k
    C = n * D

    positions = [0]  # h_0 = 0
    remainder = C - 3**(k-1)  # subtract first term

    for j in range(1, k):
        if remainder <= 0:
            return False, positions, f"remainder={remainder}<=0 at step {j}"

        gap = v2(remainder)
        h_j = positions[-1] + gap

        if h_j > p - 1:
            return False, positions, f"h_{j}={h_j} > p-1={p-1}"
        if h_j <= positions[-1]:
            return False, positions, f"h_{j}={h_j} <= h_{j-1}={positions[-1]}"

        positions.append(h_j)
        remainder = remainder // (2**gap) - 3**(k-1-j)

    if remainder == 0:
        return True, positions, "SUCCESS"
    else:
        return False, positions, f"final_remainder={remainder}"

def analyze_cascade(p, k):
    D = 2**p - 3**k
    if D <= 0:
        return

    # Compute n range
    # C_min: positions {0,1,...,k-1}
    C_min = sum(3**(k-1-j) * 2**j for j in range(k))
    # C_max: positions {0, p-k+1, ..., p-1}
    C_max = 3**(k-1) + sum(3**(k-2-j) * 2**(p-k+1+j) for j in range(k-1))

    n_min = max(1, (C_min + D - 1) // D)  # ceil
    n_max = C_max // D

    # n must be odd and coprime to 3
    valid_n = [n for n in range(n_min, n_max + 1) if n % 2 == 1 and n % 3 != 0]

    print(f"\n(p,k)=({p},{k}), D={D}")
    print(f"  n range: [{n_min}, {n_max}], valid n count: {len(valid_n)}")

    successes = []
    fail_reasons = {}

    for n in valid_n:
        ok, positions, reason = cascade(n, p, k)
        if ok:
            successes.append((n, positions))
        else:
            # Categorize failure
            key = reason.split('=')[0] if '=' in reason else reason
            fail_reasons[key] = fail_reasons.get(key, 0) + 1

    if successes:
        for n, pos in successes:
            # Check if trivial cycle
            is_trivial = (pos == list(range(0, 2*k, 2)) and p == 2*k)
            tag = " [TRIVIAL CYCLE]" if is_trivial else " [NONTRIVIAL!]"
            print(f"  SUCCESS: n={n}, positions={pos}{tag}")
            # Verify
            C = sum(3**(k-1-j) * 2**pos[j] for j in range(k))
            assert C == n * D, f"Verification failed: C={C}, nD={n*D}"
    else:
        print(f"  NO solutions found among {len(valid_n)} candidates")

    if fail_reasons:
        print(f"  Failure breakdown: {dict(sorted(fail_reasons.items(), key=lambda x: -x[1]))}")

    return len(successes)

# Standard pairs
print("=== 2-ADIC CASCADE VERIFICATION ===")
print("=== Standard (p,k) pairs ===")
for p in [5, 7, 8, 10, 12, 13, 15, 16, 17, 18, 20, 21]:
    k = round(p * log(2) / log(3))
    if 2**p - 3**k <= 0 or k < 3:
        continue
    analyze_cascade(p, k)

# Also check non-standard pairs where trivial cycle lives
print("\n=== Non-standard pairs (trivial cycle check) ===")
for m in [3, 4, 5, 6]:
    p, k = 2*m, m
    D = 2**p - 3**k
    if D > 0:
        analyze_cascade(p, k)

# Check some non-standard pairs with larger k/p gap
print("\n=== Non-standard pairs (various k) ===")
for p in [10, 15, 20]:
    for k in range(3, p):
        D = 2**p - 3**k
        if D <= 0:
            break
        if k == round(p * log(2) / log(3)):
            continue  # skip standard
        # Only check a few
        if k in [3, 4, p//2]:
            analyze_cascade(p, k)
