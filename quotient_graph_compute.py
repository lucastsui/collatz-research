"""
Quotient-Graph Operator for the Affine Collatz Markov Chain.

For each prime p, the orbit O = r_0 * <2,3> decomposes into m = K/L cosets
of <3>, where K = |<2,3>| and L = ord_p(3). On each coset C_i, decompose
into L Fourier modes (characters of Z/LZ).

For each internal mode xi (indexed by k = 0, ..., L-1), the induced operator
on the quotient graph H/<3> is an m x m matrix Q_k. The eigenvalues of the
full K x K transfer matrix are the union of eigenvalues of Q_k for all k.

This script:
1. Computes the full K x K transfer matrix P and its eigenvalues.
2. Decomposes into internal modes and computes Q_k for each k.
3. Verifies that the eigenvalues of {Q_k} match those of P.
4. Studies the phase cocycle for non-trivial k.
"""

import numpy as np
from itertools import product as iterproduct


def ord_mod(a, p):
    """Compute multiplicative order of a mod p."""
    if a % p == 0:
        return 0
    val = a % p
    r = 1
    cur = val
    while cur != 1:
        cur = (cur * val) % p
        r += 1
        if r > p:
            return p  # shouldn't happen
    return r


def subgroup_23(p):
    """Compute H = <2,3> in (Z/pZ)* and return its elements as a sorted list."""
    H = set()
    # BFS/generate
    queue = [1]
    H.add(1)
    while queue:
        x = queue.pop(0)
        for g in [2, 3]:
            y = (x * g) % p
            if y not in H:
                H.add(y)
                queue.append(y)
    return sorted(H)


def build_transfer_matrix(p, orbit):
    """
    Build the K x K transfer matrix P for the Markov operator
    (Mf)(x) = (1/2) f(x * 2^{-1}) + (1/2) f((3x+1) * 2^{-1})
    acting on Fourier modes restricted to orbit O.

    In the Fourier coefficient basis {a_r : r in O}, the eigenvalue equation is:
        a_s + omega^s a_{3s} = 2 lambda a_{2s}

    So the transfer matrix maps:
        (Pa)_s = (1/2) a_{2s} + (1/2) omega^{s/3} a_{2s/3}

    Wait -- let's be more careful. M sends chi_r to:
        (1/2) chi_{r * alpha} + (1/2) omega^{r * gamma} chi_{r * beta}
    where alpha = 2^{-1} mod p, beta = 3 * 2^{-1} mod p, gamma = 2^{-1} mod p.

    In the a-basis, b_s = (Ma)_s gets contributions from modes r that map TO s:
        r * alpha = s  =>  r = 2s  =>  contribution (1/2) a_{2s}
        r * beta = s   =>  r = s * beta^{-1} = s * 2/3  =>  contribution (1/2) omega^{(2s/3) * gamma} a_{2s/3}
                        = (1/2) omega^{s/3} a_{2s/3}

    So: (Pa)_s = (1/2) a_{2s} + (1/2) omega^{s/3} a_{2s/3}

    But wait, 2s and 2s/3 need to be computed mod p.
    """
    K = len(orbit)
    omega = np.exp(2j * np.pi / p)

    # Create index mapping
    idx = {r: i for i, r in enumerate(orbit)}
    inv2 = pow(2, p - 2, p)  # 2^{-1} mod p
    inv3 = pow(3, p - 2, p)  # 3^{-1} mod p

    P = np.zeros((K, K), dtype=complex)

    for i, s in enumerate(orbit):
        # Branch T_0: multiply mode by alpha = 2^{-1}
        # The mode r = 2s contributes (1/2) a_{2s} to (Pa)_s
        r1 = (2 * s) % p
        if r1 in idx:
            P[i, idx[r1]] += 0.5

        # Branch T_1: multiply mode by beta = 3*2^{-1}, with phase
        # The mode r = 2s/3 contributes (1/2) omega^{r * gamma} a_r to (Pa)_s
        # where gamma = 2^{-1}, r = 2s/3
        # phase = omega^{(2s/3) * (1/2)} = omega^{s/3}
        # But s/3 means s * inv3 mod p
        r2 = (2 * s * inv3) % p
        phase = omega ** ((s * inv3) % p)
        if r2 in idx:
            P[i, idx[r2]] += 0.5 * phase

    return P


