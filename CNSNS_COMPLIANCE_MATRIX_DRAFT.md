# R3-K — CNSNS compliance matrix (draft)

**Round 03, researcher deliverable.** Target per Round-02 decision: *Communications in
Nonlinear Science and Numerical Simulation* (Elsevier), with FCAA as the stretch option —
**note that the FCAA split is withdrawn in R3-A §6**, so CNSNS is now the only target on the
table and this matrix is the operative gate.

**Status legend:** ✅ done · ⚠️ partial · ❌ not done · ℹ️ needs verification against the live
Guide for Authors (the requirements below are from my knowledge of Elsevier/CNSNS practice and
are **inferred**, not read off the current guidelines page; every ℹ️ row must be checked before
submission).

---

## 1. Scope and fit

| # | requirement | status | note |
|---|---|---|---|
| 1.1 | Nonlinear dynamics / numerical simulation core | ✅ | Fractional + delay + latent dynamics, strong-Allee bifurcation structure, large-scale simulation. Squarely in scope. |
| 1.2 | Genuine nonlinear content, not a linear study in disguise | ⚠️ | Four analytical results are **linearised** (transfer functions, testing bounds). The nonlinear content is the benchmark, the Allee-crossing analysis, R3-D certification and R3-C constants. This must be stated openly, not papered over — a referee will find it in one pass. |
| 1.3 | Numerical methods described and validated | ✅ | PECE solver validated; R3-D adds a posteriori trajectory certification; R3-H adds cross-host reproduction. |
| 1.4 | Not primarily an ecology paper | ✅ | Framing is experimental design and identifiability, ecology is the substrate. |

## 2. Novelty and overlap — the gate that failed last time

| # | requirement | status | note |
|---|---|---|---|
| 2.1 | Clear novelty statement | ⚠️ | Drafted in R3-J §4 (six items, three new). **Not yet written into the manuscript.** |
| 2.2 | No undisclosed overlap with own prior/concurrent submissions | ⚠️ | `sec10.tex` has a dedicated disclosure paragraph naming `\cite{P01}` and enumerating what is shared (strong-Allee backbone + locked parameterisation) and what is not. `RELATED_PAPER_DISCLOSURE.md` and `OVERLAP_AUDIT_PREVIOUS_SUBMISSION.md` exist. **Must be attached as a cover-letter item, not left implicit.** |
| 2.3 | Prior art on the specific technique acknowledged | ❌ | **Blocking.** R3-A establishes that the `L¹` exponential-sum construction is McLean (2018), with Beylkin–Monzón, Jiang et al., Stenger, Trefethen–Weideman and Stahl/Gonchar–Rakhmanov as context. None of these are cited and T9b is still presented as a contribution. **This is the same class of error that produced the desk rejection and must be fixed before submission.** |
| 2.4 | Headline claim survives adversarial reading | ✅ | The submitted headline was falsified by our own Round-03 search and has been replaced (R3-I edits 1, 2, 5, 7, 9). The new headline is a falsification plus a positive design result, both reproducible. |

## 3. Reproducibility and data

| # | requirement | status | note |
|---|---|---|---|
| 3.1 | Data availability statement | ❌ | Not in the manuscript. Prior artifacts are public (Zenodo DOI `10.5281/zenodo.21809908`; GitHub `maximilianolucius/fractional-memory-experiment-design`) — needs a statement pointing there plus the Round-03 additions. |
| 3.2 | Code available | ⚠️ | `benchmark/` and `rescue_compute/` are in the repo and every Round-03 number is reproducible from them. Not yet packaged or referenced from the paper. |
| 3.3 | Solver/seed/grid fully specified | ✅ | Amplitudes, seeds, cell counts, replicate counts and divergence counts are all reported (2268 cells, 0 divergences; 672 validation cells, 0 divergences). |
| 3.4 | Independent reproduction of headline numbers | ✅ | R3-H: v3 reproduces to four decimals on a different host under a re-implemented driver. Worth one sentence in the paper — few submissions can say this. |

## 4. Manuscript mechanics

| # | requirement | status | note |
|---|---|---|---|
| 4.1 | Elsevier `elsarticle` class | ❌ | Currently `aims_math_style.sty` (AIMS Mathematics). Full template conversion required. |
| 4.2 | Highlights, 3–5 bullets ≤ 85 chars each | ❌ | ℹ️ Not written. Draft below (§6). |
| 4.3 | Graphical abstract | ❌ | ℹ️ Optional at CNSNS but usual. Not prepared. |
| 4.4 | CRediT author contributions | ⚠️ | A contributions paragraph exists; needs CRediT taxonomy terms. |
| 4.5 | Declaration of competing interest | ✅ | Present. |
| 4.6 | AI-use declaration | ✅ | Present, and explicit. Keep it — removing it would be worse than any referee objection to it. |
| 4.7 | Length appropriate | ✅ | 24 pages compiled; well inside norms. |
| 4.8 | Figures at publication resolution, captions self-contained | ⚠️ | 10 figures included and rendering. Fig. 10 caption corrected but **the figure itself still plots only the six classical designs** (R3-I §3). |
| 4.9 | References complete and consistent | ⚠️ | Compiles with 0 undefined citations, but §2.3 requires adding at least six references. |

## 5. Blocking items before submission, in order

1. **§2.3 — cite the prior art and demote T9b to a lemma.** Non-negotiable. R3-A §8 gives the
   exact wording and the reference list.
2. **§4.1 — convert to `elsarticle`.**
3. **§3.1 — add data availability statement.**
4. **§2.1 — write the novelty statement into the introduction** (draft in R3-J §4).
5. **§4.8 — redraw Fig. 10 and add the margin-vs-accuracy figure** (R3-J §6).
6. **§4.2 — write highlights.**

Items 1 and 5 are the ones a referee will notice immediately; 2–4 and 6 are mechanical.

## 6. Draft highlights (≤ 85 characters each)

```
Safety-informativeness trade-off is a waveform artifact, not a system property
Piecewise-constant designs: 0.803 accuracy, zero Allee crossings, same budget
Halving input amplitude does not buy safety: 71% crossings, gain 4.9x over bound
Latent complexity, not safety, is the binding obstruction: floor 0.49999 at m=128
Validated integration certifies 70x larger safe inputs than invariant-ball bounds
```
(5 bullets, longest 81 characters.)

## 7. What I would tell the chief

The paper is now defensible on content: it reports a falsification of its own previous headline,
backed by 163 840 candidate evaluations and a 672-cell validation, plus a reproducibility control
that reproduces the frozen benchmark to four decimals. The remaining risk is **not** the science,
it is item §2.3. Submitting with T9b still framed as novel, against McLean (2018), would repeat
the exact failure mode of the desk rejection. That edit is a theorem-status change and I have
deliberately left it for the chief's decision rather than making it unilaterally.
