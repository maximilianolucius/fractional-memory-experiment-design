# Final Changelog — Q1 Closeout

Date: 2026-08-14.  Baseline: chief-audited Round-6 package
(`submission-2026-08-14-round6-chiefaudit.zip`), adopted in full.

## 1. Chief Round-6 audit integrated (no claim restored)

- Chief-repaired manuscript adopted: T23 renamed/scoped as **certified
  ecological prey-response approximation** (one linearized channel, not full
  state); researcher T24 mass-only Strong-Allee witness **demoted** (kept only
  as a scope remark; its budgets used nowhere); headline testing values use
  the physical pulse cap $B=0.120$; contemporary related-work citations added;
  internal workflow language removed; fig13 conceptually corrected; fig19
  replaced by the chief's two-panel version; fig11 SHA-verified untouched.
- Chief lightweight checker re-run: 8/8 pass, ratios identical to
  `chief_round6/lightweight_check.json`.
- Chief build reproduced: 80 pp, 0 undefined, 0 warnings.

## 2. Main/supplement split (this closeout's principal change)

Main paper: **80 pp → 63 pp** (0 undefined citations/references, 0 warnings).
New `supplement.tex`: **23 pp** (xr-linked to main numbering; own bibliography;
0 undefined, 0 warnings).  Moves, by section:

- Sec. 6: full proofs of T9b, T20, T22, and the pole/branch-cut lemma →
  Supplement S2 (proof ideas retained in main); "explicit parameter choice
  for tolerance ε" subsection → S2.
- Sec. 7: full proofs of T11 and T12 → S3; practical observation design
  (spacing/cost/channels), discrimination-vs-estimation contrast, and
  constrained implementation subsections → S3 (bridging summary retained).
- Sec. 8: full proofs of T16, T17, and the linear envelope lemma → S4;
  Strong-Allee face-inequality derivations → S4 (statement of the four faces
  retained); "practical consequences" subsection → S4.
- Sec. 9 (Bayesian): main retains the utility/robust objectives, T18 and T19
  statements with proof ideas, safe-design constraints, the
  theorem/computation boundary, and fig16; joint utility, complete proofs,
  tower/greedy remarks, nested MC estimator, adaptive schedule, and the eight
  robustness axes → S5.
- Sec. 11 (prospective designs): five designs compressed to a summary list;
  full designs A–E + minimum simulation matrix → S6.
- Sec. 14 (theorem index tables) → S1.  Sec. 15 (solver validation + fig06)
  → S7.  Cross-references into moved material reworded (no dangling \ref;
  builds verified 0-undefined).

No theorem statement, scope qualifier, or chief-imposed wording was altered in
the split; kept text is verbatim from the chief-audited baseline except for
the bridging sentences and reference rewording listed above.

## 3. New closeout artifacts

- `FINAL_CLAIM_EVIDENCE_MATRIX.md` — 18 headline claims mapped to
  theorem/certification/artifacts, plus the explicit not-claimed list.
- `FINAL_REPRODUCIBILITY.md` — exact commands and expected outputs for both
  builds and all five verification layers.
- `JOURNAL_POSITIONING.md` — CNSNS (recommended), JMB, SIADS; length policies
  verified online 2026-08-14.
- `FINAL_CHANGELOG.md` — this file.

## 4. Not done / deliberately unchanged

- No new mathematical claims (closeout rule).
- Benchmark v3 and figures fig01–fig12, fig14–fig18 untouched.
- No venue-template conversion yet (depends on journal choice; checklist in
  JOURNAL_POSITIONING.md).
- Zenodo update pending operator decision on metadata creator.


## 5. Final chief consistency pass

A final package-level audit corrected residual closeout inconsistencies without
adding any research claim:

- benchmark calibration wording now matches the chief-corrected model-family scope
  (ODE/Caputo share the ecological Jacobian; DDE/latent are calibrated alternatives);
- benchmark safety language now uses low/high Allee-crossing terminology rather than
  claiming empirical designs are certified safe;
- Figure 10 was regenerated from the frozen archived JSON only, with corrected labels;
- supplement `xr` import no longer duplicates bibliography definitions;
- README / Q1 packaging metadata now matches the 63-page main + 23-page supplement;
- one Discussion typo was corrected.

Final rebuild with the shipped bibliography files: main 63 pp, supplement 23 pp,
0 undefined citations/references, 0 LaTeX/package warnings.
