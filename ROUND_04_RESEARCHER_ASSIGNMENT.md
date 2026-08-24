# ROUND 04 — RESEARCHER ASSIGNMENT

**Branch:** `rescue/aims-desk-rejection`  
**Role:** Researcher under Chief review  
**Round objective:** **submission closure for CNSNS** — no new open-ended theory unless required to close a stated gate.

Read first:

1. `CHIEF_REVIEW_ROUND_03.md`
2. `ROUND_03_DECISION.md`
3. `R3_THEOREM_B_RIGOROUS.md`
4. `R3_SAFE_DESIGN_ADVERSARIAL_SEARCH.md`
5. `R3_VALIDATED_SAFETY_REPORT.md`
6. `R3_RESPONSE_OPERATOR_SEMANTICS.md`
7. `R3_RESPONSE_CERT_M64_M128.md`
8. `R3_NONLINEAR_DISCRIMINATION_AUDIT.md`
9. `R3_MANUSCRIPT_CORRECTIONS_EXECUTED.md`
10. `CNSNS_COMPLIANCE_MATRIX_DRAFT.md`

Round 04 has **hard stop gates**. If a scientific claim cannot be made rigorous, downgrade the wording; do not manufacture a certificate.

---

# R4-A — mandatory demotion and prior-art repair

## Decision already made by Chief

Current `thm:T9b` is **not** a headline theorem/contribution.

### Required manuscript changes

1. In `paper/sections/sec3.tex`, replace the current theorem environment for T9b by a **supporting lemma**.
2. Preserve the useful statements:
   - exact scaling `E_m^+(α,T)=T^αE_m^+(α,1)`;
   - for every `c<π√(α(1−α))`, existence of `A(α,c)` with positive weights/rates and
     `E_m^+≤A(α,c)T^αe^{-c√m}`;
   - `m(ε)=O(log²(1/ε))` with the prefactor handled honestly.
3. State explicitly that the exponential-sum/log-quadrature technique and positive weights are prior art.
4. Add and cite **William McLean, “Exponential Sum Approximations for t^{-β},” Contemporary Computational Mathematics, Springer, 2018, pp. 911–930, DOI 10.1007/978-3-319-72456-0_40**, plus the already relevant Beylkin–Monzón/Jiang references.
5. Cite the actual quadrature source invoked by the proof (Stenger / Trefethen–Weideman as appropriate).
6. Keep the unrestricted-latent-dimension finite-horizon closure statement as a **corollary**.
7. Remove T9b/B.2 from every headline contribution/novelty list.
8. Remove all FCAA-split language from active decision documents or mark it explicitly WITHDRAWN.

### Deliverable

`R4_PRIOR_ART_AND_THEOREM_STATUS.md`

Include before/after manuscript excerpts and a bibliography audit showing every new reference exists and is used.

---

# R4-B — rigorous headline safety status

The PWC result is the new paper headline, so its safety status cannot rely on ambiguous “certified modulo an estimated solver error” language.

## Preferred closure

Produce a **genuine validated enclosure** for at least these 8 trajectories at `α=0.85, A=0.25, T=12, U=0.100`:

- `pwc6_found` under ODE, Caputo, DDE, latent3;
- `multiscale` under ODE, Caputo, DDE, latent3.

The enclosure must rigorously bound:

1. solver/discretization error;
2. inter-node behavior;
3. the vector-field/source term over the enclosure/tube.

Use interval/Taylor-model/validated Volterra integration or another method that produces an actual mathematical enclosure. A finer mesh alone is not enough.

## Fallback closure

If a true enclosure cannot be completed in this round:

- replace **all** unqualified `certified` / `validated integration certifies` language by
  `a posteriori verified`, `refinement-verified`, or equally precise wording;
- include the solver-error limitation next to the headline result;
- never use `certified margin` for `+0.092`.

### Deliverable

`R4_HEADLINE_SAFETY_CERTIFICATE.md`

Binary verdict:

- `RIGOROUS_CERTIFICATE = PASS`, or
- `RIGOROUS_CERTIFICATE = FAIL → MANUSCRIPT_DOWNGRADED`.

No YELLOW wording in the final manuscript.

---

# R4-C — rebuild the analytical section from the surviving mathematics

`paper/sections/sec3.tex` is stale. Replace it with a coherent final theory chain.

Required order:

1. **Structural exact separation** — foundation; no priority claim for branch-point/high-frequency ideas.
2. **Supporting positive-SOE approximation lemma** — attributed to prior work; endpoint `L¹` variant stated precisely.
3. **Response-level approximation / induced operator semantics** — use the notation settled in R3-B.
4. **Exact Gaussian two-point testing obstruction** — no unspecified `Ψ`, no Pinsker as the theorem, no invalid `L²` kernel pairing.
5. **Finite-state prey-response approximation** — extend displayed response-level results to `m=64,128` with exact status labels.
6. **Complexity corollary** — sufficiently rich latent rivals approach chance under the declared finite-horizon/noise/input setting.

### Hard semantic constraints

- Never identify bare-kernel error with prey-response error.
- Never read `Ê_m^state` as a design objective.
- Define the test/minimax reduction unambiguously.
- If a number is high-accuracy numerical rather than interval-certified, label it so.
- Exact Gaussian bound is the primary bound; Pinsker may appear only for historical comparability.

### Deliverable

`R4_THEORY_SECTION_AUDIT.md`

---

# R4-D — rewrite title, abstract, introduction, contributions and conclusion

## Working title selected by Chief

> **Safe discrimination of fractional, delayed, and latent memory beyond classical waveforms in a strong-Allee predator–prey model**

Use this unless the final mock editor gives a specific evidence-based reason to shorten it.

## Abstract

CNSNS live Guide: **≤250 words**.

The abstract must contain:

1. problem in one sentence;
2. main falsification/positive design result;
3. scope: six classical families vs searched PWC class;
4. large-`m` latent-complexity obstruction as a separate result;
5. exact safety wording from R4-B;
6. no more than 3–5 numerical values/groups.

Delete:

- `inherited from a previously submitted companion paper`;
- `our previous paper`;
- universal “waveform governs” language;
- categorical “safety is not binding” language;
- headline novelty for SOE/root-exponential construction.

## Introduction

1. Delete the companion-comparison table.
2. Keep one neutral provenance paragraph only.
3. Replace the old four-contribution list.
4. Front-load the Round-03 falsification and the true novelty.
5. State closest prior art, including McLean, before claiming the endpoint lemma.

## Final contribution hierarchy

### Headline
1. constrained search finds safe PWC waveforms outperforming every classical baseline under the same amplitude budget;
2. the six-family safety–informativeness frontier is falsified as a system-level conclusion;
3. direct response-level latent complexity to `m=128` gives a separate finite-horizon indistinguishability obstruction.

### Supporting
4. a posteriori / rigorous trajectory safety status according to R4-B;
5. cross-host reproducibility;
6. endpoint-inclusive positive-SOE lemma, explicitly attributed.

### Deliverable

`R4_NARRATIVE_FINAL.md`

Include final title, abstract word count, contribution list, and deleted-claim checklist.

---

# R4-E — visual evidence for the new headline

The main finding must have a main figure.

1. Redraw the old safety–informativeness figure so it contains:
   - six historical families;
   - top searched safe PWC designs;
   - safe/unsafe status under **all four** hypotheses;
   - margin vs macro-accuracy.
2. Add a second panel only if it materially helps:
   - class recall comparison `multiscale` vs `pwc6_found` (Caputo/DDE gain is the key story), or
   - amplitude/crossing diagnostic showing why amplitude-only tuning fails.
3. Figure caption must state search scope and non-optimality: **existence result, not certified global optimum**.
4. Remove/relegate redundant figures so the paper stays concise.
5. Export publication-grade vector PDF/EPS where possible; raster outputs must meet live CNSNS artwork requirements.

### Deliverable

`R4_FIGURE_AUDIT.md`

and updated figure files under `paper/figures/`.

---

# R4-F — live CNSNS compliance matrix (99% rule)

Rebuild `CNSNS_COMPLIANCE_MATRIX_DRAFT.md` from the **live official Guide for Authors**, not memory.

For every item record:

| Requirement | Official wording/source | Mandatory? | Applicable? | Evidence/file | Status |
|---|---|---:|---:|---|---|

Current live guide items that must be checked include at least:

- editable `.tex` source;
- concise/informative title;
- title page details and full affiliation/contact data;
- abstract ≤250 words;
- 1–7 keywords;
- **mandatory highlights**: 3–5 bullets, each ≤85 characters, separate editable file;
- figures supplied as separate files and required resolution;
- numbered sections;
- acknowledgements immediately before references;
- funding disclosure;
- CRediT statement where applicable;
- declaration of competing interests;
- declaration of generative-AI use according to the current Elsevier wording/policy;
- data statement / research-data requirements;
- numbered square-bracket citations and complete reference metadata;
- submission checklist including corresponding-author full contact details.

### Important correction

Do **not** mark `elsarticle` as mandatory unless the live CNSNS/Elsevier instructions explicitly require it. `.tex` editable source is required; a specific class may be preferred/template-based rather than mandatory.

