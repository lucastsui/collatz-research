#!/usr/bin/env python3
"""
Compute rad(2^p - 3^k) for p up to ~200, where k = floor(p * log2/log3)
and nearby values giving D > 0.

Outputs:
  - Table of (p, k, D, factorization, rad(D), rad(D)/D, log2(rad(D))/p)
  - Statistics on squarefreeness
  - Comparison with the abc-barrier threshold 0.95p
"""

from math import log, log2, floor, gcd, isqrt
from collections import defaultdict
import time

def trial_factor(n, limit=10**7):
    """Factor n by trial division up to limit. Return (factors_dict, cofactor)."""
    factors = {}
    d = 2
    while d * d <= n and d <= limit:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2
    return factors, n

def is_prime_miller_rabin(n, witnesses=None):
    """Miller-Rabin primality test."""
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    if witnesses is None:
        # Deterministic for n < 3.317e24
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in witnesses:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def pollard_rho(n):
    """Pollard's rho algorithm for factoring."""
    if n % 2 == 0:
        return 2

    from random import randint
    x = randint(2, n - 1)
    y = x
    c = randint(1, n - 1)
    d = 1

    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(abs(x - y), n)

    return d if d != n else None

def full_factor(n):
    """Fully factor n using trial division + Pollard rho."""
    if n <= 1:
        return {}

    factors = {}

    # Trial division for small primes
    trial_facts, cofactor = trial_factor(n, limit=10**6)
    factors.update(trial_facts)

    # Factor the cofactor
    stack = [cofactor]
    while stack:
        m = stack.pop()
        if m <= 1:
            continue
        if is_prime_miller_rabin(m):
            factors[m] = factors.get(m, 0) + 1
            continue

        # Try Pollard rho
        found = False
        for attempt in range(50):
            d = pollard_rho(m)
            if d and d != m:
                stack.append(d)
                stack.append(m // d)
                found = True
                break

        if not found:
            # Fallback: more trial division
            trial_facts2, cofactor2 = trial_factor(m, limit=10**8)
            for p, e in trial_facts2.items():
                factors[p] = factors.get(p, 0) + e
            if cofactor2 > 1:
                if is_prime_miller_rabin(cofactor2):
                    factors[cofactor2] = factors.get(cofactor2, 0) + 1
                else:
                    # Give up and mark as composite
                    factors[cofactor2] = factors.get(cofactor2, 0) + 1
                    print(f"  WARNING: could not fully factor {cofactor2}")

    return factors

def rad(factors):
    """Compute radical from factorization dict."""
    result = 1
    for p in factors:
        result *= p
    return result

def main():
    log2_log3 = log(2) / log(3)

    print("=" * 120)
    print("RADICAL OF D = 2^p - 3^k WHERE k ≈ p·log2/log3")
    print("=" * 120)
    print()

    results = []

    for p in range(2, 201):
        k_center = floor(p * log2_log3)

        # Try k = k_center and k_center + 1 (sometimes k_center+1 also gives D>0 and is closer)
        for k in [k_center, k_center + 1]:
            D = (1 << p) - 3**k
            if D <= 0:
                continue

            # Only use the k closest to p*log2/log3
            # For this survey, take both if D > 0

            t0 = time.time()
            factors = full_factor(D)
            t1 = time.time()

            r = rad(factors)

            # Check factorization
            product_check = 1
            for prime, exp in sorted(factors.items()):
                product_check *= prime ** exp
            assert product_check == D, f"Factorization error: {product_check} != {D}"

            is_squarefree = all(e == 1 for e in factors.values())
            num_primes = len(factors)
            max_exp = max(factors.values()) if factors else 0

            log2_rad = log2(r) if r > 0 else 0
            ratio = log2_rad / p if p > 0 else 0
            rad_over_D = r / D

            fact_str = " * ".join(
                f"{prime}" + (f"^{exp}" if exp > 1 else "")
                for prime, exp in sorted(factors.items())
            )
            if len(fact_str) > 60:
                fact_str = fact_str[:57] + "..."

            results.append({
                'p': p, 'k': k, 'D': D,
                'factors': factors,
                'rad': r, 'log2_rad': log2_rad,
                'ratio': ratio, 'rad_over_D': rad_over_D,
                'is_squarefree': is_squarefree,
                'num_primes': num_primes,
                'max_exp': max_exp,
                'time': t1 - t0,
                'fact_str': fact_str
            })

            marker = "  " if is_squarefree else "* "
            print(f"{marker}p={p:3d}, k={k:3d}, "
                  f"log2(D)={log2(D):7.2f}, "
                  f"log2(rad)={log2_rad:7.2f}, "
                  f"ratio={ratio:.4f}, "
                  f"rad/D={rad_over_D:.6f}, "
                  f"sqfree={'Y' if is_squarefree else 'N'}, "
                  f"#primes={num_primes:2d}, "
                  f"maxexp={max_exp}, "
                  f"time={t1-t0:.3f}s")

    print()
    print("=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)

    # Filter to k = floor(p*log2/log3) entries (the "canonical" ones)
    canonical = []
    seen_p = set()
    for r in results:
        if r['p'] not in seen_p:
            canonical.append(r)
            seen_p.add(r['p'])

    total = len(canonical)
    sqfree_count = sum(1 for r in canonical if r['is_squarefree'])

    print(f"\nTotal (p, k) pairs computed: {len(results)}")
    print(f"Canonical pairs (first k for each p): {total}")
    print(f"Squarefree D: {sqfree_count}/{total} = {sqfree_count/total:.1%}")

    ratios = [r['ratio'] for r in canonical if r['p'] >= 10]
    if ratios:
        print(f"\nlog2(rad(D))/p statistics (p >= 10):")
        print(f"  Min:    {min(ratios):.4f}")
        print(f"  Max:    {max(ratios):.4f}")
        print(f"  Mean:   {sum(ratios)/len(ratios):.4f}")
        print(f"  Median: {sorted(ratios)[len(ratios)//2]:.4f}")

    # How many satisfy rad(D) > 2^{0.95p}?
    above_095 = sum(1 for r in canonical if r['ratio'] >= 0.95 and r['p'] >= 10)
    above_090 = sum(1 for r in canonical if r['ratio'] >= 0.90 and r['p'] >= 10)
    above_080 = sum(1 for r in canonical if r['ratio'] >= 0.80 and r['p'] >= 10)
    n10 = sum(1 for r in canonical if r['p'] >= 10)

    print(f"\nThreshold analysis (p >= 10, n={n10}):")
    print(f"  log2(rad)/p >= 0.95: {above_095}/{n10} = {above_095/n10:.1%}")
    print(f"  log2(rad)/p >= 0.90: {above_090}/{n10} = {above_090/n10:.1%}")
    print(f"  log2(rad)/p >= 0.80: {above_080}/{n10} = {above_080/n10:.1%}")

    # Worst cases
    print(f"\nSmallest log2(rad(D))/p values (p >= 10):")
    worst = sorted(canonical, key=lambda r: r['ratio'])
    for r in worst[:20]:
        if r['p'] >= 10:
            print(f"  p={r['p']:3d}, k={r['k']:3d}, ratio={r['ratio']:.4f}, "
                  f"sqfree={'Y' if r['is_squarefree'] else 'N'}, "
                  f"factorization: {r['fact_str']}")

    # Distribution of max exponent
    print(f"\nMax prime power exponent distribution:")
    exp_dist = defaultdict(int)
    for r in canonical:
        exp_dist[r['max_exp']] += 1
    for e in sorted(exp_dist):
        print(f"  max_exp={e}: {exp_dist[e]} cases")

    # Cases with large prime powers
    print(f"\nCases with max exponent >= 3:")
    for r in canonical:
        if r['max_exp'] >= 3:
            print(f"  p={r['p']:3d}, k={r['k']:3d}, D={r['D']}, "
                  f"factorization: {r['fact_str']}")

    # GCD structure: which small primes divide D most often?
    print(f"\nSmall prime frequency among D values (p >= 10):")
    small_primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for q in small_primes:
        count = sum(1 for r in canonical if r['p'] >= 10 and q in r['factors'])
        total_10 = sum(1 for r in canonical if r['p'] >= 10)
        expected = 1/q
        print(f"  {q:3d} divides D: {count}/{total_10} = {count/total_10:.3f} (expected ~{expected:.3f})")

    print()
    print("=" * 80)
    print("PRIMITIVE PRIME DIVISOR ANALYSIS")
    print("=" * 80)

    # For each p, find primes dividing D(p) that don't divide any D(p') for p' < p
    all_primes_seen = set()
    primitive_data = []

    for r in canonical:
        p = r['p']
        primes_of_D = set(r['factors'].keys())
        new_primes = primes_of_D - all_primes_seen

        primitive_data.append({
            'p': p, 'k': r['k'],
            'num_primes': len(primes_of_D),
            'num_new': len(new_primes),
            'new_primes': sorted(new_primes),
        })

        all_primes_seen |= primes_of_D

    print(f"\nPrimitive prime divisors (primes appearing for first time):")
    for pd in primitive_data:
        if pd['p'] <= 50 or pd['num_new'] == 0:
            new_str = str(pd['new_primes'][:5])
            if len(pd['new_primes']) > 5:
                new_str += f" ... ({len(pd['new_primes'])} total)"
            print(f"  p={pd['p']:3d}: {pd['num_primes']} primes, "
                  f"{pd['num_new']} new: {new_str}")

    # Cases with NO new primes
    no_new = [pd for pd in primitive_data if pd['num_new'] == 0 and pd['p'] >= 5]
    if no_new:
        print(f"\nCases with NO primitive prime divisor (p >= 5):")
        for pd in no_new:
            r = next(r for r in canonical if r['p'] == pd['p'])
            print(f"  p={pd['p']:3d}, k={pd['k']:3d}, D={r['D']}, fact={r['fact_str']}")
    else:
        print(f"\nEvery D(p) for p >= 5 introduces at least one new prime!")

if __name__ == "__main__":
    main()
