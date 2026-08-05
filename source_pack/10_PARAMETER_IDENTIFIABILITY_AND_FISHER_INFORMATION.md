# Parameter Identifiability and Fisher Information

## 1. Fractional transfer sensitivity

Let

\[
R_\alpha(s)=(q_\alpha(s)I-J)^{-1},
\qquad
G_\alpha(s)=CR_\alpha(s)B,
\]

\[
q_\alpha(s)=\tau_0^{-1}(s\tau_0)^\alpha.
\]

Then

\[
\boxed{
\frac{\partial q_\alpha}{\partial\alpha}
=q_\alpha(s)\Log(s\tau_0).
}
\tag{1}
\]

If \(J,B,C\) do not depend on \(\alpha\),

\[
\boxed{
\frac{\partial G_\alpha}{\partial\alpha}
=-C R_\alpha(s)
\left[q_\alpha(s)\Log(s\tau_0)I\right]
R_\alpha(s)B.
}
\tag{2}
\]

### Proof

Differentiate \((qI-J)R=I\):

\[
R_\alpha'=-R q_\alpha'I R.
\]

Premultiply by \(C\) and postmultiply by \(B\). ∎

For \(s=i\omega\),

\[
\Log(i\omega\tau_0)=\log(\omega\tau_0)+i\pi/2.
\]

Thus order sensitivity contains both a log-amplitude term and a phase term. The logarithm is dimensionless because \(\tau_0\) was introduced explicitly.

## 2. Ecological parameter sensitivities

If a scalar ecological parameter \(\theta_j\) enters only through \(J\),

\[
\boxed{
\frac{\partial G}{\partial\theta_j}
=C R\frac{\partial J}{\partial\theta_j}R B.
}
\tag{3}
\]

Include additional terms when \(B\) or \(C\) depends on \(\theta_j\).

## 3. Frequency-domain Fisher information

Suppose complex Fourier-response observations at frequencies \(\omega_k\) have circular Gaussian noise variance \(\sigma_k^2\) and known input coefficient \(U_k\). For real parameters \(\psi_a\), let

\[
S_{ka}=U_k\frac{\partial G(i\omega_k;\psi)}{\partial\psi_a}.
\]

Then

\[
\boxed{
F_{ab}=2\sum_k\frac{\Re\left(S_{ka}^*S_{kb}\right)}{\sigma_k^2}.
}
\tag{4}
\]

Local practical identifiability requires \(F\) to have full column rank and an acceptable condition number.

## 4. Necessary dimension count

A scalar complex frequency response supplies at most two real numbers per frequency. Therefore, for \(p\) real unknown parameters and one scalar input/output channel,

\[
\boxed{K\ge\left\lceil\frac p2\right\rceil}
\]

distinct frequencies are necessary for local rank \(p\). This is only a necessary condition; sensitivities can still be dependent.

For example, jointly estimating a gain, a local rate, and \(\alpha\) requires at least two frequencies in a scalar frequency-response experiment.

## 5. Time-domain order sensitivity equation

Define the dimensionally consistent operator

\[
\mathcal L_\alpha x
=\tau_0^{\alpha-1}{}^C D_t^\alpha x.
\]

For \(0<\alpha<1\),

\[
{}^C D_t^\alpha x(t)
=\frac1{\Gamma(1-\alpha)}
\int_0^t(t-s)^{-\alpha}x'(s)ds.
\]

Differentiation with respect to \(\alpha\) gives

\[
\frac{\partial}{\partial\alpha}{}^C D_t^\alpha x
=\psi(1-\alpha){}^C D_t^\alpha x
-\frac1{\Gamma(1-\alpha)}
\int_0^t\log(t-s)(t-s)^{-\alpha}x'(s)ds,
\tag{5}
\]

where \(\psi\) is the digamma function.

Thus

\[
\frac{\partial\mathcal L_\alpha x}{\partial\alpha}
=\tau_0^{\alpha-1}
\left[
(\log\tau_0+\psi(1-\alpha)){}^C D_t^\alpha x
-\frac1{\Gamma(1-\alpha)}
\int_0^t\log(t-s)(t-s)^{-\alpha}x'(s)ds
\right].
\tag{6}
\]

If \(S_\alpha=\partial x/\partial\alpha\) and

\[
\mathcal L_\alpha x=f(x,\theta)+Bu,
\]

then

\[
\boxed{
\mathcal L_\alpha S_\alpha
=D_xf(x,\theta)S_\alpha
-\frac{\partial\mathcal L_\alpha x}{\partial\alpha},
}
\tag{7}
\]

with \(S_\alpha(0)=0\) when the initial state is independent of \(\alpha\).

Equation (7) is the correct time-domain sensitivity equation. It can be integrated jointly with the state for Fisher-information calculations.

## 6. Structural versus practical identifiability

Use the following terminology precisely:

- **structural identifiability:** injectivity of the ideal input–output map under a stated model class and admissible input family;
- **local weak observability/identifiability:** rank of an analytic observability or sensitivity map near a nominal point;
- **practical identifiability:** posterior/profile/Fisher concentration under finite noisy data;
- **model discrimination:** separation of different model classes after optimizing or integrating over their parameters.

A full-rank sampled Fisher matrix proves none of the global structural statements by itself.
