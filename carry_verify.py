"""
Carry analysis verification for Collatz cycle sum.

Verifies Proposition 3 (Carry Weight Identity):
    W_c(I) = sum_{m=0}^{k-1} s_1(3^m) - s_1(n_0 * D)

Also computes carry statistics for all exact solutions and near-misses.

Run with: python3 carry_verify.py
"""
from itertools import combinations
from math import log, gcd, comb

def hamming_weight(n):
    """Number of 1-bits in binary representation of n."""
    if n < 0:
        raise ValueError("Hamming weight undefined for negative n")
    return bin(n).count('1')

def carry_weight_and_carries(terms):
    """
    Compute total carry generated when adding terms in binary.
    Returns (total_carry_weight, list_of_carries_per_bit).
    """
    if not terms or all(t == 0 for t in terms):
        return 0, []
    max_bits = max(t.bit_length() for t in terms if t > 0) + len(terms) + 2
    total_carry = 0
    carry = 0
    carries = []
    for bit in range(max_bits):
        col_sum = carry
        for t in terms:
            col_sum += (t >> bit) & 1
        carry = col_sum >> 1  # floor(col_sum / 2)
        carries.append(carry)
        total_carry += carry
    return total_carry, carries

def compute_S_and_terms(I, k):
    """Compute S(I) and the individual terms T_j = 3^{k-j} * 2^{i_j}."""
    terms = []
    S = 0
    for j_idx, i_j in enumerate(I):
        j = j_idx + 1
        t = pow(3, k - j) * pow(2, i_j)
        terms.append(t)
        S += t
    return S, terms

def sum_hw_powers3(k):
    """Sum of Hamming weights of 3^0, 3^1, ..., 3^{k-1}."""
    return sum(hamming_weight(pow(3, m)) for m in range(k))

def beatty_distance(I, k, p):
    """L1 distance from I to the Beatty sequence floor(j*p/k)."""
    beatty = [int(j * p / k) for j in range(k)]
    return sum(abs(I[j] - beatty[j]) for j in range(k))

def gap_sequence(I, p):
    """Gaps between consecutive odd positions (including wrap-around)."""
    k = len(I)
    gaps = []
    for idx in range(k - 1):
        gaps.append(I[idx + 1] - I[idx] - 1)
    gaps.append(p - I[-1] + I[0] - 1)
    return gaps

def max_carry_in_region(carries, start, end):
    """Max carry value in bit positions [start, end)."""
    if start >= end or start >= len(carries):
        return 0
    return max(carries[start:min(end, len(carries))])

def verify_collatz_cycle(n0, p, I):
    """Verify n0 actually forms a Collatz cycle with period p and odd positions I."""
    n = n0
    odd_set = set(I)
    for step in range(p):
        if step in odd_set:
            if n % 2 != 1:
                return False, f"Step {step}: expected odd, got even (n={n})"
            n = (3 * n + 1) // 2
        else:
            if n % 2 != 0:
                return False, f"Step {step}: expected even, got odd (n={n})"
            n = n // 2
    return n == n0, f"{'Cycle!' if n == n0 else f'No cycle: got {n}'}"


# ============================================================
# PART 1: Verify Proposition 3 for all exact solutions
# ============================================================
print("=" * 70)
print("PART 1: CARRY WEIGHT IDENTITY VERIFICATION")
print("(Proposition 3: Wc = sum s_1(3^m) - s_1(n0*D))")
print("=" * 70)

all_solutions = []

