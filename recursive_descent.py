"""
RECURSIVE DESCENT APPROACH

Key idea: S(I) = 3^{k-1} * 2^{i_1} + T(I')
where I' = {i_2,...,i_k} is the "remaining" subset.
T(I') = sum_{j=2}^k 3^{k-j} * 2^{i_j}.

For S(I) ≡ 0 mod D: 3^{k-1} * 2^{i_1} ≡ -T(I') mod D.

This determines i_1 given I' (as a discrete log):
2^{i_1} ≡ -T(I') / 3^{k-1} mod D.

The question: is this i_1 in {0,...,min(I')-1}?

RECURSIVE STRUCTURE:
T(I') itself is a Collatz-type sum with k-1 terms and positions from
{i_2,...,i_k} ⊂ {0,...,p-1}. It has the same structure as S but with
one fewer term.

If we could show that T(I') mod D is NEVER in the coset
-3^{k-1} * {2^0, 2^1, ..., 2^{min(I')-1}} mod D,
that would prove S(I) ≠ 0.

This is a COSET AVOIDANCE problem:
The (k-1)-term restricted sumset must avoid a specific set of residues.

Let me compute: for each (p,k), what fraction of (k-1)-subsets I' have
T(I') in the "dangerous" coset that would allow cancellation with the
first term?
"""

from itertools import combinations
from math import comb, log, gcd

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def tail_value(I_prime, k):
    """Compute T(I') = sum_{j=2}^k 3^{k-j} * 2^{i_j}
    where I_prime = {i_2,...,i_k} sorted, using weights 3^{k-2},...,1."""
    I_sorted = sorted(I_prime)
    kp = len(I_sorted)
    return sum(3**(kp-j-1) * 2**I_sorted[j] for j in range(kp))

def multiplicative_order(a, n):
    if gcd(a, n) != 1: return None
    r, x = 1, a % n
    while x != 1:
        x = (x * a) % n
        r += 1
        if r > n: return None
    return r

def discrete_log_2(target, D, L):
    """Find i such that 2^i ≡ target mod D, if it exists.
    Returns i in {0,...,L-1} or None."""
    x = 1
    for i in range(L):
        if x == target % D:
            return i
        x = (x * 2) % D
    return None

def analyze_recursive(p, k):
    D = 2**p - 3**k
    if D <= 0:
        return

    L = multiplicative_order(2, D)
    inv_3k1 = pow(3, D - 1 - (k-1) % (D-1), D) if D > 1 else 1  # 3^{-(k-1)} mod D
    # Actually: 3^{k-1} mod D, then its inverse
    coeff = pow(3, k-1, D)
    inv_coeff = pow(coeff, D-2, D) if D > 1 else 1  # Fermat inverse (D prime)

    C = comb(p, k)

    print(f"\n{'='*60}")
    print(f"(p,k)=({p},{k}), D={D}, L=ord_D(2)={L}")
    print(f"{'='*60}")

    # For each (k-1)-subset I' ⊂ {0,...,p-1}:
    # Compute T(I') and check if the required i_1 exists
    dangerous_count = 0
    safe_count = 0
    total = 0

    for I_prime in combinations(range(p), k-1):
        I_prime_sorted = sorted(I_prime)
        min_pos = I_prime_sorted[0]

        # T(I') with the STANDARD Collatz weighting for k-1 terms
        T = tail_value(I_prime, k)

        # Required: 2^{i_1} ≡ -T / 3^{k-1} mod D
        target = (D - T % D) * inv_coeff % D

        if target == 0:
            # Would need 2^{i_1} ≡ 0, impossible
            safe_count += 1
        else:
            # Find discrete log
            i_1 = discrete_log_2(target, D, L)

            if i_1 is not None and 0 <= i_1 < min_pos:
                # DANGER: the required i_1 exists and is in valid range!
                dangerous_count += 1
                if total < 5:
                    # Verify
                    I_full = tuple(sorted([i_1] + list(I_prime)))
                    S = S_value(I_full, k)
                    print(f"  DANGEROUS: I'={I_prime}, T={T}, target=2^{i_1}={target}")
                    print(f"    Full I={I_full}, S={S}, S%D={S%D}")
            else:
                safe_count += 1

        total += 1

    print(f"  Total (k-1)-subsets: {total}")
    print(f"  Dangerous (i_1 exists in range): {dangerous_count}")
    print(f"  Safe (i_1 doesn't exist or out of range): {safe_count}")
    print(f"  Danger rate: {100*dangerous_count/total:.1f}%")

    if dangerous_count == 0:
        print(f"  >>> NO dangerous cases! Zero-sum IMPOSSIBLE by recursive descent! <<<")

# Test
is_prime = lambda n: n > 1 and all(n % i for i in range(2, min(int(n**0.5)+1, 10000)))

for p in [5, 7, 8, 10, 13, 15, 16]:
    k = round(p * log(2) / log(3))
    D = 2**p - 3**k
    if D <= 0 or k >= p or k < 2:
        continue
    if not is_prime(D):
        # Skip composite D for now (Fermat inverse not valid)
        print(f"\n(p,k)=({p},{k}): D={D} is COMPOSITE, skipping (need extended analysis)")
        continue
    analyze_recursive(p, k)
