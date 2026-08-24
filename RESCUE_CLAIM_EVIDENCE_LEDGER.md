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

## Round 03 additions and retractions

| # | Claim | Type | Proof / evidence | General or model-specific | Closest prior-work comparator | Status |
|---|---|---|---|---|---|---|
| 35 | **The safety–informativeness trade-off is a waveform-parameterisation artifact, not a property of the system.** At the same peak budget `U=0.100` and a hard margin `δ=0.05`, piecewise-constant designs reach BIC macro-accuracy `0.803` with **zero** Allee crossings, vs `0.514` for the only safe classical family and `0.763` for the best classical design of any kind (which crosses in 35.7% of cells) | falsification | `R3_SAFE_DESIGN_ADVERSARIAL_SEARCH.md`; Stage 1: 163 840 candidates, 87 601 safe; Stage 2: 672 cells × 100 reps, 0 divergences, identical seeds | model-specific; mechanism (parameterisation artifact) general | The manuscript's own Table `tab:benchmark-safety` is the counterexample target | **EMPIRICAL** (falsifies claim 13 as a general statement) |
| 36 | **Amplitude is the wrong knob.** Halving the amplitude leaves PRBS the most informative design while it still crosses in 71.4% of cells; realised gain *rises* to `28.07` vs the linear certificate `Γ_T=5.78` (violation 4.86×) because post-escape excursion is set by basin geometry, not by `‖u‖` | measurement | `R3_V4_REPRODUCIBILITY_CONTROL.md`; v4 complete, 2268 cells, 3 amplitudes, 0 divergences | model-specific | — | **EMPIRICAL** (refutes the Round-02 amplitude hypothesis) |
| 37 | **Reproducibility control**: v4 at `amp=0.100` reproduces frozen v3 to four decimals on a different host under a re-implemented driver (macro `0.5369` vs `0.537`; prbs `0.5836` vs `0.584`; multisine `0.5829` vs `0.583`; multiscale `0.3235` vs `0.324`; crossing rates identical) | control | same | model-specific | — | **CERTIFIED_NUMERICALLY** |
| 38 | **Validated safety classification**: 28/28 trajectory verdicts decided rigorously (12 SAFE-CERTIFIED, 16 CROSSING-CERTIFIED, 0 indeterminate) via mesh refinement plus a rigorous inter-node bound `(2F/Γ(α+1))h^α` from the Caputo modulus of continuity. **Every sampled verdict in the manuscript is confirmed.** The R3-F design is certified safe under all four model classes (margins `+0.099`…`+0.203`) | certificate | `R3_VALIDATED_SAFETY_REPORT.md` | model-specific, per-cell | — | **CERTIFIED_NUMERICALLY** (solver-error term is a refinement estimate, not an enclosure) |
| 39 | Only **two** designs are safe under *every* candidate model — multiscale and the found `pwc6`. Per-design "crossing rate" averages over model classes that differ qualitatively (`pulse` is safe under Caputo/ODE/latent3 but crosses under DDE) | certificate | `R3_VALIDATED_SAFETY_REPORT.md` §4(3) | model-specific | — | **CERTIFIED_NUMERICALLY** |
| 40 | **Interval-certified `M₂(r)`** via Hessian enclosure (no sampling): `4.896` at `r=0.0183` up to `11.778` at `r=0.40`. Round-02's sampled values understate it by 19%–76%. Certified `r_max = 0.02937` (Round 02 claimed `0.0350`); certified `U_NL = 1.419e−3`, i.e. 2.2% of the linear certificate; `ρ(0.05)/r_max = 12.5×` | certificate | `R3_NONLINEAR_CERTIFICATE_CONSTANTS.md` | model-specific | — | **CERTIFIED_NUMERICALLY**, conditional on `Γ_B`, `Γ_R` which remain **uncertified** |
| 41 | **The invariant-ball route to nonlinear safety is structurally closed** for this field: certified radius `0.0294` is `12.5×` below the margin it must protect, and validated integration certifies inputs `70×` larger | analysis | claims 38 + 40 | model-specific | Round-02 verdict was YELLOW for a different reason | **PROVED** (arithmetic on certified constants) |
| 42 | **Response-level error out to `m=128`** (not inferred from the kernel): `‖g_α−g_m‖_{L¹}` from `1.286` at `m=4` to `4.834e−5` at `m=128`; induced exact testing floor `0.4996` at `m=64` and `0.49999` at `m=128` | numerical | `R3_RESPONSE_CERT_M64_M128.md`; closed-form matrix Mittag-Leffler vs `2m`-dim LTI realisation, quadrature error 5–7 orders below the quantity | model-specific | Manuscript stops at `m=32` (floor 0.498) | **CERTIFIED_NUMERICALLY** (upper bound on `Ê_m^state`, hence floors are conservative) |
| 43 | **Kernel error and response error are distinct objects.** Same surrogate, same `L¹` norm: the plant *attenuates*, monotonically, by `1.009` at `m≈5` down to `0.675` at `m=128`. No constant propagates one into the other | analysis | `R3_RESPONSE_OPERATOR_SEMANTICS.md` §2 | general mechanism, model-specific numbers | — | **CERTIFIED_NUMERICALLY** |
| 44 | `Ê_m^state` is a **minimax** quantity (inf over rivals of sup over inputs) and is therefore valid and conservative for the obstruction, but **must not** be read as a design objective: the band maximising `sup_ω|ΔG|` (`ω≈0.4`) picks multiscale, which excites 87% of the worst case and is the **worst** design in the four-class benchmark (macro `0.514`) | analysis | `R3_RESPONSE_OPERATOR_SEMANTICS.md` §3–§4; per-input excitation spread >30× | general caution, model-specific counterexample | — | **PROVED** (the counterexample is in-paper) |
| 45 | The manuscript's testing chain (`Ê_m^state` → Young → floor) is **correct and free of gain double-counting**; Pinsker reproduces `0.340`/`0.498` exactly. The exact two-point bound is uniformly tighter: `0.3745` vs `0.340` at `m=4` | audit | `R3_NONLINEAR_DISCRIMINATION_AUDIT.md` §1 | general | — | **PROVED** (clears the manuscript) |
| 46 | **Lemma B.2 (safe form):** for every `c < π√(α(1−α))` there is `A(α,c)` with `E_m^+ ≤ A(α,c) T^α e^{−c√m}`, positive weights and rates, endpoint `t=0` included; hence `m(ε)=O(log²(1/ε))`. The endpoint split of Round 02 is **unnecessary** — the strip bound is `t`-integrable on `(0,1)` because `α>0` | theorem | `R3_THEOREM_B_RIGOROUS.md` §3–§5; three error sources bounded separately; bound verified active on 285 C-1 cells with constants `A∈[0.29,11.1]`, tight (slack `1.00×`) at `α=0.70,m=128`; `m(ε)` predicts the measured budget within a factor ~1.5 | **general** | **McLean (2018), arXiv:1606.00123** — same technique, positive weights, but on `[δ,T]` with `δ>0` | **PROVED**, but **demoted to lemma** — technique is McLean's; only the `L¹(0,T)` endpoint-inclusive form and the explicit constant are ours |
| 47 | Boundary constant: whether `c = π√(α(1−α))` is attained with a finite constant, and whether it is optimal, is **not settled**. `(cos d)^{α−1}→∞` as `d↑π/2` | open | `R3_THEOREM_B_RIGOROUS.md` §5 | general | Stahl / Gonchar–Rakhmanov give root-exponential as the *expected optimal order* for algebraic branch points | **CONJECTURAL** |

