# Chief lightweight checks

`check_strict_rectangle.py` reproduces the reviewer-side four-face test used to audit the wording around the benchmark rectangle. It is a lightweight algebraic check, not a simulation campaign.

Expected result at the current benchmark settings: `STRICT_T17_FACE_TEST: FAIL`. Therefore the plotted rectangle can be used as a numerical diagnostic region, but Theorem T17 does not certify it as positively invariant under the full `|u| <= 0.10` prey-input budget.
