# Controllability, Observability, and Informative Channels

Write the exact coexistence Jacobian as

\[
J=\begin{pmatrix}T&-c\\d&0\end{pmatrix},
\qquad c=\frac12,
\qquad d=\frac{2-3A}{10A}>0.
\]

The common fractional order changes the temporal symbol \(s\mapsto q_\alpha(s)\), but not the algebraic controllability/observability of the pair \((J,B,C)\).

## Theorem 1 — either single-species intervention controls both linearized modes

For prey intervention \(B_x=e_1\),

\[
\mathcal C_x=[B_x,JB_x]
=\begin{pmatrix}1&T\\0&d\end{pmatrix},
\]

so

\[
\det\mathcal C_x=d>0.
\]

For predator intervention \(B_y=e_2\),

\[
\mathcal C_y=[B_y,JB_y]
=\begin{pmatrix}0&-c\\1&0\end{pmatrix},
\]

so

\[
\det\mathcal C_y=c>0.
\]

Therefore either prey or predator perturbation is sufficient to excite both local modes.

## Theorem 2 — either species alone observes both linearized states

For prey-only observation \(C_x=e_1^\top\),

\[
\mathcal O_x=\begin{pmatrix}C_x\\C_xJ\end{pmatrix}
=\begin{pmatrix}1&0\\T&-c\end{pmatrix},
\qquad \det\mathcal O_x=-c\neq0.
\]

For predator-only observation \(C_y=e_2^\top\),

\[
\mathcal O_y=\begin{pmatrix}0&1\\d&0\end{pmatrix},
\qquad \det\mathcal O_y=-d\neq0.
\]

Thus the statement “both species must be observed for structural observability” is false for this linearization. Both species may still improve practical precision and robustness.

## Exact transfer channels

Define

\[
q=q_\alpha(s),\qquad
\Delta_\alpha(s)=q^2-Tq+cd=q^2-Tq+D.
\]

Then

\[
(qI-J)^{-1}
=\frac1{\Delta_\alpha(s)}
\begin{pmatrix}q&-c\\d&q-T\end{pmatrix}.
\]

The four scalar transfer functions are

\[
\boxed{G_{x\leftarrow x}(s)=\frac{q}{\Delta_\alpha(s)},}
\]

\[
\boxed{G_{y\leftarrow x}(s)=\frac{d}{\Delta_\alpha(s)},}
\]

\[
\boxed{G_{x\leftarrow y}(s)=\frac{-c}{\Delta_\alpha(s)},}
\]

\[
\boxed{G_{y\leftarrow y}(s)=\frac{q-T}{\Delta_\alpha(s)}.}
\]

## Theorem 3 — collocated channels expose the fractional order at first order

For a general channel \(G=C(qI-J)^{-1}B\), the high-frequency expansion is

\[
G(s)=\frac{CB}{q}+\frac{CJB}{q^2}+O(|q|^{-3}).
\]

If \(CB\neq0\), the leading decay is \(s^{-\alpha}\). If \(CB=0\), the leading term may be \(s^{-2\alpha}\) or lower.

For the biological channels:

- prey intervention + prey observation: \(CB=1\);
- predator intervention + predator observation: \(CB=1\);
- cross-species channels: \(CB=0\).

Therefore a collocated perturb-and-measure protocol gives the cleanest high-frequency signature of \(\alpha\). Cross-species measurements remain useful for interaction parameters and phase coupling.

## Latent environmental observability

Consider

\[
\dot\xi=J\xi+gz+Bu,
\qquad \dot z=-\lambda z+\gamma u,
\qquad y=C\xi.
\]

Let

\[
\bar A=\begin{pmatrix}J&g\\0&-\lambda\end{pmatrix},
\qquad \bar C=(C,0).
\]

Assume \(-\lambda\notin\sigma(J)\). By the PBH test, the latent mode is observable exactly when

\[
\boxed{C(J+\lambda I)^{-1}g\neq0.}
\]

### Proof

An eigenvector of \(\bar A\) for eigenvalue \(-\lambda\) can be chosen as

\[
v=\begin{pmatrix}-(J+\lambda I)^{-1}g\\1\end{pmatrix}.
\]

The latent mode is unobservable iff \(\bar C v=0\), which is precisely the negation of the displayed condition. ∎

This formula precisely states when an environmental covariate is needed: not always, but whenever the latent coupling lies in an output-invisible direction or is nearly invisible in the practical noise metric.
