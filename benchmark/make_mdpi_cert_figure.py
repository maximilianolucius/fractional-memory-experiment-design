"""Certified approximation error and induced testing floor vs latent order m.
Panel (a): interval-certified L1 errors — optimised class (m<=32) and explicit
positive-SOE surrogate (m<=128). Panel (b): exact two-point testing floor.
All plotted values are certified bounds (Arb endpoints), not float estimates."""
import json, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from math import erfc, sqrt

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
r6 = json.load(open(os.path.join(ROOT, "rescue_compute/r6_response_interval_cert.json")))
ms = [4, 8, 16, 32, 64, 128]
E_sur = [r6[str(m)]["E_upper"] for m in ms]
F_sur = [r6[str(m)]["floor_lower"] for m in ms]
m_opt = [4, 8, 16, 32]
E_opt = [0.5334, 0.1254, 0.0273, 0.0069]          # T23 certified, A=0.25
def floor_exact(E, B=0.120, sig=0.10):
    d = E*B/sig
    return 0.5*erfc(d/2/sqrt(2))
F_opt = [floor_exact(e) for e in E_opt]

C_OPT, C_SUR = "#0072B2", "#D55E00"
fig, (ax, bx) = plt.subplots(1, 2, figsize=(9.6, 3.5))
ax.plot(ms, E_sur, "s-", color=C_SUR, ms=6, lw=1.2, label="explicit surrogate (certified, $m\\leq 128$)")
ax.plot(m_opt, E_opt, "o--", color=C_OPT, ms=6, lw=1.2, label="optimised class $\\mathcal{G}_m$ (certified, $m\\leq 32$)")
ax.set_xscale("log", base=2); ax.set_yscale("log")
ax.set_xticks(ms); ax.set_xticklabels(ms)
ax.set_xlabel("latent order $m$"); ax.set_ylabel(r"certified $\|g_\alpha-g_m\|_{L^1(0,T)}$")
ax.annotate(r"$4.89\cdot 10^{-5}$", (128, E_sur[-1]), textcoords="offset points",
            xytext=(-6, 10), ha="right", fontsize=8.5, color=C_SUR)
ax.legend(fontsize=8, loc="lower left", framealpha=0.95)
ax.grid(alpha=0.25, lw=0.5, which="both")
ax.set_title("(a) interval-certified response error", fontsize=10, loc="left")

bx.axhline(0.5, color="0.35", lw=1.0, ls=":")
bx.text(4.15, 0.502, "chance level $1/2$", fontsize=8.5, color="0.35", va="bottom")
bx.plot(ms, F_sur, "s-", color=C_SUR, ms=6, lw=1.2, label="floor from surrogate bound")
bx.plot(m_opt, F_opt, "o--", color=C_OPT, ms=6, lw=1.2, label="floor from $\\mathcal{G}_m$ bound")
bx.set_xscale("log", base=2); bx.set_xticks(ms); bx.set_xticklabels(ms)
bx.set_ylim(0.18, 0.53)
bx.set_xlabel("latent order $m$"); bx.set_ylabel(r"certified $P_e^{*}\ \geq$")
bx.annotate(r"$0.49999$", (128, F_sur[-1]), textcoords="offset points",
            xytext=(-4, -14), ha="right", fontsize=8.5, color=C_SUR)
bx.legend(fontsize=8, loc="lower right", framealpha=0.95)
bx.grid(alpha=0.25, lw=0.5)
bx.set_title("(b) induced exact minimax testing floor", fontsize=10, loc="left")
fig.tight_layout()
out = os.path.join(ROOT, "paper_mdpi/fig_cert_floor.pdf")
fig.savefig(out, bbox_inches="tight")
print("wrote", out)
for m, e, f in zip(ms, E_sur, F_sur): print(f"  m={m:>3}  E<={e:.6e}  floor>={f:.7f}")
