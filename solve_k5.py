#!/usr/bin/env python3
"""
Solve (or prove unsolvable) the k=5 Collatz cycle equation:

  2^{a_0} + 3*2^{a_1} + 9*2^{a_2} + 27*2^{a_3} + 81 = 5*(2^p - 243)

with constraints:
  p >= 8
  a_0 > a_1 > a_2 > a_3 >= 1
  a_0 <= p-1

Equivalently (moving 81 to RHS):
  2^{a_0} + 3*2^{a_1} + 9*2^{a_2} + 27*2^{a_3} = 5*2^p - 1296
"""

import sys

def exhaustive_search(p_max=60):
    """Exhaustive search for all valid p up to p_max."""
    print(f"=== Exhaustive Search for p in [8, {p_max}] ===\n")
    solutions = []

    for p in range(8, p_max + 1):
        RHS = 5 * (2**p) - 1296  # = 5*2^p - 1215 - 81 = 5*2^p - 1296

        if RHS <= 0:
            continue

        # a_3 >= 1, a_2 >= a_3+1 >= 2, a_1 >= a_2+1 >= 3, a_0 >= a_1+1 >= 4
        # a_0 <= p-1
        for a_0 in range(4, p):
            term_a0 = 2**a_0
            if term_a0 > RHS:
                break  # larger a_0 only makes it worse
            remainder1 = RHS - term_a0

            for a_1 in range(3, a_0):
                term_a1 = 3 * (2**a_1)
                if term_a1 > remainder1:
                    break
                remainder2 = remainder1 - term_a1

                for a_2 in range(2, a_1):
                    term_a2 = 9 * (2**a_2)
                    if term_a2 > remainder2:
                        break
                    remainder3 = remainder2 - term_a2

                    # Need: 27 * 2^{a_3} = remainder3
                    # So remainder3 must be divisible by 27
                    if remainder3 <= 0 or remainder3 % 27 != 0:
                        continue

                    val = remainder3 // 27
                    # val must be a power of 2
                    if val & (val - 1) != 0:
                        continue

                    a_3 = val.bit_length() - 1

                    # Check constraints: a_3 >= 1 and a_3 < a_2
                    if a_3 >= 1 and a_3 < a_2:
                        # Verify
                        LHS = 2**a_0 + 3*(2**a_1) + 9*(2**a_2) + 27*(2**a_3) + 81
                        target = 5 * (2**p - 243)
                        assert LHS == target, f"Verification failed: {LHS} != {target}"

                        solutions.append((p, a_0, a_1, a_2, a_3))
                        print(f"  SOLUTION FOUND: p={p}, (a_0,a_1,a_2,a_3) = ({a_0},{a_1},{a_2},{a_3})")

    if not solutions:
        print(f"  No solutions found for p in [8, {p_max}].\n")
    else:
        print(f"\n  Total solutions: {len(solutions)}\n")

    return solutions


