# Worked Examples and Comparison

## Example 6.1: active suspension

For a known short road disturbance, OLOC can optimize actuator force $u(t)$ to reduce body acceleration and suspension deflection. This yields a best-case force history for that road profile. The result may reveal when strong actuation is needed. A final controller instead maps measured suspension deflection and body velocity to force, and its gains are tuned or co-designed in closed loop.

## Example 6.2: wind turbine

Optimizing blade-pitch trajectory against a known wind trace gives an ideal load-reduction benchmark. A real turbine does not know the future gust exactly, so an implementable controller uses rotor-speed and load measurements, perhaps with preview. MPC or gain-scheduled feedback is a more realistic final architecture.

## Example 6.3: marine energy device

OLOC can optimize PTO force for a recorded wave sequence and estimate theoretical energy capture. A practical controller must operate from measured or forecast waves. Closed-loop CCD redesigns geometry or PTO hardware together with that realizable controller.

## Comparison

| Approach | Main decision | Strength | Limitation |
| --- | --- | --- | --- |
| Open-loop optimal control | Full trajectory $\mathbf{u}(t)$ | Flexible benchmark | May need unrealistic future information |
| Controller-parameter optimization | Gain or coefficient vector $\mathbf{x}_c$ | Directly implementable | Limited by chosen structure |
| Feedback-controller CCD | Plant and controller parameters | Realistic closed-loop design | More restrictive than free trajectories |
| MPC | Repeated finite-horizon plans | Feedback with constraints and prediction | Requires online optimization and a good model |

## Common mistakes

1. **Confusing a trajectory with a controller.** A planned signal is not a feedback law.
2. **Treating OLOC as automatically implementable.** It may rely on impossible information.
3. **Ignoring the real information set.** Controllers use only measured, estimated, or credibly forecast quantities.
4. **Assuming feedback removes all uncertainty.** Feedback mitigates but does not eliminate noise and mismatch.
5. **Calling MPC purely open loop.** Repeated measurement-based replanning creates feedback.
6. **Assuming parameterized controllers are always inferior.** A realizable feedback policy can outperform a nonimplementable ideal signal on the uncertain real system.
