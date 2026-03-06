"""
Quotient-Graph Operator v3: Understanding the cocycle structure.

Key realization from v2: The "+1" phases COUPLE different internal modes.
The transfer matrix in ANY per-coset basis has off-diagonal inter-mode blocks.

New approach: Instead of trying to block-diagonalize, study the STRUCTURE
of the coupling. The transfer matrix maps:

(Pa)_s = (1/2) a_{2s} + (1/2) omega^{s * inv3} a_{2s * inv3}

For s = 3^j r_i (element j of coset C_i):
- 2s = 2 * 3^j r_i lies in coset C_{sigma(i)} at position (j + tau_i) mod L
- 2s * inv3 = 2 * 3^{j-1} r_i lies in coset C_{sigma(i)} at position (j - 1 + tau_i) mod L
- The phase omega^{s * inv3} = omega^{3^{j-1} r_i}

So P maps from position j in coset i to two positions in coset sigma(i):
- Position (j + tau_i) mod L with weight 1/2
- Position (j - 1 + tau_i) mod L with weight (1/2) omega^{3^{j-1} r_i}

The INTRA-COSET part of this is: from position j, go to position (j + tau_i)
(for T_0) or position (j - 1 + tau_i) (for T_1). The INTER-COSET part is
the permutation i -> sigma(i). The COCYCLE is the phase omega^{3^{j-1} r_i}
on the T_1 branch.

In the intra-coset Fourier basis (standard, not twisted), the T_0 branch
contributes omega_L^{k * tau_i} to mode k, and the T_1 branch contributes
omega_L^{k * (tau_i - 1)} * (phase average over the cocycle).

The cocycle omega^{3^{j-1} r_i} varies with j, so when we project onto
mode k, we get:
  (T_1 projection onto mode k) = (1/2) omega_L^{k(tau_i - 1)} *
    (1/L) sum_{j=0}^{L-1} omega_L^{-k'j} omega^{3^{j-1} r_i} omega_L^{kj}

This involves a sum over j of omega_L^{(k-k')j} * omega^{3^{j-1} r_i},
which is a "Jacobi-type" sum mixing the Fourier modes.

For k = k': the sum is (1/L) sum_j omega^{3^{j-1} r_i} -- an exponential
sum over the <3>-orbit. This is bounded by sqrt(p)/L by the Gauss sum bound.

For k != k': the sum involves omega_L^{(k-k')j} * omega^{3^{j-1} r_i},
a "twisted" exponential sum. These cross-terms are what couple modes.

The KEY QUESTION: For large p, are these cross-terms small enough that the
diagonal blocks dominate?

Let me compute this precisely for various primes.
"""

import numpy as np


def ord_mod(a, p):
    if a % p == 0:
        return 0
    val = a % p
    r = 1
    cur = val
    while cur != 1:
        cur = (cur * val) % p
        r += 1
    return r


def subgroup_23(p):
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


