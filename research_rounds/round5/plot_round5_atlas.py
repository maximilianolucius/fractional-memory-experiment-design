#!/usr/bin/env python3
"""plot_round5_atlas.py — the Safe Memory-Discrimination Atlas figure.

Headline atlas figure (3 panels), theorem-valid quantities only:
 (a) P_e lower bound on the (A, m) plane at alpha=0.85, sigma=0.10;
 (b) P_e lower bound on the (alpha, m) plane at A=0.30, sigma=0.10;
 (c) budget frontier at alpha=0.85, m=16: B_eff(A) with shape-cap, universal
     and hierarchy-uniform Allee budgets; the binding switch is the
     certified crossover.
Classification regions: hard@0.25 (P_e>=0.25), moderate@0.10, inconclusive.
"""
import json
import math
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(os.path.dirname(HERE)), 'paper', 'figures')

plt.rcParams.update({'font.size': 8, 'axes.titlesize': 9, 'axes.labelsize': 8,
                     'xtick.labelsize': 7, 'ytick.labelsize': 7,
                     'legend.fontsize': 6.5})

def grid(cells, xkey, ykey, val, xlist, ylist):
    G = np.full((len(ylist), len(xlist)), np.nan)
    for c in cells:
        if c[xkey] in xlist and c[ykey] in ylist:
            G[ylist.index(c[ykey]), xlist.index(c[xkey])] = c[val]
    return G

def main():
    D = json.load(open(os.path.join(HERE, 'atlas_cells.json')))
    cells = D['cells']
    A_list = D['A_grid']; alphas = D['alpha_grid']
    m_list = D['m_grid']; sigmas = D['sigma_grid']
    sig = 0.10
    fig, axes = plt.subplots(1, 3, figsize=(9.6, 2.9))
    # ---- (a) (A, m) at alpha=0.85, sigma=0.10
    sub = [c for c in cells if c['alpha'] == 0.85 and c['sigma'] == sig]
    G = grid(sub, 'A', 'm', 'Pe_gauss', A_list, m_list)
    ax = axes[0]
    im = ax.imshow(G, origin='lower', aspect='auto', vmin=0.0, vmax=0.5,
                   extent=[A_list[0] - 0.02, A_list[-1] + 0.02, -0.5, len(m_list) - 0.5],
                   cmap='RdYlGn_r', interpolation='nearest')
    ax.set_yticks(range(len(m_list))); ax.set_yticklabels(m_list)
    ax.set_xlabel(r'Allee threshold $A$'); ax.set_ylabel(r'latent budget $m$')
    ax.set_title(r'(a) $P_e^*$ lower bound, $\alpha=0.85$, $\sigma=0.10$')
    ax.axhline(-0.5, color='none')
    # ---- (b) (alpha, m) at A=0.30, sigma=0.10
    sub = [c for c in cells if c['A'] == 0.30 and c['sigma'] == sig]
    G2 = grid(sub, 'alpha', 'm', 'Pe_gauss', alphas, m_list)
    ax = axes[1]
    im2 = ax.imshow(G2, origin='lower', aspect='auto', vmin=0.0, vmax=0.5,
                    extent=[alphas[0] - 0.03, alphas[-1] + 0.03, -0.5, len(m_list) - 0.5],
                    cmap='RdYlGn_r', interpolation='nearest')
    ax.set_yticks(range(len(m_list))); ax.set_yticklabels(m_list)
    ax.set_xlabel(r'memory order $\alpha$'); ax.set_ylabel(r'latent budget $m$')
    ax.set_title(r'(b) $P_e^*$ lower bound, $A=0.30$, $\sigma=0.10$')
    cb = fig.colorbar(im2, ax=axes[:2], fraction=0.040, pad=0.06, shrink=0.85)
    cb.set_label(r'$P_e^*$ lower bound', size=7)
    # ---- (c) budget frontier at alpha=0.85, m=16
    ax = axes[2]
    m = 16
    sub = [c for c in cells if c['alpha'] == 0.85 and c['m'] == m and c['sigma'] == sig]
    sub.sort(key=lambda c: c['A'])
    As = [c['A'] for c in sub]
    ax.semilogy(As, [c['B_cap'] for c in sub], 'k--', lw=1.2, label='shape cap (actuator)')
    ax.semilogy(As, [c['B_univ'] for c in sub], 'k:', lw=1.2, label=r'universal $\sqrt{T}u_{\max}$')
    ax.semilogy(As, [c['B_Allee'] for c in sub], 'b-', lw=1.6,
                label=r'hierarchy-uniform Allee $\rho_\eta/d_{\rm rob}(K_m)$')
    ax.semilogy(As, [c['B_eff'] for c in sub], 'r-', lw=2.2, label=r'active budget $B_{\rm eff}$')
    ax.set_xlabel(r'Allee threshold $A$')
    ax.set_ylabel(r'safe energy budget $B_{\rm eff}$')
    ax.set_title(rf'(c) certified budget frontier, $m={m}$')
    ax.legend(loc='upper right', framealpha=0.9, bbox_to_anchor=(1.0, 1.02))
    ax.grid(True, which='both', ls=':', lw=0.4)
    fig.savefig(os.path.join(OUT, 'fig18_safe_discrimination_atlas.pdf'),
                bbox_inches='tight')
    fig.savefig(os.path.join(OUT, 'fig18_safe_discrimination_atlas.png'),
                dpi=150, bbox_inches='tight')
    print('wrote fig18_safe_discrimination_atlas.pdf/.png')

if __name__ == '__main__':
    main()
