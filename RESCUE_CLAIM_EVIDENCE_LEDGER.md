# RESCUE_CLAIM_EVIDENCE_LEDGER — Round 01, Task 8

**Unification note (operator instruction).** This file is now the **single canonical ledger** for the
rescue. It supersedes `CLAIM_EVIDENCE_LEDGER.md` (never created) and absorbs
`FINAL_CLAIM_EVIDENCE_MATRIX.md` (pre-rejection, kept only as history). Any future claim goes here.

**Status vocabulary (mandatory, no claim unlabeled).**
`PROVED` · `CERTIFIED_NUMERICALLY` · `EMPIRICAL` · `CONJECTURAL` · `REMOVE`

---

| # | Claim | Type | Proof / evidence | General or model-specific | Closest prior-work comparator | Status |
|---|---|---|---|---|---|---|
| 1 | A non-integer Caputo channel with `CB≠0` is not meromorphic near `s=0`, hence differs from every finite rational, retarded **or neutral** delay, and finite algebraic combination thereof | theorem | `THEOREM_A_AUDIT.md` §4, Theorem A′; 2-line proof from `{n−1,n}⊆E` via Lemma A.0; criterion verified numerically both directions (2.2e-16, 2.5e-16) | **general** (any `n`, any such channel) | Standard fractional-systems branch-point folklore; strictly stronger than the manuscript's asymptotic argument | **PROVED** |
| 2 | Rationality criterion: `G_α=R(s^α)` is rational **iff** `α·e∈ℤ` for all effectively present exponents `e` | lemma | `THEOREM_A_AUDIT.md` §2 (Lemma A.0), proof + numerical confirmation | **general** | Not located in the literature in this form | **PROVED** |
| 3 | With `CB=0` the separation claim **fails**: at `α=1/2`, `tr J=0`, cross channel, `G_α(s)=d/(s+cd)` exactly (occurs at `A=2/7` in this very model) | counterexample | `THEOREM_A_AUDIT.md` §3; verified `2.24e-16` | model-instantiated, general mechanism | — | **PROVED** (negative result) |
| 4 | For every `T,ε` a finite positive exponential mixture is `ε`-close to `k_α` in `L¹(0,T)` (existence only) — current `thm:T9b` | theorem | diffusive representation + quadrature | general | **Jiang–Zhang (2017)** already give an explicit `N_exp(ε)`; **Chaudhary–Diethelm et al. (2025)** refine it | **REMOVE as contribution** — cite instead |
| 5 | Complexity law in `L¹(0,T)` **including the singular endpoint**, positivity-preserving: convergence is sub-exponential and strictly faster than algebraic, so `m(ε)=O(log^κ(1/ε))`, `κ∈[1,2]` | measurement | C-1, 285 cells (Orion): 5 orders × 3 horizons × 19 budgets, `m≤128`; algebraic fit is worst at every `α` | general (kernel-level) | Published rates are uniform on `[δ,T]`, excluding `t=0` | **EMPIRICAL** — exponent **not resolved**; do not state a specific rate |
| 5b | **Lemma B.1 (scale invariance):** the *relative* `L¹` error of the best `m`-term positive exponential sum depends only on `(m,α)`, **not on `T`** | lemma | 2-line proof (`k_α(λt)=λ^{α−1}k_α(t)`, bijection of approximants); verified to `6e-17` | **general** | Jiang–Zhang's rate carries `log(T/Δt)` because it measures *uniform absolute* error | **PROVED** |
| 5c | Kernel-level safe error floors: `m=32 → 0.328`, `m=64 → 0.474`, **`m=128 → 0.4997`** (`α=0.85, δ=0.05, σ=0.02, n=120`) | numerical | C-1 `E_m` fed into Theorem D chain | model-specific constants, general chain | — | **CERTIFIED_NUMERICALLY** |
| 6 | Uniform finite-experiment testing obstruction with explicit constants: `P_e*≥Φ(−(√n/2σ)E_mU)` | theorem | `THEOREM_C_TESTING_OBSTRUCTION.md` §3, derived from scratch; exact two-point Gaussian, no inherited constants | **general** (given the observation model) | Textbook two-point Gaussian testing (Van Trees; Kay); the manuscript's `Ψ`/Pinsker version is weaker | **PROVED** |
| 7 | The exact Gaussian bound strictly dominates Pinsker (`1/2−0.19947d` vs `1/2−0.25d`; Pinsker vacuous at `d≥2√2`) | analysis | `THEOREM_C_TESTING_OBSTRUCTION.md` §4 table, verified numerically | general | — | **PROVED** |
| 8 | Any bound routed through `‖k_α−k_m‖_{L²}` is **vacuous for `α≤1/2`** (`k_α∉L²(0,T)`), so the `‖u‖₂≤B` pairing of `thm:T20` is not valid on the asserted range `0<α<1` | defect | `THEOREM_C_TESTING_OBSTRUCTION.md` §1, verified (`L²` diverges at `α=0.30,0.50`; `L¹` finite) | general | — | **PROVED** (defect to fix) |
| 9 | **Safety-constrained information ceiling**: `P_e*≥Φ(−(√n/2σ)·E_m·(x*−A−δ)/Γ_T)`, uniform over safe inputs; monotone — more safety ⇒ higher error floor | theorem | `THEOREM_D_SAFETY_INFORMATION.md` §1 (chain i–iv), constants computed this round | **general chain, linearized single channel**; specialized to strong-Allee | **`SAFE26A`** (Saligrama 2026) proves an information ceiling under safety in constrained-LQ/regret — different class, no `m`, regret not testing error | **PROVED** (scope-limited) |
| 10 | Computed constants: `Γ_T=5.7815` (`α=0.85,T=12`); `U(0.05)=0.0634`; floors 0.452 (`m=32,σ=0.02,δ=0.05`) and 0.471 (`δ=0.20`) | numerical | `THEOREM_D_SAFETY_INFORMATION.md` §2; `Ê_4,Ê_32` are certified interval enclosures of `thm:T23`; `Ê_8,Ê_16` interpolated (**flagged as illustrative, not certified**) | model-specific | — | **CERTIFIED_NUMERICALLY** (partly) |
| 11 | Certified finite-state prey-response surrogate: `‖g_α−g_m‖_{L¹}≤Ê_m^state`, `0.5335 (m=4) → 0.0070 (m=32)` at `α=0.85,T=12,A=0.25` | theorem+certificate | `thm:T23`, outward-rounded interval subdivision | **model-specific, one channel** | — | **CERTIFIED_NUMERICALLY** |
| 12 | v3 benchmark used amplitude `0.10`, i.e. **58 % above** `U(0.05)` and 167 % above `U(0.20)` ⇒ it was outside the certified-safe regime | consistency finding | this round, §3 of Theorem D file | model-specific | — | **PROVED** (arithmetic) |
| 13 | Safety–informativeness trade-off: sustained/broadband designs cross Allee at 0.36–1.00 while transient designs at 0.00–0.07, and the accuracy ordering is the reverse | empirical | `benchmark/results/nonlinear_confusion.json` (frozen v3, 1512 cells × 200 reps) | model-specific | — | **EMPIRICAL** (now *explained* by claim 9) |
| 14 | Stable-regime macro-averaged model-selection accuracy `0.537` (chance 0.25), micro `0.491`; per-class recall ODE .97 / Caputo .52 / DDE .41 / latent .24 | empirical | frozen v3 benchmark; BIC decision rule | model-specific | — | **EMPIRICAL** |
| 15 | Exact linear-Gaussian design ranking `prbs > pulse > multiscale > multisine > sinusoid > chirp` (mean min-pairwise KL, 1458 cells) | numerical | `benchmark/results/linear_factorial.json`; exact linear-Gaussian computation | model-specific but exact | — | **CERTIFIED_NUMERICALLY** |
| 16 | The optimal designs of Theorems 7.1/7.5 (principal eigenvector / maximin LP) were **computed and validated** | claim in the manuscript | none — the benchmark compares heuristic waveform families only | — | — | **REMOVE** (audit P0.8) |
| 17 | Full Bayesian OED (evidence, EIG, adaptive design, posterior safety) was implemented | claim in the manuscript | none — the decision rule is BIC | — | — | **REMOVE** (audit P0.3) |
| 18 | Theorem 9.3 sequential-information identity as printed (`KL` of the expected posterior) | theorem | **false** — the quantity is identically 0 by the tower property | — | correct form: expected KL (`audits/MATHEMATICAL_REPAIR_NOTES.md` §6) | **REMOVE / REPLACE** |
| 19 | Greedy one-step mutual-information maximization minimizes the number of experiments | claim | no proof; requires adaptive submodularity or a DP argument | — | — | **REMOVE** |
| 20 | Nonlinear (full-state) version of the safety ceiling | — | not attempted this round; needs Volterra/Grönwall continuation estimate | would be general | — | **CONJECTURAL** (declare open) |
| 21 | "First OED for fractional systems" / novelty of safe experiment design per se | positioning | precluded by FOED01–04 and `SAFE26A/B` | — | — | **REMOVE** (already conceded in text) |
| 22 | Ecological backbone (equations, locked parameters, `x*=2/3`, `y*(A)`, `J(A)`, `α*(A)`) | inherited | derived and certified in `P01` (Zenodo DOI 10.5281/zenodo.21809908); reproducible in ≤1 page | model-specific | `P01` | **CERTIFIED_NUMERICALLY** (provenance, not a contribution) |