def analytical_bounds():
    """Compute the threshold p_0 beyond which no solution can exist."""
    print("=== Analytical Bounds ===\n")

    # LHS = 2^{a_0} + 3*2^{a_1} + 9*2^{a_2} + 27*2^{a_3} + 81
    # Max LHS: a_0 = p-1, a_1 = p-2, a_2 = p-3, a_3 = p-4
    # Max LHS = 2^{p-1} + 3*2^{p-2} + 9*2^{p-3} + 27*2^{p-4} + 81
    #         = 2^{p-1} + 3*2^{p-2} + 9*2^{p-3} + 27*2^{p-4} + 81
    #         = 2^p * (1/2 + 3/4 + 9/8 + 27/16) + 81
    #         = 2^p * (8/16 + 12/16 + 18/16 + 27/16) + 81
    #         = 2^p * (65/16) + 81

    coeff = 65/16  # = 4.0625
    print(f"  Max LHS coefficient: {coeff} (i.e., max LHS ~ {coeff} * 2^p + 81)")
    print(f"  RHS = 5 * 2^p - 1215")
    print()

    # For no solution: max LHS < RHS
    # 65/16 * 2^p + 81 < 5 * 2^p - 1215
    # 81 + 1215 < (5 - 65/16) * 2^p
    # 1296 < (80/16 - 65/16) * 2^p
    # 1296 < (15/16) * 2^p
    # 2^p > 1296 * 16/15 = 1382.4
    # p > log2(1382.4) ≈ 10.43
    # So p >= 11 guarantees max LHS < RHS... wait that can't be right.
    # Let me reconsider. We need max LHS >= RHS for a solution to possibly exist.

    # Actually, let me recheck. RHS = 5*2^p - 1215. For large p, RHS ~ 5*2^p.
    # Max LHS ~ (65/16)*2^p. Since 65/16 = 4.0625 < 5, for large p, max LHS < RHS.
    # The threshold: (65/16)*2^p + 81 >= 5*2^p - 1215
    # 81 + 1215 >= (5 - 65/16)*2^p
    # 1296 >= (15/16)*2^p
    # 2^p <= 1296 * 16/15 = 1382.4
    # p <= log2(1382.4) ≈ 10.43
    # So p <= 10.

    import math
    threshold = 1296 * 16 / 15
    p_threshold = math.log2(threshold)
    print(f"  Threshold: 2^p <= {threshold:.1f}")
    print(f"  p <= log2({threshold:.1f}) = {p_threshold:.4f}")
    print(f"  So for p >= 11, max LHS < RHS, and no solution can exist.")
    print(f"  We only need to check p in [8, 10].\n")

    # Verify for specific p values
    print("  Verification of max LHS vs RHS:")
    for p in range(8, 15):
        max_lhs = 2**(p-1) + 3*2**(p-2) + 9*2**(p-3) + 27*2**(p-4) + 81
        rhs = 5 * 2**p - 1215
        gap = rhs - max_lhs
        status = "POSSIBLE" if max_lhs >= rhs else "IMPOSSIBLE"
        print(f"    p={p:2d}: max_LHS = {max_lhs:8d}, RHS = {rhs:8d}, gap = {gap:8d}  [{status}]")

    print()

    # Also check: minimum LHS
    # Min LHS: a_0=4, a_1=3, a_2=2, a_3=1
    # Min LHS = 2^4 + 3*2^3 + 9*2^2 + 27*2^1 + 81 = 16+24+36+54+81 = 211
    min_lhs = 2**4 + 3*2**3 + 9*2**2 + 27*2**1 + 81
    print(f"  Min LHS (a_0=4,a_1=3,a_2=2,a_3=1) = {min_lhs}")
    for p in range(8, 12):
        rhs = 5 * 2**p - 1215
        print(f"    p={p}: RHS = {rhs}, min_LHS {'<=' if min_lhs <= rhs else '>'} RHS: {'ok' if min_lhs <= rhs else 'min too big'}")

    print()
    return 10  # max p to check


