#!/usr/bin/env python3
"""Interval-arithmetic upper enclosures for the explicit Round-4 SOE mixtures.

Unlike scipy.integrate.quad, this checker does not treat a QUADPACK error
estimate as a proof certificate.  On each subinterval I=[a,b], it encloses
f(t)=k_alpha(t)-k_m(t) by natural interval arithmetic and uses
    integral_I |f(t)| dt <= |I| * sup_{t in I}|f(t)|.
The singular head (0,delta) is bounded by the exact component integrals
int k_alpha + int k_m.  All arithmetic in the body and head uses mpmath.iv.
"""
import json, os
import numpy as np
import mpmath as mp

HERE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(HERE)
R4=os.path.join(ROOT,'research_rounds','round4','round4_results.json')
D=json.load(open(R4))
mp.iv.dps=25
I=mp.iv
ALPHA=I.mpf(['0.85','0.85'])
T=12.0
DELTA=1e-4
SPLIT=0.1
NLOG=2500
NLIN=5000


def upper(x):
    return float(x.b)


def enclosure(c):
    m=int(c['m'])
    ell=I.mpf([str(c['ell']),str(c['ell'])])
    L=I.mpf([str(c['L']),str(c['L'])])
    h=(L-ell)/m
    ca=I.sin(I.pi*ALPHA)/I.pi
    gam=I.gamma(ALPHA)
    lams=[ell+j*h for j in range(m)]
    coeff=[ca*h*(lam**(-ALPHA)) for lam in lams]
    d=I.mpf([str(DELTA),str(DELTA)])
    head=d**ALPHA/(ALPHA*gam)
    for cj,lam in zip(coeff,lams):
        head += cj*(1-I.exp(-lam*d))/lam

    xs=np.unique(np.concatenate([
        np.geomspace(DELTA,SPLIT,NLOG+1),
        np.linspace(SPLIT,T,NLIN+1),
    ]))
    body=I.mpf([0,0])
    p=ALPHA-I.mpf([1,1])
    for a,b in zip(xs[:-1],xs[1:]):
        ai=I.mpf([str(float(a)),str(float(a))])
        bi=I.mpf([str(float(b)),str(float(b))])
        ti=I.mpf([str(float(a)),str(float(b))])
        ka=(ti**p)/gam
        km=I.mpf([0,0])
        for cj,lam in zip(coeff,lams):
            km += cj*I.exp(-lam*ti)
        width=bi-ai
        body += width*abs(ka-km)
    total=head+body
    return {
        'm':m,'ell':c['ell'],'L':c['L'],
        'head_upper':upper(head),'body_upper':upper(body),
        'Ebar_interval_upper':upper(total),
        'old_quad_estimate':c['Ebar_cert'],
        'uplift_fraction':upper(total)/c['Ebar_cert']-1.0,
        'partition':{'delta':DELTA,'split':SPLIT,'nlog':NLOG,'nlin':NLIN},
    }

rows=[enclosure(c) for c in D['phase0_certificates']]
# Because K_j subset K_m by zero padding for j<=m, the best available certified
# constructive upper envelope at budget m is the running minimum.
best=float('inf')
for r in rows:
    best=min(best,r['Ebar_interval_upper'])
    r['Ehat_nested_upper']=best
out={'method':'natural interval enclosure + exact-component singular-head bound',
     'rows':rows}
with open(os.path.join(HERE,'Ebar_interval_bounds.json'),'w') as f:
    json.dump(out,f,indent=2)
print('m  interval_upper  nested_upper  old_quad  uplift')
for r in rows:
    print(f"{r['m']:2d} {r['Ebar_interval_upper']:.9f} {r['Ehat_nested_upper']:.9f} "
          f"{r['old_quad_estimate']:.9f} {100*r['uplift_fraction']:.3f}%")
