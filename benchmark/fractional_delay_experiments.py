"""Targeted fractional-delay experiments for the Q1 restructuring pass.

Combined model:
    tau0^(alpha-1) D_t^alpha x = P(x;A) - a*x*y/(1+h*x) + u(t)
    tau0^(alpha-1) D_t^alpha y = e*a*x(t-tau)*y(t)/(1+h*x(t-tau)) - m*y(t)

At tau=0 this reduces to the Caputo model used in the main benchmark.
At alpha=1 it reduces to the retarded DDE stress-test used in the main benchmark
(up to numerical-method discretization error).

The experiments are deliberately targeted rather than a new large campaign. They provide
numerical evidence requested by the referee for the joint delay-fractional mechanism.
"""
from pathlib import Path
import json, math
import numpy as np
import matplotlib.pyplot as plt
from math import gamma

import core, bench, designs

TAU0 = 1.0
Bch = np.array([1.0,0.0])
AMP = 0.10


def caputo_delay_pece(A, alpha, tau, uf, T=12.0, N=320, amp=AMP):
    """PECE solver for the combined nonlinear fractional-delay predator-prey model.

    Constant equilibrium history is used on [-tau,0]. For tau>0 the requested grids
    satisfy tau >= h, so all delayed values in the corrector are already in the known history.
    tau=0 is delegated to the validated Caputo PECE implementation.
    """
    if tau <= 1e-14:
        return bench.sim_nonlinear("Caputo", A, alpha, uf, T, N, amp=amp)
    h = T/N
    if tau < h - 1e-12:
        raise ValueError(f"tau={tau} must be >= step h={h} for this targeted solver")
    ts, uarr, uval = bench.build_input(uf,T,N,amp)
    z0=np.array([core.x_star(),core.y_star(A)],float)
    z=np.zeros((N+1,2)); z[0]=z0
    ha=h**alpha; ga2=gamma(alpha+2.0)
    kaa=np.arange(N+2,dtype=float)**alpha
    ka1=np.arange(N+2,dtype=float)**(alpha+1.0)

    def hist(tq, max_i):
        if tq <= 0: return z0
        k=tq/h
        lo=int(np.floor(k)); frac=k-lo
        lo=min(lo,max_i)
        if lo>=max_i: return z[max_i]
        return z[lo]*(1-frac)+z[lo+1]*frac

    def rhs(t, zz, zd):
        x,y=zz; xd=zd[0]
        hol=core.AA*x*y/(1+core.HH*x)
        hol_d=core.AA*xd*y/(1+core.HH*xd)
        f=np.array([core.P(x,A)-hol+uval(t), core.EE*hol_d-core.MM*y])
        return TAU0**(1-alpha)*f

    gvals=np.zeros((N+1,2)); gvals[0]=rhs(0.0,z0,z0)
    for n in range(N):
        idx=np.arange(n+1)
        b=(ha/alpha)*(kaa[n+1-idx]-kaa[n-idx])
        zP=z0+(b[:,None]*gvals[:n+1]).sum(axis=0)
        aw=np.empty(n+2)
        aw[0]=ha/ga2*(n**(alpha+1.0)-(n-alpha)*(n+1.0)**alpha)
        if n>=1:
            jj=np.arange(1,n+1)
            aw[1:n+1]=ha/ga2*(ka1[n-jj+2]+ka1[n-jj]-2*ka1[n-jj+1])
        aw[n+1]=ha/ga2
        tn1=(n+1)*h
        zdP=hist(tn1-tau,n)
        gP=rhs(tn1,zP,zdP)
        z[n+1]=z0+(aw[:n+1,None]*gvals[:n+1]).sum(axis=0)+aw[n+1]*gP
        zd=hist(tn1-tau,n+1)
        gvals[n+1]=rhs(tn1,z[n+1],zd)
        if not np.all(np.isfinite(z[n+1])) or np.max(np.abs(z[n+1]))>100:
            z[n+1:]=np.nan; break
    return ts,z


def l2traj(ts,z1,z2):
    d=z1-z2
    return float(np.sqrt(np.trapezoid(np.sum(d*d,axis=1),ts)))


def min_allee(z,A):
    return float(np.nanmin(z[:,0])-A)


def peak_dev(z,A):
    zstar=np.array([core.x_star(),core.y_star(A)])
    return float(np.nanmax(np.linalg.norm(z-zstar,axis=1)))


