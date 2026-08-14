# Round 2 Results — Chief-Corrected Status

Date: 2026-08-14
Status: **PARTIAL**

The researcher produced a correct and numerically validated **sufficient linear safety envelope**, but the attempted conversion of that envelope into an upper bound on the energy of *all* safe inputs had the inequality direction reversed. See `CHIEF_ROUND2_AUDIT.md` for the complete audit and `ROUND2_RESULTS_RESEARCHER_ORIGINAL.md` for provenance.

## Correct result R2a — Strong-Allee certified-safe inner ball

For the focal linearized Caputo system

\[
\xi(t)=\int_0^t H_\alpha(t-s)u(s)\,ds,
\]

define the prey-coordinate finite-horizon gain

\[
\Gamma_{x,T}(A,\alpha)
=
\sup_{0\le t\le T}\int_0^t|e_1^\top H_\alpha(s)|\,ds.
\]

Fix a strict ecological reserve `eta>0` and

\[
\rho_\eta(A)=x^*-(A+\eta)>0.
\]

Then

\[
\boxed{
\|u\|_{L^\infty(0,T)}
<
\frac{\rho_\eta(A)}{\Gamma_{x,T}(A,\alpha)}
}
\]

is sufficient to guarantee

\[
x(t)>A+\eta,
\qquad 0\le t\le T,
\]

for the focal linearized Caputo model.

Using the vector gain

\[
\Gamma_T=\sup_{t\le T}\int_0^t\|H_\alpha(s)\|_2ds
\]

gives a more conservative but also valid sufficient condition.

## Critical direction

Let

\[
\mathcal U_{\rm cert}
=
\{u:\|u\|_\infty<\rho_\eta/\Gamma_{x,T}\}.
\]

Then

\[
\boxed{\mathcal U_{\rm cert}\subseteq\mathcal U_{\rm safe}}
\]

for the focal linearized model.

Therefore this result does **not** imply

\[
B_{\rm safe}\le\sqrt T\rho/\Gamma_T.
\]

It is an inner safety certificate, not an outer bound on the complete safe set.

If one defines a deliberately restricted certified protocol objective

\[
\Delta_{\rm cert}^{(m)}
=
\sup_{u\in\mathcal U_{\rm cert}}
\inf_{L\in\mathcal L_m}
D_{\rm KL}(P_C^u\|P_L^u),
\]

then Round 1 yields the valid protocol-class bound

\[
\Delta_{\rm cert}^{(m)}
\le
\frac{T}{2}
\left(\frac{\rho_\eta}{\Gamma_{x,T}}\right)^2
\|R^{-1/2}S\|^2E_m^2.
\]

But because

\[
\Delta_{\rm cert}^{(m)}\le\Delta_{\rm safe}^{(m)},
\]

this is **not** a fundamental impossibility bound for all safe experiments.

## Numerics retained

The stored vector-gain `Gamma_T` grid is numerically consistent. Chief-side recomputation of all 12 cells at lower quadrature resolution (`n=4000`) agrees with the stored `n=24000` values to maximum relative discrepancy below `4.3e-6`; see `audit_gamma_convergence_output.txt`.

The numerical values should now be interpreted as sizes of a sufficient certified input ball, not as maximum safe energies.

## R2 gate

- Sufficient Strong-Allee linear certificate: **PROVED**.
- Strict threshold certificate: **requires eta>0**; `eta=0` is only the limiting threshold-touch case.
- Common-safe certificate across the full rival family: **OPEN** until all rivals have a common ecological safety output and a uniform gain bound.
- Strong-Allee-dependent upper bound on *all* safe-input energy: **NOT PROVED**.
- Substitution of `sqrt(T) rho/Gamma_T` into R1 as an outer `B_safe`: **REJECTED**.

## Next

R3 should continue the independent `E_m(alpha,T)` approximation-complexity track, but must simultaneously repair the safety interface by restricting the implementable design class enough to obtain a necessary/coercive outer safe-excitation bound, or establish that such a bound is impossible without those additional restrictions.
