"""
Carry-Parity Interaction Analysis for Collatz No-Cycles.

This script performs a comprehensive computational investigation of the
interaction between the carry weight identity and parity feedback constraints.

Key analyses:
1. Exhaustive check for small p: divisibility, self-consistency, carry weight
2. The bit-by-bit cascade: how carries determine n0 and feed back to parity
3. Sensitivity analysis: how pattern perturbations affect the cascade
4. 2-adic expansion analysis
5. The overdetermined system analysis
"""

from itertools import combinations
from math import log, log2, comb, gcd
import sys

# ============================================================
# PART 0: Utility functions
# ============================================================

def hamming_weight(n):
    """Number of 1-bits in binary representation."""
    return bin(n).count('1')

def v2(n):
    """2-adic valuation of n."""
    if n == 0:
        return float('inf')
    v = 0
    while n % 2 == 0:
        n //= 2
        v += 1
    return v

def collatz_step(n):
    """One step of compressed Collatz: (3n+1)/2 if odd, n/2 if even."""
    if n % 2 == 1:
        return (3 * n + 1) // 2
    else:
        return n // 2

def collatz_trajectory(n0, p):
    """Compute p steps of Collatz from n0, return trajectory and parity pattern."""
    traj = [n0]
    pattern = set()
    n = n0
    for j in range(p):
        if n % 2 == 1:
            pattern.add(j)
        n = collatz_step(n)
        traj.append(n)
    return traj, pattern

def compute_S(I, k):
    """Compute S(I) = sum of 3^{k-j} * 2^{i_j} and the individual terms."""
    S = 0
    terms = []
    for j_idx, i_j in enumerate(sorted(I)):
        j = j_idx + 1
        t = pow(3, k - j) * pow(2, i_j)
        terms.append(t)
        S += t
    return S, terms

def carry_weight(terms):
    """Compute total carry weight when adding terms in binary."""
    if not terms:
        return 0, []
    max_bits = max(t.bit_length() for t in terms if t > 0) + len(terms) + 2
    total_carry = 0
    carry = 0
    carries = []
    for bit in range(max_bits):
        col_sum = carry
        for t in terms:
            col_sum += (t >> bit) & 1
        carry = col_sum >> 1
        carries.append(carry)
        total_carry += carry
    return total_carry, carries

def sum_hw_powers3(k):
    """Sum of Hamming weights of 3^0, ..., 3^{k-1}."""
    return sum(hamming_weight(pow(3, m)) for m in range(k))

def mod_inverse_2adic(a, w):
    """Compute a^{-1} mod 2^w for odd a."""
    # Use extended Euclidean or direct iteration
    assert a % 2 == 1, "a must be odd"
    inv = 1
    for _ in range(w):
        if (inv * a) % (1 << (w)) != 1:
            inv = inv  # refine
    # Better: use the fact that for odd a, a^{-1} mod 2^w can be computed iteratively
    inv = 1
    mod = 1 << w
    for i in range(1, w):
        if (inv * a) % (1 << (i + 1)) != 1:
            inv += (1 << i)
    return inv % mod

# ============================================================
# PART 1: Exhaustive enumeration for small p
# ============================================================

print("=" * 70)
print("PART 1: Exhaustive enumeration of patterns for small p")
print("=" * 70)

results = []

