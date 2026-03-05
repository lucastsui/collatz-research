"""
Sieve approach: for each small prime q, what fraction of parity patterns
give S ≡ 0 mod q?

S = sum_{j=1}^{k} 3^{k-j} * 2^{i_j} mod q

This is a linear function of the indicator variables x_i ∈ {0,1} 
(where x_i = 1 iff position i is an odd step).

S mod q = sum_{i=0}^{p-1} x_i * 3^{k - rank(i)} * 2^i mod q

But the rank depends on which positions are chosen, making this hard.
Instead, we can use the substitution: let the j-th odd step be at position i_j.
Then S = sum_{j=1}^k 3^{k-j} * 2^{i_j}.

For a random choice of k positions from {0,...,p-1}, what's P(S ≡ 0 mod q)?
"""

from itertools import combinations
from math import comb, log
import random

def compute_S_mod_q(odd_positions, k, q):
    S = 0
    for j_idx, i_j in enumerate(odd_positions):
        j = j_idx + 1
        S = (S + pow(3, k - j, q) * pow(2, i_j, q)) % q
    return S

def exact_fraction(p, k, q):
    """Exact count: fraction of C(p,k) patterns with S ≡ 0 mod q"""
    count_zero = 0
    total = 0
    for odd_pos in combinations(range(p), k):
        total += 1
        if compute_S_mod_q(odd_pos, k, q) == 0:
            count_zero += 1
    return count_zero / total, count_zero, total

def sample_fraction(p, k, q, samples=100000):
    """Monte Carlo estimate for larger (p,k)"""
    positions = list(range(p))
    count_zero = 0
    for _ in range(samples):
        chosen = sorted(random.sample(positions, k))
        if compute_S_mod_q(chosen, k, q) == 0:
            count_zero += 1
    return count_zero / samples

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# Small case: exact computation
print("=== Exact computation for p=15, k=9 ===\n")
p, k = 15, 9
print(f"C({p},{k}) = {comb(p,k):,}")
print(f"2^{p} - 3^{k} = {2**p - 3**k}")
print()

product = 1.0
for q in primes[:10]:
    denom_mod_q = (pow(2, p, q) - pow(3, k, q)) % q
    frac, cnt, total = exact_fraction(p, k, q)
    product *= frac
    print(f"  q={q:2d}: denom mod q = {denom_mod_q}, "
          f"P(S≡0 mod {q}) = {cnt}/{total} = {frac:.6f} "
          f"(vs 1/{q} = {1/q:.6f})")

print(f"\n  Product of fractions: {product:.10f}")
print(f"  1/C({p},{k}) = {1/comb(p,k):.10f}")
print(f"  Ratio (product / (1/C(p,k))): {product * comb(p,k):.4f}")

# Larger case: Monte Carlo
print("\n=== Monte Carlo for p=100, k=63 ===\n")
p, k = 100, 63
print(f"C({p},{k}) ~ 10^{log(comb(p,k))/log(10):.1f}")
print(f"2^{p} - 3^{k} = {2**p - 3**k}")
print()

product = 1.0
for q in primes:
    denom_mod_q = (pow(2, p, q) - pow(3, k, q)) % q
    frac = sample_fraction(p, k, q, samples=200000)
    product *= frac
    expected = 1/q if denom_mod_q != 0 else 1.0
    print(f"  q={q:2d}: denom mod q = {denom_mod_q:2d}, "
          f"P(S≡0 mod {q}) ≈ {frac:.6f} "
          f"(expected if uniform: {expected:.6f})")

print(f"\n  Product over 15 primes: {product:.2e}")
print(f"  1/prod(primes) = {1/eval('*'.join(str(q) for q in primes)):.2e}")
print(f"  If fractions ≈ 1/q, product ≈ 1/primorial(47)")

# Key question: is S mod q uniformly distributed?
print("\n=== Distribution of S mod q for p=100, k=63 ===\n")
for q in [5, 7, 11, 13]:
    counts = [0] * q
    positions = list(range(p))
    for _ in range(200000):
        chosen = sorted(random.sample(positions, k))
        r = compute_S_mod_q(chosen, k, q)
        counts[r] += 1
    print(f"  S mod {q}: {['%.4f' % (c/200000) for c in counts]}")
    print(f"  Expected uniform: {1/q:.4f} each")
    chi2 = sum((c/200000 - 1/q)**2 / (1/q) for c in counts) * 200000
    print(f"  Chi-squared: {chi2:.2f} (df={q-1})\n")