### Round 03 retractions (all of my own Round 01/02 claims)

| retracted | was | now | where |
|---|---|---|---|
| claim 13 as a general statement | "safety–informativeness trade-off" | property of six classical waveform families only | claim 35 |
| law exponent "exponential in `m`, `R²=0.995`" | `β=1` fit preferred | with `β` free, fitted `β` ranges `0.53`–`1.27` across `α` and `β=1` wins only at `α=0.95`; exponent **not resolved** | R3-A §7(c) |
| root-exponential constant "verified to 0.35%" | single-`α` reading | across five `α`, `c_fit/c_theory ∈ [0.81, 1.32]`; the 0.35% figure is **withdrawn** | R3-A §7(c) |
| `THEOREM_D_NONLINEAR_LIFT.md` §C4–C5 | `P_e^* ≥ Φ(−(√n/2σ)A_NL E_m^G U_NL)` | the factor `A_NL = ‖C‖E_α((‖J‖+M₂r)T^α)` **double-counts the gain**; as written the bound is **vacuous** (`P_e^* ≥ 2.6e−11`). Corrected, `P_e^* ≥ 0.4984` at `m=4` | claim 45, R3-G §2–§3 |
| Round-02 sampled `M₂` | `4.589` at `r=0.05` | certified `5.468` (sampling understates by 19%) | claim 40 |
| Round-02 `r_max` | `0.0350` | certified `0.02937` | claim 40 |
| `ROUND_02_JOURNAL_DECISION.md` FCAA split | separate short analysis paper (Lemma B.1 + Theorem B.2) to FCAA | **withdrawn** — would not clear novelty against McLean (2018) | R3-A §6 |
| R3-B first draft | kernel/response ratio "0.555–1.261, non-monotone" | that compared `L¹` against `H∞`; in the same norm the ratio is **monotone** `1.009 → 0.675` | claim 43 |