def compute_cocycle_matrix(p, cosets, L):
    """
    Compute the L x L cocycle matrix C^{(i)}_{k, k'} for each coset i.

    The cocycle arises from the "+1" phase on the T_1 branch:
    omega^{s * inv3} where s = 3^j r_i.

    The phase is omega^{3^{j-1} r_i} (for j >= 1) or omega^{3^{L-1} r_i} (for j = 0).

    In the Fourier basis, the matrix element coupling mode k' to mode k
    from coset i to coset sigma(i) is:

    For the T_1 branch:
    C^{(i)}_{k, k'} = (1/(2L)) sum_{j=0}^{L-1} omega_L^{(k'-k)j} omega_L^{-k} omega^{3^{j-1} r_i}
    (times overall phase factors from tau_i)

    Let me compute this precisely from the full transfer matrix.
    """
    m = len(cosets)
    omega_p = np.exp(2j * np.pi / p)
    omega_L = np.exp(2j * np.pi / L)
    inv3 = pow(3, p - 2, p)

    # For each coset, compute the cocycle phases
    # The phase at position j in coset i is omega_p^{coset[i][(j-1) % L]}
    # (since s * inv3 = 3^{j-1} r_i when s = 3^j r_i)

    cocycle_phases = []
    for i in range(m):
        phases = np.zeros(L, dtype=complex)
        for j in range(L):
            # s = cosets[i][j] = 3^j r_i
            # s * inv3 = 3^{j-1} r_i = cosets[i][(j-1) % L]
            s_inv3 = cosets[i][(j - 1) % L]
            phases[j] = omega_p ** s_inv3
        cocycle_phases.append(phases)

    # The Fourier-mode coupling matrix for the T_1 branch from coset i:
    # (Ignoring inter-coset permutation and tau shifts)
    # C_{k,k'} = (1/L) sum_j omega_L^{-(k-k')j} * omega_L^{-k} * cocycle_phase[j]
    # = omega_L^{-k} * (1/L) sum_j omega_L^{(k'-k)j} * cocycle_phase[j]

    # Actually, let me derive this more carefully.
    # The T_0 branch: a_{2s} with s = 3^j r_i.
    #   2s = 2 * 3^j r_i is in coset sigma(i) at position (j + tau_i) mod L.
    #   In Fourier mode k of coset sigma(i), this contributes:
    #   (1/2) * (1/sqrt(L)) omega_L^{-k(j+tau_i)} * a_{cosets[i][j]}
    #   = (1/2) omega_L^{-k*tau_i} * (1/sqrt(L)) omega_L^{-kj} * a_{cosets[i][j]}
    #   Summing over j with the mode k' of coset i:
    #   a_{cosets[i][j]} <- (1/sqrt(L)) omega_L^{k'j} * b_{i,k'}
    #   Contribution to b_{sigma(i),k}:
    #   (1/2) omega_L^{-k*tau_i} * (1/L) sum_j omega_L^{(k'-k)j} * b_{i,k'}
    #   = (1/2) omega_L^{-k*tau_i} * delta_{k,k'} * b_{i,k'}
    #
    # So T_0 is DIAGONAL in modes: it maps mode k to mode k, with phase omega_L^{-k*tau_i}.

    # The T_1 branch: a_{2s/3} = a_{2 * 3^{j-1} r_i} with s = 3^j r_i.
    #   2 * 3^{j-1} r_i is in coset sigma(i) at position ((j-1) + tau_i) mod L.
    #   Phase: omega_p^{s * inv3} = omega_p^{3^{j-1} r_i} = cocycle_phase[j].
    #   In Fourier mode k of coset sigma(i), this contributes:
    #   (1/2) * (1/sqrt(L)) omega_L^{-k((j-1)+tau_i)} * cocycle_phase[j] * a_{cosets[i][j]}
    #   = (1/2) omega_L^{-k(tau_i-1)} * (1/sqrt(L)) omega_L^{-kj} * cocycle_phase[j] * a_{cosets[i][j]}
    #   Summing over j with mode k' of coset i:
    #   (1/2) omega_L^{-k(tau_i-1)} * (1/L) sum_j omega_L^{(k'-k)j} * cocycle_phase[j] * b_{i,k'}

    # Define the Fourier transform of the cocycle:
    # F_i(k'-k) = (1/L) sum_j omega_L^{(k'-k)j} * cocycle_phase_i[j]

    # Then the total T_1 contribution to b_{sigma(i),k} from b_{i,k'} is:
    # (1/2) omega_L^{-k(tau_i-1)} * F_i(k'-k) * b_{i,k'}

    # And the total P contribution is:
    # P_{sigma(i),k; i,k'} = (1/2) omega_L^{-k*tau_i} * delta_{k,k'}
    #                       + (1/2) omega_L^{-k(tau_i-1)} * F_i(k'-k)
    # = (1/2) omega_L^{-k*tau_i} [delta_{k,k'} + omega_L^k * F_i(k'-k)]

    # Compute F_i(Delta) for each coset i and each Delta = k' - k
    F = np.zeros((m, L), dtype=complex)
    for i in range(m):
        for delta in range(L):
            F[i, delta] = np.mean([
                omega_L ** (delta * j) * cocycle_phases[i][j]
                for j in range(L)
            ])

    return F, cocycle_phases


