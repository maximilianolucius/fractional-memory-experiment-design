# Mathematical Audit of `main.pdf`

## Status

The draft is not mathematically publishable in its present form. The issues below are corrections, not stylistic preferences.

## Critical errors

### 1. Invalid Laplace transform of a nonlinear vector field

The draft writes, in effect,

\[
s^\alpha X(s)=F(X(s),\theta).
\]

For a nonlinear \(f(x(t),\theta)\), generally

\[
\mathcal L\{f(x(t),\theta)\}(s)\neq f(X(s),\theta).
\]

The resolvent formula is valid only after linearization or for a genuinely linear system.

**Correction:** explicitly linearize at an equilibrium and write

\[
(q_\alpha(s)I-J)\Xi(s)=BU(s).
\]

### 2. False time-change reduction

The claim that a Caputo system becomes an integer-order ODE under

\[
\tau=t^\alpha/\Gamma(1+\alpha)
\]

is false in general. The Caputo derivative has nonlocal memory and does not obey an ordinary chain rule that permits this reduction.

### 3. Structural identifiability is not equivalent to a sampled sensitivity rank test

Full rank of a finite sampled sensitivity matrix is a useful **local practical identifiability** diagnostic. It is not, without additional analytic assumptions, an if-and-only-if test for global or local structural identifiability of a nonlinear model.

### 4. Incorrect gamma-kernel limit

A single normalized gamma density with its rate sent to zero does not become a power-law memory kernel on the whole half-line. It retains an exponential tail for every positive rate, while the zero-rate limit is not a normalized density.

**Correction:** use the exact continuum exponential representation and finite exponential mixtures. A single gamma delay may approximate some finite-window shapes, but not as a general theorem of structural equivalence.

### 5. Incorrect exponential-sum approximation statement

The draft asserts a bound of the form

\[
\|K_\alpha-K_m\|\le Ce^{-\beta m}
\]

on \([0,T]\) without specifying norm, excluding the singular endpoint, or stating how constants depend on scale range. A finite exponential sum is bounded at \(t=0\), whereas \(t^{\alpha-1}\) is unbounded for \(0<\alpha<1\). Uniform approximation on \([0,T]\) is impossible.

**Correction:** use either relative/uniform approximation on \([\delta,T]\), \(\delta>0\), or an \(L^1(0,T)\) approximation. This pack proves a constructive \(L^1\) result.

### 6. Incorrect convolution norm bound

The displayed implication from an \(L^1\) kernel error and an \(L^\infty\) input to an \(L^2\) output omits a factor or uses incompatible Young inequalities.

Correct examples are

\[
\|(K-K_m)*u\|_{L^2}\le \|K-K_m\|_{L^1}\|u\|_{L^2},
\]

or

\[
\|(K-K_m)*u\|_{L^\infty}\le \|K-K_m\|_{L^1}\|u\|_{L^\infty}.
\]

### 7. Dimensional inconsistency

Replacing \(d/dt\) by \({}^C D_t^\alpha\) changes units from time\(^{-1}\) to time\(^{-\alpha}\). Keeping the same ecological rates while varying \(\alpha\) confounds fractional order with units.

**Correction:** introduce a reference time \(\tau_0\):

\[
\tau_0^{\alpha-1}{}^C D_t^\alpha x=f(x;\theta)+Bu.
\]

### 8. Wrong interpretation of the Matignon region

For \(0<\alpha<1\), the condition

\[
|\arg \lambda|>\alpha\pi/2
\]

allows some eigenvalues with positive real part. Relative to the integer-order left-half-plane condition, this is an enlarged stability sector, not a “more stringent” condition.

The draft’s alternative inequality for instability is not generally correct as written.

### 9. Unsupported universal bifurcation scaling

The formula

\[
K_c(\alpha,\theta)=K_c^{\mathrm{ODE}}(\theta)g(\alpha)
\]

is not a general result. For the locked strong-Allee model, the correct stability boundary can be derived from trace and determinant; it is not generally multiplicatively separable.

### 10. False componentwise stability rule for incommensurate systems

For component-specific orders, stability is not obtained by assigning each eigenvalue to one state component and checking

\[
|\arg\lambda_i|>\alpha_i\pi/2.
\]

The characteristic equation couples the orders. Multi-order systems require the appropriate common-denominator/characteristic-root theory.

### 11. False distributed-order “mean order” stability rule

The claim that distributed-order stability depends only on

\[
\int_0^1 \alpha\phi(\alpha)d\alpha
\]

is false in general. The full symbol

\[
Q(s)=\int_0^1 \phi(\alpha)s^\alpha d\alpha
\]

enters the characteristic equation. Two distributions with the same mean can have different \(Q(s)\) and different dynamics.

### 12. Contradiction concerning limit cycles

The draft discusses a fractional “limit-cycle period” after a Hopf bifurcation. For the standard autonomous Caputo state-space class with \(0<\alpha<1\), exact nonconstant periodic solutions are excluded under the usual hypotheses. The validated paper correctly warns not to claim a limit cycle at a Matignon boundary.

Use “loss of local stability” and “long-lived oscillatory transients,” not “birth of a periodic orbit,” unless the model class is changed.

### 13. Positive exponential sums are not universal continuous-kernel approximators

A positive sum

\[
\sum_j c_j e^{-\lambda_j t},\qquad c_j,\lambda_j>0,
\]

is completely monotone. It cannot approximate every continuous kernel while retaining positivity and monotonicity constraints. Signed exponentials, splines, or unconstrained neural kernels define different model classes.

### 14. Unverified empirical results

The reported posterior intervals, ELPD values, Bayes factors, SBC failures, and coverage values are results only if backed by data, code, seeds, solver tolerances, and stored outputs. None should appear in a paper as factual results without those artifacts.

### 15. Misassigned references and tools

Examples:

- Beylkin–Monzón is not a microbial predator–prey dataset source.
- a fractional calculus monograph is not the source for NUTS;
- an identifiability/PINN paper is not a generic reference for particle MCMC or simulation-based inference;
- Stan does not natively turn an arbitrary Caputo equation into a differentiable HMC model.

### 16. Model-count and notation inconsistencies

The manuscript calls \(M_0\) through \(M_6\) “six” models in places; this is seven classes. It also alternates between derivative and integral kernels and uses \(K(s)\) for both time-domain and Laplace-domain objects.

## Required editorial action

Treat Sections 4–6 and all numerical “results” in Sections 8–10 as placeholders. Rebuild the mathematics using the results in this pack. Retain only claims that have either a proof or a reproducible computational artifact.