for p in range(2, 25):
    for k in range(max(1, int(p * 0.4)), min(p, int(p * 0.75) + 1)):
        D = (1 << p) - pow(3, k)
        if D <= 0:
            continue

        if comb(p, k) > 500000:
            continue

        hw_sum = sum_hw_powers3(k)

        for I in combinations(range(p), k):
            S, terms = compute_S_and_terms(I, k)
            if S % D != 0:
                continue
            n0 = S // D
            if n0 < 1:
                continue

            Wc, carries = carry_weight_and_carries(terms)
            hw_n0D = hamming_weight(n0 * D)

            # Verify Proposition 3: Wc = sum s_1(3^m) - s_1(n0*D)
            prop3_ok = (Wc == hw_sum - hw_n0D)

            # Verify cycle
            is_cycle, cycle_msg = verify_collatz_cycle(n0, p, I)

            gaps = gap_sequence(I, p)
            bdist = beatty_distance(I, k, p)
            v2_n0 = 0
            temp = n0
            while temp % 2 == 0:
                v2_n0 += 1
                temp //= 2

            sol = {
                'p': p, 'k': k, 'D': D, 'I': I, 'n0': n0,
                'Wc': Wc, 'hw_sum': hw_sum, 'hw_n0D': hw_n0D,
                'hw_S': hamming_weight(S), 'prop3_ok': prop3_ok,
                'is_cycle': is_cycle, 'gaps': gaps,
                'bdist': bdist, 'v2_n0': v2_n0, 'v2_i1': I[0],
                'max_carry': max(carries) if carries else 0,
            }
            all_solutions.append(sol)

            status = "CYCLE" if is_cycle else "arith"
            p3_status = "OK" if prop3_ok else "FAIL"
            print(f"  p={p:2d} k={k:2d} I={str(I):30s} n0={n0:8d} "
                  f"Wc={Wc:6d} s1(n0D)={hw_n0D:4d} sum_s1={hw_sum:5d} "
                  f"Prop3={p3_status} [{status}] gaps={gaps} v2(n0)={v2_n0} i1={I[0]}")

prop3_failures = [s for s in all_solutions if not s['prop3_ok']]
print(f"\nTotal solutions found: {len(all_solutions)}")
print(f"Proposition 3 failures: {len(prop3_failures)}")
if prop3_failures:
    print("PROPOSITION 3 FAILED FOR:")
    for s in prop3_failures:
        print(f"  p={s['p']}, k={s['k']}, I={s['I']}, n0={s['n0']}")
else:
    print("Proposition 3 VERIFIED for all solutions.")

# ============================================================
# PART 2: v2 constraint verification
# ============================================================
print("\n" + "=" * 70)
print("PART 2: 2-ADIC VALUATION CONSTRAINT")
print("(v_2(n_0) should equal i_1 = min(I))")
print("=" * 70)

v2_failures = [s for s in all_solutions if s['v2_n0'] != s['v2_i1']]
if v2_failures:
    print("v2 CONSTRAINT FAILURES:")
    for s in v2_failures:
        print(f"  p={s['p']}, k={s['k']}, I={s['I']}, n0={s['n0']}, "
              f"v2(n0)={s['v2_n0']}, i1={s['v2_i1']}")
else:
    print(f"v2(n0) = i1 verified for all {len(all_solutions)} solutions.")

# ============================================================
# PART 3: Carry statistics for cycles vs non-cycles
# ============================================================
print("\n" + "=" * 70)
print("PART 3: CARRY WEIGHT STATISTICS")
print("=" * 70)

cycles = [s for s in all_solutions if s['is_cycle']]
non_cycles = [s for s in all_solutions if not s['is_cycle']]

print(f"\nValid cycles: {len(cycles)}")
for s in cycles:
    print(f"  p={s['p']:2d} k={s['k']:2d} n0={s['n0']:6d} Wc={s['Wc']:6d} "
          f"max_carry={s['max_carry']} s1(n0D)={s['hw_n0D']} "
          f"beatty_dist={s['bdist']}")

print(f"\nArithmetic-only solutions (not self-consistent): {len(non_cycles)}")
for s in non_cycles[:20]:
    print(f"  p={s['p']:2d} k={s['k']:2d} n0={s['n0']:6d} Wc={s['Wc']:6d} "
          f"max_carry={s['max_carry']} s1(n0D)={s['hw_n0D']} "
          f"beatty_dist={s['bdist']}")