def analyze_cocycle(p):
    """Analyze the cocycle structure for prime p."""
    H = subgroup_23(p)
    K = len(H)
    L = ord_mod(3, p)
    L2 = ord_mod(2, p)
    m = K // L
    orbit = H

    print(f"\n{'='*70}")
    print(f"Prime p = {p}, K = {K}, L = {L}, L_2 = {L2}, m = {m}")

    cosets, _ = decompose_cosets(p, orbit)

    # Compute inter-coset structure
    coset_idx = {}
    for ci, coset in enumerate(cosets):
        for cj, elem in enumerate(coset):
            coset_idx[elem] = (ci, cj)

    sigma = np.zeros(m, dtype=int)
    tau = np.zeros(m, dtype=int)
    for i in range(m):
        r_i = cosets[i][0]
        two_r_i = (2 * r_i) % p
        ci, cj = coset_idx[two_r_i]
        sigma[i] = ci
        tau[i] = cj

    print(f"  sigma (coset permutation under x2): {list(sigma)}")
    print(f"  tau (intra-coset shifts): {list(tau)}")

    # Compute cocycle Fourier transform
    F, cocycle_phases = compute_cocycle_matrix(p, cosets, L)

    # Show |F_i(Delta)| for each coset
    print(f"\n  Cocycle Fourier transform |F_i(Delta)|:")
    print(f"  (F_i(0) = exponential sum over <3>-orbit)")
    for delta in range(min(L, 6)):
        vals = [abs(F[i, delta]) for i in range(m)]
        print(f"    Delta={delta}: {[f'{v:.4f}' for v in vals]}")

    # The coupling strength between modes k and k' is |F_i(k'-k)|
    # For Delta = 0: F_i(0) = (1/L) sum_j omega_p^{3^{j-1} r_i}
    # This is an exponential sum over the <3>-orbit, bounded by sqrt(p)/L

    # For Delta != 0: the coupling involves a twisted exponential sum
    # These should be even smaller (they average over oscillations)

    print(f"\n  Diagonal coupling |F_i(0)| (this is 1/L * exp sum over <3>-orbit):")
    for i in range(m):
        print(f"    Coset {i} (rep={cosets[i][0]}): |F_i(0)| = {abs(F[i,0]):.6f}")

    print(f"\n  The transfer matrix in mode basis has entries:")
    print(f"  P_{{sigma(i),k; i,k'}} = (1/2) omega_L^{{-k*tau_i}} [delta_{{k,k'}} + omega_L^k * F_i(k'-k)]")
    print(f"  So mode k maps to mode k with strength (1/2)|1 + omega_L^k * F_i(0)|")
    print(f"  And mode k' maps to mode k with strength (1/2)|omega_L^k * F_i(k'-k)|")

    omega_L = np.exp(2j * np.pi / L)

    # Compute the diagonal (mode-preserving) coupling strength
    print(f"\n  Mode-preserving strength (1/2)|1 + omega_L^k * F_i(0)| for each (i, k):")
    for k in range(min(L, 6)):
        strengths = []
        for i in range(m):
            val = 0.5 * abs(1 + omega_L**k * F[i, 0])
            strengths.append(val)
        print(f"    k={k}: {[f'{s:.4f}' for s in strengths]}")

    # For comparison, the "naive" strength (without cocycle) would be:
    # (1/2)|1 + omega_L^k| (from the eigenvalue analysis of Section 12)
    print(f"\n  Naive strength (1/2)|1+omega_L^k| (cocycle-free):")
    for k in range(min(L, 6)):
        print(f"    k={k}: {0.5 * abs(1 + omega_L**k):.4f}")

    # Build the full transfer matrix in the mode basis and verify eigenvalues
    # Build full K x K transfer matrix
    omega_p = np.exp(2j * np.pi / p)
    idx = {r: i for i, r in enumerate(orbit)}
    inv3 = pow(3, p - 2, p)

    P = np.zeros((K, K), dtype=complex)
    for i_s, s in enumerate(orbit):
        r1 = (2 * s) % p
        if r1 in idx:
            P[i_s, idx[r1]] += 0.5
        s_inv3 = (s * inv3) % p
        r2 = (2 * s_inv3) % p
        phase = omega_p ** s_inv3
        if r2 in idx:
            P[i_s, idx[r2]] += 0.5 * phase

    evals_P = np.linalg.eigvals(P)
    evals_P_sorted = sorted(evals_P, key=lambda x: -abs(x))
    print(f"\n  Full transfer matrix: |lambda_1| = {abs(evals_P_sorted[0]):.6f}, "
          f"|lambda_2| = {abs(evals_P_sorted[1]):.6f}, gap = {1-abs(evals_P_sorted[1]):.6f}")

    # Build the mode-basis transfer matrix
    # Indices: flat index = i * L + k (coset i, mode k)
    # The entry P_mode[sigma(i)*L+k, i*L+k'] corresponds to:
    # (1/2) omega_L^{-k*tau_i} * [delta_{k,k'} + omega_L^k * F_i(k'-k)]

    P_mode = np.zeros((K, K), dtype=complex)
    for i in range(m):
        si = sigma[i]
        ti = tau[i]
        for k in range(L):
            for kp in range(L):
                delta = (kp - k) % L
                entry = 0.5 * omega_L ** (-k * ti) * (
                    (1.0 if k == kp else 0.0) + omega_L ** k * F[i, delta]
                )
                P_mode[si * L + k, i * L + kp] = entry

    evals_mode = np.linalg.eigvals(P_mode)
    evals_mode_sorted = sorted(evals_mode, key=lambda x: -abs(x))

    max_diff = max(abs(a - b) for a, b in zip(
        sorted([abs(e) for e in evals_P], reverse=True),
        sorted([abs(e) for e in evals_mode], reverse=True)
    ))
    print(f"\n  Mode-basis eigenvalue match: max diff = {max_diff:.2e}")
    print(f"  Mode-basis: |lambda_1| = {abs(evals_mode_sorted[0]):.6f}, "
          f"|lambda_2| = {abs(evals_mode_sorted[1]):.6f}")

    # Now study what happens when we RESTRICT to a single mode k
    # (ignoring cross-mode coupling). This is the "quotient operator" Q_k.
    print(f"\n  Single-mode quotient operators (ignoring cross-mode coupling):")
    for k in range(min(L, 6)):
        # Q_k is m x m with Q_k[sigma(i), i] = (1/2) omega_L^{-k*tau_i} * (1 + omega_L^k * F_i(0))
        Q_k = np.zeros((m, m), dtype=complex)
        for i in range(m):
            si = sigma[i]
            ti = tau[i]
            Q_k[si, i] = 0.5 * omega_L ** (-k * ti) * (1 + omega_L ** k * F[i, 0])
        evals_Qk = np.linalg.eigvals(Q_k)
        rho_k = max(abs(e) for e in evals_Qk)

        # Compare to (1/2)|1 + omega_L^k| (the naive bound)
        naive = 0.5 * abs(1 + omega_L ** k)

        print(f"    k={k}: rho(Q_k) = {rho_k:.6f}, naive (1/2)|1+w^k| = {naive:.6f}, "
              f"ratio = {rho_k/naive if naive > 1e-10 else float('inf'):.4f}")

    # KEY INSIGHT: The coupling between modes is controlled by |F_i(Delta)| for Delta != 0.
    # If these are small compared to |1 + omega_L^k F_i(0)|, the diagonal blocks dominate.
    # In the limit p -> infinity with fixed K, the cocycle phases omega_p^{3^j r_i}
    # become equidistributed on the unit circle, so:
    #   F_i(Delta) -> 0 for all Delta (including Delta = 0!)
    # In that limit, P_mode -> (1/2) * (diagonal blocks with entries omega_L^{-k*tau_i})
    # and the spectral radius -> 1/2 for all modes k != L/2.

    # For FINITE p, the key quantity is how far F_i(0) is from 0.
    # F_i(0) = (1/L) sum_j omega_p^{3^{j-1} r_i} is an exponential sum.
    # By the CDG identity applied to <3>: if L >= sqrt(p), this is O(1/sqrt(L)).
    # If L < sqrt(p), this can be O(1).

    print(f"\n  Summary of cocycle analysis:")
    print(f"    F_i(0) = (1/L) * exp_sum over <3>-orbit")
    for i in range(min(m, 4)):
        print(f"    Coset {i}: F_i(0) = {F[i,0]:.6f}, |F_i(0)| = {abs(F[i,0]):.6f}")

    # The spectral radius with cocycle corrections:
    # For k = 0: (1/2)|1 + F_i(0)|. If F_i(0) ~ 1 (all phases near 1), then rho ~ 1.
    # If F_i(0) ~ 0 (equidistributed phases), then rho ~ 1/2.
    # This is exactly the CDG/Jensen mechanism!

    # For k != 0: (1/2)|1 + omega_L^k F_i(0)|. Even if F_i(0) = 1, this is
    # (1/2)|1 + omega_L^k| = cos(pi k/L), which is < 1 for k != 0.
    # The cocycle REDUCES this further (since F_i(0) != 1 generically).

    # So the spectral gap for the FULL operator comes from:
    # max over k of (1/2)|1 + omega_L^k * F_i(0)| (for the diagonal block)
    # plus corrections from the off-diagonal coupling.

    return F, evals_P, evals_mode


