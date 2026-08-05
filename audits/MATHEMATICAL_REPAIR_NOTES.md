# Mathematical Repair Notes

This document gives replacement statements for the most important defective theorems and identifies the scope that the manuscript may safely claim.

---

## 1. Corrected generic separating-frequency theorem

### Proposition — Fixed-model separation on a compact band

Let \(G_1,\dots,G_M\) be scalar functions analytic on a connected open set \(D\subset\mathbb C\). Let

\[
K=\{i\omega:\omega\in[\omega_{\min},\omega_{\max}]\}\subset D
\]

be a compact segment containing no poles or branch point. Assume \(G_i-G_j\not\equiv0\) on \(D\) for every \(i\ne j\). Then, for every pair, the set

\[
Z_{ij}=\{\omega\in[\omega_{\min},\omega_{\max}]:G_i(i\omega)=G_j(i\omega)\}
\]

is finite. Therefore the union \(\bigcup_{i<j}Z_{ij}\) is finite, and every frequency outside that union separates all fixed model pairs.

### Proof

For each pair, \(G_i-G_j\) is nonzero and analytic, so its zeros are isolated. An infinite subset of the compact set \(K\) has an accumulation point in \(K\), contradicting the identity theorem. Hence each \(Z_{ij}\) is finite. A finite union over model pairs is finite.

### Scope

This proposition concerns a finite collection of fixed transfer functions. It does not provide uniform separation over continuously parameterized rival classes.

---

## 2. Corrected energy-optimal input theorem

### Finite-dimensional version

Let \(H_1,H_2\in\mathbb R^{n_y\times n_u}\), \(R\succ0\), and \(\Delta H=H_1-H_2\). Define

\[
Q=\Delta H^\top R^{-1}\Delta H\succeq0.
\]

For \(\|u\|_2^2\le E\),

\[
D_{12}(u)=\frac12u^\top Qu
\]

is maximized by

\[
u^*=\sqrt E\,v_{\max},
\]

where \(v_{\max}\) is any unit eigenvector associated with \(\lambda_{\max}(Q)\). The maximum is

\[
D_{12}^{\max}=\frac E2\lambda_{\max}(Q).
\]

### Hilbert-space version

Let \(A=R^{-1/2}\Delta H:\mathcal U\to\mathcal Y\) be compact between Hilbert spaces. Then \(Q=A^*A\) is compact, self-adjoint, and positive. Its spectral radius is an eigenvalue, so the same formula holds with a principal eigenfunction.

### Required manuscript change

Do not claim existence of a principal eigenfunction without compactness or an explicit finite discretization.

---

## 3. Correct scope of the finite-horizon approximation barrier

### Kernel-level theorem

For \(0<\alpha<1\), fixed \(T>0\), and fixed \(u\in L^2(0,T)\), finite positive exponential mixtures can approximate the fractional integral kernel in \(L^1(0,T)\), hence

\[
\inf_m\|(k_\alpha-k_m)*u\|_{L^2(0,T)}=0.
\]

This establishes failure of robust discrimination for a **linear convolution experiment with a fixed input** if the latent exponential-mixture dimension is unrestricted.

### Nonlinear extension that would be sufficient

Write the nonlinear Caputo system in Volterra form

\[
x(t)=x_0+(k_\alpha*F(x,u))(t),
\]

and the exponential-mixture approximation as

\[
x_m(t)=x_0+(k_m*F(x_m,u))(t).
\]

Assume on a common invariant region that

\[
\|F(x,u)-F(\widetilde x,u)\|\le L\|x-\widetilde x\|,
\qquad
\|F(x,u)\|\le M.
\]

If \(L\|k_m\|_{L^1(0,T)}<1\), then

\[
\|x-x_m\|_{L^\infty(0,T)}
\le
\frac{M\|k_\alpha-k_m\|_{L^1(0,T)}}
{1-L\|k_m\|_{L^1(0,T)}}.
\]

More general horizons require a Volterra resolvent or fractional Grönwall estimate.

### Required manuscript change

Until such a state-error theorem is included, describe Corollary 6.6 as a linearized fixed-input barrier.

---

## 4. Correct finite-support theorem and its limitation

Let \(w_1,\dots,w_P\) be continuous nonnegative functions on compact \(\Omega\). The maximin measure problem

\[
\max_{\xi,t}t
\quad\text{s.t.}\quad
\int_\Omega w_p(\omega)d\xi(\omega)\ge t,
\quad p=1,\dots,P,
\quad \xi(\Omega)\le E
\]

admits an optimal measure. There exists an optimum supported on at most \(P+1\) frequencies by Carathéodory’s theorem applied to

\[
\omega\mapsto(w_1(\omega),\dots,w_P(\omega)).
\]

### Limitation

Here \(P\) is the number of fixed constraints. For a composite rival class indexed by continuous parameters, the problem is semi-infinite. The \(P+1\) bound applies only after a justified finite reduction or discretization.

