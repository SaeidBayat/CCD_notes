# Path and Boundary Constraints

## Path constraints

A path constraint must hold throughout the time interval:

```{math}
:label: eq-ch4-path-constraint
\mathbf{g}(\mathbf{x}(t),\mathbf{u}(t),\mathbf{x}_p,\mathbf{x}_c,\mathbf{d}(t),t)\leq\mathbf{0},
\qquad t\in[t_0,t_f].
```

Examples include actuator saturation, displacement and angle limits, structural loads, temperature, speed, and safety envelopes.

## Boundary constraints

Boundary constraints apply at the start, end, or designated points:

```{math}
:label: eq-ch4-boundary-constraint
\mathbf{b}(\mathbf{x}(t_0),\mathbf{x}(t_f),\mathbf{u}(t_0),\mathbf{u}(t_f),
\mathbf{x}_p,\mathbf{x}_c,t_0,t_f)=\mathbf{0}.
```

They can enforce initial states, final positions, periodicity, terminal performance, endpoint compatibility, or mission completion. Boundary inequalities are also possible.

![A trajectory with a shaded path-constraint envelope and separate markers for initial and final boundary conditions.](imgs/fig_chp4_5.svg)

*Path constraints apply throughout time; boundary constraints apply at selected points.*

For example,

```{math}
|u(t)|\leq u_{\max},\qquad\forall t,
```

is an actuator path constraint, while

```{math}
q(t_f)=q_f
```

is a terminal boundary constraint.

```{admonition} Key idea
:class: important
Path constraints protect the design at all times. Boundary constraints enforce what must happen at the beginning, end, or another designated point. The distinction affects both modeling and numerical solution.
```
