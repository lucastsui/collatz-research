"""
OVERDETERMINED PARITY TOWER ANALYSIS FOR COLLATZ CYCLES
========================================================

A Collatz cycle of period p with k odd steps at positions I = {i_1,...,i_k}
gives starting value n_0 = S(I)/D where D = 2^p - 3^k.

The parity tower: step j gives a congruence
    n_0 = alpha_j (mod 2^{j+1})
determined uniquely by the pattern I.

After all p steps: n_0 = alpha (mod 2^p), uniquely determined.
But n_0 = S(I)/D, so n_0 is also algebraically determined.

Key question: Is the overdetermination (p constraints on ~0.37p unknowns)
enough to force no solutions?

This script investigates:
1. The tower of congruences for each (p,k,I)
2. Whether n_0 = S(I)/D satisfies the tower
3. The relationship between S(I)/D and the 2-adic tower value
4. Independence structure of the constraints
5. Empirical scaling of the failure rate
"""

from itertools import combinations
from math import log, log2, gcd, comb
from collections import Counter, defaultdict
import sys

# ============================================================================
# Core functions
# ============================================================================

def compute_S(I, k):
    """Compute S(I) = sum_{j=1}^k 3^{k-j} * 2^{i_j}."""
    S = 0
    for j_idx, i_j in enumerate(I):
        j = j_idx + 1
        S += pow(3, k - j) * pow(2, i_j)
    return S

def collatz_step(n):
    """Compressed Collatz: odd -> (3n+1)/2, even -> n/2."""
    if n % 2 == 1:
        return (3 * n + 1) // 2
    else:
        return n // 2

def collatz_trajectory(n0, p):
    """Run p compressed Collatz steps from n0.
    Returns (parity_set, trajectory_list)."""
    traj = [n0]
    parities = set()
    n = n0
    for j in range(p):
        if n % 2 == 1:
            parities.add(j)
        n = collatz_step(n)
        traj.append(n)
    return parities, traj

def is_self_consistent(I_tuple, k, p, n0):
    """Check if n_0's Collatz trajectory reproduces pattern I and closes."""
    I_set = set(I_tuple)
    parities, traj = collatz_trajectory(n0, p)
    cycle_closes = (traj[p] == n0)
    parity_matches = (parities == I_set)
    return cycle_closes and parity_matches

# ============================================================================
# 2-adic tower computation
# ============================================================================

def compute_tower_residue(I_tuple, k, p):
    """
    Compute the 2-adic tower value: the unique n_0 mod 2^p determined
    by the parity constraints.

    At step j: n_j = (3^{k_j} * n_0 + C_j) / 2^j
    Parity: n_j = b_j (mod 2)
    => 3^{k_j} * n_0 + C_j = b_j * 2^j (mod 2^{j+1})
    => n_0 = (b_j * 2^j - C_j) * (3^{k_j})^{-1} (mod 2^{j+1})

    Returns: (tower_value mod 2^p, list of intermediate residues)
    """
    I_set = set(I_tuple)

    mult = 1   # 3^{k_j}
    add = 0    # C_j (not divided by 2^j; it's the raw accumulated value)

    residues = []

    for j in range(p):
        b_j = 1 if j in I_set else 0

        modulus = 1 << (j + 1)
        target = (b_j * (1 << j) - add) % modulus
        mult_inv = pow(mult, -1, modulus)
        n0_residue = (target * mult_inv) % modulus

        residues.append((n0_residue, modulus))

        # Update for next step
        if j in I_set:
            add = 3 * add + (1 << j)
            mult = 3 * mult

    # Final tower value: n_0 mod 2^p
    tower_val = residues[-1][0] if residues else 0
    return tower_val, residues

def verify_tower_consistency(residues):
    """Check that the tower of congruences is internally consistent:
    each n_0 mod 2^{j+1} must agree with n_0 mod 2^j from the previous step."""
    for j in range(1, len(residues)):
        prev_res, prev_mod = residues[j-1]
        curr_res, curr_mod = residues[j]
        if curr_res % prev_mod != prev_res:
            return False, j
    return True, -1

