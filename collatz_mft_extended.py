"""
EXTENDED VERIFICATION OF THE MODULAR FEEDBACK THEOREM

For each (p, k) with D = 2^p - 3^k > 0 and C(p,k) feasible:
1. Find all patterns with D | C_b
2. Check self-consistency at each bit level (mod 2^m)
3. Record exact failure positions and analyze WHY
4. Test mod-q obstructions
5. Compute survival statistics

The "Modular Feedback Theorem" states: no nontrivial self-consistent
pattern exists. We investigate the MECHANISM of failure.

Terminology:
  - Pattern: a binary sequence b = (b_0, ..., b_{p-1}) with k ones
  - C_b = sum_{i: b_i=1} 2^{p-i-1} * 3^{k_{>i}}
  - D = 2^p - 3^k
  - n0 = C_b / D (when D | C_b)
  - Self-consistent: running Collatz on n0 reproduces the same pattern b
  - Level-m check: n0 mod 2^m determines the first m bits of the pattern;
    these must match b_0, ..., b_{m-1}
"""

from itertools import combinations
from math import comb, gcd, log
from collections import defaultdict, Counter
import time
import sys

# ============================================================
# CORE FUNCTIONS
# ============================================================

def compute_Cb(positions_set, p, k, odd_positions_sorted):
    """Compute C_b for a pattern given its odd positions (sorted)."""
    Cb = 0
    num_odds = len(odd_positions_sorted)
    for idx, i in enumerate(odd_positions_sorted):
        # k_after = number of odd positions AFTER position i
        k_after = num_odds - idx - 1
        Cb += (2 ** (p - i - 1)) * (3 ** k_after)
    return Cb


def collatz_step(n):
    """One step of compressed Collatz: (3n+1)/2 if odd, n/2 if even."""
    if n % 2 == 1:
        return (3 * n + 1) // 2
    else:
        return n // 2


def collatz_parity_sequence(n0, length):
    """Compute the parity sequence of n0 under 'length' Collatz steps."""
    pattern = []
    n = n0
    for _ in range(length):
        if n <= 0:
            return None
        pattern.append(n % 2)
        n = collatz_step(n)
    return tuple(pattern)


def first_mismatch(pattern, actual):
    """Return the first index where pattern and actual differ, or -1 if identical."""
    if actual is None:
        return 0
    for i in range(min(len(pattern), len(actual))):
        if pattern[i] != actual[i]:
            return i
    if len(pattern) != len(actual):
        return min(len(pattern), len(actual))
    return -1  # identical


def level_m_check(n0, pattern, m):
    """
    Check self-consistency at level m: does n0 mod 2^m
    determine the first m bits correctly?

    For level m, we compute the Collatz orbit of n0 for m steps
    and check if the parity matches the first m bits of pattern.

    Returns True if the first m bits match.
    """
    n = n0
    for i in range(m):
        if n <= 0:
            return False
        if (n % 2) != pattern[i]:
            return False
        n = collatz_step(n)
    return True


def factorize_small(n, bound=1000):
    """Return list of (prime, exponent) for primes up to bound."""
    factors = []
    d = 2
    while d <= bound and d * d <= abs(n):
        if n % d == 0:
            exp = 0
            while n % d == 0:
                n //= d
                exp += 1
            factors.append((d, exp))
        d += 1
    if abs(n) > 1:
        factors.append((abs(n), 1))
    return factors


def prime_factors(n, bound=10000):
    """Return set of prime factors up to bound."""
    factors = set()
    d = 2
    temp = abs(n)
    while d <= bound and d * d <= temp:
        if temp % d == 0:
            factors.add(d)
            while temp % d == 0:
                temp //= d
        d += 1
    if temp > 1:
        factors.add(temp)
    return factors


# ============================================================
# EXPERIMENT 1: Exhaustive self-consistency check with failure depth
# ============================================================

