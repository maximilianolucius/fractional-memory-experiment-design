import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIG = os.path.join(ROOT, 'figures')
os.makedirs(FIG, exist_ok=True)

# Harmonized with the existing Q1 figure family.
ODE = '#3b73b9'
CAPUTO = '#cf4338'
DDE = '#2a8c55'
LATENT = '#7e67ad'
MID = '#d98711'
SAFE = '#238b57'


def save(fig, name):
    fig.savefig(os.path.join(FIG, name), bbox_inches='tight', pad_inches=0.03)
    plt.close(fig)


def add_box(ax, x, y, w, h, text, fc, ec, fs=8.0, bold=False, linespacing=1.22):
    p = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.055',
                       fc=fc, ec=ec, lw=1.0)
    ax.add_patch(p)
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=fs,
            fontweight='bold' if bold else 'normal', linespacing=linespacing)


def add_arrow(ax, x1, y1, x2, y2, color='0.35', lw=1.1, ms=12):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2), arrowstyle='-|>',
                                 mutation_scale=ms, lw=lw, color=color))

# ------------------------------------------------------------------
# Figure 1: paper pipeline. Fix the previous bottom-row/footer overlap,
# simplify box wording, and preserve the 5+4 structure.
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9.6, 4.05))
ax.set_xlim(0, 12); ax.set_ylim(0, 5.0); ax.axis('off')
steps = [
    ('1. Certified\necology', 'Sec. 2', '#f0f0f0', '0.45'),
    ('2. Linearization\n& channels', 'Sec. 4', '#f0f0f0', '0.45'),
    ('3. Structural\nseparation', 'Sec. 5', '#eaf1fb', ODE),
    ('4. Finite-horizon\nbarrier', 'Sec. 6', '#eaf1fb', ODE),
    ('5. Optimal\ndesign', 'Sec. 7', '#fff6df', MID),
    ('6. Safety\nconstraints', 'Sec. 8', '#eaf6ee', SAFE),
    ('7. Bayesian layer\n(specified)', 'Sec. 9', '#fdeaea', CAPUTO),
    ('8. Calibrated\nbenchmark', 'Sec. 10', '#efe7f5', LATENT),
    ('9. Prospective\nmicrocosm', 'Sec. 11', '#efe7f5', LATENT),
]
bw, bh = 2.15, 1.28
y_top, y_bottom = 2.85, 0.75
positions=[]
for i, (title, sec, fc, ec) in enumerate(steps):
    row = 0 if i < 5 else 1
    col = i if i < 5 else i-5
    x = 0.25 + col*2.32
    y = y_top if row == 0 else y_bottom
    add_box(ax, x, y, bw, bh, title + '\n(' + sec + ')', fc, ec, fs=7.9, bold=True, linespacing=1.16)
    positions.append((x,y))
    if row == 0 and i < 4:
        add_arrow(ax, x+bw, y+bh/2, x+2.32, y+bh/2)
    if row == 1 and i < 8:
        add_arrow(ax, x+bw, y+bh/2, x+2.32, y+bh/2)
# transition from step 5 to step 6: a clear down-and-back cue without crossing text
x5,y5=positions[4]; x6,y6=positions[5]
ax.plot([x5+bw/2, x5+bw/2], [y5, 2.36], color='0.4', lw=1.1)
ax.plot([x5+bw/2, x6+bw/2], [2.36, 2.36], color='0.4', lw=1.1)
add_arrow(ax, x6+bw/2, 2.36, x6+bw/2, y6+bh, color='0.4')
ax.text(6.0, 0.24,
        'Theory → constrained design → benchmark → prospective validation',
        ha='center', fontsize=8.6, style='italic', color='0.35')
ax.set_title('Paper pipeline: from certified ecology to prospective experiment', fontsize=11.0, pad=5)
save(fig, 'fig17_paper_workflow.pdf')

