"""
R3-F Stage 2 — run the actual BIC classifier on the Pareto-frontier candidates found in Stage 1,
plus the six historical designs as controls, at the SAME amplitude (U_cap=0.10) and with the same
seeds/scoring as v3/v4. Deterministic J is reported alongside so the two metrics can be compared.
"""
import json, os, sys, time, itertools
import numpy as np
from multiprocessing import Pool
from scipy.optimize import minimize_scalar
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core, designs, bench
import r3f_safe_design_search as R

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "artifacts")
CAND = ["ODE", "Caputo", "DDE", "latent3"]
A_LIST, T, N, AMP = [0.20, 0.25], 12.0, 400, 0.10
TSAMP = designs.sample_times(T)
def _tc(m): return "latent3" if m in ("latent1","latent3") else m

def fit(model, data, A, uf, C, amp):
    def sse(param):
        kw={}
        if model=="Caputo": kw["alpha"]=param
        elif model=="DDE": kw["tau"]=param
        elif model=="latent3": kw["lam"]=(param,param*1.6,param*0.6)
        _,tr=bench.sim_nonlinear(model,A,kw.get("alpha",0.9),uf,T,N,tau=kw.get("tau",bench.DDE_TAU),
                                 lam=kw.get("lam",bench.LAT_RATES),amp=amp)
        mu=(C@bench._sample(np.linspace(0,T,N+1),tr,TSAMP).T).T.flatten()
        return np.inf if not np.all(np.isfinite(mu)) else float(np.sum((data-mu)**2))
    if model=="ODE": return sse(None),0
    b={"Caputo":(0.55,0.999),"DDE":(0.05,0.8),"latent3":(0.2,3.0)}[model]
    r=minimize_scalar(sse,bounds=b,method="bounded",options={"xatol":2e-2,"maxiter":20})
    return float(r.fun),1

def cell(arg):
    tag, kind, order, params, true_m, A, alpha, obs, snr, reps, seed0 = arg
    uf = designs.INPUTS[params] if kind=="hist" else R.make_input(kind, order, np.asarray(params))
    C = designs.CHANNELS[obs]
    tsf, tr = bench.sim_nonlinear(true_m, A, alpha, uf, T, N, amp=AMP)
    saf = bench.safety_metrics(tr, A)
    if bench.diverged(tr):
        return {"tag":tag,"true":true_m,"A":A,"obs":obs,"snr":snr,"diverged":True,
                "selected":{c:0 for c in CAND},"acc":None,"margin":saf.get("allee_margin")}
    clean=(C@bench._sample(tsf,tr,TSAMP).T).T.flatten()
    sigma=designs.noise_sigma(clean,designs.SNR_DB[snr])
    conf={c:0 for c in CAND}; cor=0
    for r in range(reps):
        rng=np.random.default_rng(seed0+r); data=clean+rng.normal(0,sigma,clean.shape)
        bics=[]
        for c in CAND:
            s_,k=fit(c,data,A,uf,C,AMP); n=data.size
            bics.append(np.inf if not np.isfinite(s_) else k*np.log(n)-2*(-0.5*n*np.log(2*np.pi*sigma**2)-0.5*s_/sigma**2))
        b=np.asarray(bics,float)
        if not np.any(np.isfinite(b)): continue
        b[~np.isfinite(b)]=np.inf; sel=CAND[int(np.argmin(b))]; conf[sel]+=1
        if sel==_tc(true_m): cor+=1
    used=sum(conf.values())
    return {"tag":tag,"true":true_m,"A":A,"obs":obs,"snr":snr,"diverged":False,
            "selected":conf,"acc":(cor/used) if used else None,"margin":saf.get("allee_margin")}

if __name__=="__main__":
    workers=int(sys.argv[1]) if len(sys.argv)>1 else 100
    reps=int(sys.argv[2]) if len(sys.argv)>2 else 100
    top=json.load(open(os.path.join(OUT,"r3f_top12.json")))
    cands=[("SEARCH#%d_%s"%(i,c["family"]), c["family"].rstrip("0123456789"),
            int("".join(ch for ch in c["family"] if ch.isdigit())), c["params"], c["J"], c["min_margin"])
           for i,c in enumerate(top[:6])]
    hist=[("HIST_"+n,"hist",0,n,None,None) for n in ["multiscale","pulse","prbs","multisine","sinusoid","chirp"]]
    jobs=[]; k=0
    for tag,kind,order,params,J,mg in cands+hist:
        p = params if kind!="hist" else params
        for tm in designs.TRUE_MODELS:
            for A in A_LIST:
                for obs in ["prey","both"]:
                    for snr in ["hi","med"]:
                        for a in ([0.70,0.85,0.95] if tm=="Caputo" else [0.90]):
                            jobs.append((tag, kind if kind!="hist" else "hist", order,
                                         p if kind!="hist" else p, tm, A, a, obs, snr, reps,
                                         1000+7919*k+int(a*100))); k+=1
    print("Stage 2: %d cells (%d designs), reps=%d, workers=%d"%(len(jobs),len(cands+hist),reps,workers),flush=True)
    t0=time.time(); res=[]
    with Pool(workers) as pool:
        for i,r in enumerate(pool.imap_unordered(cell,jobs,chunksize=2)):
            res.append(r)
            if i%200==0: print("  %d/%d (%.0fs)"%(i,len(jobs),time.time()-t0),flush=True)
    json.dump(res,open(os.path.join(OUT,"r3f_stage2.json"),"w"))
    # aggregate per design
    summ={}
    for tag in sorted(set(r["tag"] for r in res)):
        sub=[r for r in res if r["tag"]==tag and not r["diverged"] and r["acc"] is not None]
        allc=[r for r in res if r["tag"]==tag]
        if not sub: continue
        conf={t:{c:0 for c in CAND} for t in set(_tc(m) for m in designs.TRUE_MODELS)}
        tot=cor=0
        for r in sub:
            u=sum(r["selected"].values()); tot+=u; cor+=r["selected"].get(_tc(r["true"]),0)
            for c in CAND: conf[_tc(r["true"])][c]+=r["selected"][c]
        rec={c:(conf[c][c]/sum(conf[c].values()) if sum(conf[c].values()) else None) for c in CAND}
        margins=[r["margin"] for r in allc if r["margin"] is not None]
        summ[tag]={"micro":cor/tot if tot else None,
                   "macro":float(np.mean([v for v in rec.values() if v is not None])),
                   "recall":rec,"min_margin":min(margins) if margins else None,
                   "cross_rate":float(np.mean([1 if (m is not None and m<0) else 0 for m in margins])) if margins else None,
                   "n_cells":len(sub),"n_diverged":sum(1 for r in allc if r["diverged"])}
    for tag,c in zip([x[0] for x in cands],[x for x in cands]):
        if tag in summ: summ[tag]["J_stage1"]=c[4]; summ[tag]["margin_stage1"]=c[5]
    json.dump(summ,open(os.path.join(OUT,"r3f_stage2_summary.json"),"w"),indent=1)
    print("\n%-24s %7s %7s %8s %9s %s"%("design","macro","micro","min_marg","cross","J"),flush=True)
    for tag,s in sorted(summ.items(),key=lambda kv:-(kv[1]["macro"] or 0)):
        print("%-24s %7.4f %7.4f %8.3f %9.2f %s"%(tag,s["macro"],s["micro"],s["min_margin"] or 0,
              s["cross_rate"] or 0, ("%.2f"%s["J_stage1"]) if "J_stage1" in s else "-"),flush=True)
    print("DONE",flush=True)
