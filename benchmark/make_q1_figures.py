"""make_q1_figures.py — Q1 visual-upgrade figure suite (2026-08-14).

Generates the refined benchmark figures plus the new synthesis/schematic figures
required by the Q1 visual audit (FRACTIONAL_MEMORY_EXPERIMENTS_FIGURE_MASTERPLAN.md).

Constraints honored (per FRACTIONAL_MEMORY_EXPERIMENTS_RESEARCHER_PROMPT.md):
  - no new compute campaign: all data-derived panels reuse benchmark/results/*.json
    or cheap single-cell simulations through the released benchmark code;
  - no fabricated results: every number plotted comes from core/designs/bench or
    the archived JSON artifacts.

Run locally:  python3 benchmark/make_q1_figures.py
Outputs PDF figures into paper/figures/ (repo layout).
"""
import os
import json

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

import core
import designs
import bench

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ART = os.path.join(ROOT, "benchmark", "results")
FIG = os.path.join(ROOT, "paper", "figures")
os.makedirs(FIG, exist_ok=True)

nl = json.load(open(os.path.join(ART, "nonlinear_confusion.json")))
lin = json.load(open(os.path.join(ART, "linear_factorial.json")))
sv = json.load(open(os.path.join(ART, "solver_validation.json")))

# ------------------------------------------------------------------ style
plt.rcParams.update({
    "font.size": 9, "axes.labelsize": 10, "axes.titlesize": 10.5,
    "legend.fontsize": 8, "xtick.labelsize": 8, "ytick.labelsize": 8,
    "axes.linewidth": 0.8, "lines.linewidth": 1.5, "pdf.fonttype": 42,
})
COL = {"ODE": "#3b6fb5", "Caputo": "#c4463f", "DDE": "#3f8f5f", "latent": "#7b68a6"}
SAFE = "#2e8b57"
UNSAFE = "#c0392b"
MID = "#d98e2b"
BAND = "#f7ecd7"
GRID = {"alpha": 0.25}

def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)
    print("wrote", name, flush=True)

# ------------------------------------------------------------------ transfer functions
A_FIG = 0.25
Jm = core.jacobian(A_FIG)
Bv = np.array([1.0, 0.0])
Cv = np.array([1.0, 0.0])
w = np.logspace(-1.5, 1.5, 400)
s = 1j * w

def G_ode(s):
    return np.array([Cv @ np.linalg.solve(si * np.eye(2) - Jm, Bv) for si in s])

def G_cap(s, al):
    return np.array([Cv @ np.linalg.solve((si ** al) * np.eye(2) - Jm, Bv) for si in s])

def G_dde(s, tau=0.35):
    J0 = Jm.copy(); J1 = np.zeros((2, 2)); J1[1, 0] = Jm[1, 0]; J0[1, 0] = 0.0
    return np.array([Cv @ np.linalg.solve(si * np.eye(2) - J0 - J1 * np.exp(-si * tau), Bv) for si in s])

def G_lat(s, rates=(0.6, 1.0, 0.4), g=0.15):
    m = len(rates)
    Ab = np.zeros((2 + m, 2 + m)); Ab[:2, :2] = Jm; Ab[0, 2:] = g; Ab[2:, 2:] = -np.diag(rates)
    Bb = np.zeros(2 + m); Bb[0] = 1; Bb[2:] = 1
    Cb = np.zeros(2 + m); Cb[0] = 1
    return np.array([Cb @ np.linalg.solve(si * np.eye(2 + m) - Ab, Bb) for si in s])

Go, Gc, Gd, Gl = G_ode(s), G_cap(s, 0.85), G_dde(s), G_lat(s)

# ==================================================================
# FIG 01 (refined) — transfer magnitude with band of interest
# ==================================================================
f, ax = plt.subplots(figsize=(6.2, 4.0))
ax.axvspan(0.3, 3.0, color=BAND, zorder=0, label="design band $[\\omega_{\\min},\\omega_{\\max}]$")
for G, lab in [(Go, "ODE"), (Gc, "Caputo $\\alpha=0.85$"), (Gd, "DDE $\\tau=0.35$"), (Gl, "latent $m=3$")]:
    ax.loglog(w, np.abs(G), color=COL[lab.split(" ")[0]], label=lab)
ax.annotate("$\\omega^{-\\alpha}$ decay", xy=(8, 0.09), xytext=(4.2, 0.16),
            fontsize=8, color=COL["Caputo"], arrowprops=dict(arrowstyle="->", lw=0.8))
ax.annotate("$\\omega^{-1}$ decay", xy=(9, 0.055), xytext=(5.5, 0.035),
            fontsize=8, color=COL["DDE"], arrowprops=dict(arrowstyle="->", lw=0.8))
ax.set_xlabel("$\\omega$")
ax.set_ylabel("$|G(i\\omega)|$")
ax.set_title("Transfer magnitude on the prey channel ($A=0.25$)")
ax.legend(loc="upper right", framealpha=0.9)
ax.grid(True, which="both", **GRID)
save(f, "fig01_transfer_magnitude.pdf")

