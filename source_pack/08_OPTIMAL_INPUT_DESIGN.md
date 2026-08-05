# Optimal Input Design — Solved Linear-Gaussian Problems

## 1. General pairwise design

Let two fixed models map an input \(u\) to the observation vector

\[
Y_i=H_i u+\varepsilon,
\qquad \varepsilon\sim\mathcal N(0,R),
\qquad i\in\{1,2\}.
\]

Define

\[
\Delta H=H_1-H_2.
\]

The KL divergence is

\[
D_{12}(u)
=\frac12\|R^{-1/2}\Delta H u\|^2.
\tag{1}
\]

## Theorem 1 — energy-constrained optimal input

Under

\[
\|u\|^2\le E,
\]

the maximum pairwise KL divergence is

\[
\boxed{
D_{12}^{\max}=\frac{E}{2}\lambda_{\max}
\left(\Delta H^*R^{-1}\Delta H\right).
}
\tag{2}
\]

An optimal input is

\[
\boxed{u^*=\sqrt E\,v_{\max},}
\tag{3}
\]

where \(v_{\max}\) is a unit principal eigenvector/eigenfunction of

\[
Q=\Delta H^*R^{-1}\Delta H.
\]

### Proof

Equation (1) equals \(\frac12\langle u,Qu\rangle\). The Rayleigh–Ritz theorem gives

\[
\sup_{\|u\|^2\le E}\langle u,Qu\rangle=E\lambda_{\max}(Q).
\]

Equality holds at a principal eigenvector. ∎

## Interpretation

This solves the pairwise linear-Gaussian design exactly. A pulse, chirp, PRBS, or multisine is optimal only to the extent that it approximates the principal eigenfunction under additional amplitude, sign, duration, or implementation constraints.

## 2. Frequency-domain solution for stable LTI models

For scalar stable LTI models with transfer difference

\[
\Delta G(i\omega)=G_1(i\omega)-G_2(i\omega),
\]

white output noise of variance \(\sigma^2\), and an input spectral energy measure \(\xi\),

\[
D_{12}(\xi)
=\frac{1}{2\sigma^2}\int_\Omega
|\Delta G(i\omega)|^2\,d\xi(\omega),
\]

subject to

\[
\xi(\Omega)\le E.
\]

## Corollary 2.1 — optimal single frequency

For two fixed scalar models,

\[
\boxed{
\omega^*\in\arg\max_{\omega\in\Omega}|\Delta G(i\omega)|^2,
}
\]

and all available energy is assigned to \(\omega^*\). For a real input, use the conjugate pair \(\pm\omega^*\), corresponding to a sinusoid.

This result concerns **fixed simple models**. It does not imply that a single sinusoid is optimal for parameter estimation or robust composite-model discrimination.

## MIMO version

With output covariance \(R(\omega)\), the frequency score is

\[
w_{12}(\omega)=
\lambda_{\max}\left(
\Delta G(i\omega)^*R(\omega)^{-1}\Delta G(i\omega)
\right).
\]

At the selected frequency, excite the associated right singular vector.

## 3. Robust discrimination among several fixed models

Let \(p=1,\dots,P\) index model pairs and define

\[
w_p(\omega)=\frac{1}{2\sigma^2}|G_{i_p}(i\omega)-G_{j_p}(i\omega)|^2.
\]

The robust spectral design is the linear program over nonnegative measures

\[
\max_{\xi,t}\ t
\]

subject to

\[
\int_\Omega w_p(\omega)d\xi(\omega)\ge t,
\quad p=1,\dots,P,
\]

\[
\xi(\Omega)\le E,
\qquad \xi\ge0.
\tag{4}
\]

## Theorem 2 — a finite multisine is sufficient

An optimal solution of (4) exists, under compact \(\Omega\) and continuous \(w_p\), and there is an optimal spectral measure supported on at most

\[
\boxed{P+1}
\]

frequencies.

### Proof

Normalize a nonzero design by its total energy. The vector

\[
\left(\int w_1d\xi/E,\dots,\int w_Pd\xi/E\right)
\]

lies in the convex hull of

\[
\{(w_1(\omega),\dots,w_P(\omega)): \omega\in\Omega\}\subset\mathbb R^P.
\]

By Carathéodory’s theorem, every point in this convex hull has a representation using at most \(P+1\) support points. Rescale by \(E\). ∎

## Consequence

The rigorous robust counterpart of “use multiscale excitation” is a finite multisine whose frequencies and weights solve (4). A logarithmic pulse train or chirp is an implementation surrogate when precise sinusoidal control is unavailable.

## 4. Why parameter-estimation and discrimination designs differ

For parameter vector \(\psi\), local parameter estimation uses the sensitivity operator

\[
S_\psi=\frac{\partial H(\psi)}{\partial\psi}.
\]

Evaluated at one model, this leads to a Fisher matrix such as

\[
F(u)=S_\psi(u)^*R^{-1}S_\psi(u).
\]

Model discrimination uses

\[
Q_{12}=\Delta H^*R^{-1}\Delta H.
\]

These are different operators. A design can make \(F\) well conditioned while \(\Delta H u\) remains small because a latent alternative tracks the fractional model. This proves the proposal’s hypothesis H3 at the level of objective functions.

## 5. Constrained implementation

With box, rate, or cumulative-impact constraints, solve

\[
\max_u\ \frac12u^*Qu
\]

subject to

\[
|u_k|\le u_{\max},\qquad
|u_{k+1}-u_k|\le r_{\max},\qquad
\sum_k|u_k|\Delta t\le B.
\]

This is generally a nonconvex quadratic maximization. Reliable methods are:

- direct transcription with multiple starts;
- semidefinite relaxation and randomized rounding;
- dynamic programming for low-dimensional discrete inputs;
- Bayesian optimization when the forward simulator is expensive.

The unconstrained eigenvector solution is the benchmark and upper bound.