---

## Round 04 additions and retractions

| # | Claim | Type | Proof / evidence | General or model-specific | Closest prior-work comparator | Status |
|---|---|---|---|---|---|---|
| 48 | **The search advantage is not overfitting.** The search ran at `A=0.25` only; on the fully held-out `A=0.20` cells the searched designs lose `0.060` macro-accuracy on average while the six classical families lose `0.087`. The best searched design still leads out of sample (`0.907` vs `0.837`), and its advantage over the safe classical design is *larger* out of sample (`+0.486`) than in sample (`+0.255`) | control | `R4_MOCK_REFEREES.md` §1.1; `rescue_compute/r3_safe_design_search/r4j_leakage_test.json`, from the 672 Stage-2 cells | model-specific | — | **EMPIRICAL** (answers the strongest referee objection) |
| 49 | **Validated enclosure for 4 of 8 headline trajectories.** Piecewise-cubic Hermite reference built per element (so the kink in `z'` at each input discontinuity is exact), interval-bounded defect via a second-order Taylor form (order 2.01, `5.87e−09` at `N=12000`), one-sided log-norm Gronwall, self-consistency `e ≤ δ` verified. Rigorous lower bounds on `min x`: `0.441` (pwc6/ODE) and `0.309` (pwc6/latent3) against `A=0.25` | certificate | `rescue_compute/r4b_enclosure.py`, `r4b_enclosure_results.json` | model-specific, per trajectory | R3-D was refinement-based, not an enclosure | **PROVED** for those 4; **FAIL** for DDE ×2 and Caputo ×2 |
| 50 | The remaining 4 fail for diagnosed reasons, not for lack of effort: the DDE defect stalls at `O(h)` because input discontinuities re-enter through the retarded argument (defect concentrated in 5 elements at `t = jump + τ`, median elsewhere `4.6e−12`); the Caputo defect is capped by the PECE order (`≈1+α`), giving `≈15` after amplification | analysis | `R4_HEADLINE_SAFETY_CERTIFICATE.md` §3 | model-specific | — | **PROVED** (arithmetic on measured defects) |
| 51 | Interval-evaluating the defect directly loses the cancellation between `zhat'` and `f(zhat)` and gives an `O(h)` bound four orders above the true `O(h^3)` defect; the one-sided constant `μ` (not `‖Df‖`) is what makes the Gronwall amplification finite — `‖Df‖=1.62` would give `~10^9` | analysis | same | **general** (method note) | standard validated-integration practice | **PROVED** |
| 52 | Lemma B.2 is **prior art as a technique** and is stated as such in the manuscript: demoted to `lem:soe`, attributed to McLean (2018) with Beylkin–Monzón, Jiang et al., Trefethen–Weideman and Stahl cited, removed from every contribution list, FCAA split marked WITHDRAWN | status | `R4_PRIOR_ART_AND_THEOREM_STATUS.md`; 0 occurrences of every forbidden phrasing in `paper/` | — | McLean~(2018) | **CLOSED** (Round-03 blocking item) |

