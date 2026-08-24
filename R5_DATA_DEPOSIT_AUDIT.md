# R5-D — Curated reproducibility deposit

**Status: BUILT AND VERIFIED. Ready for upload. No DOI yet — that is the remaining blocker.**

`public_reproducibility/` — 50 files, 2.8 MB.

---

## 1. Contents against the chief's minimum list

| required | present |
|---|---|
| final benchmark code needed for manuscript results | `code/benchmark/` — `core.py`, `bench.py`, `designs.py`, `run_all.py`, `make_figures.py`, `make_r4_headline_figure.py`, `smoke_test.py`, `validate_results.py` |
| Round-03/04 scripts behind headline claims | `code/rescue_compute/` — 9 scripts: complexity law, response semantics, interval constants, validated safety, response certification, waveform search stages 1–2, enclosure, three-amplitude benchmark |
| frozen outputs used by final tables/figures | `data/` — 8 top-level JSON, `safe_design_search/` (7 files incl. per-cell 672-cell record and the held-out test), `benchmark_v4/` (summary + both raw shards), `benchmark_v3_frozen/` (the frozen four-class benchmark) |
| exact PWC waveform parameters | `README.md` §"The headline waveform" — Sobol coordinates, resulting levels, and the scaling convention |
| seed formula and benchmark configuration | `README.md` §Determinism — `1000 + 7919*k + floor(100*amp)`, plus search protocol constants |
| environment specification | `requirements.txt` — exact versions for both hosts, with a note that the cross-host reproduction spanned two different `numpy`/`scipy` versions |
| README with reproduction commands | `README.md` — layout, a no-recompute verification snippet, the seven-step re-run sequence with wall-clock estimates and worker counts |
| claim → artifact map | `CLAIM_ARTIFACT_MAP.md` — every abstract number and every headline claim, with file **and key** |
| SHA256 manifest | `MANIFEST_SHA256.txt` — 49 entries, verified |
| licences | `LICENSE-CODE.txt` (MIT), `LICENSE-DATA.txt` (CC BY 4.0) |

## 2. Excluded, per the chief's instruction

No chief reviews, researcher assignments, round decisions, retraction histories, recovery plans,
compliance matrices, orchestration state, or historical backups. The package contains code, data,
and the three documents needed to use them.

## 3. Verification actually performed

Not just assembled — tested.

| test | result |
|---|---|
| SHA256 manifest self-check (`sha256sum -c`) | **49/49 OK** |
| package copied to a clean directory, then `python3 benchmark/smoke_test.py` | **`SMOKE OK` (36.8 s)** — solvers, all four mechanisms, safety metrics and the BIC selector all run standalone |
| headline figure regenerated from the package's own frozen data | **wrote `figures/fig24_safe_design_frontier.pdf`**, 12 points, and independently re-derived that only `multiscale` and `pwc6_found` are safe under all four mechanisms |
| every file/key cited in `CLAIM_ARTIFACT_MAP.md` resolves | verified programmatically: `n_eval=163840`, `n_safe=87601`, `cross_rate=0.714`, `L1(m=128)=4.83e-05`, 4 rigorous enclosures, `U_NL=1.419e-03` |
| README's verification snippet reproduces the three abstract numbers | **`0.8030 / 0.5141 / 0.7628`** with matching crossing rates |

## 4. Two fixes the testing forced

**(a) The figure script was not portable.** It resolved artifacts through the development repository
layout (`rescue_compute/r3_safe_design_search/...`), which does not exist in the package, so it
failed with `FileNotFoundError` on a clean copy. Rewritten with a `_find()` helper that accepts
either the package layout (`data/...`) or the repository layout, and it now writes to the package's
`figures/` when run from there. The package copy and the repository copy are the same file.

**(b) Internal paths removed.** `~/fmi_venv/bin/python` (a virtualenv belonging to a sibling
project) appeared in two docstrings and would have confused an external reader; replaced by
`python3`. One script wrote to a scratch path under `/media/...`; now writes next to its inputs.

Scanned for credentials and infrastructure detail: no passwords, tokens, IP addresses or hostnames
beyond the compute host's name appearing in provenance logs, which is legitimate metadata.

## 5. The remaining blocker

The manuscript's data-availability statement reads:

> The code and research data supporting the findings of this study are available in
> [REPOSITORY], [DOI].

Both placeholders must be substituted before submission — the chief's rule is that the final package
contains no placeholder text. The upload itself is a single action: the directory is final, checksummed
and tested. What it needs is a Zenodo deposit and the DOI it returns.

**One caution on the deposit, carried over from `AUTHOR_METADATA_CONFIRMATION.md` §4.** There is
already a public Zenodo record of this work (`10.5281/zenodo.21809908`) whose sole listed creator is
not the submitting author. Whatever creator list the new data deposit is given should be consistent
with the manuscript's authorship and with however that existing record is resolved. Uploading the
data package under one name while the article carries another would compound the discrepancy rather
than settle it.
