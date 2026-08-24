# ROUND_02_JOURNAL_DECISION — Task R2-H

> **WITHDRAWN (Round 04, chief decision).** The FCAA split proposed in this document is
> **formally withdrawn**. R3-A established that the positive-SOE / log-quadrature construction is
> prior art (McLean 2018), so a standalone analysis paper built on it would not clear novelty.
> `thm:T9b` has been demoted to a supporting lemma in the manuscript and removed from every
> contribution list. **CNSNS is the sole active target.** See `R4_PRIOR_ART_AND_THEOREM_STATUS.md`.


**Outcome-map classification: `H3′` — a hybrid the map does not name.**
- Nonlinear lift (`R2-C`): **YELLOW** — a one-sided nonlinear theorem is proved but is operationally
  vacuous (`U_NL` = 2.5 % of the linear certificate). *Not* the GREEN of `H1`/`H2`.
- Endpoint complexity theorem (`R2-D`): **GREEN** — Theorem B.2 proved, `c(α)=π√(α(1−α))`, confirmed
  to 0.35 % at `α=1/2`. *Better* than `H3` assumes.
- Operator bridge (`R2-B`): proved, but it **removes** the large-`m` ecological floors.

Net: the paper's mathematical core is now **correct and partly stronger**, but its *ecological* safety
claim is weaker than at the end of Round 01. Recommendation follows `H3`, with one strategic addition.

---

## Primary recommendation: **CNSNS** (Communications in Nonlinear Science and Numerical Simulation)

**Official scope (paraphrase + quote), consulted 2026-08-24.** The journal "publishes original
research findings on experimental observation, mathematical modeling, theoretical analysis and
numerical simulation, for more accurate description, better prediction or novel application, of
nonlinear phenomena in science and engineering", and explicitly lists among its topics **"nonlinear
differential or delay equations"**, **"fractals, fractional calculus and dynamics"**, **"computational
methods and simulations in nonlinear science and engineering"** and **"biological physics and
networks"**. Cross-disciplinary submissions are "particularly encouraged". No length limit, but only
concisely written manuscripts are published. Single-anonymized review, ≥2 reviewers.
Source: <https://www.sciencedirect.com/journal/communications-in-nonlinear-science-and-numerical-simulation/publish/guide-for-authors> (accessed 2026-08-24).

**Manuscript fit — strong, and it is the *only* venue on the shortlist whose scope names every
component we actually have:** fractional dynamics (Caputo memory), delay equations (DDE rival),
theoretical analysis (Theorems A′, B.2, C′, D-NL), numerical simulation (v3/v4 benchmarks, validated
solver), and a biological system. The paper does not have to be recast to fit; it fits as-is.

**Main desk-rejection risk.** "Modeling + simulation study with supporting theory." CNSNS sees many
fractional predator–prey papers, so the discriminator must be visible in the abstract: this is an
**identifiability/impossibility** result, not another model-and-simulate paper.

**Emphasize:** (i) the safety–informativeness trade-off as a *quantified* obstruction with certified
constants; (ii) Theorem B.2 (endpoint-inclusive positive-SOE law) — a genuinely new analytic result in
their core topic; (iii) the delay/latent/fractional three-way discrimination with an explicit
complexity budget; (iv) reproducibility (released code + machine-readable results).
**De-emphasize:** the companion-paper provenance (one paragraph, no table); the BIC benchmark as a
headline; any Bayesian-OED vocabulary; the word "optimal" applied to designs that were not optimized.

**Mandatory submission source.** Elsevier editorial system for CNSNS; Guide for Authors at the URL
above, **to be re-downloaded within 24 h of submission**. Elsevier accepts LaTeX via the generic
`elsarticle` class (single-column preferred for review); Elsevier does **not** require the AIMS-style
front matter currently in `main.tex`.

**Preliminary compliance gaps (from `REJECTED_BASELINE_AUDIT.md` §7 + this round).**
1. `paper/aims_math_style.sty` and all `\AIMS*` macros must go — migrate to `elsarticle`.
2. `\bibliographystyle{plain}` → Elsevier numeric style (`elsarticle-num`), citation order.
3. Add Acknowledgments / Funding / Data availability / CRediT author statement; Elsevier requires a
   **declaration of interests** and a **declaration of generative-AI use in the writing process**
   (separate from AIMS' heading wording).
4. Highlights (3–5 bullets, ≤85 characters each) — CNSNS/Elsevier standard, currently absent.
5. Figures as separate files, ≥300 dpi; 22 figures is high for a "concisely written" journal — cut to
   the 7–10 that carry a claim.
6. 76 bibliography entries with only 27 cited — prune.
7. Title: Elsevier does not mandate sentence case, but keep it consistent and front-load the result.

---

## Secondary / strategic: **FCAA** (Fractional Calculus and Applied Analysis) — as a *split*, not for this paper

**Official scope, consulted 2026-08-24.** "An international journal dedicated to the theory and
applications of mathematical analysis where differentiations and integrations can be of arbitrary
non-integer order", publishing "high quality articles on original results and surveys related to
fractional calculus and applied analysis, emphasizing an interdisciplinary and applied approach,
bridging pure and applied mathematics, theoretical physics, and other natural and social sciences";
Mittag-Leffler-function analysis is a named concern.
Source: <https://link.springer.com/journal/13540> and
<https://link.springer.com/journal/13540/submission-guidelines> (accessed 2026-08-24).

**Fit of the *whole* manuscript — weak.** FCAA is an analysis journal; a 1512-cell BIC benchmark and an
ecological case study are not its centre of gravity, and the paper's ecological safety claim is now the
*weakest* part (YELLOW).

**Fit of Theorem B.2 alone — strong.** An endpoint-inclusive, positivity-preserving, root-exponential
complexity law for approximating the Caputo kernel by positive exponential sums, with an explicit
constant `c(α)=π√(α(1−α))`, plus **Lemma B.1** (horizon invariance of the relative `L¹` error), sits
exactly in FCAA's scope and improves on the published `[δ,T]` results in the norm that matters for
convolution-error propagation.

**Strategic recommendation.** Consider a **split**: a short analysis paper (Lemma B.1 + Theorem B.2 +
the C-1 numerical confirmation + Proposition B.1's cautionary constant) to FCAA, and the
discrimination/safety paper to CNSNS citing it. This converts the round's strongest *proved* result
into a publication in its natural venue, and relieves the CNSNS paper of carrying an analysis theorem
its readers will not evaluate. **Chief decision required.**

---

## Not recommended now

- **AIMS Mathematics** — desk-rejected this manuscript on novelty/significance. Nothing in Round 02
  strengthened the *ecological* claim (the bridge weakened it); resubmission would depend on the editor
  perceiving a materially different paper, which is a gamble we do not need to take.
- **Chaos, Solitons & Fractals** — as the chief noted, its own instructions require a strong
  physical/qualitative connection with numerics *assisting* the results; our numerics are load-bearing.
- **Automatica / IEEE TAC** — would require the robust full-state nonlinear theorem (currently YELLOW)
  and a head-to-head with `SAFE26A`.
- **Mathematical biology venues** — reserve for the `H4` branch, i.e. only if the analysis results are
  also dropped.

## Instruction respected

No submission-formatting migration has been performed. Migration to `elsarticle` awaits explicit chief
authorization after this decision.
