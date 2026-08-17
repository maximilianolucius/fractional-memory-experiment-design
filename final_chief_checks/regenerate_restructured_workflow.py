from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT=Path(__file__).resolve().parents[1]/'figures'/'fig17_paper_workflow.pdf'
fig,ax=plt.subplots(figsize=(10.6,4.1))
ax.set_xlim(0,12.4); ax.set_ylim(0,5.0); ax.axis('off')
steps=[
('1. Ecological model\n& memory rivals','Sec. 2','#f1f1f1','#666666'),
('2. Four core\nanalytical results','Sec. 3','#e9f1fb','#3d73b9'),
('3. Numerical methods\n& validation','Sec. 4','#edf7ee','#33885c'),
('4. Frequency / finite-\nhorizon evidence','Sec. 5','#eef2fb','#3d73b9'),
('5. Fractional-delay\nsimulations','Sec. 6','#fff1e6','#d17a24'),
('6. Experiment design\n& safety','Sec. 7','#fff7df','#c38b1c'),
('7. Large-scale\nbenchmark','Sec. 8','#f1eafa','#7758a5'),
('8. Experimental\ninterpretation','Sec. 9','#edf7ee','#33885c'),
('9. Discussion\n& conclusion','Secs. 10-11','#f1f1f1','#666666')]

def box(x,y,w,h,t,sec,fc,ec):
    p=FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.05',fc=fc,ec=ec,lw=1.15)
    ax.add_patch(p)
    ax.text(x+w/2,y+h*.58,t,ha='center',va='center',fontsize=8.2,fontweight='bold',linespacing=1.2)
    ax.text(x+w/2,y+.18,sec,ha='center',va='bottom',fontsize=7.5,color='.35')

w,h=2.18,1.48
for i,(t,sec,fc,ec) in enumerate(steps):
    row=0 if i<5 else 1
    col=i if i<5 else i-5
    x=.18+col*2.40
    y=2.78 if row==0 else .62
    box(x,y,w,h,t,sec,fc,ec)
    if row==0 and col<4:
        ax.add_patch(FancyArrowPatch((x+w,y+h/2),(x+2.40,y+h/2),arrowstyle='-|>',mutation_scale=11,lw=1,color='.42'))
    if row==1 and i<8:
        ax.add_patch(FancyArrowPatch((x+w,y+h/2),(x+2.40,y+h/2),arrowstyle='-|>',mutation_scale=11,lw=1,color='.42'))
# connector 5 -> 6
x5=.18+4*2.40
ax.add_patch(FancyArrowPatch((x5+w/2,2.78),(x5+w/2,2.30),arrowstyle='-',lw=1,color='.42'))
ax.add_patch(FancyArrowPatch((x5+w/2,2.30),(.18+w/2,2.30),arrowstyle='-',lw=1,color='.42'))
ax.add_patch(FancyArrowPatch((.18+w/2,2.30),(.18+w/2,.62+h),arrowstyle='-|>',mutation_scale=11,lw=1,color='.42'))
ax.text(6.15,.16,'Theory is compacted in the main text; detailed proofs and the Bayesian extension are in the Supplement.',ha='center',fontsize=8.2,style='italic',color='.35')
ax.set_title('Paper architecture: compact theory, expanded simulations, and a dedicated fractional-delay study',fontsize=10.7,pad=6)
fig.tight_layout()
fig.savefig(OUT,bbox_inches='tight')
print(OUT)
