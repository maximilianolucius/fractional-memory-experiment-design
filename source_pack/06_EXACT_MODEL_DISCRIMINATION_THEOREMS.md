# Exact Model-Discrimination Theorems

## Assumptions

Let

\[
G_\alpha(s)=C(q_\alpha(s)I-J)^{-1}B,
\qquad q_\alpha(s)=\tau_0^{-1}(s\tau_0)^\alpha,
\]

with \(0<\alpha<1\), and suppose \(CB\neq0\). The principal branch is used.

## Theorem 1 — a noninteger Caputo channel is not a finite-dimensional latent ODE channel

There is no finite-dimensional integer-order state-space model with transfer function

\[
G_L(s)=D+\bar C(sI-\bar A)^{-1}\bar B
\]

that equals \(G_\alpha(s)\) on a nonempty open subset of their common analytic domain.

### Proof

For \(|q_\alpha(s)|>\|J\|\), the Neumann expansion gives

\[
(q_\alpha I-J)^{-1}
=q_\alpha^{-1}\left(I+Jq_\alpha^{-1}+O(|q_\alpha|^{-2})\right).
\]

Hence

\[
G_\alpha(s)
=(CB)\tau_0^{1-\alpha}s^{-\alpha}+O(|s|^{-2\alpha}).
\tag{1}
\]

A finite-dimensional integer-order transfer function is rational. If it is strictly proper, its Laurent expansion at infinity contains only integer powers \(s^{-r}\), \(r\in\mathbb N\). If it has feedthrough, it tends to a constant. Neither can equal the noninteger leading power in (1) because \(CB\neq0\) and \(0<\alpha<1\). Equality on an open set would imply equality by analytic continuation, contradicting the incompatible asymptotics. ∎

## Corollary 1.1 — exact structural distinguishability

In an ideal experiment with a direct channel, exact broadband input–output data distinguish a noninteger Caputo model from every finite-dimensional integer-order latent model.

This is an exact statement. It does **not** imply practical distinguishability on a finite bandwidth and finite horizon.

## Theorem 2 — non-equivalence with a finite discrete-delay model

Let

\[
G_\tau(s)=C_\tau(sI-A_0-A_1e^{-s\tau})^{-1}B_\tau
\]

be a finite-dimensional retarded delay transfer function with bounded matrices. Along \(s=i\omega\),

\[
G_\tau(i\omega)=O(\omega^{-1}),
\qquad \omega\to\infty.
\]

By contrast, under \(CB\neq0\),

\[
G_\alpha(i\omega)
=(CB)\tau_0^{1-\alpha}(i\omega)^{-\alpha}+O(\omega^{-2\alpha}).
\]

Since \(\alpha\neq1\), the two transfers cannot be identical for all sufficiently large frequencies and therefore cannot be identical as analytic input–output maps.

### Proof

Because \(|e^{-i\omega\tau}|=1\), the matrix \(A_0+A_1e^{-i\omega\tau}\) remains bounded. Factor \(i\omega I\) from the delay resolvent and apply a Neumann expansion. The fractional asymptotic follows from Theorem 1. ∎

## Theorem 3 — explicit fractional high-frequency phase

If \(CB>0\) is real, then

\[
G_\alpha(i\omega)
\sim (CB)\tau_0^{1-\alpha}\omega^{-\alpha}e^{-i\alpha\pi/2}.
\]

Thus

\[
\lim_{\omega\to\infty}\arg G_\alpha(i\omega)=-\frac{\alpha\pi}{2},
\]

whereas a direct integer-order channel has asymptotic phase \(-\pi/2\). The asymptotic phase gap is

\[
\boxed{\frac{(1-\alpha)\pi}{2}.}
\]

This gives a scale-free diagnostic after gain normalization, subject to actuator bandwidth and measurement noise.

## Theorem 4 — quantitative Neumann remainder

If \(|q_\alpha(s)|\ge2\|J\|\), then

\[
\left\|G_\alpha(s)-\frac{CB}{q_\alpha(s)}\right\|
\le
\frac{2\|C\|\,\|J\|\,\|B\|}{|q_\alpha(s)|^2}.
\]

### Proof

Write

\[
(qI-J)^{-1}=q^{-1}(I-J/q)^{-1}.
\]

For \(\|J/q\|\le1/2\),

\[
\|(I-J/q)^{-1}-I\|
\le\frac{\|J/q\|}{1-\|J/q\|}
\le2\|J/q\|.
\]

Multiply on the left by \(C\), on the right by \(B\), and by \(|q|^{-1}\). ∎

## Theorem 5 — generic separating frequency for fixed models

Let \(G_1,\dots,G_M\) be scalar analytic transfer functions on a connected domain containing an interval of the imaginary axis, and suppose no pair is identical. For each pair \(i\ne j\), the zero set of

\[
G_i(i\omega)-G_j(i\omega)
\]

has no accumulation point inside the interval. Consequently, except for a measure-zero/discrete exceptional set, a frequency separates every fixed pair whose responses are evaluated there.

### Proof

A nonzero analytic function has isolated zeros. Take the finite union over model pairs. ∎

## Practical interpretation

- Exact separation is easy in principle for fixed, structurally distinct models.
- Robust separation is difficult because the response difference may be much smaller than noise.
- Composite model families can tune parameters to match one or several frequencies.
- This is why the paper needs optimal multiscale excitation rather than a generic assertion that “a chirp is informative.”