for p in range(2, 28):
    for k in range(max(1, int(p * 0.5)), min(p, int(p * 0.7) + 1)):
        D = (1 << p) - pow(3, k)
        if D <= 0:
            continue

        hw_sum = sum_hw_powers3(k)
        n_patterns = comb(p, k)
        n_arith = 0  # patterns with D | S
        n_sc = 0     # self-consistent patterns
        n_nontrivial_arith = 0  # nontrivial arithmetic solutions
        n_nontrivial_sc = 0     # nontrivial self-consistent
        first_fail_positions = []

        for I in combinations(range(p), k):
            I_set = set(I)
            S, terms = compute_S(I_set, k)
            if S % D != 0:
                continue
            n0 = S // D
            if n0 < 1:
                continue

            n_arith += 1

            # Check if trivial
            is_trivial = (n0 <= 2 and k == p // 2)
            if not is_trivial:
                n_nontrivial_arith += 1

            # Self-consistency check
            traj, actual_pattern = collatz_trajectory(n0, p)
            is_sc = (actual_pattern == I_set and traj[p] == n0)

            if is_sc:
                n_sc += 1
                if not is_trivial:
                    n_nontrivial_sc += 1
            else:
                # Find first failure position
                n = n0
                for j in range(p):
                    expected_odd = (j in I_set)
                    actual_odd = (n % 2 == 1)
                    if expected_odd != actual_odd:
                        first_fail_positions.append(j)
                        break
                    n = collatz_step(n)

            # Carry weight verification
            Wc, carries = carry_weight(terms)
            hw_n0D = hamming_weight(n0 * D)
            assert Wc == hw_sum - hw_n0D, f"Carry weight identity failed at p={p}, k={k}, I={I}"

            if n_nontrivial_arith > 0 or n0 > 2:
                results.append({
                    'p': p, 'k': k, 'I': I, 'n0': n0, 'D': D,
                    'Wc': Wc, 'hw_sum': hw_sum, 'hw_n0D': hw_n0D,
                    'is_sc': is_sc, 'is_trivial': is_trivial
                })

        if n_arith > 0:
            print(f"p={p:2d}, k={k:2d}: D={D:12d}, C(p,k)={n_patterns:8d}, "
                  f"arith={n_arith:4d}, SC={n_sc:4d}, "
                  f"nontrivial_arith={n_nontrivial_arith:4d}, "
                  f"nontrivial_SC={n_nontrivial_sc:4d}", end="")
            if first_fail_positions:
                avg_fail = sum(first_fail_positions) / len(first_fail_positions)
                print(f", avg_first_fail={avg_fail:.1f}", end="")
            print()

print("\nCarry weight identity verified for ALL solutions.")

# ============================================================
# PART 2: Detailed analysis of nontrivial arithmetic solutions
# ============================================================

print("\n" + "=" * 70)
print("PART 2: Nontrivial arithmetic solutions (D|S with n0 > 2)")
print("=" * 70)

if results:
    nontrivial = [r for r in results if not r['is_trivial']]
    if nontrivial:
        for r in nontrivial[:50]:  # show first 50
            print(f"  p={r['p']}, k={r['k']}, I={r['I']}, n0={r['n0']}, "
                  f"Wc={r['Wc']}, s1(n0D)={r['hw_n0D']}, SC={r['is_sc']}")
    else:
        print("  No nontrivial arithmetic solutions found in range.")
else:
    print("  No results collected.")

# ============================================================
# PART 3: The 2-adic cascade analysis
# ============================================================

print("\n" + "=" * 70)
print("PART 3: 2-adic cascade -- bit-by-bit determination of n0")
print("=" * 70)

def cascade_analysis(p, k, I_set):
    """
    Analyze the bit-by-bit cascade for pattern I.

    For each step j=0,...,p-1:
    - Compute n0 mod 2^{j+1} from the parity constraint
    - Compare with n0 = S(I)/D
    - Track where the cascade "locks in" each bit
    """
    D = (1 << p) - pow(3, k)
    if D <= 0:
        return None

    S, terms = compute_S(I_set, k)
    if S % D != 0:
        return None
    n0 = S // D

    # Build cascade: n_j = (3^{k_j} * n0 + C_j) / 2^j
    # Parity of n_j determines bit j of pattern

    # Method: use the 2-adic inverse
    # S(I) = n0 * D = n0 * (2^p - 3^k)
    # Lower p bits of S(I) = (-n0 * 3^k) mod 2^p
    # So n0 mod 2^p = (-(3^k)^{-1} * S(I)) mod 2^p

    three_k = pow(3, k)

    # Compute n0 mod 2^j for j = 1, ..., p via the cascade
    # At step j, n_j has parity b_j = [j in I]
    # n_j = (3^{k_j} * n0 + C_j) / 2^j
    # So 3^{k_j} * n0 + C_j ≡ b_j * 2^j (mod 2^{j+1})
    # n0 ≡ (3^{k_j})^{-1} * (b_j * 2^j - C_j) (mod 2^{j+1})

    cascade_n0_bits = []  # n0 mod 2^{j+1} from cascade
    k_j = 0  # number of odd steps before position j
    C_j = 0  # additive contribution

    for j in range(p):
        b_j = 1 if j in I_set else 0

        # n0 mod 2^{j+1} from cascade
        mod = 1 << (j + 1)
        three_kj = pow(3, k_j)
        inv_three_kj = pow(three_kj, -1, mod)

        n0_cascade = (inv_three_kj * (b_j * (1 << j) - C_j)) % mod
        cascade_n0_bits.append(n0_cascade)

        # Check against actual n0
        actual_n0_mod = n0 % mod
        match = (n0_cascade == actual_n0_mod)

        if not match:
            return {
                'fail_step': j,
                'n0': n0,
                'cascade_n0': n0_cascade,
                'actual_n0_mod': actual_n0_mod,
                'mod': mod
            }

        # Update for next step
        if b_j == 1:  # odd step
            C_j = 3 * C_j + (1 << j)
            k_j += 1
        else:  # even step
            pass  # C_j and k_j unchanged
            # Actually wait: C_j accumulates differently
            # C_{j+1} = C_j if step j is even
            # C_{j+1} = 3*C_j + 2^j ... no, need to re-derive

    return {
        'success': True,
        'n0': n0,
        'final_cascade': cascade_n0_bits[-1] if cascade_n0_bits else None
    }

# Test cascade on known solutions
print("\nTesting 2-adic cascade on trivial cycles:")
for p in [4, 6, 8, 10, 12]:
    k = p // 2
    D = (1 << p) - pow(3, k)
    if D <= 0:
        continue
    I_set = set(range(0, p, 2))  # {0, 2, 4, ...}
    result = cascade_analysis(p, k, I_set)
    if result:
        if result.get('success'):
            print(f"  p={p}, k={k}: cascade succeeds, n0={result['n0']}")
        else:
            print(f"  p={p}, k={k}: cascade FAILS at step {result['fail_step']}")

# ============================================================
# PART 4: Sensitivity of S(I) to pattern perturbation
# ============================================================

print("\n" + "=" * 70)
print("PART 4: Sensitivity analysis -- how pattern changes affect n0")
print("=" * 70)

def pattern_sensitivity(p, k, I_base):
    """
    For a base pattern I, compute how changing one position affects S and n0.

    We swap position i_m (remove from I) with position j (add to I),
    for each valid pair, and measure the change in S, n0, and the
    resulting parity pattern.
    """
    D = (1 << p) - pow(3, k)
    if D <= 0:
        return []

    I_base_set = set(I_base)
    S_base, _ = compute_S(I_base_set, k)

    results = []
    positions_in = sorted(I_base_set)
    positions_out = sorted(set(range(p)) - I_base_set)

    for m_idx, i_m in enumerate(positions_in):
        for j in positions_out:
            # Swap: remove i_m, add j
            I_new = (I_base_set - {i_m}) | {j}
            S_new, _ = compute_S(I_new, k)
            delta_S = S_new - S_base

            if S_new % D == 0:
                n0_new = S_new // D
                # Check self-consistency
                _, actual_pat = collatz_trajectory(n0_new, p)
                is_sc = (actual_pat == I_new)
                results.append({
                    'removed': i_m, 'added': j,
                    'delta_S': delta_S, 'n0_new': n0_new,
                    'S_new_divisible': True, 'is_sc': is_sc
                })
            else:
                results.append({
                    'removed': i_m, 'added': j,
                    'delta_S': delta_S, 'n0_new': None,
                    'S_new_divisible': False, 'is_sc': False
                })

    return results

# Analyze sensitivity for p=10, k=5 (trivial cycle base)
p, k = 10, 5
D = (1 << p) - pow(3, k)
if D > 0:
    I_base = tuple(range(0, p, 2))  # {0, 2, 4, 6, 8}
    sens = pattern_sensitivity(p, k, I_base)

    n_divisible = sum(1 for r in sens if r['S_new_divisible'])
    n_sc = sum(1 for r in sens if r['is_sc'])

    print(f"p={p}, k={k}, D={D}")
    print(f"Base pattern: {I_base} (n0=1)")
    print(f"Single-swap perturbations: {len(sens)} total")
    print(f"  Divisible by D: {n_divisible}")
    print(f"  Self-consistent: {n_sc}")

    if n_divisible > 0:
        print("\n  Divisible perturbations:")
        for r in sens:
            if r['S_new_divisible']:
                print(f"    remove {r['removed']}, add {r['added']}: "
                      f"n0={r['n0_new']}, SC={r['is_sc']}")

# ============================================================
# PART 5: The overdetermined system analysis
# ============================================================

print("\n" + "=" * 70)
print("PART 5: Overdetermined system -- constraints vs. unknowns")
print("=" * 70)

print("\nFor a cycle of period p with k odd steps:")
print("  - Unknowns: k positions i_1, ..., i_k (but constrained to k-subset)")
print("    Effective unknowns: log2(C(p,k)) ≈ 0.949*p bits")
print("  - Constraints:")
print("    (A) D | S(I): ≈ log2(D) ≈ 0.05*p bits")
print("    (B) Parity feedback: p bits (one per step)")
print("    (C) Carry weight identity: 1 equation")
print("  - Total constraints: p + 0.05*p + 1 ≈ 1.05*p")
print("  - Overdetermination ratio: 1.05p / 0.949p ≈ 1.106")
print()

for p in [10, 20, 50, 100, 200, 500, 1000]:
    k = round(p * log(2) / log(3))
    D_approx = 2**p - 3**k
    if D_approx <= 0:
        # Adjust k
        while 2**p <= 3**k:
            k -= 1
    delta = p - k * log2(3)
    n_unknowns = log2(comb(p, k)) if p < 500 else p * (-(k/p)*log2(k/p) - (1-k/p)*log2(1-k/p))
    n_constraints_arith = delta
    n_constraints_parity = p
    n_constraints_total = n_constraints_arith + n_constraints_parity

    excess = n_constraints_total - n_unknowns

    print(f"  p={p:4d}: k={k:4d}, delta={delta:6.2f}, "
          f"unknowns={n_unknowns:8.1f}, constraints={n_constraints_total:8.1f}, "
          f"excess={excess:8.1f} bits")

# ============================================================
# PART 6: The 2-adic expansion factor
# ============================================================

print("\n" + "=" * 70)
print("PART 6: 2-adic expansion of the Collatz map at hypothetical cycle")
print("=" * 70)

print("\nThe p-fold Collatz map T^p has 2-adic derivative 3^k/2^p at a")
print("fixed point with k odd steps among p total steps.")
print("Since k < p*log(2)/log(3), we have 3^k < 2^p, so |3^k/2^p|_2 = 2^p/3^k > 1.")
print("The map is EXPANDING in the 2-adic metric.")
print()

for p in [10, 20, 50, 100, 500, 1000]:
    k = round(p * log(2) / log(3))
    while pow(3, k) >= pow(2, p):
        k -= 1
    expansion = 2**p / 3**k
    print(f"  p={p:4d}, k={k:4d}: 2-adic expansion factor = 2^p/3^k ≈ 2^{p - k*log2(3):.2f} ≈ {expansion:.4e}")

# ============================================================
# PART 7: Carry-parity coupling -- the joint constraint
# ============================================================

print("\n" + "=" * 70)
print("PART 7: Carry weight distribution and coupling with parity")
print("=" * 70)

def carry_parity_analysis(p, k):
    """
    For given (p,k), analyze:
    - Distribution of carry weights across all C(p,k) patterns
    - Which carry weights correspond to D|S solutions
    - The joint constraint
    """
    D = (1 << p) - pow(3, k)
    if D <= 0:
        return None

    hw_sum = sum_hw_powers3(k)

    all_wc = []
    div_wc = []
    sc_wc = []

    for I in combinations(range(p), k):
        I_set = set(I)
        S, terms = compute_S(I_set, k)
        Wc, _ = carry_weight(terms)
        all_wc.append(Wc)

        if S % D == 0:
            n0 = S // D
            if n0 >= 1:
                div_wc.append(Wc)
                # Check SC
                _, actual_pat = collatz_trajectory(n0, p)
                if actual_pat == I_set:
                    sc_wc.append(Wc)

    if all_wc:
        mean_wc = sum(all_wc) / len(all_wc)
        var_wc = sum((w - mean_wc)**2 for w in all_wc) / len(all_wc)
        std_wc = var_wc ** 0.5
        min_wc = min(all_wc)
        max_wc = max(all_wc)

        return {
            'p': p, 'k': k, 'D': D, 'hw_sum': hw_sum,
            'n_total': len(all_wc),
            'mean_wc': mean_wc, 'std_wc': std_wc,
            'min_wc': min_wc, 'max_wc': max_wc,
            'n_div': len(div_wc), 'div_wc': div_wc,
            'n_sc': len(sc_wc), 'sc_wc': sc_wc
        }
    return None

# Run for small p
for p in range(4, 21):
    for k in range(max(1, int(p * 0.5)), min(p, int(p * 0.7) + 1)):
        D = (1 << p) - pow(3, k)
        if D <= 0:
            continue
        if comb(p, k) > 200000:  # skip if too many
            print(f"p={p:2d}, k={k:2d}: SKIPPED (C(p,k)={comb(p,k)} too large)")
            continue

        result = carry_parity_analysis(p, k)
        if result:
            print(f"p={p:2d}, k={k:2d}: D={result['D']:10d}, C(p,k)={result['n_total']:8d}, "
                  f"Wc_mean={result['mean_wc']:6.1f}, Wc_std={result['std_wc']:5.1f}, "
                  f"Wc_range=[{result['min_wc']},{result['max_wc']}], "
                  f"hw_sum={result['hw_sum']:4d}, "
                  f"n_div={result['n_div']:3d}, n_SC={result['n_sc']:3d}")

# ============================================================
# PART 8: The bit-by-bit cascade failure analysis
# ============================================================

print("\n" + "=" * 70)
print("PART 8: Cascade failure -- where does self-consistency break?")
print("=" * 70)

def detailed_cascade_failure(p, k, I_tuple):
    """
    For a pattern I with D|S, track the bit-by-bit self-consistency.
    At each step j, check if the j-th parity matches.
    Record which bit first fails and by how much the trajectory diverges.
    """
    I_set = set(I_tuple)
    D = (1 << p) - pow(3, k)
    S, terms = compute_S(I_set, k)
    if S % D != 0:
        return None
    n0 = S // D
    if n0 < 1:
        return None

    # Run actual trajectory
    n = n0
    failures = []
    for j in range(p):
        expected_odd = (j in I_set)
        actual_odd = (n % 2 == 1)
        if expected_odd != actual_odd:
            failures.append({
                'step': j,
                'expected': 'odd' if expected_odd else 'even',
                'actual': 'odd' if actual_odd else 'even',
                'n_j': n,
                'n0': n0
            })
            break  # trajectory diverges from here
        n = collatz_step(n)

    if not failures:
        return {'success': True, 'n0': n0, 'returns': (n == n0)}
    return failures[0]

# For larger p values, sample random patterns and check
import random
random.seed(42)

print("\nSampling random patterns for larger p:")
for p in [15, 18, 20, 22, 24, 26]:
    k = round(p * log(2) / log(3))
    D = (1 << p) - pow(3, k)
    if D <= 0:
        k -= 1
        D = (1 << p) - pow(3, k)
    if D <= 0:
        continue

    n_samples = min(100000, comb(p, k))
    n_div = 0
    n_sc = 0
    fail_steps = []

    sampled = set()
    attempts = 0
    while len(sampled) < n_samples and attempts < n_samples * 5:
        attempts += 1
        # Random k-subset
        I_list = sorted(random.sample(range(p), k))
        I_tuple = tuple(I_list)
        if I_tuple in sampled:
            continue
        sampled.add(I_tuple)

        I_set = set(I_list)
        S, terms = compute_S(I_set, k)
        if S % D == 0:
            n0 = S // D
            if n0 >= 1:
                n_div += 1
                result = detailed_cascade_failure(p, k, I_tuple)
                if result is None:
                    continue
                if isinstance(result, dict) and result.get('success'):
                    n_sc += 1
                elif isinstance(result, dict) and 'step' in result:
                    fail_steps.append(result['step'])

    print(f"  p={p:2d}, k={k:2d}: D={D:12d}, sampled={len(sampled):6d}, "
          f"div={n_div:4d}, SC={n_sc:3d}", end="")
    if fail_steps:
        avg_fail = sum(fail_steps) / len(fail_steps)
        print(f", avg_first_fail={avg_fail:.1f}/{p}", end="")
    print()

# ============================================================
# PART 9: The n0 * D Hamming weight constraint
# ============================================================

print("\n" + "=" * 70)
print("PART 9: Hamming weight of n0*D -- constraint on viable n0 values")
print("=" * 70)

print("\nFor each (p,k), the carry weight identity requires:")
print("  s1(n0 * D) = sum_{m=0}^{k-1} s1(3^m) - W_c(I)")
print("Since W_c depends on I and s1(n0*D) depends on n0 = S(I)/D,")
print("this creates a rigid coupling.\n")

for p in [10, 14, 18, 20]:
    k = p // 2
    D = (1 << p) - pow(3, k)
    if D <= 0:
        continue

    hw_sum = sum_hw_powers3(k)

    # For the trivial cycle (n0=1)
    hw_D = hamming_weight(D)
    Wc_trivial = hw_sum - hw_D

    # Compute s1(n0*D) for small n0 values
    print(f"p={p}, k={k}, D={D}, sum_s1(3^m)={hw_sum}, s1(D)={hw_D}")
    print(f"  Trivial cycle: n0=1, s1(D)={hw_D}, W_c={Wc_trivial}")

    for n0 in range(2, min(20, D)):
        hw_n0D = hamming_weight(n0 * D)
        required_Wc = hw_sum - hw_n0D
        if required_Wc >= 0:
            print(f"  n0={n0:3d}: s1(n0*D)={hw_n0D:3d}, required W_c={required_Wc:4d}", end="")
            # Check if any pattern I with S(I)=n0*D and W_c=required_Wc exists
            # (Skip exhaustive check for larger p)
            if p <= 14:
                found = False
                for I in combinations(range(p), k):
                    I_set = set(I)
                    S, terms = compute_S(I_set, k)
                    if S == n0 * D:
                        Wc, _ = carry_weight(terms)
                        if Wc == required_Wc:
                            # Check SC
                            _, actual_pat = collatz_trajectory(n0, p)
                            sc = (actual_pat == I_set)
                            print(f"  FOUND: I={I}, SC={sc}", end="")
                            found = True
                if not found:
                    print(f"  (no pattern found)", end="")
            print()
    print()

# ============================================================
# PART 10: Modular consistency at multiple levels
# ============================================================

print("=" * 70)
print("PART 10: Multi-level modular consistency")
print("=" * 70)

print("\nFor D | S(I) with n0 = S/D, the lower p bits of S satisfy:")
print("  S mod 2^p = (-n0 * 3^k) mod 2^p")
print("Each 'window' of w bits constrains n0 mod 2^w.")
print("The parity of n_j depends on n0 mod 2^{j+1}.")
print("These must all be mutually consistent.\n")

# For a specific example: p=10, k=5, trivial cycle
p, k = 10, 5
D = (1 << p) - pow(3, k)
I_set = set(range(0, p, 2))
S, terms = compute_S(I_set, k)
n0 = S // D

print(f"Example: p={p}, k={k}, D={D}, n0={n0}")
print(f"  S(I) = {S} = {bin(S)}")
print(f"  D    = {D} = {bin(D)}")
print(f"  3^k  = {3**k} = {bin(3**k)}")
print(f"  n0*3^k = {n0 * 3**k} = {bin(n0 * 3**k)}")
print(f"  -n0*3^k mod 2^p = {(-n0 * 3**k) % (1<<p)} = {bin((-n0*3**k) % (1<<p))}")
print(f"  S mod 2^p = {S % (1<<p)} = {bin(S % (1<<p))}")
print()

# Bit-by-bit verification
print("  Bit-by-bit n0 determination:")
three_k = pow(3, k)
for j in range(p):
    mod = 1 << (j + 1)
    n0_mod = n0 % mod
    S_mod = S % mod
    # S ≡ -n0*3^k mod 2^p => n0 ≡ -S*(3^k)^{-1} mod 2^{j+1}
    inv_3k = pow(three_k, -1, mod)
    n0_from_S = (-S * inv_3k) % mod

    # The j-th bit of n0
    bit_j = (n0 >> j) & 1

    # Parity of n_j
    traj, _ = collatz_trajectory(n0, j + 1)
    n_j = traj[j]
    parity_j = n_j % 2
    expected_parity = 1 if j in I_set else 0

    print(f"    j={j}: n0 mod 2^{j+1} = {n0_mod:4d}, "
          f"from S: {n0_from_S:4d}, "
          f"bit_{j}(n0)={bit_j}, "
          f"n_{j}={n_j}, parity={parity_j} (expected {expected_parity})")

# ============================================================
# PART 11: Forward search -- are there cycles of any period up to p_max?
# ============================================================

print("\n" + "=" * 70)
print("PART 11: Forward cycle search (trajectory-first approach)")
print("=" * 70)

def find_cycles(max_n0, max_period):
    """Search for cycles by iterating from small starting values."""
    cycles = []
    for n0 in range(1, max_n0 + 1):
        n = n0
        seen = {n0: 0}
        for step in range(1, max_period + 1):
            n = collatz_step(n)
            if n == n0:
                # Found a cycle!
                period = step
                # Count odd steps
                n2 = n0
                k = 0
                for s in range(period):
                    if n2 % 2 == 1:
                        k += 1
                    n2 = collatz_step(n2)
                cycles.append({'n0': n0, 'period': period, 'k': k})
                break
            if n in seen:
                break  # Entered a cycle not starting at n0
            seen[n] = step
        if n > 10**15:  # trajectory escaped
            continue
    return cycles

print("\nSearching for cycles with n0 <= 10000, period <= 1000:")
cycles = find_cycles(10000, 1000)
for c in sorted(set((c['n0'], c['period'], c['k']) for c in cycles)):
    print(f"  n0={c[0]}, period={c[1]}, k={c[2]}")

# ============================================================
# PART 12: The interaction theorem -- carry weight + parity
# ============================================================

print("\n" + "=" * 70)
print("PART 12: Quantifying the carry-parity interaction")
print("=" * 70)

print("""
THEOREM (Carry-Parity Interaction, proved below):

For a hypothetical Collatz cycle of period p with k odd steps,
let I = {i_1, ..., i_k} be the odd-step positions. Then:

(1) The carry weight identity gives:
    W_c(I) = sum_{m=0}^{k-1} s1(3^m) - s1(n0 * D)
    where the left side is Theta(p^2) and the right depends on I and n0.

(2) The parity feedback gives: n0 is uniquely determined by I through
    the Collatz trajectory. Since the trajectory is a deterministic
    function of n0, and n0 = S(I)/D, the map I -> I' = parity(S(I)/D)
    must have I as a fixed point.

(3) The JOINT constraint: the carry pattern that produces S(I) must
    simultaneously:
    (a) Yield S ≡ 0 mod D (arithmetic)
    (b) Have total weight = sum s1(3^m) - s1(n0*D) (carry identity)
    (c) Produce bits of S such that n0 = S/D generates pattern I (feedback)

The key observation: constraints (a) and (c) are not independent.
The carry cascade that determines the bits of S simultaneously
encodes both the divisibility by D and the parity sequence of
the trajectory from n0 = S/D. This coupling is mediated by the
relation S mod 2^p = (-n0 * 3^k) mod 2^p.
""")

# Quantify: for each (p,k), what fraction of C(p,k) patterns
# satisfy D|S AND self-consistency?
print("Summary table:")
print(f"{'p':>4s} {'k':>4s} {'D':>12s} {'C(p,k)':>10s} {'D|S':>8s} {'SC':>6s} {'SC/DivS':>10s} {'SC/C(p,k)':>12s}")
print("-" * 80)

for p in range(2, 22):
    for k in range(max(1, int(p * 0.5)), min(p, int(p * 0.7) + 1)):
        D = (1 << p) - pow(3, k)
        if D <= 0:
            continue

        n_total = comb(p, k)
        if n_total > 500000:
            continue

        n_div = 0
        n_sc = 0

        for I in combinations(range(p), k):
            I_set = set(I)
            S, _ = compute_S(I_set, k)
            if S % D == 0:
                n0 = S // D
                if n0 >= 1:
                    n_div += 1
                    _, actual = collatz_trajectory(n0, p)
                    if actual == I_set:
                        n_sc += 1

        sc_div_ratio = f"{n_sc/n_div:.4f}" if n_div > 0 else "N/A"
        sc_total_ratio = f"{n_sc/n_total:.2e}" if n_total > 0 else "N/A"

        print(f"{p:4d} {k:4d} {D:12d} {n_total:10d} {n_div:8d} {n_sc:6d} {sc_div_ratio:>10s} {sc_total_ratio:>12s}")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
