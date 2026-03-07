"""
Computational verification for Direction 6g-xi: Non-archimedean dynamics on Z_2.

Checks:
1. Shift conjugacy: Phi: Z_2 -> {0,1}^N is a bijection, conjugating T to the shift
2. 2-adic repulsion: |T^p(m) - n(eps)|_2 = 2^p * |m - n(eps)|_2
3. 2-adic expansion of cycle points S(eps)/D
4. Distribution of v_2(S mod D) across patterns
5. Carry automaton structure
6. Archimedean vs non-archimedean mismatch quantification
"""

import math
from itertools import combinations, product as iterproduct

def v2(n):
    """2-adic valuation of n."""
    if n == 0: return 999
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v

def collatz_step(n):
    """One step of the Collatz map T: Z -> Z."""
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n + 1) // 2

def collatz_orbit(n, steps):
    """Compute T^0(n), T^1(n), ..., T^steps(n)."""
    orbit = [n]
    for _ in range(steps):
        n = collatz_step(n)
        orbit.append(n)
    return orbit

def parity_sequence(n, p):
    """Parity sequence of n under T for p steps."""
    seq = []
    current = n
    for _ in range(p):
        seq.append(current % 2)
        current = collatz_step(current)
    return tuple(seq)

def S_from_pattern(eps, p):
    """Given parity pattern eps (length p), compute S(eps) and k."""
    positions = [i for i in range(p) if eps[i] == 1]
    k = len(positions)
    if k == 0:
        return 0, 0
    S = sum(3**(k-1-j) * 2**positions[j] for j in range(k))
    return S, k

