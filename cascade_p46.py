"""Optimized cascade for (46,29) near-critical pair."""
from math import log

def v2(n):
    if n == 0: return 999
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v

def cascade_check(n, D, k, p):
    """Returns True if n gives a nontrivial cycle."""
    rem = n * D - 3**(k-1)
    prev_h = 0
    pw3 = [3**i for i in range(k)]  # precompute
    for j in range(1, k):
        if rem <= 0: return False
        gap = v2(rem)
        h = prev_h + gap
        if h >= p: return False
        rem = (rem >> gap) - pw3[k-1-j]
        prev_h = h
    return rem == 0

p, k = 46, 29
D = 2**p - 3**k
print(f"(p,k)=({p},{k}), D={D}")

# Compute n range
C_min = sum(3**(k-1-j) * 2**j for j in range(k))
C_max = 3**(k-1) + sum(3**(k-2-j) * 2**(p-k+1+j) for j in range(k-1))
n_min = max(1, -(-C_min // D))
n_max = C_max // D
total = 0
found = 0

print(f"n range: [{n_min}, {n_max}]")

for n in range(n_min, n_max + 1):
    if n % 2 == 0 or n % 3 == 0:
        continue
    total += 1
    if cascade_check(n, D, k, p):
        # Check if trivial
        pos = list(range(0, 2*k, 2))
        C_triv = sum(3**(k-1-j) * 2**pos[j] for j in range(k))
        if n * D == C_triv and p == 2*k:
            print(f"  n={n}: TRIVIAL CYCLE")
        else:
            print(f"  n={n}: NONTRIVIAL CYCLE FOUND!")
            found += 1
    if total % 100000 == 0:
        print(f"  checked {total} candidates...")

print(f"\nTotal candidates: {total}")
print(f"Nontrivial solutions: {found}")
print("RESULT:", "NO nontrivial cycles" if found == 0 else f"FOUND {found} cycles!")
