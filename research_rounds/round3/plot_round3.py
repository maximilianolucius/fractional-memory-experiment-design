#!/usr/bin/env python3
"""plot_round3.py — diagnostic figures for Round 3 (E_m law + safety repair)."""
import json
import os

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "round3_results.json")))

plt.rcParams.update({"font.size": 9, "pdf.fonttype": 42})
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.0))

# --- (a) E_m law ---
ax = axs[0]
cells = d["track_A"]["cells"]
mm = np.array([c["m"] for c in cells])
ee = np.minimum.accumulate(np.array([c["E_m"] for c in cells]))
ax.semilogy(mm, ee, "o-", color="#7c3aed", label="best displayed $E_m$ (envelope)")
ax.semilogy(mm, [c["T9b_bound_at_tuned"] for c in cells], "s--", color="0.55",
            label="Theorem T9b bound")
ax.set_xlabel("latent modes $m$"); ax.set_ylabel("$L^1(0,T)$ kernel error")
ax.set_title("(a) Latent approximation error $E_m(\\alpha,T)$")
ax.grid(alpha=0.3, which="both"); ax.legend(fontsize=7.5)

# --- (b) high-frequency null direction ---
ax = axs[1]
hf = d["track_B"]["hf_null"]
eps = np.array([r["eps"] for r in hf])
sx = np.array([r["sup_x_unit_energy"] for r in hf])
ax.loglog(eps, sx, "D-", color="#c4463f")
ax.set_xlabel("oscillation scale $\\varepsilon$ (unit $\\|u\\|_2=1$)")
ax.set_ylabel("$\\sup_t |x_\\varepsilon(t)|$")
ax.set_title("(b) Null direction: prey excursion $\\to 0$ as $\\varepsilon\\to0$")
ax.grid(alpha=0.3, which="both")
ax.text(0.05, 0.9, "no Allee-only outer\nenergy bound exists", transform=ax.transAxes,
        fontsize=8, color="#c4463f", va="top")

# --- (c) effective outer bound vs A ---
ax = axs[2]
eb = d["effective_outer_bounds"]
for fam, col in [("pulse", "#3f8f5f"), ("multiscale", "#d98e2b")]:
    cs = [c for c in eb if c["family"] == fam]
    ax.plot([c["A"] for c in cs], [c["outer_rho_over_kappa_inf"] for c in cs],
            "o-", color=col, label=f"$\\rho_\\eta/\\kappa^\\infty$ [{fam}]")
cap = np.sqrt(d["params"]["T"]) * d["params"]["u_max"]
ax.axhline(cap, ls="--", color="0.4")
ax.text(0.255, cap * 1.03, "actuator cap $\\sqrt{T}\\,u_{\\max}$", fontsize=7.5, color="0.3")
ax.set_xlabel("Allee threshold $A$"); ax.set_ylabel("outer safe energy bound")
ax.set_title("(c) Outer bound: coercive class vs actuator cap")
ax.grid(alpha=0.3); ax.legend(fontsize=7)

fig.tight_layout()
fig.savefig(os.path.join(HERE, "round3_diagnostic.pdf"))
print("wrote round3_diagnostic.pdf")