### Round 04 retractions

| retracted | was | now | where |
|---|---|---|---|
| the benchmark's latent recall as **evidence for** the latent-complexity obstruction | "even the leading safe design recovers only 0.475 recall against the finite-latent rival" offered in support, in four passages | BIC penalises the higher-dimensional model, so the recall is *consistent with* the obstruction but not evidence for it; the obstruction now rests on the analytical result alone | `sec1`, `sec8`, `sec10`, `sec11`; referee objection 2.5 |
| "validated integration certifies these trajectories" / "certified margin +0.092" | Round-03 wording | "verified a posteriori"; "verified margins"; the word *rigorous* reserved for the 4 enclosed trajectories | R4-B fallback, applied globally |
| a sentence asserting no design exceeds `0.55` recall against the latent rival | written during the 2.5 fix, **never shipped** | cell-level check gave `0.945`: the benchmark's `latent3` column is the **pooled** latent class (`latent1`+`latent3`). Sentence removed | `R4_MOCK_REFEREES.md` §3 |
| Round-03 title "Waveform Design, Not Amplitude, Governs …" | "governs" reads as a general causal claim | chief's title: "Safe discrimination of fractional, delayed, and latent memory beyond classical waveforms in a strong-Allee predator--prey model" | `main.tex` |

### Documentation gap inherited from the frozen benchmark

The `latent3` label in every v3/v4 table denotes the **pooled** latent class, not the order-3 model
alone. The manuscript does not say so. Not fixed this round because it touches the frozen v3
presentation; flagged in `ROUND_04_DECISION.md` §4.

---

## Summary counts

| Status | Count | Claims |
|---|---:|---|
| `PROVED` | 22 | 1, 2, 3, 5b, 6, 7, 8, 9, 23, 24, 25, 28, 30, 33, 34, 41, 44, 45, 46, 49 *(4 of 8)*, 50, 51 |
| `CERTIFIED_NUMERICALLY` | 13 | 5c, 10, 11, 15, 22, 26, 29, 37, 38, 39, 40, 42, 43 |
| `EMPIRICAL` | 6 | 5, 13 *(scoped)*, 14, 35, 36, 48 |
| `CONJECTURAL` | 3 | 20, 31, 47 |
| `REMOVE` | 9 | 4, 16, 17, 18, 19, 21, 27, 32, + Round-01 tightness/floor language |
| arithmetic finding | 1 | 12 |

**Headline set after Round 02:** Theorem B.2 (claim 23, proved, general) + Theorem C′ (claim 6) + the **linear** safety ceiling (claim 9) with the nonlinear one (claim 28) declared scope-limited. Theorem A′ (claim 1) supporting. *Round-01 headline set, superseded:* claims **9** (safety ceiling, general chain) + **6** (uniform obstruction
with explicit constants) + **1** (structural separation, upgraded), with **11** and **15** as the
certified/exact computational spine and **13/14** as the empirical layer.

**Six claims must be deleted or replaced before resubmission** (4, 16, 17, 18, 19, 21). Claim 18 is a
false theorem currently printed in the manuscript and is the single most urgent correction.

---

## Headline set after Round 03

**New headline:** claim **35** (the trade-off is a parameterisation artifact — a falsification of
our own claim 13) supported by **36** (amplitude is not the knob) and **38/39** (validated safety
certification), with **42/44** (the latent-complexity obstruction, which *is* binding) as the
theoretical spine and **37** (cross-host reproduction of the frozen benchmark) as the control.

**Demoted:** claim **46** (Theorem B.2) — proved and correct, but the technique is McLean (2018);
it enters as a supporting lemma with attribution, never as a headline. This supersedes the
Round-02 headline set, which led with it.

**Scoped, not deleted:** claim 13 survives only as a statement about six classical waveform
families (manuscript edits in `R3_MANUSCRIPT_CORRECTIONS_EXECUTED.md`).

**Single most urgent remaining correction:** cite McLean (2018) and the surrounding prior art and
demote `thm:T9b` in the manuscript. Not done — it changes a theorem's claimed status and is left
for the chief. See `CNSNS_COMPLIANCE_MATRIX_DRAFT.md` §2.3, which grades it *blocking*.