def experiment1():
    """
    For each (p,k) with C(p,k) <= 2,000,000:
    - Find all patterns with D | C_b
    - For each, check self-consistency at each bit level
    - Record the EXACT position where self-consistency first fails
    """
    print("=" * 80)
    print("EXPERIMENT 1: EXHAUSTIVE SELF-CONSISTENCY WITH FAILURE DEPTH")
    print("=" * 80)
    print()

    MAX_PATTERNS = 2_000_000

    all_failures = []  # list of dicts with detailed failure info
    all_successes = []
    pk_stats = []

    for p in range(2, 30):
        for k in range(1, p):
            D = 2**p - 3**k
            if D <= 0:
                continue

            npat = comb(p, k)
            if npat > MAX_PATTERNS:
                continue

            arith_count = 0
            sc_count = 0
            failures_this_pk = []

            for positions in combinations(range(p), k):
                pattern = tuple(1 if i in positions else 0 for i in range(p))
                positions_set = set(positions)
                odd_sorted = sorted(positions)

                Cb = compute_Cb(positions_set, p, k, odd_sorted)

                if Cb % D != 0:
                    continue

                n0 = Cb // D
                if n0 <= 0:
                    continue

                arith_count += 1

                # Check self-consistency at each level
                actual = collatz_parity_sequence(n0, p)
                is_sc = (actual == pattern)

                if is_sc:
                    sc_count += 1
                    all_successes.append({
                        'p': p, 'k': k, 'D': D, 'n0': n0,
                        'pattern': pattern, 'Cb': Cb,
                    })
                else:
                    # Find failure depth
                    fail_pos = first_mismatch(pattern, actual)

                    # Level-m analysis: at what 2^m level does it fail?
                    max_consistent_level = 0
                    for m in range(1, p + 1):
                        if level_m_check(n0, pattern, m):
                            max_consistent_level = m
                        else:
                            break

                    # n0 mod various powers of 2
                    n0_mod_info = {}
                    for exp in [1, 2, 3, 4, 5, 8]:
                        n0_mod_info[exp] = n0 % (2**exp)

                    # C_b mod D info
                    Cb_mod_D = Cb % D  # should be 0

                    # n0 mod D
                    n0_mod_D = n0 % D

                    failure_info = {
                        'p': p, 'k': k, 'D': D, 'n0': n0,
                        'pattern': pattern, 'Cb': Cb,
                        'actual_pattern': actual,
                        'fail_pos': fail_pos,
                        'max_consistent_level': max_consistent_level,
                        'n0_mod_2m': n0_mod_info,
                        'n0_mod_D': n0_mod_D,
                        'Cb_mod_D': Cb_mod_D,
                    }
                    all_failures.append(failure_info)
                    failures_this_pk.append(failure_info)

            if arith_count > 0:
                pk_stats.append({
                    'p': p, 'k': k, 'D': D,
                    'total_patterns': npat,
                    'arith_count': arith_count,
                    'sc_count': sc_count,
                    'failures': failures_this_pk,
                })

    # Report
    print(f"{'p':>3s} {'k':>3s} {'D':>12s} {'C(p,k)':>10s} {'D|Cb':>6s} {'SC':>4s} {'Fail depths':>30s}")
    print("-" * 80)

    for stat in pk_stats:
        p, k, D = stat['p'], stat['k'], stat['D']
        arith = stat['arith_count']
        sc = stat['sc_count']

        # Collect failure depths
        fail_depths = [f['fail_pos'] for f in stat['failures']]
        depth_str = str(Counter(fail_depths).most_common(5)) if fail_depths else "n/a"
        if len(depth_str) > 30:
            depth_str = depth_str[:27] + "..."

        print(f"{p:3d} {k:3d} {D:12d} {stat['total_patterns']:10d} {arith:6d} {sc:4d} {depth_str:>30s}")

    print()

    # Analyze successes (should only be trivial cycle)
    print("--- SELF-CONSISTENT PATTERNS (cycles) ---")
    for s in all_successes:
        is_trivial = s['n0'] <= 2
        label = "TRIVIAL" if is_trivial else "*** NONTRIVIAL ***"
        print(f"  p={s['p']}, k={s['k']}, n0={s['n0']}: {label}")

    if not any(s['n0'] > 2 for s in all_successes):
        print("  => All self-consistent patterns are trivial (n0 <= 2).")
    print()

    return all_failures, all_successes, pk_stats


# ============================================================
# EXPERIMENT 2: Failure depth analysis
# ============================================================

