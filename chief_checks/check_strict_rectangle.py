#!/usr/bin/env python3
"""Lightweight reviewer-side check of Theorem T17 strict face conditions.

This is NOT a new benchmark campaign.  It evaluates the four worst-case
inward-pointing inequalities for the benchmark diagnostic rectangle at the
representative A=0.25, prey-only input |u|<=0.10 and locked ecological
parameters used in the manuscript.
"""

A = 0.25
r, K, a, h, e, mort = 1.5, 1.0, 1.0, 0.5, 0.8, 0.4
u_max = 0.10

# Coexistence equilibrium from predator nullcline.
x_star = mort / (a * (e - mort*h))
# prey nullcline: y = (1+hx)/a * r(1-x/K)(x/A-1)
y_star = (1+h*x_star)/a * r*(1-x_star/K)*(x_star/A-1)

xL = max(A + 0.02, 0.5*x_star)
xU = 1.6*x_star
yL = max(1e-3, 0.4*y_star)
yU = 1.9*y_star

def f1(x,y,u=0.0):
    return r*x*(1-x/K)*(x/A-1) - a*x*y/(1+h*x) + u

def f2(x,y):
    return e*a*x*y/(1+h*x) - mort*y

# For prey-only additive actuation, sufficient worst-case checks on faces:
# lower x face: min over y and u = -u_max -> y=yU
# upper x face: max over y and u = +u_max -> y=yL
# lower y face: min over x -> x=xL
# upper y face: max over x -> x=xU
margins = {
    'lower_prey_min_F1': f1(xL, yU, -u_max),
    'upper_prey_minus_max_F1': -f1(xU, yL, +u_max),
    'lower_predator_min_F2': f2(xL, yL),
    'upper_predator_minus_max_F2': -f2(xU, yU),
}

print(f'x*= {x_star:.12f}, y*= {y_star:.12f}')
print(f'R = [{xL:.12f},{xU:.12f}] x [{yL:.12f},{yU:.12f}]')
for k,v in margins.items():
    print(f'{k}: {v:+.12f}')

strict_pass = all(v > 0 for v in margins.values())
print('STRICT_T17_FACE_TEST:', 'PASS' if strict_pass else 'FAIL')
if strict_pass:
    print('Uniform strict inward margin eta may be chosen below', min(margins.values()))
else:
    print('Do not label this rectangle invariant/certified under the full +/-0.10 budget.')
