# Final Chief Audit — 2026-08-14

## Decision

**Research/novelty program: CLOSED.**  
**Mathematical scope: PASS after the Round-6 chief corrections already integrated.**  
**Final closeout: PASS after the residual corrections in this audit.**

I would not open another mathematical or computational round. The remaining work is
venue-specific editorial conversion and submission metadata.

## What the researcher did well in the final closeout

1. Split the 80-page chief-audited manuscript into a 63-page main paper and a
   23-page supplementary document without adding a new mathematical claim.
2. Preserved the chief-corrected Round-6 scope:
   - T23 is prey-input -> prey-output, not a full-state theorem;
   - the broad mass-only Strong-Allee witness is not used in the headline chain;
   - the testing bound uses the physical pulse cap;
   - the Bayesian sequential layer remains specified but unexecuted.
3. Added a useful claim-to-evidence matrix and an explicit reproducibility guide.
4. Preserved the expensive Figure 11 exactly (SHA-256 unchanged from the audited
   Round-6 package).
5. Kept the main visual architecture strong: 17 figures remain in the main paper,
   with solver validation in the supplement.

## Residual defects found and corrected by the chief

### 1. Benchmark rival-calibration wording was inconsistent with the corrected model family

Section 10 still said that **all four rivals share the same ecological Jacobian
backbone**. This contradicted Sections 1 and 3 and the chief-corrected Figure 13.

Corrected statement:
- ODE and Caputo share the ecological Jacobian exactly;
- DDE and latent models are calibrated alternative response laws at the same
  operating point, with matched input/observation channels and physical units;
- their internal generators are not asserted to equal the ecological Jacobian.

The same stale wording was removed from the Conclusion and Figure 11 caption.

### 2. Benchmark safety language was still too strong

Several residual phrases called the benchmark excitation “safe”, called a diagnostic
face distance “certified”, or labeled Figure 10 “safe but weak / informative but
unsafe”. The benchmark does not enforce T17 invariance at the full +/-0.10 budget;
the archived strict-face checker correctly returns FAIL for the plotted diagnostic
rectangle.

Corrected terminology:
- “common amplitude cap” rather than “safe excitation”;
- “benchmark diagnostic rectangle” rather than certified safe rectangle;
- “minimum signed face distance” rather than certified-face distance;
- “lower-crossing / weak” and “higher-crossing / informative” in Figure 10.

Figure 10 was regenerated from the archived benchmark JSON only; no simulation was rerun.

### 3. Supplement build emitted duplicate-bibliography warnings

The supplement used `xr` to import `main.aux` while also maintaining its own
bibliography. That imported the main paper's `\bibcite` entries and caused duplicate
natbib definitions.

Corrected by suppressing imported `\bibcite` entries during `\externaldocument{main}`
while preserving theorem/equation labels. The supplement now compiles with its own
bibliography and no duplicate-citation warnings.

### 4. Final-package metadata had stale counts and missing-file references

README/Q1 packaging notes still described the earlier visual-pass package
(67 pages, 16 figures, sec1--sec15) and referenced markdown files no longer present.
They now describe the actual final package:
- 63-page main;
- 23-page supplement;
- sec1--sec13 in the main;
- 17 main-paper figures plus the solver-validation figure in the supplement.

The journal-positioning note was also corrected: a 63-page generic-format paper does
not “meet” a 35--45-page preference simply because a venue has no formal page limit.

## Independent checks performed

### Build
Using the shipped `.bbl` files:
- main: 63 pages;
- supplement: 23 pages;
- undefined citations: 0 / 0;
- undefined references: 0 / 0;
- final LaTeX/package warnings: 0 / 0.

### Mathematical/numerical artifacts
- Round-6 lightweight prey-response check: 8/8 focal cells PASS.
- Archived benchmark consistency validation: PASS.
- Kernel interval-enclosure checker: PASS and reproduces the published nested bounds.
- Strict rectangle diagnostic: FAIL, as expected; therefore the manuscript must not
  describe that benchmark rectangle as invariant/certified at the full amplitude budget.

## Final academic assessment

### Mathematical solidity
Strong within the declared scope. The paper now has a real mathematical spine:
structural separation, finite-horizon latent approximation, testing obstructions,
optimal-design results, strict safety results, and the prey-response pole/branch-cut
finite-state approximation with interval enclosures.

### Novelty
The novelty claim is now appropriately narrow. It does not claim novelty for generic
safe information limits, generic active model discrimination, or generic Prony/rational
approximation. The distinctive contribution is the joint construction:
Strong-Allee ecology + fractional/latent memory hierarchy + complexity-dependent
finite-horizon identifiability loss + protocol/safety interface + interval-certified
prey-response testing obstruction.

### Visual quality
Submission-grade. No further general visual campaign is warranted. Figure 11 should
remain frozen. Future figure changes should be venue-template/layout changes only.

### Main remaining risk
Length/focus, not mathematics. The 63-page generic-format main paper is defensible for
a venue that permits longer contributions, but the unexecuted Bayesian section is the
first candidate to move almost entirely to the supplement if a target editor requests
additional compression.

## Final gate

**GO to venue conversion and submission preparation.**

Do not:
- open another novelty round;
- launch another large benchmark;
- broaden T23 to full state;
- restore the hierarchy-wide Strong-Allee claim;
- relabel empirical low-crossing behavior as certified safety.

Do:
- choose the target journal;
- convert to its official template;
- add required keywords/highlights/MSC/CRediT/declarations as applicable;
- update the data/reproducibility record;
- rerun the build, claim/evidence, and secret-scan gates on the exact upload ZIP.
