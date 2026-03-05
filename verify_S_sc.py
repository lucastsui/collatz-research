"""Quick verification: self-consistency using the S formula."""
from itertools import combinations
from math import comb

def collatz_step(n):
    return (3*n+1)//2 if n%2==1 else n//2

def parity_seq(n0, p):
    pat = []
    n = n0
    for _ in range(p):
        pat.append(n%2)
        n = collatz_step(n)
    return tuple(pat)

sc_found = []
for p in range(2, 22):
    for k in range(1, p):
        D = 2**p - 3**k
        if D <= 0:
            continue
        if comb(p,k) > 500000:
            continue
        for pos in combinations(range(p), k):
            S = sum(pow(3, k-j-1) * pow(2, pos[j]) for j in range(k))
            if S % D != 0:
                continue
            n0 = S // D
            if n0 <= 0:
                continue
            pattern = tuple(1 if i in pos else 0 for i in range(p))
            actual = parity_seq(n0, p)
            if actual == pattern:
                sc_found.append((p, k, n0))
                label = 'TRIVIAL' if n0 <= 2 else '*** NONTRIVIAL ***'
                print(f'SC: p={p}, k={k}, n0={n0} {label}')

if not any(n0 > 2 for _, _, n0 in sc_found):
    print(f'\nAll {len(sc_found)} SC solutions are trivial (n0<=2).')
else:
    print(f'\n!!! NONTRIVIAL CYCLES FOUND !!!')
