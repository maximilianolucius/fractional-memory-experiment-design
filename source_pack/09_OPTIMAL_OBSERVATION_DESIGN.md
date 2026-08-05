# Optimal Observation Design

## 1. Pairwise simple models with independent measurement noise

Fix an input \(u\). Let model means be \(\mu_i(t,o)\), where \(o\) denotes the observed variable/channel. Suppose a measurement at \((t,o)\) has variance \(\sigma_o^2(t)\). Define the normalized separation score

\[
s_{12}(t,o)=
\frac{\left(\mu_1(t,o)-\mu_2(t,o)\right)^2}{2\sigma_o^2(t)}.
\tag{1}
\]

For a selected set \(S\) of independent measurements,

\[
D_{12}(S)=\sum_{(t,o)\in S}s_{12}(t,o).
\tag{2}
\]

## Theorem 1 — optimal schedule on a finite candidate grid

If exactly \(n\) distinct measurements may be selected from a finite candidate set and there are no coupling constraints, the KL-optimal schedule consists of the \(n\) candidates with largest scores \(s_{12}(t,o)\).

### Proof

The objective (2) is additive. Replacing any selected candidate by an unselected candidate with a larger score strictly improves the objective. ∎

If repeated observations are allowed with identical independent noise and no saturation, every observation is placed at a global score maximum. In practice, spacing constraints, temporal correlation, or biological cost prevent this degeneracy.

## 2. Minimum spacing

For one observation channel, candidate times \(t_1<\cdots<t_N\), and a minimum index spacing \(L\), the exact dynamic program is

\[
V(k,j)=\max\{V(k-1,j),\ s(t_k)+V(k-L,j-1)\},
\]

where \(V(k,j)\) is the best score using \(j\) observations among the first \(k\) times. This solves the constrained pairwise schedule in \(O(Nn)\).

## 3. Variable costs

If measurement \((t,o)\) has cost \(c(t,o)\) and total budget \(B\), choose binary variables \(z_{t,o}\) and solve

\[
\max\sum_{t,o}s_{12}(t,o)z_{t,o}
\]

subject to

\[
\sum_{t,o}c(t,o)z_{t,o}\le B,
\qquad z_{t,o}\in\{0,1\}.
\]

This is a 0–1 knapsack problem. For several model pairs, introduce \(q\) and constraints

\[
\sum_{t,o}s_p(t,o)z_{t,o}\ge q
\]

for every pair \(p\), yielding a maximin mixed-integer linear program.

## 4. What the exact strong-Allee linearization says about variables

The observability calculations prove:

- prey only is structurally sufficient;
- predator only is structurally sufficient;
- both species are not mathematically mandatory for state observability.

However, the direct-channel asymptotics prove:

- perturb prey and measure prey for a leading \(s^{-\alpha}\) signature;
- perturb predator and measure predator for the same reason;
- use the cross-species channel to estimate interaction terms \(c,d\) and phase coupling.

Therefore the preferred practical design is not “both species at every time.” It is:

1. high-rate collocated measurement around switching/perturbation times;
2. lower-rate cross-species measurement across the recovery interval;
3. environmental covariate measurement only when the PBH latent-mode condition is weak or prior uncertainty makes latent forcing competitive.

## 5. Parameter-estimation schedules

For parameter estimation, the Fisher information is

\[
F(S)=\sum_{(t,o)\in S}
\frac{\partial\mu(t,o)}{\partial\psi}
\frac{\partial\mu(t,o)}{\partial\psi}^\top
\frac1{\sigma_o^2(t)}.
\]

D-optimality maximizes \(\log\det F\). Unlike pairwise KL, this objective is not additive because the determinant rewards complementary sensitivity directions. Consequently, the top-separation-time theorem does not apply to D-optimal parameter schedules.