def modular_analysis():
    """Modular constraints to further restrict possibilities."""
    print("=== Modular Analysis ===\n")

    # Original equation:
    # 2^{a_0} + 3*2^{a_1} + 9*2^{a_2} + 27*2^{a_3} + 81 = 5*2^p - 1215
    # Equivalently:
    # 2^{a_0} + 3*2^{a_1} + 9*2^{a_2} + 27*2^{a_3} = 5*2^p - 1296

    print("--- Mod 3 ---")
    # LHS mod 3: 2^{a_0} + 0 + 0 + 0 = 2^{a_0} mod 3
    # RHS mod 3: 5*2^p - 1296 mod 3. 1296 = 432*3 = 0 mod 3. 5 = 2 mod 3.
    # So RHS = 2*2^p = 2^{p+1} mod 3.
    # Need: 2^{a_0} ≡ 2^{p+1} (mod 3)
    # Since ord(2,3)=2: need a_0 ≡ p+1 (mod 2)
    print("  2^{a_0} ≡ 2^{p+1} (mod 3)")
    print("  => a_0 ≡ p+1 (mod 2)")
    print("  => a_0 and p+1 have the same parity")
    print("  => a_0 and p have different parity\n")

    print("--- Mod 5 ---")
    # LHS mod 5: 2^{a_0} + 3*2^{a_1} + 4*2^{a_2} + 2*2^{a_3} mod 5
    # (since 9 = 4 mod 5, 27 = 2 mod 5)
    # RHS mod 5: 5*2^p - 1296 mod 5 = -1296 mod 5 = -1296 mod 5
    # 1296 / 5 = 259*5 + 1, so 1296 ≡ 1 (mod 5), so RHS ≡ -1 ≡ 4 (mod 5)
    print("  LHS mod 5: 2^{a_0} + 3*2^{a_1} + 4*2^{a_2} + 2*2^{a_3} (mod 5)")
    print("  RHS mod 5: 5*2^p - 1296 ≡ -1296 ≡ -1 ≡ 4 (mod 5)")
    print("  (since 1296 = 259*5 + 1)")
    print("  Need: 2^{a_0} + 3*2^{a_1} + 4*2^{a_2} + 2*2^{a_3} ≡ 4 (mod 5)\n")

    # ord(2,5) = 4: 2^0=1, 2^1=2, 2^2=4, 2^3=3, 2^4=1, ...
    print("  Powers of 2 mod 5: 2^0≡1, 2^1≡2, 2^2≡4, 2^3≡3, cycle length 4")

    # Check all valid (a_0, a_1, a_2, a_3) mod 4 combinations for p=8,9,10
    print()
    print("--- Mod 8 ---")
    # LHS mod 8: For a_3 >= 1, a_2 >= 2, a_1 >= 3:
    # 27*2^{a_3}: if a_3 >= 1, this is divisible by 2. If a_3 >= 3, div by 8.
    # 9*2^{a_2}: if a_2 >= 2, this is 9*4=36≡4 mod 8 (if a_2=2), or 0 mod 8 if a_2>=3
    # 3*2^{a_1}: if a_1 >= 3, this is 3*8=24≡0 mod 8, or higher
    # 2^{a_0}: if a_0 >= 3, this is 0 mod 8
    # RHS mod 8: 5*2^p - 1296. For p >= 3: 5*2^p ≡ 0 mod 8. 1296 mod 8 = 1296 - 162*8 = 1296-1296=0.
    # So RHS ≡ 0 mod 8.
    print("  1296 mod 8 = 0 (since 1296 = 162*8)")
    print("  For p >= 3: 5*2^p ≡ 0 (mod 8)")
    print("  So RHS ≡ 0 (mod 8)\n")

    # LHS mod 8 analysis for small a values
    print("  LHS mod 8 depends on small exponent values:")
    print("  a_3=1: 27*2=54≡6 mod 8; a_3=2: 27*4=108≡4 mod 8; a_3>=3: 0 mod 8")
    print("  a_2=2: 9*4=36≡4 mod 8; a_2>=3: 0 mod 8")
    print("  a_1=3: 3*8=24≡0 mod 8; a_1>=3: always 0 mod 8")
    print("  a_0>=3: always 0 mod 8 (and a_0>=4 required)")
    print()

    # So LHS mod 8 = (contribution from a_3 if a_3 <= 2) + (contribution from a_2 if a_2=2)
    # Need LHS ≡ 0 mod 8
    # Case a_3=1, a_2=2: 6+4=10≡2 mod 8. Not 0. -> eliminated!
    # Case a_3=1, a_2>=3: 6+0=6 mod 8. Not 0. -> eliminated!
    # Case a_3=2, a_2>=3: 4+0=4 mod 8. Not 0. -> eliminated!
    # Case a_3>=3, a_2>=3 (so a_2>=4, a_3>=3, a_3<a_2 so a_3=3,a_2>=4): 0+0=0 mod 8. OK.
    # Wait, but a_2 must be at least a_3+1. If a_3>=3, then a_2>=4.

    print("  Mod 8 constraint (LHS ≡ 0 mod 8):")
    print("  a_3=1, a_2=2: 54+36 ≡ 6+4 = 10 ≡ 2 (mod 8) -> ELIMINATED")
    print("  a_3=1, a_2>=3: 54+0 ≡ 6 (mod 8) -> ELIMINATED")
    print("  a_3=2, a_2>=3: 108+0 ≡ 4 (mod 8) -> ELIMINATED")
    print("  a_3>=3, a_2>=4: 0+0 ≡ 0 (mod 8) -> OK")
    print()
    print("  CONCLUSION: Must have a_3 >= 3 and a_2 >= 4.")
    print("  This forces: a_3 >= 3, a_2 >= 4, a_1 >= 5, a_0 >= 6.\n")

    # Now recheck with these tighter constraints
    print("  With a_0 >= 6, a_1 >= 5, a_2 >= 4, a_3 >= 3:")
    print("  Min LHS = 2^6 + 3*2^5 + 9*2^4 + 27*2^3 + 81")
    min_lhs_new = 2**6 + 3*2**5 + 9*2**4 + 27*2**3 + 81
    print(f"          = 64 + 96 + 144 + 216 + 81 = {min_lhs_new}")
    print()

    for p in range(8, 12):
        rhs_full = 5 * (2**p - 243)
        print(f"    p={p}: RHS = {rhs_full}, min_LHS = {min_lhs_new}: {'feasible' if min_lhs_new <= rhs_full else 'infeasible'}")

    print()

    # Now mod 16
    print("--- Mod 16 ---")
    # Need to check LHS mod 16 with a_3 >= 3.
    # a_3=3: 27*8=216≡8 mod 16; a_3>=4: 0 mod 16
    # a_2=4: 9*16=144≡0 mod 16; a_2>=4: 0 mod 16
    # So if a_3=3: LHS ≡ 8 mod 16 (from 27*2^3 term)
    # Rest is 0 mod 16 since a_0>=6, a_1>=5, a_2>=4 all give terms div by 16.
    # RHS mod 16: 5*2^p - 1296. 1296 mod 16: 1296/16=81, so 1296 = 81*16, 1296 mod 16 = 0.
    # 5*2^p mod 16: for p>=4, 5*2^p ≡ 0 mod 16.
    # So RHS ≡ 0 mod 16.
    # If a_3=3: LHS ≡ 8 mod 16 ≠ 0 -> eliminated!
    # So a_3 >= 4.
    print("  1296 mod 16 = 0")
    print("  For p >= 4: 5*2^p ≡ 0 (mod 16), so RHS ≡ 0 (mod 16)")
    print("  If a_3=3: 27*2^3 = 216 ≡ 8 (mod 16), rest is 0 mod 16 -> LHS ≡ 8 (mod 16) -> ELIMINATED")
    print("  So a_3 >= 4, hence a_2 >= 5, a_1 >= 6, a_0 >= 7.\n")

    # Mod 32
    print("--- Mod 32 ---")
    # a_3=4: 27*16=432. 432 mod 32 = 432 - 13*32 = 432-416 = 16. So ≡ 16 mod 32.
    # a_3>=5: 27*2^a_3 with a_3>=5: 27*32=864≡0 mod 32? 864/32=27, so yes, 864≡0 mod 32.
    # Rest: a_0>=7, a_1>=6, a_2>=5 -> all terms divisible by 32.
    # Wait: a_2>=5: 9*2^5=288. 288 mod 32 = 288-9*32=288-288=0. OK.
    # a_1>=6: 3*2^6=192. 192 mod 32 = 192-6*32=192-192=0. OK.
    # a_0>=7: 2^7=128≡0 mod 32. OK.
    # RHS mod 32: 5*2^p - 1296. 1296 mod 32: 1296-40*32=1296-1280=16. So 1296≡16 mod 32.
    # For p>=5: 5*2^p ≡ 0 mod 32. So RHS ≡ -16 ≡ 16 mod 32.
    # If a_3=4: LHS ≡ 16 mod 32. RHS ≡ 16 mod 32. OK!
    # If a_3>=5: LHS ≡ 0 mod 32. RHS ≡ 16 mod 32. Not equal -> ELIMINATED!
    # So a_3 = 4 exactly (for p >= 5, which is always true since p >= 8).
    print("  1296 mod 32 = 16")
    print("  For p >= 5: 5*2^p ≡ 0 (mod 32), so RHS ≡ -16 ≡ 16 (mod 32)")
    print("  a_3=4: 27*16 = 432 ≡ 16 (mod 32), rest ≡ 0 (mod 32) -> LHS ≡ 16 (mod 32) -> MATCHES")
    print("  a_3>=5: 27*2^{a_3} ≡ 0 (mod 32), rest ≡ 0 (mod 32) -> LHS ≡ 0 (mod 32) -> ELIMINATED")
    print("  CONCLUSION: a_3 = 4 exactly.\n")

    # With a_3=4 fixed, update constraints:
    # a_2 >= 5, a_1 >= 6, a_0 >= 7, a_0 <= p-1
    print("  With a_3 = 4 fixed: a_2 >= 5, a_1 >= 6, a_0 >= 7, a_0 <= p-1\n")

    # Mod 64
    print("--- Mod 64 ---")
    # a_3=4 is fixed: 27*16=432. 432 mod 64: 432-6*64=432-384=48. So ≡ 48 mod 64.
    # a_2=5: 9*32=288. 288 mod 64: 288-4*64=288-256=32. So ≡ 32 mod 64.
    # a_2>=6: 9*2^a_2 with a_2>=6: 9*64=576≡0 mod 64.
    # a_1>=6: 3*2^6=192≡0 mod 64. (192-3*64=192-192=0)
    # a_0>=7: 2^7=128≡0 mod 64.
    # RHS mod 64: 5*2^p - 1296. 1296 mod 64: 1296-20*64=1296-1280=16. So 1296≡16 mod 64.
    # For p>=6: 5*2^p ≡ 0 mod 64. So RHS ≡ -16 ≡ 48 mod 64.
    # If a_2=5: LHS ≡ 48+32+0+0 = 80 ≡ 16 mod 64. RHS ≡ 48 mod 64. 16≠48 -> ELIMINATED.
    # If a_2>=6: LHS ≡ 48+0+0+0 = 48 mod 64. RHS ≡ 48 mod 64. MATCHES.
    # So a_2 >= 6.
    print("  1296 mod 64 = 16 (1296 = 20*64 + 16)")
    print("  For p >= 6: 5*2^p ≡ 0 (mod 64), so RHS ≡ -16 ≡ 48 (mod 64)")
    print("  a_3=4: 27*16 = 432 ≡ 48 (mod 64)")
    print("  a_2=5: 9*32 = 288 ≡ 32 (mod 64) -> LHS ≡ 48+32 = 80 ≡ 16 (mod 64) -> ELIMINATED")
    print("  a_2>=6: 9*2^{a_2} ≡ 0 (mod 64) -> LHS ≡ 48 (mod 64) -> MATCHES")
    print("  CONCLUSION: a_2 >= 6.\n")

    # With a_3=4, a_2>=6: a_1>=7, a_0>=8, a_0<=p-1, so p>=9.
    print("  Updated: a_3=4, a_2>=6, a_1>=7, a_0>=8, p>=9\n")

    # Mod 128
    print("--- Mod 128 ---")
    # a_3=4: 432 mod 128: 432-3*128=432-384=48. So ≡ 48 mod 128.
    # a_2=6: 9*64=576 mod 128: 576-4*128=576-512=64. So ≡ 64 mod 128.
    # a_2>=7: 9*2^a_2 ≡ 0 mod 128 (since 9*128=1152, div by 128).
    # a_1=7: 3*128=384 mod 128: 384-3*128=0. So ≡ 0 mod 128.
    # a_1>=7: always 0 mod 128.
    # a_0>=8: 2^8=256≡0 mod 128.
    # RHS mod 128: 1296 mod 128: 1296-10*128=1296-1280=16. So 1296≡16 mod 128.
    # For p>=7: 5*2^p ≡ 0 mod 128. RHS ≡ -16 ≡ 112 mod 128.
    # If a_2=6: LHS ≡ 48+64 = 112 mod 128. MATCHES!
    # If a_2>=7: LHS ≡ 48 mod 128. 48≠112 -> ELIMINATED.
    # So a_2 = 6 exactly.
    print("  1296 mod 128 = 16")
    print("  For p >= 7: 5*2^p ≡ 0 (mod 128), so RHS ≡ -16 ≡ 112 (mod 128)")
    print("  a_3=4: 432 ≡ 48 (mod 128)")
    print("  a_2=6: 9*64 = 576 ≡ 64 (mod 128) -> LHS ≡ 48+64 = 112 (mod 128) -> MATCHES")
    print("  a_2>=7: 0 (mod 128) -> LHS ≡ 48 (mod 128) ≠ 112 -> ELIMINATED")
    print("  CONCLUSION: a_2 = 6 exactly.\n")

    # With a_3=4, a_2=6, a_1>=7, a_0>=8, p>=9
    print("  Updated: a_3=4, a_2=6, a_1>=7, a_0>=8, p>=9\n")

    # Now the equation becomes:
    # 2^{a_0} + 3*2^{a_1} + 9*64 + 27*16 + 81 = 5*2^p - 1215
    # 2^{a_0} + 3*2^{a_1} + 576 + 432 + 81 = 5*2^p - 1215
    # 2^{a_0} + 3*2^{a_1} + 1089 = 5*2^p - 1215
    # 2^{a_0} + 3*2^{a_1} = 5*2^p - 2304
    val_fixed = 576 + 432 + 81  # = 1089
    print(f"  Fixed terms: 9*2^6 + 27*2^4 + 81 = {576} + {432} + {81} = {val_fixed}")
    print(f"  Reduced equation: 2^{{a_0}} + 3*2^{{a_1}} = 5*2^p - 1215 - {val_fixed}")
    print(f"                   = 5*2^p - {1215 + val_fixed}")
    reduced_const = 1215 + val_fixed
    print(f"                   = 5*2^p - {reduced_const}")
    print()

    # Mod 256
    print("--- Mod 256 ---")
    # Now we need: 2^{a_0} + 3*2^{a_1} = 5*2^p - 2304
    # 2304 mod 256: 2304/256 = 9, so 2304 ≡ 0 mod 256.
    # For p >= 8: 5*2^p ≡ 0 mod 256 (since 2^8=256). So RHS ≡ 0 mod 256.
    # a_1=7: 3*128=384 ≡ 128 mod 256.
    # a_1=8: 3*256=768 ≡ 0 mod 256.
    # a_0=8: 256 ≡ 0 mod 256.
    # a_0>=8: always 0 mod 256.
    # If a_1=7: LHS ≡ 0 + 128 = 128 mod 256. RHS ≡ 0 mod 256. 128≠0 -> ELIMINATED.
    # If a_1>=8: LHS ≡ 0 mod 256. MATCHES.
    # So a_1 >= 8.
    print("  Reduced: 2^{a_0} + 3*2^{a_1} = 5*2^p - 2304")
    print("  2304 mod 256 = 0")
    print("  For p >= 8: RHS ≡ 0 (mod 256)")
    print("  a_1=7: 3*128 = 384 ≡ 128 (mod 256) -> ELIMINATED")
    print("  a_1>=8: 3*2^{a_1} ≡ 0 (mod 256) -> MATCHES")
    print("  CONCLUSION: a_1 >= 8. Hence a_0 >= 9, p >= 10.\n")

    # Mod 512
    print("--- Mod 512 ---")
    # 2304 mod 512: 2304 = 4*512 + 256, so 2304 ≡ 256 mod 512.
    # For p >= 9: 5*2^p ≡ 0 mod 512. RHS ≡ -256 ≡ 256 mod 512.
    # a_1=8: 3*256=768. 768 mod 512 = 256.
    # a_1>=9: 3*512=1536≡0 mod 512.
    # a_0=9: 512≡0 mod 512.
    # a_0>=9: 0 mod 512.
    # If a_1=8: LHS ≡ 0+256=256 mod 512 = RHS. MATCHES!
    # If a_1>=9: LHS ≡ 0 mod 512 ≠ 256. ELIMINATED!
    # So a_1 = 8.
    print("  2304 mod 512 = 256")
    print("  For p >= 9: RHS ≡ -256 ≡ 256 (mod 512)")
    print("  a_1=8: 3*256 = 768 ≡ 256 (mod 512) -> LHS ≡ 0+256 = 256 -> MATCHES")
    print("  a_1>=9: 3*2^{a_1} ≡ 0 (mod 512) -> LHS ≡ 0 ≠ 256 -> ELIMINATED")
    print("  CONCLUSION: a_1 = 8 exactly.\n")

    # Now: a_3=4, a_2=6, a_1=8, a_0>=9, p>=10
    # Equation: 2^{a_0} + 3*256 = 5*2^p - 2304
    # 2^{a_0} + 768 = 5*2^p - 2304
    # 2^{a_0} = 5*2^p - 3072
    print("  Updated: a_3=4, a_2=6, a_1=8, a_0>=9, p>=10")
    print("  Equation: 2^{a_0} + 768 = 5*2^p - 2304")
    print("  2^{a_0} = 5*2^p - 3072\n")

    # 3072 = 3*1024 = 3*2^10
    # 5*2^p - 3*2^10 = 2^{a_0}
    # For this to be a power of 2, we need 5*2^p - 3*2^10 > 0 and a power of 2.
    print("  3072 = 3 * 2^10")
    print("  So: 2^{a_0} = 5 * 2^p - 3 * 2^10")
    print()

    # If p >= 11: factor out 2^10:
    # 2^{a_0} = 2^10 * (5*2^{p-10} - 3)
    # So a_0 >= 10, and 2^{a_0-10} = 5*2^{p-10} - 3.
    # For the RHS to be a power of 2:
    # 5*2^{p-10} - 3 = 2^m where m = a_0 - 10.
    # For p=10: 5*1 - 3 = 2 = 2^1. So m=1, a_0=11. But a_0 <= p-1 = 9. CONTRADICTION.
    # For p=11: 5*2 - 3 = 7. Not a power of 2. ELIMINATED.
    # For p=12: 5*4 - 3 = 17. Not a power of 2. ELIMINATED.
    # For p=10: Direct: 2^{a_0} = 5*1024 - 3072 = 5120-3072 = 2048 = 2^11. a_0=11. But a_0 <= 9. IMPOSSIBLE.

    # If p = 10: 2^{a_0} = 5*1024 - 3072 = 5120 - 3072 = 2048 = 2^11. a_0=11. But need a_0 <= p-1=9. FAIL.

    print("  Check each p:")
    for p in range(9, 25):
        val = 5 * (2**p) - 3072
        if val <= 0:
            print(f"    p={p:2d}: 5*2^{p} - 3072 = {val} <= 0 -> IMPOSSIBLE")
            continue
        # Check if power of 2
        is_pow2 = (val & (val-1)) == 0
        if is_pow2:
            a_0 = val.bit_length() - 1
            valid = a_0 <= p - 1 and a_0 >= 9
            print(f"    p={p:2d}: 5*2^{p} - 3072 = {val} = 2^{a_0} {'VALID' if valid else 'INVALID (a_0=' + str(a_0) + ' but need a_0<=' + str(p-1) + ')'}")
        else:
            print(f"    p={p:2d}: 5*2^{p} - 3072 = {val} -> not a power of 2")

    print()

    # General argument: for p >= 11
    # 5*2^p - 3072 = 2^10*(5*2^{p-10} - 3)
    # Need 5*2^{p-10} - 3 = 2^m for some m >= 0
    # 5*2^{p-10} = 2^m + 3
    # For m=0: 5*2^{p-10}=4 -> 2^{p-10}=4/5. Not integer.
    # For m=1: 5*2^{p-10}=5 -> 2^{p-10}=1 -> p=10. Already checked.
    # For m >= 2: RHS = 2^m + 3 is odd+odd = even+odd... wait.
    # 2^m + 3: for m >= 2, 2^m is divisible by 4, so 2^m + 3 ≡ 3 mod 4.
    # But LHS = 5*2^{p-10}. For p >= 12 (p-10 >= 2): LHS ≡ 0 mod 4. But RHS ≡ 3 mod 4. CONTRADICTION!
    # For p = 11 (p-10=1): LHS = 5*2=10. RHS = 2^m+3. 2^m=7, not a power of 2.
    # For p = 10 (p-10=0): LHS = 5*1=5. RHS = 2^m+3. 2^m=2, m=1. a_0=10+1=11. But a_0<=9. FAIL.

    print("  === General proof for p >= 12 ===")
    print("  For p >= 11: 2^{a_0} = 2^10 * (5*2^{p-10} - 3)")
    print("  Need: 5*2^{p-10} - 3 = 2^m (m = a_0 - 10)")
    print("  For p >= 12 (p-10 >= 2): LHS = 5*2^{p-10} ≡ 0 (mod 4)")
    print("  But 2^m + 3 for m >= 2: ≡ 0+3 = 3 (mod 4). And 5*2^{p-10} ≡ 0 (mod 4).")
    print("  So 2^m + 3 ≡ 0 (mod 4) is impossible since 2^m+3 ≡ 3 (mod 4) for m>=2.")
    print("  For m = 1: 2^m + 3 = 5, so 5*2^{p-10} = 5, p=10. But we assumed p>=12. Contradiction.")
    print("  For m = 0: 2^m + 3 = 4, so 5*2^{p-10} = 4. Not possible (LHS div by 5).")
    print("  Therefore NO SOLUTION for p >= 12.\n")

    print("  For p=11: 5*2^1 - 3 = 7, not a power of 2. NO SOLUTION.")
    print("  For p=10: 5*2^0 - 3 = 2, so a_0=10+1=11. But a_0 <= p-1 = 9. NO SOLUTION.")
    print("  For p=9: 5*512 - 3072 = 2560 - 3072 = -512 < 0. NO SOLUTION.")
    print("  For p=8: 5*256 - 3072 = 1280 - 3072 = -1792 < 0. NO SOLUTION.")
    print()
    print("  ============================================")
    print("  THEOREM: The k=5 equation has NO SOLUTIONS.")
    print("  ============================================\n")


