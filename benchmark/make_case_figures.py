"""Case-study figures: (1) trajectories under S0 vs multiscale across the four laws,
with the Allee threshold; (2) margin-vs-accuracy design plane (needs the BIC JSONs)."""
import json, os, sys
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, "rescue_compute")); sys.path.insert(0, HERE)
import case_study_vole as V

COL = {"ODE": "#0072B2", "Caputo": "#D55E00", "DDE": "#009E73", "latent3": "#CC79A7"}
LBL = {"ODE": "integer", "Caputo": r"Caputo $\alpha=0.4$", "DDE": r"delayed $\tau=0.35$", "latent3": "latent"}

def traj_fig():
    fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.4), sharey=True)
    for ax, dname, ttl in ((axs[0], "pwc6-S0", "(a) searched design S0, amplitude $8\\%\\,x^{*}$"),
                           (axs[1], "multiscale", "(b) multiscale, same amplitude")):
        uval = V.build_input(V.INPUTS[dname])
        for m in V.CAND:
            ts, tr = V.sim(m, uval)
            ax.plot(ts, tr[:, 0], color=COL[m], lw=1.3, label=LBL[m])
        ax.axhline(V.A_, color="k", lw=1.0, ls="--")
        ax.axhline(V.XSTAR, color="0.6", lw=0.8, ls=":")
        ax.set_xlabel("time (yr)")
        ax.set_title(ttl, fontsize=10, loc="left")
        ax.grid(alpha=0.25, lw=0.5)
    axs[0].set_ylabel("vole density $x(t)$ (voles/ha)")
    axs[0].text(11.9, V.A_+3, "$A$", fontsize=9, ha="right")
    axs[0].text(11.9, V.XSTAR+3, "$x^{*}$", fontsize=9, ha="right", color="0.45")
    axs[0].legend(fontsize=7.6, loc="lower left", framealpha=0.95, ncol=2)
    fig.tight_layout()
    out = os.path.join(ROOT, "paper_mdpi/fig_case_traj.pdf")
    fig.savefig(out, bbox_inches="tight"); print("wrote", out)
    for dname in ("pwc6-S0", "multiscale"):
        uval = V.build_input(V.INPUTS[dname])
        mg = {m: float(np.nanmin(V.sim(m, uval)[1][:, 0]) - V.A_) for m in V.CAND}
        print(f"  {dname}: " + "  ".join(f"{k}={v:+.1f}" for k, v in mg.items()))

def design_fig(jd):
    fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.8, 3.5))
    for name, r in jd.items():
        is_s0 = name == "pwc6-S0"
        ax.scatter([r["min_margin"]], [r["macro"]],
                   s=(80 if is_s0 else 60), marker=("s" if is_s0 else "o"),
                   facecolor=("#1b5e9c" if is_s0 else ("#b0d8a8" if r["min_margin"] > 0 else "#f2f2f2")),
                   edgecolor=("k" if is_s0 else ("#2e7d32" if r["min_margin"] > 0 else "#b3261e")),
                   linewidth=(0.8 if is_s0 else 1.1), zorder=4 if is_s0 else 3)
        dx = 6 if r["min_margin"] < 40 else -6
        ax.annotate(name, (r["min_margin"], r["macro"]), textcoords="offset points",
                    xytext=(dx, 4), fontsize=7.6, ha="left" if dx > 0 else "right",
                    fontweight="bold" if is_s0 else "normal")
    ax.axvline(0, color="0.55", lw=0.9); ax.grid(alpha=0.25, lw=0.5)
    ax.set_xlabel(r"minimum Allee margin $\min_t x(t)-A$ over the four laws (voles/ha)")
    ax.set_ylabel("four-class BIC macro-accuracy")
    ax.set_title("(a) design plane at the case-study cell", fontsize=10, loc="left")
    cls = V.CAND
    r_ms, r_s0 = jd["multiscale"]["recall"], jd["pwc6-S0"]["recall"]
    x = np.arange(len(cls)); w = 0.36
    bx.bar(x-w/2, [r_ms[c] for c in cls], w, color="#b0d8a8", edgecolor="#2e7d32", lw=0.9, label="multiscale")
    bx.bar(x+w/2, [r_s0[c] for c in cls], w, color="#1b5e9c", edgecolor="k", lw=0.7, label="S0 (pwc6)")
    bx.axhline(0.25, color="0.4", lw=0.9, ls="--")
    bx.set_xticks(x); bx.set_xticklabels([LBL[c].replace(" $\\alpha=0.4$","").replace(" $\\tau=0.35$","") for c in cls], fontsize=8.2)
    bx.set_ylabel("per-class recall"); bx.set_ylim(0, 1.1)
    bx.set_title("(b) where the difference lives", fontsize=10, loc="left")
    bx.legend(fontsize=8, loc="upper right", framealpha=0.95); bx.grid(axis="y", alpha=0.25, lw=0.5)
    fig.tight_layout()
    out = os.path.join(ROOT, "paper_mdpi/fig_case_design.pdf")
    fig.savefig(out, bbox_inches="tight"); print("wrote", out)

if __name__ == "__main__":
    traj_fig()
    merged = {}
    cdir = os.path.join(ROOT, "rescue_compute")
    for f in os.listdir(cdir):
        if f.startswith("out_") and f.endswith(".json"):
            d = json.load(open(os.path.join(cdir, f)))["designs"]
            merged.update(d)
    if len(merged) >= 7:
        design_fig(merged)
        for n, r in sorted(merged.items(), key=lambda kv: -kv[1]["macro"]):
            print(f"  {n:>11} macro={r['macro']:.4f} margin={r['min_margin']:+7.1f} recall=" +
                  " ".join(f"{k}:{v:.2f}" for k, v in r["recall"].items()))
    else:
        print(f"(design plane pending: {len(merged)}/7 BIC results)")
