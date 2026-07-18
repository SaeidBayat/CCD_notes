# States, Inputs, Outputs, and Disturbances

## States

A **state** is the minimum information needed at time $t$ so that, together with future inputs, we can predict future behavior. Dynamic systems have memory; the state records the information needed to represent that memory.

For many mechanical systems, positions and velocities are natural states. For electrical systems, currents and voltages across energy-storing elements are common states. For thermal systems, temperatures may be states.

For the mass–spring–damper example, a convenient state choice is

```{math}
x_1(t)=x(t), \qquad x_2(t)=\dot{x}(t).
```

These two variables are sufficient to predict future motion when future inputs are known.

## Inputs

An **input** is a signal that can influence the system. In control problems, we usually distinguish between:

- **control inputs**, which are commanded by the controller; and
- **exogenous inputs**, such as disturbances or reference signals.

For the mass–spring–damper system, $u(t)$ is the control input and $d(t)$ is a disturbance. For a vehicle, steering angle or brake torque may be control inputs, while road irregularities and wind gusts are disturbances.

## Outputs

An **output** is a quantity we care to measure, estimate, regulate, track, or report. Outputs do not need to equal states. Sometimes an output is a state, such as position. Sometimes it is a combination of states, such as acceleration or strain.

A suspension designer may care about body acceleration, tire deflection, and suspension travel. A wind-turbine designer may care about rotor speed, generated power, and tower-base bending moment. These are outputs because they relate to performance and constraints.

## Disturbances

A **disturbance** is an external influence that affects the dynamics but is not under direct control. Disturbances may be measurable, partially measurable, or unmeasurable. Typical examples include road bumps, wave excitation, wind variations, payload changes, and unmodeled loads.

Disturbance rejection is one of the main reasons feedback is valuable. If disturbances were absent and the model were exact, open-loop control would often be enough. Real systems are rarely that kind.

## Examples from engineering systems

| System | Possible states | Control inputs | Outputs of interest | Disturbances |
| --- | --- | --- | --- | --- |
| Mass–spring–damper | Displacement, velocity | Force $u$ | Displacement, velocity, acceleration | External force |
| Active suspension | Body and wheel positions and velocities | Actuator force | Ride comfort, road holding, suspension travel | Road profile |
| Robot arm | Joint angles, joint rates | Motor torques | End-effector position, tracking error | Payload changes, contact forces |
| Wind turbine | Rotor speed, structural states, actuator states | Pitch angle, generator torque | Power, loads, speed regulation | Wind speed and turbulence |
| Marine energy device | Heave and pitch states, PTO states | PTO force or damping command | Absorbed power, motions, loads | Wave excitation |

```{admonition} Key idea
:class: tip
States describe the system's internal memory. Inputs influence the system. Outputs are what we monitor or care about. Disturbances are external influences that alter behavior. CCD depends on identifying these quantities clearly because plant and control decisions can change them.
```
