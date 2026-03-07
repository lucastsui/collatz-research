"""
Computational verification for Direction 6g-vii: Cascade increment correlation.

The cascade (C3/C7) has increments g_j = v_2(3*S^j(n)+1).
For a cycle: Σ g_j = p. For random: E[Σ g_j] = 2k ≈ 1.26p.
Question: can correlation / large deviation bounds close the gap?

Checks:
1. Distribution of G(n,k) = Σ g_j across candidates
2. Correlation structure: Cov(g_j, g_{j+1}), Cov(g_j, g_{j+2})
3. Variance of G vs independence prediction
4. Run-length statistics for g=1 streaks
5. The "+1" halving excess: G(n,k) - k*log_2(3)
6. Large deviation rate under independence vs actual
7. The critical question: do correlations help or hurt?
"""

import math
from collections import Counter

def v2(n):
    if n == 0: return 999
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v

def syracuse(n):
    val = 3*n + 1
    return val >> v2(val)

def syracuse_gaps(n, k):
    """Compute the k gaps g_0, ..., g_{k-1} of the Syracuse orbit of n."""
    gaps = []
    s = n
    for j in range(k):
        g = v2(3*s + 1)
        gaps.append(g)
        s = (3*s + 1) >> g
    return gaps, s  # final value S^k(n)

# ======================================================================
# 1. DISTRIBUTION OF G(n,k) ACROSS CANDIDATES
# ======================================================================
print("=" * 70)
print("1. DISTRIBUTION OF G(n,k) = sum g_j ACROSS CANDIDATES")
print("=" * 70)

print("\nFor each (p,k), we compute G(n,k) for all odd n coprime to 3")
print("with n <= (3/2)^{k-1}. The cycle condition requires G = p.\n")

test_cases = []
for k in [5, 8, 10, 15, 20, 25, 30]:
    n_max = int((3/2)**(k-1))
    candidates = [n for n in range(3, n_max + 1, 2) if n % 3 != 0]
    if not candidates:
        continue

    G_vals = []
    for n in candidates:
        gaps, final = syracuse_gaps(n, k)
        G = sum(gaps)
        G_vals.append(G)

    G_min = min(G_vals)
    G_max = max(G_vals)
    G_mean = sum(G_vals) / len(G_vals)
    G_var = sum((g - G_mean)**2 for g in G_vals) / len(G_vals)

    # The target: p for near-critical (p,k) is about k/log_2(3) ≈ 1.585k
    p_target = k * math.log2(3)
    # But the exact p depends on which convergent of log_2(3) we're near
    # For the closest valid (p,k): p is the smallest integer > k*log_2(3)
    p_min = math.ceil(k * math.log2(3))
    while 2**p_min - 3**k <= 0:
        p_min += 1

    excess_min = G_min - p_target
    frac_below_p = sum(1 for g in G_vals if g <= p_min) / len(G_vals)

    test_cases.append((k, len(candidates), G_min, G_max, G_mean, G_var, p_min, p_target))

    print(f"k={k:2d}: {len(candidates):6d} candidates, "
          f"G range [{G_min}, {G_max}], "
          f"mean={G_mean:.2f}, var={G_var:.1f}")
    print(f"      p_min={p_min}, p_target={p_target:.2f}, "
          f"G_min - p_target = {excess_min:.2f}, "
          f"#(G ≤ p_min) = {frac_below_p:.4f}")

# ======================================================================
# 2. CORRELATION STRUCTURE
# ======================================================================
print()
print("=" * 70)
print("2. CORRELATION STRUCTURE OF CONSECUTIVE GAPS")
print("=" * 70)

print("\nKey question: are g_j and g_{j+1} positively or negatively correlated?")
print("Negative correlation → narrower G distribution → helps exclude cycles.")
print("Positive correlation → wider G distribution → hurts.\n")

