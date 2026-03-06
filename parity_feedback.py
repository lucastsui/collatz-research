"""
Parity Feedback Analysis for Collatz Cycles
============================================
Investigates the self-consistency constraint: the parity pattern I that
defines a hypothetical cycle must be reproduced when the Collatz map is
applied to the starting value n_0 = S(I)/D.

This script:
1. Formalizes self-consistency as a system of congruences mod 2.
2. For each (p,k,I) with D|S(I), checks whether the Collatz trajectory
   from n_0 reproduces the parity pattern I.
3. Measures the self-consistency failure rate.
4. Analyzes the interaction between carry structure and parity feedback.
5. Explores symbolic dynamics / kneading-type conditions.
"""

from itertools import combinations
from math import log, log2, gcd, comb
import sys

# ============================================================================
# Part 1: Core functions
# ============================================================================

def compute_S(I, k):
    """Compute S(I) = sum_{j=1}^k 3^{k-j} * 2^{i_j}."""
    S = 0
    terms = []
    for j_idx, i_j in enumerate(I):
        j = j_idx + 1
        t = pow(3, k - j) * pow(2, i_j)
        terms.append(t)
        S += t
    return S, terms

def collatz_step(n):
    """One step of the compressed Collatz map: if odd, (3n+1)/2; if even, n/2."""
    if n % 2 == 1:
        return (3 * n + 1) // 2
    else:
        return n // 2

def collatz_trajectory(n0, p):
    """Run p steps of the compressed Collatz map from n0.
    Returns (trajectory, parity_pattern).
    trajectory[j] = n_j for j=0,...,p.
    parity_pattern = set of positions j where n_j is odd.
    """
    traj = [n0]
    parities = set()
    n = n0
    for j in range(p):
        if n % 2 == 1:
            parities.add(j)
        n = collatz_step(n)
        traj.append(n)
    return traj, parities

def is_self_consistent(I_tuple, k, p, n0):
    """Check if the pattern I is self-consistent: the Collatz trajectory
    from n0 must reproduce the parity pattern I, and n_p = n_0."""
    I_set = set(I_tuple)
    traj, parities = collatz_trajectory(n0, p)

    # Check cycle closure
    cycle_closes = (traj[p] == n0)
    # Check parity match
    parity_matches = (parities == I_set)

    return cycle_closes, parity_matches, traj, parities

def hamming_weight(n):
    return bin(n).count('1')

def carry_weight(terms):
    """Total carry generated when adding terms in binary."""
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


# ============================================================================
# Part 2: The self-consistency as congruences mod 2
# ============================================================================

def parity_congruences_mod2(I_tuple, k, p):
    """
    Derive the system of mod-2 congruences that n_0 must satisfy.

    For a cycle with pattern I:
      n_0 * (2^p - 3^k) = S(I)
    gives n_0 = S(I) / D.

    The parity of n_j for j=0,...,p-1 must match I.

    Each n_j can be expressed as:
      n_j = (3^{k_j} * n_0 + C_j) / 2^j
    where k_j = |I cap {0,...,j-1}| and C_j accumulates the +1 terms.

    Parity: n_j = b_j (mod 2) where b_j = [j in I].
    This gives: 3^{k_j} * n_0 + C_j = b_j * 2^j (mod 2^{j+1}).

    Returns: list of (n0_residue, modulus, step_j, expected_parity) tuples.
    """
    I_set = set(I_tuple)

    mult = 1  # 3^{k_j}
    add = 0   # C_j (accumulated +1 contributions, scaled by 2^j)

    constraints = []

    for j in range(p):
        b_j = 1 if j in I_set else 0

        # n_j * 2^j = mult * n_0 + add
        # Parity: ((mult * n_0 + add) / 2^j) % 2 = b_j
        # Equivalently: bit j of (mult * n_0 + add) = b_j
        # i.e., (mult * n_0 + add) = b_j * 2^j (mod 2^{j+1})

        modulus = 1 << (j + 1)
        target = (b_j * (1 << j) - add) % modulus

        # Since mult = 3^{k_j} is odd, it's invertible mod 2^{j+1}
        mult_inv = pow(mult, -1, modulus)
        n0_residue = (target * mult_inv) % modulus

        constraints.append((n0_residue, modulus, j, b_j))

        # Update for next step
        if j in I_set:
            mult = 3 * mult
            add = 3 * add + (1 << j)

    return constraints


# ============================================================================
# Part 3: Exhaustive search and self-consistency check
# ============================================================================

