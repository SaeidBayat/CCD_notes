# Physical System Modeling

## Why modeling matters

Every control problem begins with a model, whether that model is explicit or implicit. Even when a controller is tuned experimentally, the engineer still carries an internal mental model of what the system does. In CCD, the model plays an even larger role: it is the bridge between plant design variables and control design variables.

A good model should be:

- **physically meaningful**, so that design-variable changes have understandable effects;
- **simple enough to analyze and optimize**, especially in early design stages;
- **rich enough to capture the dominant dynamics** that matter for control and performance; and
- **well matched to the decisions being made**. A conceptual design study does not need the same fidelity as a certification-grade simulation.

There is no perfect model. There are only models that are more or less useful for a given decision. The art of dynamic modeling lies in retaining the right physics while excluding details that do not materially affect the design question.

![A modeling workflow that moves from a physical system through assumptions and governing physics to differential equations, a state-space model, analysis, simulation, and design.](imgs/fig_chp2_1.svg)

*A typical modeling workflow for dynamic systems used in CCD and control analysis. The process begins with the physical system and ends with a dynamic model that can be analyzed, simulated, and used for design.*

A common modeling pipeline begins with a physical system and its governing physics. We then make assumptions: rigid body or flexible body? Linear or nonlinear? Lumped parameters or distributed parameters? Small motions or large motions? These assumptions lead to differential equations. Finally, we define states, inputs, outputs, and disturbances and express the model in a convenient form such as state space.

## Levels of model fidelity

Dynamic models are often built at different levels of fidelity:

1. **Conceptual models** capture the dominant energy-storage and dissipation mechanisms. They are excellent for teaching, intuition, and early optimization.
2. **Intermediate models** add realism such as actuator dynamics, sensor dynamics, multiple degrees of freedom, or saturation.
3. **High-fidelity models** incorporate flexible modes, nonlinearities, aerodynamic or hydrodynamic effects, contact, constraints, and implementation details.

Conceptual and intermediate models build the understanding needed to use high-fidelity models responsibly.

## A first example: mass–spring–damper system

The mass–spring–damper system contains nearly every idea we need: inertia, restoring force, damping, actuation, disturbance response, and measurable output.

![A mass connected to a wall by a spring and damper, with displacement x, control force u, and disturbance force d.](imgs/fig_chp2_2.svg)

*A single-degree-of-freedom mass–spring–damper system with a control input and a disturbance.*

Applying Newton's second law gives

```{math}
:label: eq-ch2-msd-second-order
m\ddot{x}(t)+c\dot{x}(t)+kx(t)=u(t)+d(t),
```

where $m$ is mass, $c$ is the damping coefficient, $k$ is spring stiffness, $x(t)$ is displacement, $u(t)$ is the control force, and $d(t)$ is an external disturbance force.

```{admonition} CCD connection
:class: important
Changing $m$, $c$, or $k$ changes the dynamic behavior. Since a controller acts through those dynamics, the best controller also changes. This is the essence of plant–control interaction.
```

:::{tip} Activity 2.1: Full and Reduced Models of a DC Motor
:class: dropdown

An armature-controlled DC motor is modeled by

```{math}
\begin{aligned}
J\dot{\omega}+b\omega&=K_ti-\tau_L,\\
L\dot{i}+Ri&=v-K_e\omega.
\end{aligned}
```

Use

```{math}
J=0.02\ \mathrm{kg\,m^2},
\qquad
b=0.08\ \mathrm{N\,m\,s},
```

and

```{math}
L=0.015\ \mathrm{H},
\qquad
R=1.2\ \Omega,
\qquad
K_t=K_e=0.25.
```

1. Using

   ```{math}
   \mathbf{x}=
   \begin{bmatrix}
   \theta&\omega&i
   \end{bmatrix}^{T},
   ```

   derive the complete state-space model with voltage $v$ as the control input and load torque $\tau_L$ as the disturbance.

2. Derive the characteristic polynomial of the unforced state matrix.

3. Explain why one eigenvalue is located at the origin when shaft position is included as a state.

4. Remove the position state and derive the two-state speed-current subsystem.

5. Prove that the speed-current subsystem is asymptotically stable for positive

   ```{math}
   J,\ b,\ L,\ R,\ K_t,\ K_e.
   ```

6. Set $L\dot{i}\approx0$ and derive the reduced first-order speed model.

7. Derive the reduced-model pole and compare it with the slow eigenvalue of the full speed-current model.

8. Simulate the full and reduced models for a $12$-V step input and zero load torque. Compare:

   1. motor speed;
   2. current;
   3. steady-state speed; and
   4. dominant time constant.

9. Repeat the comparison for

   ```{math}
   L\in\{0.005,\ 0.015,\ 0.08\}\ \mathrm{H}.
   ```

10. Define a quantitative criterion for deciding when the reduced model is acceptable.

11. Explain how changing rotor inertia $J$, inductance $L$, or torque constant $K_t$ changes both plant performance and the control-design problem.
:::
