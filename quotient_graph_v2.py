"""
Quotient-Graph Operator v2: Correct decomposition.

The issue with v1: the intra-coset Fourier transform does NOT block-diagonalize
the transfer matrix because the "+1" phase (omega^{s/3}) depends on the
specific element s, not just the coset. Within coset C_i, the phase at
s = 3^j r_i is omega^{3^{j-1} r_i / p}, which varies with j. This
COUPLES different internal Fourier modes.

However, there IS a way to make the decomposition work: use the eigenbasis
of the "multiplication by 3 + phase" operator D_i S on each coset, rather
than the plain Fourier basis. Since the eigenvalues of D_i S are the L-th
roots of unity (the product of phases around the cycle is 1), the eigenvectors
are "twisted" Fourier modes.

The new approach:
1. On each coset C_i, find the eigenvectors of D_i S (the "twisted cyclic shift").
2. Express the transfer matrix in this basis.
3. Check whether the modes decouple.

Key insight: The operator M maps modes between cosets via ×2^{-1}. In the
eigenbasis of D_i S, the map from coset i to coset sigma(i) carries each
mode k to mode k (same eigenvalue), but with a PHASE COCYCLE from the
change-of-basis between the twisted eigenvectors of different cosets.
"""

import numpy as np


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
            return p
    return r


def subgroup_23(p):
    """Compute H = <2,3> in (Z/pZ)*."""
    H = set()
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


def decompose_cosets(p, orbit):
    """Decompose orbit into <3>-cosets."""
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


def build_transfer_matrix(p, orbit):
    """
    Build the K x K transfer matrix P for the Markov operator on orbit O.

    The operator is (Mf)(x) = (1/2) f(x/2) + (1/2) f((3x+1)/2).

    On Fourier modes: M(chi_r) = (1/2) chi_{r/2} + (1/2) omega^{r/2} chi_{3r/2}.

    In the a-basis where f = sum a_r chi_r:
    (Pa)_s = (1/2) a_{2s} + (1/2) omega^{s/3} a_{2s/3}

    Wait, let me rederive. M sends chi_r -> (1/2) chi_{r * 2^{-1}} + (1/2) omega^{r * 2^{-1}} chi_{r * 3 * 2^{-1}}.

    So if f = sum_r a_r chi_r, then Mf = sum_r a_r [(1/2) chi_{r/2} + (1/2) omega^{r/2} chi_{3r/2}].

    The coefficient of chi_s in Mf is:
    b_s = (1/2) a_{2s} + (1/2) omega^{s} * a_{2s/3}

    Wait, let me be very careful.
    chi_{r/2} has index r/2 = r * 2^{-1}.
    chi_{3r/2} has index 3r/2 = r * 3 * 2^{-1}.

    The coefficient of chi_s in Mf is:
    b_s = sum of (1/2) a_r for all r with r/2 = s (i.e., r = 2s)
        + sum of (1/2) omega^{r/2} a_r for all r with 3r/2 = s (i.e., r = 2s/3)

    So b_s = (1/2) a_{2s} + (1/2) omega^{(2s/3) * 2^{-1}} a_{2s/3}
           = (1/2) a_{2s} + (1/2) omega^{s/3} a_{2s/3}

    where 2^{-1}, 3^{-1} are modular inverses mod p, and omega = e^{2 pi i / p}.

    Actually: the phase is omega^{r/2} where r = 2s/3 (the mode that maps to s via the T_1 branch).
    So phase = omega^{(2s/3)/2} = omega^{s/3}.

    But r/2 = (2s/3)/2 = s/3. So the exponent is s/3 mod p, i.e., s * 3^{-1} mod p.

    Let me just use: b_s = (1/2) a_{2s} + (1/2) omega^{s * inv3} a_{2s * inv3}
    where inv3 = 3^{-1} mod p.
    """
    K = len(orbit)
    omega = np.exp(2j * np.pi / p)
    idx = {r: i for i, r in enumerate(orbit)}
    inv3 = pow(3, p - 2, p)

    P = np.zeros((K, K), dtype=complex)

    for i, s in enumerate(orbit):
        # T_0 branch: a_{2s} -> (Pa)_s with weight 1/2
        r1 = (2 * s) % p
        if r1 in idx:
            P[i, idx[r1]] += 0.5

        # T_1 branch: a_{2s/3} -> (Pa)_s with weight (1/2) omega^{s/3}
        s_over_3 = (s * inv3) % p
        r2 = (2 * s_over_3) % p
        phase = omega ** s_over_3
        if r2 in idx:
            P[i, idx[r2]] += 0.5 * phase

    return P