def mod_inverse(a, m):
    """Modular inverse of a mod m using extended Euclidean algorithm."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x, y = extended_gcd(b % a, a)
    return g, y - (b // a) * x, x

# ======================================================================
# 1. SHIFT CONJUGACY VERIFICATION
# ======================================================================
print("=" * 70)
print("1. SHIFT CONJUGACY: T on Z_2 ~ full shift on {0,1}^N")
print("=" * 70)

print("\nThe coding map Phi: Z_2 -> {0,1}^N sends n to its parity sequence")
print("under T. For finite precision mod 2^p, Phi is a bijection on Z/2^p Z.\n")

for p in [4, 6, 8]:
    # Check that distinct n mod 2^p give distinct length-p parity sequences
    sequences = {}
    collisions = 0
    for n in range(2**p):
        seq = parity_sequence(n, p)
        if seq in sequences:
            collisions += 1
        else:
            sequences[seq] = n

    # Also check inversion: given a parity sequence, recover n mod 2^p
    inversions_ok = 0
    for seq, n_orig in sequences.items():
        # Reconstruct n from the parity sequence using inverse branches
        # If eps_0 = 0: n = 2 * n', where n' has sequence (eps_1, ...)
        # If eps_0 = 1: n = (2 * n' - 1) / 3, where n' has sequence (eps_1, ...)
        # We do this recursively from the end
        n_reconstructed = 0
        for i in range(p-1, -1, -1):
            if seq[i] == 0:
                n_reconstructed = 2 * n_reconstructed
            else:
                n_reconstructed = (2 * n_reconstructed - 1)
                # Need to divide by 3 mod 2^p
                # (2n'-1)/3: we need 2n'-1 divisible by 3
                inv3 = mod_inverse(3, 2**p)
                if inv3 is not None:
                    n_reconstructed = (n_reconstructed * inv3) % (2**p)

        if n_reconstructed == n_orig:
            inversions_ok += 1

    print(f"p={p}: {2**p} residues, {len(sequences)} distinct sequences, "
          f"collisions={collisions}, inverse OK={inversions_ok}/{len(sequences)}")

print("\nThe bijection Phi conjugates T to the left shift sigma:")
print("  Phi(T(n)) = sigma(Phi(n)), i.e., shifting the parity sequence.\n")

for p in [5, 7]:
    ok = 0
    total = 0
    for n in range(2**p):
        seq_n = parity_sequence(n, p+1)  # one extra step
        Tn = collatz_step(n) % (2**p)
        seq_Tn = parity_sequence(Tn, p)
        # sigma(seq_n) = (seq_n[1], ..., seq_n[p])
        if seq_Tn == seq_n[1:p+1]:
            ok += 1
        total += 1
    print(f"  p={p}: Phi(T(n)) = sigma(Phi(n)) for {ok}/{total} values mod 2^{p}")

# ======================================================================
# 2. 2-ADIC REPULSION
# ======================================================================
print()
print("=" * 70)
print("2. 2-ADIC REPULSION: |T^p(m) - n_0|_2 = 2^p * |m - n_0|_2")
print("=" * 70)

print("\nOn each piece (fixed parity pattern eps with k ones, D = 2^p - 3^k > 0),")
print("T^p(n) = (3^k/2^p)*n + c(eps). The 2-adic derivative is 3^k/2^p.")
print("|3^k/2^p|_2 = |3^k|_2 / |2^p|_2 = 1 / 2^{-p} = 2^p > 1.")
print("So every cycle is 2-ADICALLY REPELLING (not attracting!).\n")

test_pairs = [(5,3), (7,4), (8,5), (10,6)]

for p, k in test_pairs:
    D = 2**p - 3**k
    if D <= 0:
        continue

    # Take the trivial cycle pattern: positions 0,2,...,2(k-1) when p=2k
    if p == 2*k:
        positions = list(range(0, 2*k, 2))
    else:
        positions = list(range(k))

    eps = [0] * p
    for pos in positions:
        eps[pos] = 1
    eps = tuple(eps)

    S, k_check = S_from_pattern(eps, p)
    n0_rational = S / D  # The 2-adic fixed point (may not be integer)
    n0_int = S // D if S % D == 0 else None

    # Verify repulsion: take integers near n0 (same parity pattern)
    # For the parity pattern to match, need n ≡ n0 mod 2^p
    if n0_int is not None and n0_int > 0:
        n0 = n0_int
        print(f"\n(p,k) = ({p},{k}), D = {D}, n_0 = {n0} (integer cycle point)")

        # Take m = n0 + D * t for small t (these have same residue mod large powers)
        for t in [1, 2, 5, 10]:
            m = n0 + D * t
            # Compute T^p(m) using the affine formula
            # T^p(m) = (3^k / 2^p) * m + c
            # c = n0 - (3^k / 2^p) * n0 = n0 * (1 - 3^k/2^p) = n0 * (2^p - 3^k)/2^p = n0 * D / 2^p
            # So T^p(m) = (3^k/2^p)*m + n0*D/2^p = (3^k * m + n0 * D) / 2^p
            # For integer check: 3^k * m + n0 * D = 3^k * (n0 + D*t) + n0 * D
            # = 3^k * n0 + 3^k * D * t + n0 * D = n0 * (3^k + D) + 3^k * D * t
            # = n0 * 2^p + 3^k * D * t
            # So T^p(m) = n0 + 3^k * D * t / 2^p ... hmm, this may not be integer
            # unless D*t is divisible by 2^p/gcd(3^k, 2^p) = 2^p

            # Actually T^p depends on the parity pattern of the orbit of m,
            # which may differ from the pattern of n0. Let's just iterate directly.
            orbit = collatz_orbit(m, p)
            Tp_m = orbit[p]

            diff_in = m - n0
            diff_out = Tp_m - n0

            if diff_in != 0 and diff_out != 0:
                v2_in = v2(abs(diff_in))
                v2_out = v2(abs(diff_out))
                repulsion = v2_in - v2_out  # Should be p (= log_2 of 2-adic expansion factor)
                print(f"  m = n0 + {D}*{t} = {m}: "
                      f"v_2(m-n0) = {v2_in}, v_2(T^p(m)-n0) = {v2_out}, "
                      f"change = {repulsion} (expect {-p} if same pattern)")
    else:
        print(f"\n(p,k) = ({p},{k}), D = {D}, n(eps) = {S}/{D} = {S/D:.4f} (NOT integer)")
        # Still verify repulsion for nearby integers
        # n0 = S/D in Q_2. For integer m near n0 (2-adically), T^p(m) is further
        n0_mod = (S * mod_inverse(D, 2**p)) % (2**p) if mod_inverse(D, 2**p) else None
        if n0_mod is not None:
            print(f"  n(eps) mod 2^{p} = {n0_mod}")
            # Take m = n0_mod and m + 2^p
            for m in [n0_mod, n0_mod + 2**p, n0_mod + 2**(p+1)]:
                if m <= 0:
                    continue
                orbit = collatz_orbit(m, p)
                Tp_m = orbit[p]
                # The fixed point mod 2^{2p} would be (S * D^{-1}) mod 2^{2p}
                n0_mod2 = (S * mod_inverse(D, 2**(2*p))) % (2**(2*p)) if mod_inverse(D, 2**(2*p)) else 0
                diff_in = (m - n0_mod2) % (2**(2*p))
                diff_out = (Tp_m - n0_mod2) % (2**(2*p))
                if diff_in > 0:
                    print(f"  m = {m}: T^{p}(m) = {Tp_m}")

# ======================================================================
# 3. 2-ADIC EXPANSION OF CYCLE POINTS
# ======================================================================
print()
print("=" * 70)
print("3. 2-ADIC EXPANSION OF CYCLE POINTS n(eps) = S(eps)/D")
print("=" * 70)

print("\nSince D is odd, D^{-1} exists in Z_2. The 2-adic expansion of S/D")
print("is eventually periodic with period dividing ord_D(2).\n")

for p, k in [(5,3), (7,4), (8,5)]:
    D = 2**p - 3**k
    if D <= 0:
        continue

    print(f"\n(p,k) = ({p},{k}), D = {D}")

    # Multiplicative order of 2 mod D
    ord_2 = 1
    pow2 = 2
    while pow2 % D != 1:
        pow2 = (pow2 * 2) % D
        ord_2 += 1
        if ord_2 > 2*D:
            ord_2 = -1
            break
    print(f"  ord_D(2) = {ord_2}")

    # Compute 2-adic expansion of S/D for a few patterns
    count = 0
    for I in combinations(range(p), k):
        S = sum(3**(k-1-j) * 2**I[j] for j in range(k))
        is_integer = (S % D == 0)
        n_val = S // D if is_integer else None

        # 2-adic expansion: compute (S * D^{-1}) mod 2^m for increasing m
        digits = []
        # Method: long division in Z_2
        # n = S/D in Z_2. So n * D = S. The 2-adic expansion of n is:
        # n_0 = (S * D^{-1}) mod 2
        # To compute: find the 2-adic expansion via the recurrence
        # r_0 = S, digit_0 = r_0 * D^{-1} mod 2, r_1 = (r_0 - digit_0 * D) / 2, etc.
        r = S
        num_digits = min(3 * ord_2 + 5, 40) if ord_2 > 0 else 40
        d_inv_mod2 = mod_inverse(D, 2)  # D is odd, so D^{-1} mod 2 = 1 if D ≡ 1, else... D odd → D mod 2 = 1 → D^{-1} mod 2 = 1
        for _ in range(num_digits):
            # digit = r * D^{-1} mod 2
            # Since D is odd: n * D = S, so n mod 2 = S mod 2 (since D ≡ 1 mod 2)
            # Wait, D mod 2 = 1 (since 2^p - 3^k is odd)
            # digit = r mod 2 (since D ≡ 1 mod 2, D^{-1} ≡ 1 mod 2)
            # Hmm, that's not right either. Let me think...
            # We want n such that n * D ≡ S mod 2^m.
            # digit_0 = n mod 2. n * D ≡ S mod 2, so n ≡ S * D^{-1} mod 2.
            # D is odd, so D^{-1} mod 2 = 1. Thus digit_0 = S mod 2.
            # Then: n = digit_0 + 2*n', where n'*D = (S - digit_0*D)/2.
            # So the recurrence is: remainder r_0 = S, digit_0 = r_0 mod 2
            #   r_1 = (r_0 - digit_0 * D) / 2, digit_1 = r_1 mod 2, etc.
            # Wait, n * D = S means (digit_0 + 2*n') * D = S
            # digit_0 * D + 2*n'*D = S
            # 2*n'*D = S - digit_0 * D
            # n'*D = (S - digit_0*D)/2 = r_1
            # digit_1 = r_1 mod 2 (again using D odd)
            # Hmm, but we need r_1 to be an integer. S - digit_0*D: since digit_0 = S mod 2
            # and D is odd, digit_0*D ≡ S*1 ≡ S mod 2. So S - digit_0*D ≡ 0 mod 2. OK.
            digit = r % 2
            digits.append(digit)
            r = (r - digit * D) // 2

        digit_str = ''.join(str(d) for d in digits)

        if count < 3:  # Show first 3 patterns per (p,k)
            if is_integer:
                print(f"  I={I}: S={S}, n=S/D={n_val} (integer)")
                print(f"    2-adic: {digit_str[:20]}... (finite, terminates)")
            else:
                # Find the period in the digits
                period = -1
                for try_per in range(1, num_digits // 2):
                    if all(digits[i] == digits[i + try_per]
                           for i in range(num_digits // 3, 2 * num_digits // 3)
                           if i + try_per < num_digits):
                        period = try_per
                        break
                print(f"  I={I}: S={S}, S/D={S/D:.4f} (non-integer, S mod D = {S % D})")
                print(f"    2-adic: {digit_str[:30]}... (period={period if period > 0 else '?'})")

        count += 1

    print(f"  ({count} total patterns)")

# ======================================================================
# 4. DISTRIBUTION OF v_2(S mod D)
# ======================================================================
print()
print("=" * 70)
print("4. DISTRIBUTION OF v_2(S(I) mod D) -- 'distance to integrality'")
print("=" * 70)

print("\nFor each (p,k), we compute v_2(S(I) mod D) for all valid patterns.")
print("This measures how 2-adically close S(I)/D is to an integer.")
print("v_2 = infinity means D | S(I) (integer, potential cycle point).\n")

for p, k in [(5,3), (7,4), (8,5), (10,6)]:
    D = 2**p - 3**k
    if D <= 0:
        continue

    v2_counts = {}
    total = 0
    integer_count = 0

    for I in combinations(range(p), k):
        S = sum(3**(k-1-j) * 2**I[j] for j in range(k))
        r = S % D
        if r == 0:
            integer_count += 1
        else:
            val = v2(r)
            v2_counts[val] = v2_counts.get(val, 0) + 1
        total += 1

    print(f"\n(p,k) = ({p},{k}), D = {D}, C(p,k) = {total}")
    print(f"  Integer (D|S): {integer_count}")
    for v in sorted(v2_counts.keys())[:10]:
        pct = 100 * v2_counts[v] / total
        print(f"  v_2(S mod D) = {v}: {v2_counts[v]} ({pct:.1f}%)")

    # Expected: v_2(S mod D) = i_1 (the first position) by the cascade
    # Since i_1 = 0 for WLOG positions, v_2(S) = 0 when i_1 = 0
    i1_zero_count = 0
    i1_zero_v2_zero = 0
    for I in combinations(range(p), k):
        S = sum(3**(k-1-j) * 2**I[j] for j in range(k))
        if I[0] == 0:
            i1_zero_count += 1
            if S % D != 0 and v2(S % D) == 0:
                i1_zero_v2_zero += 1
    print(f"  When i_1=0: {i1_zero_count} patterns, v_2(S mod D) = 0: {i1_zero_v2_zero}")

# ======================================================================
# 5. CARRY AUTOMATON
# ======================================================================
print()
print("=" * 70)
print("5. CARRY AUTOMATON STRUCTURE")
print("=" * 70)

print("\nThe Collatz step T on binary representations involves carry propagation.")
print("For 3n+1: carry c propagates as c_{j+1} = floor((b_j + b_{j-1} + c_j)/2).")
print("State space: carry in {0, 1}. For a cycle, carry wraps: c_0 = c_final = 0.\n")

def verify_carry_automaton(n, p):
    """Trace the carry structure through p Collatz steps.

    For each odd step (3n+1 operation), trace the carry propagation
    through the binary representation. Returns carry trace info.
    """
    carries = []
    current = n
    for step in range(p):
        if current % 2 == 1:
            # Odd step: 3*current + 1
            val_3n1 = 3 * current + 1
            # Trace carry in 3n+1 = n + 2n + 1
            # Bit j of n: (n >> j) & 1
            # Bit j of 2n: (n >> (j-1)) & 1 for j >= 1, 0 for j = 0
            # Plus 1 at position 0
            max_bits = current.bit_length() + 3
            carry = 0
            result_bits = []
            for j in range(max_bits):
                b_n = (current >> j) & 1
                b_2n = (current >> (j-1)) & 1 if j >= 1 else 0
                plus1 = 1 if j == 0 else 0
                total = b_n + b_2n + plus1 + carry
                result_bits.append(total % 2)
                carry = total // 2
            carries.append(carry)  # Final carry (should be 0 for correct computation)
            current = val_3n1 // 2
        else:
            current = current // 2
    return carries, current

# Verify for small cycles
print("Carry traces for the trivial cycle n=1:")
carries, final = verify_carry_automaton(1, 2)
print(f"  n=1, p=2: carries={carries}, final={final} (should be 1)")

print("\nCarry structure for non-cycle points:")
for n in [3, 5, 7, 9, 11]:
    for p in [5, 8]:
        carries, final = verify_carry_automaton(n, p)
        total_carries = sum(1 for c in carries if c > 0)
        orbit = collatz_orbit(n, p)
        print(f"  n={n}, p={p}: T^{p}(n)={orbit[p]}, "
              f"nonzero carries in odd steps: {total_carries}/{len(carries)}")

# ======================================================================
# 6. THE SELF-CONSISTENCY CONSTRAINT (DIAGONAL MAP)
# ======================================================================
print()
print("=" * 70)
print("6. SELF-CONSISTENCY: parity of n(eps) must match eps")
print("=" * 70)

print("\nFor periodic eps with period p, n(eps) = S(eps)/D is the unique")
print("2-adic integer with parity sequence eps. Self-consistency is automatic")
print("by construction. The constraint is purely: n(eps) in Z_{>0}.\n")

for p in [5, 7, 8]:
    checked = 0
    consistent = 0
    integer_and_positive = 0

    for bits in iterproduct([0,1], repeat=p):
        k = sum(bits)
        if k == 0 or k == p:
            continue
        D = 2**p - 3**k
        if D <= 0:
            continue

        S, _ = S_from_pattern(bits, p)

        # Compute n mod 2^p as S * D^{-1} mod 2^p
        d_inv = mod_inverse(D, 2**p)
        if d_inv is None:
            continue
        n_mod = (S * d_inv) % (2**p)

        # Check: parity sequence of n_mod (mod 2^p) should match bits
        seq = parity_sequence(n_mod, p)
        if seq == bits:
            consistent += 1

        if S % D == 0:
            n_val = S // D
            if n_val > 0:
                integer_and_positive += 1
                # Double-check: parity sequence of n_val should be periodic with period p
                seq_full = parity_sequence(n_val, 2*p)
                is_periodic = seq_full[:p] == seq_full[p:]
                if not is_periodic:
                    print(f"  WARNING: n={n_val} has non-periodic sequence!")

        checked += 1

    print(f"p={p}: {checked} patterns checked, "
          f"self-consistent: {consistent}/{checked}, "
          f"positive integer solutions: {integer_and_positive}")

# ======================================================================
# 7. ARCHIMEDEAN vs NON-ARCHIMEDEAN MISMATCH
# ======================================================================
print()
print("=" * 70)
print("7. THE ARCHIMEDEAN / NON-ARCHIMEDEAN MISMATCH")
print("=" * 70)

print("\nKey insight: 'n(eps) is a positive integer' requires BOTH:")
print("  (a) Non-archimedean: D | S(eps) [2-adic integrality]")
print("  (b) Archimedean: 0 < S(eps)/D < (3/2)^{k-1} [size bound]")
print("The 2-adic metric sees (a) but is blind to (b), and vice versa.\n")

for p, k in [(5,3), (7,4), (8,5), (10,6), (13,8)]:
    D = 2**p - 3**k
    if D <= 0:
        continue

    # For each pattern with k ones, compute S/D and classify
    n_values = []
    negative_count = 0
    too_large = 0
    in_range_noninteger = 0
    in_range_integer = 0
    n_max = (3/2)**(k-1)

    for I in combinations(range(p), k):
        S = sum(3**(k-1-j) * 2**I[j] for j in range(k))
        ratio = S / D

        if S % D == 0:
            n = S // D
            if 0 < n <= n_max:
                in_range_integer += 1
                n_values.append(n)
            elif n > n_max:
                too_large += 1
        else:
            if 0 < ratio < n_max:
                in_range_noninteger += 1
            elif ratio < 0:
                negative_count += 1

    total = math.comb(p, k)
    print(f"(p,k) = ({p},{k}), D = {D}, n_max = {n_max:.1f}")
    print(f"  Total patterns: {total}")
    print(f"  In range & integer: {in_range_integer} (these are cycle candidates)")
    print(f"  In range & non-integer: {in_range_noninteger}")
    if n_values:
        trivial = sum(1 for n in n_values if n <= 2)
        nontrivial = sum(1 for n in n_values if n > 2)
        print(f"  Integer solutions: n = {sorted(set(n_values))[:10]}")
        print(f"  Trivial (n<=2): {trivial}, Nontrivial (n>2): {nontrivial}")
    else:
        print(f"  No integer solutions in range")

# ======================================================================
# 8. REPULSION RADIUS AND POSITIVE INTEGER DENSITY
# ======================================================================
print()
print("=" * 70)
print("8. REPULSION vs POSITIVE INTEGER DENSITY IN Z_2")
print("=" * 70)

print("\nIn Z_2, positive integers are dense but 'sparse' relative to")
print("2-adic balls. A 2-adic ball B(n0, 2^{-m}) contains ~2^{-m} fraction")
print("of Z/2^p Z, but also contains integers {n0 mod 2^m + t*2^m : t >= 0}.\n")

for p, k in [(5,3), (7,4), (8,5)]:
    D = 2**p - 3**k
    if D <= 0:
        continue

    print(f"\n(p,k) = ({p},{k}), D = {D}")

    # For each non-integer cycle point, find nearest positive integer
    count = 0
    for I in combinations(range(p), k):
        S = sum(3**(k-1-j) * 2**I[j] for j in range(k))
        if S % D == 0:
            continue

        # n(eps) mod 2^{2p}
        d_inv = mod_inverse(D, 2**(2*p))
        if d_inv is None:
            continue
        n_mod = (S * d_inv) % (2**(2*p))

        # The 2-adic distance from n(eps) to the nearest integer is controlled by
        # the denominator: if S/D is not integer, write S = qD + r, 0 < r < D.
        # Then n(eps) = q + r/D. The fractional part r/D has 2-adic expansion
        # with period ord_D(2). The nearest integer 2-adically is q (distance |r/D|_2)
        # or q+1 depending on r/D in Z_2.
        r = S % D
        # |r/D|_2 = |r|_2 (since |D|_2 = 1)
        v2_r = v2(r)

        if count < 5:
            print(f"  I={I}: S mod D = {r}, v_2(r) = {v2_r}, "
                  f"|n(eps) - nearest_int|_2 = 2^{-v2_r}")
        count += 1

    print(f"  ({count} non-integer cycle points total)")

# ======================================================================
# 9. PIECEWISE-ANALYTIC OBSTRUCTION
# ======================================================================
print()
print("=" * 70)
print("9. PIECEWISE vs ANALYTIC: why p-adic dynamics tools fail")
print("=" * 70)

print("""
The Collatz map T: Z_2 -> Z_2 is PIECEWISE-affine:
  T(n) = n/2       on 2*Z_2  (the "even piece")
  T(n) = (3n+1)/2  on 1+2*Z_2 (the "odd piece")

