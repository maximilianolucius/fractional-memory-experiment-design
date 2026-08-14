#!/usr/bin/env python3
"""Chief Round-5 repair of the atlas.

Repairs three audit defects:
1) theorem classes use running-envelope (nested) rate windows;
2) every constructive mixture is forced to satisfy the alpha-dependent mass cap;
3) atlas cells outside the focal Caputo Matignon-stable regime are flagged and
   excluded from headline counts.

The d_rob maximization is still ordinary high-accuracy floating-point
numerics, so this script labels its atlas as theorem-guided / numerically
validated, not interval-certified.
"""
import json, math, os, sys
import numpy as np
import mpmath as mp
from scipy.special import gamma

ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R5=os.path.join(ROOT,'research_rounds','round5')
sys.path.insert(0,R5)
sys.path.insert(0,os.path.join(ROOT,'benchmark'))
import compute_round5 as r5
import core

T=r5.T; ETA=r5.ETA; U_MAX=r5.U_MAX; X_STAR=r5.X_STAR
ALPHAS=(0.70,0.85,0.95); MS=(4,8,16,32); SIGMAS=(0.05,0.10,0.15,0.20)
A_LIST=r5.A_LIST

raw=sorted(r5.tuned_windows(), key=lambda c:c['m'])
raw_by_m={c['m']:c for c in raw}

def running_envelope(m):
    sub=[c for c in raw if c['m']<=m]
    return min(c['ell'] for c in sub), max(c['L'] for c in sub)

ENV={m:running_envelope(m) for m in MS}


def explicit_leftnode(alpha,m):
    """Stored constructive mixture (raw tuned ell,L), rescaled if required by mass cap."""
    c=raw_by_m[m]; ell=float(c['ell']); L=float(c['L'])
    h=(L-ell)/m
    lam=ell+np.arange(m)*h
    ca=math.sin(math.pi*alpha)/math.pi
    coeff=ca*h*lam**(-alpha)
    mass=float(np.sum(coeff*(1-np.exp(-lam*T))/lam))
    M_T=float(T**alpha/gamma(alpha+1)+1.0)
    scale=min(1.0,M_T/mass)
    return ell,L,lam,coeff*scale,mass,scale,M_T


def interval_error(alpha,m):
    """Interval upper enclosure for the possibly mass-rescaled explicit mixture."""
    ell,L,lam_np,coeff_np,mass,scale,M_T=explicit_leftnode(alpha,m)
    mp.iv.dps=25; I=mp.iv
    aI=I.mpf([str(alpha),str(alpha)])
    gam=I.gamma(aI)
    # Freeze lambda and coefficients as narrow outward intervals from decimal strings.
    lams=[I.mpf([str(float(x)),str(float(x))]) for x in lam_np]
    coeff=[I.mpf([str(float(x)),str(float(x))]) for x in coeff_np]
    delta=1e-4; dI=I.mpf([str(delta),str(delta)])
    head=dI**aI/(aI*gam)
    for cj,la in zip(coeff,lams):
        head += cj*(1-I.exp(-la*dI))/la
    xs=np.unique(np.concatenate([np.geomspace(delta,0.1,700+1),np.linspace(0.1,T,1200+1)]))
    body=I.mpf([0,0]); p=aI-I.mpf([1,1])
    for aa,bb in zip(xs[:-1],xs[1:]):
        ti=I.mpf([str(float(aa)),str(float(bb))])
        ka=(ti**p)/gam
        km=I.mpf([0,0])
        for cj,la in zip(coeff,lams): km += cj*I.exp(-la*ti)
        width=I.mpf([str(float(bb-aa)),str(float(bb-aa))])
        body += width*abs(ka-km)
    return {
        'raw_window':[ell,L], 'hierarchy_window':list(ENV[m]),
        'raw_mass':mass,'mass_cap':M_T,'coefficient_scale':scale,
        'U_interval':float((head+body).b)
    }


def matignon_stable(alpha,A):
    eig=np.linalg.eigvals(core.jacobian(A))
    return bool(np.all(np.abs(np.angle(eig))>alpha*np.pi/2))


