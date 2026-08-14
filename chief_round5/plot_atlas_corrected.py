#!/usr/bin/env python3
import json, os, numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,'research_rounds','round5','atlas_cells_CHIEF_CORRECTED.json')
D=json.load(open(P)); C=D['cells']; As=D['A_grid']; alphas=D['alpha_grid']; ms=D['m_grid']; sig=.10
fig,axes=plt.subplots(1,3,figsize=(11.4,3.35),constrained_layout=True)

def mat(sub,xs,ys,xkey,ykey):
    G=np.full((len(ys),len(xs)),np.nan); S=np.ones_like(G,dtype=bool)
    for c in sub:
        i=ys.index(c[ykey]); j=xs.index(c[xkey]); G[i,j]=c['Pe_gauss_grid']; S[i,j]=c['focal_matignon_stable']
    return G,S
# panel a
sub=[c for c in C if c['alpha']==.85 and c['sigma']==sig]
G,S=mat(sub,As,ms,'A','m'); Gm=np.ma.array(G,mask=~S)
im=axes[0].imshow(Gm,origin='lower',aspect='auto',vmin=0,vmax=.5,cmap='RdYlGn_r')
axes[0].set_xticks(range(len(As))); axes[0].set_xticklabels([f'{a:.2f}' for a in As],rotation=45,ha='right')
axes[0].set_yticks(range(len(ms))); axes[0].set_yticklabels(ms)
axes[0].set_xlabel('Allee threshold $A$'); axes[0].set_ylabel('latent budget $m$')
axes[0].set_title('(a) Pulse-ray error lower bound\n$\\alpha=0.85$, $\\sigma=0.10$')
for i in range(len(ms)):
 for j in range(len(As)):
  if not S[i,j]:
   axes[0].add_patch(Rectangle((j-.5,i-.5),1,1,facecolor='0.88',edgecolor='0.55',hatch='///',lw=.4))
# panel b
sub=[c for c in C if c['A']==.30 and c['sigma']==sig]
G2,S2=mat(sub,alphas,ms,'alpha','m')
im2=axes[1].imshow(G2,origin='lower',aspect='auto',vmin=0,vmax=.5,cmap='RdYlGn_r')
axes[1].set_xticks(range(len(alphas))); axes[1].set_xticklabels([f'{a:.2f}' for a in alphas])
axes[1].set_yticks(range(len(ms))); axes[1].set_yticklabels(ms)
axes[1].set_xlabel('memory order $\\alpha$'); axes[1].set_ylabel('latent budget $m$')
axes[1].set_title('(b) Pulse-ray error lower bound\n$A=0.30$, $\\sigma=0.10$')
cb=fig.colorbar(im2,ax=axes[:2],shrink=.78,pad=.02); cb.set_label('$P_e$ lower bound')
# panel c
sub=[c for c in C if c['alpha']==.85 and c['m']==16 and c['sigma']==sig]; sub.sort(key=lambda x:x['A'])
x=[c['A'] for c in sub]
axes[2].semilogy(x,[c['B_cap'] for c in sub],'--',lw=1.3,label='pulse peak-cap budget')
axes[2].semilogy(x,[c['B_univ'] for c in sub],':',lw=1.3,label='universal peak-cap budget')
axes[2].semilogy(x,[c['B_Allee_grid'] for c in sub],'-',lw=1.6,label='Allee outer budget (grid estimate)')
axes[2].semilogy(x,[c['B_eff_grid'] for c in sub],'-',lw=2.2,label='active pulse-ray budget')
axes[2].set_xlabel('Allee threshold $A$'); axes[2].set_ylabel('$L^2$ input budget')
axes[2].set_title('(c) Pulse-ray budget frontier\n$\\alpha=0.85$, $m=16$')
axes[2].grid(True,which='both',ls=':',lw=.45); axes[2].legend(fontsize=7,loc='upper right')
fig.text(.5,-.02,'Hatched cells lie outside the focal Caputo Matignon-stable regime. The gain maximization is numerically validated, not interval-certified.',ha='center',fontsize=8)
out=os.path.join(ROOT,'figures','fig18_safe_discrimination_atlas.pdf'); fig.savefig(out,bbox_inches='tight')
fig.savefig(os.path.join(ROOT,'figures','fig18_safe_discrimination_atlas.png'),dpi=170,bbox_inches='tight')
print(out)