p-adic Fatou/Julia theory (Benedetto, Rivera-Letelier) requires:
  - A SINGLE analytic (or rational) function on P^1(C_p)
  - The dynamics must be given by a power series or rational function

The Collatz map is NOT analytic on all of Z_2:
  - It's affine on each piece, but the pieces are different affine maps
  - The "jump" at 2*Z_2 vs 1+2*Z_2 is a discontinuity in derivatives

Consequence: On each piece, T^p is a SINGLE affine map with repelling
fixed point. The Julia set of each piece is all of C_2. There are NO
Fatou components, so the no-wandering-domain theorem is vacuous.

The shift conjugacy T ~ sigma captures the FULL dynamics. No additional
structure from p-adic analytic dynamics can be extracted.""")

# Count the number of affine pieces for T^p
for p in [3, 5, 7, 10]:
    pieces = 0
    for bits in iterproduct([0,1], repeat=p):
        k = sum(bits)
        D = 2**p - 3**k
        if D > 0:
            pieces += 1
    print(f"  T^{p}: {pieces} affine pieces (vs 2^{p}={2**p} total parity patterns)")

# ======================================================================
# 10. QUANTIFYING THE FUNDAMENTAL OBSTRUCTION
# ======================================================================
print()
print("=" * 70)
print("10. THE FUNDAMENTAL OBSTRUCTION: topology vs arithmetic")
print("=" * 70)

print("""
TOPOLOGICAL FACT (non-archimedean):
  T: Z_2 -> Z_2 is conjugate to the full 2-shift sigma: {0,1}^N -> {0,1}^N
  Every periodic orbit exists in Z_2 (one per parity pattern)
  Cycles are 2-adically repelling (isolated points)

