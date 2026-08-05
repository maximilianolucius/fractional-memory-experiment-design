"""make_figures.py — generate the paper's 10 figures from benchmark artifacts + core code.
Outputs PDF figures into ../figures/. Run on Orion (matplotlib in fmi_venv)."""
import os, json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import core, designs, bench

ART = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "artifacts")
FIG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figures")
os.makedirs(FIG, exist_ok=True)
J = json.load
nl = J(open(os.path.join(ART, "nonlinear_confusion.json")))
lin = J(open(os.path.join(ART, "linear_factorial.json")))
sv = J(open(os.path.join(ART, "solver_validation.json")))
A = 0.25; Jm = core.jacobian(A); B = np.array([1.0, 0.0]); C = np.array([1.0, 0.0])
def save(fig, name): fig.tight_layout(); fig.savefig(os.path.join(FIG, name)); plt.close(fig); print("wrote", name, flush=True)

# --- transfer functions of the 4 mechanisms (prey->prey channel) ---
w = np.logspace(-1.5, 1.5, 400); s = 1j * w
def G_ode(s): return np.array([C @ np.linalg.solve(si*np.eye(2)-Jm, B) for si in s])
def G_cap(s, al): return np.array([C @ np.linalg.solve((si**al)*np.eye(2)-Jm, B) for si in s])
def G_dde(s, tau=0.35):
    J0=Jm.copy(); J1=np.zeros((2,2)); J1[1,0]=Jm[1,0]; J0[1,0]=0.0
    return np.array([C @ np.linalg.solve(si*np.eye(2)-J0-J1*np.exp(-si*tau), B) for si in s])
def G_lat(s, rates=(0.6,1.0,0.4), g=0.15):
    m=len(rates); Ab=np.zeros((2+m,2+m)); Ab[:2,:2]=Jm; Ab[0,2:]=g; Ab[2:,2:]=-np.diag(rates)
    Bb=np.zeros(2+m); Bb[0]=1; Bb[2:]=1; Cb=np.zeros(2+m); Cb[0]=1
    return np.array([Cb @ np.linalg.solve(si*np.eye(2+m)-Ab, Bb) for si in s])
Go, Gc, Gd, Gl = G_ode(s), G_cap(s,0.85), G_dde(s), G_lat(s)

f=plt.figure(figsize=(6,4)); ax=f.gca()
for G,lab in [(Go,"ODE"),(Gc,"Caputo $\\alpha=0.85$"),(Gd,"DDE $\\tau=0.35$"),(Gl,"latent")]:
    ax.loglog(w, np.abs(G), label=lab)
ax.set_xlabel("$\\omega$"); ax.set_ylabel("$|G(i\\omega)|$"); ax.legend(); ax.set_title("Transfer magnitude, prey channel ($A=0.25$)"); ax.grid(True,which="both",alpha=0.3)
save(f,"fig01_transfer_magnitude.pdf")

f=plt.figure(figsize=(6,4)); ax=f.gca()
for G,lab in [(Go,"ODE"),(Gc,"Caputo"),(Gd,"DDE"),(Gl,"latent")]:
    ax.semilogx(w, np.angle(G), label=lab)
ax.set_xlabel("$\\omega$"); ax.set_ylabel("$\\arg G(i\\omega)$ [rad]"); ax.legend(); ax.set_title("Transfer phase"); ax.grid(True,which="both",alpha=0.3)
save(f,"fig02_transfer_phase.pdf")

# --- high-frequency Caputo phase -> -alpha*pi/2 ---
f=plt.figure(figsize=(6,4)); ax=f.gca()
for al in [0.7,0.85,0.95]:
    ax.semilogx(w, np.angle(G_cap(s,al)), label=f"$\\alpha={al}$")
    ax.axhline(-al*np.pi/2, ls=":", color="gray")
ax.set_xlabel("$\\omega$"); ax.set_ylabel("$\\arg G_\\alpha(i\\omega)$"); ax.legend(); ax.set_title("Caputo high-frequency phase $\\to -\\alpha\\pi/2$"); ax.grid(True,which="both",alpha=0.3)
save(f,"fig03_hf_phase.pdf")

# --- equal-amplitude waveforms ---
T=12.0; N=600; ts=np.linspace(0,T,N+1)
f=plt.figure(figsize=(7,4)); ax=f.gca()
for name in ["pulse","multiscale","sinusoid","multisine","chirp","prbs"]:
    _,ua,_=bench.build_input(designs.INPUTS[name],T,N,amp=0.10); ax.plot(ts,ua+0*0,label=name,alpha=0.8)