def verify_modular_chain():
    """Double-check all modular conclusions with brute force for small p."""
    print("=== Verification: Brute-force check against modular conclusions ===\n")

    # Check for ALL p from 8 to 40 with the original constraints
    for p in range(8, 41):
        RHS_full = 5 * (2**p - 243)
        if RHS_full <= 0:
            continue

        for a_0 in range(4, p):
            for a_1 in range(3, a_0):
                for a_2 in range(2, a_1):
                    for a_3 in range(1, a_2):
                        LHS = 2**a_0 + 3*(2**a_1) + 9*(2**a_2) + 27*(2**a_3) + 81
                        if LHS == RHS_full:
                            print(f"  SOLUTION: p={p}, a=({a_0},{a_1},{a_2},{a_3})")
                            return True

    print("  Confirmed: No solutions exist for p in [8, 40].")
    print("  (This covers the analytically-relevant range since max LHS < RHS for p >= 11.)\n")
    return False


def main():
    print("=" * 70)
    print("  ANALYSIS OF k=5 COLLATZ CYCLE EQUATION")
    print("  2^{a_0} + 3*2^{a_1} + 9*2^{a_2} + 27*2^{a_3} + 81 = 5*(2^p - 243)")
    print("=" * 70)
    print()

    # Part 1: Exhaustive search
    solutions = exhaustive_search(p_max=40)

    # Part 2: Analytical bounds
    p_max_analytical = analytical_bounds()

    # Part 3: Modular analysis
    modular_analysis()

    # Part 4: Verification
    verify_modular_chain()

    print("=" * 70)
    print("  FINAL CONCLUSION")
    print("=" * 70)
    print()
    print("  The k=5, n=5 Collatz cycle equation has NO solutions.")
    print()
    print("  Proof outline:")
    print("  1. Size bound: max LHS < RHS for p >= 11, so only p in {8,9,10} possible.")
    print("  2. Modular chain (mod 8,16,32,64,128,256,512) forces:")
    print("     a_3 = 4, a_2 = 6, a_1 = 8, leaving 2^{a_0} = 5*2^p - 3072.")
    print("  3. For p >= 12: 5*2^p - 3072 = 2^10*(5*2^{p-10}-3).")
    print("     5*2^{p-10} ≡ 0 (mod 4) but 2^m+3 ≡ 3 (mod 4) for m>=2. Contradiction.")
    print("  4. For p=11: 5*2-3=7, not a power of 2.")
    print("  5. For p<=10: 5*2^p - 3072 <= 0 or a_0 > p-1 (violates constraint).")
    print("  6. Exhaustive search for p in [8,40] confirms: zero solutions found.")
    print()


if __name__ == "__main__":
    main()