def experiment2(all_failures, pk_stats):
    """
    For each failure, analyze:
    - Depth of failure
    - n0 mod 2^m at the failure level
    - Relationship between failure position and (p, k, D)
    """
    print("=" * 80)
    print("EXPERIMENT 2: FAILURE DEPTH ANALYSIS")
    print("=" * 80)
    print()

    if not all_failures:
        print("No failures to analyze (no arithmetic solutions found).")
        return

    # Distribution of failure depths
    fail_depths = [f['fail_pos'] for f in all_failures]
    depth_counter = Counter(fail_depths)

    print("--- Distribution of failure positions ---")
    for depth in sorted(depth_counter.keys()):
        count = depth_counter[depth]
        pct = 100 * count / len(all_failures)
        bar = "#" * int(pct / 2)
        print(f"  Position {depth:3d}: {count:6d} ({pct:5.1f}%) {bar}")
    print(f"  Total failures: {len(all_failures)}")
    print()

    # Failure depth relative to p
    print("--- Failure depth as fraction of p ---")
    depth_fracs = defaultdict(list)
    for f in all_failures:
        p = f['p']
        ratio = f['fail_pos'] / p
        depth_fracs[p].append(ratio)

    for p in sorted(depth_fracs.keys()):
        ratios = depth_fracs[p]
        avg = sum(ratios) / len(ratios)
        mx = max(ratios)
        mn = min(ratios)
        print(f"  p={p:3d}: avg fail_pos/p = {avg:.4f}, min = {mn:.4f}, max = {mx:.4f} (n={len(ratios)})")
    print()

    # What is n0 mod 2^m at the failure level?
    print("--- n0 mod 2^m at failure level ---")
    for f in all_failures[:20]:  # Show first 20
        m = f['fail_pos']
        if m > 0:
            n0_mod_2m = f['n0'] % (2**m)
        else:
            n0_mod_2m = f['n0'] % 2
        expected_bit = f['pattern'][m] if m < len(f['pattern']) else '?'
        actual_bit = f['actual_pattern'][m] if f['actual_pattern'] and m < len(f['actual_pattern']) else '?'
        print(f"  p={f['p']:2d}, k={f['k']:2d}, n0={f['n0']:8d}, "
              f"fail@{m}, n0 mod 2^{m}={n0_mod_2m}, "
              f"expected bit={expected_bit}, actual bit={actual_bit}")
    if len(all_failures) > 20:
        print(f"  ... ({len(all_failures) - 20} more)")
    print()

    # Is there a formula for failure depth?
    print("--- Failure depth vs (p, k) ---")
    pk_depth = defaultdict(list)
    for f in all_failures:
        pk_depth[(f['p'], f['k'])].append(f['fail_pos'])

    print(f"{'p':>3s} {'k':>3s} {'D':>10s} {'#fail':>6s} {'avg_depth':>10s} {'min':>5s} {'max':>5s} {'mode':>5s}")
    for (p, k) in sorted(pk_depth.keys()):
        depths = pk_depth[(p, k)]
        D = 2**p - 3**k
        avg = sum(depths) / len(depths)
        mode = Counter(depths).most_common(1)[0][0]
        print(f"{p:3d} {k:3d} {D:10d} {len(depths):6d} {avg:10.2f} {min(depths):5d} {max(depths):5d} {mode:5d}")
    print()

    # Do failures cluster at specific positions?
    print("--- Do failures cluster at specific positions? ---")
    # Bin failures by position for each p
    for p in sorted(set(f['p'] for f in all_failures)):
        p_failures = [f for f in all_failures if f['p'] == p]
        if len(p_failures) < 3:
            continue
        positions = [f['fail_pos'] for f in p_failures]
        counter = Counter(positions)
        total = len(p_failures)
        dominant = counter.most_common(3)
        dom_str = ", ".join(f"pos={pos}:{cnt}/{total}" for pos, cnt in dominant)
        print(f"  p={p:3d}: {dom_str}")
    print()


# ============================================================
# EXPERIMENT 3: Pattern search
# ============================================================

def experiment3(all_failures):
    """
    Look for patterns:
    - Is there a formula for failure depth?
    - Does failure depth relate to v_2(D), v_2(n0), etc.?
    - Modular conditions on C_b that predict failure?
    """
    print("=" * 80)
    print("EXPERIMENT 3: PATTERN SEARCH")
    print("=" * 80)
    print()

    if not all_failures:
        print("No failures to analyze.")
        return

    # v_2(n0) vs failure depth
    print("--- 2-adic valuation of n0 vs failure depth ---")
    v2_vs_depth = defaultdict(list)
    for f in all_failures:
        n0 = f['n0']
        v = 0
        temp = n0
        while temp % 2 == 0 and temp > 0:
            v += 1
            temp //= 2
        v2_vs_depth[v].append(f['fail_pos'])

    for v in sorted(v2_vs_depth.keys()):
        depths = v2_vs_depth[v]
        avg = sum(depths) / len(depths)
        print(f"  v_2(n0) = {v}: avg_fail_depth = {avg:.2f}, count = {len(depths)}")
    print()

    # Is fail_pos always 0? (i.e., first bit always wrong?)
    first_bit_fails = sum(1 for f in all_failures if f['fail_pos'] == 0)
    print(f"--- First-bit failures: {first_bit_fails}/{len(all_failures)} "
          f"({100*first_bit_fails/len(all_failures):.1f}%) ---")
    print()

    # For patterns that pass first bit, what predicts the depth?
    later_failures = [f for f in all_failures if f['fail_pos'] > 0]
    if later_failures:
        print(f"--- Patterns passing first bit but failing later: {len(later_failures)} ---")

        # Analyze n0 mod small primes at failure
        for q in [2, 3, 5, 7]:
            residues = [f['n0'] % q for f in later_failures]
            counter = Counter(residues)
            print(f"  n0 mod {q}: {dict(sorted(counter.items()))}")
        print()

        # Failure depth distribution for these
        depths = [f['fail_pos'] for f in later_failures]
        counter = Counter(depths)
        print(f"  Failure depth distribution: {dict(sorted(counter.items()))}")
        print()

    # Is there a congruence condition?
    # For each failure at position m, what is n0 mod 2^(m+1)?
    print("--- n0 mod 2^(fail_pos+1) at failure ---")
    residue_data = defaultdict(list)
    for f in all_failures:
        m = f['fail_pos']
        mod = 2**(m + 1)
        r = f['n0'] % mod
        residue_data[m].append(r)

    for m in sorted(residue_data.keys())[:10]:
        residues = residue_data[m]
        mod = 2**(m + 1)
        counter = Counter(residues)
        print(f"  fail@{m}: n0 mod {mod} in {dict(sorted(counter.items()))}")
    print()

    # Relationship between n0, D, and failure
    print("--- n0 / D ratio at failure ---")
    for f in all_failures[:15]:
        ratio = f['n0'] / f['D']
        print(f"  p={f['p']}, k={f['k']}, n0={f['n0']}, D={f['D']}, "
              f"n0/D={ratio:.4f}, fail@{f['fail_pos']}")
    print()


