#!/usr/bin/env python3
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=os.path.join(ROOT,'figures','fig13_model_family.pdf')
COL={'ODE':'#4477BB','Caputo':'#CC443D','DDE':'#449966','latent':'#8069AA'}
def box(ax,x,y,w,h,text,fc,ec,fs=8,tc='black',bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.035',fc=fc,ec=ec,lw=1.1))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,color=tc,fontweight='bold' if bold else 'normal')
f,ax=plt.subplots(figsize=(9.2,4.6)); ax.set_xlim(0,12); ax.set_ylim(0,6.6); ax.axis('off')
xs=[.3,3.2,6.1,9.0]; cw=2.7
heads=[('ODE',COL['ODE']),('Caputo',COL['Caputo']),('DDE (retarded)',COL['DDE']),('latent $m$',COL['latent'])]
for (h,c),x in zip(heads,xs): box(ax,x,5.55,cw,.8,h,c,c,9.5,'white',True)
ax.add_patch(FancyBboxPatch((.3,4.35),11.4,.95,boxstyle='round,pad=.05',fc='#f0f0f0',ec='0.5'))
ax.text(6,4.82,'common experimental reference: coexistence operating point  ·  input/observation channels  ·  physical units',ha='center',va='center',fontsize=8.5)
laws=[r'$\dot{\xi}=J\xi+Bu$',r'$\tau_0^{\alpha-1}\,{}^C D_t^\alpha\xi=J\xi+Bu$',r'$\dot{\xi}=A_0\xi(t)+A_1\xi(t-\tau)+Bu$',r'$\dot q=\bar A q+\bar B u,\quad y=\bar Cq$']
chars=['Markov:\nno memory','power-law memory\nCaputo operator','single discrete\ndelay $\tau$','finite-state latent\nresponse, dim $\leq m$']
for x,law,ch,(h,c) in zip(xs,laws,chars,heads):
    box(ax,x,2.7,cw,1.35,'dynamics:\n'+law,'white',c,8)
    box(ax,x,1.05,cw,1.3,ch,'white','0.6',8)
ax.text(10.35,.55,'complexity budget:\n$m\leq m_{\max}$ (declared, not biological)',ha='center',fontsize=7.8,color=COL['latent'],style='italic')
ax.text(6,.15,'ODE/Caputo share the ecological Jacobian $J$; DDE and latent rivals are calibrated alternative response laws, not identical Jacobian copies.',ha='center',fontsize=8.2,style='italic',color='.25')
ax.set_title('Rival model family: common operating point and channels, different dynamic laws',fontsize=10.5,pad=6)
f.tight_layout(); f.savefig(OUT,bbox_inches='tight'); print('wrote',OUT)
