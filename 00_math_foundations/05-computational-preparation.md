---
numbering: false
---

# 0.5 Computational Preparation and Readiness Project

CCD studies combine mathematical models with numerical simulation and optimization. You do not need advanced software-development experience to begin, but you should be comfortable reading and modifying short computational scripts.

## Minimal MATLAB or Python preparation

Before continuing, you should be able to:

- define scalars, vectors, and matrices;
- write and call a simple function;
- evaluate a mathematical formula;
- simulate an ODE numerically;
- plot a result; and
- compute a discrete objective function.

## A simple computational workflow

A basic modeling study follows a repeatable sequence:

1. Define parameters and initial conditions.
2. Write the model equations.
3. Simulate the model and plot the results.
4. Evaluate one or more performance measures.
5. Refine the model, parameters, or numerical settings.

```{figure} imgs/fig_chp0_8.svg
:alt: Define parameters, write model equations, simulate and plot, evaluate performance, and refine.
:width: 96%
:align: center

A basic workflow for modeling and simulation. Later CCD workflows add optimization solvers, gradient computation, uncertainty studies, and validation.
```

## Python example

The following script defines a mass–spring–damper model and integrates it numerically. It is a preparation exercise rather than a full CCD implementation.

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

m = 1.0
c = 0.4
k = 4.0


def model(t, x):
    u = 1.0
    x1, x2 = x
    dx1 = x2
    dx2 = -(k / m) * x1 - (c / m) * x2 + (1 / m) * u
    return [dx1, dx2]


sol = solve_ivp(model, [0, 10], [0, 0], max_step=0.02)

plt.plot(sol.t, sol.y[0, :])
plt.xlabel("time")
plt.ylabel("displacement")
plt.show()
```

The script performs four basic tasks:

- specifies the model parameters $m$, $c$, and $k$;
- defines the first-order state equations;
- integrates the equations from an initial state; and
- plots the displacement trajectory.

## MATLAB example

An analogous MATLAB script is

```matlab
m = 1.0;
c = 0.4;
k = 4.0;

f = @(t,x) [x(2);
           -(k/m)*x(1) - (c/m)*x(2) + 1/m];

[t,x] = ode45(f,[0 10],[0;0]);

plot(t,x(:,1))
xlabel('time')
ylabel('displacement')
```

Both implementations express the same mathematical model. The syntax differs, but the modeling workflow is unchanged.

## Computing a discrete performance measure

Suppose the continuous control-effort objective is

$$
J=\int_0^T u(t)^2\,dt.
$$

After sampling $u(t)$ on a time grid, a trapezoidal approximation can be computed in Python with

```python
J = np.trapezoid(u**2, t)
```

or in MATLAB with

```matlab
J = trapz(t, u.^2);
```

This simple pattern—simulate a trajectory, compute a performance measure, and compare alternatives—later becomes part of a numerical optimization loop.

## Readiness mini-project

Before moving to Chapter 1, model and simulate a mass–spring–damper system and identify how its quantities would appear in a CCD formulation.

### Suggested tasks

1. Choose values for $m$, $c$, and $k$.
2. Write the second-order ODE and convert it to first-order state-space form.
3. Select initial conditions and a force input $u(t)$.
4. Simulate displacement and velocity.
5. Plot both state trajectories.
6. Compute at least one performance measure, such as peak displacement, RMS displacement, or control effort.
7. Explain which quantities could become decision variables and which conditions could become constraints.

### Connection to a CCD formulation

| CCD element | Mass–spring–damper example |
|---|---|
| Plant variables | $m$, $c$, and $k$ |
| Control variables | Force-input history or controller gains |
| States | Displacement and velocity |
| Possible objectives | Vibration suppression, control effort, or a weighted combination |
| Possible constraints | Actuator-force limits, displacement bounds, or parameter bounds |

:::{admonition} Readiness checkpoint
:class: tip
If you can read vectors and matrices, compute simple derivatives and integrals, convert a second-order ODE to first-order form, understand the parts of an optimization problem, and follow a short simulation script, you are ready for the main body of the course.
:::

:::{tip} Activity 0.6: State and Parameter Sensitivities for a Readiness Mini-Project
:class: dropdown

Consider the mass-spring-damper system

```{math}
m\ddot{q}+c\dot{q}+kq=u(t),
```

with

```{math}
m=1,
\qquad
q(0)=1,
\qquad
\dot{q}(0)=0,
\qquad
u(t)=e^{-t}.
```

The plant parameters and state vector are

```{math}
\mathbf{p}=\begin{bmatrix}k\\c\end{bmatrix},
\qquad
\mathbf{x}=\begin{bmatrix}q\\v\end{bmatrix}.
```

Define the performance measure

```{math}
J(k,c)=\frac{1}{2}\int_0^5\left(q(t)^2+0.1v(t)^2\right)dt
+0.01k^2+0.02c^2.
```

1. Derive the state-space model

   ```{math}
   \dot{\mathbf{x}}=\mathbf{f}(\mathbf{x},\mathbf{p},t).
   ```

2. Define the parameter-sensitivity vectors

   ```{math}
   \mathbf{s}_k=\frac{\partial\mathbf{x}}{\partial k},
   \qquad
   \mathbf{s}_c=\frac{\partial\mathbf{x}}{\partial c}.
   ```

3. Derive the sensitivity equations

   ```{math}
   \dot{\mathbf{s}}_j=
   \frac{\partial\mathbf{f}}{\partial\mathbf{x}}\mathbf{s}_j
   +\frac{\partial\mathbf{f}}{\partial p_j},
   \qquad
   j\in\{k,c\}.
   ```

4. Derive the initial conditions for both sensitivity vectors.

5. Derive $\partial J/\partial k$ and $\partial J/\partial c$ in terms of the state and sensitivity trajectories.

6. Simulate the state and sensitivity equations simultaneously at

   ```{math}
   k=4,
   \qquad
   c=0.8.
   ```

7. Verify both derivatives using central finite differences.

8. Investigate the finite-difference error for

   ```{math}
   h\in\{10^{-2}, 10^{-4}, 10^{-6}, 10^{-8}\}.
   ```

9. Use the computed gradient to perform ten steepest-descent iterations with a backtracking line search, subject to

   ```{math}
   0.5\leq k\leq10,
   \qquad
   0.05\leq c\leq4.
   ```

10. Report the final design, objective value, gradient norm, and state response.

11. Explain how this mini-project combines the main prerequisite topics of Chapter 0 and prepares students for later CCD formulations.
:::
