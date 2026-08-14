# Chief Audit — Round 3

Date: 2026-08-14

## Decision

**Round 3 contains two useful mathematical advances, but the researcher’s `GO for R4` is premature as written.**

I classify the round as **CONDITIONAL PASS / R3 closure required at the start of R4**. No extra numbered research round is needed: the repairs below are Phase 0 of Round 4. The manuscript remains frozen until Phase 0 and the R4 testing theorem both pass.

The two advances that survive are:

1. a valid high-frequency obstruction showing that state-threshold safety alone does not control input energy when no actuator/bandwidth restriction is imposed;
2. a useful constructive latent-approximation hierarchy, but currently only as **candidate upper errors**, not exact values of the best approximation `E_m`.

Several load-bearing claims require correction before they can feed the headline R4 theorem.

---

## P0.1 — `E_m` was not computed

The round defines

\[
E_m=\inf_{k_m\in\mathcal K_m}\|k_\alpha-k_m\|_{L^1(0,T)},
\]

but `compute_round3.py` does **not** solve that infimum. It searches only the two free truncation parameters `(ell,L)` of the specific left-node T9b construction; its weights and nodes remain locked by that construction.

Therefore the reported numbers such as `0.1347` at `m=32` are valid **constructive candidate errors** and hence upper bounds on the true infimum, but they are not `E_m` itself.

Use notation such as

\[
\bar E_m^{\rm LN}\ge E_m
\]

or `candidate_error_m`.

I independently re-integrated the displayed candidates with adaptive quadrature. The reported grid values are conservative by roughly 0.3--2% in the checked range, so the numerical candidates themselves are credible; the issue is their interpretation, not their numerical scale. See `chief_round3_checks.json`.

---

## P0.2 — Frozen rate window conflicts with the claimed arbitrary-tolerance collapse

The frozen class is declared with

\[
\lambda_j\in[10^{-3},10].
\]

However, the manuscript T9b arbitrary-tolerance construction obtains convergence by sending the low-rate truncation `ell` toward zero and the high-rate truncation `L` outward as the requested tolerance shrinks. That construction is **not contained in a permanently fixed rate window for arbitrary tolerance**.

Thus the sentence saying that the manuscript’s explicit `m(eps)` can be used for any tolerance inside the frozen class is false.

R4 Phase 0 must choose one coherent option:

### Option A — expanding nested rate windows (preferred for the complexity-collapse theorem)

Define a nested hierarchy

\[
\mathcal K_m=
\left\{\sum_{j=1}^m c_j e^{-\lambda_jt}:c_j\ge0,\;\lambda_j\in[\ell_m,L_m],\;\text{mass/coupling constraint}\right\},
\]

with `ell_m` nonincreasing and `L_m` nondecreasing, chosen so the T9b approximants belong to the hierarchy and the hierarchy remains nested.

### Option B — fixed window

Keep `[10^-3,10]`, but then **do not claim `E_m -> 0` from T9b**. Treat the paper as a finite-complexity / finite-window result and prove only the quantitative bounds actually available for the declared `m` range.

The two options cannot be mixed.

---

## P0.3 — The latent class still lacks a genuine coupling/normalization bound

The R3 prompt required normalization/coupling restrictions to make the common-safe rival class mathematically meaningful. The response says `c_j` are free in `[0,infinity)`. That is not a bound.

For a common-safe definition over the full latent hierarchy, unrestricted positive weights/couplings can make the rival’s ecological response arbitrarily large; this can trivialize the common-safe set or decouple the kernel approximation class from the benchmark latent model.

R4 Phase 0 must freeze a coupling/mass normalization, e.g. a declared bound on an appropriate kernel mass / DC gain / ecological coupling, and prove that the constructive T9b competitors satisfy it. The exact choice must match the latent realization used in the discrimination theorem.

---

## P0.4 — The common-safety benchmark rival set is not the `K_m` hierarchy

The round explicitly acknowledges that `latent1/latent3` from `benchmark/bench.py` are **not members of the frozen kernel class `K_m`**. Consequently the numerical worst-case safety constant over

`{ODE, Caputo, DDE, latent1, latent3}`

cannot be inserted directly into a theorem whose inner adversary is `L in L_m` built from `K_m`.

This is a model-class mismatch.

For R4, either:

- derive safety using the same latent hierarchy appearing in the KL infimum; or
- use a necessary bound coming from focal-model safety plus the actuator cap, which remains valid because every common-safe input is in particular safe for the focal model.

Do not call the five benchmark simulators the “full rival family” for the R4 theorem.

---

## P0.5 — R3b-pos repeats the Round-2 direction problem in one-sided form

Strong-Allee safety is a **one-sided floor**:

\[
x^*+(H_xu)(t)\ge A+\eta.
\]

The researcher instead uses

\[
\|H_xu\|_\infty\le\rho_\eta
\]

through `kappa = ||H_x u0||_infty/||u0||_2`, which is a stronger symmetric condition. It gives a sufficient safe ball; it does **not** imply that every one-sided-safe input obeys `||u||_2 <= rho/kappa`.

For a positive fixed-shape ray `u=c u0`, `c>=0`, define the downward gain

\[
d_M(u_0)=\frac{\max_t[-H_{x,M}u_0(t)]_+}{\|u_0\|_2},
\qquad
d_{\rm rob}=\sup_M d_M.
\]

Then common one-sided safety implies the correct necessary bound

