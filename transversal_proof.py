"""
TRANSVERSAL ZERO-SUM EXCLUSION: Provable partial results.

THEOREM 1: k=1 case. S(I) = 2^{i_1}. Since gcd(2,D) = 1, D never divides S.
THEOREM 2: k=2 case. S(I) = 3*2^{i_1} + 2^{i_2}.
    Factor: S = 2^{i_1}(3 + 2^g) where g = i_2 - i_1 >= 1.
    Since gcd(2,D) = 1, need D | (3 + 2^g).
    For the range g in {1,...,p-1}: 3 + 2^g ranges from 5 to 3+2^{p-1}.
    D = 2^p - 9. So 3 + 2^g = D iff 2^g = 2^p - 12 = 4(2^{p-2}-3).
    This requires 2^{p-2}-3 to be a power of 2, which happens only for p=4.
    For p >= 5: S < D for g <= p-2, and S = 3+2^{p-1} < D for p >= 5.
    So NO cycle for k=2 for p >= 5.

THEOREM 3 (new): The tail-subtraction lemma.
    S(I) = 3^{k-1}*2^{i_1} + T where T = sum_{j=2}^k 3^{k-j}*2^{i_j}.
    If T ≡ 0 mod D, then S ≡ 3^{k-1}*2^{i_1} ≠ 0 mod D
    (since gcd(6,D) = 1).
    So: "if the tail is zero, the whole sum is nonzero."

THEOREM 4 (new): The head-subtraction lemma.
    S(I) = 2^{i_k} + H where H = sum_{j=1}^{k-1} 3^{k-j}*2^{i_j}.
    If H ≡ 0 mod D, then S ≡ 2^{i_k} ≠ 0 mod D.
    "If the head is zero, the whole sum is nonzero."

These are trivial but they show: zero-sum requires BOTH the first and
last terms to contribute nontrivially. A "partial zero-sum" in any
contiguous sub-block of terms always leaves a nonzero residue.

THEOREM 5 (new): The recursive non-vanishing.
    For S(I) ≡ 0 mod D:
    - The "tail" T_{k-1} = 2^{i_k} must be nonzero mod D. ✓ (always)
    - The "tail" T_{k-2} = 3*2^{i_{k-1}} + 2^{i_k} must be nonzero mod D.
      This requires 3*2^{i_{k-1}} + 2^{i_k} ≠ 0 mod D,
      i.e., 2^{i_k} ≠ -3*2^{i_{k-1}} mod D.
      If i_k = i_{k-1} + 1: this gives 2 ≠ -3 mod D, i.e., D ∤ 5.
      For D > 5: always true!

    More generally, the m-term tail T_m = sum_{j=m}^k 3^{k-j}*2^{i_j}
    must be nonzero mod D for zero-sum to work. Each tail is itself a
    Collatz-type sum with fewer terms.

    CONJECTURE (Recursive Exclusion): For each m, the restricted sumset
    of the m-term tail also excludes 0 mod D. If true for m = k, this
    gives the full result.

Let me verify: does the m-term tail ALSO have the transversal barrier?
"""

from itertools import combinations
from math import comb, log

def S_value(I, k):
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(k))

def tail_sum(I, k, start_j):
    """Compute sum_{j=start_j}^k 3^{k-j} * 2^{i_j}
    This is the tail starting from the start_j-th term."""
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(start_j, k))

def head_sum(I, k, end_j):
    """Compute sum_{j=1}^{end_j} 3^{k-j} * 2^{i_j}"""
    I_sorted = sorted(I)
    return sum(3**(k-j-1) * 2**I_sorted[j] for j in range(end_j))

