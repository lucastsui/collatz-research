"""
CORRECTED Modular Feedback Theorem verification.

The CORRECT cycle equation formula is:
  C_b = Σ_{i: b_i=1} 3^{k_{>i}} · 2^i

NOT 2^{p-i-1} as used in the earlier (buggy) script.

Derivation: T^p_b = T_{b_{p-1}} ∘ ... ∘ T_{b_0}, with
  T_1(n) = (3n+1)/2, T_0(n) = n/2
gives fixed point n₀ = C_b / (2^p - 3^k) where
  C_b = Σ_{i: b_i=1} 3^{k_{>i}} · 2^i
"""
from itertools import combinations
from math import comb

def compute_Cb_correct(pattern, p, k):
    """CORRECT: C_b = Σ_{i: b_i=1} 3^{k_{>i}} · 2^i"""
    odd_positions = sorted([i for i in range(p) if pattern[i] == 1])
    Cb = 0
    for idx, i in enumerate(odd_positions):
        k_after = k - idx - 1  # number of odd positions after this one
        Cb += (3 ** k_after) * (2 ** i)
    return Cb

def compute_Cb_wrong(pattern, p, k):
    """WRONG (old formula): C_b = Σ_{i: b_i=1} 3^{k_{>i}} · 2^{p-i-1}"""
    odd_positions = sorted([i for i in range(p) if pattern[i] == 1])
    Cb = 0
    for idx, i in enumerate(odd_positions):
        k_after = k - idx - 1
        Cb += (3 ** k_after) * (2 ** (p - i - 1))
    return Cb

def collatz_orbit_parity(n0, p):
    """Compute parity pattern of n0 under p steps of compressed Collatz."""
    pattern = []
    n = n0
    for _ in range(p):
        if n <= 0:
            return None
        pattern.append(n % 2)
        if n % 2 == 1:
            n = (3 * n + 1) // 2
        else:
            n = n // 2
    return tuple(pattern)

def verify_cycle_equation(n0, pattern, p, k):
    """Verify that T^p(n0) = n0 with the given parity pattern."""
    n = n0
    for i in range(p):
        if n % 2 != pattern[i]:
            return False, i  # parity mismatch at step i
        if pattern[i] == 1:
            n = (3 * n + 1) // 2
        else:
            n = n // 2
    return (n == n0), -1  # check if orbit closes

def main():
    print("=" * 80)
    print("CORRECTED MFT VERIFICATION")
    print("=" * 80)

    # First verify the trivial cycle
    print("\n--- Trivial cycle verification ---")
    pattern_trivial = (1, 0)  # 1 → 2 → 1
    Cb_correct = compute_Cb_correct(pattern_trivial, 2, 1)
    Cb_wrong = compute_Cb_wrong(pattern_trivial, 2, 1)
    D = 2**2 - 3**1
    print(f"Pattern (1,0), p=2, k=1, D={D}")
    print(f"  Correct C_b = {Cb_correct}, n0 = {Cb_correct}/{D} = {Cb_correct/D}")
    print(f"  Wrong C_b = {Cb_wrong}, n0 = {Cb_wrong}/{D} = {Cb_wrong/D}")

    # Now test all (p,k) pairs
    print("\n--- Full verification ---")
    total_tested = 0
    total_arith = 0  # patterns with D | C_b (correct formula)
    total_consistent = 0

    for p in range(3, 23):
        for k in range(1, p):
            D = 2**p - 3**k
            if D <= 0 or D == 1:
                continue
            if comb(p, k) > 500000:
                continue

            total_tested += 1
            found_arith = []

            for positions in combinations(range(p), k):
                pattern = tuple(1 if i in positions else 0 for i in range(p))
                Cb = compute_Cb_correct(pattern, p, k)

                if Cb % D == 0:
                    n0 = Cb // D
                    if n0 > 0:
                        total_arith += 1
                        # Check actual orbit
                        actual = collatz_orbit_parity(n0, p)
                        closes, mismatch_pos = verify_cycle_equation(n0, pattern, p, k)

                        is_cycle = (actual == pattern) and closes
                        if is_cycle and n0 > 2:
                            total_consistent += 1

                        found_arith.append({
                            'pattern': pattern,
                            'Cb': Cb,
                            'n0': n0,
                            'is_cycle': is_cycle,
                            'actual': actual,
                            'closes': closes,
                            'mismatch': mismatch_pos
                        })

            if found_arith:
                print(f"\n(p={p}, k={k}): D={D}, C(p,k)={comb(p,k)}")
                print(f"  Arithmetic solutions (D|C_b): {len(found_arith)}")
                for sol in found_arith:
                    status = "CYCLE!" if sol['is_cycle'] else "not a cycle"
                    print(f"    n0={sol['n0']}, C_b={sol['Cb']}, {status}")
                    if not sol['is_cycle'] and sol['actual']:
                        for j in range(p):
                            if sol['pattern'][j] != sol['actual'][j]:
                                print(f"      Parity mismatch at pos {j}: "
                                      f"pattern={sol['pattern'][j]}, actual={sol['actual'][j]}")
                                break
                        if not sol['closes']:
                            print(f"      Orbit doesn't close: T^p(n0) ≠ n0")

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"(p,k) pairs tested: {total_tested}")
    print(f"Total arithmetic solutions (D|C_b, correct formula): {total_arith}")
    print(f"Nontrivial self-consistent cycles found: {total_consistent}")

    if total_consistent == 0:
        print("\nNO NONTRIVIAL CYCLES FOUND.")
    else:
        print(f"\n*** NONTRIVIAL CYCLE(S) FOUND: {total_consistent} ***")

if __name__ == '__main__':
    main()
