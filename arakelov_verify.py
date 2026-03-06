"""
Verify key quantities from the Arakelov analysis on R = Z[x]/(x^p - 3^k).

Checks:
1. The near-degenerate embedding: |sigma_0(x-2)| = |3^{k/p} - 2| ~ D/(p*2^{p-1})
2. Product of non-degenerate embeddings ~ p * 2^{p-1}
3. sigma_0(Q_I) ~ n * p * 2^{p-1} (exponentially large)
4. The q-adic valuation v_q(x-2) = 0 at the prime above 3
5. Norm N(F_I) and divisibility by D
"""
import cmath
import math

def v2(n):
    if n == 0: return 999
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v

def cascade_positions(n, D, k, p):
    pw3 = [3**i for i in range(k)]
    rem = n * D - pw3[k-1]
    positions = [0]
    prev_h = 0
    for j in range(1, k):
        if rem <= 0: return None
        gap = v2(rem)
        h = prev_h + gap
        if h >= p: return None
        positions.append(h)
        rem = (rem >> gap) - pw3[k-1-j]
        prev_h = h
    if rem == 0:
        return positions
    return None

# Test pairs
test_pairs = [(5,3), (7,4), (8,5), (10,6), (13,8), (16,10)]

print("=" * 70)
print("ARAKELOV ANALYSIS VERIFICATION")
print("=" * 70)

for p, k in test_pairs:
    D = 2**p - 3**k
    if D <= 0: continue

    zeta = cmath.exp(2j * cmath.pi / p)
    alpha_0 = 3**(k/p)  # real embedding

    # 1. Near-degenerate embedding
    sigma0_xm2 = alpha_0 - 2
    predicted = -D / (p * 2**(p-1))

    # 2. Product of all |sigma_m(x-2)|
    prod_all = 1.0
    prod_nonzero = 1.0
    for m in range(p):
        val = abs(zeta**m * alpha_0 - 2)
        prod_all *= val
        if m != 0:
            prod_nonzero *= val

    print(f"\n(p,k) = ({p},{k}), D = {D}")
    print(f"  sigma_0(x-2) = {sigma0_xm2:.6e}")
    print(f"  predicted     = {predicted:.6e}")
    print(f"  ratio         = {sigma0_xm2/predicted:.4f}")
    print(f"  prod_all |sigma_m(x-2)| = {prod_all:.4f} (should be D={D})")
    print(f"  prod_{'{m!=0}'} |sigma_m(x-2)| = {prod_nonzero:.4f} (should be ~p*2^(p-1)={p*2**(p-1)})")

    # 3. Check N(F_I) for trivial cycle n=1 when p=2k
    if p == 2*k:
        I = list(range(0, 2*k, 2))  # positions 0,2,4,...,2(k-1)
    else:
        # Find any n that gives a valid cascade (just for testing)
        I = None
        for n in range(1, 20):
            if n % 2 == 0 or n % 3 == 0: continue
            pos = cascade_positions(n, D, k, p)
            if pos:
                I_positions = pos
                I = pos
                break

    if I is not None:
        # Compute F_I and its norm
        # F_I(x) = sum_{j=0}^{k-1} 3^{k-1-j} * x^{i_{j+1}}
        coeffs = [0] * p
        for j in range(k):
            coeffs[I[j]] += 3**(k-1-j)

        # Compute N(F_I) = prod_m F_I(zeta^m * alpha_0)
        norm_FI = 1.0
        embeddings = []
        for m in range(p):
            sigma_m = sum(coeffs[r] * (zeta**m * alpha_0)**r for r in range(p))
            embeddings.append(sigma_m)
            norm_FI *= abs(sigma_m)

        S_I = sum(3**(k-1-j) * 2**I[j] for j in range(k))
        n_val = S_I // D if D > 0 and S_I % D == 0 else -1

        print(f"  Positions I = {I}")
        print(f"  S(I) = {S_I}, n = S(I)/D = {n_val}, D|S(I): {S_I % D == 0}")
        print(f"  |N(F_I)| = {norm_FI:.4e}")
        if n_val > 0:
            print(f"  |N(F_I)|/D = {norm_FI/D:.4e} (should be integer)")

        # Height h_inf(F_I)
        h_inf = sum(math.log(abs(e)) for e in embeddings) / p
        print(f"  h_inf(F_I) = {h_inf:.4f}")

        # If divisible, compute Q_I height
        if S_I % D == 0:
            Q_embeddings = []
            for m in range(p):
                sigma_m_xm2 = zeta**m * alpha_0 - 2
                Q_m = embeddings[m] / sigma_m_xm2
                Q_embeddings.append(Q_m)

            h_inf_Q = sum(math.log(abs(q)) for q in Q_embeddings) / p
            print(f"  h_inf(Q_I) = {h_inf_Q:.4f} (should be ~log(2)={math.log(2):.4f})")
            print(f"  |sigma_0(Q_I)| = {abs(Q_embeddings[0]):.4e}")
            print(f"  predicted |sigma_0(Q)| ~ n*p*2^(p-1) = {n_val*p*2**(p-1):.4e}")