\[
\boxed{\|u\|_2\le \rho_\eta/d_{\rm rob}.}
\]

If both signs of `c` are allowed, positive and negative rays require separate extrema; the absolute maximum is not the correct coercivity constant.

I recomputed the benchmark-rival diagnostic with this one-sided formula. At `A=0.25`, the positive pulse-ray bound is about `0.3357` rather than `0.3135`. These are still numerical diagnostics, not certificates for the full `K_m` hierarchy.

---

## P0.6 — The actuator cap was compared using the wrong energy cap for fixed shapes

The universal implication

\[
\|u\|_2\le\sqrt{T}u_{\max}
\]

is valid but loose. For a fixed shape `u=c u0`, the actual peak-amplitude constraint gives

\[
\|u\|_2\le
u(u_0):=u_{\max}\frac{\|u_0\|_2}{\|u_0\|_\infty}.
\]

For the released benchmark shapes at `T=12`:

- pulse: shape-specific cap is about `0.12`, not `0.3464`;
- multiscale: about `0.1545`, not `0.3464`.

Therefore the claim that the Allee-coercive bound is already the binding constraint at `A=0.25` or `A=0.30` is false for the actual fixed-shape protocols under the existing peak cap. My corrected diagnostic shows the Allee bound begins to compete with the peak cap only closer to the stability boundary (around `A≈0.32` for the locked benchmark rival set at `alpha=0.85`).

This is scientifically useful: the atlas should include this crossover rather than hiding it.

---

## P0.7 — The parameterized-dictionary singular-value calculation is wrong

The code normalizes dictionary columns individually and then interprets

`svdvals(K @ Mhat).min()`

as

\[
\inf_{u\in\operatorname{span}M,\|u\|_2=1}\|Ku\|_2.
\]

That is incorrect unless the columns form an orthonormal basis. The dictionaries are highly redundant / rank deficient, so the near-`1e-15` singular values mostly measure coefficient non-identifiability, not a physical null direction of the input-output operator.

I recomputed the restriction after orthonormalizing the actual input span. Correct values at the focal cell are approximately:

| family | numerical rank | corrected restricted `s_min` |
|---|---:|---:|
| sinusoid | 21 | 0.0532 |
| multisine | 13 | 0.1441 |
| chirp | 11 | 0.0997 |
| PRBS | 15 | 0.2840 |

So the statement that the finite dictionaries contain machine-zero null directions is rejected.

These `L2->L2` singular values still do **not** by themselves solve one-sided Allee safety; they are only a correction of the linear-algebra claim.

---

## P1.1 — R3b-neg is correct in substance but its proof should be repaired

The negative theorem is valuable:

> with state-threshold safety alone and no actuator/bandwidth restriction, the safe input energy is unbounded for the strictly proper fractional prey channel.

The current proof jumps from a frequency-domain asymptotic to a uniform finite-horizon `L-infinity` decay using “integration by parts”. Because the Caputo impulse kernel is singular at zero, that step needs care.

A cleaner proof needs only `h_x in L1(0,T)` and the **uniform Riemann--Lebesgue lemma for indefinite Fourier integrals**:

\[
\sup_{t\le T}\left|\int_0^t h_x(r)e^{-i\omega r}\,dr\right|\to0.
\]

For unit-energy normalized `sin(omega t)`, the output sup norm therefore tends to zero. Scaling each input by `rho/(2 delta_omega)` remains symmetrically safe while its `L2` norm diverges. This proves the theorem without claiming an `O(omega^{-alpha})` uniform rate. The observed `eps^alpha` trend can remain a numerical diagnostic only.

I recommend using this proof in R4.

---

## P1.2 — T9b constants are currently too loose for a useful testing number

At the displayed tuned candidates, the analytic T9b upper bounds remain around `13--20` even when the directly integrated candidate errors are around `0.1--0.9`. The bound is mathematically valid but extremely conservative because its triangle estimate discards large cancellations.

A formal R4 minimum-error theorem can use symbolic `Ebar_m`, but a **numerically persuasive Q1 result** will need one of:

1. a tighter analytic kernel-error upper bound; or
2. a validated numerical `L1` certificate for the explicitly frozen exponential mixture.

Do not advertise a quantitative classification impossibility from the current T9b numbers unless the final bound is non-vacuous.

---

## Independent computations performed by the chief

`chief_round3_checks.py` reproduces the following without rerunning the factorial benchmark:

- adaptive-quadrature checks of every displayed kernel candidate;
- corrected span-restricted singular values using an orthonormal basis;
- one-sided downward gains for positive pulse/multiscale rays;
- shape-specific actuator-energy caps.

Outputs are in `chief_round3_checks.json` and `chief_round3_checks_output.txt`.

The research diagnostic figure has been regenerated as `round3_diagnostic_CHIEF_CORRECTED.pdf` with corrected labels and the one-sided / shape-cap comparison. No manuscript figure was changed.

---

## Gate decision

**R3 researcher verdict: GO — rejected as written.**

**Chief verdict: CONDITIONAL PASS.** Start R4 with a mandatory short closure phase, then continue directly into the testing theorem; do not create a separate Round 3.5.

R4 may proceed only after it freezes one coherent latent hierarchy that simultaneously defines:

- the approximation adversary in `E_m` / KL;
- the ecological latent realization;
- the coupling/mass bounds;
- the common-safe set.

The manuscript remains frozen until the R4 theorem survives this closure.