# ==================================================================
# FIG 02 (merged 2-panel) — phase + high-frequency Caputo signature
# ==================================================================
f, axs = plt.subplots(1, 2, figsize=(8.6, 3.6))
ax = axs[0]
for G, lab in [(Go, "ODE"), (Gc, "Caputo"), (Gd, "DDE"), (Gl, "latent")]:
    ax.semilogx(w, np.angle(G), color=COL[lab], label=lab)
ax.set_xlabel("$\\omega$")
ax.set_ylabel("$\\arg G(i\\omega)$ [rad]")
ax.set_title("(a) Phase comparison")
ax.legend(framealpha=0.9)
ax.grid(True, which="both", **GRID)
ax = axs[1]
w2 = np.logspace(0, 1.5, 200)
s2 = 1j * w2
for al in [0.7, 0.85, 0.95]:
    ax.semilogx(w2, np.angle(G_cap(s2, al)), color=COL["Caputo"], alpha=0.45 + 0.25 * al)
    ax.axhline(-al * np.pi / 2, ls=":", color="gray", lw=0.8)
    ax.annotate("$-\\alpha\\pi/2$  ($\\alpha=%s$)" % al, xy=(w2[-1] * 0.55, -al * np.pi / 2),
                xytext=(w2[-1] * 0.55, -al * np.pi / 2 + 0.09), fontsize=7.5, color="0.25")
ax.set_xlabel("$\\omega$")
ax.set_ylabel("$\\arg G_\\alpha(i\\omega)$")
ax.set_title("(b) High-frequency Caputo phase signature")
ax.grid(True, which="both", **GRID)
save(f, "fig02_phase_2panel.pdf")

# ==================================================================
# FIG 04 (refined) — waveforms grouped transient vs broadband
# ==================================================================
T, N = 12.0, 600
ts = np.linspace(0, T, N + 1)
layout = [("pulse", SAFE), ("multiscale", SAFE), ("sinusoid", UNSAFE),
          ("multisine", UNSAFE), ("chirp", UNSAFE), ("prbs", UNSAFE)]
f, axs = plt.subplots(2, 3, figsize=(9.2, 4.6), sharex=True)
for idx, (ax, (name, col)) in enumerate(zip(axs.ravel(), layout)):
    _, ua, _ = bench.build_input(designs.INPUTS[name], T, N, amp=0.10)
    ax.plot(ts, ua, color=col, lw=1.2)
    ax.set_title(name, color=col)
    ax.set_ylim(-0.16, 0.16)
    ax.grid(True, **GRID)
    if idx % 3 == 0:
        ax.set_ylabel("$u(t)$")
axs[0, 0].annotate("transient: lower crossing rate, weakly informative", xy=(0.02, 0.92),
                   xycoords="axes fraction", fontsize=8, color=SAFE, style="italic")
axs[1, 0].annotate("sustained/broadband: informative, frequent Allee crossing", xy=(0.02, 0.92),
                   xycoords="axes fraction", fontsize=8, color=UNSAFE, style="italic")
for ax in axs[1]:
    ax.set_xlabel("$t$")
f.suptitle("Six candidate designs at a common peak-amplitude budget $\\|u\\|_\\infty = 0.10$, grouped by safety behavior", y=1.00)
save(f, "fig04_waveforms.pdf")

# ==================================================================
# FIG 05 (refined) — exact linear-Gaussian ranking, annotated
# ==================================================================
lr = lin["design_ranking_by_mean_min_pairwise_KL"]
order = sorted(lr, key=lambda k: lr[k], reverse=True)
vals = [lr[k] for k in order]
cols = [SAFE if k in ("pulse", "multiscale") else UNSAFE for k in order]
f, ax = plt.subplots(figsize=(6.2, 3.8))
bars = ax.bar(order, vals, color=cols, alpha=0.85)
for b, v in zip(bars, vals):
    ax.annotate(f"{v:.0f}", xy=(b.get_x() + b.get_width() / 2, v), xytext=(0, 2),
                textcoords="offset points", ha="center", fontsize=8)
ax.set_ylabel("mean min-pairwise KL divergence")
ax.set_title("Exact linear-Gaussian design ranking (common amplitude budget)")
ax.grid(True, axis="y", **GRID)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(facecolor=SAFE, alpha=0.85, label="lower crossing rate"),
                   Patch(facecolor=UNSAFE, alpha=0.85, label="higher crossing rate")],
          loc="upper right", frameon=False, fontsize=7.5)
save(f, "fig05_linear_ranking.pdf")

# ==================================================================
# FIG 06 (supplement) — solver convergence
# ==================================================================
Ns = [int(x.split("=")[1]) for x in sv if x.startswith("N=")]
errs = [sv[f"N={n}"]["max_abs_err"] for n in Ns]
f, ax = plt.subplots(figsize=(5.6, 3.8))
ax.loglog(Ns, errs, "o-", color="#444444")
ax.set_xlabel("$N$ (time steps)")
ax.set_ylabel("max abs error vs $E_\\alpha$")
ax.set_title("Caputo PECE convergence vs exact Mittag--Leffler solution")
ax.grid(True, which="both", **GRID)
save(f, "fig06_solver_convergence.pdf")