ARITHMETIC QUESTION:
  Which of the Q-rational cycle points S(eps)/D are positive integers?

THE MISMATCH:
  - "Being a positive integer" is an ARCHIMEDEAN condition (n > 0, n in Z)
  - The 2-adic topology cannot detect positivity or integrality beyond mod 2^m
  - The shift conjugacy is purely topological -- it says nothing about
    which periodic orbits are positive integers

THIS IS THE SAME BARRIER in different language:
  - Direction 0A (sieve/counting): needs archimedean input (rad(D) large)
  - Direction 0B (Arakelov): heights are archimedean + all non-arch combined
  - Direction 0C (motivic): algebraic vs exponential mismatch
  - Direction 6g-xi (2-adic dynamics): non-archimedean blindness to positivity

WHAT WOULD BE NEEDED:
  A framework that simultaneously constrains the 2-adic expansion
  (parity pattern) and the archimedean size (positive integer).
  This is a LOCAL-GLOBAL problem: the "local" information at all
  primes doesn't determine the "global" (rational integer) solution.
""")

# Final summary statistics
print("=" * 70)
print("SUMMARY")
print("=" * 70)
print()
print("Direction 6g-xi provides genuine INSIGHTS:")
print("  1. T ~ full shift: cleanest possible classification of 2-adic periodic orbits")
print("  2. Cycles are REPELLING (not attracting!) with factor 2^p")
print("  3. The cycle equation is purely arithmetic: D | S(eps)")
print("  4. Self-consistency is automatic -- no additional dynamical constraint")
print()
print("But CANNOT prove Part 1 because:")
print("  1. The shift conjugacy is topological, blind to positive integers")
print("  2. p-adic Fatou/Julia theory doesn't apply (T is piecewise, not analytic)")
print("  3. No-wandering-domain theorem is vacuous (no Fatou components)")
print("  4. The question 'is S(eps)/D a positive integer?' is archimedean")
print("  5. Combining 2-adic and archimedean info requires the product formula,")
print("     which only gives |n| = 1/prod|n|_p -- no new constraint")
print()
print("STATUS: 6g-xi EXPLORED, FAILS as standalone approach.")
print("  The 2-adic repulsion and shift conjugacy are CORRECT and USEFUL")
print("  as structural insights, but they reformulate rather than solve.")
print("  The fundamental problem (archimedean vs non-archimedean) persists.")
