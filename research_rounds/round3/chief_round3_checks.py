#!/usr/bin/env python3
"""Independent chief checks for Round 3.

Checks only; no factorial benchmark rerun.
1) adaptive-quadrature verification of the displayed left-node kernel errors;
2) correct restricted singular values using an orthonormal basis of each dictionary span;
3) one-sided Strong-Allee downward gains for positive transient protocols;
4) shape-specific actuator-energy caps implied by ||u||_infty <= 0.10.
"""
import os, sys, json, math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import svdvals
from scipy.optimize import brentq
from scipy.special import gamma

HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.abspath(os.path.join(HERE,'..','..'))
sys.path.insert(0,os.path.join(ROOT,'benchmark'))
sys.path.insert(0,os.path.join(ROOT,'research_rounds','round2'))
import bench, designs, core
import compute_round3 as r3

ALPHA=.85; T=12.; ETA=.02; UMAX=.10
CA=math.sin(math.pi*ALPHA)/math.pi

def exact(t): return t**(ALPHA-1)/gamma(ALPHA)
def approx(t,m,ell,L):
    h=(L-ell)/m
    lam=ell+np.arange(m)*h
    return CA*h*np.sum(lam**(-ALPHA)*np.exp(-lam*t))

def l1_adaptive(m,ell,L):
    # detect crossings, then integrate |difference| on sign-constant intervals.
    grid=np.unique(np.concatenate([np.geomspace(1e-12,1e-2,700),np.linspace(1e-2,T,2400)]))
    vals=np.array([exact(t)-approx(t,m,ell,L) for t in grid])
    roots=[]
    for i in range(len(grid)-1):
        if vals[i]*vals[i+1]<0:
            roots.append(brentq(lambda t: exact(t)-approx(t,m,ell,L),grid[i],grid[i+1],xtol=1e-14))
    total=0.; err=0.
    bounds=[0.]+roots+[T]
    for lo,hi in zip(bounds[:-1],bounds[1:]):
        v,e=quad(lambda t: abs(exact(t)-approx(t,m,ell,L)),lo,hi,
                 epsabs=1e-11,epsrel=1e-10,limit=500)
        total+=v; err+=e
    return total,err,len(roots)

def dictionary_matrix(name,ts):
    fam=designs.INPUTS[name]
    if name=='sinusoid':
        return np.column_stack([fam(ts,T,amp=1.,w=w) for w in np.linspace(.05,3.,24)])
    if name=='multisine':
        base=(.12,.49,1.6); cols=[]
        for k in range(24):
            ws=tuple(base[j]*(1+.15*(k-12)/12) for j in range(3))
            cols.append(fam(ts,T,amp=1.,ws=ws))
        return np.column_stack(cols)
    if name=='chirp':
        return np.column_stack([fam(ts,T,amp=1.,f0=.05,k=kk) for kk in np.linspace(.005,.12,20)])
    if name=='prbs':
        return np.column_stack([fam(ts,T,amp=1.,nseg=15,seed=s) for s in range(24)])
    raise ValueError(name)

def corrected_span_kappa(name,A=.25):
    n=500; ts=np.linspace(T/n,T,n); dt=ts[1]-ts[0]
    hx=r3.impulse_matrices(A,ALPHA,ts); K=r3.toeplitz_conv(hx,dt)
    M=dictionary_matrix(name,ts)
    U,s,Vt=np.linalg.svd(M,full_matrices=False)
    tol=s[0]*1e-12
    rank=int(np.sum(s>tol)); Q=U[:,:rank]
    sk=svdvals(K@Q)
    return {'rank':rank,'basis_cols':M.shape[1],
            'smin_restricted':float(sk[-1]),'smax_restricted':float(sk[0]),
            'dictionary_condition_nonzero':float(s[0]/s[rank-1])}

def transient_common_bounds(A,name,N=1600):
    rho=core.x_star()-(A+ETA)
    ts,uarr,uval=bench.build_input(designs.INPUTS[name],T,N,amp=1.0)
    dt=ts[1]-ts[0]
    peak=float(np.max(np.abs(uarr)))
    norm=float(np.sqrt(np.sum(uarr**2)*dt))
    # Unit-L2 version of the fixed positive shape.
    per={}
    for model in ['ODE','Caputo','DDE','latent1','latent3']:
        y=bench.lin_response(model,A,ALPHA,designs.INPUTS[name],T,N,
                             designs.CHANNELS['prey'],designs.sample_times(T,240),amp=1.0)[:,0]/norm
        per[model]={'min':float(np.min(y)),'max':float(np.max(y)),
                    'downward_gain':float(max(0.,-np.min(y)))}
    d=max(v['downward_gain'] for v in per.values())
    # For the positive ray c >= 0: safety x*+c g_M >= A+eta gives c <= rho/d.
    allee=float('inf') if d==0 else float(rho/d)
    # Exact shape-specific energy consequence of peak cap on u=c*u0_unitL2.
    shape_cap=float(UMAX*norm/peak)
    return {'rho_eta':rho,'per_model':per,'robust_downward_gain_sampled':d,
            'positive_ray_allee_outer_sampled':allee,
            'shape_specific_actuator_energy_cap':shape_cap,
            'effective_sampled':min(allee,shape_cap)}

def main():
    D=json.load(open(os.path.join(HERE,'round3_results.json')))
    l1=[]
    for c in D['track_A']['cells']:
        q,e,nr=l1_adaptive(c['m'],c['ell'],c['L'])
        l1.append({'m':c['m'],'reported_grid_error':c['E_m'],
                   'adaptive_error':q,'quad_error_est':e,'detected_crossings':nr,
                   'reported_over_adaptive':c['E_m']/q})
    kapp={n:corrected_span_kappa(n) for n in ['sinusoid','multisine','chirp','prbs']}
    bounds=[]
    for A in [.20,.25,.30,.32,.34,.35]:
        for n in ['pulse','multiscale']:
            bounds.append({'A':A,'family':n,**transient_common_bounds(A,n)})
    out={'l1_independent_check':l1,'corrected_dictionary_span_kappa':kapp,
         'one_sided_transient_bounds_benchmark_rivals':bounds,
         'scope_note':'Benchmark-rival bounds are numerical diagnostics for the locked five simulators, not certificates for the full K_m hierarchy.'}
    json.dump(out,open(os.path.join(HERE,'chief_round3_checks.json'),'w'),indent=2)
    print(json.dumps(out,indent=2))
if __name__=='__main__': main()