def main():
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
              101, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

    # Summary table
    print("\nSummary: Gap analysis via cocycle")
    print(f"{'p':>5} {'K':>4} {'L':>3} {'m':>3} {'|lam2|':>8} {'gap':>8} {'max|F(0)|':>10} {'k=0 rho':>8} {'k=1 rho':>8}")
    print("-" * 75)

    for p in primes:
        try:
            H = subgroup_23(p)
            K = len(H)
            L = ord_mod(3, p)
            m = K // L
            orbit = H
            cosets, _ = decompose_cosets(p, orbit)

            # Compute inter-coset structure
            coset_idx = {}
            for ci, coset in enumerate(cosets):
                for cj, elem in enumerate(coset):
                    coset_idx[elem] = (ci, cj)
            sigma = [0]*m
            tau = [0]*m
            for i in range(m):
                r_i = cosets[i][0]
                two_r_i = (2 * r_i) % p
                ci, cj = coset_idx[two_r_i]
                sigma[i] = ci
                tau[i] = cj

            F, _ = compute_cocycle_matrix(p, cosets, L)
            max_F0 = max(abs(F[i, 0]) for i in range(m))

            # Full eigenvalues
            omega_p = np.exp(2j * np.pi / p)
            idx_map = {r: i for i, r in enumerate(orbit)}
            inv3 = pow(3, p - 2, p)
            Pfull = np.zeros((K, K), dtype=complex)
            for i_s, s in enumerate(orbit):
                r1 = (2 * s) % p
                if r1 in idx_map:
                    Pfull[i_s, idx_map[r1]] += 0.5
                s_inv3 = (s * inv3) % p
                r2 = (2 * s_inv3) % p
                phase = omega_p ** s_inv3
                if r2 in idx_map:
                    Pfull[i_s, idx_map[r2]] += 0.5 * phase
            evals_P = sorted(np.linalg.eigvals(Pfull), key=lambda x: -abs(x))

            omega_L = np.exp(2j * np.pi / L)

            # Single-mode quotient operators
            rho_k0 = 0
            rho_k1 = 0
            for k in range(L):
                Q_k = np.zeros((m, m), dtype=complex)
                for i in range(m):
                    si = sigma[i]
                    ti = tau[i]
                    Q_k[si, i] = 0.5 * omega_L ** (-k * ti) * (1 + omega_L ** k * F[i, 0])
                evals_Qk = np.linalg.eigvals(Q_k)
                rho = max(abs(e) for e in evals_Qk)
                if k == 0:
                    rho_k0 = rho
                elif k == 1:
                    rho_k1 = rho

            print(f"{p:>5} {K:>4} {L:>3} {m:>3} {abs(evals_P[1]):>8.4f} {1-abs(evals_P[1]):>8.4f} "
                  f"{max_F0:>10.4f} {rho_k0:>8.4f} {rho_k1:>8.4f}")
        except Exception as e:
            print(f"{p:>5} Error: {e}")


if __name__ == "__main__":
    main()
