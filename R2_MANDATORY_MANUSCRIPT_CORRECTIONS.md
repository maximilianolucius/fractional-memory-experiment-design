# R2_MANDATORY_MANUSCRIPT_CORRECTIONS — Task R2-G

Exact targets in the **current compiled manuscript** (`paper/main.tex` → `sections/sec1..sec11.tex`).

**First, a finding that changes the list.** The compiled manuscript contains **exactly four
theorems**, all in `sec3.tex`: `thm:T4`, `thm:T9b`, `thm:T20`, `thm:T23`. There is **no Bayesian
layer** in the compiled document (`grep` for `thm:T18`, `thm:T19`, `sec:bayesian`,
"expected posterior", "posterior update" returns nothing in `sec1–sec11`). Therefore chief items 1
and 2 **do not apply to the paper as it now compiles** — they were removed when the Q1 restructure cut
the paper to four theorems. They would reappear only if the orphan files were reintegrated (see item 8).

---

| # | Chief item | Status in the compiled manuscript | Exact target | Required action |
|---|---|---|---|---|
| 1 | Theorem 9.3 / KL of the expected posterior | **NOT PRESENT** — no Bayesian theorem is stated | — | **No action on the compiled paper.** Do not reintroduce. If the Bayesian layer is ever restored, use the expected-KL identity (`audits/MATHEMATICAL_REPAIR_NOTES.md` §6) |
| 2 | "greedy one-step MI minimizes number of experiments" | **NOT PRESENT** | — | No action; keep out |
| 3 | "theoretically optimal designs validated" | **NOT PRESENT** — `grep` for *optimal design/input/excitation*, *eigenvector*, *maximin* over `sec7`,`sec8` returns nothing | — | No action. **Keep it that way**: the benchmark compares heuristic waveform families only |
| 4 | Claiming Bayesian OED was executed | **NOT CLAIMED** | — | No action |
| 5 | "first OED for fractional systems" | **ALREADY CONCEDED** — `sec10.tex:24`: *"Safe information limits and safe active model discrimination exist as general theories~\cite{SAFE26A,SAFE26B}; no novelty is claimed for safe experimental design per se"* | `sec10.tex:24` | Keep the concession, but **move it out of the Discussion opening** into the related-work paragraph so it does not consume novelty budget (see `NOVELTY_MATRIX.md`) |
| 6 | Invalid `L²`-kernel pairing on `0<α≤1/2` | **PRESENT — must be fixed** | `sec3.tex`, `thm:T20` | Replacement text below |
| 7 | "our previous paper" provenance | **PRESENT — 3 targets** | `sec1.tex:14` (`\paragraph{Explicit relationship to the previously submitted paper.}`), `sec1.tex:19` (table caption *"Relationship between the previously submitted companion paper and the present manuscript"*), `sec10.tex:15` (`\paragraph{Relation to the previously submitted companion paper.}`) | Replacement text below |
| 8 | **NEW defect found this round** | `sec14.tex` ("Theorem Index and Proof Locations") and `sec15.tex` are **orphans**: not `\input` by `main.tex`. `sec14` makes **20 theorem references and states 0 theorems**, and **14 of its labels do not exist** in the compiled paper: `thm:T10, T11, T12, T13, T16, T17, T18, T19, T21`, `lem:linear_safety`, `lem:polebranch`, `rem:greedy`, `rem:nfl_scope`, `rem:tower` | `paper/sections/sec14.tex`, `sec15.tex` | **Delete both files from the source tree** (they describe a superseded version). Reintegrating either would produce 14 dangling references and break the build |

---

## Item 6 — replacement for `thm:T20`

**Current text (verbatim, `sec3.tex`):**
> If the admissible experiment class satisfies `‖u‖₂ ≤ B`, then the composite minimax error for testing
> the fractional response against a latent hierarchy containing an explicit competitor with error `Ê_m`
> obeys `P_e*(m) ≥ Ψ(C_obs Ê_m² B²)`, where `Ψ` is any valid equal-covariance Gaussian two-point lower
> bound (Pinsker is used in the numerical plots). Thus `P_e*(m)→1/2` whenever `Ê_m→0` and `B` remains
> bounded.