def validate_limits(outdir):
    A=.25; T=6.; uf=designs.u_pulse
    rows=[]
    # alpha=1 should converge toward the DDE solution as N grows.
    for N in (200,400,800):
        tau=.35
        ts,zfd=caputo_delay_pece(A,1.0,tau,uf,T,N)
        _,zdde=bench.sim_nonlinear("DDE",A,1.0,uf,T,N,tau=tau,amp=AMP)
        rows.append({"gate":"alpha1_to_dde","N":N,"max_abs":float(np.nanmax(np.abs(zfd-zdde)))})
    # Self-convergence at a representative fractional-delay cell.
    refs={}
    for N in (200,400,800):
        ts,z=caputo_delay_pece(A,.85,.35,uf,T,N)
        refs[N]=(ts,z)
    t800,z800=refs[800]
    for N in (200,400):
        t,z=refs[N]
        zi=np.column_stack([np.interp(t800,t,z[:,j]) for j in range(2)])
        rows.append({"gate":"fd_self_convergence","N":N,"max_abs_vs_N800":float(np.max(np.abs(zi-z800)))})
    Path(outdir).mkdir(parents=True,exist_ok=True)
    Path(outdir,"fractional_delay_validation.json").write_text(json.dumps(rows,indent=2))
    return rows


def figure_trajectories(outdir):
    A=.25; alpha=.85; T=12.; N=360; uf=designs.u_pulse
    taus=[0,.15,.35,.50]
    fig,axs=plt.subplots(2,1,figsize=(7.4,6.0),sharex=True)
    for tau in taus:
        ts,z=caputo_delay_pece(A,alpha,tau,uf,T,N)
        lab=rf"$\tau={tau:.2f}$"
        axs[0].plot(ts,z[:,0],lw=1.45,label=lab)
        axs[1].plot(ts,z[:,1],lw=1.45,label=lab)
    axs[0].axhline(A,ls='--',lw=1,color='0.45',label='Allee threshold')
    axs[0].set_ylabel('prey $x(t)$'); axs[1].set_ylabel('predator $y(t)$'); axs[1].set_xlabel('time')
    axs[0].set_title(rf'Fractional-delay response to a prey pulse ($A={A}$, $\alpha={alpha}$)')
    for ax in axs: ax.grid(alpha=.22); ax.legend(fontsize=8,ncol=3)
    fig.tight_layout(); fig.savefig(Path(outdir,'fig20_fractional_delay_trajectories.pdf'),bbox_inches='tight'); plt.close(fig)


def figure_bridge(outdir):
    A=.25; T=12.; N=260; uf=designs.u_pulse
    alphas=np.array([.70,.75,.80,.85,.90,.95,1.0])
    taus=np.array([0,.10,.20,.30,.40,.50])
    dcap=np.zeros((len(alphas),len(taus))); ddde=np.zeros_like(dcap); margin=np.zeros_like(dcap)
    cache={}
    # Pure Caputo for each alpha; pure DDE for each tau (alpha=1)
    for a in alphas:
        cache[(a,0.0)]=caputo_delay_pece(A,float(a),0,uf,T,N)[1]
    for tau in taus:
        cache[(1.0,float(tau))]=caputo_delay_pece(A,1.0,float(tau),uf,T,N)[1]
    ts=caputo_delay_pece(A,.85,.2,uf,T,N)[0]
    for ia,a in enumerate(alphas):
        for jt,tau in enumerate(taus):
            key=(float(a),float(tau))
            z=cache.get(key)
            if z is None:
                _,z=caputo_delay_pece(A,float(a),float(tau),uf,T,N); cache[key]=z
            dcap[ia,jt]=l2traj(ts,z,cache[(float(a),0.0)])
            ddde[ia,jt]=l2traj(ts,z,cache[(1.0,float(tau))])
            margin[ia,jt]=min_allee(z,A)
    fig,axs=plt.subplots(1,3,figsize=(11.0,3.6),sharey=True)
    mats=[dcap,ddde,margin]
    titles=['distance to pure Caputo ($\\tau=0$)','distance to pure DDE ($\\alpha=1$)','minimum Allee margin']
    for ax,M,title in zip(axs,mats,titles):
        im=ax.imshow(M,origin='lower',aspect='auto',extent=[taus[0],taus[-1],alphas[0],alphas[-1]])
        ax.set_xlabel('delay $\\tau$'); ax.set_title(title,fontsize=9)
        fig.colorbar(im,ax=ax,shrink=.82)
    axs[0].set_ylabel('fractional order $\\alpha$')
    fig.suptitle('The fractional-delay model bridges fractional and delayed response laws',fontsize=10.5)
    fig.tight_layout(); fig.savefig(Path(outdir,'fig21_fractional_delay_bridge.pdf'),bbox_inches='tight'); plt.close(fig)
    np.savez(Path(outdir,'fractional_delay_bridge_data.npz'),alphas=alphas,taus=taus,dcap=dcap,ddde=ddde,margin=margin)


