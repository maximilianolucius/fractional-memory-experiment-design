# Desk rejection recovery plan

**Manuscript:** *Safe active discrimination of fractional, delayed, and finite latent memory in a strong-Allee predator–prey model*  
**Date:** 2026-08-24  
**Branch:** `rescue/aims-desk-rejection`

## Objective

Convert the desk-rejected manuscript into a **theorem-first, self-contained, demonstrably novel, reproducible, and submission-compliant paper** that directly addresses the editorial screening dimensions of **discipline/scope, novelty, and general significance**.

> **Submission rule:** do not submit until **100% of mandatory requirements** and **>=99% of the total applicable checklist** of the *current* target-journal instructions are satisfied. Re-download and re-audit the official instructions and official TeX template within 24 hours of submission.

---

## 1. Recovery diagnosis

The rejection was editorial, before external peer review. No mathematical error was identified. The main risk is therefore not basic correctness but **editorial perception of novelty and general significance**.

The current version can be read as an ecological/computational discrimination study supported by theory. The rescue must reverse that hierarchy:

\[
\text{general theorem}
\to
\text{finite-horizon impossibility}
\to
\text{safety-constrained information limit}
\to
\text{strong-Allee certified application}.
\]

The main manuscript should no longer make the reader work to discover the mathematical contribution.

---

## 2. North-star scientific claim

The revised paper should be understandable from title + abstract + first 1.5 pages as follows:

> Fractional, delayed, and finite-latent memory mechanisms can be structurally distinct while becoming statistically indistinguishable on finite horizons under bounded excitation; imposing a state-safety constraint can further restrict discriminating power. The paper establishes this phenomenon in a general hereditary-system framework and then certifies it in a strong-Allee predator–prey model.

The ecological system remains important, but it must not be the sole source of general significance.

---

## 3. Workstream A — mathematical novelty upgrade

### A1. Build `NOVELTY_MATRIX.md`

Perform an adversarial, current literature audit covering at least:

- fractional system identification;
- fractional vs delay model discrimination;
- diffusive / exponential-sum approximation of fractional kernels;
- rational approximation of fractional transfer functions;
- finite-horizon identifiability;
- minimax hypothesis testing for dynamical systems;
- active model discrimination;
- safe experiment design / safe identification;
- safety-constrained information acquisition;
- predator–prey fractional-delay systems.

For each closest paper record:

| Field | Required content |
|---|---|
| Citation | Exact reference |
| Model class | fractional / delay / latent / nonlinear |
| Structural identifiability | yes/no |
| Finite-horizon approximation | yes/no |
| Explicit complexity budget `m` | yes/no |
| Statistical lower bound | yes/no |
| Uniform over bounded inputs | yes/no |
| State-safety constraint | yes/no |
| Rigorous certificate | yes/no |
| What they prove | exact result |
| What we add | verifiable difference |

**Gate A1:** no novelty claim survives if essentially present in prior work. The Introduction must cite the closest competitor, not merely convenient background references.

### A2. Upgrade the four current analytical results

The central theory section should become something like:

**Finite-horizon discrimination limits for hereditary mechanisms**

#### Theorem A — exact structural non-equivalence

Formulate independently of the predator–prey model for a defined class of hereditary input/output systems.

Must state precisely:

- fractional class;
- rational / finite-state latent class;
- admissible retarded-delay class;
- common analytic domain;
- observation and input operators;
- condition such as `CB != 0`;
- meaning of exact equality/non-equivalence;
- excluded degeneracies.

Adversarially test `CB=0`, cancellations, non-collocated channels, partial observation, improper transfer functions, and multiple delays.

#### Theorem B — quantitative finite-horizon approximation

Upgrade existence of exponential-sum approximation of the Caputo kernel to an explicit complexity relation if possible:

\[
m \ge m(\varepsilon,T,\alpha,\ldots)
\quad\Longrightarrow\quad
\|k_\alpha-k_m\|_{L^1(0,T)}\le \varepsilon.
\]

Priority: obtain a usable rate or explicit upper/lower bounds in `m`.

#### Theorem C — uniform finite-experiment testing obstruction

Combine approximation error, bounded input budget, observation operator and noise into a general lower bound on discrimination:

\[
E_m\to0
\quad\Longrightarrow\quad
\inf_{\text{tests}} P_e(m,u)\to\frac12,
\]

