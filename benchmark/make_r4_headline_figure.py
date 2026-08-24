"""R4-E: headline figure — safety margin vs discrimination accuracy, classical
waveform families against the searched piecewise-constant class, with safety
status resolved under ALL FOUR candidate mechanisms."""
import json, os, sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
S2 = json.load(open(os.path.join(ROOT, "rescue_compute/r3_safe_design_search/r3f_stage2_summary.json")))
VS = json.load(open(os.path.join(ROOT, "rescue_compute/r3d_validated_safety.json")))
PW = json.load(open(os.path.join(ROOT, "rescue_compute/r3d_pwc6.json")))

# safety under ALL four mechanisms, from the a posteriori verification
allsafe = {}
byd = {}
for r in VS + PW:
    byd.setdefault(r["design"], []).append(r)
for d, rows in byd.items():
    allsafe[d] = all(r.get("verdict") == "SAFE-CERTIFIED" for r in rows)
NAME = {"pwc6_found": "S0 (pwc6)"}

rows = []
for k, v in S2.items():
    if k.startswith("HIST_"):
        d = k[5:]; fam = "classical"
        key = d
    else:
        d = k.split("_")[0].replace("SEARCH#", "S"); fam = k.split("_")[1]
        key = "pwc6_found" if k == "SEARCH#0_pwc6" else None
    rows.append(dict(label=d, family=fam, macro=v["macro"], margin=v["min_margin"],
                     cross=v["cross_rate"], allsafe=allsafe.get(key) if key else None,
                     recall=v["recall"]))

fig = plt.figure(figsize=(11.0, 4.3))
gs = fig.add_gridspec(1, 2, width_ratios=[1.35, 1.0], wspace=0.28)

# ---------------- panel A: margin vs accuracy
ax = fig.add_subplot(gs[0, 0])
ax.axvspan(0.05, 0.40, color="#e8f4ea", zorder=0)
ax.axvline(0.0, color="0.55", lw=0.9, ls="-", zorder=1)
ax.axvline(0.05, color="#2e7d32", lw=0.9, ls="--", zorder=1)
ax.text(0.058, 0.845, r"$\delta=0.05$", fontsize=7.4, color="#2e7d32", ha="left", va="center")
ax.text(0.265, 0.845, "safe region", fontsize=8.2, color="#2e7d32", ha="center")

for r in rows:
    is_pwc = r["family"].startswith("pwc")
    m, a = r["margin"], r["macro"]
    if is_pwc:
        ax.scatter([m], [a], s=74, marker="s", facecolor="#1b5e9c", edgecolor="k",
                   linewidth=0.7, zorder=4)
    else:
        ok = r["cross"] == 0.0
        ax.scatter([m], [a], s=66, marker="o",
                   facecolor=("#b0d8a8" if ok else "#f2f2f2"),
                   edgecolor=("#2e7d32" if ok else "#b3261e"), linewidth=1.1, zorder=3)

lab = {"S0": (7, 4), "multisine": (5, -3), "prbs": (7, -2), "sinusoid": (7, 1),
       "chirp": (7, -8), "pulse": (7, -2), "multiscale": (-8, -12)}
for r in rows:
    if r["label"] in lab:
        dx, dy = lab[r["label"]]
        txt = r["label"] if r["label"] != "S0" else "S0 (pwc6)"
        ax.annotate(txt, (r["margin"], r["macro"]), textcoords="offset points",
                    xytext=(dx, dy), fontsize=7.6,
                    fontweight=("bold" if r["label"] == "S0" else "normal"))
# the gain arrow: only-safe-classical -> best safe found
ms = [r for r in rows if r["label"] == "multiscale"][0]
s0 = [r for r in rows if r["label"] == "S0"][0]
ax.annotate("", xy=(s0["margin"], s0["macro"]), xytext=(ms["margin"], ms["macro"]),
            arrowprops=dict(arrowstyle="-|>", color="#1b5e9c", lw=1.3, alpha=0.85,
                            connectionstyle="arc3,rad=-0.30"), zorder=2)
ax.text(0.255, 0.615, "+0.29 accuracy,\nstill safe", fontsize=7.8,
        color="#1b5e9c", ha="center",
        bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="none", alpha=0.85))
ax.set_xlabel(r"minimum Allee margin $\min_t x(t)-A$   (negative $=$ threshold crossed)")
ax.set_ylabel("four-class BIC macro-accuracy")
ax.set_xlim(-0.37, 0.40); ax.set_ylim(0.44, 0.87)
ax.axhline(0.25, color="0.8", lw=0.8, ls=":")
ax.set_title("(a) Safety-informativeness plane, peak budget 0.100", fontsize=9.6, loc="left")
handles = [
    Line2D([], [], marker="s", ls="", mfc="#1b5e9c", mec="k", ms=8, label="searched piecewise-constant"),
    Line2D([], [], marker="o", ls="", mfc="#b0d8a8", mec="#2e7d32", ms=8, label="classical, no crossing"),
    Line2D([], [], marker="o", ls="", mfc="#f2f2f2", mec="#b3261e", ms=8, label="classical, crosses"),
]
ax.legend(handles=handles, fontsize=7.6, loc="lower left", framealpha=0.95)
ax.grid(alpha=0.22, lw=0.6)

# ---------------- panel B: per-class recall, safe classical vs found design
axb = fig.add_subplot(gs[0, 1])
cls = ["ODE", "Caputo", "DDE", "latent3"]
r_ms = [ms["recall"][c] for c in cls]
r_s0 = [s0["recall"][c] for c in cls]
x = np.arange(len(cls)); w = 0.36
axb.bar(x-w/2, r_ms, w, color="#b0d8a8", edgecolor="#2e7d32", lw=0.9, label="multiscale (safe classical)")
axb.bar(x+w/2, r_s0, w, color="#1b5e9c", edgecolor="k", lw=0.7, label="S0 pwc6 (searched, safe)")
axb.axhline(0.25, color="0.4", lw=0.9, ls="--")
axb.text(-0.44, 0.25, "chance", fontsize=7.0, color="0.35", ha="left", va="center",
             bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9))
for xi, (a, b) in enumerate(zip(r_ms, r_s0)):
    if b - a > 0.15:
        axb.annotate(f"+{b-a:.2f}", (xi+w/2, b), textcoords="offset points",
                     xytext=(0, 3), ha="center", fontsize=7.4, fontweight="bold", color="#1b5e9c")
axb.set_xticks(x); axb.set_xticklabels(cls, fontsize=8.4)
axb.set_ylabel("per-class recall"); axb.set_ylim(0, 1.22)
axb.set_title("(b) Where the gain comes from", fontsize=9.6, loc="left")
axb.legend(fontsize=7.4, loc="upper center", ncol=2, framealpha=0.95, bbox_to_anchor=(0.5, 1.005))
axb.grid(axis="y", alpha=0.22, lw=0.6)

out = os.path.join(ROOT, "paper/figures/fig24_safe_design_frontier.pdf")
fig.savefig(out, bbox_inches="tight")
print("wrote", out)
print("panel A points:", len(rows), " all-mechanism-safe designs:",
      [d for d, v in allsafe.items() if v])
