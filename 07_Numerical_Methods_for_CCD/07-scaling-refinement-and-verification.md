# Scaling, Refinement, and Verification

## Scaling and initialization

Use scaled variables and residuals,

```{math}
\widehat{z}_i=\frac{z_i-z_i^{\mathrm{ref}}}{s_i},
\qquad
\widehat{g}_j=\frac{g_j}{r_j},
```

so typical magnitudes are comparable. Dynamic defects need state-specific scales because position, velocity, temperature, and rotation have different units.

Useful initial guesses come from baseline simulation, simple boundary interpolation, known operating controls, simplified problems, and nearby parameter cases. Continuation gradually tightens constraints, increases disturbances, activates nonlinear physics, reduces regularization, or refines the mesh while warm-starting from the previous solution.

## Mesh refinement

One mesh is not enough evidence.

![A sequence of refined meshes and log-log convergence curves demonstrating expected first- and second-order accuracy.](imgs/fig_chp7_9.svg)

*Mesh refinement tests whether the reported design is stable under improved approximation.*

- **$h$-refinement:** add intervals, especially near nonsmooth behavior.
- **$p$-refinement:** increase polynomial degree in smooth regions.
- **$hp$-refinement:** combine both based on local smoothness.

Error indicators include model-versus-reconstruction derivative mismatch, low- versus high-order estimates, coefficient decay, constraint overshoot, independent-simulation error, and changes in objective and design.

Monitor several convergence quantities:

```{math}
E_J^{(r)}=\frac{|J^{(r)}-J^{(r-1)}|}{\max(1,|J^{(r)}|)},
\qquad
E_z^{(r)}=\frac{\|\mathbf{z}_d^{(r)}-\mathbf{z}_d^{(r-1)}\|_2}{\max(1,\|\mathbf{z}_d^{(r)}\|_2)},
```

along with maximum defect and path-constraint violation.

## Independent simulation

Reconstruct the optimized control and simulate the original dynamics with a separate high-accuracy integrator. Compare trajectories, terminal values, objectives, and constraints. This reveals insufficient meshes, incorrect defects, inconsistent control interpolation, and hidden violations.

Inspect primal and dual infeasibility, stationarity, complementarity, step acceptance, regularization, and restoration warnings. A solver can terminate because it cannot progress—not because it found a credible optimum.

```{admonition} Verification warning
:class: warning
Small defects at mesh points do not guarantee small continuous-time error. Check reconstructed trajectories between nodes.
```

:::{tip} Activity 7.6: Minimum-Time Control with an Active State Constraint
:class: dropdown

Consider the double integrator

```{math}
\dot{x}_1=x_2,
\qquad
\dot{x}_2=u,
```

with boundary conditions

```{math}
\mathbf{x}(0)=
\begin{bmatrix}
0\\
0
\end{bmatrix},
\qquad
\mathbf{x}(t_f)=
\begin{bmatrix}
1\\
0
\end{bmatrix},
```

and constraints

```{math}
-1\leq u(t)\leq 1,
\qquad
|x_2(t)|\leq 0.6.
```

Minimize

```{math}
J=t_f.
```

1. Derive the optimal-control structure and identify all bang and state-constrained arcs.
2. Compute the switching times and optimal final time analytically.
3. Solve the problem using GPOPS-II or Dymos.
4. Plot $x_1(t)$, $x_2(t)$, and $u(t)$, and mark every switching point.
5. Repeat the numerical solution using 20, 40, and 80 mesh intervals, and report the error in $t_f$.
6. Verify the final solution using independent high-accuracy integration.
:::