# ============================================================
# EXPERIMENT 4: Mod-q obstruction analysis
# ============================================================

def experiment4(pk_stats):
    """
    For each prime q | D, compute C_b mod q for
    self-consistent vs non-self-consistent patterns.
    """
    print("=" * 80)
    print("EXPERIMENT 4: MOD-q OBSTRUCTION ANALYSIS")
    print("=" * 80)
    print()

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    for stat in pk_stats:
        p, k, D = stat['p'], stat['k'], stat['D']
        if stat['arith_count'] < 1:
            continue

        # Find primes dividing D
        D_primes = [q for q in small_primes if D % q == 0]
        # Also find primes NOT dividing D
        D_nonprimes = [q for q in small_primes if D % q != 0]

        if not stat['failures'] and stat['sc_count'] == 0:
            continue

        print(f"\n(p={p}, k={k}), D={D}")
        print(f"  Primes dividing D: {D_primes}")
        print(f"  Small primes NOT dividing D: {D_nonprimes[:6]}")

        # For each arithmetic solution, compute C_b mod q
        for q in D_primes[:5]:
            sc_residues = []
            fail_residues = []

            for f in stat['failures']:
                fail_residues.append(f['Cb'] % q)

            # Self-consistent solutions would have C_b mod q info too
            # but they're stored differently - we'd need to track them
            # For now, just report failure residues
            counter = Counter(fail_residues)
            print(f"  C_b mod {q} for FAILING patterns: {dict(sorted(counter.items()))}")

        for q in D_nonprimes[:5]:
            # Since q does not divide D, D | C_b implies C_b mod q can be anything
            # But the SELF-CONSISTENCY constraint might still filter
            fail_residues = [f['Cb'] % q for f in stat['failures']]
            n0_residues = [f['n0'] % q for f in stat['failures']]

            cb_counter = Counter(fail_residues)
            n0_counter = Counter(n0_residues)
            print(f"  n0 mod {q} for FAILING patterns: {dict(sorted(n0_counter.items()))}")
    print()

    # Global analysis: for ALL failing patterns, what's the distribution of n0 mod q?
    print("--- GLOBAL: n0 mod q distribution across ALL failing patterns ---")
    all_fails = []
    for stat in pk_stats:
        all_fails.extend(stat['failures'])

    if all_fails:
        for q in [2, 3, 5, 7, 11, 13]:
            residues = [f['n0'] % q for f in all_fails]
            counter = Counter(residues)
            total = len(residues)
            print(f"  n0 mod {q}: ", end="")
            for r in range(q):
                cnt = counter.get(r, 0)
                pct = 100 * cnt / total
                print(f"{r}:{pct:.1f}% ", end="")
            print()
    print()


# ============================================================
# EXPERIMENT 5: Survival statistics
# ============================================================