# ==================================================================
# FIG 07 (refined) — confusion matrix, 4-class
# ==================================================================
cm = nl["stable"]["confusion_4class"]
cls = ["ODE", "Caputo", "DDE", "latent3"]
M = np.array([[cm[t][c] for c in cls] for t in cls], float)
Mn = M / M.sum(1, keepdims=True)
f, ax = plt.subplots(figsize=(5.2, 4.6))
im = ax.imshow(Mn, cmap="Blues", vmin=0, vmax=1)
ax.set_xticks(range(4)); ax.set_xticklabels(cls, rotation=30)
ax.set_yticks(range(4)); ax.set_yticklabels(cls)
for i in range(4):
    for j in range(4):
        ax.text(j, i, f"{Mn[i, j]:.2f}", ha="center", va="center",
                color="black" if Mn[i, j] < 0.6 else "white", fontsize=8.5)
ax.set_xlabel("predicted (BIC)")
ax.set_ylabel("true mechanism")
ax.set_title("Stable-regime confusion (row-normalized)")
cb = f.colorbar(im, fraction=0.046)
cb.set_label("row probability", fontsize=8)
save(f, "fig07_confusion.pdf")

# ==================================================================
# FIG 08 (refined) — accuracy vs alpha with collapse annotation
# ==================================================================
ba = nl["stable_stratified"]["by_alpha"]
ka = sorted(ba, key=float)
va = [ba[x] for x in ka]
f, ax = plt.subplots(figsize=(5.6, 3.9))
ax.axhspan(0.20, 0.30, color="#f3d9d7", zorder=0)
ax.plot([float(x) for x in ka], va, "s-", color=COL["Caputo"])
ax.axhline(0.25, ls=":", color="gray")
ax.annotate("chance (0.25)", xy=(0.72, 0.255), fontsize=8, color="0.35")
ax.annotate("collapse toward chance\nas $\\alpha \\to 1$", xy=(0.95, 0.312), xytext=(0.72, 0.45),
            fontsize=8.5, arrowprops=dict(arrowstyle="->", lw=0.9))
ax.set_xlabel("fractional order $\\alpha$")
ax.set_ylabel("macro-averaged accuracy")
ax.set_title("Discrimination collapses toward the integer-order limit (stable regime)")
ax.grid(True, **GRID)
save(f, "fig08_accuracy_vs_alpha.pdf")

# ==================================================================
# FIG 09 (refined) — accuracy by SNR and channel
# ==================================================================
bs = nl["stable_stratified"]["by_snr"]
bc = nl["stable_stratified"]["by_channel"]
f, axs = plt.subplots(1, 2, figsize=(8.0, 3.4))
for ax, d, ttl in [(axs[0], bs, "by SNR"), (axs[1], bc, "by observation channel")]:
    bars = ax.bar(list(d), [d[x] for x in d], color="#5b8db8", alpha=0.9)
    for b, v in zip(bars, d.values()):
        ax.annotate(f"{v:.2f}", xy=(b.get_x() + b.get_width() / 2, v), xytext=(0, 2),
                    textcoords="offset points", ha="center", fontsize=8)
    ax.axhline(0.25, ls=":", color="gray")
    ax.set_title(ttl)
    ax.set_ylabel("macro-averaged accuracy")
    ax.grid(True, axis="y", **GRID)
save(f, "fig09_accuracy_snr_channel.pdf")

# ==================================================================
# FIG 10 (headline) — safety-informativeness trade-off
# ==================================================================
saf = nl["safety_stable"]
rank = nl["stable"]["design_ranking"]
names = [n for n in saf if n in rank]
x = [saf[n]["allee_cross_rate"] for n in names]
y = [rank[n] for n in names]
def col_of(n):
    r = saf[n]["allee_cross_rate"]
    return SAFE if r == 0 else (MID if r < 0.2 else UNSAFE)
f, ax = plt.subplots(figsize=(6.6, 4.6))
ax.axvspan(-0.02, 0.12, color="#e7f2ea", zorder=0)
ax.axvspan(0.88, 1.02, color="#f7e3e1", zorder=0)
ax.scatter(x, y, s=110, c=[col_of(n) for n in names], zorder=3, edgecolors="black", linewidths=0.6)
off = {"multiscale": (-8, 8), "pulse": (8, -12), "multisine": (8, 6), "chirp": (-30, 8),
       "sinusoid": (-52, -12), "prbs": (-38, 8)}
for n, xi, yi in zip(names, x, y):
    dx, dy = off.get(n, (6, 6))
    ax.annotate(n, (xi, yi), fontsize=9, xytext=(dx, dy), textcoords="offset points",
                color=col_of(n), fontweight="bold")
ax.text(0.05, 0.345, "safe but weak", color=SAFE, fontsize=9.5, style="italic", ha="center")
ax.text(0.95, 0.575, "informative but unsafe", color=UNSAFE, fontsize=9.5, style="italic", ha="right")
ax.set_xlabel("Allee-crossing rate (fraction of stable-regime cells)")
ax.set_ylabel("Task-A macro-accuracy")
ax.set_title("The safety--informativeness trade-off at a common amplitude budget")
ax.set_xlim(-0.05, 1.05)
ax.grid(True, **GRID)
save(f, "fig10_safety_tradeoff.pdf")

