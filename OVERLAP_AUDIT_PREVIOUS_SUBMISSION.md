# Overlap Audit Against the Previously Submitted Paper

## Papers compared

**Current manuscript**
`Safe Active Discrimination of Fractional, Delayed, and Finite Latent Memory in a Strong-Allee Predator--Prey Model`

**Previously submitted paper**
`Computer-Assisted Stability and Extinction Certificates for a Caputo Predator--Prey System with a Strong Prey Allee Effect`

## Executive verdict

**No problematic overlap was found in the research question, headline contributions, numerical campaign, or principal figures.** The two papers intentionally share the same strong-Allee ecological backbone and locked parameterization. That inheritance is scientifically legitimate because the current manuscript uses the previous system as a fixed test bed for a different question: active discrimination of memory mechanisms.

The shared backbone must nevertheless be disclosed explicitly. Before this audit the relationship was cited, but several equilibrium/stability formulas were restated without sufficiently local attribution, especially in the Supplement. This package has been edited so that the inheritance is explicit wherever those facts enter and the earlier stability/certification results are not presented as contributions of the new paper.

**Risk after the edits: LOW**, provided the previous paper is disclosed in the journal submission/cover letter as related work.

---

## 1. What is intentionally shared

The following objects are reused from the previous paper and are now explicitly identified as inherited:

- the nonlinear strong-Allee/Holling-II predator--prey vector field;
- the locked ecological parameters
  `r=3/2, K=1, a=1, h=1/2, e=4/5, m=2/5`;
- the coexistence equilibrium `x*=2/3`, `y*(A)=2(2-3A)/(9A)`;
- the coexistence Jacobian `J(A)`;
- the Matignon stability boundary used to screen admissible/stable operating cells;
- the ecological interpretation of the strong-Allee threshold.

These are **background inputs** to the current study, not new claims.

---

## 2. What belongs only to the previous submitted paper

The previous manuscript is centered on **computer-assisted certification of the dynamics of the Caputo ecological model**. Its distinctive contributions include:

- interval Newton/Krawczyk certification of equilibria;
- certified Matignon stability classifications and the `alpha*(A)` stability atlas;
- machine-checkable certificate files and acceptance-gate architecture;
- boundary-equilibrium classification;
- extinction-funnel and global ultimate-boundedness certificates;
- analysis of the forward-Euler surrogate and the stability-verdict inversion;
- negative/obstructed claims for flip, Neimark--Sacker, period-2, chaos, and control.

**None of these is re-presented as a headline contribution of the current manuscript.** The current paper does not reproduce the previous certificate inventory, Krawczyk proof, Euler-surrogate counter-example, extinction-funnel proof, or certified Matignon parameter-grid figure.

---

## 3. What belongs only to the current manuscript

The present manuscript addresses a different research question: **which safe perturbations and observations can discriminate competing memory mechanisms?** Its distinctive contributions are:

- controlled comparison of ODE, Caputo, retarded-delay, and bounded finite-latent mechanisms;
- structural transfer-function separation of fractional memory from the declared rival classes;
- finite-horizon exponential/latent approximation and the associated complexity barrier;
- minimax/testing lower bounds for memory discrimination;
- interval-enclosed finite-state approximation of the ecological prey response;
- optimal/robust input and observation design machinery;
- six-family perturbation comparison;
- a four-class BIC model-discrimination benchmark;
- a dedicated **combined fractional-delay model** and its numerical validation;
- new `(alpha,tau)` simulations, delay sweeps, design rankings, and safety-margin plots;
- the safety--informativeness trade-off for experimental identification.

These results, simulations, and figures do not appear in the previous submitted paper.

---

## 4. Textual-overlap check

I ran a normalized exact n-gram comparison on extracted PDF text, excluding bibliographies.
This is an internal diagnostic, **not a substitute for iThenticate/Turnitin**, but it is useful for detecting copied prose.

### Current main text vs previous paper

- exact 5-word sequences shared: **0**;
- exact 4-word n-grams from the current main body shared with the previous body: about **0.017%**;
- longest exact normalized token run: **4 tokens**.

### Current Supplement vs previous paper

- exact 5-word sequences shared: **0**;
- exact 4-word n-grams shared: about **0.014%**;
- longest exact normalized token run: **4 tokens**.

Therefore I found **no evidence of copied prose or recycled paragraphs**. The overlap is conceptual/model-level, not textual.

---

## 5. Figures and numerical outputs

I found no reused headline figure from the previous paper.

- The previous paper's characteristic visual is the certified Matignon `alpha*(A)` parameter grid and its certificate-driven stability presentation.
- The current paper's figures focus on competing memory laws, transfer magnitude/phase, finite-horizon approximation, experimental inputs, fractional-delay trajectories, `(alpha,tau)` maps, model-discrimination accuracy, and safety--informativeness.
- The current memory-discrimination atlas is a different mathematical/numerical object from the previous Matignon stability atlas.

The shared ecological schematic/backbone is redrawn for a new purpose and now explicitly attributes the inherited model to the previous study.

---

## 6. Changes made during this audit

To reduce any risk of redundant-publication/self-overlap concerns, I made the following edits.

### Main Introduction
Added an explicit relationship statement explaining that the previous paper established stability/certification results and that the present paper starts from that validated backbone to study active memory discrimination.

### Main Section 2
Added local attribution before the reused model, parameterization, equilibrium, Jacobian, and Matignon boundary. The text now states explicitly that these are inherited inputs, not present-paper contributions.

### Main figure captions
The ecological schematic/backbone captions now identify the previous study as the source of the inherited ecological geometry and distinguish the new intervention/observation architecture.

### Discussion
Added a dedicated paragraph `Relation to the previously submitted companion paper` giving a direct contribution-by-contribution distinction.

### Supplement
Compressed the old detailed backbone derivation. The Supplement no longer re-derives the previous paper's discriminant factorization, exact baseline critical-order calculation, or stability classification as if they were new. It records only the algebraic model/equilibrium/Jacobian quantities required by the new input/output theory and attributes the stability screening to the previous paper.

---

## 7. Submission recommendation

The papers are sufficiently distinct for separate submission **after these edits**. I recommend that the cover letter also disclose the relationship in one short paragraph and, if the submission system asks for related manuscripts, upload/cite the previous paper.

A defensible statement is:

> The manuscript uses the same validated strong-Allee predator--prey backbone as our previously submitted work on computer-assisted stability and extinction certification. The earlier paper addresses equilibrium/stability certification, global extinction/boundedness, and discretization error. The present manuscript asks a distinct experimental-identification question and develops competing memory models, transfer-based separation, finite-horizon discrimination limits, fractional-delay simulations, optimal perturbation design, and large-scale model-discrimination benchmarks. No figures, certificate results, or manuscript text from the previous submission are reused as new contributions.

## Final gate

**PASS - distinct contribution, low textual overlap, inherited model explicitly disclosed.**
