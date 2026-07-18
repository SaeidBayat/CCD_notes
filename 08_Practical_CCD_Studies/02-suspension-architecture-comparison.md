# Comparing Suspension CCD Architectures

## Fair comparison

Sequential, nested, and simultaneous methods should use the same physical model, scenarios, system objective, bounds, path and boundary constraints, discretization accuracy, and convergence requirements. Initialization effort and solver tolerances should also be comparable. Otherwise, differences may reflect formulation rather than coordination.

## Sequential formulation

A passive-first baseline is

$$
\mathbf{x}_p^{\mathrm{seq}}=\arg\min_{\mathbf{x}_p}J(\mathbf{x}_p,\mathbf{x}_c=0),
$$

$$
\mathbf{x}_c^{\mathrm{seq}}=\arg\min_{\mathbf{x}_c}J(\mathbf{x}_p^{\mathrm{seq}},\mathbf{x}_c).
$$

It answers a practical question: how much value is lost when physical suspension selection precedes active-control design?

## Nested and simultaneous formulations

Nested CCD evaluates each plant under its best achievable controller:

$$
\min_{\mathbf{x}_p}\ \psi(\mathbf{x}_p),\qquad
\psi(\mathbf{x}_p)=\min_{\mathbf{x}_c,\mathbf{x}(\cdot),\mathbf{u}(\cdot)}J(\mathbf{x}_p,\mathbf{x}_c).
$$

The inner problem enforces control and dynamic constraints; the outer problem enforces plant constraints. This is conceptually attractive but potentially expensive.

Simultaneous CCD solves

$$
\min_{\mathbf{x}_p,\mathbf{x}_c,\mathbf{x}(\cdot),\mathbf{u}(\cdot)}J(\mathbf{x}_p,\mathbf{x}_c)
$$

subject to dynamics, plant constraints, path constraints, and controller relations. After transcription, every plant, controller, state, and control variable appears in one sparse nonlinear program.

![Sequential, nested, and simultaneous organizations for the suspension tutorial.](imgs/fig_chp8_4.svg)

## Representative result pattern

![Instructional normalized comparison. Lower system objective is better.](imgs/fig_chp8_5.svg)

With the sequential result normalized to 100, a representative pattern places nested and simultaneous results near 80. These values are instructional, not a reproduction of one dataset. Under ideal conditions, nested and simultaneous formulations can target the same coupled optimum; differences may arise from inner-solve accuracy, local minima, controller restrictions, or numerical tolerances.

Interpretation should examine whether the coordinated plant becomes softer or stiffer, how damping changes, actuator force and energy, active constraints, improvement by objective component, and performance on unseen road profiles. Active control may support passive elements that look unattractive alone but work well in the closed-loop system.

```{admonition} Do not report only the aggregate objective
:class: warning
A weighted value can hide unacceptable tradeoffs. Report individual objective terms, active constraints, trajectories, computation measures, and physical design values.
```
