# Exact Mathematics of the Strong-Allee Predator–Prey Baseline
\label{sp:model}

Consider

\[
f_1(x,y)=rx\left(1-\frac{x}{K}\right)\left(\frac{x}{A}-1\right)-\frac{axy}{1+hx},
\]

\[
f_2(x,y)=e\frac{axy}{1+hx}-my.
\]

The locked values inherited from the validated paper are

\[
r=\frac32,\quad K=1,\quad a=1,\quad h=\frac12,
\quad e=\frac45,\quad m=\frac25.
\]

## Theorem 1 — coexistence equilibrium

Assume \(e-mh>0\). Every positive coexistence equilibrium satisfies

\[
\boxed{x^*=\frac{m}{a(e-mh)}}.
\tag{1}
\]

For the locked parameters,

\[
\boxed{x^*=\frac23.}
\tag{2}
\]

The predator coordinate is

\[
\boxed{
y^*=\frac{1+hx^*}{a}\,r\left(1-\frac{x^*}{K}\right)
\left(\frac{x^*}{A}-1\right).
}
\tag{3}
\]

For the locked parameters,

\[
\boxed{
y^*(A)=\frac{2(2-3A)}{9A}.}
\tag{4}
\]

Hence positive coexistence exists exactly for

\[
\boxed{0<A<\frac23.}
\]

### Proof

At a positive equilibrium, \(f_2=0\) and \(y^*>0\), so

\[
\frac{eax^*}{1+hx^*}=m.
\]

Solving gives (1). Substitution into \(f_1=0\), followed by division by \(x^*>0\), gives (3). Substituting the locked rational parameters yields (2) and (4). Positivity of (4) is equivalent to \(A<2/3\). ∎

## Theorem 2 — exact Jacobian

At coexistence,

\[
J=\begin{pmatrix}
P'(x^*)-\dfrac{ay^*}{(1+hx^*)^2} & -\dfrac{ax^*}{1+hx^*}\\[1.2ex]
\dfrac{eay^*}{(1+hx^*)^2} & 0
\end{pmatrix}.
\tag{5}
\]

For the locked parameters,

\[
\boxed{
J(A)=
\begin{pmatrix}
\dfrac{7A-2}{8A} & -\dfrac12\\[1.2ex]
\dfrac{2-3A}{10A} & 0
\end{pmatrix}.
}
\tag{6}
\]

Consequently,

\[
\boxed{T(A)=\operatorname{tr}J(A)=\frac{7A-2}{8A},}
\tag{7}
\]

\[
\boxed{D(A)=\det J(A)=\frac{2-3A}{20A}.}
\tag{8}
\]

The discriminant factorizes as

\[
\boxed{
T(A)^2-4D(A)=\frac{(19A-10)(23A-2)}{320A^2}.
}
\tag{9}
\]

### Proof

Differentiate the Holling term using

\[
\frac{d}{dx}\frac{x}{1+hx}=\frac{1}{(1+hx)^2}.
\]

At coexistence, \(\partial f_2/\partial y=0\). Direct rational substitution gives (6). Equations (7)–(9) follow by elementary algebra. ∎

## Corollary 2.1 — exact breakpoints

The eigenvalue type changes at

\[
A=\frac{2}{23},\qquad A=\frac{10}{19}.
\]

The trace changes sign at

\[
A=\frac27,
\]

and coexistence disappears at

\[
A=\frac23.
\]

These are exactly the four rational breakpoints reported in the validated paper.

## Theorem 3 — Matignon boundary

For a commensurate Caputo system of order \(0<\alpha<1\), the coexistence equilibrium is locally asymptotically stable when every eigenvalue \(\mu\) of \(J\) satisfies

\[
|\arg\mu|>\frac{\alpha\pi}{2}.
\]

In the regime

\[
\frac27<A<\frac{10}{19},
\]

the eigenvalues are a complex pair with positive real part. The critical order is

\[
\boxed{
\alpha^*(A)=\frac{2}{\pi}
\arctan\left(\frac{\sqrt{4D(A)-T(A)^2}}{T(A)}\right).
}
\tag{10}
\]

Stability holds exactly for

\[
0<\alpha<\alpha^*(A).
\]

### Baseline \(A=3/10\)

\[
J=\begin{pmatrix}1/24&-1/2\\11/30&0\end{pmatrix},
\qquad T=\frac1{24},\qquad D=\frac{11}{60}.
\]

The exact critical order is

\[
\boxed{
\alpha^*\left(\frac3{10}\right)
=\frac{2}{\pi}\arctan\sqrt{\frac{2107}{5}}
\approx0.9690122761517084.
}
\tag{11}
\]

Thus \(\alpha=0.9\) is stable and \(\alpha=1\) is unstable, reproducing the certified verdict.

## Design implication

The baseline \(A=0.3\) is exceptionally informative for distinguishing a stable fractional model from the same integer-order skeleton because the models make opposite local stability predictions. It is not automatically the safest or fairest benchmark: an unstable alternative may leave the local linear regime. For controlled frequency-response comparisons in which every candidate should remain stable, use \(A\le2/7\); \(A=1/4\) is a convenient exact choice.

At \(A=1/4\),

\[
J=\begin{pmatrix}-1/8&-1/2\\1/2&0\end{pmatrix},
\qquad T=-\frac18,
\qquad D=\frac14,
\]

so the ODE and every \(0<\alpha\le1\) commensurate Caputo version are locally stable.
