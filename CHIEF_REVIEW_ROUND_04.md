# CHIEF REVIEW — ROUND 04

**Branch:** `rescue/aims-desk-rejection`  
**Reviewed commit:** `a3c3976359befe14e2de9dfc0e3828b0479a3793`  
**Chief verdict:** **SCIENTIFIC PACKAGE ACCEPTED; SUBMISSION STILL BLOCKED ONLY BY FINAL FORMAT/METADATA/DATA-DEPOSIT CLOSURE**

Round 04 closes the scientific rescue. The T9b novelty problem is repaired, the headline safety language is honest, the theory section is rebuilt at the correct operator level, held-out evidence addresses the strongest computational-referee objection, and the manuscript builds cleanly.

No further open-ended mathematics is required for this submission. The next round is a short **submission-engineering closure**, not a research round.

---

# 1. Decisions now in force

## D1 — Template conversion: **AUTHORIZED AND REQUIRED**

Do it now.

The manuscript must not carry AIMS branding into a CNSNS submission. Convert the front matter and running style to the **current Elsevier/CNSNS LaTeX submission format**. Use the live Elsevier template/package if available; `elsarticle` is acceptable if it is the current Elsevier LaTeX template in the environment. The hard requirement is:

- zero `AIMS*` macros in the submission source;
- zero `aims_math_style.sty` dependency;
- zero AIMS journal banners/running headers;
- editable `.tex` source;
- CNSNS/Elsevier-compatible numbered references and front matter;
- clean build from a fresh directory.

This is an internal hard gate even if CNSNS does not mandate one specific LaTeX class.

## D2 — Keyword count: **CLOSED / PASS**

The live CNSNS Guide for Authors states **1 to 7 keywords**. The manuscript has 6. No change is required unless a keyword is scientifically improved.

Source checked 2026-08-24:
`https://www.sciencedirect.com/journal/communications-in-nonlinear-science-and-numerical-simulation/publish/guide-for-authors`

## D3 — Corresponding-author metadata: **MOSTLY RESOLVED, ONE AUTHOR CONFIRMATION STILL REQUIRED**

Public academic records consistently support:

- **Author:** Ibrahim Alraddadi
- **Affiliation:** Department of Mathematics, Faculty of Science, Islamic University of Madinah, Madinah 42351, Saudi Arabia
- **Email:** `ialraddadi@iu.edu.sa`
- **ORCID:** `0000-0002-0094-7937`

The live CNSNS submission checklist requires the corresponding author's **full contact details**, including email, full postal address **and phone numbers**.

Therefore:

- insert the public affiliation/postal code and ORCID in the manuscript/title page;
- **do not invent a phone number**;
- obtain the author's preferred corresponding-author telephone number before submission;
- ask the author to confirm the ORCID before the final metadata freeze even though it is strongly supported by published records.

## D4 — Funding: **AUTHOR CONFIRMATION REQUIRED**

Do not infer funding status from silence or from other papers.

The final source may contain exactly one of the following after author confirmation:

**No external funding:**
> This research received no external funding.

or the actual funder/grant statement supplied by the author.

Until the author answers, this remains a submission blocker.

## D5 — Data availability: **CURATED DEPOSIT, NOT “ON REQUEST”**

CNSNS currently applies Elsevier research-data **Option C**: research data must be deposited in a relevant repository and cited/linked in the article, unless sharing is impossible and the reason is stated.

Therefore the final paper will **not** use “available from the author on request.”

Prepare a curated public reproducibility package containing only material needed to reproduce or audit the published claims, not the full internal rescue history.

Minimum contents:

- `benchmark/` code required by the final manuscript;
- `rescue_compute/` scripts required by final headline claims;
- frozen machine-readable outputs used by the final tables/figures;
- exact PWC waveform parameters;
- seed formula and benchmark configuration;
- environment/dependency specification;
- `README_REPRODUCIBILITY.md` with one-command or staged reproduction instructions;
- `MANIFEST_SHA256.txt`;
- license for code/data where appropriate;
- mapping from each headline table/figure/number to script + artifact.

Exclude from the public dataset package unless independently useful:

- Chief/researcher review memos;
- rejected-claim discussion;
- recovery-plan documents;
- internal orchestration state;
- historical backups unrelated to reproducibility.

