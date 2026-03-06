"""
Deep test of anti-correlation for S(I) divisibility.

Key question: For composite Q = q1*q2 dividing D, is
P(Q | S(I)) < P(q1 | S(I)) * P(q2 | S(I))?

Also test for Q that DON'T divide D (control experiment).
And test intermediate composites (not necessarily = D).
"""
from itertools import combinations
from math import comb, log, gcd
from collections import Counter

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def factorize(n):
    if n <= 1:
        return []
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def prime_factors(n):
    return list(set(factorize(n)))

def correlation_test(p, k, Q, label=""):
    """Test whether divisibility by Q shows anti-correlation across prime factors."""
    D = 2**p - 3**k
    C = comb(p, k)

    pf = prime_factors(Q)
    if len(pf) < 2:
        return None

    # Count divisibility by each factor and by Q
    counts = {q: 0 for q in pf}
    counts[Q] = 0
    # Also count pairwise composites
    pairs = []
    for i in range(len(pf)):
        for j in range(i+1, len(pf)):
            pairs.append((pf[i], pf[j]))
            counts[pf[i]*pf[j]] = 0

    for I in combinations(range(p), k):
        s = S_value(I, k)
        for q in pf:
            if s % q == 0:
                counts[q] += 1
        for q1, q2 in pairs:
            if s % (q1*q2) == 0:
                counts[q1*q2] += 1
        if s % Q == 0:
            counts[Q] += 1

    print(f"\n  {label}Q = {Q} = {'*'.join(map(str,pf))}, D = {D}, Q|D = {D % Q == 0}")
    for q in pf:
        print(f"    P({q}|S) = {counts[q]}/{C} = {counts[q]/C:.5f} (uniform: {1/q:.5f})")

    for q1, q2 in pairs:
        Q12 = q1 * q2
        p_joint = counts[Q12] / C if C > 0 else 0
        p_prod = (counts[q1]/C) * (counts[q2]/C) if C > 0 else 0
        ratio = p_joint / p_prod if p_prod > 0 else float('inf')
        expected_joint = 1/(q1*q2)
        print(f"    P({q1}*{q2}={Q12}|S) = {counts[Q12]}/{C} = {p_joint:.6f}")
        print(f"    P({q1})*P({q2}) = {p_prod:.6f}")
        print(f"    Ratio (joint/product) = {ratio:.4f}  {'ANTI-CORR' if ratio < 0.9 else 'POSITIVE' if ratio > 1.1 else 'NEUTRAL'}")
        print(f"    Expected uniform: {expected_joint:.6f}")

print("=" * 70)
print("TEST 1: Composite D, check anti-correlation across its factors")
print("=" * 70)

test_cases = [
    (10, 6),   # D = 295 = 5*59
    (15, 9),   # D = 13085 = 5*2617
    (16, 10),  # D = 6487 = 13*499
    (18, 11),  # D = 84997 = 11*7727
]

for p, k in test_cases:
    D = 2**p - 3**k
    if D <= 0:
        continue
    pf = prime_factors(D)
    if len(pf) >= 2:
        print(f"\n(p,k) = ({p},{k}): D = {D} = {'*'.join(map(str,pf))}")
        correlation_test(p, k, D, "D itself: ")

print("\n" + "=" * 70)
print("TEST 2: Composite moduli NOT dividing D (control)")
print("=" * 70)

for p, k in [(10, 6), (15, 9), (16, 10)]:
    D = 2**p - 3**k
    if D <= 0:
        continue
    # Test a composite Q that doesn't divide D
    for Q in [6, 15, 35, 77, 143]:
        pf = prime_factors(Q)
        if all(D % q != 0 for q in pf):  # Q shares no factors with D
            correlation_test(p, k, Q, "Control: ")
            break

print("\n" + "=" * 70)
print("TEST 3: Proper composite divisors of D (not D itself)")
print("=" * 70)

# For cases where D has 3+ factors
for p in range(5, 25):
    k = round(p * log(2) / log(3))
    if k >= p or k < 1:
        continue
    D = 2**p - 3**k
    if D <= 0:
        continue
    pf = prime_factors(D)
    if len(pf) >= 3:
        # Test a proper divisor of D with 2 prime factors
        Q = pf[0] * pf[1]
        if Q < D:
            print(f"\n(p,k) = ({p},{k}): D = {D}, testing proper divisor Q = {Q}")
            correlation_test(p, k, Q, f"Proper divisor of D: ")

print("\n" + "=" * 70)
print("TEST 4: Quantify anti-correlation strength vs p")
print("=" * 70)

for p in range(8, 22):
    k = round(p * log(2) / log(3))
    if k >= p or k < 1:
        continue
    D = 2**p - 3**k
    if D <= 0:
        continue
    C = comb(p, k)

    # For each prime q | D, compute deviation from 1/q
    pf = prime_factors(D)
    if len(pf) < 2:
        continue

    all_S = [S_value(I, k) for I in combinations(range(p), k)]

    devs = []
    for q in pf:
        count = sum(1 for s in all_S if s % q == 0)
        dev = count/C - 1/q
        devs.append((q, count/C, 1/q, dev))

    # Joint for full D
    count_D = sum(1 for s in all_S if s % D == 0)
    product = 1
    for q, prob, _, _ in devs:
        product *= prob

    print(f"p={p}, k={k}, D={D}={'*'.join(map(str,pf))}, C={C}")
    for q, prob, unif, dev in devs:
        print(f"  q={q}: P={prob:.5f}, 1/q={unif:.5f}, dev={dev:+.5f}")
    print(f"  P(D|S) = {count_D/C:.8f}, Product = {product:.8f}")
    if product > 0:
        print(f"  Ratio = {(count_D/C)/product:.6f}")