def test_partial_sums(p, k):
    D = 2**p - 3**k
    if D <= 0:
        return

    print(f"\n{'='*60}")
    print(f"(p,k)=({p},{k}), D={D}")
    print(f"{'='*60}")

    # For each I, check if ANY partial sum (head or tail) is ≡ 0 mod D
    tail_zeros = [0] * k  # tail_zeros[m] = number of I where T_{m+1} ≡ 0
    head_zeros = [0] * k  # head_zeros[m] = number of I where H_{m} ≡ 0
    total = comb(p, k)

    for I in combinations(range(p), k):
        for m in range(k):
            # Tail: last (k-m) terms
            t = tail_sum(I, k, m)
            if t % D == 0:
                tail_zeros[m] += 1

            # Head: first (m+1) terms
            h = head_sum(I, k, m+1)
            if h % D == 0:
                head_zeros[m] += 1

    print(f"  Tail zeros (T_m ≡ 0 mod D):")
    for m in range(k):
        num_terms = k - m
        print(f"    T({m}) [{num_terms} terms]: {tail_zeros[m]}/{total} = {100*tail_zeros[m]/total:.1f}%")

    print(f"  Head zeros (H_m ≡ 0 mod D):")
    for m in range(k):
        num_terms = m + 1
        print(f"    H({m}) [{num_terms} terms]: {head_zeros[m]}/{total} = {100*head_zeros[m]/total:.1f}%")

    # KEY TEST: If S(I) = T(0) ≡ 0 mod D (which should be 0 cases),
    # can any STRICT partial sum also be ≡ 0?
    # If no partial sum is zero, that constrains the cancellation pattern.
    partial_zero_count = 0
    for I in combinations(range(p), k):
        s = S_value(I, k)
        if s % D != 0:  # Only consider non-divisible cases
            has_partial_zero = False
            for m in range(1, k):  # Skip m=0 (= S itself)
                t = tail_sum(I, k, m)
                if t % D == 0:
                    has_partial_zero = True
                    break
                h = head_sum(I, k, m)
                if h % D == 0:
                    has_partial_zero = True
                    break
            if has_partial_zero:
                partial_zero_count += 1

    print(f"\n  I with S ≢ 0 but some partial sum ≡ 0: {partial_zero_count}/{total}")

# Run tests
for p in [5, 7, 8, 10, 13]:
    k = round(p * log(2) / log(3))
    if 0 < k < p and 2**p - 3**k > 0:
        test_partial_sums(p, k)

# THEOREM VERIFICATION: k=2 case
print("\n" + "="*60)
print("THEOREM: k=2 no cycles")
print("="*60)

for p in range(5, 40):
    k = 2
    D = 2**p - 3**k
    if D <= 0:
        continue
    # S = 3*2^a + 2^b with a < b < p
    # S = 2^a * (3 + 2^{b-a})
    # Need D | (3 + 2^g) for g = b-a in {1,...,p-1}
    max_val = 3 + 2**(p-1)
    has_solution = False
    for g in range(1, p):
        if (3 + 2**g) % D == 0:
            has_solution = True
            print(f"  p={p}: CYCLE EXISTS! g={g}, 3+2^g={3+2**g}, D={D}")
            break
    if not has_solution and p <= 20:
        # Check if it's because max < D
        if max_val < D:
            reason = "SIZE (max S < D)"
        else:
            reason = "ARITHMETIC (3+2^g never ≡ 0)"
        print(f"  p={p}: No cycle. D={D}, reason: {reason}")

# NEW TEST: Consecutive partial sums
print("\n" + "="*60)
print("CONSECUTIVE PARTIAL SUM STRUCTURE")
print("For each I, what is the sequence of partial sums mod D?")
print("="*60)

for p in [5, 7]:
    k = round(p * log(2) / log(3))
    D = 2**p - 3**k
    if D <= 0:
        continue

    print(f"\n(p,k)=({p},{k}), D={D}")
    for I in combinations(range(p), k):
        s_full = S_value(I, k)
        I_sorted = sorted(I)
        partials = []
        running = 0
        for j in range(k):
            running += 3**(k-j-1) * 2**I_sorted[j]
            partials.append(running % D)
        print(f"  I={I}: partial sums mod D = {partials}, S%D={s_full%D}")
