#!/usr/bin/env python3
"""
Investigation of the universal spectral gap via compactness.

For each K = |<2,3>| in F_p*, we find all primes p with that group order K,
compute the spectral gap at each, and track rho(K) = max |lambda_2| over
those primes.

Key question: does rho(K) -> 1 as K -> infinity?

Additionally, for fixed K, we study the K x K block transfer matrix
as a function of the phase parameter t = r_0/p, and compute the
spectral radius as a function of t.
"""

import numpy as np
from scipy.linalg import eigvals
from collections import defaultdict
import time

def multiplicative_order(a, p):
    """Compute ord_p(a)."""
    if a % p == 0:
        return 0
    r = 1
    power = a % p
    while power != 1:
        power = (power * a) % p
        r += 1
        if r > p:
            return p - 1
    return r

def subgroup_order_23(p):
    """Compute |<2,3>| in (Z/pZ)*."""
    seen = {1}
    frontier = {1}
    while frontier:
        new_elts = set()
        for x in frontier:
            for g in [2, 3]:
                y = (x * g) % p
                if y not in seen:
                    seen.add(y)
                    new_elts.add(y)
        frontier = new_elts
    return len(seen)

def build_markov_dense(p):
    """Build Collatz Markov matrix on {1,...,p-1}."""
    n = p - 1
    inv2 = pow(2, p - 2, p)
    M = np.zeros((n, n))
    for x_idx in range(n):
        x = x_idx + 1
        y1 = (x * inv2) % p
        y2 = ((3 * x + 1) * inv2) % p
        if y2 == 0:
            M[y1 - 1, x_idx] += 1.0
        else:
            M[y1 - 1, x_idx] += 0.5
            M[y2 - 1, x_idx] += 0.5
    return M

def spectral_gap(p):
    """Compute |lambda_2(p)| for the Collatz Markov chain mod p."""
    M = build_markov_dense(p)
    evals = eigvals(M)
    mags = np.abs(evals)
    mags_sorted = np.sort(mags)[::-1]
    return mags_sorted[1]

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

# ============================================================
# Part 1: For each K, find primes and compute spectral gaps
# ============================================================
def survey_by_K(max_p=2000):
    """Survey primes up to max_p, grouping by K = |<2,3>|."""
    results = defaultdict(list)

    for p in range(5, max_p + 1):
        if not is_prime(p):
            continue
        K = subgroup_order_23(p)
        lam2 = spectral_gap(p)
        results[K].append((p, lam2))

    return results

# ============================================================
# Part 2: Orbit matrix in frequency space
# ============================================================
def compute_orbit_matrix(p, r0):
    """
    Compute the K x K matrix for the Collatz operator restricted to
    the <2,3>-orbit of r0 in frequency space.

    The Markov operator M acts on Fourier modes as:
      M chi_r = (1/2) chi_{r*inv2} + (1/2) omega^{r*inv2} chi_{3r*inv2}

    So on the orbit O = r0 * <2,3>, M is a K x K matrix.
    """
    inv2p = pow(2, p-2, p)
    inv3p = pow(3, p-2, p)

    # Generate orbit
    orbit_set = {r0 % p}
    frontier = {r0 % p}
    while frontier:
        new_elts = set()
        for x in frontier:
            for g in [2, 3, inv2p, inv3p]:
                y = (x * g) % p
                if y != 0 and y not in orbit_set:
                    orbit_set.add(y)
                    new_elts.add(y)
        frontier = new_elts

    orbit = sorted(orbit_set)
    K = len(orbit)
    idx = {s: i for i, s in enumerate(orbit)}

    omega = np.exp(2j * np.pi / p)

    A = np.zeros((K, K), dtype=complex)

    for j, s_j in enumerate(orbit):
        # Branch 1: chi_{s_j} -> (1/2) chi_{s_j * inv2}
        target1 = (s_j * inv2p) % p
        if target1 in idx:
            A[idx[target1], j] += 0.5

        # Branch 2: chi_{s_j} -> (1/2) omega^{s_j * inv2} chi_{3 * s_j * inv2}
        target2 = (3 * s_j * inv2p) % p
        phase_exp = (s_j * inv2p) % p
        phase = omega ** phase_exp
        if target2 in idx:
            A[idx[target2], j] += 0.5 * phase

    return A, orbit