### Gate

- 100% mandatory PASS;
- ≥99% applicable total PASS.

### Deliverable

`CNSNS_COMPLIANCE_MATRIX_FINAL.md`

---

# R4-G — manuscript migration and end matter

Once R4-A–F stabilize content:

1. Remove AIMS-only front matter/style assumptions.
2. Use the current Elsevier/CNSNS-compatible LaTeX workflow/template.
3. Add/update:
   - full postal affiliation and corresponding-author details;
   - Highlights file;
   - Acknowledgements;
   - Funding;
   - CRediT/author-contribution statement as applicable;
   - Data availability/data statement;
   - Declaration of competing interest;
   - Generative-AI declaration using current required wording/location.
4. Ensure every bibliography entry is cited and every citation resolves.
5. Prune unused references.
6. Add DOI to McLean and every reference where available.
7. Build from a clean directory.

### Deliverable

`R4_FORMAT_AND_ENDMATTER_AUDIT.md`

---

# R4-H — reproducibility freeze

Create a submission-tagged reproducibility manifest:

- exact git commit;
- code paths for the 163,840-candidate search;
- exact top PWC levels;
- Stage-2 BIC validation paths/seeds;
- v3/v4 reproduction artifacts;
- response-level `m=64,128` artifacts;
- safety verification/certificate artifacts;
- software/environment versions;
- one clean command or documented sequence reproducing every headline table/figure.

No new run may silently overwrite frozen Round-03 outputs.

### Deliverable

`R4_REPRODUCIBILITY_FREEZE.md`

---

# R4-I — mock editor gate

Give a mock editor only:

- title;
- abstract;
- first 1.5 pages;
- main figure;
- conclusions.

Ask:

1. What is new?
2. What was falsified relative to the previous version?
3. What is theorem vs empirical vs certified/verified?
4. Why CNSNS?
5. Is any headline contradicted by the limitations?
6. Does the paper look like another fractional predator–prey simulation paper?

**PASS condition:** all six answers are correct without explanation from the authors.

### Deliverable

`R4_MOCK_EDITOR.md`

---

# R4-J — adversarial referee gate

Run two independent reviews:

### Mathematical referee
Attack:

- SOE novelty/prior art;
- quantifier order in the endpoint lemma;
- response-operator semantics;
- Gaussian/minimax reduction;
- large-`m` response certification/status;
- any surviving universal language.

### Computational/nonlinear referee
Attack:

- search leakage/overfitting;
- same-seed reuse;
- safety criterion across unknown candidate mechanisms;
- global-optimum language;
- solver/certificate status;
- BIC fairness;
- class imbalance;
- reproducibility across hosts;
- amplitude comparisons.

Every objection must be classified:

`FATAL / MUST_FIX / MINOR / REJECTED_WITH_REASON`.

### Deliverable

`R4_MOCK_REFEREES.md`

---

# R4-K — final decision

Create `ROUND_04_DECISION.md` with binary gates:

| Gate | PASS condition |
|---|---|
| R4.1 Prior art | McLean cited; T9b demoted everywhere |
| R4.2 Headline safety | rigorous certificate OR manuscript consistently downgraded |
| R4.3 Theory | kernel/response/test semantics consistent |
| R4.4 Narrative | ≤250-word abstract; no falsified claims |
| R4.5 Visuals | new headline figure present and scoped |
| R4.6 Reproducibility | frozen artifacts + manifest PASS |
| R4.7 Compliance | 100% mandatory, ≥99% applicable |
| R4.8 Mock editor | PASS |
| R4.9 Mock referees | no unresolved FATAL/MUST_FIX |
| R4.10 Build | clean compile; zero undefined refs/citations |

**Submission is authorized only if R4.1–R4.10 are GREEN.**

---

# Required Round-04 outputs

1. `R4_PRIOR_ART_AND_THEOREM_STATUS.md`
2. `R4_HEADLINE_SAFETY_CERTIFICATE.md`
3. `R4_THEORY_SECTION_AUDIT.md`
4. `R4_NARRATIVE_FINAL.md`
5. `R4_FIGURE_AUDIT.md`
6. `CNSNS_COMPLIANCE_MATRIX_FINAL.md`
7. `R4_FORMAT_AND_ENDMATTER_AUDIT.md`
8. `R4_REPRODUCIBILITY_FREEZE.md`
9. `R4_MOCK_EDITOR.md`
10. `R4_MOCK_REFEREES.md`
11. `ROUND_04_DECISION.md`
12. modified `paper/` and all final submission-side files

**No submission before Chief review of Round 04.**
