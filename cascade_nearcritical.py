"""Cascade verification for near-critical pairs skipped in extended_v2."""

def v2(n):
    if n == 0: return 999
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v

def cascade_check(n, D, k, p, pw3):
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

pairs = [(54, 34), (59, 37)]

for p, k in pairs:
    D = 2**p - 3**k
    pw3 = [3**i for i in range(k)]
    C_min = sum(pw3[k-1-j] * 2**j for j in range(k))
    C_max = pw3[k-1] + sum(pw3[k-2-j] * 2**(p-k+1+j) for j in range(k-1))
    n_min = max(1, -(-C_min // D))
    n_max = C_max // D
    print(f"(p,k)=({p},{k}), D={D}")
    print(f"n range: [{n_min}, {n_max}]")

    total = 0
    found = 0
    for n in range(n_min, n_max + 1):
        if n % 2 == 0 or n % 3 == 0: continue
        total += 1
        if cascade_check(n, D, k, p, pw3):
            is_triv = (p == 2*k and n == 1)
            if not is_triv:
                print(f"  n={n}: NONTRIVIAL!")
                found += 1
        if total % 500000 == 0:
            print(f"  checked {total}...")

    print(f"Total candidates: {total}, nontrivial: {found}")
    print(f"RESULT: {'NO nontrivial cycles' if found == 0 else f'FOUND {found}!'}")
    print()
