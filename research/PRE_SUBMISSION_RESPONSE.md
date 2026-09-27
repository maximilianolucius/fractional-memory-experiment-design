# Pre-submission referee simulation — MDPI version (directives §26)

Three independent adversarial passes against `paper_mdpi/mathematics-fmed.tex`. Each objection
is answered in the manuscript or the scope proposition; nothing is deferred to rebuttal.

## Referee A — mathematical rigor

**A1. "Theorem 2 is a textbook two-point bound dressed as a theorem."** Answered in the text:
the identity is credited to the detection literature [Kay]; the stated content is the pairing
with a *certified* response-level error and the resulting input-uniformity. The theorem carries
its hypotheses (common covariance) and its equality case explicitly.

**A2. "The L² route would be easier."** Forbidden and said so: ‖k_α−k_m‖_{L²} = ∞ for α ≤ 1/2,
which would make the statement vacuous on part of the declared range. The bound is routed
through L¹ of the *response* kernel.

**A3. "Lemma 1's boundary rate."** The quantifier order is explicit, the constant's divergence
as c ↑ π√(α(1−α)) is stated, and attainment is listed as OPEN-1. No sharpness is claimed.

**A4. "Nonlocal dynamics treated as ODEs?"** The linear layer uses transfer operators only; the
nonlinear layer states its solution concept (mild/Volterra), cites local Picard theory, and
inherits positivity/continuation from the companion on the regimes used. No global-existence
circularity: nothing here proves or needs a new a priori bound.

**A5. "Equality/critical cases."** Floor equality case stated; separation theorem hypotheses
(CB ≠ 0, irrational α) stated with the CB = 0 failure known; Matignon-violating cells hatched
and excluded in the atlas; safety margins graded (verified vs enclosed) rather than binarized.

**A6. "Are the m surrogate poles all found?"** Yes, and proved: m pairwise-disjoint interval-
Newton boxes for a degree-m secular polynomial account for all roots, all simple; negative real
parts certified. The double-precision seeding failure at m = 32 is reported, not hidden.

## Referee B — novelty and literature

**B1. "Exponential sums are known."** The manuscript says so in the same subsection, names
McLean, Beylkin–Monzón, Jiang et al., Trefethen–Weideman, Stahl, and claims only the
endpoint-inclusive L¹(0,T) form with exact horizon scaling.

**B2. "Isn't this the companion paper again?"** The companion study (accepted, no DOI yet) is
**not cited**, per the directive forbidding unpublished references. The backbone is attributed to
the published strong-Allee/Holling-II literature (Wang–Shi–Wei 2011), its stability facts are
re-derived in-text from the exact invariants via Matignon's criterion, and the question posed —
distinguishability under safety — is disjoint from stability certification. Re-cite the companion
only once its DOI is assigned.

**B3. "The benchmark is one parameter point."** Stated: locked rationals are an instance, not
a calibration (Discussion), the search is existence-only at one amplitude and one α
(Proposition 1(ii)), and the held-out control quantifies transfer to A = 0.20. The floor's
atlas figure extends the certified statement across (α, A, m).

**B4. "The safety–informativeness refutation could be selection bias."** The held-out result is
in the manuscript: searched designs lose *less* out of sample (0.060) than never-optimized
classical families (0.087) and lead 0.907 vs 0.837.

## Referee C — computation and reproducibility

**C1. "Certified vs floating."** Table 1 prints both, with slack ≤ 1.1%; all certified numbers
are Arb endpoints at 256 bits; the near-zero segment and tails are closed-form/geometric.

**C2. "Solver adequacy."** Self-test against exact Mittag-Leffler with the refinement trend
shown; common-grid BIC comparison cancels shared discretization bias; cross-host reproduction
to 4 decimals under different library versions.

**C3. "Can figures be regenerated?"** Every figure/table maps to a script and a frozen artifact
in the public deposit (DOI 10.5281/zenodo.22087770), cited in Data Availability. NOTE: the
deposit predates `r6_response_interval_cert.py`; a new deposit version must be published before
submission so the citation covers the certified table. **This is the one open pre-submission
action.**

**C4. "Pooled latent class."** Documented in Proposition 1(v), the confusion-figure caption,
and the benchmark text; raw files keep per-generator labels so the pooling is reversible.

**B5. "The whole paper is one rational benchmark."** Now answered twice: the held-out control
within the benchmark, and Section 7's empirically anchored vole--weasel cell, where the exact
invariants (16/53, 25/636), the certified floor, the safety-inversion experiment, and the
transferred design all re-run at a literature-anchored operating point. Scenario elements
(net r, Allee threshold, memory mechanisms) are declared in-text and in Proposition 1(vi).

**C5. "Case-study seeds."** Deterministic: base seed + crc32 of the (design, law, SNR, channel)
tuple; the earlier python-hash seeding was caught and replaced before the production run.

## Directive-compliance checks (§28, §30)

- pages: 20 ≤ 25 ✔ (buffer 5 pp)
- unpublished references (arXiv / preprint / in press / submitted / personal comm.): **0** in the
  bibliography — two arXiv items replaced by Sui et al. (ICML 2015, PMLR 37) and Harirchi & Ozay
  (Automatica 2018, DOI 10.1016/j.automatica.2018.03.040); the accepted-but-DOI-less companion
  removed and replaced by Wang–Shi–Wei (J. Math. Biol. 2011, DOI 10.1007/s00285-010-0332-1);
  all metadata verified against publisher/PMLR pages ✔
- AI/LLM/drafting references in manuscript: `grep -ci "artificial intelligence\|language model\|AI-assisted\|GPT\|LLM"` = 0 ✔
- supplementary material: none; all load-bearing content in main text ✔
- figures: 12 environments / 19 panels, all vector, all discussed, captions state
  analytic vs certified vs corroboration ✔
- title foregrounds strongest theorem ✔; abstract states the general result before the
  benchmark numbers ✔; abstract/conclusion sentences all trace to CLAIMS.md ✔
- exact arithmetic for algebraic claims (rational J, exact r₁,₂) ✔; intervals only for
  transcendental enclosures ✔
- placeholders: editor/dates blank pending submission (MDPI fills); no draft-only language ✔