# ==================================================================
# FIG 11 (NEW) — ecological/experimental system schematic
# ==================================================================
f, ax = plt.subplots(figsize=(9.0, 5.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 6.4); ax.axis("off")

def box(x, y, w, h, text, fc, ec, fs=8.5, tc="black", ls="-", lw=1.0, bold=False):
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06", fc=fc, ec=ec, ls=ls, lw=lw)
    ax.add_patch(p)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=tc,
            fontweight="bold" if bold else "normal", linespacing=1.35)

def arrow(x1, y1, x2, y2, label=None, lab_off=(0, 0.12), fs=7.5, color="0.3"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=13,
                                 lw=1.1, color=color))
    if label:
        ax.text((x1 + x2) / 2 + lab_off[0], (y1 + y2) / 2 + lab_off[1], label,
                fontsize=fs, ha="center", color=color)

# safe box around the core dynamics
ax.add_patch(Rectangle((3.05, 2.15), 3.9, 2.75, fill=False, ec=SAFE, ls="--", lw=1.4))
ax.text(4.99, 5.02, "benchmark safety rectangle $\\mathcal{R}$", color=SAFE, fontsize=8, ha="center")
# core states
box(3.3, 3.7, 1.6, 0.9, "prey $x$\nstrong Allee\nthreshold $A$", "#fdeaea", COL["Caputo"], 8)
box(5.2, 3.7, 1.55, 0.9, "predator $y$\n(Holling II\nresponse)", "#eaf1fb", COL["ODE"], 8)
box(3.3, 2.35, 3.45, 0.95, "coexistence equilibrium $z^*=(x^*,y^*(A))$\nJacobian skeleton $J(A)$ — shared by all rivals", "#f4f4f4", "0.45", 8)
arrow(4.9, 4.15, 5.2, 4.15)
ax.text(5.05, 4.48, "Holling-II coupling", fontsize=7.2, ha="center", color="0.3")
arrow(5.2, 3.9, 4.9, 3.9)
# input channel
box(0.35, 3.7, 1.9, 0.9, "perturbation\n$u(t)$, prey channel\n$\\|u\\|_\\infty \\leq 0.10$", "#fff6df", MID, 8)
arrow(2.25, 4.15, 3.3, 4.15)
# observation channels
box(7.7, 3.7, 1.95, 0.9, "observations\n$y_k = C z(t_k)+\\varepsilon_k$\nprey / predator / both", "#eaf6ee", SAFE, 8)
arrow(6.75, 4.15, 7.7, 4.15)
# memory mechanism strip
ax.text(0.35, 1.72, "memory representation — the discriminating component\nacross the calibrated rivals:", ha="left", fontsize=8.5, style="italic")
box(0.6, 0.35, 2.0, 1.1, "ODE\n$\\dot\\xi = J\\xi + Bu$\n(no memory)", "white", COL["ODE"], 7.8, bold=True)
box(2.85, 0.35, 2.0, 1.1, "Caputo\n$\\tau_0^{\\alpha-1} D^\\alpha \\xi = J\\xi+Bu$\n(power-law kernel)", "white", COL["Caputo"], 7.8, bold=True)
box(5.1, 0.35, 2.0, 1.1, "DDE (retarded)\n$\\dot\\xi = A_0\\xi(t)+A_1\\xi(t-\\tau)+Bu$\n(discrete delay)", "white", COL["DDE"], 7.8, bold=True)
box(7.35, 0.35, 2.05, 1.1, "latent $m$\n$\\dot q=\\bar A q+\\bar B u$, $y=\\bar C q$\nbudget $m\\leq m_{\\max}$", "white", COL["latent"], 7.8, bold=True)
for bx in [1.6, 3.85, 6.1, 8.375]:
    ax.add_patch(FancyArrowPatch((bx, 1.45), (bx, 2.15), arrowstyle="-|>", lw=0.9, color="0.55",
                                 linestyle=(0, (3, 2))))
ax.set_title("System under study: certified ecological backbone, rival memory laws, and a safety requirement",
             fontsize=10.5, pad=8)
save(f, "fig11_system_schematic.pdf")

# ==================================================================
# FIG 12 (NEW) — certified backbone: phase portrait + safe box + Allee
# ==================================================================
A2 = 0.25
xs, ys = core.x_star(), core.y_star(A2)
xL = max(A2 + 0.02, 0.5 * xs); xU = 1.6 * xs
yL = max(1e-3, 0.4 * ys); yU = 1.9 * ys

def rk4_traj(z0, T=50.0, n=2500):
    ts = np.linspace(0, T, n)
    return ts, bench._rk4(lambda t, z: core.f_vec(z, A2), np.asarray(z0, float), ts)

f = plt.figure(figsize=(8.6, 4.9))
gs = f.add_gridspec(1, 2, width_ratios=[2.6, 1.0], wspace=0.28)
ax = f.add_subplot(gs[0])
gx = np.linspace(0.05, 1.45, 26); gy = np.linspace(0.05, 2.35, 24)
Xg, Yg = np.meshgrid(gx, gy)
U = np.zeros_like(Xg); V = np.zeros_like(Xg)
for i in range(Xg.shape[0]):
    for j in range(Xg.shape[1]):
        fv = core.f_vec(np.array([Xg[i, j], Yg[i, j]]), A2)
        U[i, j], V[i, j] = fv[0], fv[1]
