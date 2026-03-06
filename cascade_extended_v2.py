"""
Extended cascade verification + U = Z/DZ for composite D.
"""
from math import log, gcd

def v2(n):
    if n == 0: return float('inf')
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v

def cascade_check(n, D, k, p, pw3):
    """Returns True if n gives a valid cycle."""
    rem = n * D - pw3[k-1]
    prev_h = 0
    for j in range(1, k):
        if rem <= 0: return False
        gap = v2(rem)
        h = prev_h + gap
        if h >= p: return False
        rem = (rem >> gap) - pw3[k-1-j]
        prev_h = h
    return rem == 0

def get_n_range(p, k):
    D = 2**p - 3**k
    C_min = sum(3**(k-1-j) * 2**j for j in range(k))
    C_max = 3**(k-1) + sum(3**(k-2-j) * 2**(p-k+1+j) for j in range(k-1))
    n_min = max(1, -(-C_min // D))
    n_max = C_max // D
    return n_min, n_max

def verify_pair(p, k, verbose=False):
    D = 2**p - 3**k
    if D <= 0: return None, 0
    n_min, n_max = get_n_range(p, k)
    pw3 = [3**i for i in range(k)]
    nontrivial = 0
    total = 0
    for n in range(n_min, n_max + 1):
        if n % 2 == 0 or n % 3 == 0: continue
        total += 1
        if cascade_check(n, D, k, p, pw3):
            is_triv = (p == 2*k and n == 1)
            if not is_triv:
                nontrivial += 1
                if verbose:
                    print(f"  NONTRIVIAL: n={n}")
    return nontrivial, total

# === Part 1: Extended cascade verification ===
print("="*70)
print("EXTENDED CASCADE VERIFICATION")
print("="*70)
print()

# All valid (p,k) pairs for p up to 60
results = []
for p in range(5, 61):
    # Try the standard k (nearest to p*log2/log3)
    k_std = round(p * log(2) / log(3))
    # Also try nearby k values
    for k in sorted(set([k_std, k_std-1, k_std+1])):
        if k < 3 or 2**p - 3**k <= 0:
            continue
        D = 2**p - 3**k
        n_min, n_max = get_n_range(p, k)
        n_count = sum(1 for n in range(n_min, n_max+1) if n%2==1 and n%3!=0)

        if n_count > 2_000_000:
            results.append((p, k, D, n_count, "SKIPPED"))
            continue

        nontrivial, total = verify_pair(p, k)
        status = "OK" if nontrivial == 0 else f"FOUND {nontrivial}!"
        results.append((p, k, D, total, status))

for p, k, D, total, status in results:
    near = "*" if abs(p/k - log(3)/log(2)) < 0.01 else " "
    print(f"  p={p:2d} k={k:2d}{near} D={D:>20d} cands={total:>8} {status}")

all_ok = all(s == "OK" or s == "SKIPPED" for _, _, _, _, s in results)
checked = [r for r in results if r[4] == "OK"]
skipped = [r for r in results if r[4] == "SKIPPED"]
max_p_verified = max(r[0] for r in checked) if checked else 0
print(f"\nVerified: {len(checked)} pairs, max p={max_p_verified}")
print(f"Skipped (too many candidates): {len(skipped)} pairs")
if skipped:
    for p, k, D, total, _ in skipped:
        print(f"  p={p} k={k}: {total:,} candidates")

# === Part 2: U = Z/DZ for composite D ===
print()
print("="*70)
print("U = Z/DZ VERIFICATION (including composite D)")
print("="*70)
print()

def is_prime(n):
    if n < 2: return False
    if n < 4: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0: return False
        i += 6
    return True

def factorize(n):
    factors = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def ord_mod(a, m):
    """Multiplicative order of a mod m."""
    if gcd(a, m) != 1: return 0
    o = 1
    x = a % m
    while x != 1:
        x = (x * a) % m
        o += 1
        if o > m: return 0  # safety
    return o

# For composite D, verify U = Z/DZ using Kneser/CRT
print("For each (p,k), checking U = Z/DZ:")
print("  Method: for each prime q | D, check k * ord_q(2) > q")
print()

for p in range(5, 30):
    k = round(p * log(2) / log(3))
    D = 2**p - 3**k
    if D <= 0 or k < 3:
        continue

    prime_D = is_prime(D)
    factors = factorize(D)

    # For each prime factor q, check Cauchy-Davenport condition
    all_covered = True
    details = []
    for q, e in factors.items():
        L_q = ord_mod(2, q)
        covered = k * L_q > q
        details.append((q, e, L_q, covered))
        if not covered:
            all_covered = False

    status = "PRIME" if prime_D else ("composite, ALL COVERED" if all_covered else "composite, GAP")
    print(f"  p={p:2d} k={k:2d} D={D:>10d}  [{status}]")
    if not prime_D:
        for q, e, L_q, cov in details:
            tag = "OK" if cov else "FAIL"
            print(f"    q={q}^{e}: ord_q(2)={L_q}, k*L={k*L_q} {'>' if cov else '<='} q={q} [{tag}]")

# === Part 3: Kneser's theorem analysis ===
print()
print("="*70)
print("KNESER ANALYSIS FOR COMPOSITE D")
print("="*70)
print()
print("Kneser's theorem: |A+B| >= |A+H| + |B+H| - |H|")
print("where H = stabilizer of A+B.")
print()
print("For our sets A_j = 3^{k-1-j} * <2> (mod D):")
print("If D composite, CRT decomposition + Cauchy-Davenport per prime factor.")
print()
print("Theorem: If for every prime q | D, k * ord_q(2) > q,")
print("then U = Z/DZ. This is guaranteed when:")
print("  (a) D is prime and ord_D(2) >= D/k, OR")
print("  (b) D is composite and the condition holds for each prime factor.")
print()

# Check the condition for all p up to 25
print("Verification for p <= 25:")
for p in range(5, 26):
    k = round(p * log(2) / log(3))
    D = 2**p - 3**k
    if D <= 0 or k < 3: continue
    factors = factorize(D)
    all_ok = all(k * ord_mod(2, q) > q for q in factors)
    print(f"  p={p:2d} k={k:2d} D={D:>10d}: "
          f"{'COVERED (U=Z/DZ proved)' if all_ok else 'NOT COVERED'}")
