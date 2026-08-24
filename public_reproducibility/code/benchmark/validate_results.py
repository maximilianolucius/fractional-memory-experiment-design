#!/usr/bin/env python3
"""Internal-consistency checks for the archived benchmark summaries.

The script does not establish scientific validity or rerun the full Monte Carlo
campaign. It verifies that aggregate claims imported by the manuscript agree with
the included confusion matrices, per-cell records, solver errors, and analytic
gates.
"""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
TOL = 1e-12


def load(name: str):
    return json.loads((RESULTS / name).read_text())


def close(a: float, b: float, tol: float = TOL) -> bool:
    return math.isclose(float(a), float(b), rel_tol=tol, abs_tol=tol)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS: {message}")


def metrics(confusion: dict[str, dict[str, int]]):
    classes = list(confusion)
    total = sum(sum(row.values()) for row in confusion.values())
    diagonal = sum(confusion[c][c] for c in classes)
    recalls = {
        c: confusion[c][c] / sum(confusion[c].values()) for c in classes
    }
    precisions = {}
    for c in classes:
        col = sum(confusion[r][c] for r in classes)
        precisions[c] = confusion[c][c] / col
    return total, diagonal / total, sum(recalls.values()) / len(recalls), recalls, precisions


def main() -> None:
    nonlinear = load("nonlinear_confusion.json")
    solver = load("solver_validation.json")
    gates = load("gates.json")
    linear = load("linear_factorial.json")

    check(gates["PASS"] and gates["x_star_ok"] and gates["alpha_star_0.30_ok"],
          "analytic gate flags are true")
    check(close(gates["x_star"], 2 / 3), "coexistence prey coordinate equals 2/3")
    check(close(gates["alpha_star_0.30"], gates["alpha_star_0.30_ref"], 1e-14),
          "critical order matches the independent reference")
    check(gates["ranks_full"], "tested controllability/observability ranks are full")

    errs = [solver[f"N={n}"]["max_abs_err"] for n in (250, 500, 1000)]
    check(errs[0] > errs[1] > errs[2] > 0, "solver error decreases under grid refinement")
    check(solver["converges"] and solver["PASS"], "solver summary reports convergence")
    check(close(errs[-1], solver["final_err"]), "final solver error equals the finest-grid error")

    check(nonlinear["n_cells"] == nonlinear["stable"]["n_good"] + nonlinear["verdict"]["n_good"],
          "stable and verdict cells partition the archived nonlinear grid")

    for regime in ("stable", "verdict"):
        summary = nonlinear[regime]
        conf = summary["confusion_4class"]
        total, micro, macro, recalls, precisions = metrics(conf)
        expected = summary["n_good"] * nonlinear["reps_per_cell"]
        check(total == expected, f"{regime} confusion total equals cells x replicates")
        check(close(micro, summary["micro_accuracy"]), f"{regime} micro accuracy matches confusion matrix")
        check(close(macro, summary["macro_accuracy"]), f"{regime} macro recall matches confusion matrix")
        for c in conf:
            check(close(recalls[c], summary["per_class_recall"][c]),
                  f"{regime} recall for {c} matches confusion matrix")
            check(close(precisions[c], summary["per_class_precision"][c]),
                  f"{regime} precision for {c} matches confusion matrix")

    rows = [json.loads(line) for line in (RESULTS / "state_nl.jsonl").read_text().splitlines() if line.strip()]
    check(len(rows) == nonlinear["n_cells"], "per-cell JSONL length matches n_cells")
    safety = defaultdict(lambda: {"n": 0, "crossed": 0, "min_margin": math.inf})
    for row in rows:
        if row.get("regime") != "stable" or row.get("diverged"):
            continue
        name = row["input"]
        rec = safety[name]
        rec["n"] += 1
        rec["crossed"] += int(row["safety"]["allee_crossed"])
        rec["min_margin"] = min(rec["min_margin"], float(row["safety"]["allee_margin"]))
    for name, rec in safety.items():
        archived = nonlinear["safety_stable"][name]
        check(rec["n"] == archived["n"], f"stable safety cell count for {name} matches JSONL")
        check(rec["crossed"] == archived["crossed"], f"threshold-crossing count for {name} matches JSONL")
        check(close(rec["crossed"] / rec["n"], archived["allee_cross_rate"]),
              f"threshold-crossing rate for {name} is consistent")
        check(close(rec["min_margin"], archived["min_allee_margin"]),
              f"worst Allee margin for {name} matches JSONL")

    by_design = defaultdict(list)
    for row in linear["rows"]:
        if close(row["A"], 0.25):
            by_design[row["input"]].append(float(row["min_pairwise_KL"]))
    stable_means = {k: sum(v) / len(v) for k, v in by_design.items()}
    best = max(stable_means, key=stable_means.get)
    check(best == "pulse", "stable-only linear subset has pulse as the largest mean min-pairwise KL")
    check(len(linear["rows"]) == 1458, "linear factorial contains 1458 cells")

    print("\nALL ARCHIVED-RESULT CONSISTENCY CHECKS PASSED")


if __name__ == "__main__":
    main()
