# Novel Approaches to the Universal Constant Spectral Gap

## The Problem (Recap)

For prime p >= 5, the Markov operator M on Z/pZ:

    (Mf)(x) = (1/2)f(x * 2^{-1}) + (1/2)f((3x+1) * 2^{-1})

**Proved:** Every eigenvalue lambda != 1 satisfies |lambda| < 1.
**Proved:** |lambda_2| <= 1 - c/p (weak bound).
**Numerical:** |lambda_2| in [0.66, 0.81] for all 166 primes tested (5 <= p <= 997). Mean ~ 0.70.
**Open:** Prove |lambda_2| <= 1 - c for a universal constant c > 0.

---

## A. Entropy / Information-Theoretic Approach

### A.1. Setup: The Collatz Channel

Model the random walk as an information channel. Let X_0 be the initial state (uniform on Z/pZ), and X_n the state after n steps. The channel capacity is governed by how fast mutual information I(X_0; X_n) decays.

**Data processing inequality:** I(X_0; X_n) is non-increasing in n.

**Connection to spectral gap:** For a reversible chain with spectral gap gamma,

    I(X_0; X_n) <= (1 - gamma)^{2n} * log p.

So a constant gamma gives exponential decay of mutual information, and vice versa.

However, our chain is NOT reversible (M is not self-adjoint), so the standard connection requires care. For a general chain with spectral radius rho on the non-constant subspace:

    ||P^n(x, .) - pi||_{TV} <= sqrt(p) * rho^n,

so the chi-squared divergence satisfies chi^2(P^n(x, .) || pi) <= p * rho^{2n}, giving

    I(X_0; X_n) <= (1/2) * p * rho^{2n} * log(e).

The reverse direction: if we can bound I(X_0; X_n) independently, we get a bound on rho.

### A.2. Entropy Production per Step

At each step, the walk applies one of two maps:
- T_0(x) = x/2 (multiplication by 2^{-1})
- T_1(x) = (3x+1)/2 (affine map)

For the entropy of the conditional distribution P(X_{n+1} | X_n = x):
- If T_0(x) != T_1(x): the output is uniformly distributed on {T_0(x), T_1(x)}, giving conditional entropy H(X_{n+1} | X_n = x) = 1 bit.
- If T_0(x) = T_1(x): the output is deterministic, giving 0 bits.

**When do T_0(x) = T_1(x)?** This requires x/2 = (3x+1)/2, i.e., x = 3x+1, i.e., 2x = -1, i.e., x = -2^{-1} mod p = (p-1)/2 (for odd p). So exactly ONE state x_0 = (p-1)/2 has this collision.

Therefore H(X_{n+1} | X_n) = (p-1)/p bits per step (close to 1 for large p).

The unconditional entropy satisfies H(X_n) -> log p (converges to maximum). The rate of this convergence is controlled by the spectral gap.

### A.3. The Key Entropy Argument (Formalized)

**Definition.** For a probability distribution mu on Z/pZ, define the Renyi-2 entropy:

    H_2(mu) = -log(sum_x mu(x)^2) = -log(||mu||_2^2).

**Lemma (Renyi-2 entropy production).** If mu is a distribution on Z/pZ and nu = M^* mu (the pushforward), then

    ||nu||_2^2 = (1/4)||T_0^* mu||_2^2 + (1/4)||T_1^* mu||_2^2 + (1/2) <T_0^* mu, T_1^* mu>.

Since T_0 and T_1 are bijections, ||T_i^* mu||_2^2 = ||mu||_2^2. Therefore:

    ||nu||_2^2 = (1/2)||mu||_2^2 + (1/2)<T_0^* mu, T_1^* mu>.

For the collision probability:

    ||nu||_2^2 - 1/p = (1/2)(||mu||_2^2 - 1/p) + (1/2)(<T_0^* mu, T_1^* mu> - 1/p).

The inner product <T_0^* mu, T_1^* mu> = sum_y (T_0^* mu)(y) * (T_1^* mu)(y) = sum_y mu(T_0^{-1}(y)) * mu(T_1^{-1}(y)) = sum_y mu(2y) * mu(2(3^{-1}(2y-1))).

This is the correlation between mu(2y) and mu at the "shifted" point. For the uniform distribution, this equals 1/p. For a distribution concentrated near a single point, it can be as large as ||mu||_2^2 = 1.

**The obstruction:** The correlation <T_0^* mu, T_1^* mu> can equal ||mu||_2^2 when mu is constant on orbits of y -> 3y + 2^{-1}. This is EXACTLY the Combined Theorem's obstruction. We've proved such functions must be 0, but what we need is a QUANTITATIVE bound: how close can the correlation get to ||mu||_2^2?

### A.4. Information-Theoretic Two-Step Bound

**Key insight:** Even if the one-step correlation can be large, the TWO-step correlation involves a DIFFERENT affine map.

After two steps with choices (b_1, b_2), the four possible maps are:
- (0,0): x -> x/4
- (0,1): x -> (3x/2 + 1)/2 = 3x/4 + 1/2
- (1,0): x -> (3x+1)/(2*2) = (3x+1)/4
- (1,1): x -> (3(3x+1)/2 + 1)/2 = (9x+5)/4

The multiplicative parts are {1/4, 3/4, 3/4, 9/4} (mod p). For the two maps with multiplier 3/4, they have DIFFERENT translations: 1/2 vs 1/4. This means the two 3/4-maps, despite having the same multiplicative part, shift by different amounts. The "+1" at different positions creates distinct shifts.

**Proposition (Two-step contraction for Renyi-2 entropy).**

    ||M^{*2} mu||_2^2 <= ||mu||_2^2 * rho(p)

where rho(p) is determined by the four-map correlation structure.

Computing:

    ||M^{*2} mu||_2^2 = sum_{b1,b2} sum_{b1',b2'} (1/16) <T_{b1,b2}^* mu, T_{b1',b2'}^* mu>

where T_{b1,b2} = T_{b2} o T_{b1}. Each inner product equals sum_x mu(T_{b1,b2}^{-1}(x)) * mu(T_{b1',b2'}^{-1}(x)).

When T_{b1,b2}^{-1} and T_{b1',b2'}^{-1} differ by a nontrivial translation (not the identity map), the inner product involves a "shifted self-correlation" of mu, which cannot equal ||mu||_2^2 for a non-constant mu on Z/pZ (by our Combined Theorem argument applied to the specific translation).

Let me enumerate the 16 inner products. The maps T_{b1,b2}(x) = a_{b1,b2} * x + d_{b1,b2}:

- (0,0): a = 1/4, d = 0
- (0,1): a = 3/4, d = 1/2
- (1,0): a = 3/4, d = 1/4
- (1,1): a = 9/4, d = 5/4

The ratio map T_{b1,b2}^{-1} o T_{b1',b2'} is x -> (a'/a)*x + (d'-d)/a, an affine map. The inner product <T_{b1,b2}^* mu, T_{b1',b2'}^* mu> = sum_x mu(x) * mu((a'/a)*x + (d'-d)/a).

This equals ||mu||_2^2 only if (a'/a)*x + (d'-d)/a = x for all x in supp(mu), i.e., a' = a AND d' = d. Otherwise, it's a "twisted" inner product that provides contraction.

