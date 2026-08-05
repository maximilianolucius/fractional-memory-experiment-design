# Exponential Mixtures, Finite-Horizon Approximation, and an Impossibility Result

All formulas below use nondimensional time. Restore units with \(t/\tau_0\).

## Theorem 1 — exact positive diffusive representation

For \(0<\alpha<1\), the fractional integral kernel

\[
k_\alpha(t)=\frac{t^{\alpha-1}}{\Gamma(\alpha)}
\]

has the exact representation

\[
\boxed{
k_\alpha(t)=\frac{\sin(\pi\alpha)}{\pi}
\int_0^\infty \lambda^{-\alpha}e^{-\lambda t}\,d\lambda.
}
\tag{1}
\]

The derivative-memory kernel also satisfies

\[
\boxed{
\frac{t^{-\alpha}}{\Gamma(1-\alpha)}
=\frac{\sin(\pi\alpha)}{\pi}
\int_0^\infty \lambda^{\alpha-1}e^{-\lambda t}\,d\lambda.
}
\tag{2}
\]

### Proof

Use

\[
\int_0^\infty \lambda^{\nu-1}e^{-\lambda t}d\lambda
=\Gamma(\nu)t^{-\nu}
\]

and Euler’s reflection identity

\[
\Gamma(\alpha)\Gamma(1-\alpha)=\frac{\pi}{\sin\pi\alpha}.
\]

Set \(\nu=1-\alpha\) for (1) and \(\nu=\alpha\) for (2). ∎

## Consequence

Fractional memory is exactly an **infinite continuum of exponential relaxation modes**. A finite latent ODE model is a quadrature approximation to this continuum.

## Theorem 2 — uniform approximation at the singular endpoint is impossible

No finite exponential sum

\[
k_m(t)=\sum_{j=1}^m c_je^{-\lambda_jt}
\]

with finite coefficients can approximate \(k_\alpha\) uniformly on \([0,T]\) when \(0<\alpha<1\).

### Proof

Every finite sum has finite value \(k_m(0)=\sum_jc_j\). But

\[
\lim_{t\downarrow0}k_\alpha(t)=+\infty.
\]

Therefore \(\sup_{0\le t\le T}|k_\alpha(t)-k_m(t)|=\infty\). ∎

This corrects any claim of a uniform absolute-error approximation on an interval containing zero.

## Theorem 3 — constructive finite \(L^1(0,T)\) approximation

Let

\[
c_\alpha=\frac{\sin(\pi\alpha)}{\pi}.
\]

Choose \(0<\ell<L\), divide \([\ell,L]\) into \(m\) equal intervals of width

\[
h=\frac{L-\ell}{m},
\]

and use left nodes \(\lambda_j=\ell+(j-1)h\). Define

\[
k_m(t)=c_\alpha h\sum_{j=1}^m\lambda_j^{-\alpha}e^{-\lambda_jt}.
\tag{3}
\]

Then

\[
\boxed{
\|k_\alpha-k_m\|_{L^1(0,T)}
\le c_\alpha\left[
\frac{T\ell^{1-\alpha}}{1-\alpha}
+\frac{L^{-\alpha}}{\alpha}
+Th\ell^{-\alpha}
\right].
}
\tag{4}
\]

### Proof

Split (1) into \((0,\ell)\), \([\ell,L]\), and \((L,\infty)\).

For the low-rate tail,

\[
\int_0^T\int_0^\ell \lambda^{-\alpha}e^{-\lambda t}d\lambda dt
\le T\int_0^\ell\lambda^{-\alpha}d\lambda
=\frac{T\ell^{1-\alpha}}{1-\alpha}.
\]

For the high-rate tail, Tonelli’s theorem gives

\[
\int_0^T\int_L^\infty \lambda^{-\alpha}e^{-\lambda t}d\lambda dt
=\int_L^\infty\lambda^{-\alpha-1}(1-e^{-\lambda T})d\lambda
\le\frac{L^{-\alpha}}{\alpha}.
\]

For fixed \(t\), \(\lambda^{-\alpha}e^{-\lambda t}\) is decreasing in \(\lambda\). The gap between left and right Riemann sums on \([\ell,L]\) is at most

\[
h\left(\ell^{-\alpha}e^{-\ell t}-L^{-\alpha}e^{-Lt}\right)
\le h\ell^{-\alpha}.
\]

Integrate over \(t\in[0,T]\), multiply by \(c_\alpha\), and add the three errors. ∎

## Explicit parameter choice for tolerance \(\varepsilon\)

It suffices to choose

\[
\ell=\left(\frac{\varepsilon(1-\alpha)}{3c_\alpha T}\right)^{1/(1-\alpha)},
\]

\[
L=\left(\frac{3c_\alpha}{\alpha\varepsilon}\right)^{1/\alpha},
\]

\[
h\le\frac{\varepsilon\ell^\alpha}{3c_\alpha T},
\qquad
m\ge\frac{L-\ell}{h}.
\]

This construction is conservative, not complexity-optimal. It is sufficient for a complete existence theorem.

## Theorem 4 — output approximation

For \(u\in L^2(0,T)\),

\[
\boxed{
\|(k_\alpha-k_m)*u\|_{L^2(0,T)}
\le\|k_\alpha-k_m\|_{L^1(0,T)}\|u\|_{L^2(0,T)}.
}
\tag{5}
\]

### Proof

This is Young’s convolution inequality. ∎

## Theorem 5 — finite-horizon no-free-lunch result

Fix a horizon \(T\), an input \(u\in L^2(0,T)\), and any output tolerance \(\eta>0\). There exists a finite positive exponential mixture \(k_m\) such that

\[
\|(k_\alpha-k_m)*u\|_{L^2(0,T)}<\eta.
\]

### Proof

By Theorem 3, choose \(m\) so that

\[
\|k_\alpha-k_m\|_1<\eta/\|u\|_2
\]

when \(u\ne0\). Apply Theorem 4. The zero-input case is trivial. ∎

## Corollary — unrestricted latent dimension destroys robust discrimination

If the alternative latent-state class allows arbitrary dimension \(m\), then for every finite experiment and every positive noise floor, a latent model can be chosen whose output lies below that noise floor. Therefore a maximin design against the unrestricted class has zero robust separation in the closure.

## Required modeling restriction

The paper must impose at least one of:

1. a fixed maximum latent dimension \(m\);
2. a lower bound/spacing constraint on latent rates;
3. a complexity penalty or prior that shrinks large \(m\);
4. a specified experimental bandwidth and horizon;
5. auxiliary environmental measurements that constrain the latent mechanism.

Without such a restriction, “fractional versus latent” is not a well-posed finite-data contest.
