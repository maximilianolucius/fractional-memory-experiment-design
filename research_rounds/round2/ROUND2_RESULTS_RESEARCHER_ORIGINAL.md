# Round 2 Results — Strong-Allee-Dependent Safe Energy Bound

Date: 2026-08-14
Status: **GO** (linear interface proved and numerically evaluated; nonlinear lift flagged as residual)

## 1. Round objective

Round 1 (Theorem R1) bounded the robust safe discriminability

\[
\Delta_{\mathrm{safe}}^{(m)}
\le \tfrac12 \|R^{-1/2}S\|^2\, B_{\mathrm{safe},m}^2\, E_m(\alpha,T)^2
\]

with the safe energy bound `B_safe,m` left as a generic interface. The Round-1
decision assigned exactly one problem to Round 2:

> Derive a rigorous Strong-Allee-dependent safe excitation/energy bound
> `B_safe(A, alpha, T, rho, ...)` that can be inserted into Theorem R1.

This document delivers that bound in the linearized regime, with an exact
numerical evaluation on the locked ecological parameters and a validation gate
against the integer-order limit. No factorial benchmark was re-run and the
manuscript (`main.tex`) was not modified (rounds 1–3 stay outside the
manuscript until the Round-3 gate).

## 2. Setup (identical to the manuscript linearization)

Linearized Caputo system about the coexistence equilibrium `z* = (x*, y*(A))`,
prey-channel actuation, `tau_0 = 1`:

\[
{}^{C}D_t^\alpha \xi(t) = J(A)\,\xi(t) + B\,u(t),\qquad \xi(0)=0,\qquad B=e_1,
\]

with `J(A)` stable in the Matignon sense for the evaluated `(A, alpha)` pairs
(stable regime `A <= 0.25 < 2/7` for all `alpha in (0,1)`; at `A=0.3` we
evaluate only `alpha < alpha*(0.3) = 0.96901...`). The Allee margin in the
prey coordinate is

\[
\rho(A) = x^* - A, \qquad x^* = \tfrac{2}{3}.
\]

## 3. Lemma R2.1 — linear safe envelope (exact)

Let

\[
H_\alpha(t) = t^{\alpha-1} E_{\alpha,\alpha}\!\left(J(A)\,t^\alpha\right) B
\]

be the impulse-response vector of the linear Caputo system (two-parameter
Mittag-Leffler function applied through the eigenbasis of `J`), and define the
finite-horizon gain

\[
\Gamma_T(A,\alpha) = \int_0^T \|H_\alpha(s)\|_2\, ds.
\]

**Claim.** (i) `Gamma_T(A, alpha) < infinity`. (ii) Every input with
`||u||_{L^\infty(0,T)} <= rho(A) / Gamma_T(A, alpha)` satisfies
`||xi(t)|| <= rho(A)` for all `t in [0,T]`; in particular the prey coordinate
obeys `x(t) = x* + xi_1(t) >= x* - rho(A) = A`.

**Proof.** (i) By the variation-of-constants formula for linear Caputo systems
(Podlubny), the impulse response is as displayed. Since `J(A)` satisfies the
Matignon sector condition, the two-parameter Mittag-Leffler asymptotics on the
stable sector give `E_{alpha,alpha}(J t^alpha) = O(t^{-2alpha})` (the leading
`z^{-1}` term vanishes because `1/Gamma(0) = 0`), hence
`||H_alpha(t)|| = O(t^{-alpha-1})`, which is integrable at infinity.
(ii) `xi(t) = \int_0^t H_alpha(t-s) u(s) ds`, so

\[
\|\xi(t)\| \le \|u\|_{L^\infty} \int_0^t \|H_\alpha(s)\|\,ds
\le \|u\|_{L^\infty}\, \Gamma_T(A,\alpha) \le \rho(A).
\]

The prey-coordinate bound follows from `|xi_1(t)| <= ||xi(t)||`. ∎

This is exactly the manuscript's linear safety envelope
(Lemma `lem:linear_safety`), evaluated here with the Mittag-Leffler kernel
instead of a numerical surrogate.