---

## Round-02 additions and revisions

| # | Claim | Type | Proof / evidence | General or model-specific | Closest comparator | Status |
|---|---|---|---|---|---|---|
| 23 | **Theorem B.2** (endpoint-inclusive positive-SOE law): `ε_rel ≤ A(α)e^{−c(α)√m}`, `c(α)=π√(α(1−α))`, all weights positive, valid for every `T` | theorem | `THEOREM_B_ENDPOINT_COMPLEXITY_PROOF.md` §2 (10 steps; trapezoid-in-strip estimate cited from Trefethen–Weideman 2014); constant confirmed to **0.35 %** at `α=1/2` by C-1 | **general** | Jiang–Zhang (2017) `O(log(1/ε)log(T/Δt))` on `[δ,T]`; Chaudhary–Diethelm et al. (2025) on `[δ,T]` — **endpoint excluded in both** | **PROVED** |
| 24 | `m(ε)=O(log²(1/ε))` for the endpoint-inclusive problem | corollary | Theorem B.2 (not from any fit) | general | — | **PROVED** |
| 25 | **Proposition B.1** (kernel→response bridge): `‖C(ξ_F−ξ_m)‖_∞ ≤ C_res E_m^K U`, `C_res=‖C‖E_α(‖J‖T^α)(‖J‖Γ_T+‖B‖)` | theorem | `R2_OPERATOR_BRIDGE.md` §B2, via fractional Grönwall (Ye–Gao–Ding 2007); naive Neumann route shown to fail (`‖J‖‖K_α‖₁=4.95>1`) | general | — | **PROVED** |
| 26 | The bridge constant is **large**: `C_res≈2352` at `α=0.85,T=12` ⇒ kernel proximity is a weak proxy for response indistinguishability | numerical | `R2_OPERATOR_BRIDGE.md` §B2 table (`E_α(‖J‖T^α)`: 294/550/771) | model-specific | — | **CERTIFIED_NUMERICALLY** |
| 27 | Ecological error floors at `m=64,128` (`0.4742`, `0.4997`) | previously claimed | **withdrawn** — computed from `E_m^K` without a bridge; after bridging they are `0.0000`, `0.0482` | — | — | **REMOVE** (retracted) |
| 28 | **Theorem D-NL** (one-sided nonlinear safety ceiling): full nonlinear trajectory stays above `A+δ` for `‖u‖_∞≤U_NL(δ)`, with the testing floor `Φ(−(√n/2σ)A_NL E_m^G U_NL)` | theorem | `THEOREM_D_NONLINEAR_LIFT.md` §C5; constants `M₂(r)∈[4.59,6.71]`, `Γ_B=5.7815`, `Γ_R=6.2225` | general chain; **reference-model only**, single channel | `SAFE26A` (LQ/regret) | **PROVED** (scope-limited) |
| 29 | `U_NL(0.05)=1.6·10^{-3}` = **2.5 %** of the linear certificate; certifiable radius `0.035` vs ecological margin `0.367` ⇒ the nonlinear certificate is operationally vacuous | numerical | same, §C2; weighted-norm search over `w∈[0.1,2]` does not improve it | model-specific | — | **CERTIFIED_NUMERICALLY** |
| 30 | **No inward-pointing rectangle exists** around the coexistence equilibrium of this field (predator faces carry no control and `e a x/(1+hx)−m` vanishes at `x*`, interior to any such rectangle) | theorem (negative) | `THEOREM_D_NONLINEAR_LIFT.md` §C3; exhaustive 24³ geometry search finds none at any `δ` | **general for this field class** | contradicts the applicability of `source_pack` `T17`/§4 | **PROVED** (negative) |
| 31 | Robust (hierarchy-uniform) nonlinear safety | target | not proved; blocked by claim 30 | — | — | **CONJECTURAL** (declared open) |
| 32 | Theorem C′ "tight to first order in `d`" | previously claimed | **withdrawn**: only the final Gaussian step is exact; Young and `‖·‖₂≤√n‖·‖_∞` slack is unquantified (up to `√n≈11` at `n=120`) | — | — | **REMOVE** (retracted) |
| 33 | Manuscript defect: `sec14.tex`/`sec15.tex` are orphans; `sec14` makes 20 theorem references, states 0 theorems, and **14 of its labels do not exist** in the compiled paper | audit finding | `R2_MANDATORY_MANUSCRIPT_CORRECTIONS.md` item 8 | model-specific | — | **PROVED** (arithmetic) |
| 34 | Manuscript status: the **Bayesian layer is absent** from the compiled paper, so the false Theorem 9.3 and the greedy-MI claim are **no longer present** | audit finding | `grep` over `sec1–sec11`: 4 theorems only (`T4,T9b,T20,T23`) | model-specific | — | **PROVED** (supersedes Round-01 urgency call) |

