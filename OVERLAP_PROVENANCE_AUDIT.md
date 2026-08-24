# OVERLAP_PROVENANCE_AUDIT — Round 01, Task 7

**Central problem resolved here.** The manuscript repeatedly writes *"our previously submitted
companion paper"*, but its author list and the author of `P01` are **different people**. This is an
authorship misstatement, not a style preference, and it must be corrected before any resubmission.

---

## 1. The inconsistency, precisely

| Item | Value |
|---|---|
| Present manuscript author | **Ibrahim Alraddadi** (single author), Islamic University of Madinah |
| `P01` bibliography author | **Lucius, Maximiliano** |
| `P01` identity | *Computer-Assisted Stability and Extinction Certificates for a Caputo Predator–Prey System with a Strong Prey Allee Effect*; note field: companion manuscript, draft 2026-07-30, **published as Zenodo preprint DOI 10.5281/zenodo.21809908** |
| First-person phrasing found | "previously submitted companion paper", "previously submitted paper" (15 occurrences, `sec1.tex` and `sec10.tex`) |

**Verdict.** Every first-person reference to `P01` is factually incorrect and must be replaced by
neutral third-person provenance. A referee who checks the Zenodo record sees a different author and
concludes either an undisclosed authorship change or a misrepresentation — both fatal at desk stage.

**Secondary point.** `P01` is now a **published Zenodo preprint with a DOI**, not an unpublished
private draft. That helps self-containment (it is citable and permanently retrievable) but does *not*
make it peer-reviewed; it cannot carry a proof the present paper depends on.

---

## 2. Inventory of reused material

Declared in the manuscript verbatim: *"inherited from `\cite{P01}`: the strong-Allee equations, the
locked parameters, the coexistence equilibrium, and `J(A)`"*, and *"the shared material is the
strong-Allee backbone with its locked parameterization"*.

| Category | Reused? | What exactly | Must be reproduced for self-containment? |
|---|---|---|---|
| Model equations | **yes** | Strong-Allee predator–prey vector field with Holling-II response | **Yes** — 2 displayed equations |
| Locked parameters | **yes** | `r=3/2, K=1, a=1, h=1/2, e=4/5, m=2/5` | **Yes** — one line |
| Coexistence equilibrium | **yes** | `x*=m/(a(e−mh))=2/3`, `y*(A)=2(2−3A)/(9A)` | **Yes** — derivation is 3 lines |
| Jacobian | **yes** | `J(A)`, `T(A)=(7A−2)/(8A)`, `D(A)=(2−3A)/(20A)` | **Yes** — direct differentiation |
| Matignon boundary `α*(A)` | **yes** (as an admissibility filter) | `α*(A)=(2/π)arctan(√(4D−T²)/T)` | **Yes** — statement + citation of the sector condition |
| Extinction / boundedness statements | referenced | global extinction funnel below `A` | **No** — cite only; not load-bearing for any present result |
| Interval/Krawczyk certificates of `P01` | **no** | — | No |
| Certified parameter grid, certificate inventory | **no** | — | No |
| Figures | **none shared** (verified: no figure file is imported from `P01`) | — | — |
| Text | descriptive backbone sentences | ecological setup prose | Rewrite in the author's own wording |
| **Dependence on an unpublished result** | **none identified** | every inherited item is elementary algebra reproducible in ≤1 page | — |

**Key finding for Gate G4.** Nothing the present paper *proves* depends on a result that exists only
inside `P01`. The entire inherited layer is elementary, verifiable algebra (equilibrium, Jacobian,
trace/determinant, sector condition). Therefore **full self-containment is achievable in roughly one
page** and does not require reproducing `P01`'s certification machinery.

---

## 3. The Introduction comparison table — remove

`sec1.tex` lines 22–32 contain a 3-column, 5-row table:
`Aspect | Previously submitted paper~\cite{P01} | Present paper`, with rows *Scientific question,
Shared material, Primary mathematics, Primary computation, Headline output*.

**Recommendation: delete from the main text.** It is a defensive artifact: it spends prime
novelty real estate (the Introduction) explaining what the paper is *not*. Its content belongs in
(a) the cover letter, and (b) a short internal disclosure file for the editor if requested.

Replace with a **single provenance paragraph** (proposed wording below).

---

## 4. Recommended neutral provenance wording

For the Introduction (one paragraph, no table):

> The ecological backbone used here — the strong-Allee predator–prey model with Holling type-II
> response, its locked parameterization, the coexistence equilibrium `(x*,y*(A))` and the Jacobian
> `J(A)` — follows the companion certification study [P01], where those objects were derived and
> verified with validated numerics. For completeness, Section 2 restates the equations, parameters,
> equilibrium and Jacobian used in this paper, so that all results below can be checked without
> consulting [P01]. The present work addresses a different question: not whether the dynamical
> regimes of that model can be certified, but whether — and under what safety-constrained
> excitation — its memory mechanism can be identified at all.

For any in-text reuse marker, use *"follows [P01]"*, *"as derived in [P01]"*, *"restated here from
[P01] for completeness"*. **Never** *"our previous paper"*, *"our companion paper"*, *"we previously
showed"*.

---

## 5. Novelty-disclaimer language to remove from the main text

These are separate from provenance and cost novelty budget directly (all verified present):

| Text found | Action |
|---|---|
| "no novelty is claimed for safe experimental design per se" | Move to cover letter; in the paper, state positively what *is* new |
| "inherited inputs, not new contributions of the present paper" | Delete; the provenance paragraph already covers it |
| "Inherited backbone versus new experimental layer" (heading) | Delete heading; fold into §2 |
| repeated "inherited from [P01]" (5 occurrences) | Keep **one** at first use, in §2 |

---

## 6. Similarity / iThenticate posture

- **Unavoidable overlap:** the model equations, parameter values, equilibrium and Jacobian. These are
  *mathematical objects*; identical formulas are legitimate and expected. Label the restatement
  explicitly ("restated from [P01]").
- **Avoidable overlap:** descriptive prose about the ecological setup, and any methods sentences
  carried over. Rewrite in the author's own words.
- **Zero figure overlap** — verified; keep it that way.
- The earlier AI-detection pass (documented in `HANDOFF.md`) already rewrote much of the prose;
  re-run similarity comparison against the **Zenodo published version** of `P01` (now public), not
  against a private draft, since a public preprint will be indexed.

---

## 7. Gate status

| Gate | Status |
|---|---|
| G4 self-containment | **achievable** — no critical mathematical dependency on `P01`; needs ~1 page of restatement |
| Authorship consistency | **currently FAILING** — 15 first-person references must be rewritten |
| Figure overlap | PASS (none) |
| Disclosure location | to be moved: main text → cover letter + §2 provenance paragraph |
