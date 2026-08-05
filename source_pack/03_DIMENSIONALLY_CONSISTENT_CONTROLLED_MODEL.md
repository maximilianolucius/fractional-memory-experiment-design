# Dimensionally Consistent Controlled Model

## 1. Why a reference timescale is mandatory

For a population state \(x\),

\[
\left[{}^C D_t^\alpha x\right]=[x]\,[t]^{-\alpha}.
\]

The ecological vector field \(f(x;\theta)\), when inherited from an ordinary differential equation, has units \([x][t]^{-1}\). Therefore the dimensionally consistent commensurate Caputo model is

\[
\boxed{
\tau_0^{\alpha-1}{}^C D_t^\alpha z(t)
=f(z(t);\theta)+Bu(t)
}
\tag{1}
\]

where \(\tau_0>0\) is a declared reference time. At \(\alpha=1\), (1) reduces exactly to the ODE.

Equivalently, with \(\hat t=t/\tau_0\),

\[
{}^C D_{\hat t}^\alpha z(\hat t)
=\tau_0 f(z(\hat t);\theta)+\tau_0 Bu(\hat t).
\]

This separation prevents \(\alpha\) from silently changing the units of every ecological rate.

## 2. Nonlinear controlled strong-Allee model

Let \(z=(x,y)^\top\), with prey \(x\), predator \(y\), and

\[
P(x)=rx\left(1-\frac{x}{K}\right)\left(\frac{x}{A}-1\right).
\]

The controlled model is

\[
\tau_0^{\alpha-1}{}^C D_t^\alpha x
=P(x)-\frac{axy}{1+hx}+b_{x1}u_1+b_{x2}u_2,
\tag{2}
\]

\[
\tau_0^{\alpha-1}{}^C D_t^\alpha y
=e\frac{axy}{1+hx}-my+b_{y1}u_1+b_{y2}u_2.
\tag{3}
\]

A natural channel convention is

\[
B=\begin{pmatrix}1&0\\0&1\end{pmatrix},
\]

where \(u_1\) is net prey addition/removal and \(u_2\) is net predator release/removal. Other interventions, such as nutrients, should enter through a mechanistically stated parameter or latent environmental state rather than being inserted as an arbitrary additive term.

## 3. Linearization at an equilibrium

Let \(z^*\) satisfy \(f(z^*;\theta)=0\), define \(\xi=z-z^*\), and let

\[
J=D_z f(z^*;\theta).
\]

For small perturbations,

\[
\tau_0^{\alpha-1}{}^C D_t^\alpha \xi(t)
=J\xi(t)+Bu(t)+O(\|\xi\|^2).
\tag{4}
\]

The output model is

\[
y_k=C\xi(t_k)+\varepsilon_k,
\qquad \varepsilon_k\sim\mathcal N(0,R_k).
\tag{5}
\]

The design is

\[
d=(u,\mathcal T,C),\qquad \mathcal T=\{t_1,\dots,t_n\}.
\]

## 4. Transfer function

Assume zero initial perturbation and use the principal branch of \(s^\alpha\) on \(\mathbb C\setminus(-\infty,0]\). The Laplace transform of (4) is

\[
(q_\alpha(s)I-J)\Xi(s)=BU(s),
\]

where

\[
\boxed{
q_\alpha(s)=\tau_0^{\alpha-1}s^\alpha
=\tau_0^{-1}(s\tau_0)^\alpha.
}
\tag{6}
\]

Thus

\[
\boxed{
G_\alpha(s)=C(q_\alpha(s)I-J)^{-1}B.
}
\tag{7}
\]

Only this linearized object may be manipulated as a transfer function. For the nonlinear model, \(\mathcal L\{f(z(t))\}\neq f(Z(s))\) in general.

## 5. Competing linear model classes

### Integer-order ODE

\[
\dot\xi=J_0\xi+B_0u,
\qquad G_0(s)=C_0(sI-J_0)^{-1}B_0.
\]

### Discrete-delay model

\[
\dot\xi(t)=A_0\xi(t)+A_1\xi(t-\tau)+Bu(t),
\]

\[
G_\tau(s)=C(sI-A_0-A_1e^{-s\tau})^{-1}B.
\]

### Finite latent-state model

\[
\dot q=\bar A q+\bar B u,
\qquad y=\bar C q,
\]

\[
G_L(s)=\bar C(sI-\bar A)^{-1}\bar B.
\]

### Distributed-order model

For a normalized nonnegative weight \(w\), define

\[
Q_w(s)=\int_0^1 w(\beta)\tau_0^{-1}(s\tau_0)^\beta d\beta.
\]

Then the commensurate linear symbol is

\[
G_w(s)=C(Q_w(s)I-J)^{-1}B.
\]

The entire function \(Q_w\), not merely the mean of \(w\), controls the dynamics.