def figure_design_ranking(outdir):
    A=.25; T=12.; N=240
    alphas=[.75,.85,.95]; taus=[.15,.30,.45]
    rows=[]
    for name,uf in designs.INPUTS.items():
        vals=[]; margins=[]
        for a in alphas:
            _,zc=caputo_delay_pece(A,a,0,uf,T,N)
            for tau in taus:
                ts,zfd=caputo_delay_pece(A,a,tau,uf,T,N)
                _,zdde=caputo_delay_pece(A,1.0,tau,uf,T,N)
                # conservative separation from either limiting explanation
                vals.append(min(l2traj(ts,zfd,zc),l2traj(ts,zfd,zdde)))
                margins.append(min_allee(zfd,A))
        rows.append({"design":name,"mean_min_bridge_distance":float(np.mean(vals)),
                     "min_allee_margin":float(np.min(margins)),
                     "cross_fraction":float(np.mean(np.asarray(margins)<=0))})
    rows=sorted(rows,key=lambda r:r['mean_min_bridge_distance'],reverse=True)
    Path(outdir,'fractional_delay_design_ranking.json').write_text(json.dumps(rows,indent=2))
    fig,axs=plt.subplots(1,2,figsize=(8.8,3.8))
    names=[r['design'] for r in rows]; x=np.arange(len(names))
    axs[0].bar(x,[r['mean_min_bridge_distance'] for r in rows]); axs[0].set_xticks(x,names,rotation=35,ha='right')
    axs[0].set_ylabel('mean min. trajectory distance'); axs[0].set_title('Discrimination of fractional-delay dynamics')
    axs[1].bar(x,[r['cross_fraction'] for r in rows]); axs[1].set_xticks(x,names,rotation=35,ha='right')
    axs[1].set_ylabel('Allee-crossing fraction'); axs[1].set_title('Numerical safety stress test')
    for ax in axs: ax.grid(axis='y',alpha=.22)
    fig.tight_layout(); fig.savefig(Path(outdir,'fig22_fractional_delay_design_ranking.pdf'),bbox_inches='tight'); plt.close(fig)
    return rows


def figure_delay_sweep(outdir):
    A=.25; T=12.; N=280; uf=designs.u_pulse
    taus=np.linspace(0,.55,12); alphas=[.75,.85,.95]
    fig,axs=plt.subplots(1,3,figsize=(10.7,3.5))
    for a in alphas:
        tpk=[]; ppk=[]; marg=[]
        for tau in taus:
            ts,z=caputo_delay_pece(A,a,float(tau),uf,T,N)
            im=int(np.nanargmax(z[:,1]))
            tpk.append(float(ts[im])); ppk.append(float(z[im,1])); marg.append(min_allee(z,A))
        axs[0].plot(taus,tpk,'o-',ms=3,label=rf'$\alpha={a}$')
        axs[1].plot(taus,ppk,'o-',ms=3,label=rf'$\alpha={a}$')
        axs[2].plot(taus,marg,'o-',ms=3,label=rf'$\alpha={a}$')
    axs[2].axhline(0,ls='--',color='0.4',lw=1)
    axs[0].set_ylabel('time of predator peak'); axs[1].set_ylabel('predator peak'); axs[2].set_ylabel('minimum Allee margin')
    for ax in axs: ax.set_xlabel(r'delay $\tau$'); ax.grid(alpha=.22); ax.legend(fontsize=7.5)
    axs[0].set_title('Delay shifts predator response'); axs[1].set_title('Peak amplitude'); axs[2].set_title('Safety margin')
    fig.suptitle('Delay sweep in the combined fractional-delay model (pulse experiment)',fontsize=10.5)
    fig.tight_layout(); fig.savefig(Path(outdir,'fig23_fractional_delay_sweep.pdf'),bbox_inches='tight'); plt.close(fig)


def main():
    outdir=Path(__file__).resolve().parents[1]/'figures'
    validate_limits(outdir)
    figure_trajectories(outdir)
    figure_bridge(outdir)
    figure_design_ranking(outdir)
    figure_delay_sweep(outdir)
    print('fractional-delay figures and validation generated in',outdir)

if __name__=='__main__': main()