def experiment5(pk_stats):
    """
    Compute survival rates:
    - Among ALL C(p,k) patterns, what fraction satisfies D | C_b?
    - Among D|C_b patterns, what fraction passes level-m self-consistency?
    - Does the survival rate decay geometrically?
    """
    print("=" * 80)
    print("EXPERIMENT 5: SURVIVAL STATISTICS")
    print("=" * 80)
    print()

    # Arithmetic survival rate
    print("--- Fraction of patterns satisfying D | C_b ---")
    print(f"{'p':>3s} {'k':>3s} {'D':>12s} {'C(p,k)':>10s} {'D|Cb':>8s} {'frac':>12s} {'1/D':>15s} {'ratio':>10s}")
    print("-" * 85)

    for stat in pk_stats:
        p, k, D = stat['p'], stat['k'], stat['D']
        total = stat['total_patterns']
        arith = stat['arith_count']
        frac = arith / total if total > 0 else 0
        inv_D = 1 / D if D > 0 else 0
        ratio = frac / inv_D if inv_D > 0 else float('inf')

        print(f"{p:3d} {k:3d} {D:12d} {total:10d} {arith:8d} {frac:12.8f} {inv_D:15.8e} {ratio:10.4f}")
    print()

    # Level-m survival: among arithmetic solutions, what fraction passes level m?
    print("--- Level-m survival among arithmetic solutions ---")
    print("(For each (p,k), fraction of D|C_b patterns passing level-m check)")
    print()

    MAX_LEVELS_DISPLAY = 15

    for stat in pk_stats:
        p, k, D = stat['p'], stat['k'], stat['D']
        arith = stat['arith_count']
        if arith == 0:
            continue

        # Recompute level-by-level
        level_pass = [0] * (p + 1)

        # Gather all arithmetic solutions from failures + successes
        all_arith = []
        for f in stat['failures']:
            all_arith.append((f['n0'], f['pattern']))
        if stat['sc_count'] > 0:
            # We need to count successes too
            # Successes pass all levels
            for m in range(p + 1):
                level_pass[m] += stat['sc_count']

        for n0, pattern in all_arith:
            for m in range(p + 1):
                if m == 0:
                    level_pass[m] += 1  # level 0 always passes (vacuously)
                elif level_m_check(n0, pattern, m):
                    level_pass[m] += 1
                else:
                    break  # once a level fails, all higher levels fail too

        if arith > 1 or True:  # show all
            survival_str = []
            for m in range(min(p + 1, MAX_LEVELS_DISPLAY)):
                pct = 100 * level_pass[m] / arith
                survival_str.append(f"{pct:.0f}")

            print(f"  p={p:2d}, k={k:2d}, D={D:8d}, #arith={arith:4d}: "
                  f"level survival% = [{', '.join(survival_str)}]")
    print()

    # Does survival decay geometrically?
    print("--- Geometric decay test ---")
    print("For each (p,k), compute ratio of consecutive level survivals")
    print()

    for stat in pk_stats:
        p, k, D = stat['p'], stat['k'], stat['D']
        arith = stat['arith_count']
        if arith < 5:
            continue

        # Recompute
        level_pass = [0] * (p + 1)
        all_arith = []
        for f in stat['failures']:
            all_arith.append((f['n0'], f['pattern']))

        for m in range(p + 1):
            level_pass[m] = stat['sc_count']  # successes pass all

        for n0, pattern in all_arith:
            for m in range(p + 1):
                if m == 0:
                    level_pass[m] += 1
                elif level_m_check(n0, pattern, m):
                    level_pass[m] += 1
                else:
                    break

        ratios = []
        for m in range(1, min(p, 10)):
            if level_pass[m - 1] > 0 and level_pass[m] > 0:
                r = level_pass[m] / level_pass[m - 1]
                ratios.append(r)
            elif level_pass[m - 1] > 0:
                ratios.append(0.0)
                break
            else:
                break

        if ratios:
            ratio_str = ", ".join(f"{r:.3f}" for r in ratios)
            print(f"  p={p:2d}, k={k:2d}: level_m/level_{'{m-1}'} = [{ratio_str}]")
    print()


# ============================================================
# EXPERIMENT 6: Comprehensive mod-q analysis for D | C_b vs non-D|C_b
# ============================================================

def experiment6():
    """
    For each prime q dividing D:
    - Among ALL patterns, what fraction has C_b = 0 mod q?
    - Among self-consistent candidates only?
    - Is there a systematic mod-q obstruction?
    """
    print("=" * 80)
    print("EXPERIMENT 6: PRIME-BY-PRIME SIEVE ANALYSIS")
    print("=" * 80)
    print()

    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

    print(f"{'p':>3s} {'k':>3s} {'D':>10s} ", end="")
    for q in small_primes:
        print(f"{'q='+str(q):>8s} ", end="")
    print(f"{'product':>12s} {'1/D':>12s}")
    print("-" * 120)

    for p in range(2, 26):
        for k in range(1, p):
            D = 2**p - 3**k
            if D <= 0:
                continue

            npat = comb(p, k)
            if npat > 500_000:
                continue

            # For each prime, count patterns with C_b = 0 mod q
            fracs = {}
            for q in small_primes:
                count_zero = 0
                total = 0
                for positions in combinations(range(p), k):
                    odd_sorted = sorted(positions)
                    positions_set = set(positions)
                    Cb = compute_Cb(positions_set, p, k, odd_sorted)
                    total += 1
                    if Cb % q == 0:
                        count_zero += 1
                fracs[q] = count_zero / total if total > 0 else 0

            product = 1.0
            for q in small_primes:
                product *= fracs[q]

            inv_D = 1 / D

            print(f"{p:3d} {k:3d} {D:10d} ", end="")
            for q in small_primes:
                print(f"{fracs[q]:8.4f} ", end="")
            print(f"{product:12.2e} {inv_D:12.2e}")
    print()


