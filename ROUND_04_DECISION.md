# ROUND 04 — Researcher decision memo

**Branch:** `rescue/aims-desk-rejection`. All 11 tasks executed.

## VERDICT: **SUBMISSION NOT AUTHORISED.** 8 of 10 gates GREEN, 1 RED, 1 AMBER.

The two blockers are **clerical, not scientific**: a template/journal-branding conversion and four
missing end-matter metadata items, two of which require information I do not have and must not
invent. Every scientific gate is GREEN.

---

## 1. Gate table

| Gate | PASS condition | Status | Evidence |
|---|---|:--:|---|
| **R4.1** Prior art | McLean cited; T9b demoted everywhere | **GREEN** | `thm:T9b` deleted; `lem:soe` + `cor:closure` in its place with a dedicated attribution block; 11 cross-references retargeted; `K07`/`K08`/`K09` added with DOIs; 0 occurrences of every forbidden phrasing. `R4_PRIOR_ART_AND_THEOREM_STATUS.md` |
| **R4.2** Headline safety | rigorous certificate **OR** manuscript consistently downgraded | **GREEN** (via the fallback) | `RIGOROUS_CERTIFICATE = FAIL` → downgrade applied globally: "verified a posteriori", "verified margins", `+0.092` never called certified. 4 of 8 trajectories *do* carry a genuine enclosure and only those are called rigorous. `R4_HEADLINE_SAFETY_CERTIFICATE.md` |
| **R4.3** Theory | kernel/response/test semantics consistent | **GREEN** | `sec3.tex` rebuilt in the required order; (O1)/(O2)/(O3) defined and never conflated; exact `Φ(−d/2)` primary, Pinsker comparability-only; `Ψ` gone; no `L²` kernel pairing; every number status-labelled. `R4_THEORY_SECTION_AUDIT.md` |
| **R4.4** Narrative | ≤250-word abstract; no falsified claims | **GREEN** | abstract **243 words**; chief's title applied; contribution list rebuilt; companion-comparison table deleted; single neutral provenance paragraph; 11-item deleted-claim checklist all ✔. `R4_NARRATIVE_FINAL.md` |
| **R4.5** Visuals | new headline figure present and scoped | **GREEN** | `fig24_safe_design_frontier.pdf`, two panels, safe/unsafe under all four mechanisms, existence-not-optimality stated in the caption; Fig. 10 caption scoped to the classical families. `R4_FIGURE_AUDIT.md` |
| **R4.6** Reproducibility | frozen artifacts + manifest PASS | **GREEN** | 12 headline claims each mapped to script + artifact + md5; exact PWC levels and seed formula recorded; no Round-03 output overwritten. `R4_REPRODUCIBILITY_FREEZE.md` |
| **R4.7** Compliance | 100% mandatory, ≥99% applicable | **RED** | mandatory **8/12**. Open: data statement (wording chosen but no deposit), funding, corresponding-author postal/ORCID, keyword count unverified. `CNSNS_COMPLIANCE_MATRIX_FINAL.md` |
| **R4.8** Mock editor | PASS | **AMBER** | 5/6 answers correct from the material; Q3 (theorem vs empirical vs verified) failed and was fixed by adding an evidence-classification sentence. Remaining blocker: the running header still reads **"AIMS Mathematics"**. `R4_MOCK_EDITOR.md` |
| **R4.9** Mock referees | no unresolved FATAL/MUST_FIX | **GREEN** | 0 FATAL; all 3 MUST_FIX closed (overfitting closed by a new held-out test; scope closed by explicit statements; BIC-vs-obstruction closed by weakening the claim in four places); 4 MINOR open, none touching a reported number. `R4_MOCK_REFEREES.md` |
| **R4.10** Build | clean compile; zero undefined refs/citations | **GREEN** | clean-directory build: exit 0, 0 LaTeX errors, 0 undefined references, 0 multiply-defined labels, 0 bibtex warnings, 0 `??` in the PDF, 25 pages |

## 2. What has to happen before submission

Four items, none scientific, in order of who can do them:

1. **Template conversion (closes R4.8).** The manuscript is still in AIMS house style; page 1 carries
   an AIMS banner and every page header says "AIMS Mathematics". A CNSNS editor sees that
   immediately. Mechanical: swap the `\AIMS*` front-matter macros for `elsarticle`'s equivalents.
   I deferred it because content was under review and this project has lost time to LaTeX breakage
   before; say the word and it is done in one pass.
2. **Funding statement (R4.7).** Required either way. I did not insert the standard no-funding
   sentence because I cannot verify it, and asserting a funding status in a submitted record would be
   fabrication.
3. **Corresponding-author postal address and ORCID (R4.7).** Not in my possession.
4. **Keyword count (R4.7).** 6 supplied; the CNSNS maximum could not be read — ScienceDirect returns
   403 to automated fetching. Needs one look at the guide in a browser.

Plus one **disclosure decision that is yours, not mine** (`R4_FORMAT_AND_ENDMATTER_AUDIT.md` §2): the
data-availability statement currently says "available from the author on request". A concrete deposit
is stronger, but the existing public repository contains the entire rescue record — the recovery plan,
your reviews, and the audits where we falsify our own earlier claims. Pointing a referee at that is a
real decision. My recommendation is a curated deposit with `benchmark/`, `rescue_compute/`, the frozen
artifacts and a README, and nothing else.

## 3. What Round 04 actually changed in the science

- **The SOE result is gone as a contribution.** Demoted to a lemma, technique attributed to McLean
  (2018) in the same subsection, removed from every contribution list, FCAA split marked WITHDRAWN.
  This was the blocking item from Round 03 and it is closed.
- **The safety claim is now the one the evidence supports.** Attempting a genuine enclosure was worth
  it: 4 of 8 headline trajectories carry one, with rigorous lower bounds 0.441 and 0.309 against the
  threshold 0.25. The other 4 do not, for reasons now diagnosed exactly (delay-propagated input
  discontinuities; PECE order). So the manuscript says "verified", reserves "rigorous" for the four,
  and states the failure causes.
- **The overfitting objection is answered with data, not rhetoric.** The searched designs lose 0.060
  macro-accuracy on the held-out threshold; the classical families lose 0.087. The advantage over the
  safe classical design is *larger* out of sample. This is now in the paper.
- **One of my own over-claims is retracted.** The benchmark's low latent recall was being offered as
  support for the latent-complexity obstruction. BIC penalises the higher-dimensional model, the two
  explanations are not separated, and four passages now say so. The obstruction rests on the
  analytical result alone, where it is secure.
- **A near-miss worth recording.** While weakening that claim I wrote a sentence asserting no design
  exceeds 0.55 recall against the latent rival. Checking against cell-level data gave 0.945: the
  benchmark's `latent3` column is the *pooled* latent class (`latent1`+`latent3`). The sentence was
  removed. **Flagging it because the manuscript does not currently say that the label is pooled** —
  that is a real documentation gap in the frozen benchmark's presentation, inherited from before this
  round.

## 4. Open items I am not closing unilaterally

| item | why |
|---|---|
| Penalty-free decision rule (referee 2.5, proper fix) | changes the benchmark's decision layer; the frozen v3 comparison is a headline and I will not perturb it without your call |
| Deleting Fig. 10 in favour of Fig. 24 | Fig. 24 strictly contains it; deleting renumbers everything after it |
| `latent3` = pooled latent class, undocumented | pre-existing in the frozen benchmark; fixing the label touches v3 presentation |
| Rigorous enclosure for DDE and Caputo | mechanical for DDE (split the history at every `jump + kτ`), a distinct piece of work for Caputo (higher-order reference than PECE) |
| Full DOI sweep of the other 73 bib entries | minor compliance, ~1 hour |

## 5. Honest assessment

The paper is in better shape than at any earlier round, and the two things that were wrong at the end
of Round 03 — an uncited 2018 paper carrying our headline lemma, and a safety claim stronger than the
evidence — are both fixed. The adversarial passes found one substantive over-claim of mine and I
removed it rather than defending it.

What is left is paperwork and two facts about the author that I do not have. I am not marking R4.7
green by filling those in with plausible guesses, so the verdict is NOT AUTHORISED until you or the
author closes them.