uniformly over the precisely stated admissible input class.

Re-audit all constants and factors involving:

- sampling;
- noise covariance;
- number of observations;
- observation operator;
- `L1/L2` convolution inequalities;
- KL / total variation / Pinsker;
- priors.

#### Theorem D — safety-constrained information ceiling

Attempt to prove the strongest new result in the rescue:

1. a state-safety requirement such as `x(t) >= A + delta` restricts admissible excitation;
2. this yields an upper bound on observable model separation/information;
3. combined with Theorem C, sufficiently rich latent rivals cannot be uniformly discriminated from fractional memory on a finite horizon under safe excitation.

If this cannot be proved at theorem level, downgrade it explicitly to a certified/numerical phenomenon; do not overclaim.

### A3. Strong-Allee system becomes specialization/corollary

The ecological model should serve as:

- a nontrivial application;
- a system where safety has genuine dynamical meaning;
- a certified test case;
- a numerical realization of the general bounds.

### A4. Main proofs belong in the main paper

Do not hide the intellectually nonstandard parts of headline proofs in Supplementary Material. Supplement only repetitive derivations, large tables, solver details, secondary lemmas, and exhaustive grids.

---

## 4. Workstream B — editorial narrative reconstruction

### B1. Title

Use sentence case and front-load the general mathematical result. Candidate directions:

- *Finite-horizon limits of discriminating fractional, delayed and latent memory under safety constraints*
- *When fractional memory is structurally identifiable but experimentally indistinguishable*
- *Safe discrimination of hereditary mechanisms under bounded experiments: Fractional, delayed and latent memory*

### B2. Abstract

Target 180–240 words, and in all cases below the current journal limit.

Structure:

1. general problem;
2. theorem-level novelty;
3. safety consequence;
4. strong-Allee certified application;
5. broad significance.

Remove from the abstract:

- “inherited”;
- “not claimed as new”;
- companion-paper narrative;
- large grid inventories;
- long lists of numerical metrics.

### B3. First 1.5 pages

The Introduction must immediately answer:

1. What is the mathematical problem?
2. What was previously unknown?
3. What exactly is proved here?
4. Why is it significant beyond predator–prey ecology?
5. Why is the strong-Allee model a meaningful hard specialization?

Remove the current companion-paper comparison table from the Introduction. Replace it with one concise, factual provenance paragraph.

### B4. Contributions must be claims, not activities

Prefer:

- “We prove…”
- “We derive…”
- “We certify…”
- “We show that no admissible experiment can…”
- “We obtain an explicit complexity-dependent bound…”

Avoid presenting simulation or benchmarking activity itself as the main novelty.

---

## 5. Workstream C — provenance, overlap, and self-containment

### C1. Correct authorship/provenance wording

The current manuscript has Ibrahim Alraddadi as author while `P01` is bibliographically attributed to Maximiliano Lucius. Do not use “our previous paper” unless authorship/provenance genuinely supports that wording.

Use factual language such as:

> The ecological backbone follows the companion study [X] …

and state exactly what is reused.

### C2. Make the paper self-contained

No proof, assumption, equilibrium, Jacobian, parameter definition, or stability fact required by the present theorems may depend on an inaccessible/unpublished companion manuscript.

### C3. Create `OVERLAP_PROVENANCE_AUDIT.md`

Audit:

- shared equations;
- shared parameters;
- shared figures;
- shared text;
- justification;
- citation/disclosure location.

The objective is legitimate, fully disclosed reuse—not a mechanically minimized similarity percentage.

---

## 6. Workstream D — numerical evidence and reproducibility

### D1. Reduce visual density in the main paper

The rejected paper is visually simulation-heavy. Keep only figures and tables that establish a central claim. Move secondary grids, waveform galleries, repeated sweeps, and solver diagnostics to Supplementary Material.

### D2. Clean-run reproducibility

Create a reproducibility workflow that from a clean checkout:

1. recreates numerical results;
2. recreates figures/tables;
3. compiles main + supplement;
4. checks hashes/tolerances;
5. records environment/dependencies.

Required artifacts:

- `REPRODUCIBILITY.md`;
- locked environment / requirements;
- `run_all.py` or equivalent;
- seed policy;
- numerical tolerance policy;
- sanity tests.

### D3. Statistical audit

Audit BIC, likelihood normalization, effective observations, class priors, parameter fitting fairness, complexity penalties, Monte Carlo uncertainty, SNR, horizon, sampling cadence, and latent budget `m`.

