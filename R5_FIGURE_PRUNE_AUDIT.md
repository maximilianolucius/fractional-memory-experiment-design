# R5-G — Figure pruning

**Status: DONE. Fig. 10 removed from the main manuscript, not relegated to the supplement.**

---

## 1. What was removed

`fig10_safety_tradeoff` — the six-family safety–informativeness frontier — is gone from `sec8`,
together with its `figure` environment, caption and `fig:safety-tradeoff` label. The one prose
reference to it, in `sec10`, was rewritten to point at `fig:safe-frontier` instead.

**Not moved to the supplement.** The chief allowed relegation "only if it remains useful for the
amplitude-history discussion". It is not: `subsec:amplitude` makes its point with the three-amplitude
crossing rates and the realised-gain numbers, which are quantitative and in a table, and the
classical frontier itself is fully contained in panel (a) of the headline figure as the six circle
markers. Keeping the plot anywhere in the submission would re-centre a story the paper refutes.

The PDF file stays in `paper/figures/` and in git history, so the desk-rejected version remains
reproducible.

## 2. What the headline figure now carries alone

`fig24_safe_design_frontier`, `fig:safe-frontier`, in `sec8` after the waveform-search table:

- panel (a): all twelve designs in the margin-vs-accuracy plane, with safe/unsafe status resolved
  under **all four** candidate mechanisms (not a single-model crossing rate), the `δ = 0.05`
  boundary drawn, and the `+0.29` gain from the safe classical design to the leading searched design
  annotated inside the safe region;
- panel (b): per-class recall of those two designs, showing the gain concentrated on the Caputo
  (`+0.51`) and delayed (`+0.41`) mechanisms.

Caption states the validation protocol, that only two of twelve designs are safe under all four
mechanisms, and that the search gives existence rather than a certified global optimum.

## 3. Reference integrity after removal

| check | result |
|---|---:|
| `fig:safety-tradeoff` references remaining | **0** |
| `fig10_safety_tradeoff` `\includegraphics` remaining | **0** |
| undefined references after rebuild | **0** |
| figures cited by the manuscript | 18 |
| cited figures whose PDF exists | **18/18** |

## 4. Remaining redundancy, flagged not acted on

The manuscript still cites 18 figures. Two are plausible further cuts:

- `fig05_linear_ranking` — the linear-Gaussian design ranking, largely superseded by the nonlinear
  benchmark that follows it;
- `fig18_safe_discrimination_atlas` — the protocol-restricted discrimination atlas, which overlaps
  the response-level table now extended to `m = 128`.

Neither is misleading, and CNSNS sets no figure limit ("no length limitation… but only concisely
written manuscripts are published"). I did not cut them because the case is a judgement about
concision rather than correctness, unlike Fig. 10 where the figure actively re-centred a refuted
claim. Say the word and either goes.
