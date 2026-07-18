# Simultaneous Control Co-Design

Simultaneous CCD optimizes plant, controller, and often trajectory variables in one integrated problem.

![Plant, controller, state, and control-trajectory decisions entering one simultaneous optimization block.](imgs/fig_chp5_5.svg)

*All coupled decisions are optimized together.*

A generic continuous-time statement is

```{math}
\underset{\mathbf{x}_p,\mathbf{x}_c,\mathbf{x}(\cdot),\mathbf{u}(\cdot)}{\text{minimize}}
\quad J(\mathbf{x}_p,\mathbf{x}_c,\mathbf{x},\mathbf{u})
\qquad\text{subject to all model and engineering constraints.}
```

After transcription, this becomes one large nonlinear program. The optimizer can change physical and control decisions together while accounting for the resulting trajectories and constraints.

## Advantages

- Strongest coordination.
- Direct access to plant–control tradeoffs.
- Unified mathematical structure.
- Natural use of sparse gradient-based optimization.

## Limitations

The integrated nonlinear program can be large and difficult. Successful implementation may require:

- careful scaling;
- strong initial guesses;
- reliable derivatives;
- specialized nonlinear-programming tools; and
- sophisticated software integration.

Simultaneous CCD offers a direct route to a coordinated optimum, especially under strong coupling, but it is not automatically the easiest or most reliable architecture.