**Four defects:** (a) `‖u‖₂` pairs with `‖K_α−K_m‖_{L²}`, but `K_α∉L²(0,T)` for `α≤1/2`, so the
statement is void on part of its own asserted range; (b) `Ψ` "any valid bound" is unfalsifiable and
Pinsker is *strictly weaker* than the exact Gaussian formula (and vacuous for `d≥2√2`); (c) `C_obs` is
never defined; (d) `Ê_m` is not marked kernel-level or response-level — the two differ by
`C_res≈2.4·10³` here (Gate B).

**Replacement (use `THEOREM_C_PRIME_FINAL.md` §3):**
> **Theorem (uniform finite-experiment testing obstruction).** Let the observations be
> `y_k=μ(t_k)+ε_k`, `ε_k∼N(0,σ²)` i.i.d., `k=1,…,n`, `t_k∈(0,T]`, and let
> `E_m^G := ‖μ_F−μ_m‖_{L^∞(0,T)}/‖u‖_∞` be the **observed prey-response** discrepancy of an exhibited
> `m`-mode latent competitor. Then for every admissible input with `‖u‖_∞ ≤ U` and every sampling
> schedule,
> \[
> P_e^*\;\ge\;\Phi\!\Big(-\frac{\sqrt n}{2\sigma}\,\|C\|\,E_m^G\,U\Big),
> \]
> uniformly over waveform shape and sample placement. Hence `E_m^G→0` with `n,U,σ,T` fixed forces
> `P_e^*→1/2`.

Also: (i) delete "Pinsker is used in the numerical plots" and regenerate any figure that used it with
`Φ(−d/2)`; (ii) state `‖C‖` explicitly; (iii) label `E_m^G` as response level and cite `thm:T23` as its
source; (iv) say **"minimax lower bound via an exhibited confuser"**, not "composite minimax error",
since no prior is placed on the rival family.

## Item 7 — replacement provenance text

**`sec1.tex:14` + `sec1.tex:19` (delete the paragraph heading and the whole comparison table)** →
replace with one paragraph:
> The ecological backbone used here — the strong-Allee predator–prey model with Holling type-II
> response, its locked parameterization, the coexistence equilibrium `(x*,y*(A))` and the Jacobian
> `J(A)` — follows the companion certification study [P01], where those objects were derived and
> verified with validated numerics. Section 2 restates the equations, parameters, equilibrium and
> Jacobian used below, so that every result in this paper can be checked without consulting [P01].

**`sec10.tex:15`** → change the paragraph heading from
`\paragraph{Relation to the previously submitted companion paper.}` to
`\paragraph{Relation to the companion certification study.}` and replace every first-person reference
("our previously submitted…") by "the companion study [P01]" / "as derived in [P01]".

**Reason (non-negotiable):** the manuscript author is **Ibrahim Alraddadi**; `P01` is authored by
**Maximiliano Lucius**. First-person phrasing is a factual misstatement of authorship, and `P01` is now
a public Zenodo preprint (DOI 10.5281/zenodo.21809908), so the mismatch is externally checkable.

## Additional corrections carried from Round 01 (still applicable)

| Target | Action |
|---|---|
| `main.tex` `\AIMSTitle` | Title Case → **sentence case** (journal-dependent; see `ROUND_02_JOURNAL_DECISION.md`) |
| `main.tex` end matter | add **Acknowledgments**, **Funding**, **Data availability**; heading must match the target journal exactly |
| `main.tex` | `\bibliographystyle{plain}` → citation-order style of the target journal; add `lineno` if required |
| `bibliography.bib` | 76 entries, **27 cited** → prune or cite; audit `P01`, `SAFE26A`, `SAFE26B` (all three verified to exist this round) |
| `sec3.tex` `thm:T4` | replace the asymptotic proof by Lemma A.0 + Theorem A′ (`THEOREM_A_AUDIT.md` §4); state the `CB=0` counterexample at `α=1/2`, `A=2/7` |
| `sec3.tex` `thm:T9b` | demote: cite Jiang–Zhang (2017) for the law; state Theorem B.2 (endpoint-inclusive, root-exponential) as the paper's variant |
| anywhere | never write "equivalently"/"hence" between kernel-level and response-level errors (Gate B) |