def decompose_cosets(p, orbit):
    """
    Decompose orbit O into <3>-cosets.
    Returns list of cosets, each coset is a list of elements in order
    [r, 3r, 9r, ..., 3^{L-1} r].
    """
    L = ord_mod(3, p)
    visited = set()
    cosets = []

    for r in orbit:
        if r in visited:
            continue
        coset = []
        x = r
        for _ in range(L):
            coset.append(x)
            visited.add(x)
            x = (x * 3) % p
        cosets.append(coset)

    return cosets, L


def build_quotient_operator(p, orbit, cosets, L, k):
    """
    Build the m x m quotient operator Q_k for internal mode k.

    The eigenvalue equation a_s + omega^s a_{3s} = 2 lambda a_{2s} can be
    rewritten in terms of the intra-coset Fourier modes.

    On coset C_i = {r_i, 3 r_i, ..., 3^{L-1} r_i}, define the Fourier modes:
        b_{i,k} = (1/sqrt(L)) sum_{j=0}^{L-1} omega_L^{-kj} a_{3^j r_i}
    where omega_L = e^{2 pi i / L}.

    The transfer matrix in the (i, k) basis: we need to express (Pa)_s in terms
    of the b_{i,k} coefficients.

    From (Pa)_s = (1/2) a_{2s} + (1/2) omega^{s/3} a_{2s/3}:

    For s = 3^j r_i (the j-th element of coset C_i):
        2s = 2 * 3^j * r_i. Now 2 * r_i belongs to some coset C_{sigma(i)}, say
        2 * r_i = 3^{tau_i} * r_{sigma(i)}. Then 2s = 3^{j + tau_i} * r_{sigma(i)}.

        2s/3 = 2 * 3^{j-1} * r_i = 3^{j-1+tau_i} * r_{sigma(i)}.

    So the action of P on coset position (i, j) maps to coset position (sigma(i), j + tau_i)
    for branch T_0, and to (sigma(i), j - 1 + tau_i) for branch T_1 (with phase).

    In the Fourier basis for the intra-coset modes, this becomes:
        (P b)_{sigma(i), k} = (1/2) omega_L^{k tau_i} b_{i,k}
                             + (1/2) omega_L^{k (tau_i - 1)} * phi_{i,k} * b_{i,k}

    Wait, the phase from the "+1" translation depends on which element we're at.
    Let me be more careful.
    """
    m = len(cosets)
    K = len(orbit)
    omega_p = np.exp(2j * np.pi / p)
    omega_L = np.exp(2j * np.pi / L)
    inv3 = pow(3, p - 2, p)

    # For each coset i, find sigma(i) and tau_i such that
    # 2 * r_i = 3^{tau_i} * r_{sigma(i)}
    # where r_i = cosets[i][0] is the coset representative.
    coset_rep = [c[0] for c in cosets]
    coset_idx = {}
    for i, c in enumerate(cosets):
        for j, elem in enumerate(c):
            coset_idx[elem] = (i, j)

    sigma = np.zeros(m, dtype=int)
    tau = np.zeros(m, dtype=int)

    for i in range(m):
        r_i = coset_rep[i]
        two_r_i = (2 * r_i) % p
        ci, cj = coset_idx[two_r_i]
        sigma[i] = ci
        tau[i] = cj

    # Now build Q_k.
    # The transfer matrix action: for s = 3^j r_i:
    #   (Pa)_{3^j r_i} = (1/2) a_{2 * 3^j r_i} + (1/2) omega^{3^{j-1} r_i} a_{2 * 3^{j-1} r_i}
    #                                                     (using s/3 = 3^{j-1} r_i for j>=1, or 3^{L-1} r_i for j=0)
    #
    # 2 * 3^j r_i = 3^{j + tau_i} r_{sigma(i)}   (in the target coset)
    # 2 * 3^{j-1} r_i = 3^{j-1+tau_i} r_{sigma(i)}
    #
    # So in terms of intra-coset indices within the target coset sigma(i):
    #   - The "a_{2s}" term at position j maps to position (j + tau_i) mod L in coset sigma(i)
    #   - The "a_{2s/3}" term at position j maps to position (j - 1 + tau_i) mod L in coset sigma(i)
    #   - The phase for the second term is omega^{3^{j-1} r_i / ... }
    #
    # Actually let me recompute. The phase in (Pa)_s = (1/2) a_{2s} + (1/2) omega^{s * inv3} a_{2s * inv3}
    # is omega^{s * inv3 mod p}.
    #
    # For s = 3^j r_i: s * inv3 = 3^{j-1} r_i (mod p), so the phase is omega_p^{3^{j-1} r_i}.
    # And 2s * inv3 = 2 * 3^{j-1} r_i = 3^{j-1+tau_i} r_{sigma(i)}.

    # Build the full transfer matrix in the (coset, intra-coset Fourier) basis.
    # For mode k, Q_k is m x m.
    #
    # In the intra-coset Fourier basis:
    #   b_{i,k} = (1/sqrt(L)) sum_{j=0}^{L-1} omega_L^{-kj} a_{3^j r_i}
    #
    # We need: (Pb)_{sigma(i), k} as a function of b_{i', k'} for various i', k'.
    #
    # From (Pa) at position (sigma(i), j+tau_i):
    #   (Pa)_{3^{j+tau_i} r_{sigma(i)}} = (1/2) a_{2 * 3^{j+tau_i} r_{sigma(i)}} + ...
    #
    # This is getting complicated. Let me just compute Q_k numerically by projecting.

    # Build the full transfer matrix P
    P = build_transfer_matrix(p, orbit)

    # Build the change-of-basis matrix from (a_r) to (b_{i,k})
    # b_{i,k} = (1/sqrt(L)) sum_{j=0}^{L-1} omega_L^{-kj} a_{cosets[i][j]}
    # So U[ik_flat, r_idx] = (1/sqrt(L)) omega_L^{-kj} where orbit[r_idx] = cosets[i][j]

    U = np.zeros((K, K), dtype=complex)
    for i in range(m):
        for kk in range(L):
            row = i * L + kk  # flattened (i, k) index
            for j in range(L):
                elem = cosets[i][j]
                col = orbit.index(elem)
                U[row, col] = (1.0 / np.sqrt(L)) * omega_L ** (-kk * j)

    # Transform P to the new basis: P_new = U P U^{-1}
    # Since U is unitary: P_new = U P U^H
    P_new = U @ P @ np.conj(U.T)

    # Extract the k-th block: rows and columns with internal mode k
    # In the flattened index, mode k corresponds to rows i*L + k for i = 0, ..., m-1
    indices_k = [i * L + k for i in range(m)]
    Q_k = P_new[np.ix_(indices_k, indices_k)]

    # Check: is Q_k approximately decoupled from other modes?
    # The off-diagonal blocks (coupling mode k to mode k') should be zero if
    # the decomposition is exact.
    coupling_norm = 0.0
    for kp in range(L):
        if kp == k:
            continue
        indices_kp = [i * L + kp for i in range(m)]
        block = P_new[np.ix_(indices_k, indices_kp)]
        coupling_norm += np.linalg.norm(block)

    return Q_k, coupling_norm, P, P_new, sigma, tau


