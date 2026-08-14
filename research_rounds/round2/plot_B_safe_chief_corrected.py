import json, os
import numpy as np
import matplotlib.pyplot as plt

HERE=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(os.path.join(HERE,'B_safe_grid.json')))
u_cap=d['u_cap']
cells=d['cells']
As=sorted({c['A'] for c in cells})
fig,axs=plt.subplots(1,2,figsize=(11.4,4.8),constrained_layout=True)
for A in As:
    rows=sorted([c for c in cells if c['A']==A], key=lambda c:c['alpha'])
    al=np.array([c['alpha'] for c in rows])
    uc=np.array([c['u_safe'] for c in rows])
    axs[0].plot(al,uc,marker='o',label=fr'$A={A}$')
    frac=np.minimum(1.0,uc/u_cap)**2
    axs[1].plot(al,frac,marker='s',label=fr'$A={A}$')
axs[0].axhline(u_cap,ls='--',lw=1.2,label=fr'generic cap $u_{{\max}}={u_cap:.2f}$')
axs[0].set_xlabel(r'fractional order $\alpha$')
axs[0].set_ylabel(r'sufficient certified amplitude $u_{\rm cert}=\rho/\Gamma_T$')
axs[0].set_title('(a) Sufficient Strong-Allee amplitude certificate')
axs[0].legend(fontsize=9)
axs[0].grid(alpha=.25)
axs[1].axhline(1.0,ls='--',lw=1.0)
axs[1].set_xlabel(r'fractional order $\alpha$')
axs[1].set_ylabel(r'$[\min(1,u_{\rm cert}/u_{\max})]^2$')
axs[1].set_ylim(0,1.06)
axs[1].set_title('(b) Certified-ball fraction of generic energy cap')
axs[1].legend(fontsize=9)
axs[1].grid(alpha=.25)
fig.suptitle('Round 2 diagnostic only — this is an inner safe-ball certificate, not an upper bound on all safe inputs',fontsize=11)
fig.savefig(os.path.join(HERE,'B_safe_vs_alpha_CHIEF_CORRECTED.pdf'),bbox_inches='tight')
fig.savefig(os.path.join(HERE,'B_safe_vs_alpha_CHIEF_CORRECTED.png'),dpi=180,bbox_inches='tight')