### D4. Safety audit

Separate rigorously:

- analytical/certified safety;
- sufficient conditions;
- numerical non-crossing diagnostics;
- empirical crossing rates.

Do not label simulation-only evidence as a proof of safety.

---

## 7. Workstream E — >=99% current journal compliance

### Rule

At final submission, use the **current official instructions and current official TeX template as source of truth**. Do not rely on memory, cached notes, or a homemade style that merely imitates the published appearance.

For AIMS Mathematics, the current source set must be rechecked immediately before submission:

- AIMS Mathematics journal portal;
- official Submission Guidelines;
- official JAMS submission system;
- official `Tex Template` linked from the current instructions.

If the target journal changes, rebuild the compliance matrix against the new journal from scratch.

### E1. Create `JOURNAL_COMPLIANCE_MATRIX.md`

Columns:

| Requirement | Official source | Mandatory? | Applicable? | Current status | Evidence/file | Fix | Final PASS |
|---|---|---:|---:|---|---|---|---|

Operational definition:

- **mandatory requirements: 100% PASS**;
- **total applicable checklist: >=99% PASS**.

No known mandatory deviation is acceptable.

### E2. Current AIMS items to audit explicitly

- official submission template, not `aims_math_style.sty` as a substitute;
- cover letter;
- full text with figures/tables;
- line numbers for review when required/recommended by current template/instructions;
- title in sentence case;
- full affiliations;
- corresponding-author metadata, including exact address, email and telephone when required;
- heading hierarchy and sentence case;
- abstract below current word limit;
- 5–10 keywords;
- body typography/spacing per current template;
- Introduction / methods-equivalent / results / discussion / conclusions as appropriate;
- author contributions;
- exact current heading **Use of Generative-AI tools declaration**;
- acknowledgments/funding disclosures as applicable;
- conflict of interest;
- data/code availability statement if required or appropriate;
- references numbered in **order of first citation**, not alphabetically;
- journal abbreviations / DOI / author-list formatting per current style;
- current policy for preprints and unpublished material;
- figures embedded and supplied separately in accepted formats/resolution/color mode;
- captions and table titles in required positions;
- permissions for reused material;
- supplementary material cross-referenced correctly.

### E3. 24-hour refresh gate

Within 24 hours before submission:

1. reopen official instructions;
2. download the template again;
3. compare version/date/hash if possible;
4. rerun the entire compliance matrix;
5. inspect actual JAMS fields;
6. check for newly required statements;
7. rebuild PDF from a clean folder.

**No submission unless this gate is GREEN.**

---

## 8. Workstream F — bibliography and positioning

The current use of `\bibliographystyle{plain}` must be removed if incompatible with the official target-journal template.

Actions:

1. migrate to official bibliography mechanism;
2. order citations by first appearance if required;
3. DOI audit;
4. ISO-4 abbreviation audit where applicable;
5. claim-to-citation audit;
6. update 2024–2026 literature;
7. replace preprints with published versions when available;
8. include closest competing work even when it narrows our novelty claim;
9. audit `P01`, `SAFE26A`, `SAFE26B` and any unpublished references.

**Gate F:** a specialist referee should not be able to say that the paper omits the closest literature.

---

## 9. Workstream G — cover letter against the desk rejection

The new cover letter should contain:

1. one paragraph: general problem + central result;
2. at most three bullets: theorem-level novelty;
3. one paragraph: why the result matters to the journal readership beyond the ecological case;
4. one paragraph: exact companion-paper boundary/provenance;
5. all mandatory submission declarations;
6. reviewers only if useful and conflict-free.

Do not frame the revision as “more simulations” or “more pages”. The message is that the scientific hierarchy and theorem-level contribution have changed.

---

## 10. Workstream H — adversarial pre-review

### H1. 90-second mock editor

Provide only title, abstract, first 1.5 pages and conclusion. The reviewer must correctly identify:

- novelty in one sentence;
- central theorem;
- general significance;
- journal fit;
- difference from closest literature.

If not, FAIL.

### H2. Mathematical mock referee

Attack assumptions, analytic domains, branch cuts, asymptotics, approximation near `t=0`, complexity rate in `m`, uniformity, noise model, observation operator, Pinsker/KL constants, safety theorem, interval arithmetic, and certificate reproducibility.

