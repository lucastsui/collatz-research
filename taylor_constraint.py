"""
NEW DIRECTION: Taylor coefficient constraints.

F_I(x) = sum 3^{k-j} x^{i_j}. If D | F_I(2), then F_I = (x-2)Q + n(x^p - 3^k).

The Taylor expansion F_I(x) = sum_{m=0}^{p-1} (F^{(m)}(2)/m!) (x-2)^m
combined with F_I = (x-2)Q + nG gives constraints on the Taylor coefficients.

Key idea: The Taylor coefficients F^{(m)}(2)/m! are "moments" of the position
distribution I, weighted by geometric coefficients. The divisibility condition
D | F_I(2) forces these moments to satisfy specific integrality/divisibility
conditions. Maybe these are incompatible with I being a valid k-subset?

Also test: the SHIFT IDENTITY. When p-1 in I:
S(sigma(I)) = (2n-1)D/3 where n = S(I)/D.
So n' = (2n-1)/3 = inverse Collatz step on n.
Iterating the shift gives a sequence of starting values.
Does this sequence have impossible properties?
"""
from itertools import combinations
from math import comb, log, factorial, gcd
from fractions import Fraction

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def taylor_coefficients(I, k, p, x0=2, max_order=None):
    """Compute F_I^{(m)}(x0)/m! for m = 0, 1, ..., min(p-1, max_order)"""
    if max_order is None:
        max_order = p - 1
    I_sorted = sorted(I)
    coeffs = []
    for m in range(max_order + 1):
        val = Fraction(0)
        for idx, j in enumerate(range(k)):
            i_j = I_sorted[j]
            coeff_3 = 3**(k-j-1)
            # d^m/dx^m [x^{i_j}] at x=x0 = i_j! / (i_j-m)! * x0^{i_j-m}
            if i_j >= m:
                falling_fact = 1
                for r in range(m):
                    falling_fact *= (i_j - r)
                term = Fraction(coeff_3 * falling_fact * x0**(i_j - m), factorial(m))
                val += term
        coeffs.append(val)
    return coeffs