# ============================================================================
# Experiment 1: Tower vs cycle equation comparison
# ============================================================================

def tower_vs_cycle_equation(p_max=22):
    """
    For each (p,k,I) with D|S(I), compare:
    1. n_0 = S(I)/D (cycle equation)
    2. alpha = tower value mod 2^p

    Check: does n_0 = alpha (mod 2^p)?
    If n_0 < 2^p, this means n_0 = alpha (they must be equal).

    Also check self-consistency (actual Collatz trajectory matches I).
    """
    print("=" * 100)
    print("EXPERIMENT 1: TOWER OF CONGRUENCES vs CYCLE EQUATION")
    print("=" * 100)
    print(f"{'p':>4} {'k':>4} {'C(p,k)':>10} {'D':>12} {'|D|S|':>7} "
          f"{'tower=n0':>10} {'SC':>5} {'n0_bits':>8} {'tower_bits':>10}")

    all_results = []

    for p in range(2, p_max + 1):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 5_000_000:
                continue

            div_count = 0
            tower_match_count = 0
            sc_count = 0
            n0_bits_list = []

            for I in combinations(range(p), k):
                S = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                div_count += 1

                # Compute tower value
                tower_val, residues = compute_tower_residue(I, k, p)

                # Check tower matches n0
                tower_matches = (n0 % (1 << p) == tower_val)
                if tower_matches:
                    tower_match_count += 1

                # Check self-consistency
                sc = is_self_consistent(I, k, p, n0)
                if sc:
                    sc_count += 1

                n0_bits_list.append(n0.bit_length())

            if div_count > 0:
                avg_n0_bits = sum(n0_bits_list) / len(n0_bits_list) if n0_bits_list else 0
                print(f"{p:4d} {k:4d} {total:10d} {D:12d} {div_count:7d} "
                      f"{tower_match_count:10d} {sc_count:5d} "
                      f"{avg_n0_bits:8.1f} {p:10d}")
                all_results.append({
                    'p': p, 'k': k, 'total': total, 'D': D,
                    'div_count': div_count, 'tower_match': tower_match_count,
                    'sc_count': sc_count, 'avg_n0_bits': avg_n0_bits
                })

    return all_results

# ============================================================================
# Experiment 2: The 2-adic identity: tower = S/D mod 2^p?
# ============================================================================

def twoadic_identity_test(p_max=22):
    """
    Test the KEY IDENTITY:

    Is it always true that S(I)/D = tower_val (mod 2^p)?

    If yes: the tower adds NO new constraints beyond D|S(I).
    If no: the tower provides additional constraints.
    """
    print("\n" + "=" * 100)
    print("EXPERIMENT 2: 2-ADIC IDENTITY TEST")
    print("Does n_0 = S/D always = tower(I) mod 2^p?")
    print("=" * 100)

    total_patterns = 0
    identity_holds = 0
    identity_fails = 0
    sc_and_identity = 0
    nosc_and_identity = 0
    sc_and_noidentity = 0
    nosc_and_noidentity = 0

    for p in range(4, p_max + 1):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 5_000_000:
                continue

            p_patterns = 0
            p_identity = 0
            p_sc = 0

            for I in combinations(range(p), k):
                S = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                total_patterns += 1
                p_patterns += 1

                tower_val, _ = compute_tower_residue(I, k, p)
                id_holds = (n0 % (1 << p) == tower_val)
                sc = is_self_consistent(I, k, p, n0)

                if id_holds:
                    identity_holds += 1
                    p_identity += 1
                else:
                    identity_fails += 1

                if sc and id_holds:
                    sc_and_identity += 1
                    p_sc += 1
                elif sc and not id_holds:
                    sc_and_noidentity += 1
                elif not sc and id_holds:
                    nosc_and_identity += 1
                else:
                    nosc_and_noidentity += 1

            if p_patterns > 0:
                print(f"p={p:2d}, k={k:2d}: {p_patterns:6d} patterns, "
                      f"{p_identity:6d} tower=n0 ({p_identity/p_patterns*100:5.1f}%), "
                      f"{p_sc:6d} SC ({p_sc/p_patterns*100:5.1f}%)")

    print(f"\n{'='*60}")
    print(f"TOTALS: {total_patterns} patterns tested")
    print(f"  Identity holds: {identity_holds} ({identity_holds/total_patterns*100:.1f}%)")
    print(f"  Identity fails: {identity_fails} ({identity_fails/total_patterns*100:.1f}%)")
    print(f"\nCross-tabulation:")
    print(f"  SC and identity:    {sc_and_identity}")
    print(f"  SC but no identity: {sc_and_noidentity}")
    print(f"  No SC but identity: {nosc_and_identity}")
    print(f"  No SC no identity:  {nosc_and_noidentity}")

    if sc_and_noidentity > 0:
        print("\n!!! ANOMALY: Self-consistent patterns where tower != n_0 !!!")
    if nosc_and_identity > 0:
        print("\n!!! ANOMALY: Tower = n_0 but not self-consistent !!!")
    else:
        print("\nCONCLUSION: tower=n0 <==> self-consistent (as expected)")

