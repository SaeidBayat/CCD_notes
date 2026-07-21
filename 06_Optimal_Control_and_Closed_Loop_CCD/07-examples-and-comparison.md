# Examples and Comparison

## Example 6.1: active suspension

For a known short road disturbance, OLOC can optimize actuator force $u(t)$ to reduce body acceleration and suspension deflection. This yields a best-case force history for that road profile. The result may reveal when strong actuation is needed. A final controller instead maps measured suspension deflection and body velocity to force, and its gains are tuned or co-designed in closed loop.

## Example 6.2: wind turbine

Optimizing blade-pitch trajectory against a known wind trace gives an ideal load-reduction benchmark. A real turbine does not know the future gust exactly, so an implementable controller uses rotor-speed and load measurements, perhaps with preview. MPC or gain-scheduled feedback is a more realistic final architecture.

## Example 6.3: marine energy device

OLOC can optimize PTO force for a recorded wave sequence and estimate theoretical energy capture. A practical controller must operate from measured or forecast waves. Closed-loop CCD redesigns geometry or PTO hardware together with that realizable controller.

## Example 6.4: prediction horizon and architecture complexity in a quarter-car study

A study of six quarter-car active-suspension architectures makes the OLOC-versus-MPC trade-off concrete. Each architecture connects the road input to a single translational-force actuator through a different number of auxiliary masses, springs, and dampers—from a control-only case with no additional plant design variables up to a six-design-variable architecture. All six architectures share the objective

```{math}
\psi_d=\int_{t_0}^{t_f}
\left(
w_1(z_U-\delta)^2
+w_2\ddot z_S^2
+w_3F^2
\right)dt,
```

combining road-handling performance, passenger comfort (sprung-mass acceleration), and a control-effort penalty. For each architecture, the plant variables and the controller's prediction horizon $p$ are optimized together in a nested CCD loop—once with OLOC in the inner loop, and once with MPC at $p=40,\,10,\,5$ for a fixed control sampling time.

Two findings stand out:

- **Plant complexity cannot fully substitute for information.** Moving from a simple two-design-variable architecture to the richest six-design-variable architecture markedly improves the open-loop and long-horizon objective values. Yet even the richer plant, evaluated with a short prediction horizon, remains far from its own open-loop bound—while still outperforming the simpler architecture operating fully open loop. A more sophisticated plant design can partially compensate for limited prediction capability, but the controller's information horizon remains a first-order factor, not a detail to optimize last.
- **Disturbance frequency amplifies the OLOC/MPC gap.** At low road-disturbance frequencies (around 2 Hz), OLOC- and MPC-based co-design produce objective values within about 4-5% of each other and nearly identical optimized plant designs. As the disturbance frequency rises toward 20 Hz, the objective-value gap exceeds 18% and the relative difference between the two optimized plant designs grows to roughly 650%. Faster disturbance content relative to the controller's update rate makes the prediction-horizon and sampling-time choices matter far more.

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
7. **Treating the MPC prediction horizon as fixed.** Prediction horizon and control sampling time can be optimized alongside plant variables in a nested CCD loop; treating them as fixed implementation details after the fact overlooks a first-order design choice.
