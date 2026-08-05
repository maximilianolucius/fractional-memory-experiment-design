# Safe Experiment Design

## 1. Safe set

Let \(\mathcal S\subset\mathbb R^n\) be a closed safe region and suppose the equilibrium \(z^*\) lies in its interior with margin

\[
\rho=\operatorname{dist}(z^*,\partial\mathcal S)>0.
\]

For the strong-Allee system, a minimal prey safety condition is typically

\[
x(t)\ge x_{\min}>A,
\]

with additional upper abundance and predator constraints as required.

## Theorem 1 — existence of a safe informative perturbation

Consider two locally well-posed Caputo models with the same safe equilibrium \(z^*\), and let their first-order input–output operators over \([0,T]\) be \(H_1\) and \(H_2\). Assume:

1. the nonlinear solution maps are continuous with respect to input amplitude on \([0,T]\);
2. there exists an admissible direction \(v\) such that
   \[
   (H_1-H_2)v\neq0;
   \]
3. \(z^*\) has positive safety margin \(\rho\).

Then there exists \(\varepsilon_0>0\) such that every

\[
u_\varepsilon=\varepsilon v,
\qquad 0<\varepsilon<\varepsilon_0,
\]

is safe for both models and has strictly positive pairwise Gaussian KL utility.

### Proof

By continuity of the solution map and the positive interior margin, there is \(\varepsilon_s>0\) such that the state remains in \(\mathcal S\) for both models when \(|\varepsilon|<\varepsilon_s\). The output difference has the expansion

\[
\mu_1(u_\varepsilon)-\mu_2(u_\varepsilon)
=\varepsilon(H_1-H_2)v+o(\varepsilon).
\]

Since the leading vector is nonzero, the difference is nonzero for sufficiently small positive \(\varepsilon\). Under nonsingular Gaussian noise, its KL divergence is a positive quadratic form. Choose \(\varepsilon_0\) below both thresholds. ∎

This proves existence, but not that the resulting information exceeds a specified operational minimum. A positive required utility creates a feasibility test.

## 2. Linear finite-horizon safety bound

For the stable linear Caputo system

\[
\tau_0^{\alpha-1}{}^C D_t^\alpha\xi=J\xi+Bu,
\]

write the impulse-response matrix

\[
H_\alpha(t)=\tau_0^{1-\alpha}t^{\alpha-1}
E_{\alpha,\alpha}(\tau_0^{1-\alpha}Jt^\alpha)B.
\]

Then

\[
\xi(t)=\int_0^tH_\alpha(t-s)u(s)ds.
\]

Define

\[
\Gamma_T=\sup_{0\le t\le T}\int_0^t\|H_\alpha(s)\|ds.
\]

If

\[
\|u\|_{L^\infty(0,T)}\le\frac{\rho}{\Gamma_T},
\]

then

\[
\sup_{0\le t\le T}\|\xi(t)\|\le\rho.
\]

This is a conservative local trust-region condition.

## 3. Fractional inward-pointing rectangle theorem

Consider a Caputo system

\[
{}^C D_t^\alpha z=F(t,z),
\qquad 0<\alpha<1,
\]

with continuous, locally Lipschitz \(F\). Let

\[
\mathcal R=\prod_{i=1}^n[\ell_i,u_i].
\]

Assume, for every \(t\) and every boundary point of \(\mathcal R\),

\[
F_i(t,z)\ge0\quad\text{when }z_i=\ell_i,
\]

\[
F_i(t,z)\le0\quad\text{when }z_i=u_i.
\]

Then \(\mathcal R\) is forward invariant.

### Proof sketch

Suppose a component exits through a lower face for the first time at \(t_*\). It attains a new minimum there. The Caputo extremum principle implies its Caputo derivative is strictly negative relative to its initial interior value, while the boundary condition requires a nonnegative derivative: contradiction. The upper-face case is analogous using a new maximum. Boundary initial conditions follow by an interior approximation argument. ∎

## 4. Strong-Allee boundary inequalities

For a rectangular design domain

\[
\mathcal R=[x_L,x_U]\times[y_L,y_U]
\]

and additive controls \((u_x,u_y)\), sufficient robust conditions are:

### Lower prey face

\[
P(x_L)-\frac{ax_Ly_U}{1+hx_L}+b_xu_x^{\min}\ge0.
\tag{1}
\]

### Upper prey face

\[
P(x_U)-\frac{ax_Uy_L}{1+hx_U}+b_xu_x^{\max}\le0.
\tag{2}
\]

### Lower predator face

\[
y_L\left(\frac{eax}{1+hx}-m\right)+b_yu_y^{\min}\ge0
\quad\text{for all }x\in[x_L,x_U].
\tag{3}
\]

### Upper predator face

\[
y_U\left(\frac{eax}{1+hx}-m\right)+b_yu_y^{\max}\le0
\quad\text{for all }x\in[x_L,x_U].
\tag{4}
\]

These inequalities can be checked with interval arithmetic over parameter uncertainty. They are sufficient, not necessary.

## 5. Experimental consequence of the Allee threshold

Negative prey pulses are scientifically informative but dangerous because the validated paper proves an extinction funnel below \(x<A\). A safe protocol should therefore:

- reserve a certified margin above \(A\);
- cap cumulative prey removal;
- use positive nutrient/prey pulses or predator perturbations when the lower-face condition fails;
- terminate adaptively if the posterior predictive probability of crossing \(x_L\) exceeds the safety level.
