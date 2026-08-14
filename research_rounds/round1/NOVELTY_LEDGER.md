# Novelty Ledger — Round 1

Date: 2026-08-14

## Prior art that closes broad novelty claims

### arXiv:2607.16895 — Saligrama, *When Can Safe Controllers Adapt? Information before Commitment*

**Collision:** generic safety-limited information is not new. In deterministic linear-Gaussian settings the paper reduces available precommitment information to a constrained experiment-design problem; under a single quadratic safety budget it obtains an exact generalized-Rayleigh-quotient formula, and under multiple quadratic constraints it provides semidefinite upper certificates.

**Consequence for us:** do not present `safe budget -> maximum information` or the generalized eigenvalue formula as our novelty.

### arXiv:2606.19590 — Ni, Ornik, Chou, Coogan, *Safe, Real-Time Active Model Discrimination...*

**Collision:** safe active discrimination of a finite set of uncertain nonlinear dynamical models is already an explicit research object, with robust state-input constraints and online design.

**Consequence for us:** do not claim novelty for "safe active model discrimination" in general.

### arXiv:2603.12365 / CMAME 457 (2026) 119022 — Bhattacharya, Cao, Stuart, *Optimal Experimental Design for Reliable Learning of History-Dependent Constitutive Laws*

**Collision:** Bayesian OED for history-dependent models is established, and the paper explicitly names hereditary integrals, fractional time derivatives, and internal state variables as memory representations.

**Important distinction:** its stated goal is reliable **parameter identification within selected history-dependent constitutive models**, not active mechanism discrimination between a fractional law and an increasingly expressive latent approximation class under an ecological safety barrier.

### arXiv:2508.20311 — Chaudhary, Diethelm, Farhadi, Fuchs, *An Efficient Exponential Sum Approximation of Power-Law Kernels...*

**Collision:** finite sums of exponentials for approximating fractional power-law kernels, and their conversion into auxiliary first-order ODE states, are established numerical-analysis machinery.

**Consequence for us:** the SOE approximation itself is infrastructure, not the novelty.

## Surviving novelty hypothesis

The literature stress test did **not** reveal an equivalent result organized around the following joint object:

\[
\sup_{u\in \text{common-safe inputs}}
\inf_{L\in\mathcal L_m}
D_{\rm KL}(P_{C_\alpha}^u\|P_L^u),
\]

where

1. the focal mechanism is fractional/Caputo memory,
2. the rival class is a **nested latent approximation hierarchy** indexed by complexity `m`, and
3. safety is induced by a **Strong-Allee ecological barrier** rather than only by a generic action budget.

This negative search is **not proof of absolute priority**. The defensible wording is:

> We did not find prior work that jointly characterizes safety-constrained discrimination of fractional memory against a nested finite-latent approximation hierarchy, especially under a Strong-Allee viability constraint.

## Candidate Round-1 novelty

Theorem R1 gives a uniform safe-class upper bound

\[
\Delta_{\rm safe}^{(m)}
\le
\tfrac12\|R^{-1/2}S\|^2
B_{\rm safe,m}^2 E_m(\alpha,T)^2,
\]

and therefore a **uniform collapse of robust discrimination over all safe inputs** as the latent approximation error tends to zero.

This is structurally different from the generic information-budget result of arXiv:2607.16895:

- Saligrama: safety limits information available for a fixed family of alternatives;
- our R1 mechanism: the **rival class itself becomes denser around the focal memory law as complexity grows**, while safety caps how strongly the system can be excited.

The final novelty will only be strong if Round 2 introduces a genuine Strong-Allee-dependent `B_safe` and Round 3 quantifies `E_m` for the declared latent class.