if len(non_cycles) > 20:
    print(f"  ... ({len(non_cycles) - 20} more)")

# ============================================================
# PART 4: Hamming weight of powers of 3
# ============================================================
print("\n" + "=" * 70)
print("PART 4: HAMMING WEIGHT OF POWERS OF 3")
print("(Used in the carry weight identity)")
print("=" * 70)

print(f"\n{'m':>4s} {'3^m':>20s} {'bits':>6s} {'s1(3^m)':>8s} {'density':>8s}")
cumsum = 0
for m in range(20):
    val = pow(3, m)
    hw = hamming_weight(val)
    bits = val.bit_length()
    density = hw / bits if bits > 0 else 0
    cumsum += hw
    print(f"{m:4d} {val:20d} {bits:6d} {hw:8d} {density:8.3f}   cumsum={cumsum}")

print(f"\nFor k=13 (typical for p=20): sum_hw = {sum_hw_powers3(13)}")
print(f"Predicted carry weight for trivial cycle: ~{sum_hw_powers3(13)//2}")

# ============================================================
# PART 5: Carry weight vs p^2 scaling
# ============================================================
print("\n" + "=" * 70)
print("PART 5: CARRY WEIGHT SCALING (Wc vs p^2)")
print("=" * 70)

for s in sorted(cycles, key=lambda x: x['p']):
    p, k = s['p'], s['k']
    ratio = s['Wc'] / (p * p) if p > 0 else 0
    print(f"  p={p:2d} k={k:2d} Wc={s['Wc']:6d} p^2={p*p:6d} Wc/p^2={ratio:.4f}")

# ============================================================
# PART 6: Near-miss carry analysis
# ============================================================
print("\n" + "=" * 70)
print("PART 6: NEAR-MISS ANALYSIS")
print("(Patterns where S/D is close to integer but not exact)")
print("=" * 70)

for p in [10, 12, 14, 16]:
    target_ratio = log(2) / log(3)
    k = round(p * target_ratio)
    if k < 1 or k >= p:
        continue
    D = (1 << p) - pow(3, k)
    if D <= 0:
        continue

    hw_sum_k = sum_hw_powers3(k)

    best_remainder = D
    best_info = None
    carry_weights = []

    for I in combinations(range(p), k):
        S, terms = compute_S_and_terms(I, k)
        remainder = S % D

        Wc, carries = carry_weight_and_carries(terms)
        carry_weights.append(Wc)

        if remainder < best_remainder:
            best_remainder = remainder
            n0_approx = S // D
            best_info = {
                'I': I, 'S': S, 'n0': n0_approx,
                'rem': remainder, 'Wc': Wc,
                'hw_S': hamming_weight(S),
            }

    avg_Wc = sum(carry_weights) / len(carry_weights)
    std_Wc = (sum((w - avg_Wc)**2 for w in carry_weights) / len(carry_weights)) ** 0.5

    print(f"\np={p}, k={k}, D={D}, hw_sum={hw_sum_k}")
    print(f"  Carry weight stats: mean={avg_Wc:.1f}, std={std_Wc:.1f}, "
          f"min={min(carry_weights)}, max={max(carry_weights)}")
    print(f"  Best near-miss: remainder={best_remainder}, n0~{best_info['n0']}")
    print(f"    I={best_info['I']}, Wc={best_info['Wc']}, s1(S)={best_info['hw_S']}")

    if best_remainder == 0:
        print(f"    EXACT SOLUTION FOUND")
        # For exact solutions, verify Proposition 3
        n0 = best_info['n0']
        hw_n0D = hamming_weight(n0 * D)
        expected_Wc = hw_sum_k - hw_n0D
        print(f"    Prop 3 check: s1(n0*D)={hw_n0D}, expected Wc={expected_Wc}, actual Wc={best_info['Wc']}")

print("\n" + "=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)
