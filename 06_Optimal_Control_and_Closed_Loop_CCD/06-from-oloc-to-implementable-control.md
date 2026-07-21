# From OLOC to Implementable Control

A productive development path is:

1. solve an ideal OLOC problem;
2. study its control patterns and performance;
3. choose a realizable controller structure that captures the important behavior; and
4. co-design the plant with that implementable controller.

![A workflow from open-loop optimization and insight extraction through controller selection, closed-loop co-design, validation, and implementation.](imgs/fig_chp6_8.svg)

*An ideal trajectory can guide—but should not be confused with—the final controller.*

## What OLOC can teach us

An optimal trajectory can reveal:

- when control action should be active;
- whether it behaves like stiffness, damping, or phase lead;
- required control bandwidth and authority; and
- which physical plant properties are most valuable.

## Typical transitions

- OLOC $\rightarrow$ PID or gain-scheduled feedback.
- OLOC $\rightarrow$ LQR or state feedback.
- OLOC $\rightarrow$ MPC.
- OLOC $\rightarrow$ a rule-based controller informed by optimal behavior.
- OLOC $\rightarrow$ a parameterized policy fitted to optimal trajectories.

OLOC remains valuable because it supplies a best-case reference, explains ideal behavior, benchmarks practical controllers, and helps separate plant limitations from controller limitations. It is often best treated as an intermediate design-analysis tool.

## A three-stage design framework

One way to operationalize the OLOC-to-implementable-control transition is a three-stage process developed for dynamic-system architecture design:

1. **Stage 1 — plant architecture design, co-designed with OLC.** The physical architecture and its design variables are optimized together with an unrestricted control trajectory $\mathbf{u}(t)$. No actuator or control-architecture assumptions are made, so this stage searches the broadest design space and produces a system-optimal benchmark plant.
2. **Stage 2 — controller architecture design, co-designed with CLC.** A specific, implementable control architecture (for example, full-state feedback with optimized gains) is selected, and the plant is re-optimized jointly with that controller's finite-dimensional parameter vector.
3. **Stage 3 — digital controller design.** The continuous-time control law produced in Stage 2 is realized as a digital controller, addressing sampling, discretization, and computation.

Mechanical engineers typically own Stage 1, while control engineers own Stages 2 and 3. Iteration between stages—and revision of a stage's own formulation—is expected as insights from later stages feed back into earlier ones.

### A worked progression: semi-active suspension

A trailing-arm quarter-car suspension study shows how performance degrades, in a controlled and explainable way, as each stage adds a layer of realism. Each row below is informed by the solution of the previous one:

| Problem | Control representation | $\Phi_*$ | Change |
| --- | --- | --- | --- |
| P0 — passive | fixed linear damping, no active or semi-active control | $5.80\times10^{-4}$ | an idealized passive benchmark that cannot actually be realized, because underlying geometric nonlinearities keep true passive damping nonlinear |
| P1 — active OLC | unrestricted actuator force $u(t)$ (Stage 1) | $2.06\times10^{-4}$ | benchmark: best achievable performance with no actuator or architecture restriction |
| P2 — semi-active OLC, ideal damper | force restricted to always dissipate energy, $F(u)=-u(t)\,(\dot z_s-\dot z_{us})$, $u(t)\geq0$ | $3.72\times10^{-4}$ | about $1.80\times$ worse than P1 |
| P3 — semi-active OLC, realistic MR-damper model | current-to-force map $F(I,\dot z_s-\dot z_{us})$ identified from a physical damper | $9.58\times10^{-4}$ | about $2.57\times$ worse than P2 |
| P4 — semi-active CLC, full-state feedback (Stage 2) | optimized feedback gains $\mathbf{K}$ acting on measured/estimated states, damper current $I(t)$ as the physical output, $0\leq\mathbf{K}\boldsymbol{\xi}(t)\leq1$ | $2.00\times10^{-3}$ | about $2.08\times$ worse than P3; about $9.70\times$ worse than the P1 benchmark |