def build_DS_operator(p, coset, L):
    """
    Build the "twisted cyclic shift" D_i S on coset C_i.

    On coset C = {r, 3r, 9r, ..., 3^{L-1} r}, the operator D S acts as:
    (D S a)_{3^j r} = omega^{3^j r * ???} * a_{3^{j+1} r}

    Wait, what exactly is D S here? From the eigenvalue equation
    a_s + omega^s a_{3s} = 2 lambda a_{2s}, the "3-part" of the dynamics
    involves the term omega^s a_{3s}. The operator on the coset that
    captures the multiplication-by-3 with phase is:

    (Qa)_{3^j r} = omega^{3^j r} * a_{3^{j+1} r}

    This is a twisted cyclic shift with phases omega^{3^j r} at position j.
    """
    omega = np.exp(2j * np.pi / p)
    D_S = np.zeros((L, L), dtype=complex)

    for j in range(L):
        s = coset[j]
        # D_S maps position j+1 to position j with phase omega^s
        next_j = (j + 1) % L
        D_S[j, next_j] = omega ** s

    return D_S


def verify_DS_eigenvalues(p, cosets, L):
    """
    Verify that eigenvalues of D_i S on each coset are the L-th roots of unity.
    This requires the product of phases around the cycle to be 1.
    """
    omega = np.exp(2j * np.pi / p)

    for idx, coset in enumerate(cosets):
        DS = build_DS_operator(p, coset, L)
        evals = np.linalg.eigvals(DS)
        evals_sorted = sorted(evals, key=lambda x: np.angle(x))

        # Product of phases
        prod_phase = 1.0
        for j in range(L):
            prod_phase *= omega ** coset[j]

        # The eigenvalues should be L-th roots of (product of phases)
        # Check: product of phases = omega^{sum_{j=0}^{L-1} 3^j r}
        # = omega^{r * (3^L - 1) / (3 - 1)} = omega^{r * (3^L - 1) / 2}
        # Since 3^L = 1 mod p, (3^L - 1)/2 = 0 mod p. So product = 1.

        sum_phases = sum(coset[j] for j in range(L)) % p
        print(f"  Coset {idx}: rep={coset[0]}, "
              f"sum of elems mod p = {sum_phases}, "
              f"product of phases ~ omega^{sum_phases} = {abs(prod_phase):.6f} angle {np.angle(prod_phase):.6f}")

        # Check eigenvalue magnitudes
        mags = sorted([abs(e) for e in evals])
        print(f"    Eigenvalue magnitudes: {[f'{m:.6f}' for m in mags]}")