### H3. Applied/computational mock referee

Attack ecological interpretation, perturbation realism, parameter sensitivity, BIC fairness, SNR, sampling, crossing behavior, solver accuracy, fractional-delay implementation, and latent-model calibration.

---

## 11. Recommended manuscript architecture

1. Introduction
2. General hereditary discrimination framework
3. Structural separation and finite-horizon approximation
4. Statistical limits under bounded and safe excitation
5. Strong-Allee specialization
6. Numerical methods and validation
7. Fractional-delay and active-design results
8. Model-discrimination benchmark
9. Discussion
10. Conclusions
11. Author contributions
12. Use of Generative-AI tools declaration
13. Acknowledgments / Funding
14. Data availability
15. Conflict of interest
16. References
17. Supplementary material

---

## 12. Do not do these things

- Do not resubmit essentially the same paper with a new template.
- Do not respond to the desk rejection merely by adding 6–8 pages.
- Do not increase figure count as a proxy for significance.
- Do not overload the abstract with provenance disclaimers.
- Do not claim generality without a general theorem.
- Do not hide the central mathematics in Supplementary Material.
- Do not call numerical non-crossing a safety proof.
- Do not imitate a production PDF instead of using the official submission template.
- Do not submit with any known mandatory compliance failure.

---

## 13. Journal decision gate

### Scenario 1 — theorem-level upgrade succeeds

If the rescue establishes a general finite-horizon discrimination theorem, useful complexity dependence, and preferably a safety-constrained bound, the paper can target a stronger general/applied mathematics venue.

### Scenario 2 — theory remains application-specific

If the central result remains prey-channel-specific, mostly numerical/BIC-driven, and lacks a general safety/information theorem, target a specialized journal in nonlinear/fractional dynamics, system identification, or mathematical biology rather than overselling general mathematical significance.

The journal must be selected for the paper that actually exists after the rescue.

---

## 14. Final deliverables

Required before submission:

- `main.tex` on the current official template;
- `main.pdf`;
- `supplement.tex`;
- `supplement.pdf`;
- cover letter;
- `NOVELTY_MATRIX.md`;
- `CLAIM_EVIDENCE_LEDGER.md`;
- `OVERLAP_PROVENANCE_AUDIT.md`;
- `JOURNAL_COMPLIANCE_MATRIX.md`;
- `REPRODUCIBILITY.md`;
- reproducible source code;
- separate figure files;
- bibliography audit;
- clean-build report;
- mock-editor report;
- mock-referee reports;
- final submission package.

---

## 15. Definition of done — GREEN gates

### G0 — Scope
Title/abstract/cover letter establish journal fit.

### G1 — Novelty
Every main contribution has a closest-prior-work comparison and a demonstrable difference.

### G2 — General significance
At least one central result exists beyond the strong-Allee specialization.

### G3 — Mathematical correctness
Headline theorems survive adversarial proof and counterexample audit.

### G4 — Self-containment
No critical mathematical dependency on an unavailable companion paper.

### G5 — Numerical credibility
Clean reproducibility plus solver/statistical/safety audits PASS.

### G6 — Editorial presentation
Title/abstract/Introduction communicate novelty before provenance and limitations.

### G7 — Journal compliance
- 100% mandatory requirements PASS;
- >=99% total applicable checklist PASS;
- instructions/template refreshed within 24 hours of submission.

### G8 — Submission package
Clean compilation, correct metadata, bibliography, figures, cover letter and upload package.

**Submit only when G0–G8 are GREEN.**

---

## 16. Immediate priority order

1. Freeze rejected version as baseline.
2. Build `NOVELTY_MATRIX.md`.
3. Audit and strengthen Theorems A–D.
4. Seek explicit `m`-versus-`epsilon` complexity.
5. Seek a safety-constrained information theorem.
6. Rewrite title + abstract + first 1.5 pages only after theorems stabilize.
7. Remove companion-comparison table from Introduction.
8. Resolve provenance and self-containment.
9. Rebalance main paper vs supplement.
10. Re-audit numerics/reproducibility.
11. Select final journal.
12. Download current official journal instructions/template.
13. Migrate manuscript source to official template.
14. Build `JOURNAL_COMPLIANCE_MATRIX.md`.
15. Run mock editor + mathematical referee + applied referee.
16. Clean build.
17. Refresh compliance within 24 hours.
18. Submit.