---

## 5. Safer fractional rectangle theorem

### Strict inward-pointing version

Consider

\[
{}^CD_t^\alpha z(t)=F(t,z(t)),\qquad0<\alpha<1,
\]

with a unique continuous solution and

\[
R=\prod_{i=1}^n[\ell_i,u_i].
\]

Assume \(z(0)\in\operatorname{int}R\) and there exists \(\eta>0\) such that for all \(t\ge0\):

\[
F_i(t,z)\ge\eta
\quad\text{whenever }z_i=\ell_i,
\]

and

\[
F_i(t,z)\le-\eta
\quad\text{whenever }z_i=u_i.
\]

Then no component can have a first contact with a face of \(R\). At a first lower-face minimum, the Caputo extremum principle yields \({}^CD_t^\alpha z_i(t^*)<0\), contradicting \(F_i\ge\eta\); the upper-face case is analogous. Hence the solution remains in \(\operatorname{int}R\).

### Caveat

This strict theorem is easier to justify than the current non-strict statement. A non-strict version should be based on a cited viability theorem and a careful treatment of initial points on the boundary.

---

## 6. Correct Bayesian sequential information identity

Let \(\mathcal D_n=(Y_{1:n},d_{1:n})\), and let \(d\) be the next design. Then

\[
I(M;Y_{n+1}\mid\mathcal D_n,d)
=
\mathbb E_{Y_{n+1}\mid\mathcal D_n,d}
\left[
D_{\mathrm{KL}}\left(
 p(M\mid\mathcal D_n,Y_{n+1},d)
 \|\
 p(M\mid\mathcal D_n)
\right)
\right].
\]

Also,

\[
0\le I(M;Y_{n+1}\mid\mathcal D_n,d)
\le H(M\mid\mathcal D_n).
\]

The upper bound follows from

\[
I(M;Y\mid\mathcal D_n,d)
=H(M\mid\mathcal D_n)-H(M\mid\mathcal D_n,Y,d).
\]

Equality holds if the future observation determines \(M\) almost surely conditional on the current data and design.

### Do not claim

Do not state that greedy maximization of this one-step quantity globally minimizes expected experiment count without an additional theorem.

---

## 7. Correct model-discrimination scope

The manuscript should distinguish three problems.

### Fixed simple hypotheses

\[
M_i:\quad Y\sim p_i(\cdot\mid d).
\]

Pairwise KL and eigenvector design are directly applicable.

### Composite hypotheses

\[
M_i:\quad Y\sim p_i(\cdot\mid\theta_i,d),
\qquad \theta_i\in\Theta_i.
\]

A maximin design uses

\[
\max_d\min_{i<j}\inf_{\theta_i,\theta_j}
\mathcal D\bigl(p_i(\cdot\mid\theta_i,d),p_j(\cdot\mid\theta_j,d)\bigr).
\]

Positivity requires separation of the induced predictive families; a finite latent-dimension cap alone does not guarantee it.

### Bayesian model uncertainty

Parameters are integrated out:

\[
p(Y\mid M_i,d)=\int p(Y\mid\theta_i,M_i,d)p(\theta_i\mid M_i)d\theta_i.
\]

This is the level at which mutual information between model identity and future data is computed.

The manuscript currently moves between these three levels without consistently marking the transition.

---

## 8. Stable-only benchmark specification

The primary benchmark should impose

\[
A<2/7
\]

so that the integer-order equilibrium is locally stable. Suggested values are

\[
A\in\{0.20,0.25,0.28\}.
\]

The \(A=0.30\) and \(A=0.40\) cases should be moved to a separate stability-verdict study.

For each rival mechanism:

1. match the same equilibrium;
2. match static gain or initial recovery moments where feasible;
3. fit nuisance parameters on passive/pre-excitation data;
4. evaluate active discrimination only on held-out perturbation data;
5. use the same observation horizon and energy/amplitude budgets.

This prevents trivial classification by baseline mismatch.

---

## 9. Required numerical consistency checks

Given the displayed four-class confusion matrix:

\[
N=189000,
\qquad
N_{\mathrm{correct}}=141517,
\qquad
\mathrm{accuracy}=0.748767.
\]

The ODE–Caputo bidirectional confusion is

\[
290+20331=20621,
\]

not 34621.

The Caputo row total is

\[
20331+58159+1491+1019=81000.
\]

All prose, captions, JSON summaries, and aggregation scripts must be reconciled against these arithmetic identities.

---

## 10. Appendix reconstruction rule

For every theorem:

1. state the exact spaces and domains;
2. state whether the result is finite-dimensional, infinite-dimensional, linearized, or nonlinear;
3. list every regularity, compactness, stability, and identifiability assumption;
4. prove exactly the stated theorem once;
5. do not introduce new constraints or variables only in the appendix;
6. separate mathematical theorems from computational algorithms and empirical observations.