def analyze_with_twisted_basis(p):
    """
    Full analysis using the twisted eigenbasis on each coset.

    Strategy:
    1. On each coset C_i, compute eigenvectors of D_i S.
    2. Build the change-of-basis matrix U using these eigenvectors.
    3. Transform P to U P U^{-1}.
    4. Check if modes decouple.
    """
    H = subgroup_23(p)
    K = len(H)
    L = ord_mod(3, p)
    L2 = ord_mod(2, p)
    m = K // L
    orbit = H

    print(f"\n{'='*70}")
    print(f"Prime p = {p}, K = {K}, L = {L}, L_2 = {L2}, m = {m}")

    cosets, _ = decompose_cosets(p, orbit)

    # Build and verify D_i S
    # verify_DS_eigenvalues(p, cosets, L)

    # Build full transfer matrix
    P = build_transfer_matrix(p, orbit)
    evals_P = np.linalg.eigvals(P)
    evals_P_sorted = sorted(evals_P, key=lambda x: -abs(x))

    print(f"  Full transfer matrix eigenvalues (top 5):")
    for i, e in enumerate(evals_P_sorted[:5]):
        print(f"    lambda_{i+1} = {e:.6f}, |lambda| = {abs(e):.6f}")
    print(f"  Spectral gap = {1 - abs(evals_P_sorted[1]):.6f}")

    # Build twisted eigenbasis
    # On each coset, the eigenvectors of D_i S
    omega = np.exp(2j * np.pi / p)
    omega_L = np.exp(2j * np.pi / L)

    coset_elem_to_idx = {}
    for ci, coset in enumerate(cosets):
        for cj, elem in enumerate(coset):
            coset_elem_to_idx[elem] = (ci, cj)

    # For each coset, compute eigenvectors of D_i S
    eigvecs_per_coset = []
    eigvals_per_coset = []
    for ci in range(m):
        DS = build_DS_operator(p, cosets[ci], L)
        evals, evecs = np.linalg.eig(DS)

        # Sort by angle of eigenvalue
        order = np.argsort(np.angle(evals))
        evals = evals[order]
        evecs = evecs[:, order]

        eigvals_per_coset.append(evals)
        eigvecs_per_coset.append(evecs)

    # Build U: change of basis from orbit ordering to (coset, mode) ordering
    U = np.zeros((K, K), dtype=complex)
    for ci in range(m):
        evecs = eigvecs_per_coset[ci]
        for k in range(L):
            row = ci * L + k  # (coset ci, mode k)
            for j in range(L):
                elem = cosets[ci][j]
                col = orbit.index(elem)
                U[row, col] = np.conj(evecs[j, k])  # Use adjoint of eigenvector

    # Check U is unitary
    UUh = U @ np.conj(U.T)
    print(f"  ||U U^H - I|| = {np.linalg.norm(UUh - np.eye(K)):.2e}")

    # Transform P
    P_twisted = U @ P @ np.linalg.inv(U)

    # Check eigenvalues match
    evals_twisted = np.linalg.eigvals(P_twisted)
    evals_twisted_sorted = sorted(evals_twisted, key=lambda x: -abs(x))
    max_diff = max(abs(a - b) for a, b in zip(
        sorted([abs(e) for e in evals_P], reverse=True),
        sorted([abs(e) for e in evals_twisted], reverse=True)
    ))
    print(f"  Eigenvalue match after change of basis: max diff = {max_diff:.2e}")

    # Now examine the block structure of P_twisted
    # P_twisted should have blocks Q_{k,k'} of size m x m
    # where Q_{k,k'}[sigma(i), i] gives the coupling from mode k' on coset i
    # to mode k on coset sigma(i)

    print(f"\n  Block structure of P in twisted basis:")
    print(f"  (Block (k, k') is the m x m matrix coupling mode k' to mode k)")

    block_norms = np.zeros((L, L))
    for k1 in range(L):
        for k2 in range(L):
            rows = [ci * L + k1 for ci in range(m)]
            cols = [ci * L + k2 for ci in range(m)]
            block = P_twisted[np.ix_(rows, cols)]
            block_norms[k1, k2] = np.linalg.norm(block)

    # Print diagonal and off-diagonal block norms
    print(f"\n  Diagonal block norms (mode k -> mode k):")
    for k in range(min(L, 6)):
        print(f"    k={k}: ||Q_{{k,k}}|| = {block_norms[k,k]:.6f}")

    off_diag_max = 0
    for k1 in range(L):
        for k2 in range(L):
            if k1 != k2:
                off_diag_max = max(off_diag_max, block_norms[k1, k2])
    print(f"\n  Max off-diagonal block norm: {off_diag_max:.6f}")
    print(f"  Is block-diagonal? {'YES' if off_diag_max < 1e-10 else 'NO'}")

    if off_diag_max < 1e-10:
        print(f"\n  The twisted basis DOES block-diagonalize P!")
        print(f"  Spectral radii of diagonal blocks:")
        for k in range(L):
            rows = [ci * L + k for ci in range(m)]
            Qk = P_twisted[np.ix_(rows, rows)]
            evals_Qk = np.linalg.eigvals(Qk)
            rho_k = max(abs(e) for e in evals_Qk)
            print(f"    k={k}: rho(Q_k) = {rho_k:.6f}, "
                  f"(1/2)|1+omega_L^k| = {0.5 * abs(1 + omega_L**k):.6f}")
    else:
        # Even if not exactly block-diagonal, the off-diagonal coupling
        # might be small. Let's check the structure more carefully.
        print(f"\n  Modes are coupled. Examining which couplings are present...")

        # For each pair (k1, k2), show the coupling strength
        if L <= 8:
            print(f"\n  Block norm matrix:")
            for k1 in range(L):
                row_str = " ".join(f"{block_norms[k1,k2]:7.4f}" for k2 in range(L))
                print(f"    k={k1}: [{row_str}]")

    # Analyze the DIAGONAL blocks more carefully
    print(f"\n  Detailed analysis of diagonal blocks:")
    for k in range(min(L, 4)):
        rows = [ci * L + k for ci in range(m)]
        Qk = P_twisted[np.ix_(rows, rows)]
        evals_Qk = np.linalg.eigvals(Qk)
        rho_k = max(abs(e) for e in evals_Qk)

        # Expected: (1/2)(1 + omega_L^k) * (permutation with phases)
        expected_scale = 0.5 * abs(1 + omega_L**k)

        print(f"\n    Mode k = {k}:")
        print(f"      rho(Q_k) = {rho_k:.6f}")
        print(f"      (1/2)|1+omega_L^k| = {expected_scale:.6f}")
        if m <= 6:
            print(f"      Q_k matrix:")
            for row in range(m):
                row_str = " ".join(f"{Qk[row,col]:10.4f}" for col in range(m))
                print(f"        [{row_str}]")
            print(f"      Q_k eigenvalues: {[f'{e:.6f}' for e in sorted(evals_Qk, key=lambda x: -abs(x))]}")


def main():
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]

    for p in primes:
        try:
            analyze_with_twisted_basis(p)
        except Exception as e:
            print(f"\nError for p={p}: {e}")
            import traceback
            traceback.print_exc()


if __name__ == "__main__":
    main()