def exhaustive_check(p_max=22):
    """For each (p,k,I) with D|S(I), check self-consistency."""

    print("=" * 80)
    print("PART 3: EXHAUSTIVE SELF-CONSISTENCY CHECK")
    print("=" * 80)

    total_divisible = 0
    total_self_consistent = 0

    for p in range(2, p_max + 1):
        for k in range(max(1, int(p * 0.4)), min(p, int(p * 0.7) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            div_count = 0
            sc_count = 0

            if comb(p, k) > 5_000_000:
                continue

            for I in combinations(range(p), k):
                S, terms = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                div_count += 1
                total_divisible += 1

                cycle_closes, parity_matches, traj, parities = is_self_consistent(I, k, p, n0)

                if cycle_closes and parity_matches:
                    sc_count += 1
                    total_self_consistent += 1
                    print(f"  [SELF-CONSISTENT] p={p}, k={k}, I={I}, n0={n0}")
                else:
                    reasons = []
                    if not cycle_closes:
                        reasons.append(f"cycle doesn't close (n_p={traj[p]} != n0={n0})")
                    if not parity_matches:
                        expected = set(I)
                        actual = parities
                        diff = expected.symmetric_difference(actual)
                        reasons.append(f"parity mismatch at positions {sorted(diff)}")
                    print(f"  [FAILS] p={p}, k={k}, I={I}, n0={n0}: {'; '.join(reasons)}")

            if div_count > 0:
                print(f"  SUMMARY p={p}, k={k}: {div_count} patterns with D|S, "
                      f"{sc_count} self-consistent "
                      f"({sc_count/div_count*100:.1f}%)")

    print(f"\nGRAND TOTAL: {total_divisible} patterns with D|S, "
          f"{total_self_consistent} self-consistent")
    return total_divisible, total_self_consistent


# ============================================================================
# Part 4: Self-consistency failure rate by bit position
# ============================================================================

def failure_rate_by_bit(p_max=20):
    """For each pattern I with D|S(I), find the FIRST bit position
    where the parity constraint fails."""

    print("\n" + "=" * 80)
    print("PART 4: FAILURE POSITION ANALYSIS")
    print("=" * 80)

    from collections import Counter
    failure_positions = Counter()
    total_fails = 0
    total_tested = 0

    for p in range(2, p_max + 1):
        for k in range(max(1, int(p * 0.4)), min(p, int(p * 0.7) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            if comb(p, k) > 2_000_000:
                continue

            for I in combinations(range(p), k):
                S, terms = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                total_tested += 1
                I_set = set(I)

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
                    failure_positions[first_fail] += 1
                    total_fails += 1

    print(f"\nTotal patterns tested (with D|S): {total_tested}")
    print(f"Total failures: {total_fails}")
    if total_tested > 0:
        print(f"Failure rate: {total_fails/total_tested*100:.1f}%")

    if failure_positions:
        print("\nFirst failure position distribution:")
        for pos in sorted(failure_positions.keys()):
            count = failure_positions[pos]
            pct = count / total_fails * 100 if total_fails > 0 else 0
            print(f"  Position {pos}: {count} ({pct:.1f}%)")

    return failure_positions


# ============================================================================
# Part 5: Degrees of Freedom Analysis
# ============================================================================

def degrees_of_freedom(p_max=22):
    """
    Count effective degrees of freedom after self-consistency.
    """

    print("\n" + "=" * 80)
    print("PART 5: DEGREES OF FREEDOM ANALYSIS")
    print("=" * 80)
    print(f"{'p':>4} {'k':>4} {'C(p,k)':>12} {'D':>15} {'|D|S|':>8} "
          f"{'|SC|':>6} {'D|S/C(p,k)':>12} {'SC/D|S':>10} {'SC/C(p,k)':>12}")

    for p in range(2, p_max + 1):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 5_000_000:
                continue

            div_count = 0
            sc_count = 0

            for I in combinations(range(p), k):
                S, terms = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                div_count += 1

                cycle_closes, parity_matches, _, _ = is_self_consistent(I, k, p, n0)
                if cycle_closes and parity_matches:
                    sc_count += 1

            if div_count > 0:
                ratio_ds = div_count / total
                ratio_sc = sc_count / div_count if div_count > 0 else 0
                ratio_total = sc_count / total
            else:
                ratio_ds = 0
                ratio_sc = 0
                ratio_total = 0

            print(f"{p:4d} {k:4d} {total:12d} {D:15d} {div_count:8d} "
                  f"{sc_count:6d} {ratio_ds:12.2e} {ratio_sc:10.4f} {ratio_total:12.2e}")


# ============================================================================
# Part 6: Self-consistency failure rate scaling (KEY COMPUTATION)
# ============================================================================

def failure_rate_scaling(p_max=24):
    """
    The critical question: among patterns with D|S(I), what fraction
    are self-consistent?

    If this fraction is f(p), then the expected number of nontrivial cycles is:
      C(p,k) * (1/D) * f(p)

    We need C(p,k)/D * f(p) < 1 for large p.
    C(p,k)/D ~ 2^{0.899p}.
    So we need f(p) < 2^{-0.899p}, i.e., the self-consistency must eliminate
    a 2^{-0.899p} fraction.
    """

    print("\n" + "=" * 80)
    print("PART 6: SELF-CONSISTENCY FAILURE RATE SCALING")
    print("=" * 80)
    print(f"{'p':>4} {'k':>4} {'C(p,k)':>12} {'D':>15} {'|D|S|':>8} "
          f"{'|SC|':>6} {'SC_rate':>12} {'log2(SC_rate)':>14} {'C(p,k)/D':>12}")

    results = []

    for p in range(2, p_max + 1):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 8_000_000:
                continue

            div_count = 0
            sc_count = 0

            for I in combinations(range(p), k):
                S, terms = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                div_count += 1

                cycle_closes, parity_matches, _, _ = is_self_consistent(I, k, p, n0)
                if cycle_closes and parity_matches:
                    sc_count += 1

            if div_count > 0:
                sc_rate = sc_count / div_count
                log2_sc = log2(sc_rate) if sc_rate > 0 else float('-inf')
                cpk_over_d = total / D

                results.append((p, k, total, D, div_count, sc_count, sc_rate, log2_sc))

                print(f"{p:4d} {k:4d} {total:12d} {D:15d} {div_count:8d} "
                      f"{sc_count:6d} {sc_rate:12.6f} {log2_sc:14.2f} {cpk_over_d:12.2f}")

    return results


# ============================================================================
# Part 7: Information-theoretic analysis
# ============================================================================

def information_analysis(p_max=22):
    """Quantify the information content of the self-consistency constraint."""

    print("\n" + "=" * 80)
    print("PART 7: INFORMATION-THEORETIC ANALYSIS")
    print("=" * 80)
    print(f"{'p':>4} {'k':>4} {'H(I)':>8} {'log2(n0_max)':>14} "
          f"{'deficit':>8} {'|D|S|':>8} {'|SC|':>6} {'log2(|D|S|/|SC|)':>18}")

    for p in range(4, p_max + 1):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 3_000_000:
                continue

            H_I = log2(total) if total > 1 else 0

            div_count = 0
            sc_count = 0
            n0_vals = []

            for I in combinations(range(p), k):
                S, terms = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                div_count += 1
                n0_vals.append(n0)

                cycle_closes, parity_matches, _, _ = is_self_consistent(I, k, p, n0)
                if cycle_closes and parity_matches:
                    sc_count += 1

            if div_count > 0:
                n0_max = max(n0_vals) if n0_vals else 1
                log2_n0max = log2(n0_max) if n0_max > 1 else 0
                deficit = H_I - log2_n0max

                if div_count > sc_count and sc_count > 0:
                    log2_ratio = log2(div_count / sc_count)
                elif sc_count == 0 and div_count > 0:
                    log2_ratio = float('inf')
                else:
                    log2_ratio = 0

                print(f"{p:4d} {k:4d} {H_I:8.2f} {log2_n0max:14.2f} "
                      f"{deficit:8.2f} {div_count:8d} {sc_count:6d} "
                      f"{log2_ratio:18.2f}")


# ============================================================================
# Part 8: Carry-parity interaction
# ============================================================================

def carry_parity_interaction(p_max=18):
    """Analyze how carry weight relates to self-consistency success/failure."""

    print("\n" + "=" * 80)
    print("PART 8: CARRY-PARITY INTERACTION")
    print("=" * 80)

    for p in range(6, min(p_max + 1, 20)):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            if comb(p, k) > 2_000_000:
                continue

            sc_cws = []
            fail_cws = []

            for I in combinations(range(p), k):
                S, terms = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                Wc, carries = carry_weight(terms)

                cycle_closes, parity_matches, _, _ = is_self_consistent(I, k, p, n0)

                if cycle_closes and parity_matches:
                    sc_cws.append(Wc)
                else:
                    fail_cws.append(Wc)

            if sc_cws or fail_cws:
                sc_str = f"SC: mean={sum(sc_cws)/len(sc_cws):.1f}" if sc_cws else "SC: none"
                fail_str = f"Fail: mean={sum(fail_cws)/len(fail_cws):.1f}, count={len(fail_cws)}" if fail_cws else "Fail: none"
                print(f"  p={p}, k={k}: {sc_str}; {fail_str}")


# ============================================================================
# Part 9: Kneading analysis
# ============================================================================

def kneading_analysis(p_max=16):
    """Find all genuine cycles by forward search from n_0 values."""

    print("\n" + "=" * 80)
    print("PART 9: KNEADING / CYCLE SEARCH")
    print("=" * 80)

    for p in range(4, min(p_max + 1, 16)):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            S_max = sum(pow(3, k - j - 1) * pow(2, p - k + j) for j in range(k))
            n0_max = S_max // D + 1

            if n0_max > 100000:
                continue

            valid_cycles = []
            for n0 in range(1, min(n0_max + 1, 100001)):
                traj, parities = collatz_trajectory(n0, p)
                if traj[p] == n0 and len(parities) == k:
                    I_tuple = tuple(sorted(parities))
                    S, _ = compute_S(I_tuple, k)
                    if S % D == 0 and S // D == n0:
                        valid_cycles.append((n0, I_tuple))

            if valid_cycles:
                print(f"  p={p}, k={k}, D={D}: Found {len(valid_cycles)} valid cycles")
                for n0, I in valid_cycles:
                    print(f"    n0={n0}, I={I}")


# ============================================================================
# Part 10: Detailed modular propagation examples
# ============================================================================

def modular_propagation_examples(p_max=12):
    """Show the step-by-step parity propagation for specific examples."""

    print("\n" + "=" * 80)
    print("PART 10: DETAILED MODULAR PROPAGATION EXAMPLES")
    print("=" * 80)

    for p in range(6, min(p_max + 1, 13)):
        for k in range(max(1, int(p * 0.45)), min(p, int(p * 0.68) + 1)):
            D = (1 << p) - pow(3, k)
            if D <= 0:
                continue

            total = comb(p, k)
            if total > 500_000:
                continue

            examples_shown = 0
            for I in combinations(range(p), k):
                S, terms = compute_S(I, k)
                if S % D != 0:
                    continue
                n0 = S // D
                if n0 < 1:
                    continue

                if examples_shown >= 2:
                    break

                I_set = set(I)
                n = n0
                print(f"\n  p={p}, k={k}, I={I}, n0={n0}, binary(n0)={bin(n0)}")

                consistent_bits = 0
                for j in range(p):
                    expected = 1 if j in I_set else 0
                    actual = n % 2

                    if expected == actual:
                        consistent_bits += 1
                        if j < 8:
                            print(f"    Step {j}: n_{j}={n}, expected={'odd' if expected else 'even'}, "
                                  f"actual={'odd' if actual else 'even'} -> OK")
                    else:
                        print(f"    Step {j}: n_{j}={n}, expected={'odd' if expected else 'even'}, "
                              f"actual={'odd' if actual else 'even'} -> FAIL (first failure)")
                        print(f"    Consistent for {consistent_bits}/{p} steps before failure")
                        break

                    n = collatz_step(n)
                else:
                    print(f"    ALL {p} steps consistent! Cycle: n_{p}={n}, closes={n==n0}")

                examples_shown += 1


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    print("PARITY FEEDBACK ANALYSIS FOR COLLATZ CYCLES")
    print("=" * 80)

    print("\n\n### Running Part 3: Exhaustive self-consistency check ###")
    exhaustive_check(p_max=22)

    print("\n\n### Running Part 4: Failure position analysis ###")
    failure_rate_by_bit(p_max=20)

    print("\n\n### Running Part 5: Degrees of freedom ###")
    degrees_of_freedom(p_max=22)

    print("\n\n### Running Part 6: Failure rate scaling ###")
    results = failure_rate_scaling(p_max=24)

    print("\n\n### Running Part 7: Information-theoretic analysis ###")
    information_analysis(p_max=22)

    print("\n\n### Running Part 8: Carry-parity interaction ###")
    carry_parity_interaction(p_max=18)

    print("\n\n### Running Part 9: Kneading analysis ###")
    kneading_analysis(p_max=16)

    print("\n\n### Running Part 10: Detailed modular propagation ###")
    modular_propagation_examples(p_max=12)

    print("\n\nDONE.")