print()
print("=" * 70)
print("KEY FINDING: SLOPE ANALYSIS")
print("=" * 70)
print()

# For each (p,k), compute the anisotropy ratio of Q_I
for p, k in [(8,5), (10,6), (16,10)]:
    D = 2**p - 3**k
    if D <= 0 or p != 2*k: continue
    I = list(range(0, 2*k, 2))
    coeffs = [0] * p
    for j in range(k):
        coeffs[I[j]] += 3**(k-1-j)
    S_I = sum(3**(k-1-j) * 2**I[j] for j in range(k))
    if S_I % D != 0: continue
    n_val = S_I // D

    zeta = cmath.exp(2j * cmath.pi / p)
    alpha_0 = 3**(k/p)

    embeddings = []
    for m in range(p):
        sigma_m = sum(coeffs[r] * (zeta**m * alpha_0)**r for r in range(p))
        sigma_m_xm2 = zeta**m * alpha_0 - 2
        Q_m = sigma_m / sigma_m_xm2
        embeddings.append(abs(Q_m))

    max_emb = max(embeddings)
    min_emb = min(embeddings)
    print(f"(p,k) = ({p},{k}): Q_I anisotropy ratio = {max_emb/min_emb:.2e}")
    print(f"  max |sigma(Q)| = {max_emb:.4e} (at m=0)")
    print(f"  min |sigma(Q)| = {min_emb:.4e}")

print()
print("=" * 70)
print("q-ADIC VALUATIONS")
print("=" * 70)
print()

# Verify v_q(x-2) = 0 by checking that x-2 is a unit mod 3 in R/3R
for p, k in test_pairs:
    D = 2**p - 3**k
    if D <= 0: continue
    # In R/3R = F_3[x]/(x^p), the element x-2 = x-2 = x+1 (mod 3)
    # x+1 is a unit in F_3[x]/(x^p) iff gcd(x+1, x^p) = 1 in F_3[x]
    # Since x+1 and x are coprime, yes.
    # Inverse: (x+1)^{-1} = sum_{j=0}^{p-1} (-x)^j = sum (-1)^j x^j (geometric series, truncated since x^p=0)
    inv_coeffs = [(-1)**j % 3 for j in range(p)]
    # Check: (x+1) * inv = 1 mod (x^p, 3)
    prod = [0] * p
    for i in range(p):
        for j in range(p):
            if i + j < p:
                prod[i+j] = (prod[i+j] + ([1,1][i<=1 and i>=0] if i <= 1 else 0) * inv_coeffs[j]) % 3

    # Simpler: just note x+1 doesn't divide x^p in F_3[x]
    print(f"(p,k) = ({p},{k}): x-2 = x+1 mod 3. gcd(x+1, x^p) = 1 in F_3[x]. So v_q(x-2) = 0.")

print()
print("=" * 70)
print("CONCLUSION")
print("=" * 70)
print()
print("The near-degenerate embedding sigma_0 has |sigma_0(x-2)| ~ D/(p*2^{p-1}),")
print("exponentially small. This concentrates all norm mass at sigma_0 for Q_I.")
print("But the extreme anisotropy is automatic whenever D|S(I) holds.")
print("No height-based contradiction can be extracted: the lattice (x-2)R")
print("contains elements of all shapes, and membership is a linear condition.")
print("Direction 0B does not escape the barriers.")