The P2 solution was used to select and size an actual component: a Lord 8041-1 magnetorheological (MR) damper, with a continuous current operating range of 0-1 A and a maximum stroke of 74 mm. That damper's hysteretic, current-dependent force-velocity behavior was characterized in the laboratory to build the P3 surrogate model, $F(I,\dot z_s-\dot z_{us})$. In P4, all states were assumed measurable—mass accelerations from accelerometers, relative displacements from linear encoders, and velocities obtained by integrating the acceleration signals—and the feedback gains were optimized subject to the damper's saturation limits. No single step in P1 $\to$ P4 involved a design mistake: each one simply removed an assumption (unlimited actuator authority, an idealized semi-active component, or unlimited state/future information) that a real system cannot provide, and the resulting performance gap is the accumulated cost of implementability.

:::{tip} Activity 6.6: Converting an OLOC Trajectory into TVLQR Feedback
:class: dropdown

Consider a torque-controlled pendulum. Let $\theta=0$ denote the upright position and $\theta=\pi$ the downward position.

The dynamics are

```{math}
\dot{\theta}=\omega,
\qquad
\dot{\omega}
=\frac{g}{l}\sin\theta
-\frac{b}{ml^2}\omega
+\frac{1}{ml^2}u.
```

Use

```{math}
m=1\ \mathrm{kg},
\qquad
l=1\ \mathrm{m},
\qquad
b=0.05\ \mathrm{N\,m\,s},
```

and

```{math}
g=9.81\ \mathrm{m/s^2},
\qquad
|u(t)|\leq8\ \mathrm{N\,m}.
```

The boundary conditions are

```{math}
\mathbf{x}(0)=
\begin{bmatrix}
\pi\\
0
\end{bmatrix},
\qquad
\mathbf{x}(4)=
\begin{bmatrix}
0\\
0
\end{bmatrix}.
```

Minimize

```{math}
J=
\int_0^4
\left(
0.001\omega(t)^2
+
0.01u(t)^2
\right)dt.
```

1. Solve the swing-up OLOC problem using GPOPS-II or Dymos.

2. Denote the optimal trajectory by

   ```{math}
   \mathbf{x}^*(t),
   \qquad
   u^*(t).
   ```

   Linearize the dynamics along the optimal trajectory and show that

   ```{math}
   A(t)=
   \begin{bmatrix}
   0&1\\
   \dfrac{g}{l}\cos\theta^*(t)&-\dfrac{b}{ml^2}
   \end{bmatrix},
   \qquad
   B(t)=
   \begin{bmatrix}
   0\\
   \dfrac{1}{ml^2}
   \end{bmatrix}.
   ```

3. Solve the time-varying Riccati equation

   ```{math}
   -\dot{S}=A^TS+SA-SBR^{-1}B^TS+Q,
   ```

   with terminal condition

   ```{math}
   S(4)=Q_f.
   ```

4. Implement the trajectory-tracking controller

   ```{math}
   u(t)=
   \operatorname{sat}
   \left[
   u^*(t)
   -R^{-1}B(t)^TS(t)
   \left(\mathbf{x}(t)-\mathbf{x}^*(t)\right)
   \right].
   ```

5. Compare pure open-loop implementation and TVLQR feedback for the perturbed initial conditions

   ```{math}
   \theta(0)=\pi+\Delta\theta,
   \qquad
   \Delta\theta\in\{-0.15,-0.10,0.10,0.15\}.
   ```

6. Repeat with

   ```{math}
   10\%\ \text{error in }m,
   \qquad
   10\%\ \text{error in }l,
   ```

   and additive measurement noise.

7. Report

   ```{math}
   \|\mathbf{x}(4)\|_2,
   \qquad
   \max_t|u(t)|,
   \qquad
   J.
   ```

8. Determine the largest initial perturbation for which the TVLQR controller successfully reaches the upright neighborhood

   ```{math}
   |\theta(4)|\leq0.05,
   \qquad
   |\omega(4)|\leq0.1.
   ```

9. Explain why the OLOC trajectory remains valuable even though it is not robust enough for direct implementation.
:::
