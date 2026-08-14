"""Chief-side lightweight audit of stored Gamma_T values.
Recomputes all 12 cells with n=4000 (vs researcher's n=24000) and reports relative discrepancies.
This is a numerical consistency audit, not a proof certificate.
"""
import importlib.util, os, json
HERE=os.path.dirname(os.path.abspath(__file__))
spec=importlib.util.spec_from_file_location('r2compute', os.path.join(HERE,'compute_B_safe.py'))
r2=importlib.util.module_from_spec(spec); spec.loader.exec_module(r2)
d=json.load(open(os.path.join(HERE,'B_safe_grid.json')))
errs=[]
for c in d['cells']:
    g=r2.gamma_T(c['A'],c['alpha'],d['T_bench'],n=4000)
    rel=abs(g-c['Gamma_T'])/c['Gamma_T']
    errs.append(rel)
    print(f"A={c['A']:.2f} alpha={c['alpha']:.2f} stored={c['Gamma_T']:.12g} audit={g:.12g} rel={rel:.3e}")
print(f"MAX_REL={max(errs):.3e}")
assert max(errs) < 5e-5
print('AUDIT_GAMMA_CONVERGENCE: PASS')
