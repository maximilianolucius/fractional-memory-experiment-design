#!/usr/bin/env python3
import os,json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=os.path.dirname(os.path.abspath(__file__))
r=json.load(open(os.path.join(HERE,'round3_results.json')))
c=json.load(open(os.path.join(HERE,'chief_round3_checks.json')))
fig,axs=plt.subplots(1,3,figsize=(13.6,4.1))
# (a) candidate approximation upper errors, not the exact infimum E_m
ax=axs[0]; cells=r['track_A']['cells']; mm=np.array([x['m'] for x in cells])
rep=np.array([x['reported_grid_error'] for x in c['l1_independent_check']])
ad=np.array([x['adaptive_error'] for x in c['l1_independent_check']])
env=np.minimum.accumulate(rep)
ax.semilogy(mm,env,'o-',label=r'constructive candidate envelope $\bar E_m$')
ax.semilogy(mm,ad,'x',label='independent adaptive quadrature')
ax.semilogy(mm,[x['T9b_bound_at_tuned'] for x in cells],'s--',label='T9b analytic upper bound')
ax.set_xlabel('latent modes $m$'); ax.set_ylabel('$L^1(0,T)$ kernel error')
ax.set_title('(a) Constructive approximation bounds (not exact $E_m$)'); ax.grid(alpha=.3,which='both'); ax.legend(fontsize=7)
# (b) HF diagnostic
ax=axs[1]; hf=r['track_B']['hf_null']; eps=np.array([x['eps'] for x in hf]); sx=np.array([x['sup_x_unit_energy'] for x in hf])
ax.loglog(eps,sx,'D-'); ax.set_xlabel(r'oscillation scale $\varepsilon$ (unit $\|u\|_2$)'); ax.set_ylabel(r'$\sup_t|H_xu_\varepsilon(t)|$')
ax.set_title('(b) High-frequency attenuation: numerical check'); ax.grid(alpha=.3,which='both')
ax.text(.05,.9,'supports the null-direction theorem;\nrate is diagnostic, not used in proof',transform=ax.transAxes,va='top',fontsize=7.5)
# (c) corrected one-sided positive-ray bounds + shape-specific actuator caps
ax=axs[2]
for fam,marker in [('pulse','o'),('multiscale','s')]:
    rows=[x for x in c['one_sided_transient_bounds_benchmark_rivals'] if x['family']==fam]
    A=[x['A'] for x in rows]; B=[x['positive_ray_allee_outer_sampled'] for x in rows]; cap=[x['shape_specific_actuator_energy_cap'] for x in rows]
    line=ax.plot(A,B,marker+'-',label=f'Allee outer, {fam}')[0]
    ax.plot(A,cap,'--',color=line.get_color(),alpha=.8,label=f'peak-cap energy, {fam}')
ax.set_xlabel('Allee threshold $A$'); ax.set_ylabel(r'upper bound on $\|u\|_2$')
ax.set_title('(c) Positive transient rays: benchmark-rival diagnostic'); ax.grid(alpha=.3); ax.legend(fontsize=6.8)
fig.tight_layout(); fig.savefig(os.path.join(HERE,'round3_diagnostic_CHIEF_CORRECTED.pdf'))
fig.savefig(os.path.join(HERE,'round3_diagnostic_CHIEF_CORRECTED.png'),dpi=180)
print('wrote corrected diagnostic')