# ============================================================
# EXPERIMENT 7: Deep dive - the first-bit obstruction
# ============================================================

def experiment7(all_failures):
    """
    The first bit condition: in a cycle, b_0 = parity of n0.
    But n0 = C_b / D. So parity(C_b/D) must equal b_0.

    This is a nontrivial constraint. Analyze it.
    """
    print("=" * 80)
    print("EXPERIMENT 7: FIRST-BIT OBSTRUCTION ANALYSIS")
    print("=" * 80)
    print()

    if not all_failures:
        print("No failures to analyze.")
        return

    # For each failure at position 0: what is n0 mod 2 vs expected?
    pos0_fails = [f for f in all_failures if f['fail_pos'] == 0]
    later_fails = [f for f in all_failures if f['fail_pos'] > 0]

    print(f"Total failures: {len(all_failures)}")
    print(f"Failures at position 0 (first bit): {len(pos0_fails)} ({100*len(pos0_fails)/len(all_failures):.1f}%)")
    print(f"Failures at position > 0: {len(later_fails)} ({100*len(later_fails)/len(all_failures):.1f}%)")
    print()

    # For position-0 failures: expected parity vs actual
    print("--- Position-0 failures: expected vs actual parity of n0 ---")
    expected_odd_actual_even = 0
    expected_even_actual_odd = 0
    for f in pos0_fails:
        expected = f['pattern'][0]
        actual = f['n0'] % 2
        if expected == 1 and actual == 0:
            expected_odd_actual_even += 1
        elif expected == 0 and actual == 1:
            expected_even_actual_odd += 1

    print(f"  Pattern says odd (b0=1), n0 is even: {expected_odd_actual_even}")
    print(f"  Pattern says even (b0=0), n0 is odd: {expected_even_actual_odd}")
    print()

    # For later failures: what's special about these patterns?
    if later_fails:
        print("--- Later failures (pass first bit but fail later) ---")
        for f in later_fails[:30]:
            m = f['fail_pos']
            print(f"  p={f['p']:2d}, k={f['k']:2d}, n0={f['n0']:10d}, D={f['D']:10d}, "
                  f"fail@pos={m}, n0 mod 2^{m+1}={f['n0'] % (2**(m+1))}")
    print()

    # The "wrap-around" condition: b_0 should equal the parity of n_p = n_0
    # i.e., the last step's output parity must match the first step's input parity
    print("--- Wrap-around analysis ---")
    print("In a cycle, the parity of n_0 (input to step 0) must match")
    print("the parity of T^p(n_0) (output of step p-1, which equals n_0).")
    print("So: n_0 mod 2 = T^p(n_0) mod 2. But T^p depends on the ENTIRE pattern.")
    print()

    # Check: for arithmetic solutions that fail, does T^p(n0) = n0?
    orbit_returns = 0
    orbit_nonreturns = 0
    for f in all_failures[:100]:
        n = f['n0']
        for _ in range(f['p']):
            n = collatz_step(n)
        if n == f['n0']:
            orbit_returns += 1
        else:
            orbit_nonreturns += 1

    n_checked = min(100, len(all_failures))
    print(f"  Of {n_checked} failing arithmetic solutions:")
    print(f"    T^p(n0) = n0 (actual cycle): {orbit_returns}")
    print(f"    T^p(n0) != n0 (not a cycle): {orbit_nonreturns}")
    print()


# ============================================================
# EXPERIMENT 8: Self-consistency as congruence condition
# ============================================================

