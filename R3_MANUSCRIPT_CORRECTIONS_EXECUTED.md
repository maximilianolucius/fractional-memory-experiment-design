# R3-I — Manuscript corrections executed

**Round 03, researcher deliverable.** All edits are on branch `rescue/aims-desk-rejection`.
Pre-edit state is preserved in `paper/backup_preR3/` (14 files). The manuscript compiles
**clean: exit 0, 0 LaTeX errors, 0 undefined references, 0 `??` in the PDF, 24 pages.**

---

## 1. Edits made

| # | file | change | driver |
|---|---|---|---|
| 1 | `main.tex` | **Title** → "Waveform Design, Not Amplitude, Governs Safe Memory Discrimination in a Strong-Allee Predator--Prey Model" (option T1 of R3-J) | R3-F, R3-H |
| 2 | `main.tex` | **Abstract fully rewritten.** Removes the safety–informativeness trade-off as a conclusion; separates the non-binding structural obstruction from the binding latent-complexity one; states the falsification with its numbers (0.803 / 0.514 / 0.763) | R3-F, R3-E, R3-H |
| 3 | `sections/sec5.tex` | `tab:state-approx` gains an **exact two-point bound** column alongside Pinsker (`0.340 → 0.3745` at `m=4`, both `A`); caption states why the exact bound is valid | R3-G §1.1 |
| 4 | `sections/sec5.tex` | New paragraph + `tab:state-approx-large`: **response-level error and testing floor out to `m = 128`** (`4.83e−5`, floor `0.49999`), with the explicit statement that the surrogate is not the certified infimum and the floors are therefore conservative | R3-E |
| 5 | `sections/sec8.tex` | `\subsection{Safety--informativeness trade-off}` → **`{The trade-off within classical waveform families}`**; opening sentence now scopes the frontier to the six families and forward-references the falsification | R3-F |
| 6 | `sections/sec8.tex` | New `\subsection{Amplitude is the wrong knob}` (`subsec:amplitude`): three-amplitude benchmark, PRBS still crossing 71.4% at half amplitude, realised gain rising to 28.07 vs `Γ_T = 5.78`, low-amplitude runs labelled linear-certificate diagnostics | R3-H |
| 7 | `sections/sec8.tex` | New `\subsection{Waveform search: the frontier is a parameterisation artifact}` (`subsec:safe-search`) + `tab:safe-search` with all 12 designs; includes both required qualifications (existence not optimality; constraint active at `δ = 0.05`) | R3-F |
| 8 | `sections/sec8.tex` | Fig. 10 caption relabelled: frontier is "across the six classical waveform families", and states that the piecewise-constant designs lie above and to the left of every plotted point | R3-F §5 C5 |
| 9 | `sections/sec10.tex` | Discussion conclusion 3 scoped to classical families; **new conclusion 4** stating the falsification and naming latent complexity as the binding constraint | R3-F, R3-E |
| 10 | `sections/sec10.tex` | Limitations paragraph extended: search is existence-only, single amplitude, single `α`, active constraint; a posteriori certification described with its exact status (rigorous inter-node bound, refinement-based solver error) | R3-D, R3-F |
| 11 | `sections/sec10.tex` | Closing paragraph: the constrained design problem should be *solved*, quantifying the cost of not solving it (0.29 macro-accuracy) | R3-F |

## 2. Corrections from R3-J §5 that are done

- Safety–informativeness trade-off removed as a general claim from abstract, `sec8` subsection
  title, `sec10` conclusions and figure caption. ✔
- "the most informative perturbation is not the safest, by a wide margin" now scoped to classical
  families. ✔
- Pinsker replaced by the exact bound as the quoted figure, Pinsker retained for comparability. ✔
- `Ê_m^state` table extended past `m = 32`. ✔

## 3. Corrections NOT done, and why

| item | status | reason |
|---|---|---|
| Demote the `L¹` approximation novelty claim (T9b), attribute the technique to McLean (2018) | **not done** | Requires editing `sec3.tex` (theorem statements) and adding bibliography entries. This changes a *theorem's* claimed status, which I judge to be the chief's call, not mine — see R3-A §6 for the recommended wording and the reference list. **This is the largest remaining correction.** |
| Redraw Fig. 10 with the search designs included | **not done** | Caption is corrected (edit 8) so it is no longer misleading, but the figure still plots only six points. Needs `benchmark/make_figures.py` regeneration. |
| New figure: safety margin vs macro-accuracy over the 12 designs | **not done** | Recommended in R3-J §6; the paper's main result currently has no figure. |
| Withdraw the FCAA split | n/a to manuscript | Affects `ROUND_02_JOURNAL_DECISION.md`, retracted in R3-A §6. |
| Remove readings of `Ê_m^state` as a design objective | **not audited line-by-line** | R3-B §4 gives the required warning text; I did not sweep every occurrence in `sec5`/`sec7`. |
| Round-02 `THEOREM_D_NONLINEAR_LIFT.md` `A_NL` factor | retracted in R3-G, **not** in the manuscript | Theorem D-NL was never imported into the manuscript, so nothing to fix there. Do not import it. |

## 4. Build verification

```
bash paper/build_latex.sh   ->  exit 0
main.log: 0 "! " errors, 0 undefined references, 0 multiply-defined labels
main.pdf: 24 pages, 741427 bytes, 0 occurrences of "??"
new cross-references resolved: tab:state-approx-large, tab:safe-search,
                               subsec:amplitude, subsec:safe-search
```

New numbers present in the rendered PDF (verified by `pdftotext`): title, `0.803`, `163 840`,
`0.49999`, `28.07`, `pwc`, "parameterisation artifact", "Amplitude is the wrong knob".

## 5. Reversal

`cp paper/backup_preR3/main.tex paper/ && cp paper/backup_preR3/sec*.tex paper/sections/`
restores the pre-Round-03 manuscript exactly.
