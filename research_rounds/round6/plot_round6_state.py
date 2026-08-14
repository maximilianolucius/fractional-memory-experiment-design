#!/usr/bin/env python3
"""plot_round6_state.py — fig19: certified full ecological-state theorem.

Three panels (alpha=0.85, pulse ray, Matignon-stable focal cells only):
 (a) certified E^state_m vs m (solid) against kernel-level E^IA_m (dashed);
 (b) certified Pinsker lower bound on the state-level testing error at
     sigma=0.10 under B_eff = min(B_Allee^state, shape cap, universal cap);
 (c) interval-certified B_Allee^state(A,m) sandwich vs A, with caps.

Data: round6_results*.json (interval-certified quantities only).
"""
import glob
import json
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPDF = os.path.join(HERE, '..', '..', 'paper', 'figures', 'fig19_state_theorem.pdf')
OUTPNG = os.path.join(HERE, 'fig19_state_theorem.png')

# chief-repaired kernel-level interval enclosures (R4/R5, alpha=0.85)
KERNEL_E = {4: 0.352, 8: 0.248, 16: 0.200, 32: 0.134}
MS = [4, 8, 16, 32]

cells = {}
for fp in sorted(glob.glob(os.path.join(HERE, 'round6_results*.json'))):
    res = json.load(open(fp))
    for Akey, cell in res['cells'].items():
        cells[float(Akey.split('=')[1])] = cell

A_sorted = sorted(cells)
cmap = plt.get_cmap('viridis')
colors = {A: cmap(i/(len(A_sorted) - 1 + 1e-9)) for i, A in enumerate(A_sorted)}

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2))

# (a) E^state vs m
ax = axes[0]
for A in A_sorted:
    E = [cells[A]['budgets'][f'm={m}']['E_upper'] for m in MS]
    ax.plot(MS, E, 'o-', color=colors[A], label=f'$A={A:.2f}$')
ax.plot(MS, [KERNEL_E[m] for m in MS], 'k--', lw=2, label='kernel level $\\widehat E_m^{\\rm IA}$')
ax.set_xscale('log', base=2)
ax.set_yscale('log')
ax.set_xticks(MS)
ax.set_xticklabels([str(m) for m in MS])
ax.set_xlabel('latent state budget $m$')
ax.set_ylabel('certified $L^1(0,T)$ enclosure')
ax.set_title('(a) State-level approximation error\n(interval-certified upper enclosures)')
ax.legend(fontsize=7, ncol=2)
ax.grid(alpha=0.3)

# (b) Pe lower bound vs m at sigma=0.10
ax = axes[1]
for A in A_sorted:
    pe = [cells[A]['budgets'][f'm={m}']['testing']['0.10']['Pe_pinsker'] for m in MS]
    ax.plot(MS, pe, 'o-', color=colors[A], label=f'$A={A:.2f}$')
ax.axhline(0.25, color='crimson', ls=':', lw=1.5)
ax.text(4.1, 0.255, 'hard threshold 0.25', color='crimson', fontsize=8)
ax.set_xscale('log', base=2)
ax.set_xticks(MS)
ax.set_xticklabels([str(m) for m in MS])
ax.set_ylim(0, 0.52)
ax.set_xlabel('latent state budget $m$')
ax.set_ylabel('certified $P_e$ lower bound (Pinsker)')
ax.set_title('(b) State-level testing bound\n($\\sigma=0.10$, pulse ray, $B_{\\rm eff}$)')
ax.grid(alpha=0.3)

# (c) B_Allee^state vs A
ax = axes[2]
for m in MS:
    B = [cells[A]['budgets'][f'm={m}']['allee']['B_Allee_state'] for A in A_sorted]
    ax.plot(A_sorted, B, 'o-', label=f'$m={m}$', alpha=0.8)
ax.axhline(0.120, color='gray', ls='--', lw=1.2)
ax.text(A_sorted[0], 0.123, 'pulse shape cap 0.120', color='gray', fontsize=8)
ax.axhline(0.346, color='gray', ls='-.', lw=1.2)
ax.text(A_sorted[0], 0.35, 'universal cap 0.346', color='gray', fontsize=8)
ax.set_xlabel('Allee threshold $A$')
ax.set_ylabel('$B_{\\rm Allee}^{\\rm state}(A,m)$')
ax.set_title('(c) Certified state-level Allee budget\n(closed-form interval sandwich)')
ax.legend(fontsize=8)
ax.grid(alpha=0.3)

fig.suptitle('Certified full ecological-state theorem — pulse ray, Matignon-stable cells, '
             '$\\alpha=0.85$ (all values are outward-rounded interval enclosures)',
             fontsize=10, y=1.02)
fig.tight_layout()
fig.savefig(OUTPDF, bbox_inches='tight')
fig.savefig(OUTPNG, dpi=150, bbox_inches='tight')
print('wrote', OUTPDF, 'and', OUTPNG)