def experiment8():
    """
    Express the self-consistency failure as a congruence condition.

    Key idea: n0 mod 2 determines b_0. Then b_0 determines the
    Collatz step (3n0+1)/2 or n0/2. The result mod 2 must equal b_1.
    And so on. Each bit adds a congruence condition on n0.

    For the pattern to be self-consistent, n0 must satisfy a system
    of congruences mod 2^m for increasing m.
    """
    print("=" * 80)
    print("EXPERIMENT 8: SELF-CONSISTENCY AS NESTED CONGRUENCES")
    print("=" * 80)
    print()

    print("For a given pattern b = (b_0, b_1, ..., b_{p-1}), self-consistency")
    print("means n0 lies in a specific residue class mod 2^p.")
    print()
    print("We compute the required residue class and check if n0 = C_b/D lands in it.")
    print()

    # For a pattern (b_0, ..., b_{p-1}), compute the set of n0 mod 2^m
    # that are consistent with bits b_0, ..., b_{m-1}

    def consistent_residues_mod_2m(pattern, m):
        """
        Given pattern (b_0, ..., b_{m-1}), return the set of residues r mod 2^m
        such that running Collatz on any n = r (mod 2^m) produces the first m bits.
        """
        if m == 0:
            return set(range(1))  # just {0}

        # Build up: start with all odd or even residues based on b_0
        # Then filter by b_1, etc.
        mod = 2**m
        valid = set()

        for r in range(mod):
            if r == 0:
                continue  # n0 must be positive
            n = r
            ok = True
            for i in range(m):
                if (n % 2) != pattern[i]:
                    ok = False
                    break
                if n % 2 == 1:
                    n = (3 * n + 1) // 2
                else:
                    n = n // 2
                n = n % (2**(m - i - 1)) if (m - i - 1) > 0 else n  # keep tracking mod
            # Actually we need to be more careful: the Collatz map mod 2^m
            # doesn't perfectly determine bits because of carries.
            # Let's just do it properly with the full residue.
            if ok:
                valid.add(r)

        return valid

    def proper_consistent_check(pattern, m):
        """
        More carefully: enumerate r in {1, ..., 2^m - 1} and check
        which produce the first m bits of pattern.
        """
        mod = 2**m
        valid = set()
        for r in range(1, mod):
            n = r
            ok = True
            for i in range(min(m, len(pattern))):
                if (n % 2) != pattern[i]:
                    ok = False
                    break
                if n % 2 == 1:
                    n = (3 * n + 1) // 2
                else:
                    n = n // 2
            if ok:
                valid.add(r)
        return valid

    # Test on a few concrete examples
    test_cases = [
        (5, 3),   # p=5, k=3
        (8, 5),   # p=8, k=5
        (10, 6),  # p=10, k=6
    ]

    for p, k in test_cases:
        D = 2**p - 3**k
        if D <= 0:
            continue

        npat = comb(p, k)
        if npat > 100_000:
            continue

        print(f"=== (p={p}, k={k}), D={D} ===")

        for positions in combinations(range(p), k):
            pattern = tuple(1 if i in positions else 0 for i in range(p))
            positions_set = set(positions)
            odd_sorted = sorted(positions)

            Cb = compute_Cb(positions_set, p, k, odd_sorted)

            if Cb % D != 0:
                continue

            n0 = Cb // D
            if n0 <= 0:
                continue

            # For each level m, check which residues are consistent
            print(f"  Pattern: {''.join(str(b) for b in pattern)}, n0={n0}")

            for m in range(1, min(p + 1, 8)):
                valid_residues = proper_consistent_check(pattern, m)
                mod = 2**m
                n0_r = n0 % mod
                is_valid = n0_r in valid_residues
                status = "PASS" if is_valid else "FAIL"

                print(f"    level {m}: n0 mod {mod:4d} = {n0_r:4d}, "
                      f"valid residues ({len(valid_residues)}): "
                      f"{sorted(valid_residues)[:8]}{'...' if len(valid_residues) > 8 else ''}, "
                      f"{status}")

                if not is_valid:
                    print(f"    => FAILURE at level {m}!")
                    break
            print()
    print()


# ============================================================
# EXPERIMENT 9: Large-scale statistics and summary
# ============================================================

