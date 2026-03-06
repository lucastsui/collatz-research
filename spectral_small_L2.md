# Spectral Data for Primes with Small ord_p(2)

## Key Finding

**The spectral gap is NOT proportional to 1/p, even for the smallest L₂ values.** The gap is Ω(1) for all tested primes.

gap × p for primes with L₂ ≤ 10:
| p | L₂ | gap | gap×p |
|---|---|---|---|
| 7 | 3 | 0.286 | 2.00 |
| 5 | 4 | 0.191 | 0.95 |
| 31 | 5 | 0.275 | 8.54 |
| 127 | 7 | 0.312 | 39.6 |
| 17 | 8 | 0.300 | 5.10 |
| 73 | 9 | 0.244 | 17.8 |
| 11 | 10 | 0.331 | 3.64 |

If gap ∝ 1/p, gap×p would be constant. Instead it GROWS with p.

## Worst |λ₂| by L₂

| L₂ | # primes | worst |λ₂| | at p= | best |λ₂| | at p= |
|---|---|---|---|---|---|
| 3 | 1 | 0.714 | 7 | 0.714 | 7 |
| 4 | 1 | 0.809 | 5 | 0.809 | 5 |
| 5 | 1 | 0.725 | 31 | 0.725 | 31 |
| 7 | 1 | 0.688 | 127 | 0.688 | 127 |
| 8 | 1 | 0.700 | 17 | 0.700 | 17 |
| 9 | 1 | 0.756 | 73 | 0.756 | 73 |
| 10 | 1 | 0.669 | 11 | 0.669 | 11 |
| 11 | 2 | 0.728 | 23 | 0.682 | 89 |
| 12 | 1 | 0.669 | 13 | 0.669 | 13 |
| 43 | 1 | 0.767 | 431 | 0.767 | 431 |

**Global maximum: |λ₂| = 0.809 at p = 5 (L₂ = 4).**

## Crucial Observation

For FIXED L₂, the number of primes is FINITE (bounded by ω(2^{L₂} - 1) ≤ L₂). So:

**For L₂ ≤ N₀:** finitely many primes, each with |λ₂| < 1 computed directly → constant gap by finite verification.

**For L₂ > N₀:** need theoretical bound (Theorem 16 or CDG approach).

This suggests the universal gap might be provable by combining:
1. Direct computation for L₂ ≤ N₀ (finite check)
2. Theorem 16 for primes with |⟨2,3⟩| ≥ p^{1/2+ε}
3. A theoretical bound for the remaining "gap" primes