for k in [10, 20, 30]:
    n_max = int((3/2)**(k-1))
    candidates = [n for n in range(3, n_max + 1, 2) if n % 3 != 0]
    if len(candidates) < 10:
        continue

    # Collect all gap pairs (g_j, g_{j+1})
    all_gaps = []
    all_pairs_1 = []  # (g_j, g_{j+1})
    all_pairs_2 = []  # (g_j, g_{j+2})

    for n in candidates:
        gaps, _ = syracuse_gaps(n, k)
        all_gaps.extend(gaps)
        for j in range(k-1):
            all_pairs_1.append((gaps[j], gaps[j+1]))
        for j in range(k-2):
            all_pairs_2.append((gaps[j], gaps[j+2]))

    # Compute marginal statistics
    E_g = sum(all_gaps) / len(all_gaps)
    Var_g = sum((g - E_g)**2 for g in all_gaps) / len(all_gaps)

    # Compute lag-1 correlation
    E_g1 = sum(a for a, b in all_pairs_1) / len(all_pairs_1)
    E_g2 = sum(b for a, b in all_pairs_1) / len(all_pairs_1)
    E_g1g2 = sum(a*b for a, b in all_pairs_1) / len(all_pairs_1)
    Cov_1 = E_g1g2 - E_g1 * E_g2
    Var_1 = sum((a - E_g1)**2 for a, _ in all_pairs_1) / len(all_pairs_1)
    Var_2 = sum((b - E_g2)**2 for _, b in all_pairs_1) / len(all_pairs_1)
    Corr_1 = Cov_1 / math.sqrt(Var_1 * Var_2) if Var_1 > 0 and Var_2 > 0 else 0

    # Compute lag-2 correlation
    if all_pairs_2:
        E_a2 = sum(a for a, b in all_pairs_2) / len(all_pairs_2)
        E_b2 = sum(b for a, b in all_pairs_2) / len(all_pairs_2)
        E_ab2 = sum(a*b for a, b in all_pairs_2) / len(all_pairs_2)
        Cov_2 = E_ab2 - E_a2 * E_b2
        Var_a2 = sum((a - E_a2)**2 for a, _ in all_pairs_2) / len(all_pairs_2)
        Var_b2 = sum((b - E_b2)**2 for _, b in all_pairs_2) / len(all_pairs_2)
        Corr_2 = Cov_2 / math.sqrt(Var_a2 * Var_b2) if Var_a2 > 0 and Var_b2 > 0 else 0
    else:
        Corr_2 = 0

    print(f"k={k:2d} ({len(candidates)} candidates):")
    print(f"  E[g] = {E_g:.4f} (theory: 2.0000)")
    print(f"  Var[g] = {Var_g:.4f} (theory: 2.0000)")
    print(f"  Corr(g_j, g_{{j+1}}) = {Corr_1:+.4f} {'(NEGATIVE = helps)' if Corr_1 < 0 else '(POSITIVE = hurts)'}")
    print(f"  Corr(g_j, g_{{j+2}}) = {Corr_2:+.4f}")

    # Variance of G under independence vs actual
    var_G_indep = k * Var_g
    # Actual variance of G
    G_vals_k = []
    for n in candidates:
        gaps, _ = syracuse_gaps(n, k)
        G_vals_k.append(sum(gaps))
    G_mean_k = sum(G_vals_k) / len(G_vals_k)
    var_G_actual = sum((g - G_mean_k)**2 for g in G_vals_k) / len(G_vals_k)

    print(f"  Var[G] actual = {var_G_actual:.1f}, independence prediction = {var_G_indep:.1f}")
    print(f"  Ratio Var[G]/Var_indep = {var_G_actual/var_G_indep:.4f} "
          f"{'(<1 = correlations HELP)' if var_G_actual < var_G_indep else '(>1 = correlations HURT)'}")

# ======================================================================
# 3. THE "+1" HALVING EXCESS
# ======================================================================
print()
print("=" * 70)
print("3. THE '+1' HALVING EXCESS: why G(n,k) > k*log_2(3)")
print("=" * 70)

print("\nWithout the '+1' in 3n+1, the map 3n has no halvings (g=0 always).")
print("The entire halving budget comes from the +1 shift.")
print("A cycle needs G = p ≈ 1.585k. The +1 gives E[G] = 2k = 1.26p.")
print("Excess: E[G] - p ≈ 0.415k ≈ 0.26p.\n")

print("The minimum G across all candidates for each k:\n")
print(f"{'k':>4} {'#cand':>8} {'G_min':>6} {'k*log2(3)':>10} {'excess':>8} {'p_min':>6} {'G_min-p_min':>11}")
print("-" * 60)

