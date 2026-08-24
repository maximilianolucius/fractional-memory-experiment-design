# Cover letter — CNSNS submission

**Status: draft, ready except for the bracketed line in §3, which depends on the Zenodo republish.**

---

To the Editors,
*Communications in Nonlinear Science and Numerical Simulation*

Dear Editors,

I submit for your consideration the manuscript **"Safe discrimination of fractional, delayed, and
latent memory beyond classical waveforms in a strong-Allee predator–prey model."**

## 1. What the paper does

Fitting a fractional order to ecological data does not establish a fractional mechanism: on a finite
horizon, delayed feedback or a few hidden states reproduce similar trajectories. The paper asks when
a controlled experiment can separate these mechanisms while keeping the prey population above its
Allee threshold, and it reports two results that point in opposite directions.

The first is a falsification. Restricted to six classical excitation families, the system appears to
impose a severe safety–informativeness frontier: the accuracy-leading designs all cross the Allee
threshold, and the only safe family is the least informative. The paper shows that this frontier
belongs to the waveform parameterisation rather than to the ecology. Reducing amplitude does not
restore safety — the leading design still crosses in 71% of cells at half amplitude, while its
realised response gain rises to 4.9 times the linear certificate, the signature of basin escape
rather than linear response. A constrained search over 163 840 candidate waveforms, at the same
peak-amplitude budget and under a hard margin constraint, instead returns piecewise-constant designs
with four-class model-selection accuracy 0.803 and no observed threshold crossings, against 0.514 for
the only safe classical family and 0.763 for the best classical design of any kind, which crosses in
36% of cells. A held-out comparison confirms the advantage is not an artifact of selecting and
evaluating at the same operating point: the searched designs lose 0.060 macro-accuracy on the
held-out Allee threshold while the classical families, never optimised at all, lose 0.087.

The second result survives the first and does not yield to input design. Computed directly at the
prey-response level rather than inferred from the memory kernel, finite-state surrogates reach an
`L¹` error of `5·10⁻⁵` at latent order 128, and the exact two-point minimax testing floor they induce
reaches 0.49999 — uniformly over every admissible input, since the surrogate error is an operator
norm. Identifying ecological memory is therefore limited by the declared rival-complexity budget
rather than by the safety margin.

## 2. Fit with CNSNS

The work sits in the journal's core: Caputo fractional dynamics, retarded delay systems, a
strong-Allee nonlinearity whose basin structure drives the safety question, large-scale simulation
(2268 benchmark cells at three amplitudes, no solver divergences), and numerical-methods content in
the validated-integration and interval-arithmetic components. The framing is experimental design and
identifiability rather than another parameter study of a fractional predator–prey model.

## 3. Prior dissemination

An earlier version of this manuscript was publicly posted as a Zenodo preprint,
**DOI 10.5281/zenodo.21809908**. The present submission is not a light revision. Its central
conclusion is the opposite of the preprint's: the preprint concluded that safe identification of
ecological memory is constrained by an intrinsic safety–informativeness trade-off, and the
adversarial waveform search reported here falsifies that conclusion. The finite-horizon
exponential-sum approximation result that the preprint presented as a contribution is demoted in this
version to a supporting lemma and attributed to McLean (2018) and the surrounding literature; the
response-level complexity analysis, the validated trajectory-safety verification and the held-out
generalisation test are new. The paper discloses the preprint in a dedicated section and cites it.

**[The preprint record's creator metadata has been corrected so that it is consistent with the
authorship of this submission.]** — *include this sentence only once the Zenodo record has actually
been republished; see the note at the end of this file.*

## 4. Related work by the author

The ecological backbone — the equations, locked parameters, coexistence equilibrium and Jacobian —
follows a companion certification study, which is cited in the manuscript and restated there only for
self-containment. No result of the present paper recertifies that backbone, and nothing from it is
claimed as a contribution here. The companion study certifies dynamical regimes of a specified Caputo
model; it does not address whether such a model can be distinguished from a delayed or latent
mechanism reproducing the same observations, which is the question posed here.

## 5. Data and reproducibility

All code and numerical artifacts are openly available at **DOI 10.5281/zenodo.22087770** (CC BY 4.0;
code under MIT). The deposit reproduces every headline result and contains the frozen outputs the
tables and figures were generated from, so the reported numbers can be verified without re-running
any computation. It includes a claim-to-artifact map naming the file and key for each reported value,
a SHA256 manifest, and the environment specification. The frozen four-class benchmark reproduces to
four decimal places on an independent host under a re-implemented driver and different library
versions.

## 6. Declarations

The manuscript has not been published elsewhere and is not under consideration by another journal.
There are no competing interests. The research received no external funding. AI-assisted tools were
used during manuscript preparation, as declared in the manuscript; responsibility for the scientific
content rests with the author.

Thank you for considering this submission.

Yours sincerely,

**Ibrahim Alraddadi**
Department of Mathematics, Faculty of Science
Islamic University of Madinah, Madinah 42351, Saudi Arabia
`ialraddadi@iu.edu.sa` · ORCID 0000-0002-0094-7937

---

## Note before sending

The bracketed sentence in §3 asserts that the preprint record's creator metadata has been corrected.
**That correction is prepared but not yet public.** The creator list on record
`10.5281/zenodo.21809908` was changed to Alraddadi (with ORCID) in an open edit draft, but the
republish step is pending — see `R5_PREPRINT_DISCLOSURE.md` §3. Publish the record first, then include
the sentence. Sending the letter with that claim while the public record still shows a different
creator would be a false statement to an editor.
