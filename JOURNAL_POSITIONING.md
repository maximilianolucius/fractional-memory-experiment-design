# Journal Positioning — Q1 candidates

Date: 2026-08-14.  Policies verified online today (sources cited per journal).
Current shape of the submission: main paper 63 pp (11pt article, ~44 pp of text
+ 17 figures + ~6 pp references) + 23 pp supplement, LaTeX, fully self-contained.

## Candidate 1 (recommended): Communications in Nonlinear Science and Numerical Simulation (Elsevier)

- **Quartile / fit**: Q1 (Applied Mathematics / Numerical Analysis). The journal
  has an explicit **Fractional Dynamics section** (fractional dynamics, control,
  and fractional calculus) — the closest scope match for a paper whose spine is
  Caputo-vs-latent identifiability with certified fractional approximation.
  The strong-Allee ecological backbone and safe experimental design fit the
  journal's nonlinear-science breadth.
- **Length policy (verified)**: "no length limitation for contributions is set,
  but only concisely written manuscripts are published." Our 63-pp main +
  supplement split satisfies this directly; no further compression forced.
- **Template changes needed**: Elsevier `elsarticle` class (frontmatter,
  highlights 3–5 bullets, keywords, CRediT statement, declaration of
  interests); numbered references via `elsarticle-num` (current natbib
  `plain` numeric style converts trivially).
- **Risk**: the ecological-safety framing must be pitched as nonlinear-science
  methodology, not as ecology per se — the abstract already does this.
- Source: [CNSNS Guide for Authors](https://www.sciencedirect.com/journal/communications-in-nonlinear-science-and-numerical-simulation/publish/guide-for-authors)

## Candidate 2: Journal of Mathematical Biology (Springer)

- **Quartile / fit**: Q1 (Applied Math / Modeling & Simulation; core math-biology
  venue). Best fit for the ecological substance: strong-Allee predator–prey,
  safety near extinction thresholds, experimental design for ecological model
  discrimination. The fractional-calculus machinery is the methodological
  vehicle.
- **Length policy (verified)**: no explicit page or length limit in the
  submission guidelines; LaTeX preferred (Springer Nature template);
  supplementary files supported.
- **Template changes needed**: Springer Nature LaTeX template (`sn-jnl.cls`),
  MSC 2020 codes required, structured declarations section.
- **Risk**: reviewers may ask for stronger biological grounding of the
  fractional-memory hypothesis; Section on microcosm protocols (main + S6)
  is the mitigation. Interval-arithmetic certification is unusual for this
  venue (a selling point if framed as rigor, a hurdle if framed as numerics).
- Source: [JMB submission guidelines](https://link.springer.com/journal/285/submission-guidelines)

## Candidate 3: SIAM Journal on Applied Dynamical Systems (SIADS)

- **Quartile / fit**: Q1 (Applied Mathematics). Excellent fit for the
  dynamical-systems core: Matignon sectors, pole/branch-cut structure,
  invariance certificates, bifurcation-adjacent backbone analysis, and the
  certified-computation ethos (SIADS values validated numerics).
- **Length policy (verified)**: "Generally, manuscripts should not exceed
  40 pages"; exceptions require justification in the cover letter. In SIAM's
  10pt/6in×8in format our 63 pp (11pt article) re-flows to roughly 45–50 pp,
  so submission needs either (i) the exception route with a cover-letter
  justification (18 theorems + certified computation), or (ii) a further
  compression pass moving Secs. 10–11 material to the supplement.
- **Template changes needed**: SIAM macros (`siamart` class), SIAM
  supplementary-materials index (supplement is peer-reviewed there).
- **Risk**: the 40-page guideline makes this the highest-friction option;
  choose only if the dynamical-systems framing is judged the strongest review
  path.
- Source: [SIADS instructions for authors](https://epubs.siam.org/journal/siads/instructions-for-authors)

## Recommendation

Submit to **CNSNS** first (scope + explicit no-length-limit policy + fractional
dynamics section), with **JMB** as the ecology-forward alternative and **SIADS**
as the prestige dynamical-systems option requiring a length exception or a
third compression pass.  The current 63-page generic-format main paper remains longer than the chief's
35–45-page preference. CNSNS explicitly permits longer contributions provided they
are concise, while the JMB guidelines inspected do not state a page limit; SIADS
would require either further compression or a justified exception.

## Uniform pre-submission checklist (any venue)

1. Convert to the venue template; re-run the full build checks of
   FINAL_REPRODUCIBILITY.md afterwards.
2. Add venue-specific frontmatter (highlights / MSC codes / CRediT).
3. Data-availability statement: point to the reproducibility package
   (Zenodo record; use "New version" on concept DOI 10.5281/zenodo.21809908 —
   metadata creator decision pending with the operator).
4. Cover letter: one-paragraph novelty claim exactly as in
   NOVELTY_LEDGER_after_R6_CHIEF.md ("the joint construction, not the generic
   components"); for SIADS add the length-exception justification.
5. Re-run the secret scan on the final ZIP before any upload.
