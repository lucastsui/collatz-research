#!/usr/bin/env python3
"""
Compute ||M^n||_op on the non-constant subspace for the affine Collatz walk.

Key question: Is ||M^2||_op < 1 uniformly in p?
If yes, this gives a universal constant spectral gap.

We project M onto the non-constant subspace (orthogonal to the all-ones vector)
and compute the operator norm of M^n restricted to that subspace.
"""

import numpy as np
from numpy.linalg import eigvals, svd, norm


def mod_inverse(a, p):
    return pow(a, p - 2, p)


def build_affine_markov_matrix(p):
    inv2 = mod_inverse(2, p)
    M = np.zeros((p, p))
    for x in range(p):
        y_even = (x * inv2) % p
        y_odd = ((3 * x + 1) * inv2) % p
        M[y_even][x] += 0.5
        M[y_odd][x] += 0.5
    return M


def project_to_nonconstant(M, p):
    """Project M onto the subspace orthogonal to the all-ones vector."""
    # Projection matrix: I - (1/p) * 1*1^T
    ones = np.ones((p, 1))
    P = np.eye(p) - (1.0 / p) * (ones @ ones.T)
    # Restricted operator: P M P (acts on non-constant subspace)
    return P @ M @ P


def operator_norm_on_nonconstant(M_proj):
    """Compute the operator norm (largest singular value) of the projected matrix."""
    s = svd(M_proj, compute_uv=False)
    # The largest singular value corresponds to eigenvalue 1 projected out,
    # so the second-largest is what we want. But since we projected,
    # the largest remaining singular value IS the operator norm on the subspace.
    # There will be one zero singular value (the projected-out direction).
    s_sorted = np.sort(s)[::-1]
    # Skip near-zero singular values from the projection
    return s_sorted[0]


def analyze_prime(p, max_n=4):
    M = build_affine_markov_matrix(p)
    M_proj = project_to_nonconstant(M, p)

    results = {}
    M_power = np.eye(p)
    for n in range(1, max_n + 1):
        M_power = M_power @ M
        M_power_proj = project_to_nonconstant(M_power, p)
        op_norm = operator_norm_on_nonconstant(M_power_proj)
        # The n-th root gives the effective per-step contraction
        per_step = op_norm ** (1.0 / n)
        results[n] = (op_norm, per_step)

    # Also compute actual eigenvalues for comparison
    eigs = eigvals(M)
    eigs_sorted = sorted(np.abs(eigs), reverse=True)
    lambda2 = eigs_sorted[1]  # second largest |eigenvalue|

    return results, lambda2


def main():
    from sympy import primerange

    primes = list(primerange(5, 500))

    print(f"{'p':>5} | {'|lam2|':>7} | {'||M||':>7} | {'||M^2||':>7} | {'||M^2||^(1/2)':>13} | {'||M^3||^(1/3)':>13} | {'||M^4||^(1/4)':>13}")
    print("-" * 90)

    worst_m2_norm = 0
    worst_m2_prime = 0

    for p in primes:
        results, lambda2 = analyze_prime(p, max_n=4)

        m1_norm = results[1][0]
        m2_norm = results[2][0]
        m2_root = results[2][1]
        m3_root = results[3][1]
        m4_root = results[4][1]

        if m2_norm > worst_m2_norm:
            worst_m2_norm = m2_norm
            worst_m2_prime = p

        print(f"{p:5d} | {lambda2:7.4f} | {m1_norm:7.4f} | {m2_norm:7.4f} | {m2_root:13.4f} | {m3_root:13.4f} | {m4_root:13.4f}")

    print()
    print(f"Worst ||M^2||_op = {worst_m2_norm:.6f} at p = {worst_m2_prime}")
    print(f"Worst ||M^2||_op^(1/2) = {worst_m2_norm**0.5:.6f}")
    print()

    # Summary statistics
    m2_norms = []
    for p in primes:
        results, _ = analyze_prime(p, max_n=2)
        m2_norms.append(results[2][0])

    m2_arr = np.array(m2_norms)
    print(f"||M^2||_op statistics:")
    print(f"  max  = {m2_arr.max():.6f}")
    print(f"  mean = {m2_arr.mean():.6f}")
    print(f"  min  = {m2_arr.min():.6f}")
    print(f"  All < 1? {np.all(m2_arr < 1.0)}")


if __name__ == "__main__":
    main()