# ------------------------------------------------------------------
# Figure 2: system schematic. Correct the stale Jacobian claim, rename
# the rectangle as diagnostic (not certified safe), and rebalance text.
# ------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9.0, 5.25))
ax.set_xlim(0,10); ax.set_ylim(0,6.45); ax.axis('off')

# benchmark diagnostic rectangle around core dynamics
ax.add_patch(Rectangle((3.02, 2.18), 3.93, 2.73, fill=False, ec=SAFE, ls='--', lw=1.35))
ax.text(4.99, 5.04, 'benchmark diagnostic rectangle $\\mathcal{R}$',
        color=SAFE, fontsize=9.0, ha='center')

add_box(ax, 3.26, 3.72, 1.68, 0.90,
        'prey $x$\nstrong Allee\nthreshold $A$', '#fdeaea', CAPUTO, fs=9.0)
add_box(ax, 5.18, 3.72, 1.62, 0.90,
        'predator $y$\nHolling II\nresponse', '#eaf1fb', ODE, fs=9.0)
add_arrow(ax, 4.94, 4.18, 5.18, 4.18)
add_arrow(ax, 5.18, 3.93, 4.94, 3.93)
ax.text(5.06, 4.64, 'Holling-II coupling', fontsize=8.0, ha='center', color='0.35')

# Accurate operating-point statement: only ODE and Caputo share J(A).
add_box(ax, 3.26, 2.39, 3.54, 0.92,
        'common operating point $z^*=(x^*,y^*(A))$\n'
        'ODE + Caputo: shared $J(A)$\nDDE + latent: calibrated response laws',
        '#f4f4f4', '0.45', fs=8.6)

add_box(ax, 0.33, 3.72, 1.92, 0.90,
        'perturbation\n$u(t)$ on prey channel\n$\\|u\\|_\\infty\\leq0.10$',
        '#fff6df', MID, fs=8.8)
add_arrow(ax, 2.25, 4.18, 3.26, 4.18)

add_box(ax, 7.72, 3.72, 1.95, 0.90,
        'observations\n$y_k=Cz(t_k)+\\varepsilon_k$\nprey / predator / both',
        '#eaf6ee', SAFE, fs=8.6)
add_arrow(ax, 6.80, 4.18, 7.72, 4.18)

ax.text(0.38, 1.77,
        'memory law = discriminating component across calibrated rivals',
        ha='left', fontsize=8.8, style='italic')

add_box(ax, 0.58, 0.34, 2.03, 1.10,
        'ODE\n$\\dot\\xi=J\\xi+Bu$\n(no memory)', 'white', ODE, fs=8.5, bold=True)
add_box(ax, 2.84, 0.34, 2.03, 1.10,
        'Caputo\n$\\tau_0^{\\alpha-1}D^\\alpha\\xi=J\\xi+Bu$\n(power-law memory)',
        'white', CAPUTO, fs=8.15, bold=True)
add_box(ax, 5.10, 0.34, 2.03, 1.10,
        'DDE (retarded)\n$\\dot\\xi=A_0\\xi(t)+A_1\\xi(t-\\tau)+Bu$\n(discrete delay)',
        'white', DDE, fs=7.9, bold=True)
add_box(ax, 7.36, 0.34, 2.07, 1.10,
        'latent $m$\n$\\dot q=\\bar A q+\\bar Bu$, $y=\\bar Cq$\n$m\\leq m_{\\max}$',
        'white', LATENT, fs=8.15, bold=True)
for bx in [1.595, 3.855, 6.115, 8.395]:
    ax.add_patch(FancyArrowPatch((bx,1.44),(bx,2.18),arrowstyle='-|>',lw=0.85,
                                 color='0.55',linestyle=(0,(3,2)),mutation_scale=9))

ax.set_title('System, observation channels, and rival memory laws', fontsize=11.0, pad=6)
save(fig, 'fig11_system_schematic.pdf')

print('Regenerated manuscript Figures 1 and 2.')