def analyze_prime(p):
    """Full analysis of the quotient-graph operator for prime p."""
    H = subgroup_23(p)
    K = len(H)
    L = ord_mod(3, p)
    L2 = ord_mod(2, p)
    m = K // L

    print(f"\n{'='*60}")
    print(f"Prime p = {p}")
    print(f"  K = |<2,3>| = {K}, L = ord_p(3) = {L}, L_2 = ord_p(2) = {L2}, m = K/L = {m}")

    # Use orbit r_0 = 1 (or any representative)
    orbit = H  # orbit of 1 under <2,3>

    # Decompose into cosets
    cosets, L_check = decompose_cosets(p, orbit)
    assert L_check == L
    assert len(cosets) == m

    # Full transfer matrix eigenvalues
    P = build_transfer_matrix(p, orbit)
    evals_full = np.linalg.eigvals(P)
    evals_full_sorted = sorted(evals_full, key=lambda x: -abs(x))

    # Find the eigenvalue closest to 1 (stationary)
    lambda_1 = evals_full_sorted[0]
    lambda_2 = evals_full_sorted[1] if len(evals_full_sorted) > 1 else 0

    print(f"  |lambda_1| = {abs(lambda_1):.6f} (should be ~1)")
    print(f"  |lambda_2| = {abs(lambda_2):.6f}")
    print(f"  Spectral gap = {1 - abs(lambda_2):.6f}")

    # Quotient operators for each internal mode k
    all_Q_evals = []

    for k_mode in range(L):
        Q_k, coupling, _, P_new, sigma_perm, tau_perm = build_quotient_operator(
            p, orbit, cosets, L, k_mode
        )

        Q_evals = np.linalg.eigvals(Q_k)
        Q_evals_sorted = sorted(Q_evals, key=lambda x: -abs(x))
        all_Q_evals.extend(Q_evals)

        max_abs = abs(Q_evals_sorted[0])

        if k_mode <= 3 or k_mode == L - 1:
            print(f"\n  Internal mode k = {k_mode}:")
            print(f"    |Q_k coupling to other modes| = {coupling:.2e}")
            print(f"    max |eigenvalue of Q_k| = {max_abs:.6f}")
            print(f"    Q_k eigenvalues (magnitudes): {[f'{abs(e):.4f}' for e in Q_evals_sorted[:min(5,m)]]}")

            if k_mode == 0 and m > 0:
                print(f"    sigma permutation: {list(sigma_perm)}")
                print(f"    tau shifts: {list(tau_perm)}")

    # Verify: eigenvalues of all Q_k should match eigenvalues of P
    all_Q_evals_sorted = sorted(all_Q_evals, key=lambda x: -abs(x))

    print(f"\n  Verification:")
    print(f"    Full P eigenvalues (top 5 magnitudes): {[f'{abs(e):.6f}' for e in evals_full_sorted[:5]]}")
    print(f"    Union of Q_k eigenvalues (top 5): {[f'{abs(e):.6f}' for e in all_Q_evals_sorted[:5]]}")

    # Check match
    evals_P_mags = sorted([abs(e) for e in evals_full], reverse=True)
    evals_Q_mags = sorted([abs(e) for e in all_Q_evals], reverse=True)

    if len(evals_P_mags) == len(evals_Q_mags):
        max_diff = max(abs(a - b) for a, b in zip(evals_P_mags, evals_Q_mags))
        print(f"    Max magnitude difference: {max_diff:.2e}")
        match = max_diff < 1e-8
        print(f"    MATCH: {'YES' if match else 'NO'}")
    else:
        print(f"    Size mismatch: {len(evals_P_mags)} vs {len(evals_Q_mags)}")

    # Key analysis: spectral radius of Q_k for each k
    print(f"\n  Spectral radius by internal mode:")
    for k_mode in range(L):
        Q_k, coupling, _, _, _, _ = build_quotient_operator(
            p, orbit, cosets, L, k_mode
        )
        Q_evals = np.linalg.eigvals(Q_k)
        rho_k = max(abs(e) for e in Q_evals)
        cos_k = abs(np.cos(np.pi * k_mode / L))

        # For k != 0, we expect rho_k < 1 even without the cocycle
        # The "naive" bound is cos(pi*k/L) * 1 (from the intra-coset eigenvalue
        # times the spectral radius of the inter-coset permutation).
        print(f"    k={k_mode}: rho(Q_k) = {rho_k:.6f}, "
              f"cos(pi*k/L) = {cos_k:.6f}, "
              f"ratio = {rho_k/cos_k if cos_k > 1e-10 else float('inf'):.6f}, "
              f"coupling = {coupling:.2e}")

    return evals_full, all_Q_evals


def main():
    # Test primes
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    for p in primes:
        try:
            analyze_prime(p)
        except Exception as e:
            print(f"\nError for p={p}: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
