# R4-E — Figure audit

**Status: DONE. New headline figure created, inserted, rendering. Fig. 10's caption scoped.**

---

## 1. The new headline figure

`paper/figures/fig24_safe_design_frontier.pdf`, referenced as `fig:safe-frontier`, placed in
`sec8` immediately after `tab:safe-search`. Vector PDF, two panels, full text width.
Generator: `benchmark/make_r4_headline_figure.py` (reads only frozen Round-03 artifacts).

**Panel (a) — safety–informativeness plane.** All twelve designs: minimum Allee margin over the
four candidate mechanisms on the horizontal axis, four-class BIC macro-accuracy on the vertical.
Encoding:

| marker | meaning |
|---|---|
| blue square | design returned by the constrained search (piecewise-constant) |
| filled green circle | classical family, no observed crossing |
| open red circle | classical family, crosses |

The safe region (`margin ≥ δ = 0.05`) is shaded, the `δ` boundary drawn, and an arrow marks the
`+0.29` accuracy gain from the only safe classical design to the leading searched design while
staying inside the safe region. Every requirement of the assignment is on the plot: six historical
families, top searched designs, margin against accuracy, and safe/unsafe status resolved under
**all four** hypotheses (from the a posteriori verification of R3-D/R4-B, not from a single-model
crossing rate).

**Panel (b) — where the gain comes from.** Per-class recall, safe classical design against leading
searched design, with the chance line at 0.25 and the three material deltas annotated
(`+0.51` Caputo, `+0.41` DDE, `+0.23` latent3). This is the panel the chief listed first as
"materially helps": it shows that the safe classical design is essentially blind to fractional and
delayed memory (0.40 / 0.45 against chance 0.25) while the searched design reaches 0.91 / 0.85.

## 2. Scope and non-optimality in the caption

The caption states, verbatim in the manuscript:

> Of the twelve designs, only multiscale and the searched \textsc{pwc}6 design are safe under
> *all four* mechanisms. […] The search establishes *existence* of such designs --- Sobol sampling
> with local refinement over the stated families, at a single amplitude and a single $\alpha$ ---
> and is not a certified global optimum.

It also names the validation protocol (56 cells × 100 replicates, identical seeds) so the figure is
readable without the body text.

## 3. Fig. 10 (`fig10_safety_tradeoff`)

Not redrawn. Its caption is corrected to state that the frontier shown is specific to the six
classical families and that the piecewise-constant designs "lie above and to the left of every
point plotted here". With Fig. 11 present, Fig. 10 is now the *setup* for the falsification rather
than a competing headline, and its caption says so.

**Judgement call, flagged for the chief:** the cleanest outcome would be to delete Fig. 10 and keep
only Fig. 11, since Fig. 11 contains all of Fig. 10's information plus the searched designs. I kept
Fig. 10 because the amplitude discussion in `subsec:amplitude` refers to the classical frontier as
a separate object, and because deleting a figure changes the numbering of everything after it. Say
the word and it goes.

## 4. Figure inventory after this round

The paper cites 19 figure files. All 19 resolve to an existing PDF in `paper/figures/`
(verified by matching every `\includegraphics` argument against the directory).

| file | status |
|---|---|
| `fig01`, `fig02`, `fig04`–`fig10`, `fig11_system_schematic`, `fig12`, `fig15`, `fig17`, `fig18`, `fig20`–`fig23` | unchanged |
| `fig10_safety_tradeoff` | caption scoped to the classical families |
| **`fig24_safe_design_frontier`** | **new, headline** |

The new file is numbered 24, not 11: a `fig11_system_schematic` already exists, and two
different figures sharing the `fig11` prefix is an invitation to a wrong-file error at
production. Nothing was pruned. The chief's item 4 ("remove/relegate redundant figures so the paper stays
concise") is **not** executed beyond the Fig. 10 caption: at 25 pages with no length limit at
CNSNS, and with every figure currently cited, I judged deletion to be the chief's call rather than
mine. The candidate for removal is Fig. 10, as above.

## 5. Artwork compliance

| requirement | status |
|---|---|
| vector format where possible | ✔ PDF, all text as glyphs, no rasterisation |
| separate figure files | ✔ all figures live in `paper/figures/` as individual PDFs |
| readable at print size | ✔ smallest label 7.0 pt at full text width |
| self-contained caption | ✔ protocol, encoding, scope and non-optimality all in caption |
| colour-blind safety | partial — the blue/green/red encoding is also distinguished by **marker shape** (square / filled circle / open circle), so the figure survives greyscale and colour-vision deficiency |
| raster resolution | n/a (no raster panels) |

## 6. Build verification

`bash paper/build_latex.sh` → exit 0, no undefined references. `pdftotext` confirms the caption
text ("Each point is one design") is present; the document is 25 pages, one more than before.
