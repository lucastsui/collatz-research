"""
Verify the Modular Feedback Theorem for Collatz cycles.

For each (p,k) with D = 2^p - 3^k > 0:
1. Enumerate all C(p,k) parity patterns
2. Find which satisfy D | C_b (arithmetic constraint)
3. Check which are 2-adically self-consistent (dynamical constraint)
4. Report whether any pattern satisfies BOTH
"""
from itertools import combinations
from math import comb

def compute_Cb(pattern, p, k):
    """Compute C_b = sum_{i: b_i=1} 2^{p-i-1} * 3^{k_{>i}}"""
    odd_positions = [i for i in range(p) if pattern[i] == 1]
    Cb = 0
    for idx, i in enumerate(odd_positions):
        # k_{>i} = number of odd positions after position i
        k_after = len([j for j in odd_positions if j > i])
        Cb += (2 ** (p - i - 1)) * (3 ** k_after)
    return Cb

def collatz_orbit_parity(n0, p):
    """Compute the parity pattern of n0 under p steps of compressed Collatz."""
    pattern = []
    n = n0
    for _ in range(p):
        if n <= 0:
            return None  # invalid
        pattern.append(n % 2)
        if n % 2 == 1:
            n = (3 * n + 1) // 2
        else:
            n = n // 2
    return tuple(pattern)

def analyze_pk(p, k):
    """Analyze all patterns for given (p,k)."""
    D = 2**p - 3**k
    if D <= 0:
        return None

    total_patterns = comb(p, k)
    arithmetic_solutions = []  # patterns with D | C_b
    self_consistent = []       # patterns that are also dynamically consistent

    # Enumerate all k-subsets of {0,...,p-1}
    for positions in combinations(range(p), k):
        pattern = tuple(1 if i in positions else 0 for i in range(p))

        Cb = compute_Cb(pattern, p, k)

        if Cb % D == 0:
            n0 = Cb // D
            if n0 > 0:
                # Check self-consistency
                actual_pattern = collatz_orbit_parity(n0, p)
                is_consistent = (actual_pattern == pattern)

                # Check first-bit condition
                first_bit_ok = (pattern[0] == pattern[p-1])

                arithmetic_solutions.append({
                    'pattern': pattern,
                    'Cb': Cb,
                    'n0': n0,
                    'first_bit_ok': first_bit_ok,
                    'self_consistent': is_consistent,
                    'actual_pattern': actual_pattern
                })

                if is_consistent:
                    self_consistent.append((pattern, n0))

    return {
        'p': p, 'k': k, 'D': D,
        'total_patterns': total_patterns,
        'arithmetic_count': len(arithmetic_solutions),
        'arithmetic_solutions': arithmetic_solutions,
        'self_consistent': self_consistent
    }

def main():
    print("=" * 80)
    print("MODULAR FEEDBACK THEOREM VERIFICATION")
    print("=" * 80)

    # Test all valid (p,k) up to p=20
    results = []
    for p in range(2, 21):
        for k in range(1, p):
            D = 2**p - 3**k
            if D <= 0:
                continue
            if D == 1 and p == 2 and k == 1:
                continue  # skip trivial cycle case

            # Skip if too many patterns
            if comb(p, k) > 500000:
                continue

            result = analyze_pk(p, k)
            if result is None:
                continue
            results.append(result)

            arith = result['arithmetic_count']
            sc = len(result['self_consistent'])

            if arith > 0:
                print(f"\n(p={p}, k={k}): D={D}, C(p,k)={result['total_patterns']}")
                print(f"  Arithmetic solutions (D|C_b): {arith}")
                print(f"  Self-consistent: {sc}")

                for sol in result['arithmetic_solutions']:
                    status = "CYCLE!" if sol['self_consistent'] else "FAIL"
                    fb = "b0=bp1" if sol['first_bit_ok'] else "b0!=bp1"
                    print(f"    n0={sol['n0']}, {fb}, {status}")
                    if not sol['self_consistent'] and sol['actual_pattern']:
                        # Find first mismatch
                        for j in range(p):
                            if sol['pattern'][j] != sol['actual_pattern'][j]:
                                print(f"      First mismatch at position {j}: "
                                      f"expected {sol['pattern'][j]}, got {sol['actual_pattern'][j]}")
                                break

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    any_nontrivial = False
    for r in results:
        for pattern, n0 in r['self_consistent']:
            if n0 > 2:  # exclude trivial cycle {1,2}
                print(f"NONTRIVIAL CYCLE FOUND: p={r['p']}, k={r['k']}, n0={n0}")
                any_nontrivial = True

    if not any_nontrivial:
        print("No nontrivial self-consistent patterns found.")
        print(f"Tested {len(results)} (p,k) pairs.")

    # Statistics on WHY arithmetic solutions fail
    print("\n" + "=" * 80)
    print("FAILURE ANALYSIS")
    print("=" * 80)

    total_arith = 0
    fail_first_bit = 0
    fail_later = 0

    for r in results:
        for sol in r['arithmetic_solutions']:
            if not sol['self_consistent']:
                total_arith += 1
                if not sol['first_bit_ok']:
                    fail_first_bit += 1
                else:
                    fail_later += 1

    print(f"Total non-trivial arithmetic solutions: {total_arith}")
    print(f"  Failed at first bit (b0 != b_{'{p-1}'}): {fail_first_bit} ({100*fail_first_bit/max(total_arith,1):.1f}%)")
    print(f"  Passed first bit, failed later: {fail_later} ({100*fail_later/max(total_arith,1):.1f}%)")

if __name__ == '__main__':
    main()
