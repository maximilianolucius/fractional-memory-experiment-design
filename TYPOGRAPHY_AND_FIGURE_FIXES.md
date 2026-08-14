# Typography and Figure 1–2 fixes

## Global typography

- Main manuscript class changed from `11pt` to `10pt`.
- Supplement changed to `10pt` as well.
- Resulting pagination:
  - main paper: 63 -> 55 pages;
  - supplement: 23 -> 21 pages.
- Final compile has 0 undefined citations/references and 0 LaTeX/package warnings.
- Existing overfull-box count is essentially unchanged from the previous audited build; the font reduction did not introduce a new layout pathology.

This 10pt setting is appropriate for the current pre-submission PDF. A journal template such as `elsarticle` will ultimately control the production font size.

## Figure 1 — paper pipeline

Problems in the previous version:

- bottom-row boxes overlapped the footer/result text;
- the transition from step 5 to step 6 was visually ambiguous;
- several labels were unnecessarily long.

Changes:

- rebalanced the two rows vertically;
- removed the overloaded numerical footer and replaced it with a short conceptual progression line;
- added a clear step-5 -> step-6 transition;
- shortened box labels while preserving section mapping;
- increased effective figure text readability.

## Figure 2 — system / rival-memory schematic

Problems in the previous version:

- stale internal text incorrectly said that the Jacobian skeleton `J(A)` was shared by all rivals;
- the green rectangle was labelled as a safety rectangle, although it is only a benchmark diagnostic rectangle unless the strict invariance hypotheses are verified;
- dense text was difficult to scan.

Changes:

- corrected the central statement to:
  - ODE + Caputo share `J(A)`;
  - DDE + latent models are calibrated alternative response laws;
- renamed the green region `benchmark diagnostic rectangle R`;
- simplified and reflowed labels;
- improved spacing and text hierarchy;
- moved the Holling-II coupling label to avoid collision with the state boxes.

## Reproducibility

A dedicated generator was added:

`final_chief_checks/regenerate_fig01_fig02.py`

The original Q1 generator was also patched so that regenerating the schematic does not reintroduce the stale Jacobian/safety wording.

---

## Operator-requested follow-up (same day, post chief typography-fix)

### Figure 1 residual overflow

The chief's Figure 1 still had box labels wider than their boxes (rows crossed by
'5. Optimal experiment design' and '7. Bayesian extension'). Fixed in
final_chief_checks/regenerate_fig01_fig02.py: labels shortened to '5. Optimal design'
and '7. Bayesian layer (specified)', in-box font 8.5 -> 7.9. Figure 2 (fig11) was NOT
regenerated: its chief-audited bytes are preserved (md5 0ceaa3bb...). Note: the
generator resolves its output dir relative to its own location; when run from the
repo it writes to REPO_ROOT/figures/ - copy the result into paper/figures/.

### Font size 10pt -> 9pt

Per operator request, main and supplement now use documentclass[9pt]{extarticle}.
Pagination: main 55 -> 50 pages, supplement 21 -> 18 pages; 0 undefined, 0 warnings.
Overfull boxes DECREASED 27 -> 19 versus the 10pt control build (no new layout
pathology). As before, a journal template will control the production font.