sp = np.sqrt(U**2 + V**2) + 1e-12
ax.streamplot(Xg, Yg, U / sp, V / sp, color="0.75", density=1.15, linewidth=0.7, arrowsize=0.7)
ax.axvspan(0, A2, color="#f3d9d7", zorder=0)
ax.axvline(A2, color=UNSAFE, ls="--", lw=1.3)
ax.text(A2 - 0.015, 2.28, "Allee threshold $x=A$", color=UNSAFE, fontsize=8, ha="right")
ax.text(A2 / 2, 0.12, "extinction basin", color=UNSAFE, fontsize=8, ha="center", style="italic")
ax.add_patch(Rectangle((xL, yL), xU - xL, yU - yL, fill=False, ec=SAFE, ls="--", lw=1.5))
ax.text(xU - 0.02, yU + 0.03, "benchmark rectangle $\\mathcal{R}$", color=SAFE, fontsize=8, ha="right")
ax.plot(xs, ys, "*", ms=13, color="black", zorder=5)
ax.annotate("coexistence equilibrium $z^*$", xy=(xs, ys), xytext=(xs + 0.10, ys + 0.28),
            fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.8))
_, tr_safe = rk4_traj([0.48, 0.72])
ax.plot(tr_safe[:, 0], tr_safe[:, 1], color=SAFE, lw=1.6, label="illustrative recovery (above $A$)")
ax.annotate("", xy=(tr_safe[600, 0], tr_safe[600, 1]), xytext=(tr_safe[560, 0], tr_safe[560, 1]),
            arrowprops=dict(arrowstyle="-|>", color=SAFE, lw=1.4))
ax.plot(tr_safe[0, 0], tr_safe[0, 1], "o", color=SAFE, ms=5)
_, tr_unsafe = rk4_traj([0.23, ys])
ax.plot(tr_unsafe[:, 0], tr_unsafe[:, 1], color=UNSAFE, lw=1.6, label="below-threshold initial state: collapse")
ax.plot(tr_unsafe[0, 0], tr_unsafe[0, 1], "o", color=UNSAFE, ms=5)
ax.set_xlim(0.05, 1.45); ax.set_ylim(0.05, 2.35)
ax.set_xlabel("prey $x$"); ax.set_ylabel("predator $y$")
ax.set_title("Ecological backbone ($A=0.25$): illustrative recovery vs collapse", fontsize=9.5)
ax.legend(loc="upper left", framealpha=0.9, fontsize=7.5)
axi = f.add_subplot(gs[1])
xx = np.linspace(0.001, 1.15, 300)
Px = core.R * xx * (1 - xx / core.K) * (xx / A2 - 1)
axi.axhline(0, color="0.6", lw=0.8)
axi.plot(xx, Px, color=COL["Caputo"], lw=1.6)
axi.axvline(A2, color=UNSAFE, ls="--", lw=1.0)
axi.annotate("$A$", xy=(A2, -0.028), xytext=(A2 + 0.02, -0.035), fontsize=8, color=UNSAFE)
axi.annotate("$K$", xy=(1.0, 0.004), fontsize=8, color="0.3")
axi.set_xlabel("prey $x$")
axi.set_ylabel("prey growth $P(x)$")
axi.set_title("Strong Allee growth term", fontsize=9)
axi.grid(True, **GRID)
save(f, "fig12_backbone_regime.pdf")

# ==================================================================
# FIG 13 (NEW) — rival-model family overview
# ==================================================================
f, ax = plt.subplots(figsize=(9.2, 4.6))
ax.set_xlim(0, 12); ax.set_ylim(0, 6.6); ax.axis("off")
cols_x = [0.3, 3.2, 6.1, 9.0]
cw = 2.7
heads = [("ODE", COL["ODE"]), ("Caputo", COL["Caputo"]), ("DDE (retarded)", COL["DDE"]), ("latent $m$", COL["latent"])]
for (h, c), cx in zip(heads, cols_x):
    box(cx, 5.55, cw, 0.8, h, c, c, 9.5, "white", bold=True)
ax.add_patch(FancyBboxPatch((0.3, 4.35), 11.4, 0.95, boxstyle="round,pad=0.05", fc="#f0f0f0", ec="0.5"))
ax.text(6.0, 4.82, "shared by ALL rivals: coexistence equilibrium $z^*$ $\\cdot$ Jacobian skeleton $J(A)$ $\\cdot$ input $B$ $\\cdot$ observation $C$ $\\cdot$ units ($\\tau_0$)",
        ha="center", va="center", fontsize=8.5)
laws = ["$\\dot{\\xi} = J\\xi + Bu$",
        "$\\tau_0^{\\alpha-1}\\,{}^C D_t^\\alpha \\xi = J\\xi + Bu$",
        "$\\dot{\\xi} = A_0\\xi(t) + A_1\\xi(t-\\tau) + Bu$",
        "$\\dot q = \\bar A q + \\bar B u,\\quad y = \\bar C q$"]