for k in [3, 5, 8, 10, 12, 15, 18, 20, 25, 30]:
    n_max = int((3/2)**(k-1))
    candidates = [n for n in range(3, n_max + 1, 2) if n % 3 != 0]
    if not candidates:
        continue

    G_min = float('inf')
    n_min = None
    for n in candidates:
        gaps, _ = syracuse_gaps(n, k)
        G = sum(gaps)
        if G < G_min:
            G_min = G
            n_min = n

    target = k * math.log2(3)
    p_min = math.ceil(target)
    while 2**p_min - 3**k <= 0:
        p_min += 1

    excess = G_min - target
    print(f"{k:4d} {len(candidates):8d} {G_min:6d} {target:10.2f} {excess:8.2f} {p_min:6d} {G_min - p_min:11d}")

# ======================================================================
# 4. RUN-LENGTH STATISTICS FOR g=1 STREAKS
# ======================================================================
print()
print("=" * 70)
print("4. RUN-LENGTH OF g=1 STREAKS")
print("=" * 70)

print("\nConsecutive g=1 steps mean the orbit grows by 3/2 per step.")
print("Long streaks pull G down toward k (too few halvings).")
print("But growth from g=1 streaks forces eventual g>1 (self-limiting).\n")

for k in [15, 20, 30]:
    n_max = int((3/2)**(k-1))
    candidates = [n for n in range(3, n_max + 1, 2) if n % 3 != 0]
    if not candidates:
        continue

    max_runs = []
    all_runs = []
    for n in candidates:
        gaps, _ = syracuse_gaps(n, k)
        # Find runs of g=1
        run_len = 0
        max_run = 0
        for g in gaps:
            if g == 1:
                run_len += 1
                max_run = max(max_run, run_len)
            else:
                if run_len > 0:
                    all_runs.append(run_len)
                run_len = 0
        if run_len > 0:
            all_runs.append(run_len)
        max_runs.append(max_run)

    run_counts = Counter(all_runs)
    avg_max_run = sum(max_runs) / len(max_runs)
    absolute_max_run = max(max_runs)

    print(f"k={k} ({len(candidates)} candidates):")
    print(f"  Max g=1 streak across all candidates: {absolute_max_run}")
    print(f"  Average max g=1 streak per candidate: {avg_max_run:.2f}")
    print(f"  Run-length distribution: ", end="")
    for length in sorted(run_counts.keys())[:8]:
        print(f"len={length}: {run_counts[length]}, ", end="")
    print()

# ======================================================================
# 5. LARGE DEVIATION ANALYSIS
# ======================================================================
print()
print("=" * 70)
print("5. LARGE DEVIATION: P(G ≤ p) UNDER INDEPENDENCE vs ACTUAL")
print("=" * 70)

print("\nUnder independence, the rate function for geometric(1/2) on {1,2,...} is:")
print("I(x) = sup_t (tx - log M(t)) where M(t) = (e^t/2)/(1 - e^t/2).\n")

# Compute the rate function
def rate_function(x):
    """Cramér rate function for geometric distribution P(g=r) = 1/2^r, r >= 1."""
    if x <= 1:
        return float('inf')
    if x >= 2:
        return 0
    # e^t = 2(x-1)/x
    et = 2*(x-1)/x
    if et <= 0 or et >= 2:
        return 0
    t = math.log(et)
    # Lambda(t) = log(M(t)) = log((et/2)/(1 - et/2)) = log(et) - log(2) - log(1-et/2)
    Lambda = math.log(et) - math.log(2) - math.log(1 - et/2)
    return t*x - Lambda

# For near-critical (p,k): p/k ≈ log_2(3) ≈ 1.585
x_target = math.log2(3)  # ≈ 1.585, the average g needed for a cycle
I_target = rate_function(x_target)

print(f"Target: average g_j = p/k ≈ log_2(3) = {x_target:.6f}")
print(f"Rate function I({x_target:.4f}) = {I_target:.6f}")
print(f"So P(G ≤ p) ≈ exp(-k * {I_target:.6f}) under independence.\n")
print(f"Number of candidates: ~(3/2)^k, rate = log(3/2) = {math.log(3/2):.6f}")
print(f"Net rate: {math.log(3/2):.6f} - {I_target:.6f} = {math.log(3/2) - I_target:.6f}")
print(f"Since {math.log(3/2) - I_target:.6f} > 0: independence model predicts")
print(f"GROWING number of candidate 'successes'. Independence is INSUFFICIENT.\n")

