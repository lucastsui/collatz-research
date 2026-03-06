"""
Computational verification for Direction 0C: Motivic/Categorical analysis.

Checks:
1. Newton polygon geometry and BKK mixed volumes
2. Norm N(F_I) factorization when D | S(I) (trivial cycle cases)
3. Tropical valuations v_2(S(I)) and v_3(S(I))
4. Partition function Z(s; p, k) = sum |S(I)|^{-s}
5. Configuration space statistics
"""

import cmath
import math
from itertools import combinations

def v2(n):
    if n == 0: return 999
    v = 0
    while n % 2 == 0: n //= 2; v += 1
    return v

def v3(n):
    if n == 0: return 999
    v = 0
    while n % 3 == 0: n //= 3; v += 1
    return v

# ======================================================================
# 1. Newton Polygon and BKK Mixed Volume
# ======================================================================
print("=" * 70)
print("1. NEWTON POLYGONS AND BKK MIXED VOLUMES")
print("=" * 70)

def newton_polygon(points):
    """Compute convex hull of 2D points (simple gift-wrapping)."""
    from functools import cmp_to_key
    pts = sorted(set(points))
    if len(pts) <= 2:
        return pts
    # Andrew's monotone chain
    def cross(O, A, B):
        return (A[0]-O[0])*(B[1]-O[1]) - (A[1]-O[1])*(B[0]-O[0])
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def polygon_area(hull):
    """Area of convex polygon via shoelace formula."""
    n = len(hull)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    return abs(area) / 2.0

def minkowski_sum(P, Q):
    """Minkowski sum of two convex polygons (or segments)."""
    result = []
    for p in P:
        for q in Q:
            result.append((p[0]+q[0], p[1]+q[1]))
    return newton_polygon(result)

def mixed_volume_2d(P, Q):
    """MV(P,Q) = Vol(P+Q) - Vol(P) - Vol(Q)."""
    PQ = minkowski_sum(P, Q)
    return polygon_area(PQ) - polygon_area(P) - polygon_area(Q)

test_pairs = [(5,3), (7,4), (8,5), (10,6)]

for p, k in test_pairs:
    D = 2**p - 3**k
    if D <= 0:
        continue

    # Newton polygon of G(u,v) = u^p - v^k
    newt_G = [(p, 0), (0, k)]

    # For F_I: use trivial cycle positions if p=2k, else compact positions
    if p == 2*k:
        positions = list(range(0, 2*k, 2))
    else:
        positions = list(range(k))  # compact: 0,1,...,k-1

    # Newton polygon of F_I
    newt_F = [(positions[j], k-1-j) for j in range(k)]
    hull_F = newton_polygon(newt_F)

    mv = mixed_volume_2d(newt_G, hull_F)

    # Width of F perpendicular to G
    # Direction of G: (-k, p). Perp direction: (p, k)
    norm_perp = math.sqrt(p**2 + k**2)
    projections = [(p*positions[j] + k*(k-1-j))/norm_perp for j in range(k)]
    width = max(projections) - min(projections)

    print(f"\n(p,k) = ({p},{k}), D = {D}")
    print(f"  Newt(G) = segment {newt_G}")
    print(f"  Newt(F_I) vertices: {hull_F[:min(6,len(hull_F))]}{'...' if len(hull_F)>6 else ''}")
    print(f"  Area(Newt(F_I)) = {polygon_area(hull_F):.1f}")
    print(f"  BKK mixed volume MV(Newt(G), Newt(F_I)) = {mv:.1f}")
    print(f"  Width of F_I perp to G = {width:.2f}")
    print(f"  BKK bound on common zeros in (C*)^2: {int(round(mv))}")

# ======================================================================
# 2. Norm N(F_I) and Factorization
# ======================================================================
print()
print("=" * 70)
print("2. NORM N(F_I) AND FACTORIZATION")
print("=" * 70)

for p, k in test_pairs:
    D = 2**p - 3**k
    if D <= 0:
        continue

    zeta = cmath.exp(2j * cmath.pi / p)
    alpha_0 = 3**(k/p)

    # Positions for trivial cycle
    if p == 2*k:
        positions = list(range(0, 2*k, 2))
    else:
        positions = list(range(k))

    # Coefficients of F_I(x)
    coeffs = [0] * p
    for j in range(k):
        coeffs[positions[j]] = 3**(k-1-j)

    # Compute N(F_I) = prod_m F_I(zeta^m * alpha_0)
    norm_FI = 1.0
    for m in range(p):
        val = sum(coeffs[r] * (zeta**m * alpha_0)**r for r in range(p))
        norm_FI *= abs(val)

    # S(I)
    S_I = sum(3**(k-1-j) * 2**positions[j] for j in range(k))

    print(f"\n(p,k) = ({p},{k}), D = {D}")
    print(f"  Positions = {positions}")
    print(f"  S(I) = {S_I}, D|S(I): {S_I % D == 0}")
    print(f"  |N(F_I)| = {norm_FI:.4e}")
    print(f"  |N(F_I)|/D = {norm_FI/D:.4e}")
    if S_I % D == 0:
        n = S_I // D
        print(f"  n = S(I)/D = {n}")
        print(f"  N(Q_I) = N(F_I)/D = {norm_FI/D:.4e}")