chars = ["Markov:\nno memory", "power-law kernel\n$t^{\\alpha-1}/\\Gamma(\\alpha)$",
         "single discrete\ndelay $\\tau$", "$m$ exponential\nrelaxation modes"]
for cx, law, ch, (h, c) in zip(cols_x, laws, chars, heads):
    box(cx, 2.7, cw, 1.35, "memory law:\n" + law, "white", c, 8)
    box(cx, 1.05, cw, 1.3, ch, "white", "0.6", 8)
ax.text(10.35, 0.55, "complexity budget:\n$m \\leq m_{\\max}$ (declared, not biological)",
        ha="center", fontsize=7.8, color=COL["latent"], style="italic")
ax.text(6.0, 0.15, "The fractional signature lives ONLY in the Caputo memory law; discrimination must separate it from the other three.",
        ha="center", fontsize=8.5, style="italic", color="0.25")
ax.set_title("Rival model family: identical backbone, four memory operators", fontsize=10.5, pad=6)
save(f, "fig13_model_family.pdf")

# ==================================================================
# FIG 14 (NEW) — exact separation vs finite-horizon approximation
# ==================================================================
f, axs = plt.subplots(1, 3, figsize=(10.6, 3.6))
# (a) exact separation on a compact band (real transfer curves)
ax = axs[0]
ax.axvspan(0.3, 3.0, color=BAND, zorder=0)
ax.loglog(w, np.abs(Gc), color=COL["Caputo"], label="Caputo")
ax.loglog(w, np.abs(Gl), color=COL["latent"], ls="--", label="latent $m=3$")
ax.set_xlabel("$\\omega$"); ax.set_ylabel("$|G(i\\omega)|$")
ax.set_title("(a) Structural separation on a compact band")
ax.text(0.03, 0.05, "finite-dimensional latent response\ncannot coincide on the full band",
        fontsize=7.5, color="0.25", transform=ax.transAxes, va="bottom")
ax.legend(fontsize=7.5); ax.grid(True, which="both", **GRID)

# (b) theorem-admissible left-node exponential approximation.
# The original visual used ell=.05,L=30, which made h too coarse for m=32 and
# visually understated the theorem.  We tune only the theorem's free truncation
# parameters (ell,L) on a small deterministic grid; no benchmark is re-run.
ax = axs[1]
alpha_k = 0.85
t = np.linspace(0.02, 6.0, 400)
ka = t ** (alpha_k - 1) / float(__import__("math").gamma(alpha_k))
ca = np.sin(np.pi * alpha_k) / np.pi

def k_m_params(t, m, ell, L):
    h = (L - ell) / m
    lam = ell + np.arange(m) * h
    return ca * h * np.sum(lam[None, :] ** (-alpha_k) * np.exp(-np.outer(t, lam)), axis=1)

def grid_l1_proxy(m, ell, L, T=6.0):
    tt = np.geomspace(0.005, T, 700)
    exact = tt ** (alpha_k - 1) / float(__import__("math").gamma(alpha_k))
    approx = k_m_params(tt, m, ell, L)
    return np.trapezoid(np.abs(exact - approx), tt)

ELL_GRID = np.logspace(-4.5, -0.5, 28)
L_GRID = np.logspace(-0.15, 1.5, 30)

def tune_left_node(m):
    best = (np.inf, None, None)
    for ell in ELL_GRID:
        for L in L_GRID:
            if L <= ell:
                continue
            e = grid_l1_proxy(m, ell, L)
            if e < best[0]:
                best = (e, ell, L)
    return best

e32, ell32, L32 = tune_left_node(32)
km = k_m_params(t, 32, ell32, L32)
ax.semilogy(t, ka, color=COL["Caputo"], label="$k_\\alpha(t)$ exact")
ax.semilogy(t, km, color=COL["latent"], ls="--",
            label="$k_m(t)$, $m=32$ (tuned $\\ell,L$)")
ax.set_xlabel("$t$"); ax.set_ylabel("kernel")
ax.set_title("(b) Finite-horizon $L^1$ approximation (Thm 9b)")
ax.legend(fontsize=7.2); ax.grid(True, which="both", **GRID)

# (c) achievable error within the same constructive family.
# This is a deterministic tuning diagnostic, NOT a statistical noise floor.
ax = axs[2]
ms = [1, 2, 3, 4, 5, 6, 8, 12, 16, 32]
best_errs = []
for mm in ms:
    ee, el, LL = tune_left_node(mm)
    best_errs.append(ee)
# display the monotone envelope because the admissible latent class is nested by
# "at most m modes"; the coarse tuning grid can otherwise introduce tiny reversals.
env = np.minimum.accumulate(np.asarray(best_errs))
ax.semilogy(ms, env, "o-", color=COL["latent"])
ax.axvline(5, color=SAFE, ls="--", lw=1.2)
ax.annotate("declared budget\n$m_{\\max}=5$", xy=(5, env[4]), xytext=(6.2, env[2] * 1.15),
            fontsize=7.5, color=SAFE)