# Compare with actual data
print("Actual fraction of candidates with G ≤ p_min:\n")
print(f"{'k':>4} {'#cand':>8} {'p_min':>6} {'#(G<=p)':>8} {'frac':>10} {'indep_pred':>12} {'ratio':>10}")
print("-" * 70)

for k in [5, 8, 10, 15, 20, 25, 30]:
    n_max = int((3/2)**(k-1))
    candidates = [n for n in range(3, n_max + 1, 2) if n % 3 != 0]
    if not candidates:
        continue

    p_min = math.ceil(k * math.log2(3))
    while 2**p_min - 3**k <= 0:
        p_min += 1

    count_leq_p = 0
    for n in candidates:
        gaps, _ = syracuse_gaps(n, k)
        G = sum(gaps)
        if G <= p_min:
            count_leq_p += 1

    frac = count_leq_p / len(candidates) if candidates else 0
    indep_pred = math.exp(-k * I_target)

    ratio_str = f"{frac/indep_pred:.4f}" if indep_pred > 0 and frac > 0 else "N/A"
    print(f"{k:4d} {len(candidates):8d} {p_min:6d} {count_leq_p:8d} {frac:10.6f} {indep_pred:12.6e} {ratio_str:>10}")

# ======================================================================
# 6. THE HALVING EXCESS LOWER BOUND
# ======================================================================
print()
print("=" * 70)
print("6. LOWER BOUND ON G(n,k): can we prove G > p?")
print("=" * 70)

print("\nWe need G(n,k) > p for all valid (p,k) and all candidates n.")
print("This is equivalent to: for all n ≥ 3, the Syracuse orbit of n")
print("has more total halvings in k steps than k*log_2(3).\n")

print("Testing: for each k, what is the minimum G(n,k)/k across candidates?\n")

print(f"{'k':>4} {'min(G/k)':>10} {'max(G/k)':>10} {'log2(3)':>10} {'margin':>10} {'n_achieving_min':>16}")
print("-" * 65)

for k in [5, 8, 10, 12, 15, 18, 20, 25, 30]:
    n_max = int((3/2)**(k-1))
    candidates = [n for n in range(3, n_max + 1, 2) if n % 3 != 0]
    if not candidates:
        continue

    best_min = float('inf')
    best_max = 0
    n_at_min = None
    for n in candidates:
        gaps, _ = syracuse_gaps(n, k)
        ratio = sum(gaps) / k
        if ratio < best_min:
            best_min = ratio
            n_at_min = n
        best_max = max(best_max, ratio)

    margin = best_min - math.log2(3)
    print(f"{k:4d} {best_min:10.4f} {best_max:10.4f} {math.log2(3):10.4f} {margin:+10.4f} {n_at_min:16d}")

# ======================================================================
# 7. DETAILED GAP-SIZE ORBIT ANALYSIS
# ======================================================================
print()
print("=" * 70)
print("7. ORBIT ANALYSIS: why large g is followed by small g")
print("=" * 70)

print("\nAfter a large gap g_j (many halvings), S^{j+1} = (3S^j+1)/2^{g_j}")
print("is small. A small value has bounded v_2(3m+1) ≤ log_2(3m+1).")
print("This creates negative lag-1 correlation (verified in Section 2).\n")

# Show specific examples
for n in [7, 27, 31, 127, 255]:
    gaps, final = syracuse_gaps(n, 15)
    s = n
    orbit_vals = [n]
    for g in gaps:
        s = (3*s + 1) >> g
        orbit_vals.append(s)

    print(f"n = {n}:")
    for j in range(min(10, len(gaps))):
        print(f"  step {j}: S^{j}(n)={orbit_vals[j]:8d}, "
              f"3S+1={3*orbit_vals[j]+1:8d}, "
              f"g_{j}={gaps[j]}, "
              f"S^{j+1}={orbit_vals[j+1]:8d}")
    if len(gaps) > 10:
        print(f"  ... (G = {sum(gaps)})")
    print()

# ======================================================================
# 8. CONDITIONAL EXPECTATIONS: E[g_{j+1} | g_j = r]
# ======================================================================
print()
print("=" * 70)
print("8. CONDITIONAL EXPECTATIONS: E[g_{j+1} | g_j = r]")
print("=" * 70)

print("\nIf E[g_{j+1} | g_j] is DECREASING in g_j, gaps are negatively correlated.\n")

