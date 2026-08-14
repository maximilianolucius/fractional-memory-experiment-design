import json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
nl=json.load(open(os.path.join(ROOT,"benchmark","results","nonlinear_confusion.json")))
SAFE="#2e8b57"; UNSAFE="#c0392b"; MID="#d98e2b"; GRID={"alpha":0.25}
saf=nl["safety_stable"]; rank=nl["stable"]["design_ranking"]
names=[n for n in saf if n in rank]
x=[saf[n]["allee_cross_rate"] for n in names]
y=[rank[n] for n in names]
def col_of(n):
    r=saf[n]["allee_cross_rate"]
    return SAFE if r==0 else (MID if r<0.2 else UNSAFE)
plt.rcParams.update({"font.size":9,"axes.labelsize":10,"axes.titlesize":10.5,
                     "legend.fontsize":8,"xtick.labelsize":8,"ytick.labelsize":8,
                     "axes.linewidth":0.8,"lines.linewidth":1.5,"pdf.fonttype":42})
f,ax=plt.subplots(figsize=(6.6,4.6))
ax.axvspan(-0.02,0.12,color="#e7f2ea",zorder=0)
ax.axvspan(0.88,1.02,color="#f7e3e1",zorder=0)
ax.scatter(x,y,s=110,c=[col_of(n) for n in names],zorder=3,edgecolors="black",linewidths=0.6)
off={"multiscale":(-8,8),"pulse":(8,-12),"multisine":(8,6),"chirp":(-30,8),
     "sinusoid":(-52,-12),"prbs":(-38,8)}
for n,xi,yi in zip(names,x,y):
    dx,dy=off.get(n,(6,6))
    ax.annotate(n,(xi,yi),fontsize=9,xytext=(dx,dy),textcoords="offset points",
                color=col_of(n),fontweight="bold")
ax.text(0.015,0.355,"lower-crossing / weak",color=SAFE,fontsize=9.5,style="italic",ha="left")
ax.text(0.95,0.575,"higher-crossing / informative",color=UNSAFE,fontsize=9.5,style="italic",ha="right")
ax.set_xlabel("Allee-crossing rate (fraction of stable-regime cells)")
ax.set_ylabel("Task-A macro-accuracy")
ax.set_title("The safety--informativeness trade-off at a common amplitude budget")
ax.set_xlim(-0.05,1.05); ax.grid(True,**GRID)
f.tight_layout()
out=os.path.join(ROOT,"figures","fig10_safety_tradeoff.pdf")
f.savefig(out); plt.close(f)
print(out)
