#!/usr/bin/env python3
"""
Spectral gap computation for the Collatz Markov chain mod p.

For each prime p, the Collatz map T(x) = x/2 if x even, (3x+1)/2 if x odd
induces a Markov chain on Z/pZ (excluding 0). The transition matrix M has:
  M[T_even(x), x] = 1/2  (the "even" branch: x -> x * 2^{-1} mod p)
  M[T_odd(x), x]  = 1/2  (the "odd" branch: x -> (3x+1) * 2^{-1} mod p)

Actually, let's be more careful. The Collatz-like map on Z/pZ*:
  With probability 1/2: x -> x/2 mod p  (multiply by inverse of 2)
  With probability 1/2: x -> (3x+1)/2 mod p

This gives a (p-1) x (p-1) transition matrix on the nonzero residues.

We compute:
- L2 = ord_p(2)
- L  = ord_p(3)
- K  = |<2,3>| in (Z/pZ)*
- |lambda_2| = second largest eigenvalue magnitude
- CDG product = prod_{j=0}^{L2-1} |cos(pi * 2^j / p)|
"""

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigs
from sympy import isprime, primitive_root
import sys
import json
import time

def multiplicative_order(a, p):
    """Compute ord_p(a), the multiplicative order of a mod p."""
    if a % p == 0:
        return 0
    r = 1
    power = a % p
    while power != 1:
        power = (power * a) % p
        r += 1
        if r > p:
            return p - 1  # fallback
    return r

def subgroup_size(p):
    """Compute |<2,3>| in (Z/pZ)*."""
    # Generate elements by multiplying by 2 and 3
    seen = {1}
    frontier = {1}
    while frontier:
        new = set()
        for x in frontier:
            for g in [2, 3]:
                y = (x * g) % p
                if y not in seen:
                    seen.add(y)
                    new.add(y)
        frontier = new
    return len(seen)

def build_collatz_matrix_dense(p):
    """Build the Collatz Markov transition matrix on {1, ..., p-1}.

    States are indexed 0..p-2 corresponding to residues 1..p-1.
    """
    n = p - 1
    inv2 = pow(2, p - 2, p)  # 2^{-1} mod p

    M = np.zeros((n, n), dtype=np.float64)

    for x_idx in range(n):
        x = x_idx + 1  # residue

        # Branch 1: x -> x/2 mod p
        y1 = (x * inv2) % p
        y1_idx = y1 - 1

        # Branch 2: x -> (3x+1)/2 mod p
        y2 = ((3 * x + 1) * inv2) % p
        if y2 == 0:
            # (3x+1)/2 = 0 mod p means 3x+1 = 0 mod p, i.e. x = (p-1)/3 mod p
            # This maps to 0 which is outside our state space.
            # In this case we can handle it by wrapping: treat as absorbing or skip.
            # Actually for x = (p-1)*inv3 mod p, (3x+1) = 0 mod p.
            # We'll redistribute this probability. Let's just give full weight to branch 1.
            M[y1_idx, x_idx] += 1.0
            continue
        y2_idx = y2 - 1

        M[y1_idx, x_idx] += 0.5
        M[y2_idx, x_idx] += 0.5

    return M

def build_collatz_matrix_sparse(p):
    """Build sparse Collatz Markov transition matrix."""
    n = p - 1
    inv2 = pow(2, p - 2, p)

    rows = []
    cols = []
    vals = []

    for x_idx in range(n):
        x = x_idx + 1

        y1 = (x * inv2) % p
        y1_idx = y1 - 1

        y2 = ((3 * x + 1) * inv2) % p

        if y2 == 0:
            rows.append(y1_idx)
            cols.append(x_idx)
            vals.append(1.0)
            continue

        y2_idx = y2 - 1

        rows.append(y1_idx)
        cols.append(x_idx)
        vals.append(0.5)

        rows.append(y2_idx)
        cols.append(x_idx)
        vals.append(0.5)

    M = sparse.csr_matrix((vals, (rows, cols)), shape=(n, n))
    return M

def compute_eigenvalues_dense(p):
    """Compute all eigenvalues for small p."""
    M = build_collatz_matrix_dense(p)
    eigenvalues = np.linalg.eigvals(M)
    mags = np.abs(eigenvalues)
    mags_sorted = np.sort(mags)[::-1]
    # Largest should be ~1 (stationary distribution)
    lambda2 = mags_sorted[1] if len(mags_sorted) > 1 else 0
    return lambda2

def compute_eigenvalues_sparse(p, k=6):
    """Compute top-k eigenvalues for larger p using sparse solver."""
    M = build_collatz_matrix_sparse(p)
    try:
        # Get largest magnitude eigenvalues
        eigenvalues = eigs(M, k=min(k, p - 3), which='LM', return_eigenvectors=False)
        mags = np.abs(eigenvalues)
        mags_sorted = np.sort(mags)[::-1]
        lambda2 = mags_sorted[1] if len(mags_sorted) > 1 else 0
        return lambda2
    except Exception as e:
        print(f"  Sparse solver failed for p={p}: {e}", file=sys.stderr)
        return None

def cdg_product(p, L2):
    """Compute prod_{j=0}^{L2-1} |cos(pi * 2^j / p)|."""
    product = 1.0
    power = 1
    for j in range(L2):
        product *= abs(np.cos(np.pi * power / p))
        power = (power * 2) % p
    return product

def orbit_cos_sin_averages(p, L2):
    """Compute average cos^2 and sin^2 over the <2>-orbit of 1 in Z/pZ."""
    power = 1
    cos2_sum = 0.0
    sin2_sum = 0.0
    for j in range(L2):
        angle = 2 * np.pi * power / p
        cos2_sum += np.cos(angle) ** 2
        sin2_sum += np.sin(angle) ** 2
        power = (power * 2) % p
    return cos2_sum / L2, sin2_sum / L2

def main():
    primes = [p for p in range(5, 5001) if isprime(p)]
    print(f"Total primes in range: {len(primes)}", file=sys.stderr)

    results = []

    for i, p in enumerate(primes):
        L2 = multiplicative_order(2, p)
        L = multiplicative_order(3, p)
        K = subgroup_size(p)
        index = (p - 1) // K

        # Decide computation method
        lambda2 = None
        if p <= 1000:
            lambda2 = compute_eigenvalues_dense(p)
        elif L2 <= 30:
            # Use sparse for primes with small L2
            lambda2 = compute_eigenvalues_sparse(p, k=10)

        gap = (1 - lambda2) if lambda2 is not None else None

        # CDG quantities
        cdg = cdg_product(p, L2)
        avg_cos2, avg_sin2 = orbit_cos_sin_averages(p, L2)

        result = {
            'p': p,
            'L2': L2,
            'L': L,
            'K': K,
            'index': index,
            'lambda2': lambda2,
            'gap': gap,
            'cdg_product': cdg,
            'two_neg_L2': 2**(-L2),
            'avg_cos2': avg_cos2,
            'avg_sin2': avg_sin2,
        }
        results.append(result)

        if (i + 1) % 50 == 0:
            print(f"  Processed {i+1}/{len(primes)} primes...", file=sys.stderr)

    # Sort by L2
    results.sort(key=lambda r: (r['L2'], r['p']))

    # Output as JSON for further processing
    print(json.dumps(results))

if __name__ == '__main__':
    main()