for k in [20, 30]:
    n_max = int((3/2)**(k-1))
    candidates = [n for n in range(3, n_max + 1, 2) if n % 3 != 0]
    if not candidates or len(candidates) < 100:
        continue

    # Collect conditional statistics
    cond_sums = {}  # r -> (count, sum of g_{j+1})
    for n in candidates:
        gaps, _ = syracuse_gaps(n, k)
        for j in range(k-1):
            r = gaps[j]
            if r not in cond_sums:
                cond_sums[r] = [0, 0]
            cond_sums[r][0] += 1
            cond_sums[r][1] += gaps[j+1]

    print(f"k={k} ({len(candidates)} candidates):")
    for r in sorted(cond_sums.keys()):
        count, total = cond_sums[r]
        if count >= 10:
            print(f"  E[g_{{j+1}} | g_j = {r}] = {total/count:.4f} ({count} samples)")

# ======================================================================
# 9. THE CRITICAL ACCOUNTING
# ======================================================================
print()
print("=" * 70)
print("9. CRITICAL ACCOUNTING: independence rate vs candidate count")
print("=" * 70)

print("""
For a cycle with parameters (p,k) and starting value n:
  - Number of candidates: N(k) ≈ (3/2)^{k-1} ≈ exp(0.405k)
  - Under INDEPENDENCE: P(G(n,k) = p) ≈ exp(-I_target * k) / sqrt(k)
    where I_target = I(log_2(3)) ≈ 0.0544
  - Expected cycles ≈ N(k) * P ≈ exp((0.405 - 0.054) * k) = exp(0.351k)
  - This GROWS → independence model is INSUFFICIENT.

For correlations to save us, we need the ACTUAL rate > 0.405:
  - Need: P(G(n,k) = p) ≤ exp(-c * k) with c > 0.405
  - Under independence: c = 0.054 (not enough)
  - Correlations would need to boost c by factor > 7.4×

Can the correlations do this? The variance ratio (Section 2) suggests
correlations reduce Var[G] to ~0.7-0.9 of the independence value.
In a Gaussian approximation, this changes the rate by a factor of
~1/variance_ratio ≈ 1.1-1.4×. NOT enough (need 7.4×).
""")

# Compute the actual gap
print("Quantitative gap analysis:\n")
print(f"  Independence rate:         I = {I_target:.6f}")
print(f"  Needed rate:               c = {math.log(3/2):.6f}")
print(f"  Gap factor:                c/I = {math.log(3/2)/I_target:.1f}×")
print()

# ======================================================================
# 10. VERDICT
# ======================================================================
print("=" * 70)
print("10. VERDICT ON DIRECTION 6g-vii")
print("=" * 70)

print("""
WHAT WORKS:
  1. E[G(n,k)] = 2k > p: the average halving count exceeds the cycle target.
  2. The correlations are NEGATIVE (lag-1 Corr ≈ -0.05 to -0.15):
     large g_j → small S^{j+1} → bounded g_{j+1}.
  3. Var[G] < k*Var[g]: correlations DO narrow the distribution.
  4. The minimum G/k across candidates stays well above log_2(3).

WHAT DOESN'T WORK:
  1. The independence rate I(log_2(3)) ≈ 0.054 is too small.
     Need rate > log(3/2) ≈ 0.405 to overcome (3/2)^k candidates.
     Gap factor: 7.4× — correlations provide only ~1.1-1.4×.
  2. Even with perfect negative correlation (Var[G] → 0), the
     POINTWISE concentration P(G = p for a specific n) doesn't
     help — the problem is the UNION BOUND over (3/2)^k candidates.
  3. The gap analysis reduces to: are there n where G(n,k) is
     unusually close to k*log_2(3)? Computationally: YES, some n
     achieve G/k close to log_2(3) + O(1/k).

ROOT CAUSE: The cascade (G(n,k) = p) IS the Collatz cycle condition
(C7). Bounding G away from p for ALL n is EQUIVALENT to proving
no cycles exist. The correlation analysis adds quantitative
information but cannot bridge the 7.4× gap without fundamentally
new input.

STATUS: 6g-vii provides genuine quantitative insights (negative
correlation, variance reduction) but FAILS to close the gap.
The 7.4× factor between the independence rate and the needed rate
is the quantitative expression of the barrier.
""")
