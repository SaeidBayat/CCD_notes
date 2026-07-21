# From Optimization to Implementable Hardware

A numerical optimum is an idealized mathematical object. Implementation requires physical dimensions and components, a digital controller, sensor and estimator specifications, real-time software, communications, and safe saturation and fault behavior.

![A staged path from optimization to hardware.](imgs/fig_chp8_9.svg)

## Constraints to model

A closed-loop CCD formulation should consider:

- actuator saturation, rate, stroke, bandwidth, and efficiency;
- sampling and computational delay;
- sensor bandwidth, resolution, bias, and noise;
- state-estimation dynamics;
- anti-windup and saturation logic;
- electrical power and thermal limits;
- quantization and communications; and
- behavior when control is disabled.

```{admonition} Passive safety
:class: tip
When sensing, computation, or actuation fails, the passive plant should remain stable and avoid catastrophic behavior. The resulting constraints may reduce nominal performance but improve deployability.
```

## Controller realization

An open-loop optimal trajectory can inform a realizable controller but normally should not be implemented directly unless future inputs are known. Practical transitions include fitting low-order feedback to optimal trajectories, gain scheduling, embedding the problem in MPC, identifying switching or feedforward rules, and simplifying learned policies under explicit safety constraints.

## A physical example: from open-loop control to a laboratory MR damper

One suspension study made the transition from open-loop optimal control (OLC) trajectories to closed-loop control (CLC) concrete using a physical, reconfigurable trailing-arm suspension testbed whose geometric plant variables could be adjusted on the bench. The design process moved through a sequence of increasingly realistic and increasingly constrained control representations, each solved with the same road input and an objective that minimized sprung-mass acceleration and tire deflection: an unstructured active-force open-loop trajectory gave the best possible, but unrealizable, performance benchmark; a semi-active open-loop damping-force trajectory — assuming an idealized damper able to supply any commanded force at a given velocity — came reasonably close to that benchmark; a semi-active open-loop current trajectory, constrained to the current-versus-force-versus-velocity behavior of a specific, laboratory-characterized magnetorheological (MR) damper, performed measurably worse than the idealized semi-active case because real MR dampers are hysteretic and can only dissipate, not supply, energy; and finally a full-state feedback controller acting on that same MR damper gave the most realizable, but least performant, design in the sequence.

The actuator selected for the physical build was a Lord 8041-1 MR damper, operated over a 0–1 A continuous current range with a maximum stroke of 74 mm. Its force–velocity–current behavior was characterized experimentally in the laboratory and fit with a smooth surrogate model before being used as a hard constraint in both the open-loop and closed-loop problems. Each step in this sequence traded some performance for realizability, and the overall pattern — ideal active, then idealized semi-active, then structured semi-active with a real component model, then closed-loop feedback — is a template for moving any CCD result from an idealized optimal-control benchmark toward a design that can be built and tested.

```{admonition} Bench validation closes the loop
:class: tip
A physical, reconfigurable testbed lets each stage of this sequence be checked against hardware rather than only against a higher-fidelity simulation. Reconfigurable geometric plant variables on the bench let the same optimization formulation drive both the numerical study and the physical build.
```

## Validation stages

A staged campaign can proceed through:

1. software-in-the-loop simulation;
2. Monte Carlo uncertainty tests;
3. processor-in-the-loop or real-time execution;
4. hardware-in-the-loop testing;
5. component bench tests;
6. scaled or full prototypes; and
7. field validation.

Each stage should address a named modeling or implementation risk and use predefined acceptance criteria.

:::{tip} Activity 8.5: From Optimized Suspension to Implementable Hardware
:class: dropdown

Use the optimized active-suspension design from Activity 8.1. Replace the ideal implementation with the sampled-data controller

```{math}
f_{c,k}=\operatorname{sat}\!\left[-K\widehat{\mathbf{x}}_k,F_{\max}\right],
```

which is updated every $T_s$ seconds and held constant between updates. The sensor measurements satisfy

```{math}
\mathbf{y}_k=C\mathbf{x}_k+\mathbf{v}_k,
```

where $\mathbf{v}_k$ is zero-mean measurement noise. The command is delayed by $n_d$ sampling intervals, and the actuator also satisfies

```{math}
|\dot{f}_a|\leq R_{\max}.
```

1. Derive a discrete-time model using zero-order hold.

2. Construct a state observer or Kalman filter for the available measurements.

3. Implement the delayed command

   ```{math}
   f_{c,k}^{\mathrm{applied}}=f_{c,k-n_d}.
   ```

4. Impose the actuator-rate limit using

   ```{math}
   |f_{a,k+1}-f_{a,k}|\leq R_{\max}T_s.
   ```

5. Evaluate

   ```{math}
   T_s\in\{0.001, 0.005, 0.01, 0.02, 0.05\}\ \mathrm{s}
   ```

   and

   ```{math}
   n_d\in\{0, 1, 2, 5\}.
   ```

6. Determine the largest sampling time and delay for which all path constraints remain satisfied.

7. Add a passive-safety requirement: when the actuator is disabled, the passive suspension must satisfy

   ```{math}
   |z_s-z_u|\leq0.10\ \mathrm{m}.
   ```

8. Re-optimize the plant and controller while including sampling time, command delay, observer dynamics, force-rate limits, and passive safety.

9. Compare the ideal and implementable CCD designs in terms of

   ```{math}
   J,\quad k_s,\quad c_s,\quad F_{\max},\quad \text{constraint margin}.
   ```

10. Design a software-in-the-loop, hardware-in-the-loop, and bench-test validation sequence for the final design.
:::