### Revisions to Round-01 rows

- **claim 5** → now reads: *over `m≤128`, stretched-exponential fits outperform a single algebraic fit
  for the tested orders; the asymptotic class remains unresolved by C-1* (**EMPIRICAL**). The asymptotic
  statement is carried by claim 24 instead (**PROVED**).
- **claim 5c** (kernel-level floors) → valid **only** for the abstract convolution-kernel model; the
  ecological reading is removed (see claim 27).
- **claim 5b** (Lemma B.1) → unchanged, **PROVED**.
- **claims 9/10** (linear safety ceiling and its constants) → unchanged and valid, but must now be
  labelled **linear certificate**; the nonlinear counterpart is claim 28.

---

## Summary counts

| Status | Count | Claims |
|---|---:|---|
| `PROVED` | 15 | 1, 2, 3, 5b, 6, 7, 8, 9, 23, 24, 25, 28, 30, 33, 34 |
| `CERTIFIED_NUMERICALLY` | 7 | 5c, 10, 11, 15, 22, 26, 29 |
| `EMPIRICAL` | 3 | 5, 13, 14 |
| `CONJECTURAL` | 2 | 20, 31 |
| `REMOVE` | 9 | 4, 16, 17, 18, 19, 21, 27, 32, + Round-01 tightness/floor language |
| arithmetic finding | 1 | 12 |

**Headline set after Round 02:** Theorem B.2 (claim 23, proved, general) + Theorem C′ (claim 6) + the **linear** safety ceiling (claim 9) with the nonlinear one (claim 28) declared scope-limited. Theorem A′ (claim 1) supporting. *Round-01 headline set, superseded:* claims **9** (safety ceiling, general chain) + **6** (uniform obstruction
with explicit constants) + **1** (structural separation, upgraded), with **11** and **15** as the
certified/exact computational spine and **13/14** as the empirical layer.

**Six claims must be deleted or replaced before resubmission** (4, 16, 17, 18, 19, 21). Claim 18 is a
false theorem currently printed in the manuscript and is the single most urgent correction.
