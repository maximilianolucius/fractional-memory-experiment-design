# NOVELTY_MATRIX — Round 01, Task 2

**Method.** Adversarial search against the *closest* literature, not generic background. Every entry
below was retrieved and read in this round (abstract level at minimum; the two decisive arXiv items
were fetched in full-abstract detail). Where a search returned nothing, that is recorded as a
*negative result with its limitation stated* — "not found" is not proof of "does not exist".

**Areas covered.** fractional system identification · fractional-vs-delay discrimination · diffusive
representation / exponential sums · rational approximation of fractional kernels · finite-horizon
identifiability · minimax testing for dynamical systems · active model discrimination · safe
experiment design · safety-constrained identification · fractional/delayed predator–prey systems.

---

## 1. The two decisive competitors (both already cited in the manuscript as `SAFE26A/B`)

### SAFE26A — Saligrama, *When Can Safe Controllers Adapt? Information before Commitment*, arXiv:2607.16895 (18 Jul 2026)

| Field | Content |
|---|---|
| Model class | Constrained **linear** systems, quadratic regulation cost; deterministic linear-Gaussian |
| Structural identifiability | no |
| Finite-horizon approximation | no |
| Explicit complexity budget *m* | **no** |
| Statistical lower bound | **yes** — information ceiling: bounded pre-commitment information (KL) leaves a fixed fraction of the oracle gap unavoidable; **Ω(T) gap ⇒ linear regret** for every uniformly safe policy |
| Uniform over bounded inputs | uniform over *plausible models* (safety must hold under all) |
| **State-safety constraint** | **yes — this is the paper's core** |
| Rigorous certificate | semidefinite upper certificates (linear-Gaussian case) |
| What it proves | Safety can forbid the informative experiment: "commitment" is the first action foreclosing a safe continuation; bounded pre-commitment information ⇒ irreducible regret |
| **What we would add** | The **hereditary/non-Markovian** analogue: the obstruction driven by *memory-kernel approximability* with an **explicit latent-complexity budget m**, measured as a **testing-error floor** (not regret), on a **finite horizon** |

**This is the single most dangerous reference for the rescue.** "Safety limits available information"
is *already a theorem* in the literature — in the LQ/regret setting. Theorem D cannot be sold as the
first safety-constrained information limit.

### SAFE26B — Ni, Ornik, Chou, Coogan, *Safe, Real-Time Active Model Discrimination and Fault Diagnosis for Nonlinear Systems via Differentiable Reachability*, arXiv:2606.19590 (2026)

| Field | Content |
|---|---|
| Model class | Continuous-time **nonlinear**, process+measurement disturbances, output feedback; **no** hereditary/fractional/delay/latent dynamics |
| Statistical lower bound | **no** — algorithm design and empirical validation only |
| Impossibility result | **no** (constructive direction) |
| State-safety constraint | yes — robust enforcement of state-input safety over a finite horizon |
| Finite-horizon kernel approximation / *m* | no |
| What it proves | A synthesis method: drives measurements to be consistent with **at most one** model (deterministic diagnosis) in <50 ms, under safety constraints |
| **What we would add** | The **converse/negative** direction: when safe excitation is *insufficient* for discrimination, with a quantitative floor |

**Reading:** SAFE26B occupies "safe active model discrimination" **constructively** (assuming models
*are* discriminable). The impossibility direction for hereditary mechanisms is complementary, not
covered.

---

## 2. Approximation literature — this is where Theorem B collides

| Work | Result | Norm / interval | Consequence for us |
|---|---|---|---|
| Jiang, Zhang, Zhang, Zhang (2017), *Fast evaluation of the Caputo fractional derivative…*, Commun. Comput. Phys.; arXiv:1511.03453 | Sum-of-exponentials approximation of `t^{-1-α}` with **uniform absolute error ε** using `N_exp = O( log(1/ε)(log log(1/ε) + log(T/Δt)) + log(1/Δt)(log log(1/ε) + log(1/Δt)) )` | uniform error, interval bounded away from the singularity via `Δt` | **A complexity law already exists** and is *stronger* than our Theorem T9b (which only asserts existence) |
| Chaudhary, **Diethelm**, Farhadi, Fuchs (2025), *An efficient exponential sum approximation of power-law kernels…*, arXiv:2508.20311 / J. Comput. Appl. Math. | Pre-specifies the number of exponentials and minimizes approximation error | explicitly on **[δ,T], δ>0 — the singular endpoint t=0 is excluded** | Confirms the field works **away from t=0** |
| Beylkin & Monzón (2005, 2010) | Constructive exponential-sum approximation | function/interval specific | Standard machinery, cited already |
| Montseny (1998) | Diffusive (continuum-of-exponentials) representation | exact identity | The starting identity, not a novelty |

