# Chief Audit — Research Round 2

Date: 2026-08-14
Decision: **PARTIAL / NO-GO for the claimed R2 theorem; GO for the corrected inner-certificate result**

## Executive finding

The numerical calculation of the Caputo finite-horizon gain `Gamma_T` is internally consistent, and the researcher correctly identified a useful Strong-Allee-dependent **sufficient safety certificate**. However, the central Round-2 theorem has the inequality direction reversed relative to the Round-1 definition of `B_safe,m`.

The submitted claim

\[
B_{\mathrm{safe},m}\le \sqrt{T}\,\frac{\rho}{\Gamma_T}
\]

does **not** follow from Lemma R2.1. The lemma proves that the amplitude ball

\[
\|u\|_\infty\le \rho/\Gamma_T
\]

is contained in the safe set. Therefore it yields an **inner approximation** of the safe class, not an outer bound on all safe inputs.

If

\[
B_{\mathrm{safe},m}=\sup_{u\in\mathcal U_{\mathrm{safe},m}}\|u\|_2,
\]

then, for the focal linearized Caputo model and an otherwise unrestricted input space,

\[
\boxed{
B_{\mathrm{safe},m}\;\ge\;\sqrt{T}\,\rho/\Gamma_T
}
\]

whenever the full constant-amplitude ball is admissible. The direction needed to sharpen the Round-1 impossibility ceiling is the opposite one.

Consequently, the displayed Round-2 substitution

\[
\Delta_{\mathrm{safe}}^{(m)}
\le
\frac{T\rho^2}{2\Gamma_T^2}\|R^{-1/2}S\|^2E_m^2
\]

is **not established for the full safe class**.

This is a load-bearing issue: R2 cannot currently support the planned fundamental statement “Allee proximity forces all safe experiments to have small information.”

---

## What is valid and should be preserved

### 1. The linear safety-envelope lemma

For the focal linearized Caputo system,

\[
\xi(t)=(H_\alpha*u)(t),
\]

with

\[
\Gamma_T=\sup_{t\le T}\int_0^t\|H_\alpha(s)\|\,ds,
\]

the implication

\[
\|u\|_\infty\le \rho/\Gamma_T
\quad\Longrightarrow\quad
\sup_{t\le T}\|\xi(t)\|\le\rho
\]

is correct. This is a **sufficient certified-safe input ball**.

For prey-threshold safety specifically, a sharper coordinate form is available:

\[
\Gamma_{x,T}
=
\sup_{t\le T}\int_0^t|e_1^\top H_\alpha(s)|\,ds,
\]

so that

\[
\|u\|_\infty<\frac{x^*-(A+\eta)}{\Gamma_{x,T}}
\]

certifies the strict margin

\[
x(t)>A+\eta,
\qquad \eta>0.
\]

This is preferable to using the Euclidean vector gain when the safety requirement is specifically the Allee prey floor.

### 2. The `Gamma_T` numerical values

I independently re-ran all 12 stored cells using a separate lightweight convergence check at `n=4000`, versus the researcher's `n=24000` grid. The maximum relative discrepancy was below

\[
4.3\times 10^{-6}.
\]

The audit is reproducible with:

```bash
python research_rounds/round2/audit_gamma_convergence.py
```

See `audit_gamma_convergence_output.txt`.

Thus the numerical table is not the problem; the problem is its **mathematical interpretation**.

### 3. The benchmark diagnostic rectangle result

The zero-input face analysis is useful and consistent with the prior chief audit: the benchmark rectangle is not a T17 invariant rectangle, and changing only the prey-input amplitude cannot repair the predator faces. Keep this as a negative structural result.

---

## Additional mathematical corrections

### A. Strict Allee safety needs a reserve margin

The Round-2 notes use

\[
\rho=x^*-A
\]

and conclude only `x(t) >= A`. For a robust safe experiment this is too weak: equality at the Allee threshold is not a protected state, especially in the presence of predators.

Use instead

\[
\rho_\eta=x^*-(A+\eta),\qquad \eta>0,
\]

and a strict amplitude inequality. Numerical plots with `eta=0` may be retained only as limiting diagnostics and must not be labelled strict safety certificates.

### B. Common-safe across rivals is not yet proved

The Round-2 text says the same `Gamma_T` bounds the whole rival family because the models share a Jacobian skeleton. This is not sufficient.

The ODE, Caputo, DDE, and latent models have different input-to-state propagators. For robust common safety one needs either

\[
\bar\Gamma_T
=
\sup_{M\in\{C_\alpha\}\cup\mathcal L_m}\Gamma_{T,M}<\infty,
\]

with a common ecological prey-state/output map explicitly defined for every rival, or a different robust-safety argument.

