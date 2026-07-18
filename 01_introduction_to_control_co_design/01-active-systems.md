# Actively Controlled Engineering Systems

## The physical system is only part of the design

An engineering system is **active** when it senses its condition or environment and uses an actuator to modify its behavior. A useful system description contains five interacting elements:

1. **Physical plant:** the object or process being controlled, such as a vehicle suspension, wind turbine, robotic arm, building, aircraft, or energy converter.
2. **Sensors:** devices that measure position, velocity, strain, temperature, pressure, acceleration, current, or other quantities.
3. **Controller:** logic that uses measurements, models, references, and design parameters to determine a command.
4. **Actuators:** devices that convert the command into physical action such as force, torque, heat flow, voltage, valve position, or blade pitch.
5. **Environment:** external conditions and disturbances such as road roughness, wind, waves, payload changes, and uncertain loads.

```{figure} imgs/feedback-block-diagram.svg
:alt: Feedback diagram connecting environment, plant, sensors, controller, and actuator.
:width: 90%
:align: center

A generic actively controlled engineering system. Every block contributes to the behavior of the complete system.
```

```{admonition} Definition
:class: important
An actively controlled engineering system is a physical system whose behavior is intentionally modified using sensing, computation, and actuation.
```

The controller is not an isolated software object. It acts through a physical actuator, receives imperfect measurements from physical sensors, and operates on a plant exposed to disturbances. Sensor bandwidth, actuator limits, power availability, computation, and plant dynamics therefore belong to the same engineering story.

## Plant and control design variables

Engineers choose quantities called **design variables**. In CCD, two broad groups are useful.

Plant design variables $x_p \in \mathbb{R}^{n_p}$ describe the physical system. Examples include:

- geometry, shape, and material;
- mass, inertia, stiffness, and damping;
- gear ratio, generator rating, battery capacity, and actuator size;
- component placement, connections, and architecture; and
- sensor or actuator placement when it changes the physical system.

Control design variables $x_c \in \mathbb{R}^{n_c}$ describe how control action is generated. Examples include:

- PID or state-feedback gains;
- estimator and filter parameters;
- sampling time and model-predictive-control horizon;
- parameters of a control policy; and
- an entire control trajectory $u(t)$ in open-loop optimal control.

The boundary is sometimes context dependent. A sensor can be viewed as hardware, an information-architecture choice, or both. The label is less important than representing how the decision changes dynamics, information, performance, cost, or constraints.

## States, outputs, controls, and disturbances

Let the state, control input, disturbance, and output be

$$
\xi(t) \in \mathbb{R}^{n_s}, \qquad
u(t) \in \mathbb{R}^{n_u}, \qquad
d(t) \in \mathbb{R}^{n_d}, \qquad
y(t) \in \mathbb{R}^{n_y}.
$$

A general state-space model is

$$
\dot{\xi}(t)=f\!\left(t,\xi(t),u(t),x_p,d(t)\right),
$$

$$
y(t)=h\!\left(t,\xi(t),u(t),x_p,d(t)\right).
$$

The physical design $x_p$ appears inside the dynamic model. Changing a mass, dimension, stiffness, aerodynamic shape, or gear ratio changes the equations of motion and can therefore change which controller is best.

```{admonition} Checkpoint
:class: tip
For an active vehicle suspension, identify one plant variable, state, disturbance, sensor output, control input, and system-level performance metric. Then draw arrows showing which quantities directly influence one another.
```