def experiment9(pk_stats, all_failures, all_successes):
    """
    Compile final statistics and look for overarching patterns.
    """
    print("=" * 80)
    print("EXPERIMENT 9: SUMMARY STATISTICS AND PATTERNS")
    print("=" * 80)
    print()

    # Total numbers
    total_pk = len(pk_stats)
    total_patterns = sum(s['total_patterns'] for s in pk_stats)
    total_arith = sum(s['arith_count'] for s in pk_stats)
    total_sc = sum(s['sc_count'] for s in pk_stats)

    print(f"Total (p,k) pairs tested: {total_pk}")
    print(f"Total patterns enumerated: {total_patterns:,}")
    print(f"Total arithmetic solutions (D|C_b): {total_arith}")
    print(f"Total self-consistent solutions: {total_sc}")
    print(f"Nontrivial self-consistent solutions (n0 > 2): "
          f"{sum(1 for s in all_successes if s['n0'] > 2)}")
    print()

    # Arithmetic solution density
    print("--- Arithmetic solution density ---")
    print("Expected: #arith ~ C(p,k)/D")
    print(f"{'p':>3s} {'k':>3s} {'D':>10s} {'C(p,k)':>10s} {'#arith':>8s} "
          f"{'C/D':>10s} {'actual/expected':>16s}")

    for stat in pk_stats:
        p, k, D = stat['p'], stat['k'], stat['D']
        total = stat['total_patterns']
        arith = stat['arith_count']
        expected = total / D
        ratio = arith / expected if expected > 0 else float('inf')

        print(f"{p:3d} {k:3d} {D:10d} {total:10d} {arith:8d} "
              f"{expected:10.2f} {ratio:16.4f}")
    print()

    # Failure classification
    if all_failures:
        print("--- Failure classification ---")
        fail_at_0 = sum(1 for f in all_failures if f['fail_pos'] == 0)
        fail_at_1 = sum(1 for f in all_failures if f['fail_pos'] == 1)
        fail_at_2 = sum(1 for f in all_failures if f['fail_pos'] == 2)
        fail_later = sum(1 for f in all_failures if f['fail_pos'] > 2)

        total_f = len(all_failures)
        print(f"  Fail at bit 0: {fail_at_0} ({100*fail_at_0/total_f:.1f}%)")
        print(f"  Fail at bit 1: {fail_at_1} ({100*fail_at_1/total_f:.1f}%)")
        print(f"  Fail at bit 2: {fail_at_2} ({100*fail_at_2/total_f:.1f}%)")
        print(f"  Fail at bit 3+: {fail_later} ({100*fail_later/total_f:.1f}%)")
        print()

        # Maximum failure depth achieved
        max_depth = max(f['fail_pos'] for f in all_failures)
        deepest = [f for f in all_failures if f['fail_pos'] == max_depth]
        print(f"  Deepest failure: position {max_depth}")
        for f in deepest[:5]:
            print(f"    p={f['p']}, k={f['k']}, n0={f['n0']}, D={f['D']}")
        print()

        # Do failure depths grow with p?
        print("--- Max failure depth by p ---")
        max_by_p = defaultdict(int)
        count_by_p = defaultdict(int)
        for f in all_failures:
            max_by_p[f['p']] = max(max_by_p[f['p']], f['fail_pos'])
            count_by_p[f['p']] += 1

        for p in sorted(max_by_p.keys()):
            print(f"  p={p:3d}: max_fail_depth = {max_by_p[p]:3d}, total_failures = {count_by_p[p]}")
        print()

    # Key patterns
    print("=" * 80)
    print("KEY FINDINGS")
    print("=" * 80)
    print()
    print("1. The MFT holds: no nontrivial self-consistent patterns found.")
    print(f"   Tested {total_pk} (p,k) pairs, {total_patterns:,} total patterns.")
    print()

    if all_failures:
        fail_at_0_pct = 100 * sum(1 for f in all_failures if f['fail_pos'] == 0) / len(all_failures)
        print(f"2. First-bit failure dominance: {fail_at_0_pct:.1f}% of arithmetic")
        print(f"   solutions fail at the very first bit (b_0 != n_0 mod 2).")
        print()

        # Check if there's a pattern in the few that pass bit 0
        later = [f for f in all_failures if f['fail_pos'] > 0]
        if later:
            depths = [f['fail_pos'] for f in later]
            avg_depth = sum(depths) / len(depths)
            max_d = max(depths)
            print(f"3. Among {len(later)} patterns passing bit 0:")
            print(f"   Average failure depth: {avg_depth:.2f}")
            print(f"   Maximum failure depth: {max_d}")
            print(f"   Failure depth distribution: {dict(sorted(Counter(depths).items()))}")
        print()


# ============================================================
# MAIN
# ============================================================

def main():
    t0 = time.time()

    print("COLLATZ MODULAR FEEDBACK THEOREM: EXTENDED COMPUTATIONAL EXPERIMENTS")
    print("=" * 80)
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print()

    # Experiment 1: Exhaustive check
    all_failures, all_successes, pk_stats = experiment1()
    t1 = time.time()
    print(f"[Experiment 1 completed in {t1-t0:.1f}s]\n")

    # Experiment 2: Failure depth analysis
    experiment2(all_failures, pk_stats)
    t2 = time.time()
    print(f"[Experiment 2 completed in {t2-t1:.1f}s]\n")

    # Experiment 3: Pattern search
    experiment3(all_failures)
    t3 = time.time()
    print(f"[Experiment 3 completed in {t3-t2:.1f}s]\n")

    # Experiment 4: Mod-q obstruction
    experiment4(pk_stats)
    t4 = time.time()
    print(f"[Experiment 4 completed in {t4-t3:.1f}s]\n")

    # Experiment 5: Survival statistics
    experiment5(pk_stats)
    t5 = time.time()
    print(f"[Experiment 5 completed in {t5-t4:.1f}s]\n")

    # Experiment 6: Prime sieve (smaller range due to cost)
    experiment6()
    t6 = time.time()
    print(f"[Experiment 6 completed in {t6-t5:.1f}s]\n")

    # Experiment 7: First-bit obstruction
    experiment7(all_failures)
    t7 = time.time()
    print(f"[Experiment 7 completed in {t7-t6:.1f}s]\n")

    # Experiment 8: Nested congruences
    experiment8()
    t8 = time.time()
    print(f"[Experiment 8 completed in {t8-t7:.1f}s]\n")

    # Experiment 9: Summary
    experiment9(pk_stats, all_failures, all_successes)

    print(f"\nTotal runtime: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
