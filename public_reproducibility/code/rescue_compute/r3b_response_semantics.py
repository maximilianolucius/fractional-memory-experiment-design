import numpy as np, math, json, sys
sys.path.insert(0,"benchmark")
import core

A=0.25; alpha=0.85; T=12.0
J=core.jacobian(A); B=np.array([[1.0],[0.0]]); C=np.array([[1.0,0.0]])
print("J=",J.tolist(),"  ||J||_2=%.6f"%np.linalg.svd(J,compute_uv=False)[0])

def soe_positive(alpha,m,d=1.4,T=1.0):
    """Trapezoidal SOE on log grid, balanced as in Lemma B.2. Returns (c,lam) positive."""
    ca=math.sin(math.pi*alpha)/math.pi
    h=math.sqrt(2*math.pi*d/(m*alpha*(1-alpha)))
    Mp=int(round(2*math.pi*d/(alpha*h*h))); Mm=int(round(2*math.pi*d/((1-alpha)*h*h)))
    # rescale so total nodes ~= m
    tot=Mp+Mm+1; sc=math.sqrt(tot/m); h*=sc
    Mp=max(1,int(round(2*math.pi*d/(alpha*h*h)))); Mm=max(1,int(round(2*math.pi*d/((1-alpha)*h*h))))
    k=np.arange(-Mm,Mp+1); lam=np.exp(k*h); c=ca*h*lam**(1-alpha)
    return c,lam

def kernel_L1_err(alpha,c,lam,T,N=200000):
    t=np.linspace(T/N,T,N)
    K=t**(alpha-1)/math.gamma(alpha)
    S=(c[None,:]*np.exp(-np.outer(t,lam))).sum(1)
    return np.trapezoid(np.abs(K-S),t)

def G_alpha(w):
    s=1j*w; return (C@np.linalg.inv(s**alpha*np.eye(2)-J)@B)[0,0]
def G_m(w,c,lam):
    s=1j*w; Rm=(c/(s+lam)).sum()
    return (C@np.linalg.inv((1.0/Rm)*np.eye(2)-J)@B)[0,0]

w=np.logspace(-3,3,4000)
print()
print(f"{'m':>5} {'kernelL1(T=12)':>15} {'sup|dG| (operator)':>19} {'ratio op/kern':>14}")
res={}
for m in (4,8,16,32,64,128):
    c,lam=soe_positive(alpha,m)
    ek=kernel_L1_err(alpha,c,lam,T)
    dg=np.array([abs(G_alpha(x)-G_m(x,c,lam)) for x in w])
    op=dg.max()
    res[m]=dict(m_actual=len(c),kernel_L1=float(ek),op_sup=float(op),argmax_w=float(w[dg.argmax()]))
    print(f"{len(c):>5} {ek:>15.6e} {op:>19.6e} {op/ek:>14.4f}")
print()
print("=== fixed-input vs operator: how much of the worst case does each input actually excite? ===")
def spec(uf,N=8192):
    t=np.linspace(0,T,N); u=np.array([uf(x) for x in t])
    U=np.fft.rfft(u)*(T/N); f=np.fft.rfftfreq(N,T/N); return 2*math.pi*f, U
INP={
 "sinusoid": lambda t: math.sin(2*math.pi*t/3.0),
 "multisine": lambda t: (math.sin(2*math.pi*t/6)+math.sin(2*math.pi*t/2)+math.sin(2*math.pi*t/0.8))/3,
 "multiscale": lambda t: (math.sin(2*math.pi*t/12)+0.5*math.sin(2*math.pi*t/4))/1.5,
 "chirp": lambda t: math.sin(2*math.pi*(0.1+0.4*t/T)*t),
 "pulse": lambda t: 1.0 if 1.0<=t<=2.0 else 0.0,
}
# best pwc6 found by R3-F
pw=[0.756699881516397,0.1325216805562377,0.8458247799426317,0.7344822846353054,0.14397935662418604,0.32357181794941425]
def pwc6(t):
    k=min(5,int(t/(T/6))); return 2*pw[k]-1
INP["pwc6_found"]=pwc6
for m in (4,32,128):
    c,lam=soe_positive(alpha,m); mm=len(c)
    dgf=lambda x: abs(G_alpha(x)-G_m(x,c,lam))
    dg=np.array([dgf(x) for x in w]); op=dg.max()
    print(f"\n m={mm}  operator error sup|dG| = {op:.6e}  (at w={w[dg.argmax()]:.4g})")
    print(f"   {'input':>12} {'fixed-input err/||u||2':>23} {'/operator err':>14}")
    for nm,uf in INP.items():
        ww,U=spec(uf)
        sel=(ww>0)&(ww<=w.max())
        d=np.array([dgf(x) for x in ww[sel]])
        num=math.sqrt((np.abs(d*U[sel])**2).sum()); den=math.sqrt((np.abs(U[sel])**2).sum())
        r=num/den
        print(f"   {nm:>12} {r:>23.6e} {r/op:>14.4f}")
json.dump(res,open("r3b_response_semantics_out.json","w"),indent=1)