# ============================================================
# Part 3: Transfer matrix parametric analysis
# ============================================================
def study_transfer_matrix_limit():
    """
    Study the K x K transfer matrix in the limit as the phase parameter -> 0.

    At t = 0 (all phases = 1), the matrix has eigenvalue 1.
    As t grows from 0, the gap opens. Question: how fast?
    """
    print("\n" + "=" * 80)
    print("PART 3: Transfer matrix - behavior as phase -> 0")
    print("=" * 80)

    test_primes = [7, 13, 31, 43, 73, 127, 157]

    for p in test_primes:
        if not is_prime(p):
            continue

        K = subgroup_order_23(p)
        if K > 100:
            continue

        inv2p = pow(2, p-2, p)
        inv3p = pow(3, p-2, p)

        # Generate <2,3> as subset of {1,...,p-1}
        orbit_set = {1}
        frontier = {1}
        while frontier:
            new_elts = set()
            for x in frontier:
                for g in [2, 3, inv2p, inv3p]:
                    y = (x * g) % p
                    if y != 0 and y not in orbit_set:
                        orbit_set.add(y)
                        new_elts.add(y)
            frontier = new_elts

        orbit = sorted(orbit_set)
        K_actual = len(orbit)
        idx = {s: i for i, s in enumerate(orbit)}

        # Phase exponents: c_j = h_j * inv2 mod p for h_j in orbit
        c_j_list = [(h * inv2p) % p for h in orbit]

        # Build matrix at t=0 (all phases = 1)
        A0 = np.zeros((K_actual, K_actual), dtype=complex)
        for j, h_j in enumerate(orbit):
            target1 = (h_j * inv2p) % p
            if target1 in idx:
                A0[idx[target1], j] += 0.5
            target2 = (3 * h_j * inv2p) % p
            if target2 in idx:
                A0[idx[target2], j] += 0.5
        evals0 = eigvals(A0)
        mags0 = np.abs(evals0)
        rho0 = np.max(mags0)

        # Parametric sweep: replace omega^{c_j} with exp(2*pi*i*t*c_j) for varying t
        t_vals = np.logspace(-6, -0.3, 500)
        rho_vals = []

        for t in t_vals:
            A = np.zeros((K_actual, K_actual), dtype=complex)
            for j, h_j in enumerate(orbit):
                target1 = (h_j * inv2p) % p
                if target1 in idx:
                    A[idx[target1], j] += 0.5
                target2 = (3 * h_j * inv2p) % p
                c_j = (h_j * inv2p) % p
                phase = np.exp(2j * np.pi * t * c_j)
                if target2 in idx:
                    A[idx[target2], j] += 0.5 * phase

            evals = eigvals(A)
            mags = np.abs(evals)
            rho_vals.append(np.max(mags))

        # Fit: rho(t) ~ rho(0) - c * t^alpha near t=0
        gaps = [rho0 - r for r in rho_vals]
        valid = [(t_vals[i], gaps[i]) for i in range(len(gaps)) if gaps[i] > 1e-12]

        alpha, c_fit = 0, 0
        if len(valid) > 10:
            log_t = np.log([v[0] for v in valid[:50]])
            log_gap = np.log([v[1] for v in valid[:50]])
            if len(log_t) > 2:
                coeffs = np.polyfit(log_t, log_gap, 1)
                alpha = coeffs[0]
                c_fit = np.exp(coeffs[1])

        # Find rho at t = 1/p (the "real" value)
        idx_real = np.searchsorted(t_vals, 1/p)
        if idx_real >= len(rho_vals):
            idx_real = len(rho_vals) - 1

        print(f"\np = {p}, K = {K_actual}:")
        print(f"  rho(0) = {rho0:.10f} (all phases = 1)")
        print(f"  rho(t) ~ {rho0:.4f} - {c_fit:.6f} * t^{alpha:.4f} for small t")
        print(f"  At t = 1/p = {1/p:.8f}: rho ~ {rho_vals[idx_real]:.10f}")
        print(f"  Eigenvalue mags at t=0: {np.sort(mags0)[::-1][:min(6,K_actual)]}")

        # Also compute at the actual value omega = exp(2*pi*i/p)
        A_real, _ = compute_orbit_matrix(p, 1)
        evals_real = eigvals(A_real)
        mags_real = np.abs(evals_real)
        print(f"  Actual eigenvalue mags (r0=1): {np.sort(mags_real)[::-1][:min(6,K_actual)]}")


