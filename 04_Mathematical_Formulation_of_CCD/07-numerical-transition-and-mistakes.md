# From Formulation to Numerical Optimization

## Finite-dimensional transcription

A computer cannot optimize arbitrary functions directly. A continuous-time formulation is converted into a nonlinear program by:

- parameterizing state and control trajectories;
- sampling trajectories at finite points;
- enforcing dynamics through simulation or defect equations; and
- approximating integral objectives numerically.

For example, quadrature gives

```{math}
\int_{t_0}^{t_f}L(t)\,dt\approx\sum_{i=1}^{N}w_iL(t_i).
```

Later chapters develop these transcription choices. The important point here is that reliable numerical methods begin with a sound mathematical formulation.

```{admonition} CCD viewpoint
:class: important
Static design variables are usually numbers. Dynamic CCD variables include both finite-dimensional design parameters and time-dependent trajectories. The formulation must unify engineering design optimization with dynamic-system modeling.
```

## Common formulation mistakes

1. **Leaving out essential physics.** The result may not transfer to the real system.
2. **Confusing variables and parameters.** A quantity is a decision variable only if the optimizer may change it.
3. **Using an objective that misses the engineering goal.** Minimizing control effort alone, for example, may destroy tracking.
4. **Treating path constraints as endpoint constraints.** This permits dangerous intermediate violations.
5. **Over-constraining the problem.** Excessively tight limits may eliminate all feasible designs.
6. **Forgetting variable bounds.** The optimizer may enter unrealistic model regions.
7. **Mixing open- and closed-loop representations.** A feedback-parameterized controller must be reflected consistently in the dynamics and decisions.
