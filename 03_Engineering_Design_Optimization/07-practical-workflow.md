# A Practical Optimization Workflow

## 1. Define the mission and requirements

State what the system must accomplish, under which operating conditions, and how success will be measured. Do not begin with the solver.

## 2. Choose the design representation

Identify variables and bounds. Confirm that every variable corresponds to a realizable decision and that the representation is not unnecessarily redundant.

## 3. Build and verify the analysis model

Check equations, units, baseline behavior, and sensitivity to variables. An optimizer will exploit every model defect it can find.

## 4. Define objective and constraints

Separate preferences from requirements. Normalize quantities where appropriate and include limits that prevent physically meaningless exploitation.

## 5. Explore before optimizing

Use parameter sweeps, plots, and hand calculations to understand trends. Check smoothness and inspect likely active constraints.

## 6. Scale variables and functions

Bring typical values near order one. Select solver tolerances only after scaling.

## 7. Use more than one initial design

For nonlinear problems, compare several starts. Preserve the initial designs and solver settings for reproducibility.

## 8. Verify the solution

A trustworthy optimum should satisfy every constraint, have an understood termination message, exhibit acceptable optimality residuals, survive small perturbations, have interpretable active constraints, reproduce under independent simulation, and remain credible under higher-fidelity analysis.

## 9. Interpret the engineering result

Ask which variables moved, which constraints became active, what tradeoffs the optimum reveals, how uncertainty affects it, and whether the design is manufacturable, controllable, maintainable, and safe.

```{admonition} Audit checkpoint
:class: tip
For any optimization result, identify the active constraints, termination condition, initial guess, scaling choices, and evidence that the result is not a numerical artifact. Without these items, the result is not fully auditable.
```

## Common formulation and solver mistakes

1. **Choosing dependent or redundant variables**, creating singularity and poor conditioning.
2. **Using an objective that does not reflect the mission.**
3. **Omitting essential constraints**, producing unrealistic optima.
4. **Mixing dimensional constraints with wildly different magnitudes.**
5. **Trusting one initial guess in a nonconvex problem.**
6. **Ignoring derivative quality**, causing false convergence.
7. **Failing to handle simulation failures** in unstable or invalid regions.
8. **Reporting only the objective** rather than the design, margins, trajectories, and diagnostics.
9. **Assuming convergence means correctness.** A solver can converge to an infeasible, poorly scaled, or incorrectly modeled solution.