def study_large_K_primes():
    """
    Hunt for primes with K = |<2,3>| in range 50-500 and compute gaps.
    """
    print("\n" + "=" * 80)
    print("PART 4: Larger K values via factoring 2^d - 1")
    print("=" * 80)

    primes_found = set()

    for d in range(1, 100):
        val = pow(2, d) - 1
        temp = val
        for f in range(2, min(int(temp**0.5) + 2, 200000)):
            while temp % f == 0:
                if f >= 5 and is_prime(f):
                    primes_found.add(f)
                temp //= f
        if temp > 1 and temp >= 5 and is_prime(temp) and temp < 100000:
            primes_found.add(temp)

    for d in range(1, 60):
        val = pow(3, d) - 1
        temp = val
        for f in range(2, min(int(temp**0.5) + 2, 200000)):
            while temp % f == 0:
                if f >= 5 and is_prime(f):
                    primes_found.add(f)
                temp //= f
        if temp > 1 and temp >= 5 and is_prime(temp) and temp < 100000:
            primes_found.add(temp)

    print(f"\nFound {len(primes_found)} candidate primes from 2^d-1 and 3^d-1")

    small_K_primes = []
    for p in sorted(primes_found):
        if p < 5 or p > 10000:
            continue
        K = subgroup_order_23(p)
        ratio = np.log(K) / np.log(p) if p > 1 else 0
        if K < p - 1:  # only non-trivial cases
            small_K_primes.append((p, K, ratio))

    small_K_primes.sort(key=lambda x: x[1])

    print(f"\n{'p':>8} | {'K':>8} | {'K/(p-1)':>10} | {'logK/logp':>12} | {'|lam2|':>12} | {'gap':>10}")
    print("-" * 80)

    rho_by_K = defaultdict(list)

    for p, K, ratio in small_K_primes:
        if p > 4000:
            continue
        try:
            lam2 = spectral_gap(p)
            gap = 1 - lam2
            print(f"{p:>8} | {K:>8} | {K/(p-1):>10.6f} | {ratio:>12.6f} | {lam2:>12.8f} | {gap:>10.8f}")
            rho_by_K[K].append((lam2, p))
        except Exception as e:
            print(f"{p:>8} | {K:>8} | ERROR: {e}")

    print(f"\nSummary: rho(K) = max |lam2| by K value:")
    print(f"{'K':>8} | {'rho(K)':>12} | {'worst p':>8} | {'gap':>10}")
    print("-" * 50)
    for K in sorted(rho_by_K.keys()):
        worst = max(rho_by_K[K], key=lambda x: x[0])
        print(f"{K:>8} | {worst[0]:>12.8f} | {worst[1]:>8} | {1-worst[0]:>10.8f}")

    return rho_by_K


def study_worst_case_phase():
    """
    For each prime p with small K, find the orbit with the largest |lambda|.
    Track the worst orbit's r_0/p and the corresponding spectral radius.
    """
    print("\n" + "=" * 80)
    print("PART 5: Worst-case orbit analysis (which r_0 gives largest |lambda|)")
    print("=" * 80)

    test_primes = []
    for p in range(5, 2500):
        if not is_prime(p):
            continue
        K = subgroup_order_23(p)
        if K <= 60 and K < p - 1:
            test_primes.append((p, K))

    test_primes.sort(key=lambda x: x[1])

    print(f"\n{'p':>8} | {'K':>6} | {'worst |lam|':>14} | {'worst r0':>10} | {'r0/p':>10} | {'min(r0)/p':>10}")
    print("-" * 80)

    for p, K in test_primes[:40]:  # limit to manageable number
        inv2p = pow(2, p-2, p)
        visited = {0}
        worst_lam = 0
        worst_r0 = 0
        all_lams = []
        min_r0 = p

        for r0 in range(1, p):
            if r0 in visited:
                continue

            A, orbit = compute_orbit_matrix(p, r0)
            visited.update(orbit)

            evals = eigvals(A)
            mags = np.abs(evals)
            max_mag = np.max(mags)
            all_lams.append(max_mag)

            if max_mag > worst_lam:
                worst_lam = max_mag
                worst_r0 = min(orbit)

            min_r0_orbit = min(orbit)
            if min_r0_orbit < min_r0:
                min_r0 = min_r0_orbit

        print(f"{p:>8} | {K:>6} | {worst_lam:>14.10f} | {worst_r0:>10} | {worst_r0/p:>10.6f} | {min_r0/p:>10.6f}")


