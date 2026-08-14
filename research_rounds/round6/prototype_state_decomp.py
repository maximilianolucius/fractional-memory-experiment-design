#!/usr/bin/env python3
"""Round-6 prototype (float): pole/branch-cut decomposition of the exact
fractional prey-channel impulse response
    g_alpha(t) = e1^T L^{-1}[(s^a I - J(A))^{-1}] e1
               = sum_i w_i t^{a-1} E_{a,a}(lam_i t^a),  w_i = lam_i/(lam_i-lam_j).
Validates: decomposition (pole + branch integral) vs Mittag-Leffler series,
then measures branch-density mass and naive quadrature error decay.
NOT a certificate: float only, for design decisions.
"""
import numpy as np, math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','benchmark'))
import core as bench
from scipy.special import gamma as G
from scipy.integrate import quad

ALPHA=0.85; T=12.0

def eig_w(A):
    J=bench.jacobian(A)
    tr=J[0,0]; det=J[0,0]*J[1,1]-J[0,1]*J[1,0]  # J22=0 -> det=-J12*J21
    disc=complex(tr*tr-4*det)
    l1=(tr+np.sqrt(disc))/2; l2=(tr-np.sqrt(disc))/2
    w1=l1/(l1-l2); w2=l2/(l2-l1)
    return l1,l2,w1,w2

def ml_series(t, lam, terms=120):
    # t^{a-1} E_{a,a}(lam t^a) by series (ok for moderate |lam| t^a)
    z=lam*t**ALPHA
    s=0j; term=1.0/G(ALPHA)
    for k in range(terms):
        s+=term
        term=term*z*G(ALPHA*k+ALPHA)/G(ALPHA*(k+1)+ALPHA)
    return t**(ALPHA-1)*s

def pole_branch(t, lam):
    # sheet pole s0=lam^{1/a} exists iff |arg lam| < a*pi
    a=ALPHA
    s0=abs(lam)**(1/a)*np.exp(1j*np.angle(lam)/a)
    pole=(s0/(a*lam))*np.exp(s0*t)
    def phi(r):
        return (1/math.pi)*r**a*math.sin(a*math.pi)/(r**(2*a)-2*lam*r**a*math.cos(a*math.pi)+lam*lam)
    re,_=quad(lambda r: (np.exp(-r*t)*phi(r)).real,0,np.inf,limit=400)
    im,_=quad(lambda r: (np.exp(-r*t)*phi(r)).imag,0,np.inf,limit=400)
    return pole+re+1j*im

for A in (0.25,0.30):
    l1,l2,w1,w2=eig_w(A)
    print(f'A={A}: lam={l1:.6f}, w1={w1:.6f}, |arg lam|={abs(np.angle(l1)):.4f} in (api/2,api)=({ALPHA*np.pi/2:.4f},{ALPHA*np.pi:.4f})')
    s0=abs(l1)**(1/ALPHA)*np.exp(1j*np.angle(l1)/ALPHA)
    print(f'   sheet pole s0={s0:.6f} (Re<0: {s0.real<0}), residue coeff s0/(a*lam)={s0/(ALPHA*l1):.6f}')
    # validate decomposition at several t
    errs=[]
    for t in (0.05,0.3,1.0,3.0,8.0,12.0):
        v1=ml_series(t,l1); v2=pole_branch(t,l1)
        errs.append(abs(v1-v2))
    print('   decomp vs ML-series max abs err:', max(errs))
    # combined real branch density and masses
    def Phi(r):
        phi=(1/math.pi)*r**ALPHA*math.sin(ALPHA*math.pi)/(r**(2*ALPHA)-2*l1*r**ALPHA*math.cos(ALPHA*math.pi)+l1*l1)
        return 2*(w1*phi).real
    massL1,_=quad(lambda r: abs(Phi(r))*(1-math.exp(-r*T))/r,0,np.inf,limit=400)
    print(f'   int |Phi|(1-e^-rT)/r dr (L1(0,T) mass of branch part) = {massL1:.4f}')
    # g_alpha L1 norm and pole-part L1 norm
    gl1,_=quad(lambda t: abs(2*(w1*ml_series(t,l1)).real),0,T,limit=400)
    pl1,_=quad(lambda t: abs(2*(w1*(s0/(ALPHA*l1))*np.exp(s0*t)).real),0,T,limit=400)
    print(f'   ||g_alpha||_L1(0,T)={gl1:.4f}   ||pole part||_L1={pl1:.4f}')