# ============================================================================
# Experiment 3: First failure position in parity tower
# ============================================================================

def first_failure_analysis(p_max=20):
    """
    For patterns with D|S(I) that fail self-consistency:
    At which step j does the parity first mismatch?
    """
    print("\n" + "=" * 100)
    print("EXPERIMENT 3: FIRST PARITY FAILURE POSITION")
    print("=" * 100)

    failure_dist = defaultdict(lambda: Counter())
    total_by_p = Counter()
    fails_by_p = Counter()

    for p in range(4, p_max + 1):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 3_000_000:
                continue

            for I in combinations(range(p), k):
                S = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                total_by_p[p] += 1
                I_set = set(I)

                # Trace trajectory and find first mismatch
                n = n0
                first_fail = None
                for j in range(p):
                    expected_odd = (j in I_set)
                    actual_odd = (n % 2 == 1)
                    if expected_odd != actual_odd:
                        first_fail = j
                        break
                    n = collatz_step(n)

                if first_fail is not None:
                    fails_by_p[p] += 1
                    failure_dist[p][first_fail] += 1

    # Print summary
    for p in sorted(total_by_p.keys()):
        t = total_by_p[p]
        f = fails_by_p[p]
        if t > 0:
            print(f"\np={p}: {t} patterns with D|S, {f} fail ({f/t*100:.1f}%)")
            if f > 0:
                dist = failure_dist[p]
                for pos in sorted(dist.keys()):
                    cnt = dist[pos]
                    print(f"  First fail at step {pos}: {cnt} ({cnt/f*100:.1f}% of failures)")

    return failure_dist, total_by_p, fails_by_p

# ============================================================================
# Experiment 4: Conditional probability analysis (independence test)
# ============================================================================

