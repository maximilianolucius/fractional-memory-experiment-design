# R5-F — Pooled latent-class label repair

**Status: DONE, no recomputation. The frozen data files are untouched.**

---

## 1. The defect

The benchmark's four candidate classes are `ODE`, `Caputo`, `DDE`, `latent3`. Its data-generating
set, however, contains latent generators of **two** orders:

```
true generators present : Caputo, DDE, ODE, latent1, latent3
candidate hypotheses    : Caputo, DDE, ODE, latent3
cells per generator     : Caputo 288, DDE 96, ODE 96, latent1 96, latent3 96
```

Trajectories from the `latent1` generator are scored against the single `latent3` hypothesis, so
every class-wise statistic for that class is measured over data from **both** latent orders. The
manuscript called the class `latent-3`, which reads as "the order-3 model" and is wrong: the
reported recall of `0.242` is not the recall on order-3 data, it is the recall on pooled order-1 and
order-3 data.

This is a documentation defect, not a numerical one. Every number stays as computed.

## 2. Repairs, all in the manuscript

| location | change |
|---|---|
| `sec8` benchmark introduction | new paragraph stating the bookkeeping explicitly: one latent hypothesis (`m=3`), two latent generators (`m∈{1,3}`), and that the column "is a **pooled** class: its recall is measured over data generated at both latent orders, not at `m=3` alone" |
| `sec8` class-wise statistics | `latent-$3$: $0.242/0.848$` → `finite-latent (pooled $m\in\{1,3\}$ generators, single $m=3$ hypothesis): $0.242/0.848$` |
| `sec8` confusion-matrix caption | added: "The finite-latent row pools data generated at latent orders `m=1` and `m=3`, both scored against the single `m=3` latent hypothesis." |
| `sec8` waveform-search table caption | added: "The finite-latent column pools generators of order `m=1` and `m=3` against the single `m=3` hypothesis." |
| `sec2` model definitions | added, where the latent rival is introduced: "In the benchmark the latent *hypothesis* is fixed at `m=3` while latent *data* are generated at `m=1` and `m=3`; class-wise statistics for that class are therefore pooled over the two generators, and are labelled *finite-latent* rather than *latent-3* wherever this matters." |

Zero occurrences of `latent-$3$` remain in the manuscript. "pooled" appears three times in the
rendered PDF.

## 3. Data files

Unchanged, deliberately. The raw per-cell files keep the original generator labels in their `true`
field (`latent1` / `latent3`), so the pooling is reversible by anyone who wants the per-order
breakdown. Renaming labels in the frozen files would have broken the correspondence with the
frozen v3 benchmark and with every checksum in `MANIFEST_SHA256.txt`.

The mapping is documented for external readers in `public_reproducibility/README.md`, under
"One label to be aware of".

## 4. What this does *not* fix

The pooled recall still mixes two difficulties: order-1 latent data are easier to distinguish from
the fractional model than order-3 data, so the pooled figure is an average over unequal problems.
Splitting it would be informative but requires re-tabulating the frozen benchmark, which the chief
ruled out for this round (D8, D9). The manuscript now says what the number *is*; it does not claim
the split is uninteresting.