ax.set_xlabel("$t$"); ax.set_ylabel("$u(t)$ (peak $=0.10$)"); ax.legend(ncol=3,fontsize=8); ax.set_title("Equal-amplitude input designs"); ax.grid(True,alpha=0.3)
save(f,"fig04_waveforms.pdf")

# --- linear-Gaussian design ranking ---
lr=lin["design_ranking_by_mean_min_pairwise_KL"]; k=list(lr); v=[lr[x] for x in k]
f=plt.figure(figsize=(6,4)); ax=f.gca(); ax.bar(k,v,color="steelblue"); ax.set_ylabel("mean min-pairwise KL"); ax.set_title("Exact linear-Gaussian design ranking"); ax.tick_params(axis="x",rotation=30); ax.grid(True,axis="y",alpha=0.3)
save(f,"fig05_linear_ranking.pdf")

# --- solver convergence PECE vs Mittag-Leffler ---
Ns=[int(x.split("=")[1]) for x in sv if x.startswith("N=")]; errs=[sv[f"N={n}"]["max_abs_err"] for n in Ns]
f=plt.figure(figsize=(6,4)); ax=f.gca(); ax.loglog(Ns,errs,"o-"); ax.set_xlabel("N (time steps)"); ax.set_ylabel("max abs error vs $E_\\alpha$"); ax.set_title("Caputo PECE convergence vs Mittag--Leffler"); ax.grid(True,which="both",alpha=0.3)
save(f,"fig06_solver_convergence.pdf")

# --- confusion matrix (stable, 4-class) ---
cm=nl["stable"]["confusion_4class"]; cls=["ODE","Caputo","DDE","latent3"]
M=np.array([[cm[t][c] for c in cls] for t in cls],float); Mn=M/M.sum(1,keepdims=True)
f=plt.figure(figsize=(5.2,4.6)); ax=f.gca(); im=ax.imshow(Mn,cmap="Blues",vmin=0,vmax=1)
ax.set_xticks(range(4)); ax.set_xticklabels(cls,rotation=30); ax.set_yticks(range(4)); ax.set_yticklabels(cls)
for i in range(4):
    for j in range(4): ax.text(j,i,f"{Mn[i,j]:.2f}",ha="center",va="center",color="black" if Mn[i,j]<0.6 else "white",fontsize=8)
ax.set_xlabel("predicted"); ax.set_ylabel("true"); ax.set_title("Confusion (stable, row-normalized)"); f.colorbar(im,fraction=0.046)
save(f,"fig07_confusion.pdf")

# --- accuracy vs alpha ---
ba=nl["stable_stratified"]["by_alpha"]; ka=sorted(ba,key=float); va=[ba[x] for x in ka]
f=plt.figure(figsize=(5.5,4)); ax=f.gca(); ax.plot([float(x) for x in ka],va,"s-"); ax.axhline(0.25,ls=":",color="gray",label="chance"); ax.set_xlabel("$\\alpha$"); ax.set_ylabel("accuracy"); ax.set_title("Accuracy vs fractional order (stable)"); ax.legend(); ax.grid(True,alpha=0.3)
save(f,"fig08_accuracy_vs_alpha.pdf")

# --- accuracy by SNR and channel ---
bs=nl["stable_stratified"]["by_snr"]; bc=nl["stable_stratified"]["by_channel"]
f,axs=plt.subplots(1,2,figsize=(8,3.6))
for ax,d,ttl in [(axs[0],bs,"by SNR"),(axs[1],bc,"by channel")]:
    ax.bar(list(d),[d[x] for x in d],color="teal"); ax.axhline(0.25,ls=":",color="gray"); ax.set_title(ttl); ax.set_ylabel("accuracy"); ax.grid(True,axis="y",alpha=0.3)
save(f,"fig09_accuracy_snr_channel.pdf")

# --- safety-informativeness trade-off ---
saf=nl["safety_stable"]; rank=nl["stable"]["design_ranking"]
names=[n for n in saf if n in rank]
x=[saf[n]["allee_cross_rate"] for n in names]; y=[rank[n] for n in names]
f=plt.figure(figsize=(6,4.4)); ax=f.gca(); ax.scatter(x,y,s=60,color="crimson")
for n,xi,yi in zip(names,x,y): ax.annotate(n,(xi,yi),fontsize=8,xytext=(4,4),textcoords="offset points")
ax.set_xlabel("Allee-crossing rate (unsafe $\\to$)"); ax.set_ylabel("Task-A accuracy"); ax.set_title("Safety--informativeness trade-off"); ax.grid(True,alpha=0.3)
save(f,"fig10_safety_tradeoff.pdf")
print("ALL FIGURES DONE:", len(os.listdir(FIG)))