Preferred final repository: **Zenodo or another persistent research-data repository with a DOI**. The GitHub repository can remain the development source, but the manuscript should cite the frozen persistent deposit.

## D6 — Safety status: **ACCEPT THE DOWNGRADE; DO NOT DELAY SUBMISSION FOR THE OTHER FOUR ENCLOSURES**

Round 04 did the correct thing. Four headline trajectories have genuine enclosures; the remaining four have refinement/a-posteriori verification with explicitly documented limitations. The manuscript has been downgraded globally where required.

Do not spend another round forcing a rigorous DDE/Caputo enclosure unless a referee later asks. The current wording is publication-defensible.

## D7 — Fig. 10: **REMOVE FROM MAIN OR MOVE TO SUPPLEMENT**

`fig24_safe_design_frontier` strictly supersedes the old six-family frontier for the main conclusion. Keeping both consumes space and risks visually re-centering the falsified six-family story.

Preferred action: remove Fig. 10 from the main manuscript and, only if it remains useful for the amplitude-history discussion, move it to the supplement. Do not preserve it merely to avoid renumbering.

## D8 — pooled latent label: **FIX NOW WITHOUT RECOMPUTATION**

The benchmark column currently called `latent3` is actually the pooled latent class (`latent1 + latent3`) in the reported benchmark layer. This is a documentation defect, not a numerical defect.

Fix table headers/captions/text so the reader knows exactly what is pooled. Do not alter the frozen data or rerun the benchmark.

## D9 — penalty-free classifier sensitivity: **NOT A PRE-SUBMISSION BLOCKER**

The BIC decision layer is clearly declared and the manuscript no longer uses low latent recall as evidence for the analytical complexity obstruction. Do not perturb the frozen headline benchmark now. A penalty-free sensitivity analysis may be added later if requested by reviewers.

## D10 — DOI sweep: **DO BEFORE FINAL ZIP**

Complete a final DOI/reference audit for all cited references where DOIs exist. This is a quality gate, not a scientific one.

---

# 2. Submission authorization conditions

Submission becomes authorized only after all of the following are simultaneously true:

1. AIMS branding removed; current Elsevier/CNSNS LaTeX source builds cleanly.
2. Abstract remains <=250 words after conversion.
3. 6 keywords retained (within the verified CNSNS range 1–7).
4. Highlights remain 3–5 bullets, <=85 characters each including spaces, separate editable file.
5. Corresponding-author postal affiliation + ORCID inserted; **author-confirmed phone number supplied**.
6. **Funding status explicitly confirmed by the author** and inserted.
7. Curated reproducibility deposit frozen and assigned a persistent identifier/DOI; data statement cites it.
8. `latent3` pooled-label ambiguity fixed everywhere in the manuscript.
9. Fig. 10 removed from main or relegated to supplement; Fig. 24 remains the headline visual.
10. Full references/DOIs audited; all citations resolve.
11. Clean build from a fresh directory: 0 LaTeX errors, 0 undefined refs/citations, 0 BibTeX warnings.
12. Live CNSNS Guide for Authors and submission checklist rechecked **within 24 hours of submission**.
13. Final compliance matrix: **100% mandatory PASS and >=99% applicable PASS**.

Until items 5–7 are closed, the manuscript can be made submission-ready but must not be uploaded as final.

---

# 3. Scientific assessment after Round 04

The desk-rejection rescue is scientifically successful.

The final paper no longer depends on the claims that failed the adversarial audit. Its strongest contribution is now the experimentally and computationally supported **existence of safe, highly informative piecewise-constant inputs outside the six classical waveform families**, with held-out evidence showing the advantage is not an in-sample artifact. The finite-horizon latent-complexity obstruction remains a separate analytical result and is no longer conflated with the BIC behavior of the pooled latent class.

The correct editorial message is:

> A severe safety-information frontier appears if experiment design is restricted to conventional waveform families, but it is not intrinsic to the system. Expanding the design class produces safe inputs with substantially higher discrimination, while increasing latent-model complexity remains a distinct finite-horizon identifiability obstruction.

That is materially different from the manuscript desk-rejected by AIMS Mathematics and is well aligned with CNSNS's nonlinear modeling, fractional dynamics, computation and simulation scope.