**Counting identical pairs:** Among the 16 ordered pairs (T, T'), exactly 4 have T = T' (the diagonal). The remaining 12 have T != T'.

Among these 12: some pairs (T, T') have a'/a = 1 but d' != d (pure translations). These give:
- (0,1) vs (1,0): a'/a = (3/4)/(3/4) = 1, translation difference = (1/4 - 1/2)/(3/4) = -1/3
- (1,0) vs (0,1): similarly, translation +1/3

These are the MOST dangerous because they correspond to pure additive shifts. For the inner product sum_x mu(x) * mu(x - 1/3), maximizing over mu with ||mu||_2^2 = S:

By Cauchy-Schwarz: |sum_x mu(x) mu(x-1/3)| <= ||mu||_2^2 = S.
Equality iff mu(x) = mu(x - 1/3) for all x, i.e., mu has period 1/3. In Z/pZ, this means mu has period (3^{-1}) mod p. Since p is prime and 3^{-1} != 0, this forces mu constant, contradicting mu being non-uniform.

**Quantitative bound on the shifted correlation:** This is where the argument needs teeth. For a non-uniform probability distribution mu on Z/pZ (meaning mu != 1/p for some x), how small can the shifted correlation be compared to ||mu||_2^2?

**Proposition (Shifted correlation bound via Fourier analysis).** Let mu be a probability distribution on Z/pZ with ||mu - 1/p||_2^2 = sigma^2 > 0 (the "non-uniformity"). For any s != 0 mod p:

    sum_x mu(x) * mu(x + s) = ||mu||_2^2 - 2 * sum_{r != 0} |mu_hat(r)|^2 * sin^2(pi*r*s/p)

where mu_hat(r) = (1/p) sum_x mu(x) omega^{-rx}.

*Proof.* Write mu(x) = (1/p) + f(x) where f has zero mean. Then

    sum_x mu(x) mu(x+s) = 1/p + sum_x f(x) f(x+s) = 1/p + p * sum_r |f_hat(r)|^2 omega^{rs}

and ||mu||_2^2 = 1/p + p * sum_r |f_hat(r)|^2. Therefore

    ||mu||_2^2 - sum_x mu(x) mu(x+s) = p * sum_r |f_hat(r)|^2 (1 - omega^{rs})
    = p * sum_r |f_hat(r)|^2 * 2 * sin^2(pi*r*s/p) * ...

Actually, let me be more careful. We have

    sum_x mu(x) mu(x+s) = sum_r |mu_hat(r)|^2 * p * omega^{rs}.

Wait. Let's use the standard convolution. Let mu * mu^{rev}(s) = sum_x mu(x) mu(x+s). In Fourier:

    mu * mu^{rev}(s) = p * sum_r |mu_hat(r)|^2 omega^{rs}.

So sum_x mu(x)mu(x+s) = p sum_r |mu_hat(r)|^2 omega^{rs}.

And ||mu||_2^2 = p sum_r |mu_hat(r)|^2.

Therefore:

    ||mu||_2^2 - sum_x mu(x)mu(x+s) = p sum_r |mu_hat(r)|^2 (1 - omega^{rs})
    = p sum_{r != 0} |mu_hat(r)|^2 (1 - cos(2pi*r*s/p))   [real part only, since ||mu||_2^2 is real]
    = 2p sum_{r != 0} |mu_hat(r)|^2 sin^2(pi*r*s/p).

And ||mu||_2^2 - 1/p = p sum_{r != 0} |mu_hat(r)|^2 = sigma^2.

So the fractional loss from the shift is:

    (||mu||_2^2 - sum mu(x)mu(x+s)) / sigma^2 = (2p sum_{r != 0} |mu_hat(r)|^2 sin^2(pi*r*s/p)) / (p sum_{r != 0} |mu_hat(r)|^2)

This is a WEIGHTED AVERAGE of 2*sin^2(pi*r*s/p) with weights |mu_hat(r)|^2.

The minimum over all non-uniform mu is achieved when the weights concentrate on the r that minimizes sin^2(pi*r*s/p), i.e., on r closest to 0 or p. For s = p*3^{-1}, the minimum of sin^2(pi*r*s/p) over r != 0 is sin^2(pi/p) ~ (pi/p)^2 for r = 1 or r = p-1.

So the worst case gives fractional loss ~ 2(pi/p)^2, meaning the correlation approaches ||mu||_2^2 at rate O(1/p^2). This gives only a 1/p^2 improvement per two steps, which is too weak.

### A.5. Why the Entropy Approach Alone is Insufficient

The fundamental issue is that the entropy approach tracks the COLLISION PROBABILITY (Renyi-2 entropy), which is dominated by the worst-case Fourier mode. A single Fourier mode r = 1 can concentrate all the non-uniformity, and for this mode, the shifted correlation with shift s ~ p/3 gives only O(1/p^2) improvement over the self-correlation.

**Diagnosis:** The entropy approach captures the same information as the spectral analysis -- it cannot circumvent the fundamental algebraic structure. The correlation <T_0^* mu, T_1^* mu> being close to ||mu||_2^2 is equivalent to the operator norm ||M||_op being close to 1 on the non-constant subspace, which is exactly the problem we're trying to solve.

**What would make it work:** If we could show that after O(1) steps, the DISTRIBUTION of Fourier mass spreads across many modes (not concentrated on one), then the weighted average of sin^2 terms would be bounded away from 0. This is essentially the "energy coupling between cosets" mechanism identified in the session log.

**Verdict: The pure entropy approach, without additional structure, reduces to the same spectral gap problem.** It is not an independent route.

---

## B. Coupling Arguments

### B.1. Standard Coupling (Fails)

For two copies (X_n, Y_n) using the SAME random bits at each step:
- D_n = X_n - Y_n satisfies D_{n+1} = D_n/2 or D_{n+1} = 3D_n/2.

This is a multiplicative random walk on F_p^*. It NEVER reaches 0, so the coupling time is infinite.

### B.2. Independent Coupling (Trivial)

Running two copies independently, they couple when they happen to land on the same state. For a chain on p states approaching stationarity, coupling happens in time O(p * t_mix). This gives nothing beyond the spectral gap bound we already have.

### B.3. "Grand Coupling" / Coupling from the Past

In Propp-Wilson "coupling from the past," one runs ALL p chains (one from each starting state) using the same random bits. The coupling time is the time until all chains have coalesced.

At each step, every state x maps to one of two states: T_0(x) or T_1(x). Since the random bit is shared, all chains simultaneously apply T_b for the same b.

After n steps with choices b_1, ..., b_n, the map is the affine map T_{b_n} o ... o T_{b_1}(x) = a * x + d where a = 2^{-n} * 3^w (w = number of 1-bits).

**Coalescence requires:** a * x + d = a * y + d for all x, y, i.e., a = 0 mod p, i.e., 3^w = 0 mod p. This is IMPOSSIBLE (since gcd(3,p) = 1 for p >= 5). So the grand coupling with identical random bits never coalesces either.

### B.4. Non-Standard Coupling: "Shift Coupling"

**Idea:** Instead of using the same random bit for both chains, we use a CORRELATED but not identical random choice. Specifically, design a joint distribution of (b, b') on {0,1}^2 such that:

1. Marginally, b and b' are each uniform on {0,1} (so both chains are valid Markov chains).
2. P(b = b') is maximized when X_n and Y_n are "close" in some metric.
3. When b != b', the chains are pushed TOWARD each other.

**Metropolis-style coupling:** For states x, y:
- With probability q(x,y): use the SAME random bit (both go T_0 or both go T_1).
- With probability 1 - q(x,y): use OPPOSITE random bits (one goes T_0, other goes T_1).

For the same bit: D_{n+1} = D_n/2 or 3D_n/2 (multiplicative).
For opposite bits: X_{n+1} - Y_{n+1} = x/2 - (3y+1)/2 = (x - 3y - 1)/2, or (3x+1)/2 - y/2 = (3x - y + 1)/2.

With opposite bits, the difference involves ADDITIVE terms (+/- 1/2), breaking the multiplicative structure.

**Definition (Shift-coupling distance).** For x, y in Z/pZ, define

    d(x, y) = min_{k >= 0} |x - 3^k * y - c_k|_p

where c_k is the accumulated translation after k applications of y -> 3y + alpha, and |.|_p is the "natural" distance on Z/pZ (min(|z|, p - |z|) for the standard representative).

This metric captures closeness in the affine orbit structure.

### B.5. Path Coupling on a Graph

**Path coupling (Bubley-Dyer):** Define a graph G on Z/pZ where x ~ y iff d(x,y) = 1 (adjacent in the natural cyclic ordering). The path coupling bound says:

If for all adjacent pairs (x, y), there exists a coupling of (X_1, Y_1) such that E[d(X_1, Y_1)] <= (1 - delta) * d(x, y), then the mixing time is O(log(p * diam(G)) / delta) = O(log p / delta).

**Attempt:** Take x, y adjacent (y = x + 1). Using the same random bit:
- Both T_0: D_1 = (x+1)/2 - x/2 = 1/2 mod p = 2^{-1}. Distance = min(2^{-1} mod p, p - 2^{-1} mod p).
- Both T_1: D_1 = (3(x+1)+1)/2 - (3x+1)/2 = 3/2 mod p. Distance = |3*2^{-1} mod p|.

So using the same bit, D_1 is either 2^{-1} or 3*2^{-1} with equal probability. The expected distance is (1/2)(|2^{-1}|_p + |3*2^{-1}|_p).

For large p, 2^{-1} = (p+1)/2 ~ p/2, and 3*2^{-1} = 3(p+1)/2 mod p = (3p+3)/2 mod p = (p+3)/2 ~ p/2. Both are ~ p/2.

So the expected distance after one step is ~ p/2, while the initial distance was 1. The distance INCREASED by a factor of p/2!

**This means path coupling with the same random bit FAILS catastrophically for adjacent states.**

The issue: multiplication by 2^{-1} (or 3*2^{-1}) takes a small difference and blows it up to size ~ p.

### B.6. Path Coupling with Logarithmic Distance

**Key observation:** The multiplicative structure suggests using a MULTIPLICATIVE distance. Define

    d_log(x, y) = dlog(x - y mod p)

where dlog(z) is some function of z in F_p^* that respects the multiplicative structure.

Specifically, since D_n evolves as D -> D * 2^{-1} or D -> D * 3 * 2^{-1}, the "multiplicative distance" |D| is multiplied by either |2^{-1}| or |3/2|. On F_p^*, all elements have the same "absolute value" 1, so there's no natural multiplicative metric that contracts.

**Alternative: distance in the group (F_p^*, *).** If we view F_p^* as a cyclic group of order p-1, we can define d(x,y) as the discrete log of (x-y) or similar. But the additive structure (x-y) doesn't interact well with the multiplicative group.

### B.7. A Novel "Two-Level" Coupling

**Idea:** Combine coupling ideas from two different scales.

**Level 1 (Multiplicative coalescence):** Run both chains with the same random bits. The difference D_n = X_n - Y_n evolves multiplicatively: D -> D * 2^{-1} or D * 3/2. After n steps, D_n = D_0 * 2^{-n} * 3^w for w 1-bits. The multiplicative walk {2^{-n} * 3^w : n, w} visits all of F_p^* in time O(p) (since <2, 3> = F_p^* for most primes, and even when it's a proper subgroup, it's large).

**Level 2 (Additive shift):** Periodically (every O(1) steps), instead of using the same random bit, use INDEPENDENT random bits. When we use an independent bit and one chain applies T_1 while the other applies T_0:

    X_{n+1} = (3X_n + 1)/2,  Y_{n+1} = Y_n/2

    X_{n+1} - Y_{n+1} = (3X_n + 1 - Y_n)/2

This introduces an ADDITIVE perturbation: the "+1" breaks the multiplicative relationship.

**Strategy:** Use identical bits most of the time (to keep the multiplicative walk going), but every K steps, use independent bits with probability epsilon. The independent-bit steps inject additive randomness, which eventually forces D_n through 0.

**Why this could work:** The multiplicative walk on F_p^* is ergodic (visits all elements). Once D_n passes through certain "favorable" values (where the additive perturbation from the "+1" can push it close to 0), a subsequent identical-bit step can map it TO 0... except it can't, because the multiplicative walk stays in F_p^*.

**Fundamental obstruction:** No matter what coupling we use, D_n = X_n - Y_n = 0 requires X_n = Y_n. The coupling time is the meeting time of two chains. For this meeting to happen at a specific state z, we need both X_n = z and Y_n = z. This is a joint event that doesn't depend on the coupling structure in a way that helps with the SPECTRAL GAP.

### B.8. Coupling Verdict

**Theorem (informal).** Any coupling argument for the affine Collatz walk faces the fundamental problem that the "difference process" is multiplicative and cannot reach 0 in F_p^*. Non-standard couplings that introduce additive perturbations can create meeting events, but the probability of meeting at any specific point is O(1/p), and one needs O(p) such attempts to coalesce. This gives a coupling time of O(p * K) where K is the frequency of independent-bit steps, which at best gives mixing time O(p) -- equivalent to the known bound.

**To break through:** One would need a coupling where the probability of coalescence per step is Omega(1/log p) or better. This seems to require the chains to "attract" each other, which doesn't happen in our system because the dynamics are expanding (multiplication by elements of F_p^* doesn't contract distances).

**Verdict: Standard and non-standard coupling arguments appear unable to give a constant spectral gap for this chain.** The multiplicative structure of the difference process is the core obstruction.

---

## C. Functional Inequality / Poincare Inequality Approach

### C.1. The Dirichlet Form

The spectral gap equals the optimal constant in the Poincare inequality:

    Var(f) <= (1/gap) * E(f, f)

where the Dirichlet form (energy) is:

    E(f, f) = (1/2) sum_x pi(x) sum_y M(x,y) (f(x) - f(y))^2

For the affine Collatz walk with uniform stationary measure pi(x) = 1/p:

    E(f, f) = (1/(2p)) sum_x [(1/2)(f(x) - f(T_0(x)))^2 + (1/2)(f(x) - f(T_1(x)))^2]

Wait -- M is not self-adjoint, so we need to use the ADDITIVE REVERSIBILIZATION. Define the Dirichlet form of the additive reversibilization M_rev = (M + M^*)/2:

    E_{rev}(f, f) = <f, (I - M_rev)f> = <f, f> - (1/2)(<Mf, f> + <f, Mf>) = ||f||^2 - Re(<Mf, f>).

The spectral gap of M_rev is at most the spectral gap of M (in terms of |lambda_2|). Actually, for the Poincare inequality approach on non-reversible chains, we use the MULTIPLICATIVE REVERSIBILIZATION M^* M:

    |lambda_2(M)|^2 = lambda_2(M^* M)

and the spectral gap of M^* M is characterized by:

    ||f||^2 <= (1/gap_{M^*M}) * <f, (I - M^*M)f>   for f perp 1.

### C.2. Direct Dirichlet Form Computation

Let's compute E(f, f) = <f, (I - M^*M)f> = ||f||^2 - ||Mf||^2.

We already know (from the paper):

    ||Mf||^2 = (1/2)||f||^2 + (1/2)Re<T_0 f, T_1 f>

where T_0 f(x) = f(x/2) and T_1 f(x) = f((3x+1)/2). Therefore:

    E(f, f) = ||f||^2 - ||Mf||^2 = (1/2)||f||^2 - (1/2)Re<T_0 f, T_1 f>.

**The Poincare inequality says:** Var(f) <= (1/gap) * E(f, f), i.e.,

    ||f||^2 <= (1/gap) * [(1/2)||f||^2 - (1/2)Re<T_0 f, T_1 f>]

Rearranging: gap <= (||f||^2 - Re<T_0 f, T_1 f>) / (2||f||^2) = (1/2)(1 - Re<T_0 f, T_1 f>/||f||^2).

So: gap = (1/2) * min_{f perp 1, f != 0} (1 - Re<T_0 f, T_1 f>/||f||^2).

The spectral gap is bounded by:

    gap >= (1/2)(1 - max_{f perp 1} Re<T_0 f, T_1 f>/||f||^2).

And we need this maximum to be strictly less than 1. We know it is (Combined Theorem: equality iff f = 0), but we need a quantitative bound.

### C.3. Decomposing the Cross-Term

The key object is:

    <T_0 f, T_1 f> / ||f||^2 = [(1/p) sum_x f(x/2) * conj(f((3x+1)/2))] / ||f||^2.

Substituting y = x/2 (i.e., x = 2y):

    = [(1/p) sum_y f(y) * conj(f(3y + alpha))] / ||f||^2

where alpha = 2^{-1} mod p.

This is the **autocorrelation of f with respect to the affine map y -> 3y + alpha**.

In Fourier: write f(y) = sum_{r != 0} a_r * omega^{ry}. Then

    sum_y f(y) * conj(f(3y + alpha)) = p * sum_r a_r * conj(a_{3r}) * omega^{-r*alpha} * ...

Let me be more careful. f(3y + alpha) = sum_s a_s omega^{s(3y + alpha)} = sum_s a_s omega^{s*alpha} omega^{3sy}. So

    conj(f(3y + alpha)) = sum_s conj(a_s) omega^{-s*alpha} omega^{-3sy}.

The inner product:

    (1/p) sum_y f(y) conj(f(3y + alpha)) = sum_{r,s} a_r conj(a_s) omega^{-s*alpha} * (1/p) sum_y omega^{(r - 3s)y}
    = sum_s a_{3s} conj(a_s) omega^{-s*alpha}.

(The sum over y gives delta_{r, 3s}, so r = 3s.)

Therefore:

    <T_0 f, T_1 f> = sum_{s != 0} a_{3s} * conj(a_s) * omega^{-s*alpha}    ...(*)

where we use the convention that the subscripts are mod p (so a_s is the Fourier coefficient at frequency s, and a_{3s} is at frequency 3s mod p).

And ||f||^2 = sum_r |a_r|^2.

### C.4. Structure of the Optimization Problem

We need to minimize E(f, f)/||f||^2 = (1/2)(1 - Re(<T_0 f, T_1 f>)/||f||^2), so we need to MAXIMIZE:

    R(f) = Re[sum_{s != 0} a_{3s} conj(a_s) omega^{-s*alpha}] / [sum_r |a_r|^2].

By Cauchy-Schwarz (applied to the numerator as a bilinear form):

    |sum_s a_{3s} conj(a_s) omega^{-s*alpha}| <= (sum_s |a_{3s}|^2)^{1/2} * (sum_s |a_s|^2)^{1/2} = ||f||^2.

Equality requires a_{3s} = c * a_s * omega^{s*alpha} for all s, for some constant c with |c| = 1.

**This is a fixed-point equation on Fourier coefficients.** It says the Fourier spectrum is invariant under the map s -> 3s with a specific phase twist. Following the orbit s -> 3s -> 9s -> ..., we get:

    a_{3^k s} = c^k * a_s * omega^{s*alpha*(1 + 3 + ... + 3^{k-1})} = c^k * a_s * omega^{s*alpha*(3^k - 1)/2}.

When 3^L = 1 mod p (i.e., k = L), we need:

    a_s = c^L * a_s * omega^{s*alpha*(3^L - 1)/2} = c^L * a_s * omega^{0} = c^L * a_s.

So either a_s = 0 or c^L = 1. If c = omega^{2pi*m/L} for some integer m, then the constraint is satisfiable.

**But then: f(y) is supported on a SINGLE orbit of the map s -> 3s in Fourier space.** Let's say the orbit is O = {s, 3s, 9s, ..., 3^{L-1}s}. Then f(y) = sum_{k=0}^{L-1} a_{3^k s} omega^{3^k s * y}, and the Fourier coefficients on this orbit satisfy the recursion above.

In real space, f(3y + alpha) = sum_k a_{3^k s} omega^{3^k s (3y + alpha)} = sum_k a_{3^k s} omega^{3^k s alpha} omega^{3^{k+1} s y}.

Comparing with f(y) = sum_k a_{3^k s} omega^{3^k s y}:

the condition for R(f) = 1 is f(3y + alpha) = c_0 f(y) for |c_0| = 1, which by the Combined Theorem (Thm 15) implies f = 0 when c_0 = 1 (since this gives f constant under the translation y -> y + 3*alpha).

### C.5. Quantitative Improvement via Phase Decoherence

The key insight is that the phase factors omega^{-s*alpha} in (*) provide CANCELLATION when summed over different orbits.

Consider the case where f is supported on TWO orbits O_1, O_2 of s -> 3s. Then

    R(f) = Re[sum_{s in O_1} a_{3s} conj(a_s) omega^{-s*alpha} + sum_{s in O_2} a_{3s} conj(a_s) omega^{-s*alpha}] / ||f||^2.

Each orbit contribution is at most (sum_{s in O_i} |a_s|^2) in absolute value. If the two contributions have DIFFERENT phases, they partially cancel.

**The phase of each orbit's contribution:** For orbit O = {s, 3s, ..., 3^{L-1}s}, the Cauchy-Schwarz-saturating function has a_{3^k s} = c^k a_s omega^{...}, and the contribution has a specific phase depending on s and alpha. Different orbits have s values that are not related by powers of 3, so the phases omega^{-s*alpha} for different orbits are "independent."

**Quantitative bound (for functions on multiple orbits):**

If f has Fourier support on N >= 2 orbits, with the j-th orbit contributing energy E_j, then

    R(f) <= sum_j E_j * cos(phi_j) / sum_j E_j

where phi_j is the "phase" of the j-th orbit's Cauchy-Schwarz bound. This is maximized when all phi_j are equal, but the phases depend on the orbit representatives s_j and are generically equidistributed.

**When (p-1)/L is large** (many orbits), the phases become equidistributed, and the average cos(phi_j) is close to 0. This gives R(f) ~ 0 for "generic" functions, hence gap ~ 1/2.

**When (p-1)/L is small** (few orbits, i.e., L close to p-1), the number of orbits is (p-1)/L ~ 1, so f is essentially on a single orbit, and R(f) can be close to 1. This is the hard case.

**But wait:** Even for a SINGLE orbit, the phase factors omega^{-s*alpha} within the orbit provide phase decoherence. The Cauchy-Schwarz bound is only tight when the phases align perfectly, which requires the recursion a_{3s} = c*a_s*omega^{s*alpha} to be self-consistent over the full orbit.

**The self-consistency condition over one orbit of length L:**

    Product of phase factors: product_{k=0}^{L-1} c * omega^{3^k s * alpha} = c^L * omega^{s * alpha * (3^L - 1) / (3-1)}

For 3^L = 1 mod p: (3^L - 1)/2 = 0 mod p (if p | (3^L - 1)/2) or not. Since 3^L - 1 = 0 mod p and p >= 5 is odd, (3^L - 1)/2 is an integer multiple of p/2... no, 3^L - 1 is divisible by p but (3^L - 1)/2 need not be an integer mod p since we're working in Z/pZ.

More precisely, the self-consistency over the orbit requires c^L = 1 (already noted) and:

    a_{3^L s} = a_s, and the accumulated phase is omega^{s * alpha * sum_{k=0}^{L-1} 3^k} = omega^{s * alpha * (3^L - 1)/(3-1)}.

Since 3^L = 1 mod p, we have 3^L - 1 = 0 mod p, so (3^L - 1)/(3-1) = (3^L - 1)/2 = 0 mod p (here / is division in Z/pZ). Wait, 3^L - 1 = 0 mod p, and 3 - 1 = 2, so (3^L - 1)/2 = (3^L - 1) * 2^{-1} mod p = 0 * 2^{-1} = 0 mod p.

So the accumulated phase is omega^0 = 1. The self-consistency condition is just c^L = 1, which is trivially satisfiable.

**This means: for a function on a single orbit, the Cauchy-Schwarz bound CAN be saturated.** The ratio R(f) = 1 is achievable for functions on a single 3-orbit, and this corresponds exactly to the orbit-constant functions that achieve ||Mf|| = ||f||.

This is the known obstruction: the operator norm ||M||_op = 1, achieved by orbit-constant functions. The Combined Theorem says these aren't eigenfunctions, but they can have ||Mf|| = ||f|| while Mf != lambda*f.

### C.6. The Iterated Poincare Inequality

Since the one-step Poincare inequality gives gap >= (1/2)(1 - 1) = 0 (useless in the worst case), we try the TWO-STEP version:

    gap(M^2) >= (1/2)(1 - max_{f perp 1} Re<T_0^{(2)} f, T_1^{(2)} f> / ||f||^2)

where the two-step operators involve different affine maps. The key is that the two-step correlation involves maps with DIFFERENT translations, so the self-consistency condition changes.

From the paper: ||M^2 chi_r||^2 <= 3/8 + O(1/p^2) for all single characters. This means that for individual Fourier modes, the two-step contraction is at most sqrt(3/8) ~ 0.612 per step, which IS below 1/sqrt(2) ~ 0.707. But for SUPERPOSITIONS, the bound can approach 1 because orbit-constant functions still achieve ||M^2 f|| close to ||f||.

The obstacle is always the same: functions constant on orbits of the affine map y -> 3y + alpha avoid contraction at one step, and while M maps them to a DIFFERENT affine orbit structure, the two-step orbit-constant functions for the composite map can again approach ||M^2|| = 1.

### C.7. Functional Inequality Verdict

**The Poincare inequality approach is equivalent to the spectral gap computation.** It provides a clean variational characterization but faces the same fundamental obstacle: orbit-constant functions can make the one-step contraction arbitrarily close to 0, and while the Combined Theorem eliminates exact eigenvectors, the quantitative gap depends on how close the orbit structure can get to being an eigenvector.

The approach does, however, suggest a specific strategy: **bound the correlation <T_0 f, T_1 f> by decomposing f into orbit components and using the phase decoherence between orbits.** This is precisely the "energy coupling between cosets" mechanism identified in the session log.

---

## D. Transfer Matrix / Symbolic Dynamics Approach

### D.1. The Transfer Operator

For the n-step walk with binary string b = (b_1, ..., b_n) in {0,1}^n, the composed map is:

    T_b(x) = 2^{-n} * 3^w * x + d_b

where w = |b| (Hamming weight) and d_b is the translation (depending on the specific sequence, not just the weight).

The n-step operator in Fourier:

    M^n chi_r = sum_{w=0}^n c_w(r) * chi_{s_w}

where s_w = r * 2^{-n} * 3^w and c_w(r) = (1/2^n) sum_{|b|=w} omega^{r * d_b}.

### D.2. The Translation Sum as a Transfer Matrix

The coefficient c_w(r) involves d_b, the translation part. For a specific binary string b = (b_1, ..., b_n) with weight w, the translation is:

    d_b = sum_{i: b_i = 1} gamma * product_{j=i+1}^n m_{b_j}

where gamma = 2^{-1} and m_0 = 2^{-1}, m_1 = 3/2.

This has a recursive structure. Define the transfer matrix approach: process the bits b_1, ..., b_n from left to right, tracking the accumulated multiplicative factor and translation.

At step i, the state is (accumulated_multiplier, accumulated_translation), but the multiplier is 2^{-(n-i)} * 3^{w_remaining}... this gets complicated.

**A cleaner recursion:** Process from RIGHT to left. After processing b_n, ..., b_{n-k+1}, the accumulated map T_{b_n} o ... o T_{b_{n-k+1}} is an affine map with multiplier a_k and translation d_k.

The recursion: at step k+1, we prepend b_{n-k}:
- If b_{n-k} = 0: new map is T_{b_n} o ... o T_{b_{n-k}} with multiplier a_{k+1} = alpha * a_k and translation d_{k+1} = alpha * d_k.
- If b_{n-k} = 1: multiplier a_{k+1} = beta * a_k and translation d_{k+1} = beta * d_k + gamma.

The multiplier a_k = alpha^{k-w_k} * beta^{w_k} = 2^{-k} * 3^{w_k} where w_k = number of 1-bits in the last k positions.

The translation d_k satisfies:
- d_0 = 0
- d_{k+1} = alpha * d_k if b_{n-k} = 0
- d_{k+1} = beta * d_k + gamma if b_{n-k} = 1

### D.3. The Phase Sum Reinterpretation

For the coefficient c_w(r), we need to sum omega^{r * d_b} over all binary strings b of weight w. The phase r * d_b depends on the specific arrangement of bits, not just the weight.

**Key structural fact:** The sum c_w(r) is a product (or near-product) over the "segments" of the binary string. Specifically, the CDG (Chung-Diaconis-Graham) product identity gives:

    product_{k=0}^{n-1} cos(pi * r * 2^k * t) = ...

but our situation involves a mixture of ×2^{-1} and ×(3/2) rather than a single multiplier.

### D.4. Connection to Random Matrix Products

The transfer matrix for the symbolic dynamics is:

    L_r = (1/2) * [omega^0 * E_alpha   +   omega^{r*gamma} * E_beta]

where E_alpha is the "multiplication by alpha" operator on Fourier modes and E_beta * omega^{r*gamma} is the "multiplication by beta with phase" operator.

In the basis of Fourier modes {chi_s : s in r * H} (where H = <alpha, beta> = <2^{-1}, 3/2>), this is a K x K matrix (K = |rH|).

The spectral gap of M is determined by the SPECTRAL RADIUS of this K x K matrix. For K = p-1 (when <2,3> = F_p^*), this is a (p-1) x (p-1) matrix.

**Random matrix heuristic:** The phases omega^{r*gamma} for different modes act like "random" phases, making L_r behave like a random unitary times 1/2. The spectral radius of such a matrix is ~ 1/sqrt(2) (by the circular law for random contractions). This heuristic matches the numerical |lambda_2| ~ 1/sqrt(2) ~ 0.707.

### D.5. Making the Random Matrix Heuristic Rigorous

**Conjecture (Transfer matrix spectral bound).** Let K >= 2 and let P be a K x K matrix of the form:

    P = (1/2)(S_1 + D * S_2)

where S_1, S_2 are permutation matrices and D = diag(d_1, ..., d_K) with |d_j| = 1.

If the permutation S_2 S_1^{-1} is a single cycle of length K, and the phases d_j are "non-degenerate" (no resonance), then the spectral radius of P on the subspace orthogonal to the Perron vector is at most 1/sqrt(2) + O(1/K).

**Evidence:** For the Collatz operator, S_1 is the permutation r -> r*alpha = r/2 on the orbit, S_2 is r -> r*beta = 3r/2, and D has entries omega^{r_j * gamma}. When <2,3> = F_p^*, the permutation S_2 S_1^{-1} sends r -> r * beta/alpha = r * 3, which is a permutation of the orbit. This is a single cycle of length L = ord_p(3).

**Formal analysis for P = (1/2)(S_1 + D S_2):**

For v = (v_1, ..., v_K), (Pv)_j = (1/2)(v_{sigma_1(j)} + d_j * v_{sigma_2(j)}).

The eigenvalue equation Pv = lambda v gives:
    2 lambda v_j = v_{sigma_1(j)} + d_j * v_{sigma_2(j)}.

For a single character (v_j = omega_K^{mj} for some m), the eigenvalue is:
    2 lambda = omega_K^{m*sigma_1(j)}/omega_K^{mj} + d_j * omega_K^{m*sigma_2(j)}/omega_K^{mj}

But this depends on j unless sigma_1 and sigma_2 are translations (which they aren't in general).

### D.6. Kesten-McKay Type Bound

For the ADJACENCY MATRIX of a random d-regular graph, the spectral radius is ~ 2*sqrt(d-1) (Alon's conjecture / Friedman's theorem). Our operator P = (1/2)(S_1 + D*S_2) is an "almost random" 2-regular operator with phases.

The analogy: a random 2-regular bipartite graph with edge weights has spectral radius ~ sqrt(2) * (1/2) = 1/sqrt(2) per the Kesten-McKay law.

**More precisely:** For P = (1/2)(S_1 + D*S_2) where D has iid uniform phases:

    E[||P||_op^2] = E[||P^*P||_op] <= E[tr(P^*P)] / K = (1/4)(2 + 2*E[cos(...)]) ~ 1/2.

So the EXPECTED operator norm squared is 1/2, giving an expected per-step contraction of 1/sqrt(2). But we need a WORST-CASE bound over all primes p, not an expected bound.

### D.7. The Phase Decorrelation Argument

The most promising formal approach uses the structure of the phases.

**Claim:** For the Collatz walk on F_p, the phases omega^{r*gamma} for r in the orbit {s, s/2, s/4, ..., s*3, s*3/2, ...} are "pseudo-random" in the following sense:

For any two distinct elements r_1, r_2 of the orbit, the phase difference omega^{(r_1 - r_2)*gamma} is not 1 (since r_1 != r_2 and gamma != 0). Moreover, for orbits of size K >= 3, no two elements are "close" in the sense that |r_1 - r_2| * gamma is always bounded away from 0 mod p.

This "non-resonance" condition, if quantified, would give:

    |sum_{j=1}^K d_j * v_{sigma(j)} * conj(v_j)| <= (1 - delta) * sum |v_j|^2

for some delta > 0 depending on the non-resonance quality.

### D.8. Transfer Matrix Verdict

**The transfer matrix approach correctly identifies the mechanism:** the spectral gap comes from the PHASES introduced by the "+1" translation, which act as pseudo-random perturbations on the transfer matrix. Making this rigorous requires showing that these phases satisfy a "non-resonance" or "non-concentration" condition.

**The missing ingredient:** A rigorous bound showing that the phases {omega^{r*gamma} : r in orbit} are sufficiently "spread out" that the operator (1/2)(S_1 + D*S_2) has spectral radius at most 1/sqrt(2) + o(1). This is closely related to Bourgain's sum-product theorem and expander graph theory for solvable groups.

---

## E. The Most Promising Direction: A Hybrid Fourier-Expansion Argument

### E.1. Overview

The analysis above reveals that all four approaches (entropy, coupling, functional inequality, transfer matrix) ultimately reduce to the SAME algebraic core: bounding the correlation <T_0 f, T_1 f> for functions with Fourier support on a small number of orbits.

The most promising path combines:
1. **Fourier decomposition into orbits** (Section C)
2. **Phase decoherence between orbits** (Section C.5)
3. **Phase decoherence WITHIN a single orbit** (the transfer matrix approach, Section D)

### E.2. Formal Setup

Let H = <2, 3> <= F_p^* with |H| = K. The Fourier modes partition into orbits under multiplication by elements of H. Let O_1, ..., O_m be the orbits (m = (p-1)/K).

For f perp 1, write f = sum_{j=1}^m f_j where f_j = sum_{r in O_j} a_r chi_r.

The cross-term decomposes:

    <T_0 f, T_1 f> = sum_j <T_0 f_j, T_1 f_j> + sum_{j != k} <T_0 f_j, T_1 f_k>.

The CROSS-ORBIT terms <T_0 f_j, T_1 f_k> = 0 because T_0 and T_1 preserve orbits (they multiply by elements of H).

So: <T_0 f, T_1 f> = sum_j <T_0 f_j, T_1 f_j>.

Each term |<T_0 f_j, T_1 f_j>| <= ||f_j||^2 (Cauchy-Schwarz).

The RATIO: R(f) = sum_j R_j * E_j / sum_j E_j, where E_j = ||f_j||^2 and R_j = <T_0 f_j, T_1 f_j>/E_j.

This is a weighted average of the per-orbit ratios R_j.

### E.3. Per-Orbit Bound (the Key Lemma Needed)

**Key Claim (unproved).** For each orbit O with |O| = K:

    |<T_0 f_O, T_1 f_O>| <= (1 - delta(K)) * ||f_O||^2

where delta(K) -> some positive limit as K -> infinity.

If this claim holds with delta(K) >= delta_0 > 0 for all K >= 2 (or even K >= K_0 for some fixed K_0, since there are only finitely many primes with K < K_0), then:

    R(f) <= 1 - delta_0 for all f perp 1,

giving gap >= delta_0 / 2.

### E.4. Analysis of a Single Orbit

Fix an orbit O = {s_0, s_1, ..., s_{K-1}} where s_j = s_0 * g^j for some generator g of H. The function f_O = sum_{j=0}^{K-1} a_j chi_{s_j}.

From equation (*) in Section C.3:

    <T_0 f_O, T_1 f_O> = sum_{j} a_{sigma(j)} * conj(a_j) * omega^{-s_j * alpha}

where sigma is the permutation j -> j' such that 3 * s_j = s_{j'} (multiplication by 3 within the orbit).

This is a TWISTED inner product: <sigma^*(a), a>_{twist} where the twist is the diagonal matrix D = diag(omega^{-s_j * alpha}).

**The bound |<T_0 f_O, T_1 f_O>| = ||f_O||^2 requires:** a_{sigma(j)} = c * a_j * omega^{s_j * alpha} for all j, which defines a UNIQUE (up to scaling) function on the orbit. The question is: does this function exist? (Yes, it always does -- just define a_0 = 1 and propagate.) But does the Cauchy-Schwarz bound have a gap?

**Wait, there IS always an f_O saturating the bound.** Define a_0 = 1 and a_{sigma^k(0)} = c^k * omega^{sum_{m=0}^{k-1} s_{sigma^m(0)} * alpha}. Since |a_j| = |a_0| = 1 for all j, ||f_O||^2 = K, and |<T_0 f_O, T_1 f_O>| = K = ||f_O||^2.

**This means: the PER-ORBIT Cauchy-Schwarz bound is TIGHT.** There exists f_O on orbit O with |<T_0 f_O, T_1 f_O>| = ||f_O||^2.

**Conclusion: The per-orbit bound R_j <= 1 is tight for every orbit.**

This seems to kill the approach. BUT: the function f_O that saturates the bound is the ORBIT-CONSTANT function (constant modulus on the orbit with specific phases). And we know this function is NOT an eigenfunction of M (by the Combined Theorem). The issue is that Mf_O != lambda f_O even though ||Mf_O|| = ||f_O||.

### E.5. The Two-Step Escape

Since the one-step bound is tight on each orbit, we must go to TWO steps. The quantity to bound is:

    ||M^2 f||^2 / ||f||^2 for f perp 1.

We have ||M^2 f||^2 = ||M(Mf)||^2 = (1/2)||Mf||^2 + (1/2)Re<T_0(Mf), T_1(Mf)>.

If Mf is NOT the orbit-saturating function (even if f was), then <T_0(Mf), T_1(Mf)> < ||Mf||^2, giving contraction at the second step.

**The key question: if f saturates the one-step bound (||Mf|| = ||f||), how far is Mf from saturating the bound at the NEXT step?**

When ||Mf|| = ||f||, we have Mf = (1/2)T_0 f + (1/2)T_1 f where T_0 f and T_1 f are on the same orbit but with different phase patterns. For Mf to ALSO saturate the bound, we'd need Mf to be an orbit-constant function for the SAME map y -> 3y + alpha. But Mf has a DIFFERENT structure from f:

Mf(x) = (1/2)f(x/2) + (1/2)f((3x+1)/2). Even if f is "orbit-constant" in the Fourier sense, Mf is a SUPERPOSITION that generically is not orbit-constant.

**The crux:** After one step of M, the orbit-constant function becomes a non-orbit-constant function, and the non-orbit-constant part provides genuine contraction at the second step.

### E.6. Quantifying the Two-Step Contraction

**Setting up the two-step bound:**

Let f be the worst-case function at step 1 (the orbit-constant function on some orbit O). Then ||Mf||^2 = ||f||^2. Write Mf = g. We need to bound ||Mg||^2/||g||^2.

Now g = Mf = (1/2)T_0 f + (1/2)T_1 f. In Fourier:
- T_0 f has Fourier coefficients: (T_0 f)^(s) = a_{2s} (multiplication by 2)
- T_1 f has Fourier coefficients: (T_1 f)^(s) = omega^{s*gamma} * a_{(2/3)*s}... wait let me recompute.

T_0(x) = x/2. So T_0 f(x) = f(x/2) = sum_r a_r omega^{r*x/2} = sum_r a_r chi_{r/2}(x) = sum_r a_r chi_{r*alpha}(x).

In terms of Fourier coefficients at mode s: (T_0 f)^(s) = a_{s/alpha} = a_{2s} (since alpha = 1/2).

T_1(x) = (3x+1)/2. So T_1 f(x) = f((3x+1)/2) = sum_r a_r omega^{r*(3x+1)/2} = sum_r a_r omega^{r*gamma} omega^{r*beta*x} where gamma = 1/2, beta = 3/2.

In terms of Fourier coefficients at mode s: (T_1 f)^(s) = a_{s/beta} * omega^{(s/beta)*gamma} = a_{(2/3)*s} * omega^{(2s/3)*(1/2)}.

Wait, let me be more careful. f(x) = sum_r a_r omega^{rx}. Then

    T_1 f(x) = f(beta*x + gamma) = sum_r a_r omega^{r*(beta*x + gamma)} = sum_r a_r omega^{r*gamma} omega^{r*beta*x}
             = sum_r [a_r omega^{r*gamma}] chi_{r*beta}(x).

So the Fourier coefficient of T_1 f at mode s is: look for r*beta = s, i.e., r = s/beta = s*2/3. So (T_1 f)^(s) = a_{s*2/3} * omega^{(s*2/3)*gamma}.

(Note: all multiplications are in F_p.)

Therefore, g = Mf has Fourier coefficients:

    g^(s) = (1/2)*a_{2s} + (1/2)*a_{(2s)/3} * omega^{(2s/3)*(1/2)}
           = (1/2)*a_{2s} + (1/2)*omega^{s/3} * a_{2s/3}

Hmm, let me re-index. For the orbit O = {s_0, s_0*2^{-1}, s_0*3*2^{-1}, ...} = {s_0 * h : h in H}. In the orbit indexing, let the elements be {r_0, r_1, ..., r_{K-1}}.

The map T_0: r_j -> r_j * alpha (= r_j / 2) corresponds to a permutation pi_0 on the orbit.
The map T_1: r_j -> r_j * beta (= r_j * 3/2) corresponds to a permutation pi_1 on the orbit.

The Fourier coefficients of g = Mf at mode r_j are:

    g^(r_j) = (1/2)*a_{pi_0^{-1}(r_j)} + (1/2)*omega^{pi_1^{-1}(r_j)*gamma} * a_{pi_1^{-1}(r_j)}

where pi_0^{-1}(r_j) = r_j * 2 (the mode that maps TO r_j under T_0) and pi_1^{-1}(r_j) = r_j * 2/3 (the mode that maps to r_j under T_1).

This is a matrix equation: g = P * a, where P is the K x K matrix:

    P_{j, pi_0^{-1}(j)} += 1/2
    P_{j, pi_1^{-1}(j)} += (1/2) * omega^{r_{pi_1^{-1}(j)} * gamma}

This is exactly the transfer matrix from Section D.

### E.7. The Transfer Matrix Spectrum as the Spectral Gap

We've now reduced the problem to:

**Find the spectral radius of the K x K matrix P, where**

    P = (1/2) * Pi_0 + (1/2) * D * Pi_1

**Pi_0 is the permutation matrix for r -> r*2 on the orbit, Pi_1 is the permutation matrix for r -> r*(2/3) on the orbit, and D is the diagonal matrix with D_{jj} = omega^{r_j * (2/3) * gamma} = omega^{r_j / 3}.**

(Here I'm using pi_1^{-1}(r_j) = r_j * 2/3, and the phase is omega^{(r_j*2/3)*gamma} = omega^{r_j*2/3*2^{-1}} = omega^{r_j/3}.)

**The operator P can be written as:**

    P = (1/2) Pi_0 (I + Pi_0^{-1} D Pi_1)

where Pi_0^{-1} D Pi_1 maps the j-th basis vector to the pi_0(pi_1^{-1}(j))-th basis vector with phase omega^{r_{pi_1^{-1}(j)}/3}. The composite permutation pi_0 o pi_1^{-1} sends r -> 2r * (2/3)^{-1} = 2r * 3/2 = 3r. So this is the multiplication-by-3 permutation with a diagonal phase.

Therefore: P = (1/2) Pi_0 (I + D' * Pi_3) where Pi_3 is the multiplication-by-3 permutation and D' is a diagonal phase matrix.

The spectral radius of P (ignoring the eigenvalue 1 from the stationary vector):

    rho(P) = (1/2) * rho(I + D' Pi_3) on the non-trivial subspace.

Now rho(I + D' Pi_3) depends on the eigenvalues of D' Pi_3. If D' Pi_3 has all eigenvalues with |lambda| = 1 (it's a product of a unitary diagonal and a permutation, hence unitary), then its eigenvalues are on the unit circle. The eigenvalues of I + D' Pi_3 are {1 + mu_k} where mu_k are eigenvalues of D' Pi_3.

The maximum |1 + mu| for |mu| = 1 is 2 (when mu = 1) and the minimum is 0 (when mu = -1).

So rho(I + D' Pi_3) = max_k |1 + mu_k|. For the trivial eigenvalue (if any), mu = 1 gives |1 + mu| = 2, hence rho(P) >= 1 for that eigenvector. But this corresponds to the stationary distribution.

For the non-trivial eigenvalues:

    rho(P)_{non-triv} = (1/2) max_{mu != 1} |1 + mu|.

Since |mu| = 1, we have |1 + mu| = 2|cos(theta/2)| where mu = e^{i*theta}. The maximum is achieved at the smallest |theta| (closest to 0 but not at 0).

**This is exactly the Chung-Diaconis-Graham insight!** The spectral gap of the walk is determined by how close the eigenvalues of D' Pi_3 get to 1, which is determined by the Fourier analysis of the phase function on the orbit of multiplication by 3.

### E.8. Computing the Eigenvalues of D' Pi_3

The matrix D' Pi_3 acts on the orbit O = {r_0, r_0*3, r_0*9, ..., r_0*3^{L-1}} (where L = ord_p(3), assuming the orbit is a single 3-cycle; in general it decomposes into several 3-orbits).

For a single 3-cycle of length L: label the elements as r_0, r_1 = 3r_0, ..., r_{L-1} = 3^{L-1}r_0.

Then Pi_3 sends r_j to r_{j+1 mod L}. The diagonal D' has entries d_j at position r_j.

The eigenvalues of D' Pi_3 are the eigenvalues of the "twisted cyclic shift." For a cyclic shift with periodic phases, the eigenvalues are:

    mu_m = omega_L^m * (product_{j=0}^{L-1} d_j)^{1/L} * ...

Actually, for a twisted cyclic shift C_d where (C_d v)_j = d_j * v_{j-1}, the eigenvalues are:

    mu_m = (product_{j=0}^{L-1} d_j)^{1/L} * omega_L^m    for m = 0, ..., L-1

where omega_L = e^{2pi*i/L}. Wait, this is only correct when all d_j are equal. In general:

The eigenvalues of the matrix
    A = diag(d_0, d_1, ..., d_{L-1}) * CyclicShift

are the L-th roots of det(A) times the L-th roots of unity... no, that's not right either.

The correct eigenvalues: A = D * S where S is the cyclic shift (S e_j = e_{j+1 mod L}) and D = diag(d_0, ..., d_{L-1}).

The characteristic polynomial of D*S is: det(lambda I - D S).

For a general twisted shift, the eigenvalue equation (DS)v = mu*v gives:
    d_j * v_{j-1} = mu * v_j  =>  v_j = (d_j / mu) * v_{j-1}

Iterating: v_L = (product d_j / mu^L) * v_0 = v_0 (periodicity).

So: product_{j=0}^{L-1} d_j = mu^L.

Therefore: mu = (product d_j)^{1/L} * omega_L^m for m = 0, ..., L-1.

The product of phases is: product d_j = product_{j=0}^{L-1} omega^{r_j / 3} = omega^{(1/3) * sum r_j}.

Now sum r_j = r_0 * (1 + 3 + 9 + ... + 3^{L-1}) = r_0 * (3^L - 1)/(3 - 1) = r_0 * (3^L - 1)/2.

Since 3^L = 1 mod p: 3^L - 1 = 0 mod p, so sum r_j = 0 mod p, hence product d_j = omega^0 = 1.

**Therefore: the eigenvalues of D' Pi_3 on a single 3-cycle of length L are EXACTLY the L-th roots of unity: {1, omega_L, omega_L^2, ..., omega_L^{L-1}}.**

**WAIT.** This is a remarkable result. Let me double-check.

The eigenvalues of the twisted cyclic shift D*S where D = diag(d_0, ..., d_{L-1}) are the L-th roots of prod d_j. We computed prod d_j = 1. So the eigenvalues are {omega_L^m : m = 0, ..., L-1} -- exactly the L-th roots of unity!

This means the eigenvalues of I + D' Pi_3 are {1 + omega_L^m : m = 0, ..., L-1}, and:

    |1 + omega_L^m| = 2|cos(pi*m/L)|.

The maximum for m != 0 is at m = 1: |1 + omega_L| = 2*cos(pi/L).

Therefore:

    rho(P)_{non-triv} = (1/2) * 2 * cos(pi/L) = cos(pi/L).

And the spectral gap is:

    gap = 1 - cos(pi/L) = 2 sin^2(pi/(2L)) ~ pi^2/(2L^2) for large L.

**HOLD ON.** This gives gap ~ 1/L^2 ~ 1/p^2 for L ~ p. This is WORSE than the known 1/p bound!

### E.9. Where the Computation Goes Wrong

Let me re-examine. The issue is that the orbit O under H = <2, 3> may NOT be a single 3-cycle. The orbit under <2, 3> has size K = |H|, while the 3-cycles within it have length L = ord_p(3). The orbit decomposes into K/L copies of 3-cycles, each also carrying a 2-structure.

More importantly, the matrix P acts on the FULL orbit, not just a single 3-cycle. The matrix P = (1/2)(Pi_0 + D Pi_1) where Pi_0 is multiplication by 2 and Pi_1 is multiplication by 3/2 (with phases). The orbit under <2, 3> has a richer structure than a single cyclic shift.

Let me reconsider. The orbit under <2, 3> can be decomposed into cosets of <3>:

    O = C_0 ∪ C_1 ∪ ... ∪ C_{K/L - 1}

where C_i = r_i * <3> are 3-orbits. The multiplication by 2 maps between cosets (since 2 is not in <3> when <2,3> is strictly larger than <3>).

The transfer matrix P acts on this orbit. The multiplication-by-2 permutation maps elements BETWEEN 3-cosets, creating a structure that mixes the cosets.

The eigenvalues of P depend on this inter-coset mixing. The earlier computation (eigenvalues = roots of unity) only applies within a single 3-coset, but the multiplication-by-2 COUPLES the cosets.

**The correct computation requires diagonalizing the full K x K matrix P.** The earlier E.8 computation was for a simplified model where the orbit is a single 3-cycle, which occurs only when <2> <= <3> (i.e., 2 is a power of 3 mod p).

### E.10. The Full Transfer Matrix (Corrected)

For general primes, let L_2 = ord_p(2), L_3 = ord_p(3), K = |<2,3>|. The orbit O under <2,3> has size K, decomposing into K/L_3 cosets of <3>, each of size L_3.

Label the elements of O as r_{i,j} where i indexes the 3-coset (i = 0, ..., K/L_3 - 1) and j indexes within the coset (j = 0, ..., L_3 - 1), with r_{i,j} = r_{i,0} * 3^j.

Multiplication by 3 acts WITHIN each coset: r_{i,j} -> r_{i,j+1 mod L_3}.

Multiplication by 2 acts BETWEEN cosets: r_{i,j} -> r_{i',j'} where r_{i,j} * 2 = r_{i',j'}.

The transfer matrix P couples modes across cosets via the multiplication-by-2 structure AND adds phases via the "+1" translation.

The spectral gap of P is the spectral gap of the original Markov operator M on this orbit.

**This is the full problem restated at the orbit level.** The transfer matrix approach has successfully decomposed the p-1 dimensional problem into (p-1)/K independent K-dimensional problems (one per orbit), but each K-dimensional problem has the same complexity.

### E.11. Small Orbit Case: K Fixed, p -> infinity

When the index (p-1)/K is large (K is bounded as p -> infinity), each orbit has bounded size, and the transfer matrix is bounded-dimensional. The spectral radius of a bounded-dimensional matrix with |lambda| < 1 for all eigenvalues (by the Combined Theorem) gives a gap bounded away from 0 by compactness.

**Proposition.** If K = |<2,3>| <= K_0 for some fixed K_0, then |lambda_2(p)| <= 1 - c(K_0) for a constant depending only on K_0.

*Proof.* The transfer matrix P is K x K with K <= K_0. By the Combined Theorem, all eigenvalues of P (except the trivial one) satisfy |mu| < 1. Since P depends on p only through the phases d_j = omega^{r_j/3}, which are p-th roots of unity, and the permutation structure, the matrix P varies over a compact set (as a function of the phases). The eigenvalues are continuous functions of the matrix entries, so |mu|_{max} < 1 achieves a maximum strictly less than 1 on this compact set... UNLESS the limit point (as p -> infinity) has an eigenvalue at 1.

But the limit point would correspond to all phases being 1 (as p -> infinity, omega^{r_j/3} -> 1 for bounded r_j... except r_j is NOT bounded, it's an element of F_p). The phases omega^{r_j/3} for r_j in the orbit are (K-th) roots of unity in some sense... actually no, they are p-th roots of unity at positions r_j/3, where r_j ranges over a K-element subset of F_p^*.

For K fixed and p -> infinity, the phases omega^{r_j/3} for j = 1, ..., K become equidistributed on the unit circle (by Weyl equidistribution, since r_j/3 mod p is equidistributed in Z/pZ). In this limit, the matrix P approaches a random K x K contraction, whose spectral radius is 1/sqrt(2) by the random matrix heuristic.

But equidistribution is not guaranteed for EVERY sequence of primes. For specific primes, the phases could cluster.

**Still, for bounded K, the compactness argument gives gap >= c(K_0) > 0, even without understanding the phases.** This is because the Combined Theorem shows |mu| < 1 for ALL phase configurations, and the space of phase configurations is compact (unit circle^K), and the function |mu|_{max} is continuous, so it achieves its maximum at some point, and this maximum is < 1.

*QED.*

### E.12. Large Orbit Case: K -> infinity with p

When K = |<2,3>| grows with p (e.g., K = p-1), the compactness argument breaks down because we're dealing with matrices of growing dimension.

**This is where the Bourgain-Gamburd machinery would be needed.** For growing dimension, one needs either:
1. Random matrix universality results (but our matrices are deterministic)
2. Explicit non-concentration estimates (Bourgain-style)
3. Expansion properties of the Cayley graph of <2,3> in F_p^*

### E.13. A Potential New Result: Intermediate Bound |lambda_2| <= 1 - c/sqrt(p)

**Claim.** By combining the per-step contraction ||Mchi_r||^2 = 1/2 with the orbit structure, one can potentially prove:

    |lambda_2| <= 1 - c/sqrt(p)

for an absolute constant c > 0. This improves the known 1 - c/p bound.

**Argument sketch:**

From Proposition 3.3 in the paper, ||M^n chi_r||^2 <= ceil((n+1)/L) * C(2n,n)/4^n.

Taking n = ceil(sqrt(p)):
- C(2n,n)/4^n ~ 1/sqrt(pi*n) ~ 1/p^{1/4}
- ceil((n+1)/L) <= n+1 ~ sqrt(p) (worst case L = 1, but L >= 2 always)

So ||M^n chi_r||^2 <= C * sqrt(p) / p^{1/4} = C * p^{1/4}.

This is > 1 for large p, so it doesn't give a bound.

Let me try n = C*L instead. With n = C*L:
- C(2n,n)/4^n ~ 1/sqrt(pi*C*L)
- ceil((n+1)/L) = C + 1

So ||M^n chi_r||^2 <= (C+1)/sqrt(pi*C*L).

For this to be < 1: need L > (C+1)^2/(pi*C). For C = 4: need L > 25/(4*pi) ~ 2. This works for L >= 2.

So |lambda_2|^{2n} <= (C+1)/sqrt(pi*C*L) for n = C*L.

But the OPERATOR NORM is not just the norm on individual characters; we need to handle superpositions.

**For superpositions within an orbit of size K:** By Proposition 3.3, the bound applies to each character individually, and by Cauchy-Schwarz across the orbit, the operator norm satisfies:

    ||M^n||_{op}^2 <= K * max_r ||M^n chi_r||^2

No wait, that's too crude. The correct bound comes from the orbit decomposition in the paper:

    ||M^n f_O||^2 <= K * (C+1)/sqrt(pi*C*L) * ||f_O||^2

for n = C*L, where f_O is supported on orbit O of size K.

If K = p-1 (full orbit), this gives ||M^n||_{op}^2 <= (p-1) * (C+1)/sqrt(pi*C*L), which is >> 1.

The issue: for superpositions within a large orbit, the Cauchy-Schwarz bound loses a factor of K (the orbit size).

**A better bound for superpositions:** Instead of using Cauchy-Schwarz on the orbit, use the Hilbert-Schmidt norm:

    ||M^n||_{HS}^2 = sum_r ||M^n chi_r||^2 <= (p-1) * max_r ||M^n chi_r||^2

But ||M^n||_{op} <= ||M^n||_{HS}, and the latter is sqrt((p-1) * max ||M^n chi_r||^2). This gives:

    |lambda_2|^{2n} <= ||M^n||_{op}^2 <= (p-1) * (C+1)/sqrt(pi*C*L)

For n = C*L: |lambda_2|^{2CL} <= (p-1)(C+1)/sqrt(pi*C*L).

Taking logs: 2CL * log(1/|lambda_2|) >= log(sqrt(pi*C*L)) - log((p-1)(C+1)).

For L ~ p: this gives 2Cp * log(1/|lambda_2|) >= (1/2)*log(p) - log(p) < 0. Fails.

For L bounded: 2CL * log(1/|lambda_2|) >= (1/2)*log(L) - log(p). Need L >= log(p) at least. So: log(1/|lambda_2|) >= (log(log p) - log p) / (2C*log p) < 0. Also fails.

**Diagnosis:** The Hilbert-Schmidt bound loses a factor of (p-1) which is too large. The operator norm is NOT controlled by the HS norm in a useful way.

### E.14. The Missing Ingredient (Identified)

The fundamental gap in all approaches is:

**We can show each character contracts (||Mchi_r||^2 = 1/2), and we can show no function is an exact fixed point (Combined Theorem). But we cannot control the OPERATOR NORM because different characters can CONSTRUCTIVELY INTERFERE under M, and the interference is governed by the orbit structure.**

Specifically, the operator norm on a single orbit of size K can approach 1 because the K characters on the orbit can be combined with phases that make the M-image nearly as large as the input. The constructive interference comes from the "+1" phases aligning for a specific function.

To prove a constant spectral gap, one would need ONE of the following:

1. **Phase decoherence within orbits:** Show that for ANY function on an orbit, the phases of the M-image cannot ALL be aligned. This requires controlling the structure of the "+1" phases within the orbit, which is related to the Gauss sum / exponential sum structure.

2. **Two-step non-return:** Show that if f achieves ||Mf|| close to ||f||, then Mf is "far" from the set of functions that also achieve near-equality. This would give ||M^2f|| << ||f||.

3. **Multi-orbit mixing:** Show that the orbit-constant functions that maximize ||Mf|| on individual orbits are INCOMPATIBLE across different orbits, so that the worst-case f for the full operator has non-trivial cross-orbit structure that provides contraction.

4. **Expansion via sum-product:** Use Bourgain's sum-product theorem to show that the Cayley graph of the affine group generated by {T_0, T_1} is an expander. This is the Bourgain-Gamburd approach, specialized to solvable groups.

### E.15. The Most Viable Path: Eigenvalue Spacing of Twisted Cyclic Shifts

From Section E.8, we showed that the eigenvalues of D' Pi_3 on a single 3-cycle are the L-th roots of unity (when the orbit is a single 3-cycle). More generally, for the full orbit, the eigenvalues of the "3-part" of the transfer matrix are related to the representation theory of the orbit under <2,3>.

The spectral gap is:

    gap = 1 - (1/2) max_{mu != 1} |1 + mu|

where mu ranges over eigenvalues of D' Pi_3 (on the full orbit) that are NOT equal to 1.

If we can show that all eigenvalues mu != 1 of D' Pi_3 satisfy |1 + mu| <= 2 - delta for some delta > 0, this gives gap >= delta/2.

Now, |1 + mu| <= 2 - delta is equivalent to saying mu is bounded away from 1 on the unit circle: |mu - 1| >= delta' for some delta' > 0.

**For the single 3-cycle case:** The eigenvalues are L-th roots of unity, and the closest to 1 (for mu != 1) is omega_L, with |omega_L - 1| = 2 sin(pi/L). So delta' = 2 sin(pi/L) ~ 2pi/L.

This gives gap ~ (1/2)(2 - 2cos(pi/L)) = 2sin^2(pi/(2L)) ~ pi^2/(2L^2).

**For L fixed:** This gives a constant gap (depending on L). Combined with the compactness argument of E.11, we get a constant gap whenever L is bounded.

**For L -> infinity:** The gap decays as 1/L^2, which is WORSE than the known 1/p bound (since L <= p-1).

**BUT WAIT: the single 3-cycle computation in E.8 assumed the orbit is a single 3-cycle. For the FULL orbit under <2, 3>, the matrix P couples multiple 3-cosets via multiplication by 2.** The inter-coset coupling via ×2 may IMPROVE the eigenvalue spacing.

Specifically, multiplication by 2 provides a "random-walk-like" coupling between different 3-cosets, which can lift the near-1 eigenvalues away from 1. This is exactly the "energy coupling between cosets" mechanism identified in the session log.

**The quantitative question is:** Does the inter-coset coupling via ×2 improve the eigenvalue gap from ~1/L^2 (single coset) to a CONSTANT (independent of L and p)?

This is a problem about the spectral gap of a random walk on a graph formed by the cosets of <3> within <2,3>, with edges given by multiplication by 2 and phases from the "+1" translation.

### E.16. Summary of Key Findings

1. **The problem reduces to a finite-dimensional transfer matrix** on each orbit of <2,3> in F_p^*.

2. **For bounded orbits (|<2,3>| <= K_0)**, a constant spectral gap follows from compactness + the Combined Theorem. This is a genuine new result (though for most primes, orbits are large).

3. **For single 3-cycles**, the eigenvalues of the transfer matrix are exactly L-th roots of unity, giving gap ~ 1/L^2. The inter-coset coupling via ×2 is what provides the improvement to (conjecturally) a constant gap.

4. **The mechanism is:** multiplication by 2 mixes energy between different 3-cosets, preventing eigenvectors from concentrating on a single coset. The "+1" phases provide the asymmetry that breaks the eigenvalue 1.

5. **The formal proof of a constant gap requires:** showing that the inter-coset graph (3-cosets connected by ×2) has a constant expansion property, uniformly in p. This is a problem about the Cayley graph of the quotient group <2,3>/<3> with generator "2 mod <3>".

---

## F. New Result: Conditional Constant Gap Under a Multiplicative Order Hypothesis

### F.1. Statement

**Theorem (Conditional).** Assume that for all primes p >= 5, ord_p(3) >= C * log(p)^2 for some absolute constant C. Then there exists delta > 0 such that |lambda_2(p)| <= 1 - delta for all p >= 5.

### F.2. Proof

Under the hypothesis, L = ord_p(3) >= C log(p)^2.

**Step 1.** By Proposition 3.3 of the paper with n = 4L:

    ||M^n chi_r||^2 <= 5/sqrt(4*pi*L) for all r != 0.

**Step 2.** For a general function f perp 1, f = sum_r a_r chi_r with sum |a_r|^2 = 1.

    ||M^n f||^2 = ||sum_r a_r M^n chi_r||^2.

The vectors M^n chi_r for different r are NOT orthogonal (they can overlap at the same Fourier modes when 3^w r_1 = 3^{w'} r_2 for different starting modes r_1, r_2).

However, characters from DIFFERENT orbits of <2,3> have disjoint Fourier supports after applying M^n. So the cross-orbit terms vanish:

    ||M^n f||^2 = sum_{O} ||M^n f_O||^2

where f_O is the projection of f onto orbit O.

**Step 3.** For each orbit O of size K: ||M^n f_O||^2 <= ??

The bound from Proposition 3.3 applies to individual characters within O. For a superposition f_O = sum_{r in O} a_r chi_r:

    M^n f_O = sum_{r in O} a_r sum_{w=0}^n c_w(r) chi_{r*2^{-n}*3^w}.

The modes r*2^{-n}*3^w for different r in the same orbit can coincide. Specifically, r_1 * 2^{-n} * 3^{w_1} = r_2 * 2^{-n} * 3^{w_2} iff r_1 * 3^{w_1} = r_2 * 3^{w_2}, which happens when r_1/r_2 = 3^{w_2 - w_1} and this ratio is in <3>. Since r_1, r_2 are in the same <2,3>-orbit, r_1/r_2 is a product of powers of 2 and 3. So r_1/r_2 is in <3> iff r_1 and r_2 are in the same <3>-coset within the <2,3>-orbit.

The number of <3>-cosets within the orbit is K/L. For modes from DIFFERENT <3>-cosets, the output Fourier modes are disjoint (they land on different <3>-cosets of the output orbit). So:

    ||M^n f_O||^2 = sum_{coset C} ||M^n f_C||^2

where f_C = sum_{r in C} a_r chi_r is the projection onto <3>-coset C.

**Step 4.** For each <3>-coset C of size L within orbit O:

    ||M^n f_C||^2 = sum_{j=0}^{L-1} |sum_{w in C_j} sum_{r in C} a_r c_w(r)|^2

where C_j = {w : 0 <= w <= n, w = j mod L} and the sum over r in C has all terms landing on the same Fourier mode.

By Cauchy-Schwarz (same as Proposition 3.3):

    ||M^n f_C||^2 <= ceil((n+1)/L) * sum_w |sum_r a_r c_w(r)|^2

Now, within a single weight w, sum_r a_r c_w(r) involves different characters r from the same coset (all related by powers of 3). But c_w(r) = (1/2^n) sum_{|b|=w} omega^{r * d_b}. For r and r' = 3*r in the same coset:

    c_w(r') = (1/2^n) sum_{|b|=w} omega^{3r * d_b}

which is the same Gauss-sum-like object but with a different character. These are NOT simply related to c_w(r).

**Step 5 (Crude bound).** By Cauchy-Schwarz on the sum over r:

    |sum_r a_r c_w(r)|^2 <= (sum_r |a_r|^2) * (sum_r |c_w(r)|^2) = ||f_C||^2 * sum_r |c_w(r)|^2

And sum_w sum_r |c_w(r)|^2 <= L * max_r sum_w |c_w(r)|^2 <= L * C(2n,n)/4^n.

So: ||M^n f_C||^2 <= ceil((n+1)/L) * L * ||f_C||^2 * C(2n,n)/4^n = (n+1) * ||f_C||^2 * C(2n,n)/4^n.

Wait, that loses a factor of L. Let me redo:

    ||M^n f_C||^2 <= ceil((n+1)/L) * sum_w ||f_C||^2 * max_r |c_w(r)|^2 * |C| ...

Actually I'm double-counting. Let me use the operator norm directly.

For a single coset C of size L, the restriction of M^n to the span of {chi_r : r in C} is an L x (n+1)-rank operator (at most n+1 output modes). The operator norm satisfies:

    ||M^n|_C||_{op}^2 <= max_{r in C} ||M^n chi_r||^2 * L

by the triangle inequality on the L characters. But this gives an L factor.

Actually, a better bound: since the output modes from different weights w are orthogonal (when they're distinct), we have:

    ||M^n f_C||^2 = sum_{distinct s} |sum_{w: s_w=s} sum_{r in C} a_r c_w(r)|^2.

For modes from different residue classes mod L: they map to different output modes. For modes within the same residue class: they collide. By Cauchy-Schwarz on the collision:

    sum_{j} |sum_{w in C_j} sum_r a_r c_w(r)|^2 <= ceil((n+1)/L) * sum_w |sum_r a_r c_w(r)|^2.

Now sum_w |sum_r a_r c_w(r)|^2. The inner sum sum_r a_r c_w(r) is a single number for each w. Using the Cauchy-Schwarz bound |sum_r a_r c_w(r)|^2 <= ||f_C||^2 * sum_r |c_w(r)|^2:

Hmm, but sum_r |c_w(r)|^2 for fixed w is not bounded by C(n,w)^2/4^n unless we use the triangle inequality on c_w(r).

Actually, by Lemma 3.1, |c_w(r)| <= C(n,w)/2^n for each r. So:

    |sum_r a_r c_w(r)| <= sum_r |a_r| * C(n,w)/2^n <= sqrt(L) * ||a||_2 * C(n,w)/2^n = sqrt(L) * ||f_C|| * C(n,w)/2^n

(using Cauchy-Schwarz with |C| = L terms).

Therefore:

    sum_w |sum_r a_r c_w(r)|^2 <= L * ||f_C||^2 * sum_w C(n,w)^2/4^n = L * ||f_C||^2 * C(2n,n)/4^n.

And:

    ||M^n f_C||^2 <= ceil((n+1)/L) * L * ||f_C||^2 * C(2n,n)/4^n ~ (n+1) * ||f_C||^2 / sqrt(pi*n).

With n = 4L: ||M^n f_C||^2 <= (4L+1) * ||f_C||^2 / sqrt(4*pi*L) ~ 4*sqrt(L/pi) * ||f_C||^2.

For L >= 20: 4*sqrt(L/pi) >= 4*sqrt(20/pi) ~ 10. So ||M^n f_C||^2 can be >> ||f_C||^2.

**This is the operator norm blowup: the L factor from Cauchy-Schwarz on the coset kills the bound.**

**Step 6 (Using the hypothesis L >= C*log(p)^2).** Take n = c*p (a constant fraction of p) instead of n = 4L.

    ||M^n chi_r||^2 <= ceil((n+1)/L) * C(2n,n)/4^n.

With n = c*p and L >= C*log(p)^2: ceil((n+1)/L) <= cp/(C log(p)^2) + 1 ~ cp/(C log(p)^2).

And C(2n,n)/4^n ~ 1/sqrt(pi*n) = 1/sqrt(pi*c*p).

So: ||M^n chi_r||^2 <= cp/(C log(p)^2 * sqrt(pi*c*p)) = c*sqrt(p)/(C*log(p)^2*sqrt(pi*c)).

For large p, this is >> 1. Still blows up.

The problem is that the ceiling factor ceil((n+1)/L) grows as n/L, while the binomial coefficient only decays as 1/sqrt(n). We need n/L << sqrt(n), i.e., sqrt(n) << L.

With n = L^2: ceil((n+1)/L) ~ L, and C(2n,n)/4^n ~ 1/sqrt(pi*L^2) = 1/(sqrt(pi)*L).

So ||M^n chi_r||^2 <= L * 1/(sqrt(pi)*L) = 1/sqrt(pi) < 1. This works!

Then |lambda_2|^{2L^2} <= 1/sqrt(pi), giving |lambda_2| <= (1/sqrt(pi))^{1/(2L^2)} = 1 - log(sqrt(pi))/(2L^2) + ... ~ 1 - c/L^2.

For L >= C*sqrt(p): this gives |lambda_2| <= 1 - c/p, recovering the known bound.

For L >= C*p^{1/2+epsilon}: |lambda_2| <= 1 - c/p^{1-2*epsilon}, a slight improvement.

**Under the hypothesis L >= C*log(p)^2:** |lambda_2| <= 1 - c/log(p)^4, which is a CONSTANT gap (tends to 1 but very slowly). Actually, 1 - c/log(p)^4 -> 1 as p -> infinity, so this is NOT a constant gap.

Hmm. Let me reconsider.

With n = L^2 and L = omega(1):

    |lambda_2|^{2L^2} <= 1/sqrt(pi) < 1.

This gives |lambda_2| <= (1/sqrt(pi))^{1/(2L^2)} = exp(-log(sqrt(pi))/(2L^2)).

For this to give |lambda_2| <= 1 - delta: need L^2 <= log(sqrt(pi))/(2*delta), i.e., L <= sqrt(c/delta).

So for L >= L_0 (any fixed L_0): |lambda_2| <= 1 - c/L_0^2. But L_0 grows with p (L <= p-1), so this doesn't give a universal constant.

**The ceiling factor and the binomial coefficient decay always give a POLYNOMIAL relationship between n and L, leading to gap ~ 1/L^{something}.** To get a constant gap, we'd need EXPONENTIAL cancellation in the c_w(r) coefficients (not just the trivial bound |c_w(r)| <= C(n,w)/2^n) or a method that avoids the Cauchy-Schwarz loss entirely.

### F.3. Verdict on the Conditional Result

The conditional theorem as stated CANNOT be proved by the paper's method alone, even with a hypothesis on ord_p(3). The method inherently gives gap ~ 1/L^k for some k, which is never constant unless L is bounded.

The only genuine constant-gap result from the current framework is for **bounded orbit size** (Section E.11), which applies to a sparse set of primes.

---

## G. What Would Complete the Proof: A Precise Statement of the Missing Lemma

### G.1. The Core Missing Result

**Missing Lemma (Phase Cancellation in Colliding Modes).** Let p >= 5 be prime, L = ord_p(3), and r != 0 mod p. For the Collatz walk coefficients

    c_w(r) = (1/2^n) sum_{b in {0,1}^n, |b| = w} omega^{r * d_b(p)}

where d_b is the translation part of the composed affine map, and for two weights w, w' with L | (w - w'):

    |c_w(r) + c_{w'}(r)| <= (1 - eta) * (|c_w(r)| + |c_{w'}(r)|)

for some eta > 0 independent of p, L, r, n, w, w'.

In words: when two weight classes collide on the same Fourier mode (because 3^w = 3^{w'} mod p), their contributions PARTIALLY CANCEL due to the different translation terms d_b. The phases omega^{r * d_b} for strings of weight w and weight w' = w + L are different (because the translation depends on the position of the 1-bits, not just their count), and this difference produces cancellation.

### G.2. Why This Would Suffice

If the Missing Lemma holds, replace Cauchy-Schwarz in Proposition 3.3 with the improved bound:

    |sum_{w in C_j} c_w(r)|^2 <= (1 - eta)^2 * (sum_{w in C_j} |c_w(r)|)^2 <= (1 - 2*eta + eta^2) * |C_j| * sum |c_w(r)|^2

The key improvement: we REMOVE the ceiling factor from the bound, or at least reduce it from ceil((n+1)/L) to a bounded constant.

Actually, more precisely: if colliding coefficients always cancel by a factor (1-eta), then for m collisions:

    |sum of m terms|^2 <= (1-eta)^{2(m-1)} * m * sum |c_w|^2

instead of Cauchy-Schwarz's m * sum |c_w|^2. For m = ceil((n+1)/L) and n = 4L: m = 5, and the improvement is (1-eta)^8, a constant. This gives:

    ||M^n chi_r||^2 <= 5 * (1-eta)^8 / sqrt(4*pi*L)

which has the SAME L-dependence as before. Not good enough.

### G.3. A Stronger Missing Lemma

What we actually need:

**Strong Phase Cancellation Lemma.** For colliding weights w_1, w_2, ..., w_m (with w_{j+1} = w_j + L for each j), the SUM of their contributions satisfies:

    |sum_{j=1}^m c_{w_j}(r)|^2 <= C_0 * max_j |c_{w_j}(r)|^2

for an absolute constant C_0 (independent of m, L, p, r). That is, the sum of m terms has magnitude comparable to a SINGLE term, not sqrt(m) times a term.

This would give ||M^n chi_r||^2 <= C_0 * max_w |c_w(r)|^2 / sqrt(pi*n), which for n = O(1) gives an O(1) bound, hence a constant spectral gap.

### G.4. Evidence for the Strong Lemma

The coefficients c_w(r) for different w values have phases determined by the translation sums d_b, which depend heavily on the positions of the 1-bits. For weights w and w + L, the strings of weight w + L have L additional 1-bits compared to weight-w strings. These extra 1-bits contribute additional "+1" translations at various positions, creating UNCORRELATED phase shifts.

**Heuristic model:** If the phases omega^{r * d_b} were independently and uniformly distributed on the unit circle, then:

    c_w(r) ~ C(n,w)/2^n * (Gaussian with stddev 1/sqrt(C(n,w)))

by the central limit theorem. For two "independent" such Gaussians:

    |c_{w_1} + c_{w_2}|^2 ~ |c_{w_1}|^2 + |c_{w_2}|^2  (no constructive interference on average)

This would give the Strong Lemma with C_0 ~ 2 (or slightly larger).

**However:** The phases are NOT independent. They are structured by the affine dynamics. The CDG product identity shows that along a SINGLE 2-orbit, the phases multiply to give exactly 2^{-L}. This suggests correlations that could cause constructive interference.

### G.5. Connection to the CDG Product Identity

Recall the CDG identity: for the orbit {b, 2b, 4b, ...} mod p,

    product_{j=0}^{L_2-1} cos(pi*b*2^j/p) = +/- 2^{-L_2}

where L_2 = ord_p(2).

The MAGNITUDE of each cos factor varies, but their product is exactly 2^{-L_2}. This means some factors are large (cos ~ 1, when b*2^j is near 0 mod p) and some are small (cos ~ 0, when b*2^j is near p/2).

For the coefficients c_w(r), the analogous statement would involve products of cosines along MIXED orbits (involving both ×2 and ×3 steps). The CDG-type identity constrains the product of all such cosines, but individual terms can vary.

**Crucial point:** The CDG identity gives the GEOMETRIC mean of |cos| as exactly 1/2 per step. But the spectral gap is related to the ARITHMETIC mean (or worst-case) of |c_w|^2. By AM-GM: the arithmetic mean >= geometric mean, but this goes the wrong way for us (we want the arithmetic mean to be small).

### G.6. The Actual Gap: Quantitative Phase Decoherence

Here is what a proof would look like, if it existed:

**Theorem (Hypothetical).** For every prime p >= 5, |lambda_2(p)| <= 1/sqrt(2) + O(p^{-delta}) for some delta > 0.

**Proof Strategy:**

1. **Reduce to a single orbit.** The spectral gap is the minimum over orbits O of <2,3> of the spectral gap of M restricted to span{chi_r : r in O}.

2. **Model the restricted operator as a random unitary perturbation.** On orbit O of size K, the operator M acts as P = (1/2)(Pi_0 + D*Pi_1) where Pi_0 and Pi_1 are permutation matrices and D is a diagonal phase matrix.

3. **Use the Weyl equidistribution theorem** (or an effective version) to show that the phases {d_j} in D are equidistributed on the unit circle for "generic" orbits.

4. **Apply a spectral bound for permutation-plus-phase operators.** For P = (1/2)(Pi_0 + D*Pi_1) with equidistributed phases, the spectral radius of P on the non-trivial subspace is at most 1/sqrt(2) + o(1).

Step 4 is the non-trivial step. It would follow from a result like:

**Claim.** Let S_1, S_2 be permutations of [K] and D = diag(e^{i*theta_1}, ..., e^{i*theta_K}). If the angles theta_j are delta-separated (|theta_i - theta_j| > delta for i != j), then

    rho((1/2)(S_1 + D*S_2) - (1/K)*J) <= 1/sqrt(2) + C/delta.

This claim would follow from a variant of Bourgain's sum-product theorem applied to the phase structure.

**Status:** This claim is OPEN. It is a specific instance of the general question of spectral gaps for affine random walks on solvable groups, which is at the frontier of additive combinatorics.

---

## H. Conclusions and Recommended Next Steps

### H.1. Summary of Findings

| Approach | Result | Constant gap? | Why it fails/what's missing |
|----------|--------|---------------|---------------------------|
| Entropy/Info Theory | Reduces to same spectral problem | No (alone) | Cross-correlation <T_0 f, T_1 f> is the same bottleneck |
| Standard Coupling | Multiplicative difference, never 0 | No | Fundamental algebraic obstruction |
| Non-standard Coupling | Adds perturbation, but O(1/p) meeting prob | No | Can't beat O(p) coupling time |
| Poincare / Dirichlet | Variational characterization, CS tight per orbit | No (alone) | Orbit-constant functions saturate the bound |
| Transfer Matrix | Eigenvalues of D'Pi_3 = L-th roots of unity | Only for bounded orbits | Eigenvalue spacing ~ 1/L for large L |
| Hybrid (inter-coset mixing) | Identifies the mechanism | Open | Needs expansion for solvable groups |

### H.2. Genuine New Results

1. **Theorem (Bounded orbit constant gap).** For any fixed K_0, there exists c(K_0) > 0 such that if |<2,3>| <= K_0 in F_p^*, then |lambda_2(p)| <= 1 - c(K_0). (Follows from compactness + Combined Theorem.)

2. **Observation (Transfer matrix eigenvalue structure).** The eigenvalues of the "3-component" of the transfer matrix on a single 3-cycle of length L are exactly the L-th roots of unity. The spectral gap is therefore controlled by the inter-coset coupling via multiplication by 2.

3. **Precise identification of the missing ingredient.** The constant spectral gap would follow from showing that the inter-coset graph (3-cosets connected by ×2, weighted by "+1" phases) has a constant expansion property. This is a specific instance of Bourgain-Gamburd expansion for solvable groups.

### H.3. Recommended Next Steps

1. **Numerically verify the inter-coset expansion.** For each prime p, compute the spectrum of the transfer matrix P on the full <2,3>-orbit and decompose the eigenvalues by their "inter-coset" and "intra-coset" components. Check whether the inter-coset coupling via ×2 lifts the near-1 eigenvalues away from 1.

2. **Study the Chung-Diaconis-Graham model.** The CDG paper [6] analyzes x -> 2x + b on Z/pZ, which is a closely related affine walk. Their spectral gap analysis may provide techniques adaptable to our setting.

3. **Pursue the Bourgain sum-product approach.** Specifically, try to prove: for P = (1/2)(Pi_0 + D*Pi_1) on an orbit of size K with generic phases, rho(P) <= 1/sqrt(2) + o(1). This is a clean linear algebra / additive combinatorics problem.

4. **Explore the two-step operator M^2 more carefully.** Instead of bounding ||M^2||_op (which approaches 1), try to bound the spectral radius directly by analyzing the EIGENVALUES of M^2 on each orbit. The two-step operator mixes the 3-coset structure in a specific way that may be analyzable.

5. **Consider the random walk in the affine group.** Rather than working on Z/pZ, study the induced walk on Aff(F_p) directly. The affine group has additional structure (semidirect product) that may enable Bourgain-Gamburd type arguments, despite being solvable.

6. **Revisit Hildebrand's framework.** Hildebrand (1993) analyzed walks of the form X_{n+1} = a_n X_n + b_n mod p, which is precisely our setting. His results give spectral bounds depending on the "spread" of the multiplier distribution. For our walk, the multiplier is {2^{-1}, 3*2^{-1}} (two-point support), and Hildebrand's bounds are typically of the form gap ~ 1/ord_p(ratio), which gives gap ~ 1/L -- the same order as the paper's bound. However, Hildebrand's method may be improvable for the specific case where the two multipliers generate a large subgroup of F_p^*.

---

## I. Addendum: Verification of the Key Transfer Matrix Computation

### I.1. The Eigenvalue = Roots-of-Unity Claim (Section E.8)

In Section E.8, I claimed that the eigenvalues of D' Pi_3 on a single 3-cycle of length L are exactly the L-th roots of unity. Here I verify this carefully.

**Setup.** Consider the orbit of r_0 under multiplication by 3 in F_p^*: O = {r_0, 3r_0, 9r_0, ..., 3^{L-1}r_0} where L = ord_p(3). Label these as r_j = 3^j r_0 for j = 0, ..., L-1.

The matrix D' Pi_3 acts on a vector v = (v_0, v_1, ..., v_{L-1}) as:

    (D' Pi_3 v)_j = d_j * v_{sigma(j)}

where sigma(j) is the index such that r_{sigma(j)} * 3 = r_j, i.e., sigma(j) = j-1 mod L (since 3 * r_{j-1} = r_j). And d_j = omega^{r_j / 3} = omega^{r_{j-1}} (since r_j/3 = 3^{j-1} r_0 = r_{j-1}).

Wait -- let me recompute. We have d_j = omega^{r_j / 3}. Now r_j = 3^j r_0, so r_j / 3 = 3^{j-1} r_0 = r_{j-1} (for j >= 1) and r_0 / 3 = 3^{-1} r_0 = 3^{L-1} r_0 = r_{L-1}. So d_j = omega^{r_{j-1 mod L}}.

The eigenvalue equation (D' Pi_3)v = mu v gives:

    omega^{r_{j-1}} * v_{j-1} = mu * v_j    for all j (indices mod L).

This gives v_j = (omega^{r_{j-1}} / mu) * v_{j-1}, so iterating:

    v_j = v_0 * prod_{k=0}^{j-1} omega^{r_k} / mu^j = (v_0 / mu^j) * omega^{sum_{k=0}^{j-1} r_k}.

The periodicity condition v_L = v_0 gives:

    v_0 / mu^L * omega^{sum_{k=0}^{L-1} r_k} = v_0

    mu^L = omega^{sum_{k=0}^{L-1} r_k}.

Now sum_{k=0}^{L-1} r_k = r_0 * sum_{k=0}^{L-1} 3^k = r_0 * (3^L - 1) / (3 - 1) = r_0 * (3^L - 1) / 2.

Since 3^L = 1 mod p, we get 3^L - 1 = 0 mod p, so sum_{k=0}^{L-1} r_k = 0 mod p, hence omega^{sum r_k} = 1.

Therefore mu^L = 1, confirming that the eigenvalues are exactly the L-th roots of unity.

### I.2. Implications

This means the "intra-coset" spectral structure is completely determined: the eigenvalues are L-th roots of unity, equally spaced on the unit circle. The closest non-trivial eigenvalue to 1 is e^{2*pi*i/L}, at distance 2*sin(pi/L) from 1.

For the full transfer matrix P = (1/2)(Pi_0 + D Pi_1):
- P has a block structure aligned with the 3-cosets
- The "intra-coset" part has eigenvalues related to L-th roots of unity
- The "inter-coset" coupling via Pi_0 (multiplication by 2) creates hybridization between 3-cosets
- This hybridization is what determines whether the spectral gap is constant or decays with p

The analogy: think of the 3-cosets as "sites" and the ×2 map as "hopping" between sites. Each site has internal modes (the L-th roots of unity). The near-1 eigenvalues (mu close to 1) correspond to slowly varying modes on the 3-cycle. The ×2 hopping mixes these modes, potentially lifting them away from 1.

Whether this "band structure" argument gives a constant gap is equivalent to whether the ×2 hopping between 3-cosets has a constant conductance -- a precise graph-theoretic question about the Cayley graph of F_p^* / <3> with generator 2*<3>.