def study_t_squared_behavior():
    """
    Precisely characterize how rho(A(t)) behaves near t=0.

    Theory: At t=0 all phases are 1 and the matrix is a stochastic matrix
    on the group, so rho = 1. Near t=0, the gap opens as c*t^alpha.

    We compute alpha precisely for several group structures.

    CRITICAL INSIGHT: The gap at t=0 is 0. But the actual primes have
    t = r_0/p >= 1/p. For fixed K, p <= 3^K, so t >= 1/3^K.
    If rho(t) = 1 - c*t^2, then gap >= c/9^K -> 0 exponentially.
    This would mean rho(K) -> 1 exponentially fast, and the universal gap
    is NOT provable by this approach.

    Alternatively, maybe the group-theoretic constraint limits which t values
    are actually achievable, giving a better bound.
    """
    print("\n" + "=" * 80)
    print("PART 6: Precise t^alpha behavior near t=0")
    print("=" * 80)

    for p in [7, 13, 31, 43, 73, 127, 211, 257, 683]:
        if not is_prime(p):
            continue

        K = subgroup_order_23(p)
        if K > 100 or K == p - 1:
            continue

        inv2p = pow(2, p-2, p)
        inv3p = pow(3, p-2, p)

        # Generate <2,3>
        orbit_set = {1}
        frontier = {1}
        while frontier:
            new_elts = set()
            for x in frontier:
                for g in [2, 3, inv2p, inv3p]:
                    y = (x * g) % p
                    if y != 0 and y not in orbit_set:
                        orbit_set.add(y)
                        new_elts.add(y)
            frontier = new_elts

        orbit = sorted(orbit_set)
        K_actual = len(orbit)
        idx_map = {s: i for i, s in enumerate(orbit)}

        # Phase exponents c_j = h_j * inv2 mod p
        c_j_list = [(h * inv2p) % p for h in orbit]

        # Very fine scan near t=0
        t_vals = np.logspace(-8, -1, 2000)
        rho_vals = []

        for t in t_vals:
            A = np.zeros((K_actual, K_actual), dtype=complex)
            for j, h_j in enumerate(orbit):
                target1 = (h_j * inv2p) % p
                if target1 in idx_map:
                    A[idx_map[target1], j] += 0.5
                target2 = (3 * h_j * inv2p) % p
                c_j = c_j_list[j]
                phase = np.exp(2j * np.pi * t * c_j)
                if target2 in idx_map:
                    A[idx_map[target2], j] += 0.5 * phase

            evals = eigvals(A)
            mags = np.abs(evals)
            rho_vals.append(np.max(mags))

        rho_vals = np.array(rho_vals)
        gaps = 1.0 - rho_vals

        # Fit log(gap) vs log(t)
        valid_mask = gaps > 1e-13
        if np.sum(valid_mask) > 20:
            log_t = np.log(t_vals[valid_mask])
            log_gap = np.log(gaps[valid_mask])
            # Use first 100 points for fit
            n_fit = min(100, len(log_t))
            coeffs = np.polyfit(log_t[:n_fit], log_gap[:n_fit], 1)
            alpha = coeffs[0]
            c_fit = np.exp(coeffs[1])

            # Also compute the gap at the actual achievable t_min = 1/p
            # and at t = 1/(3^K)
            t_min_actual = 1.0 / p
            t_min_theoretical = 1.0 / (3.0 ** K_actual)

            gap_at_actual = c_fit * t_min_actual ** alpha
            gap_at_theoretical = c_fit * t_min_theoretical ** alpha

            print(f"\np = {p}, K = {K_actual}:")
            print(f"  gap(t) ~ {c_fit:.6f} * t^{alpha:.4f}")
            print(f"  t_min = 1/p = {t_min_actual:.2e}, predicted gap = {gap_at_actual:.2e}")
            print(f"  t_min = 1/3^K = {t_min_theoretical:.2e}, predicted gap = {gap_at_theoretical:.2e}")
            print(f"  Actual gap (from full matrix): {1 - spectral_gap(p):.8f}")

            # Check: is alpha = 2 (quadratic)?
            print(f"  Exponent alpha = {alpha:.6f} (2.0 would be quadratic)")
        else:
            print(f"\np = {p}, K = {K_actual}: insufficient data for fit")


def main():
    t0 = time.time()

    # Part 1: Basic survey
    print("=" * 80)
    print("PART 1: Survey of rho(K) = max |lambda_2| over primes with |<2,3>| = K")
    print("=" * 80)

    max_p = 2000
    print(f"\nSurveying primes up to {max_p}...")

    results = survey_by_K(max_p)

    rho_K = {}
    print(f"\n{'K':>6} | {'#primes':>7} | {'primes (up to 5)':40s} | {'rho(K)':>10} | {'min gap':>10}")
    print("-" * 90)

    for K in sorted(results.keys()):
        data = results[K]
        primes = [d[0] for d in data]
        gaps = [d[1] for d in data]
        rho = max(gaps)
        min_gap = 1 - rho
        rho_K[K] = rho

        prime_str = str(primes[:5])
        if len(primes) > 5:
            prime_str = prime_str[:-1] + ", ...]"

        print(f"{K:>6} | {len(primes):>7} | {prime_str:40s} | {rho:.8f} | {min_gap:.8f}")

    # Part 2: Transfer matrix limit
    study_transfer_matrix_limit()

    # Part 3: Large K primes
    rho_by_K_large = study_large_K_primes()

    # Part 4: Worst case orbit
    study_worst_case_phase()

    # Part 5: t^alpha behavior
    study_t_squared_behavior()

    elapsed = time.time() - t0
    print(f"\n\nTotal computation time: {elapsed:.1f} seconds")


if __name__ == "__main__":
    main()