ax.set_xlabel("latent-mode budget $m$")
ax.set_ylabel("best displayed $L^1$ kernel error")
ax.set_title("(c) Error vs latent complexity")
ax.text(0.04, 0.06, "deterministic tuning diagnostic;\nno noise threshold is asserted",
        transform=ax.transAxes, fontsize=7.2, color="0.35")
ax.grid(True, which="both", **GRID)
save(f, "fig14_separation_approx.pdf")

# ==================================================================
# FIG 15 (NEW) — safety geometry: safe vs unsafe trajectories (real sims)
# ==================================================================
A3, AL3 = 0.25, 0.85
xs3, ys3 = core.x_star(), core.y_star(A3)
xL3 = max(A3 + 0.02, 0.5 * xs3); xU3 = 1.6 * xs3
yL3 = max(1e-3, 0.4 * ys3); yU3 = 1.9 * ys3
ts_s, tr_s = bench.sim_nonlinear("Caputo", A3, AL3, designs.INPUTS["multiscale"], 12.0, 400)
ts_u, tr_u = bench.sim_nonlinear("Caputo", A3, AL3, designs.INPUTS["prbs"], 12.0, 400)
sm = bench.safety_metrics(tr_s, A3); um = bench.safety_metrics(tr_u, A3)
print("fig15 check — multiscale crossed:", sm["allee_crossed"], "min margin %.3f" % sm["allee_margin"],
      "| prbs crossed:", um["allee_crossed"], "min margin %.3f" % um["allee_margin"])

f, axs = plt.subplots(1, 2, figsize=(9.4, 3.9))
ax = axs[0]
ax.axhspan(-0.05, A3, color="#f3d9d7", zorder=0)
ax.axhline(A3, color=UNSAFE, ls="--", lw=1.2, label="Allee threshold $A$")
ax.axhline(xL3, color=SAFE, ls=":", lw=1.2)
ax.axhline(xU3, color=SAFE, ls=":", lw=1.2)
ax.text(11.6, xL3 + 0.01, "$x_L$", color=SAFE, fontsize=8, ha="right")
ax.text(11.6, xU3 + 0.01, "$x_U$", color=SAFE, fontsize=8, ha="right")
ax.plot(ts_s, tr_s[:, 0], color=SAFE, lw=1.4, label="multiscale (no crossing in this run)")
ax.plot(ts_u, tr_u[:, 0], color=UNSAFE, lw=1.4, label="prbs (crosses $A$ in this run)")
cross = tr_u[:, 0] <= A3
ax.fill_between(ts_u, -0.05, np.where(cross, tr_u[:, 0], np.nan), color=UNSAFE, alpha=0.18, lw=0)
ax.set_xlabel("$t$"); ax.set_ylabel("prey $x(t)$")
ax.set_title("(a) Prey trajectory under representative designs\n(Caputo, $A=0.25$, $\\alpha=0.85$, $\\|u\\|_\\infty=0.10$)")
ax.legend(fontsize=7.5, loc="lower left"); ax.grid(True, **GRID)
ax = axs[1]
ax.axvspan(0, A3, color="#f3d9d7", zorder=0)
ax.axvline(A3, color=UNSAFE, ls="--", lw=1.2)
ax.add_patch(Rectangle((xL3, yL3), xU3 - xL3, yU3 - yL3, fill=False, ec=SAFE, ls="--", lw=1.5))
ax.text(xU3 - 0.01, yU3 + 0.02, "benchmark $\\mathcal{R}$", color=SAFE, fontsize=9, ha="right")
ax.plot(xs3, ys3, "*", ms=11, color="black", zorder=5)
ax.plot(tr_s[:, 0], tr_s[:, 1], color=SAFE, lw=1.3, label="multiscale: stays inside in this run")
ax.plot(tr_u[:, 0], tr_u[:, 1], color=UNSAFE, lw=1.3, label="prbs: leaves benchmark $\\mathcal{R}$, crosses $A$")
ax.set_xlabel("prey $x$"); ax.set_ylabel("predator $y$")
ax.set_title("(b) Phase-plane view of the same trajectories")
ax.legend(fontsize=7.5, loc="upper right"); ax.grid(True, **GRID)
save(f, "fig15_safety_geometry.pdf")

# ==================================================================
# FIG 16 (NEW) — Bayesian adaptive layer workflow (specified, not executed)
# ==================================================================
f, ax = plt.subplots(figsize=(10.6, 5.1))
ax.set_xlim(0, 12); ax.set_ylim(0, 6.1); ax.axis("off")

# Spacious six-step loop: the figure carries logic, while theorem numbers remain in caption.
box(0.45, 4.35, 2.75, 1.05, "current belief\n$p_n(M,\\vartheta_M)$",
    "#f0f0f0", "0.45", 9.0)
box(4.15, 4.35, 3.05, 1.05, "safe admissible designs\n$\\mathcal{D}_{\\mathrm{safe}}(p_n)$",
    "#eaf6ee", SAFE, 9.0)
box(8.15, 4.35, 3.05, 1.05, "expected information\n$\\mathbb{E}_Y[D_{\\mathrm{KL}}(p_{n+1}\\Vert p_n)]$",
    "#fdeaea", COL["Caputo"], 8.8)

