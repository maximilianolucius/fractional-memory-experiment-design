# Manifest

solver: fractional_solver_PECE
status: DONE
solver_tolerances:
  status: DONE
  spec: |
    The fractional solver (PECE) has been implemented and gates 1,3,4 have been tested.
    Gate 2 (equilibrium time) test exists and clarification on the analytical expression has been provided.
    Gates 5 (controllability range), 6 (observability range), and 7 (step refinement and independent re-simulation) are now implemented.
    Tolerances: gate1 at 12 digits, gates 2-6 at 1e-6, gate7 at 1e-6.