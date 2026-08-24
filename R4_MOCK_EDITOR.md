# R4-I — Mock editor gate

**Verdict: 5 of 6 answers correct from the material alone. Question 3 fails.
`MOCK_EDITOR = FAIL` until the fix in §3 is applied. Two format defects also surfaced.**

---

## 0. Method, and its honest limitation

The material given to the mock editor is exactly what the chief specified: title, abstract, the
first 1.5 pages (through the contribution list), the main figure with its caption, and the
conclusions. Nothing else — no theory section, no benchmark tables, no supplementary documents.

**Limitation to state plainly:** I ran this myself, and I know what the rest of the paper says. That
biases the exercise in the paper's favour, so a "pass" here is weaker evidence than a pass from a
genuinely uninformed reader. What the exercise *can* do reliably is detect where the material is
**insufficient** — where answering requires information that is not on those pages. Two such gaps
were found, and both were real.

## 1. The six questions

### Q1 — What is new? ✔ CORRECT FROM MATERIAL

Answerable from the abstract and contribution list without help: a constrained search over
piecewise-constant waveforms finds designs that are both safe and substantially more informative
than any of the six classical families at the same amplitude budget (0.803 vs 0.514 / 0.763); the
apparent safety–informativeness frontier is therefore a property of the waveform parameterisation;
and, separately, a response-level latent-complexity obstruction persists to `m = 128`. The
contribution list also states explicitly what is *not* new (structural separation; the
positive-SOE construction, attributed to McLean).

### Q2 — What was falsified relative to the previous version? ✔ CORRECT FROM MATERIAL

The abstract states the previous reading ("which suggests an intrinsic safety–informativeness
frontier") and then refutes it ("We show that frontier belongs to the waveform parameterisation,
not to the system"). The conclusion repeats it with the mechanism. An editor gets this in one pass.

### Q3 — What is theorem vs empirical vs certified/verified? ✘ **FAILS**

From the given material an editor can see:
- "verified a posteriori by mesh refinement with a rigorous inter-node modulus, and for half of the
  headline trajectories by a validated enclosure" — clear, and correctly hedged;
- "Theorem 3.1" and "Corollary 3.3" referenced by number in the conclusion.

But the first 1.5 pages **never say which of the three headline contributions are theorems and
which are numerical experiments.** Contribution 3 reads as though the `m = 128` obstruction were
proved, when the manuscript's own position (correctly) is that the `m ≤ 32` bounds are interval
enclosures while the `m = 64, 128` values are high-accuracy floating-point evaluations that upper-bound
the certified quantity. An editor doing a suitability screen on the front matter would not know that,
and could reasonably feel misled on reaching Section 3.

**This is a genuine defect and it is the one the gate exists to catch.** Fix in §3.

### Q4 — Why CNSNS? ✔ CORRECT FROM MATERIAL

Fractional and delay dynamics, a strong-Allee nonlinearity with basin escape, large-scale
simulation, and a numerical-methods component (validated integration, interval arithmetic). Visible
from the abstract and contribution list.

### Q5 — Is any headline contradicted by the limitations? ✔ CORRECT

No. The abstract itself carries the counterweight — "A Pareto cost nevertheless remains, so safety
is not free" — and the figure caption states that the search gives existence, not a certified global
optimum. The safety wording is downgraded consistently. I looked specifically for a headline that
the limitations undercut and did not find one; this is the question that would have failed in the
Round-03 version, where the abstract asserted a general trade-off the paper's own data refuted.

### Q6 — Does it look like another fractional predator–prey simulation paper? ✔ CORRECT (no)

The title leads with "beyond classical waveforms", the abstract leads with a falsification, and the
figure is a design-space plane rather than a set of trajectories. The framing is experimental design
and identifiability, not another parameter study.

## 2. Format defects the gate surfaced

| # | defect | severity |
|---|---|---|
| F1 | The running header on every page reads **"AIMS Mathematics"**, and the front matter carries an AIMS journal banner, DOI/Received/Accepted stubs and "Research article" label. Submitting this to CNSNS would show an editor, on page 1, that the manuscript was prepared for a different journal. | **MUST_FIX before submission** |
| F2 | Duplicated provenance: an older paragraph ("The ecological backbone is not built here…") and the new neutral paragraph both appeared on page 1. **Fixed this round** — the old paragraph is deleted and the two facts worth keeping were folded into the neutral one. | fixed |
| F3 | The safety paragraph on page 1 quoted "the best-discriminating input crosses the threshold in 100% of stable-regime cells" with no forward reference, so a reader of page 1 alone would carry away exactly the claim the paper refutes. **Fixed this round** by scoping it to the classical families and pointing at the falsification. | fixed |

F1 is the same item as `R4_FORMAT_AND_ENDMATTER_AUDIT.md` §4 (template conversion). The gate
escalates it: it is not merely a formatting preference, it is visible to the editor in the first
second and it signals a rejected-elsewhere manuscript.

## 3. Required fix for Q3

Add one sentence at the end of the contribution list, before the "not contributions" paragraph:

> Contributions 1, 2 and 5 are empirical, established by the benchmark and the search; contribution
> 3 combines a proved bound (Theorem~\ref{thm:T20}) with computed surrogate errors, interval-enclosed
> for $m\le32$ and high-accuracy numerical for $m=64,128$; contribution 4 is a verification result
> whose exact status is stated per trajectory in Section~\ref{sec:benchmark}.

That is the minimum that makes Q3 answerable from the front matter. Applied below.

## 4. Re-run after the fix

With the sentence added, Q3 is answerable: an editor can classify every headline claim by evidence
type without leaving page 2. **`MOCK_EDITOR = PASS` conditional on F1 (template) being closed**, since
an editor who sees "AIMS Mathematics" in the header will not get as far as the questions.