# ======================================================================
# 3. Tropical Valuations
# ======================================================================
print()
print("=" * 70)
print("3. TROPICAL VALUATIONS")
print("=" * 70)

for p, k in [(5,3), (7,4), (8,5), (10,6), (13,8)]:
    D = 2**p - 3**k
    if D <= 0:
        continue
    print(f"\n(p,k) = ({p},{k}), D = {D}")

    # Check a few subsets
    count = 0
    v2_correct = 0
    v3_correct = 0
    checked = 0
    for I in combinations(range(p), k):
        S = sum(3**(k-1-j) * 2**I[j] for j in range(k))
        pred_v2 = I[0]  # tropical prediction
        pred_v3 = 0      # tropical prediction
        if v2(S) == pred_v2:
            v2_correct += 1
        if v3(S) == pred_v3:
            v3_correct += 1
        checked += 1
        if checked >= 500:
            break

    print(f"  Checked {checked} subsets")
    print(f"  v_2(S) = i_1 (tropical): {v2_correct}/{checked} correct ({100*v2_correct/checked:.1f}%)")
    print(f"  v_3(S) = 0 (tropical):   {v3_correct}/{checked} correct ({100*v3_correct/checked:.1f}%)")

# ======================================================================
# 4. Partition Function Z(s; p, k)
# ======================================================================
print()
print("=" * 70)
print("4. PARTITION FUNCTION Z(s; p, k)")
print("=" * 70)

for p, k in [(5,3), (7,4), (8,5)]:
    D = 2**p - 3**k
    if D <= 0:
        continue

    # Compute all S(I) values
    S_vals = []
    for I in combinations(range(p), k):
        S = sum(3**(k-1-j) * 2**I[j] for j in range(k))
        S_vals.append(S)

    total = len(S_vals)
    S_min = min(S_vals)
    S_max = max(S_vals)
    S_mean = sum(S_vals) / total

    print(f"\n(p,k) = ({p},{k}), D = {D}, C(p,k) = {total}")
    print(f"  S range: [{S_min}, {S_max}]")
    print(f"  S mean:  {S_mean:.1f}, D = {D}")
    print(f"  S/D range: [{S_min/D:.2f}, {S_max/D:.2f}]")

    # Z(s) for various s
    for s in [0.0, 0.5, 1.0, 2.0]:
        if s == 0:
            Z_s = total
        else:
            Z_s = sum(v**(-s) for v in S_vals)
        print(f"  Z({s:.1f}) = {Z_s:.6f}")

    # Pressure P(s) = (1/p) log Z(s)
    print(f"  Pressure P(0) = {math.log(total)/p:.4f} (entropy/p)")
    Z1 = sum(1.0/v for v in S_vals)
    print(f"  Pressure P(1) = {math.log(Z1)/p:.4f}")
    print(f"  Expected count Z(1)*D = sum D/S(I) = {Z1*D:.4f}")

    # Check functional equation: Z(s) vs Z(1-s) * something
    Z_half = sum(v**(-0.5) for v in S_vals)
    Z_neg_half = sum(v**(0.5) for v in S_vals)
    ratio = Z_half / Z_neg_half if Z_neg_half != 0 else float('inf')
    print(f"  Z(0.5)/Z(-0.5) = {ratio:.6e} (no functional eq. if this isn't const)")

# ======================================================================
# 5. Configuration Space: Residue Distribution
# ======================================================================
print()
print("=" * 70)
print("5. RESIDUE DISTRIBUTION S(I) mod D")
print("=" * 70)

