#!/usr/bin/env python3
"""Independent lightweight floating-point cross-check for Round 6 T23 certificates.

This is NOT a certificate. It evaluates the exact Mittag-Leffler-series prey response
on a transformed time grid t=T*x^3, which resolves the integrable t^(alpha-1)
singularity at t=0. A naive uniform coarse grid badly overestimates this L1 integral.
The resulting numerical L1 errors must lie below the interval-certified E_upper values.
"""
import json, math, os, sys
import numpy as np

HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT,'benchmark'))
import core as bench

ALPHA=.85
T=12.0
TERMS=180
N=10001
Q=3

# stable gamma ratios for the ML series
ratios=np.exp([math.lgamma(ALPHA*k+ALPHA)-math.lgamma(ALPHA*(k+1)+ALPHA)
               for k in range(TERMS)])
g0=math.gamma(ALPHA)

def ml_vec(ts, lam):
    z=lam*ts**ALPHA
    term=np.full(ts.shape,1.0/g0,dtype=complex)
    acc=np.zeros(ts.shape,dtype=complex)
    for k in range(TERMS):
        acc += term
        term *= z*ratios[k]
    return ts**(ALPHA-1)*acc

def check(A, mkey):
    d=json.load(open(os.path.join(ROOT,'research_rounds','round6',f'round6_results_{A}.json')))
    cell=d['cells'][f'A={A}']; cert=cell['budgets'][mkey]
    Aval=float(A)
    J=bench.jacobian(Aval); tr=J[0,0]; det=-J[0,1]*J[1,0]
    disc=complex(tr*tr-4*det)
    lam=(tr+np.sqrt(disc))/2
    w1=lam/(lam-lam.conjugate())
    s0=abs(lam)**(1/ALPHA)*np.exp(1j*np.angle(lam)/ALPHA)
    Pcoef=w1*s0/(ALPHA*lam)

    # transformed grid resolves integrable near-zero singularity
    x=np.linspace(1e-9,1.0,N)
    ts=T*x**Q
    ga=2*(w1*ml_vec(ts,lam)).real
    gm=2*(Pcoef*np.exp(s0*ts)).real
    for nd in cert['nodes']:
        gm += nd['v']*np.exp(-nd['rhat']*ts)
    integrand=np.abs(ga-gm)*(T*Q*x**(Q-1))
    l1=float(np.trapezoid(integrand,x))
    return {'A':A,'m':mkey,'float_L1_transformed':l1,
            'certified_E_upper':cert['E_upper'],
            'ratio':l1/cert['E_upper'],'pass':l1<=cert['E_upper']}

if __name__=='__main__':
    out=[]
    for A in ('0.25','0.30'):
        for m in ('m=4','m=8','m=16','m=32'):
            out.append(check(A,m))
    print(json.dumps(out,indent=2))
    with open(os.path.join(HERE,'lightweight_check.json'),'w') as f:
        json.dump(out,f,indent=2)