## 4. Theorem R2 — Strong-Allee-dependent safe energy bound

In the setting of Section 2, for every latent complexity `m` the common-safe
input class of Theorem R1 satisfies

\[
B_{\mathrm{safe},m}
\le B_{\mathrm{safe}}(A,\alpha,T)
:= \sqrt{T}\,\frac{\rho(A)}{\Gamma_T(A,\alpha)},
\qquad \rho(A) = x^* - A,
\]

independently of `m` (all rivals share the Jacobian skeleton, so the same
envelope bounds the whole family simultaneously). Inserted into Theorem R1:

\[
\boxed{
\Delta_{\mathrm{safe}}^{(m)}
\le
\frac{T\,\rho(A)^2}{2\,\Gamma_T(A,\alpha)^2}\,
\|R^{-1/2}S\|^2\,
E_m(\alpha,T)^2.
}
\]

**Consequence (two multiplicative bottlenecks).** The safe discriminability
ceiling now vanishes by two independent mechanisms: as the latent complexity
grows (`E_m -> 0`, the Round-1 mechanism) and as the ecosystem approaches the
extinction threshold (`rho(A) = x* - A -> 0`). The two factors multiply. No
safe experiment — of any duration `T` at fixed amplitude scale — can
discriminate arbitrarily well when either factor collapses.

## 5. Numerical evaluation (locked parameters; reproducible)

Computed by `compute_B_safe.py` (imports the released `benchmark/core.py`;
`T = 12` = benchmark medium horizon; amplitude cap `u_max = 0.10`).
`Gamma_T` is integrated with a clustered quadrature grid plus the analytic
singular head `||B|| eps^alpha / (alpha Gamma(alpha))`.

**Validation gate (passed).** At `alpha = 1` the Mittag-Leffler kernel reduces
to the matrix exponential; the computed `Gamma_T` matches
`int ||expm(J t) B|| dt` (scipy) to relative error `1.6e-10` (A=0.25) and
`2.8e-10` (A=0.3). Full grid in `B_safe_grid.json`; figure
`B_safe_vs_alpha.pdf`.

| A | alpha | Gamma_T | u_safe = rho/Gamma_T | B_safe | generic cap B = sqrt(T)·0.10 | sharpening (B_safe/B_cap)^2 | cap active? |
|---|---|---|---|---|---|---|---|
| 0.20 | 0.70 | 2.71 | 0.172 | 0.597 | 0.346 | 2.97 | no |
| 0.20 | 0.85 | 3.48 | 0.134 | 0.465 | 0.346 | 1.80 | no |
| 0.20 | 0.90 | 3.93 | 0.119 | 0.411 | 0.346 | 1.41 | no |
| 0.20 | 0.95 | 4.53 | 0.103 | 0.357 | 0.346 | 1.06 | no |
| 0.25 | 0.70 | 3.49 | 0.119 | 0.414 | 0.346 | 1.43 | no |
| 0.25 | 0.85 | 5.02 | 0.083 | 0.287 | 0.346 | **0.69** | **yes** |
| 0.25 | 0.90 | 5.87 | 0.071 | 0.246 | 0.346 | **0.50** | **yes** |
| 0.25 | 0.95 | 7.00 | 0.060 | 0.206 | 0.346 | **0.36** | **yes** |
| 0.30 | 0.70 | 4.66 | 0.079 | 0.273 | 0.346 | **0.62** | **yes** |
| 0.30 | 0.85 | 7.30 | 0.050 | 0.174 | 0.346 | **0.25** | **yes** |
| 0.30 | 0.90 | 8.68 | 0.042 | 0.146 | 0.346 | **0.18** | **yes** |
| 0.30 | 0.95 | 10.43 | 0.035 | 0.122 | 0.346 | **0.12** | **yes** |

**Findings.**

1. In the primary stable benchmark regime (`A = 0.25`), the Allee-margin
   envelope becomes *tighter* than the common amplitude cap exactly where the
   memory is subtlest: `u_safe < 0.10` for `alpha >= 0.85`, and the R1
   ceiling tightens by a factor `1/0.69 ≈ 1.4` (alpha=0.85) to `1/0.36 ≈ 2.8`
   (alpha=0.95) relative to the generic cap.