for p, k in [(5,3), (7,4), (8,5)]:
    D = 2**p - 3**k
    if D <= 0:
        continue

    residues = {}
    total = 0
    for I in combinations(range(p), k):
        S = sum(3**(k-1-j) * 2**I[j] for j in range(k))
        r = S % D
        residues[r] = residues.get(r, 0) + 1
        total += 1

    missing = [r for r in range(D) if r not in residues]
    hit_zero = 0 in residues

    print(f"\n(p,k) = ({p},{k}), D = {D}, total subsets = {total}")
    print(f"  Distinct residues hit: {len(residues)}/{D}")
    print(f"  Missing residues: {missing if len(missing) <= 10 else f'{len(missing)} residues'}")
    print(f"  0 in residues: {hit_zero}")
    if not hit_zero:
        # Nearest to 0
        min_r = min(r for r in residues)
        max_r = max(r for r in residues)
        nearest = min(min_r, D - max_r)
        print(f"  Nearest residue to 0: {nearest}")

    # Uniformity: chi-squared test
    expected = total / D
    chi2 = sum((residues.get(r, 0) - expected)**2 / expected for r in range(D))
    print(f"  Chi-squared (uniformity): {chi2:.2f} (df={D-1}, expect ~{D-1})")

# ======================================================================
# 6. The Exponential-Algebraic Divide: Quantification
# ======================================================================
print()
print("=" * 70)
print("6. EXPONENTIAL-ALGEBRAIC DIVIDE")
print("=" * 70)

print("\nThe condition D|S(I) is about divisibility of an EXPONENTIAL sum")
print("by an EXPONENTIAL modulus. Quantifying the gap between existing tools:")
print()

for p, k in [(10,6), (16,10), (21,13)]:
    D = 2**p - 3**k
    if D <= 0:
        continue

    # Baker-type bound: |p log 2 - k log 3| > exp(-C sqrt(p) log p)
    linear_form = abs(p * math.log(2) - k * math.log(3))
    baker_lower = math.exp(-10 * math.sqrt(p) * math.log(p))  # rough Baker bound

    # abc prediction: rad(D) > D^{1-epsilon}
    # Stewart bound: log rad(D) > C sqrt(p) / log p
    stewart_bound = math.sqrt(p) / math.log(p)

    # What we need: log rad(D) > 0.95 p log 2
    needed = 0.95 * p * math.log(2)

    print(f"(p,k) = ({p},{k}), D = {D}")
    print(f"  |p log 2 - k log 3| = {linear_form:.6e}")
    print(f"  Baker lower bound:     {baker_lower:.6e}")
    print(f"  Stewart: log rad(D) >  {stewart_bound:.2f}")
    print(f"  Need: log rad(D) >     {needed:.2f}")
    print(f"  Gap factor:            {needed/stewart_bound:.1f}x")
    print()

# ======================================================================
# 7. Pila-Wilkie: Dimension and Height Check
# ======================================================================
print("=" * 70)
print("7. PILA-WILKIE APPLICABILITY CHECK")
print("=" * 70)
print()

for p, k in [(10,6), (16,10)]:
    D = 2**p - 3**k
    if D <= 0:
        continue

    # The definable set X in R^{k+1} has dimension k
    # Height of integer solutions: H = max(i_j) <= p-1
    # Pila-Wilkie: #X(Z) cap [0,H]^k <= C_eps * H^eps for transcendental part
    # But H = p-1 and the algebraic part could contain all solutions

    print(f"(p,k) = ({p},{k})")
    print(f"  Dimension of definable set X: {k}")
    print(f"  Height bound H = {p-1}")
    print(f"  Pila-Wilkie gives: #{'{X(Z)}'} <= C_eps * {p-1}^eps")
    print(f"  Need: #{'{X(Z)}'} = 0")
    print(f"  Issue: eps-bound is O(1) for small p, and C_eps depends on k={k}")
    print(f"  Evertse-Schlickewei: at most C(k)=2^(2^(2^k)) solutions for FIXED k")
    print(f"  For k={k}: C(k) ~ 2^(2^(2^{k})) -- astronomically large")
    print()

print("=" * 70)
print("CONCLUSION")
print("=" * 70)
print()
print("Direction 0C fails at the foundational level:")
print("  1. No algebraic variety encodes the Collatz cycle set")
print("     (the constraint 2^{i_j} is exponential, not polynomial)")
print("  2. No zeta function exists (no natural varying parameter)")
print("  3. No cohomology theory handles exponential-algebraic hybrids")
print("  4. Toric/tropical methods lose the fine arithmetic (D-divisibility)")
print("  5. O-minimal methods (Pila-Wilkie) are too weak for growing dimension")
print()
print("ROOT CAUSE: The Collatz condition lives at the intersection of the")
print("exponential world (2^{i_j}, 3^{k-j}) and the algebraic world")
print("(divisibility by D = 2^p - 3^k). No existing mathematical framework")
print("handles this intersection.")