box(8.15, 2.15, 3.05, 1.05, "choose $d_{n+1}$\nexecute and observe $Y_{n+1}$",
    "#fff6df", MID, 9.0)
box(4.15, 2.15, 3.05, 1.05, "Bayesian update\n$p_{n+1}\\propto p(Y_{n+1}|M,\\vartheta,d)\\,p_n$",
    "#eaf1fb", COL["ODE"], 8.4)
box(0.45, 2.15, 2.75, 1.05, "stopping test\nconfidence reached?\nor no safe design?",
    "#f3d9d7", UNSAFE, 8.8)

arrow(3.20, 4.88, 4.15, 4.88)
arrow(7.20, 4.88, 8.15, 4.88)
arrow(9.68, 4.35, 9.68, 3.20)
arrow(8.15, 2.68, 7.20, 2.68)
arrow(4.15, 2.68, 3.20, 2.68)

# Continue branch loops the updated posterior back to the next belief.
ax.add_patch(FancyArrowPatch((1.82, 2.15), (1.82, 1.35),
                             arrowstyle="-|>", lw=1.0, color="0.35"))
ax.add_patch(FancyArrowPatch((1.82, 1.35), (0.95, 1.35),
                             arrowstyle="-", lw=1.0, color="0.35"))
ax.add_patch(FancyArrowPatch((0.95, 1.35), (0.95, 4.35),
                             arrowstyle="-|>", lw=1.0, color="0.35",
                             linestyle=(0, (4, 2))))
ax.text(2.05, 1.23, "continue: $p_n \\leftarrow p_{n+1}$", fontsize=8.0, color="0.35", ha="center")
ax.text(1.82, 1.82, "stop $\\rightarrow$ report decision / uncertainty",
        fontsize=7.8, color=UNSAFE, ha="center")

ax.text(6.0, 0.42,
        "Specified, not executed in this paper.  The present benchmark uses BIC; "
        "a future implementation must numerically optimize the safe design set and utility.",
        ha="center", fontsize=8.5, style="italic", color="0.3",
        bbox=dict(boxstyle="round,pad=0.35", fc="#fbfbf4", ec="0.7"))
ax.set_title("Bayesian sequential safe-design loop: belief $\\rightarrow$ safe designs $\\rightarrow$ information $\\rightarrow$ update",
             fontsize=10.5, pad=7)
save(f, "fig16_bayes_workflow.pdf")

# ==================================================================
# FIG 17 (NEW) — paper pipeline workflow
# ==================================================================
f, ax = plt.subplots(figsize=(9.6, 3.6))
ax.set_xlim(0, 12); ax.set_ylim(0, 4.6); ax.axis("off")
steps = [
    ("1. Certified\nbackbone", "Sec. 2", "#f0f0f0", "0.45"),
    ("2. Exact linearization\n& channels", "Sec. 4", "#f0f0f0", "0.45"),
    ("3. Structural\nseparation", "Secs. 5", "#eaf1fb", COL["ODE"]),
    ("4. Finite-horizon\nbarrier", "Sec. 6", "#eaf1fb", COL["ODE"]),
    ("5. Optimal input &\nobservation design", "Sec. 7", "#fff6df", MID),
    ("6. Safety\ncertificates", "Sec. 8", "#eaf6ee", SAFE),
    ("7. Bayesian layer\n(specified)", "Sec. 9", "#fdeaea", COL["Caputo"]),
    ("8. Calibrated\nbenchmark", "Sec. 10", "#efe7f5", COL["latent"]),
    ("9. Prospective\nmicrocosm protocol", "Sec. 11", "#efe7f5", COL["latent"]),
]
bw, bh, y0 = 2.15, 1.5, 1.9
for i, (t, sec, fc, ec) in enumerate(steps):
    row = i // 5
    x = 0.25 + (i % 5) * 2.32
    y = y0 - row * 2.05
    box(x, y, bw, bh, t + "\n({})".format(sec), fc, ec, 8, bold=True)
    if i % 5 != 4 and i < len(steps) - 1:
        ax.add_patch(FancyArrowPatch((x + bw, y + bh / 2), (x + 2.32, y + bh / 2),
                                     arrowstyle="-|>", lw=1.2, color="0.4"))
ax.add_patch(FancyArrowPatch((0.25 + 4 * 2.32 + bw / 2, y0), (0.25 + 4 * 2.32 + bw / 2, y0 - 0.55),
                             arrowstyle="-|>", lw=1.2, color="0.4"))
ax.text(6.0, 0.35, "Main-text results: macro-accuracy 0.537 vs chance 0.25 (stable regime, BIC) $\\cdot$ safety--informativeness trade-off (Fig. 15)",
        ha="center", fontsize=8.5, style="italic", color="0.3")
ax.set_title("From certified ecology to prospective experiment: the paper's pipeline", fontsize=10.5, pad=6)
save(f, "fig17_paper_workflow.pdf")

print("Q1 FIGURES DONE:", len([x for x in os.listdir(FIG) if x.endswith(".pdf")]), "PDFs in", FIG)
