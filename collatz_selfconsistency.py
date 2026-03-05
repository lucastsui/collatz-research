"""
THE SELF-CONSISTENCY OBSTRUCTION

New framework: In a Collatz cycle, n_0 determines its own parity sequence,
and the parity sequence determines n_0 via the cycle equation. This creates
a self-referential fixed point condition.

Define two maps:
  Psi: n -> parity sequence (via Collatz dynamics)
  Phi: parity sequence -> n_0 (via cycle equation)

A cycle exists iff Phi(Psi(n)) = n.

Key question: How "stable" is this fixed point? If small perturbations
of n cause large changes in Phi(Psi(n)), the fixed point is unstable
and generically doesn't exist.

EXPERIMENT: For each n, compute:
  1. Psi(n) = parity sequence for p steps
  2. Phi(Psi(n)) = n' (the n_0 implied by the cycle equation)
  3. The "self-consistency error" |n - n'|/n

If this error is always large (bounded away from 0), no cycle exists.
"""

def collatz_orbit(n, p):
    """Compute p steps of Collatz, return parity sequence and final value"""
    orbit = [n]
    parities = []
    for _ in range(p):
        if n % 2 == 1:
            parities.append(1)
            n = (3 * n + 1) // 2
        else:
            parities.append(0)
            n = n // 2
        orbit.append(n)
    return parities, orbit

def cycle_equation_n0(parities, p):
    """Given a parity sequence, compute what n_0 WOULD be if this were a cycle"""
    k = sum(parities)
    if k == 0 or k == p:
        return None, None, None
    
    D = 2**p - 3**k
    if D <= 0:
        return None, None, None
    
    # Compute S
    odd_positions = [i for i, e in enumerate(parities) if e == 1]
    S = 0
    for j_idx, i_j in enumerate(odd_positions):
        j = j_idx + 1
        S += pow(3, k - j) * pow(2, i_j)
    
    if S % D == 0:
        return S // D, S, D
    else:
        return S / D, S, D  # fractional = not a valid cycle

def self_consistency_error(n, p):
    """How far is n from being the start of a cycle of length p?"""
    parities, orbit = collatz_orbit(n, p)
    n0_implied, S, D = cycle_equation_n0(parities, p)
    
    if n0_implied is None:
        return None, None
    
    error = abs(n0_implied - n) / n if n > 0 else float('inf')
    return error, n0_implied

# === EXPERIMENT 1: Self-consistency error for various n and p ===
print("=== Self-Consistency Error: |Phi(Psi(n)) - n| / n ===\n")

for p in [10, 20, 30, 50]:
    print(f"p = {p}:")
    min_error = float('inf')
    min_n = None
    errors = []
    
    for n in range(3, 1001, 2):  # odd numbers (since n_min must be odd)
        err, n0_impl = self_consistency_error(n, p)
        if err is not None:
            errors.append(err)
            if err < min_error:
                min_error = err
                min_n = n
    
    if errors:
        avg_err = sum(errors) / len(errors)
        print(f"  Tested {len(errors)} odd numbers in [3, 999]")
        print(f"  Min error: {min_error:.6f} at n={min_n}")
        print(f"  Avg error: {avg_err:.2f}")
        print(f"  Fraction with error < 0.1: {sum(1 for e in errors if e < 0.1)/len(errors):.4f}")
        print(f"  Fraction with error < 0.01: {sum(1 for e in errors if e < 0.01)/len(errors):.4f}")
    print()

# === EXPERIMENT 2: The "derivative" of Phi∘Psi ===
# How much does Phi(Psi(n)) change when n changes by 2 (staying odd)?
print("=== Sensitivity: |Phi(Psi(n+2)) - Phi(Psi(n))| / 2 ===\n")

for p in [10, 20, 30]:
    print(f"p = {p}:")
    sensitivities = []
    
    for n in range(3, 501, 2):
        err1, n0_1 = self_consistency_error(n, p)
        err2, n0_2 = self_consistency_error(n + 2, p)
        if n0_1 is not None and n0_2 is not None:
            sensitivity = abs(n0_2 - n0_1) / 2
            sensitivities.append(sensitivity)
    
    if sensitivities:
        avg_sens = sum(sensitivities) / len(sensitivities)
        max_sens = max(sensitivities)
        min_sens = min(sensitivities)
        # Count how often sensitivity > 1 (meaning the map is "expansive")
        expansive_frac = sum(1 for s in sensitivities if s > 1) / len(sensitivities)
        print(f"  Avg |dPhi∘Psi/dn|: {avg_sens:.2f}")
        print(f"  Min: {min_sens:.4f}, Max: {max_sens:.2f}")
        print(f"  Fraction where |derivative| > 1 (expansive): {expansive_frac:.4f}")
    print()

# === EXPERIMENT 3: Fixed point iteration ===
# Start with n, compute n' = Phi(Psi(n)), then n'' = Phi(Psi(n')), etc.
# If the iteration diverges, no fixed point exists nearby.
print("=== Fixed Point Iteration: n -> Phi(Psi(n)) -> ... ===\n")

for n_start in [3, 7, 15, 27, 101, 255, 511, 999]:
    for p in [10, 20]:
        n = n_start
        trajectory = [n]
        converged = False
        diverged = False
        
        for step in range(20):
            parities, orbit = collatz_orbit(int(round(n)), p)
            n_new, S, D = cycle_equation_n0(parities, p)
            if n_new is None or n_new <= 0 or n_new > 10**15:
                diverged = True
                break
            trajectory.append(n_new)
            if isinstance(n_new, int) and n_new == int(round(n)):
                converged = True
                break
            n = n_new
        
        status = "CONVERGED" if converged else ("DIVERGED" if diverged else "oscillating")
        traj_str = " -> ".join(f"{t:.1f}" if isinstance(t, float) else str(t) for t in trajectory[:6])
        if len(trajectory) > 6:
            traj_str += " -> ..."
        print(f"  n={n_start:4d}, p={p:2d}: {status:11s} | {traj_str}")

print()
print("=== KEY INSIGHT ===")
print("If Phi∘Psi is 'expansive' (|derivative| > 1 almost everywhere),")
print("then fixed points are repelling and generically don't exist.")
print("This would be a topological obstruction, not a probabilistic one.")