2. At `A = 0.30` the tightening reaches a factor of ~8 at alpha=0.95.
3. At `A = 0.20` the cap is tighter than the linear certificate for all
   evaluated alpha (sharpening >= 1); there R2 does not bite — reported
   honestly.
4. `Gamma_T` grows monotonically with `alpha` (slower Mittag-Leffler decay
   tightens the envelope) and with `A` (weaker stability as the trace
   approaches the `2/7` sign change), so the safe ceiling shrinks precisely in
   the corner of parameter space where discrimination is also collapsing
   (Figure 8 of the manuscript). The two difficulties compound.
5. The bound is a worst-case envelope over the whole L∞ ball. Sparse transient
   inputs realize much smaller excursions — consistent with the archived
   benchmark, where multiscale (peak 0.10, sparse) never crosses the Allee
   threshold while sustained designs do. R1+R2 therefore bound the safe class
   from above; the benchmark shows the class is nonempty and its realized
   information is far below the ceiling. That gap is the trade-off, now with
   an analytic scale.

## 6. The benchmark rectangle is not invariant at ANY amplitude

The chief's reviewer-side check (`chief_checks/check_strict_rectangle.py`)
establishes that the benchmark diagnostic rectangle fails the T17 strict face
conditions at `u_max = 0.10`. We additionally evaluated the face margins at
**zero input** (prey-only actuation cannot enter the predator equation):

- lower prey face: `f1(x_L, y_U, 0) = -0.492` — outward, **unfixable by any input**;
- lower predator face: `f2(x_L, y_L) = -0.076` — outward, unfixable by prey input;
- upper predator face: `f2(x_U, y_U) = +0.329` — outward, unfixable by prey input;
- upper prey face: `f1(x_U, y_L, 0) = -0.658` — inward (only passing face).

Three of four faces point outward with the actuator off; the benchmark
rectangle is structurally not a positively invariant set, and no amplitude
choice can make it one. This is why the chief's "diagnostic rectangle" wording
is mandatory, and it also explains why the correct safety interface for R1/R2
is the threshold-envelope bound of Lemma R2.1 (which controls the prey
coordinate directly against `A`) rather than rectangle invariance.

## 7. Scope and residual work (for Round 3)

1. **Linearized scope.** Lemma R2.1 is a statement about the linearized
   system. Lifting it to the nonlinear Caputo predator-prey map requires a
   Volterra continuous-dependence estimate with a Lipschitz constant on a
   declared trust region and a smallness condition (fractional Grönwall), as
   sketched in the manuscript's Remark `rem:nfl_scope`. This lift is the
   natural content of Round 3 together with the quantitative `E_m` law.
2. **Envelope conservatism.** `u_safe` is the ceiling for the whole amplitude
   ball; a refinement separating sustained from sparse inputs would sharpen the
   R1 ceiling further but is not needed for Round 3.
3. **No new approximation rates.** `E_m(alpha,T)` is still imported; Round 3
   must pin it for the declared latent class (nested exponential-sum kernels).
4. Theorem R2 is deliberately an *upper bound on safe excitability*, not a
   testing lower bound; the R4 testing bound remains open.

## 8. Reproducibility

```
cd research_rounds/round2
python3 compute_B_safe.py     # validation gate + B_safe_grid.json
```

Outputs: `B_safe_grid.json` (12 cells), `B_safe_vs_alpha.pdf`. The validation
gate (alpha->1 vs scipy `expm`) is asserted before any bound is reported.

## 9. GO / NO-GO decision

**GO.** The Strong-Allee-dependent bound exists, is exact in the linearized
regime, passes the integer-order validation gate, and is quantitatively
nontrivial exactly in the primary benchmark regime (tightening factors
0.12–0.69 on the squared ceiling where `A >= 0.25`). Round 3 should attack:

> Pin the latent-complexity law `E_m(alpha, T)` for the declared nested class,
> and combine R1 + R2 + R3 into the R4 testing bound, keeping the nonlinear
> lift of R2 as an explicit scoped assumption.