def independence_test(p_max=20):
    """
    For patterns with D|S(I), check parity step by step.
    At step j, what is the conditional probability that step j matches,
    given steps 0..j-1 all match?

    If independent: P(match at j | matches at 0..j-1) ~ 1/2
    If dependent: this conditional probability varies.
    """
    print("\n" + "=" * 100)
    print("EXPERIMENT 4: CONDITIONAL PARITY MATCH PROBABILITIES")
    print("=" * 100)

    for p in range(8, min(p_max + 1, 22)):
        for k in range(max(1, int(p * 0.5)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 2_000_000:
                continue

            # Track survival at each step
            survived = [0] * (p + 1)

            for I in combinations(range(p), k):
                S = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                survived[0] += 1
                I_set = set(I)

                n = n0
                for j in range(p):
                    expected_odd = (j in I_set)
                    actual_odd = (n % 2 == 1)
                    if expected_odd != actual_odd:
                        break
                    survived[j + 1] += 1
                    n = collatz_step(n)

            if survived[0] > 5:
                print(f"\np={p}, k={k}: {survived[0]} patterns with D|S")
                print(f"  Step-by-step survival:")
                for j in range(p + 1):
                    if survived[j] > 0:
                        if j > 0 and survived[j-1] > 0:
                            cond_prob = survived[j] / survived[j-1]
                            print(f"    After step {j:2d}: {survived[j]:6d} survive "
                                  f"(cond. prob: {cond_prob:.4f})")
                        else:
                            print(f"    After step {j:2d}: {survived[j]:6d} survive")
                    else:
                        print(f"    After step {j:2d}: 0 survive (all eliminated)")
                        break

# ============================================================================
# Experiment 5: Scaling of self-consistency rate
# ============================================================================

def scaling_analysis(p_max=24):
    """
    For each (p,k), compute the fraction of D|S patterns that are SC.
    Track the log2 of the SC rate and compare with the overdetermination prediction.
    """
    print("\n" + "=" * 100)
    print("EXPERIMENT 5: SCALING OF SELF-CONSISTENCY RATE")
    print("=" * 100)
    print(f"{'p':>4} {'k':>4} {'|D|S|':>8} {'|SC|':>6} {'SC_rate':>12} "
          f"{'log2(rate)':>12} {'avg_log2_n0':>12} {'excess=p-bits':>14} "
          f"{'expected_log2':>14}")

    summary = []

    for p in range(4, p_max + 1):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 10_000_000:
                continue

            div_count = 0
            sc_count = 0
            n0_bits_sum = 0

            for I in combinations(range(p), k):
                S = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                div_count += 1
                n0_bits_sum += n0.bit_length()

                sc = is_self_consistent(I, k, p, n0)
                if sc:
                    sc_count += 1

            if div_count > 2:
                sc_rate = sc_count / div_count
                log2_rate = log2(sc_rate) if sc_rate > 0 else float('-inf')
                avg_bits = n0_bits_sum / div_count
                excess = p - avg_bits
                expected_log2 = -excess

                print(f"{p:4d} {k:4d} {div_count:8d} {sc_count:6d} {sc_rate:12.8f} "
                      f"{log2_rate:12.3f} {avg_bits:12.2f} {excess:14.2f} "
                      f"{expected_log2:14.2f}")

                summary.append({
                    'p': p, 'k': k, 'div_count': div_count, 'sc_count': sc_count,
                    'sc_rate': sc_rate, 'log2_rate': log2_rate,
                    'avg_bits': avg_bits, 'excess': excess
                })

    return summary

# ============================================================================
# Experiment 6: Bit-by-bit constraint satisfaction
# ============================================================================

def bit_constraint_analysis(p_max=18):
    """
    For each pattern with D|S(I), check bit-by-bit whether n_0 = S/D
    satisfies the tower constraint at each level.
    """
    print("\n" + "=" * 100)
    print("EXPERIMENT 6: BIT-BY-BIT CONSTRAINT SATISFACTION")
    print("=" * 100)

    for p in range(6, min(p_max + 1, 20)):
        for k in range(max(1, int(p * 0.5)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 1_000_000:
                continue

            bit_matches = [0] * p
            tested = 0
            sc_count = 0

            for I in combinations(range(p), k):
                S = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                tested += 1
                tower_val, residues = compute_tower_residue(I, k, p)

                for j in range(p):
                    res_j, mod_j = residues[j]
                    if n0 % mod_j == res_j:
                        bit_matches[j] += 1

                sc = is_self_consistent(I, k, p, n0)
                if sc:
                    sc_count += 1

            if tested > 5:
                print(f"\np={p}, k={k}: {tested} patterns with D|S, {sc_count} self-consistent")
                print(f"  Bit-by-bit tower match rates:")
                for j in range(p):
                    rate = bit_matches[j] / tested
                    print(f"    bit {j:2d} (mod 2^{j+1:2d}): {bit_matches[j]:6d}/{tested:6d} = {rate:.4f}")

# ============================================================================
# Experiment 7: Combined constraint summary
# ============================================================================

def combined_constraint_count(p_max=24):
    """
    Summary of all constraints and their cumulative effect.
    """
    print("\n" + "=" * 100)
    print("EXPERIMENT 7: COMBINED CONSTRAINT ANALYSIS")
    print("=" * 100)
    print(f"{'p':>4} {'k':>4} {'C(p,k)':>12} {'|D|S|':>8} {'|SC|':>6} "
          f"{'log2 C/D':>10} {'log2 SC/C':>10} {'log2 SC rate':>12}")

    for p in range(4, p_max + 1):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 10_000_000:
                continue

            div_count = 0
            sc_count = 0

            for I in combinations(range(p), k):
                S = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                div_count += 1
                sc = is_self_consistent(I, k, p, n0)
                if sc:
                    sc_count += 1

            if div_count > 0:
                log2_cd = log2(total / D) if total > D else 0
                log2_sc_total = log2(sc_count / total) if sc_count > 0 else float('-inf')
                sc_rate = sc_count / div_count
                log2_sc_rate = log2(sc_rate) if sc_rate > 0 else float('-inf')

                print(f"{p:4d} {k:4d} {total:12d} {div_count:8d} {sc_count:6d} "
                      f"{log2_cd:10.3f} {log2_sc_total:10.3f} {log2_sc_rate:12.3f}")

# ============================================================================
# Experiment 8: Tower value range analysis
# ============================================================================

def tower_range_analysis(p_max=20):
    """
    For each (p,k), examine the range of n_0 values vs tower values.
    """
    print("\n" + "=" * 100)
    print("EXPERIMENT 8: TOWER VALUE RANGE AND n_0 COMPARISON")
    print("=" * 100)

    for p in range(6, min(p_max + 1, 20)):
        for k in range(max(1, int(p * 0.5)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 1_000_000:
                continue

            n0_values = []
            tower_values = []
            matches = 0
            tested = 0

            for I in combinations(range(p), k):
                S = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                tested += 1
                tower_val, _ = compute_tower_residue(I, k, p)
                n0_values.append(n0)
                tower_values.append(tower_val)

                if n0 == tower_val:
                    matches += 1

            if tested > 5:
                n0_max = max(n0_values)
                n0_min = min(n0_values)
                tower_max = max(tower_values)
                tower_min = min(tower_values)

                print(f"\np={p}, k={k}: {tested} patterns")
                print(f"  n0 range: [{n0_min}, {n0_max}] ({n0_max.bit_length()} bits)")
                print(f"  tower range: [{tower_min}, {tower_max}] ({tower_max.bit_length()} bits)")
                print(f"  Matches (tower=n0): {matches}/{tested} = {matches/tested*100:.1f}%")
                print(f"  n0_max / 2^p = {n0_max / (1 << p):.6f}")


# ============================================================================
# Main
# ============================================================================

if __name__ == "__main__":
    print("OVERDETERMINED PARITY TOWER ANALYSIS FOR COLLATZ CYCLES")
    print("=" * 100)

    print("\n\n")
    r1 = tower_vs_cycle_equation(p_max=22)

    print("\n\n")
    r2 = twoadic_identity_test(p_max=22)

    print("\n\n")
    r3 = first_failure_analysis(p_max=20)

    print("\n\n")
    r4 = independence_test(p_max=20)

    print("\n\n")
    r5 = scaling_analysis(p_max=24)

    print("\n\n")
    r7 = combined_constraint_count(p_max=24)

    print("\n\n")
    r6 = bit_constraint_analysis(p_max=18)

    print("\n\n")
    r8 = tower_range_analysis(p_max=20)

    print("\n\nDONE.")
