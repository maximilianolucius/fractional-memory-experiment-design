# Nonlinear Bayesian Extension

The analytical theorems solve the local linear-Gaussian layer. This document specifies the full nonlinear layer without pretending it has a closed-form solution.

## 1. Bayesian model-discrimination utility

Let \(M\in\{1,\dots,K\}\), parameters \(\vartheta_M\sim p(\vartheta_M\mid M)\), design \(d\), and future data \(Y\). The exact expected model information is

\[
U_{\mathrm{MI}}(d)
=I(M;Y\mid d)
=\mathbb E\left[
\log\frac{p(Y\mid M,d)}{\sum_jp(M_j)p(Y\mid M_j,d)}
\right].
\tag{1}
\]

where

\[
p(Y\mid M,d)=\int p(Y\mid\vartheta_M,M,d)p(\vartheta_M\mid M)d\vartheta_M.
\]

No Gaussian or linear approximation is implied by (1).

## 2. Joint model-and-parameter information

If the purpose includes parameter recovery,

\[
U_{\mathrm{joint}}(d)=I((M,\vartheta_M);Y\mid d).
\]

This objective can favor designs that are good for within-model parameter estimation but not robust model separation. Report model-only and joint utilities separately.

## 3. Robust alternative

For parameter sets \(\Theta_i\), define

\[
U_{\min}(d)=
\min_{i<j}
\inf_{\theta_i\in\Theta_i,\theta_j\in\Theta_j}
D_{\mathrm{KL}}
\left(p_i(Y\mid\theta_i,d)\|p_j(Y\mid\theta_j,d)\right).
\tag{2}
\]

Equation (2) protects against alternatives that tune themselves to mimic the focal model. It becomes zero if the latent class is unrestricted, by the no-free-lunch theorem.

## 4. Safe Bayesian design

A chance constraint is

\[
\Pr\left(z(t)\in\mathcal S\ \forall t\in[0,T]\mid d\right)
\ge1-\delta_s.
\tag{3}
\]

A more conservative robust constraint requires safety for every parameter in a credible/admissible set. The paper should report which interpretation is used.

## 5. Nested Monte Carlo estimator

A direct estimator for (1) is:

1. sample \(M^{(r)}\sim p(M)\);
2. sample \(\vartheta^{(r)}\sim p(\vartheta\mid M^{(r)})\);
3. simulate \(Y^{(r)}\sim p(Y\mid M^{(r)},\vartheta^{(r)},d)\);
4. estimate each model evidence \(p(Y^{(r)}\mid M_j,d)\) with inner parameter samples;
5. average the log ratio in (1).

Use common random numbers across candidate designs to reduce optimizer noise.

## 6. Variance-reduction hierarchy

Use the following order:

1. exact linear-Gaussian utility for screening and unit tests;
2. Laplace approximation around posterior modes;
3. importance sampling/SMC evidence;
4. neural ratio or mutual-information lower bounds only after calibration against tractable cases.

## 7. Adaptive design

After data \(Y_{1:n}\), update model and parameter posteriors and choose

\[
d_{n+1}=\arg\max_d
I(M;Y_{n+1}\mid Y_{1:n},d)
\]

subject to posterior safety. Stop when one of the following occurs:

- posterior model probability exceeds a predeclared threshold;
- expected value of another experiment is below cost;
- no safe design attains the minimum information target;
- the model set fails posterior predictive checks, signaling out-of-class dynamics.

## 8. Mandatory robustness axes

Every reported “optimal” design should be re-evaluated under:

- prior perturbations for \(\alpha,\tau,m\), and latent rates;
- process versus observation noise;
- uncertain initial history/prehistory;
- intervention-amplitude error;
- missing samples;
- solver and exponential-sum truncation error;
- out-of-model functional responses;
- correlated environmental forcing.

## 9. Honest theorem/computation boundary

The paper may prove the local design results and then state:

> The nonlinear Bayesian optimum is computed, not symbolically derived. Its validity is established by convergence diagnostics, independent re-simulation, utility confidence intervals, and recovery on analytically solvable benchmarks.