**Verdict on Theorem B as currently framed.** T9b ("for every ε there exists a finite positive
mixture with L¹ distance < ε") is **weaker than published results** and must not be presented as a
contribution. The chief's requested upgrade — "obtain a complexity law" — is **already in the
literature**, so it must be *cited*, not proved.

**The genuinely open technical gap:** the published rates are for **uniform error away from the
singularity** (`[δ,T]`, or with a `Δt` cutoff). The manuscript's chain needs the error in
**`L¹(0,T)` including the singular endpoint**, because that is the norm that controls the *output*
separation through Young's inequality. Translating a `[δ,T]` uniform rate into an `L¹(0,T)` rate
with the endpoint included, **and with weights kept positive** (the latent rival must be a physically
realizable relaxation hierarchy), is the part not settled by the cited work. Computation **C-1**
measures exactly this quantity.

---

## 3. Fractional-vs-delay discrimination and finite-horizon identifiability — negative result

Searched for impossibility/indistinguishability theorems with finite-data lower bounds between
fractional and delay mechanisms (2024–2026). **Nothing found.** What exists is:

- parameter-identification *methods* for fractional-order systems with delays (operational matrices,
  block-pulse functions, Bernoulli polynomials, gradient descent — several 2024–2025 papers);
- identifiability of delay differential equations (Verduyn Lunel 2001; Belkoura et al.);
- Kharazmi et al. (2021), integer vs fractional identifiability/predictability with PINNs — an
  *empirical/inverse-problem* observation that the two are hard to separate, **not a lower bound**.

**Limitation of this finding.** Absence of search hits is weak evidence. The claim we may make is
narrow and checkable: *no lower-bound/impossibility theorem for finite-horizon discrimination between
fractional, delay and bounded-complexity latent mechanisms was located*. If a referee produces one,
the novelty claim collapses to the safety coupling only.

---

## 4. Required adversarial question — answered

> *Could a specialist reasonably say: "The four analytical results are standard consequences of known
> approximation and testing tools, with the only novelty being the ecological case study"?*

**Largely yes, as the four results currently stand.** Honest per-result assessment:

| Result | Specialist's likely objection | Defensible? |
|---|---|---|
| **T4** structural separation (`O(ω^{-α})` vs `O(ω^{-1})` / rational) | Folklore: high-frequency asymptotics of a branch-point symbol vs a rational/quasi-polynomial function. A one-paragraph exercise | **No** — supporting result at best |
| **T9b** finite-horizon approximation | Weaker than Jiang–Zhang (2017), which gives an explicit `N_exp(ε)`; the existence statement follows from the diffusive representation + quadrature | **No** — must cite, not claim |
| **T20** testing obstruction | Composition of Young's convolution inequality with a standard two-point Gaussian/Pinsker bound; `Ψ` is left unspecified ("any valid bound") | **Partly** — the statement is standard machinery; its value is as the bridge, and it is currently loose |
| **T23** certified prey-response surrogate | The interval-arithmetic enclosure is real work, but it is **model-specific** (one channel, one parameter slice) | **Yes, but not general** — it certifies, it does not generalize |

**Where the critique fails — the escape route.** The specialist's sentence would be *wrong* about one
thing: in T20 the input budget `‖u‖₂ ≤ B` is an **assumption**. Nothing in the four results derives
`B` from the dynamics. If `B` is instead *forced* by a state-safety requirement — i.e. `B = B(δ)`
obtained from the Allee margin and the system's L¹ impulse gain — then the obstruction stops being a
hypothesis about the experimenter's budget and becomes a **consequence of the ecology**. That
coupling is what SAFE26A does for LQ/regret and what nobody located does for hereditary mechanisms
with an explicit `m`.

**Therefore the theorem needed to escape the critique is exactly Theorem D**, and its novelty must be
stated narrowly: *not* "safety limits information" (Saligrama has that), *not* "exponential sums
approximate fractional kernels" (Jiang–Zhang has that), but the **composite**: safety geometry ⇒
admissible excitation bound ⇒ separation ceiling against a bounded-complexity hereditary hierarchy ⇒
testing-error floor, with the constants computable for a certified ecological operating point.

---

## 5. Surviving novelty claims (after this audit)

| # | Claim | Status |
|---|---|---|
| N1 | Safety-constrained information ceiling for **hereditary** mechanism discrimination, with explicit latent-complexity dependence and a testing-error floor | **candidate headline** — requires Theorem D (Task 6) |
| N2 | `L¹(0,T)` complexity law **including the singular endpoint**, with positivity-preserving weights, and its propagation to output separation | **candidate secondary** — requires C-1 + a proof that the endpoint term is controlled |
| N3 | Certified (interval-arithmetic) finite-state surrogate bound for the prey response at a certified operating point | **supporting, model-specific** (this is T23; keep, do not headline) |
| N4 | Structural separation (T4) | **background** — cite as known-style argument, not a contribution |
| N5 | "First OED for fractional systems" / "safe experiment design" | **dead** — FOED01–04 and SAFE26A/B preclude it; the manuscript already concedes this |

**Gate A1 verdict.** Two claims (N1, N2) can survive if the corresponding mathematics closes. N4 and
N5 must be demoted explicitly. N3 stays as certification, not as general significance.

## Sources
- [When Can Safe Controllers Adapt? Information before Commitment (arXiv:2607.16895)](https://arxiv.org/abs/2607.16895)
- [Safe, Real-Time Active Model Discrimination… (arXiv:2606.19590)](https://arxiv.org/abs/2606.19590)
- [Fast evaluation of the Caputo fractional derivative… (arXiv:1511.03453)](https://arxiv.org/abs/1511.03453)
- [An efficient exponential sum approximation of power-law kernels (arXiv:2508.20311)](https://arxiv.org/html/2508.20311)
- [Fast Evaluation of the Caputo Fractional Derivative (Commun. Comput. Phys.)](https://www.cambridge.org/core/journals/communications-in-computational-physics/article/abs/fast-evaluation-of-the-caputo-fractional-derivative-and-its-applications-to-fractional-diffusion-equations/AF5FDC74FD7A010ED0ACD291BB1A92B1)
- [Parameter identifiability of differential delay equations (Verduyn Lunel)](https://onlinelibrary.wiley.com/doi/10.1002/acs.690)
- [Identifiability and predictability of integer- and fractional-order epidemiological models (PINNs)](https://www.medrxiv.org/content/10.1101/2021.04.05.21254919.full.pdf)