In particular, the current arbitrary latent realization `qdot=Abar q+Bbar u, y=Cbar q` does not by itself specify which latent coordinates constitute ecological prey/predator states for state-safety purposes. This must be frozen before claiming `U_safe,m` is common-safe.

### C. No general monotonicity in `alpha` should be claimed from the 12-cell grid

The observed values increase with `alpha` on this particular grid. That does not justify a general theorem that `Gamma_T` is monotone in fractional order, nor the explanation that larger `alpha` means “slower Mittag-Leffler decay.” At long time, fractional and exponential decay comparisons are subtler, and finite-horizon gain depends on the spectrum and horizon.

State this only as an empirical property of the locked grid unless proved.

### D. Finite-horizon integrability does not require the asymptotic stability argument

For `T<infinity`, local behavior near zero,

\[
H_\alpha(t)\sim t^{\alpha-1}B/\Gamma(\alpha),
\]

is enough to establish integrability because `alpha>0`. The large-time `O(t^{-alpha-1})` asymptotic is useful only for infinite-horizon discussion and requires the appropriate sector/invertibility assumptions.

---

## Why the original R2 target is harder than it looked

A state-safety condition is generally **not an upper bound on input energy**. Stable strictly proper systems can strongly attenuate oscillatory/high-frequency inputs; therefore large-energy inputs can sometimes produce small state excursions. A universal Strong-Allee-dependent bound

\[
\|u\|_2\le C\rho
\]

for every safe input cannot be inferred from an inward state margin alone without additional restrictions such as actuator amplitude, bandwidth, total variation, waveform family, or an input-to-state coercivity condition.

This is exactly why the generic experimental cap `||u||_infty <= u_max` remains a valid outer energy bound, while `rho/Gamma_T` is only a sufficient inner certificate.

A mathematically viable repair is to freeze an implementable finite-dimensional or band-limited design class `V` and prove a coercivity constant

\[
\kappa_V
:=
\inf_{u\in V,\ \|u\|_2=1}
\|\mathcal H_xu\|_{\mathrm{safety}}>0.
\]

Then a symmetric trust-region condition

\[
\|\mathcal H_xu\|_{\mathrm{safety}}\le \rho
\]

implies the **necessary** outer bound

\[
\|u\|_2\le \rho/\kappa_V.
\]

That is the type of inequality R1 actually needs if we want an Allee-dependent impossibility ceiling.

---

## Visual audit

### Main manuscript figures

No visual regression was introduced. I raster-compared all 16 current manuscript figure PDFs against the previous chief-patched package at 100 dpi. Every rendered figure was pixel-identical (`mean absolute difference = 0` for all 16). Figure 11 and the other chief-fixed visuals were preserved exactly.

### Round-2 research figure

`B_safe_vs_alpha.pdf` had a presentation defect: the axes clipped much of the `A=0.20` and `A=0.30` series, while the legend displayed all three, making the orange `A=0.25` curve appear to be the only data. Panel (b) also called values greater than one a “sharpening factor,” which is misleading.

I generated a corrected diagnostic:

- `B_safe_vs_alpha_CHIEF_CORRECTED.pdf`
- `B_safe_vs_alpha_CHIEF_CORRECTED.png`
- generator: `plot_B_safe_chief_corrected.py`

It shows all three `A` series and labels the quantity correctly as a **sufficient certified amplitude ball**, not a bound on the full safe class. The energy fraction is clipped with the existing generic amplitude cap and therefore lies in `[0,1]`.

The submitted `compute_B_safe.py` also claimed the figure as an output but did not contain plotting code. The new plotting script closes that reproducibility gap.

---

## Governance decision

### R1

**UNCHANGED / PROVED** under its stated assumptions. Its generic outer bound from the explicit actuator cap remains valid:

\[
B_{\mathrm{safe},m}\le\sqrt T\,u_{\max}.
\]

### R2

**REJECTED AS STATED.** Replace status `PROVED` by:

> **PARTIAL — sufficient Strong-Allee certified-safe inner ball proved; no Strong-Allee-dependent outer energy bound for the full safe class yet.**

### R3

Proceed with the latent approximation law `E_m(alpha,T)`, because that track is independent and remains valuable. But R3 must also repair the safety interface before R4:

1. freeze the precise latent class and ecological safety output;
2. determine whether a uniform common-safe gain exists;
3. freeze an implementable input class (bandwidth / finite waveform dictionary / total-variation or equivalent constraint);
4. prove a **necessary/coercive outer bound** on safe excitation in that class, or prove rigorously that no such bound follows without the added restriction.

Only after that should R4 convert the upper-KL result into a universal testing lower bound.