def main():
    # Construct valid interval Ehat values.
    e_details={}; Ehat={}
    for alpha in ALPHAS:
        best=float('inf')
        for m in MS:
            d=interval_error(alpha,m)
            best=min(best,d['U_interval'])
            Ehat[(alpha,m)]=best
            e_details[f'a={alpha},m={m}']=d|{'Ehat_running_min':best}
            print('E',alpha,m,d['U_interval'],'scale',d['coefficient_scale'],'best',best,flush=True)

    # Robust-gain lower estimates over the actual nested hierarchy windows.
    ts=np.linspace(1e-4,T,4001); dt=ts[1]-ts[0]
    u0=r5.proto_pulse(ts); cap,nrm=r5.shape_cap(u0,dt)
    fmax={}
    for m in MS:
        ell,L=ENV[m]
        lams=np.geomspace(ell,L,100)
        for A in A_LIST:
            vals=[r5.F_over_w(l,A,u0,ts,dt,nrm) for l in lams]
            # This is a numerical lower estimate of sup F/w (grid points belong to interval).
            # It is intentionally NOT called an interval certificate.
            fmax[(A,m)]=float(max(vals))
        print('gain m',m,'done',flush=True)

    cells=[]
    for alpha in ALPHAS:
        M_T=float(T**alpha/gamma(alpha+1)+1.0)
        for A in A_LIST:
            rho=X_STAR-(A+ETA)
            stable=matignon_stable(alpha,A)
            for m in MS:
                d_grid=M_T*fmax[(A,m)]
                B_Allee=rho/d_grid
                B_univ=math.sqrt(T)*U_MAX
                B_eff=min(B_Allee,cap,B_univ)
                binding='Allee' if B_Allee<=min(cap,B_univ) else ('shape_cap' if cap<=B_univ else 'universal')
                Eh=Ehat[(alpha,m)]
                for sig in SIGMAS:
                    U=(Eh*B_eff)**2/(2*sig**2)
                    pe=0.5*math.erfc(math.sqrt(U)/2.0)  # Phi(-sqrt(U/2))
                    pe_pin=max(0.0,0.5*(1-math.sqrt(U/2)))
                    cls='hard@0.25' if pe>=.25 else ('moderate@0.10' if pe>=.10 else 'inconclusive')
                    cells.append({'alpha':alpha,'A':A,'m':m,'sigma':sig,
                                  'focal_matignon_stable':stable,
                                  'M_T':M_T,'Ehat_IA_valid':Eh,
                                  'd_rob_grid_lower_estimate':d_grid,
                                  'B_Allee_grid':B_Allee,'B_cap':cap,'B_univ':B_univ,
                                  'B_eff_grid':B_eff,'binding_grid':binding,
                                  'U_grid':U,'Pe_gauss_grid':pe,'Pe_pinsker_grid':pe_pin,
                                  'class_grid':cls})
    out={'status':'chief-corrected theorem-guided numerical atlas',
         'warning':'d_rob constants are high-accuracy numerical grid lower estimates, not interval-certified maxima',
         'protocol':'positive pulse ray only',
         'nested_windows':{str(m):list(ENV[m]) for m in MS},
         'E_details':e_details,'alpha_grid':list(ALPHAS),'A_grid':list(A_LIST),
         'm_grid':list(MS),'sigma_grid':list(SIGMAS),'cells':cells}
    p=os.path.join(R5,'atlas_cells_CHIEF_CORRECTED.json')
    json.dump(out,open(p,'w'),indent=1)
    from collections import Counter,defaultdict
    allc=defaultdict(Counter); stc=defaultdict(Counter)
    for c in cells:
        allc[c['alpha']][c['class_grid']]+=1
        if c['focal_matignon_stable']: stc[c['alpha']][c['class_grid']]+=1
    print('ALL', {a:dict(x) for a,x in allc.items()})
    print('STABLE', {a:dict(x) for a,x in stc.items()})
    with open(os.path.join(ROOT,'chief_round5','repair_summary.json'),'w') as f:
        json.dump({'nested_windows':out['nested_windows'],'E_details':e_details,
                   'counts_all':{str(a):dict(x) for a,x in allc.items()},
                   'counts_stable':{str(a):dict(x) for a,x in stc.items()}},f,indent=2)

if __name__=='__main__': main()
