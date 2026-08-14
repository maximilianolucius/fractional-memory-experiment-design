#!/usr/bin/env python3
import glob, json, math, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R6=os.path.join(ROOT,'research_rounds','round6')
OUT=os.path.join(ROOT,'figures','fig19_state_theorem.pdf')
OUTPNG=os.path.join(ROOT,'chief_round6','fig19_state_theorem_CHIEF_CORRECTED.png')
MS=[4,8,16,32]
KERNEL_E={4:0.352,8:0.248,16:0.200,32:0.134}
SIGMA=0.10
B_SHAPE=0.120
cells={}
for fp in sorted(glob.glob(os.path.join(R6,'round6_results*.json'))):
    d=json.load(open(fp))
    for ak,c in d['cells'].items():
        cells[float(ak.split('=')[1])]=c
A_sorted=sorted(cells)
cmap=plt.get_cmap('viridis')
colors={A:cmap(i/max(1,len(A_sorted)-1)) for i,A in enumerate(A_sorted)}

def pinsker(E):
    U=(E*B_SHAPE)**2/(2*SIGMA**2)
    return max(0.0,(1-math.sqrt(U/2))/2)

fig,axes=plt.subplots(1,2,figsize=(10.8,4.25))
ax=axes[0]
for A in A_sorted:
    E=[cells[A]['budgets'][f'm={m}']['E_upper'] for m in MS]
    ax.plot(MS,E,'o-',label=fr'$A={A:.2f}$',color=colors[A])
ax.plot(MS,[KERNEL_E[m] for m in MS],'k--',lw=2,label=r'kernel-level $\widehat E_m^{\rm IA}$')
ax.set_xscale('log',base=2); ax.set_yscale('log')
ax.set_xticks(MS); ax.set_xticklabels([str(m) for m in MS])
ax.set_xlabel(r'finite-state budget $m$')
ax.set_ylabel(r'certified $L^1(0,T)$ upper enclosure')
ax.set_title('(a) Exact prey-channel response approximation')
ax.grid(alpha=.3); ax.legend(fontsize=7,ncol=2)

ax=axes[1]
for A in A_sorted:
    vals=[]
    for m in MS:
        E=cells[A]['budgets'][f'm={m}']['E_upper']
        vals.append(pinsker(E))
    ax.plot(MS,vals,'o-',label=fr'$A={A:.2f}$',color=colors[A])
ax.axhline(.25,ls=':',lw=1.5,color='crimson')
ax.text(4.05,.257,'declared 0.25 hardness threshold',fontsize=8,color='crimson')
ax.set_xscale('log',base=2); ax.set_xticks(MS); ax.set_xticklabels([str(m) for m in MS])
ax.set_ylim(0,.515)
ax.set_xlabel(r'finite-state budget $m$')
ax.set_ylabel(r'$P_e$ lower bound (Pinsker)')
ax.set_title(r'(b) Testing obstruction under pulse peak cap ($B=0.120$, $\sigma=0.10$)')
ax.grid(alpha=.3)

fig.suptitle(r'Certified prey-response finite-state approximation and testing bound ($\alpha=0.85$, $T=12$)',fontsize=11,y=1.01)
fig.tight_layout()
fig.savefig(OUT,bbox_inches='tight')
fig.savefig(OUTPNG,dpi=180,bbox_inches='tight')
print('wrote',OUT)