def check_taylor_integrality(p, k):
    """For each I with D | S(I), check Taylor coefficient properties."""
    D = 2**p - 3**k
    if D <= 0:
        return

    print(f"\n(p,k) = ({p},{k}): D = {D}")

    # For reference, compute Taylor coefficients for ALL I
    # and check what distinguishes the ones with D | S

    # First check: are there any I with D | S?
    divisible = []
    for I in combinations(range(p), k):
        s = S_value(I, k)
        if s % D == 0:
            divisible.append((I, s // D))

    if not divisible:
        # No divisible I. Check Taylor coeff patterns for near-misses
        # (smallest |S mod D|)
        best = None
        best_rem = D
        for I in combinations(range(p), k):
            s = S_value(I, k)
            r = s % D
            r = min(r, D - r)  # distance to 0 mod D
            if r < best_rem:
                best_rem = r
                best = I

        n_approx = S_value(best, k) / D
        print(f"  No divisible I. Closest: I={best}, S/D={n_approx:.4f}, rem={best_rem}")

        # Compute Taylor coefficients for the closest I
        tc = taylor_coefficients(best, k, p, x0=2, max_order=min(5, p-1))
        print(f"  Taylor coeffs F^(m)(2)/m!: {[float(c) for c in tc[:6]]}")

        # Check: what fraction of Taylor coefficients are integers?
        int_count = sum(1 for c in tc if c.denominator == 1)
        print(f"  Integer Taylor coeffs: {int_count}/{len(tc)}")
    else:
        for I, n in divisible:
            print(f"  DIVISIBLE: I={I}, n={n}")

def shift_sequence(n, num_steps=20):
    """Apply the inverse Collatz step n -> (2n-1)/3 repeatedly.
    Only valid when n ≡ 2 mod 3."""
    seq = [n]
    for _ in range(num_steps):
        n_curr = seq[-1]
        if (2*n_curr - 1) % 3 != 0:
            break
        n_next = (2*n_curr - 1) // 3
        if n_next <= 0:
            break
        seq.append(n_next)
        if n_next == seq[0]:  # cycle detected
            break
    return seq

def analyze_shift_orbits():
    """For hypothetical cycle starting values, trace the shift sequence.
    The shift map n -> (2n-1)/3 should cycle after p steps.
    Check: does it hit any impossible values?"""
    print("\n" + "="*60)
    print("SHIFT ORBIT ANALYSIS")
    print("Inverse Collatz step: n -> (2n-1)/3")
    print("="*60)

    # The shift orbit must close after p steps.
    # For small n, compute the orbit.
    for n in [2, 5, 8, 11, 14, 17, 20, 23]:
        seq = shift_sequence(n, 30)
        print(f"\n  n={n}: orbit = {seq}")
        if len(seq) > 1 and seq[-1] == seq[0]:
            print(f"    CLOSED after {len(seq)-1} steps!")
        elif len(seq) > 1:
            print(f"    Terminated after {len(seq)-1} steps (not ≡ 2 mod 3)")

def check_mod_constraints(p, k):
    """Check: for D | S(I), what mod conditions does n = S/D satisfy?"""
    D = 2**p - 3**k
    if D <= 0:
        return

    # n must satisfy n ≡ 2 mod 3 (proved above)
    # What other mod constraints exist?

    # n mod 4:
    # S(I) = nD. S(I) mod 4 depends on I.
    # D mod 4: D = 2^p - 3^k. For p >= 2: 2^p ≡ 0 mod 4, 3^k mod 4 = 3 or 1.
    # If k odd: 3^k ≡ 3 mod 4, D ≡ -3 ≡ 1 mod 4.
    # If k even: 3^k ≡ 1 mod 4, D ≡ -1 ≡ 3 mod 4.

    D_mod4 = D % 4
    D_mod8 = D % 8
    D_mod9 = D % 9
    D_mod5 = D % 5

    print(f"\n(p,k)=({p},{k}): D={D}")
    print(f"  D mod 3 = {D%3}, D mod 4 = {D_mod4}, D mod 8 = {D_mod8}")
    print(f"  D mod 5 = {D_mod5}, D mod 9 = {D_mod9}")

    # For each I, compute n = S/D and check its mod properties
    n_values = set()
    n_mod3 = set()
    n_mod4 = set()
    n_mod8 = set()

    for I in combinations(range(p), k):
        s = S_value(I, k)
        if s % D == 0:
            n = s // D
            n_values.add(n)
            n_mod3.add(n % 3)
            n_mod4.add(n % 4)
            n_mod8.add(n % 8)

    if n_values:
        print(f"  Found {len(n_values)} divisible cases")
        print(f"  n mod 3: {sorted(n_mod3)}")
        print(f"  n mod 4: {sorted(n_mod4)}")
        print(f"  n mod 8: {sorted(n_mod8)}")
    else:
        # Check what n mod 3 WOULD be for the closest near-misses
        # This tests whether n ≡ 2 mod 3 is the ONLY mod constraint
        # or if there are additional ones
        near_n = []
        for I in combinations(range(p), k):
            s = S_value(I, k)
            r = s % D
            if r == 0:
                continue
            # n that would give this I
            n_hypothetical = s / D
            near_n.append((r, n_hypothetical, I))

        near_n.sort(key=lambda x: min(x[0], D - x[0]))
        print(f"  No divisible I. Top 5 near-misses:")
        for r, n_h, I in near_n[:5]:
            print(f"    I={I}, S/D={n_h:.6f}, remainder={min(r, D-r)}")

print("="*60)
print("TAYLOR COEFFICIENT ANALYSIS")
print("="*60)

for p in [5, 7, 8, 10, 13]:
    k = round(p * log(2) / log(3))
    if 0 < k < p:
        check_taylor_integrality(p, k)

analyze_shift_orbits()

print("\n" + "="*60)
print("MOD CONSTRAINT ANALYSIS")
print("="*60)

for p in [5, 7, 8, 10, 13, 15, 16]:
    k = round(p * log(2) / log(3))
    if 0 < k < p and 2**p - 3**k > 0:
        check_mod_constraints(p, k)
