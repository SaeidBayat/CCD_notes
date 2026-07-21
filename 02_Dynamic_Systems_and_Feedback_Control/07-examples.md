# Examples

## Example 2.1: derive and analyze a state-space model

Consider a mass–spring–damper system with $m=2$ kg, $c=3$ N s/m, and $k=8$ N/m. The control input is force $u$ and the measured output is displacement $y=x$.

**Step 1: Write the dynamic equation.**

```{math}
2\ddot{x}+3\dot{x}+8x=u.
```

**Step 2: Define the states.**

```{math}
x_1=x, \qquad x_2=\dot{x}.
```

**Step 3: Write the first-order model.**

```{math}
\dot{x}_1=x_2,
\qquad
\dot{x}_2=-4x_1-1.5x_2+0.5u,
```

so

```{math}
\dot{\mathbf{x}}=
\begin{bmatrix}0&1\\-4&-1.5\end{bmatrix}\mathbf{x}
+\begin{bmatrix}0\\0.5\end{bmatrix}u,
\qquad
y=\begin{bmatrix}1&0\end{bmatrix}\mathbf{x}.
```

**Step 4: Analyze stability.** The eigenvalues are the roots of

```{math}
\lambda^2+1.5\lambda+4=0,
```

which are

```{math}
\lambda=-0.75\pm j1.854.
```

Their real parts are negative, so the open-loop equilibrium is asymptotically stable.

**Step 5: Interpret the result.** The system oscillates, but the oscillations decay. If the designer raises stiffness to $k=18$ without changing damping, the oscillation frequency increases and the best feedback tuning may change.

## Example 2.2: effect of PD feedback

Suppose Example 2.1 uses

```{math}
u=-6x-4\dot{x}.
```

The closed-loop equation is

```{math}
2\ddot{x}+(3+4)\dot{x}+(8+6)x=0,
```

with characteristic equation

```{math}
2\lambda^2+7\lambda+14=0.
```

The closed-loop poles have a more negative real part than the open-loop poles, indicating increased damping and faster decay. Feedback improves the response by altering the effective dynamics.

## Example 2.3: identify signals in cruise control

Consider a simple vehicle moving along a straight road:

```{math}
m\dot{v}=F_t-c_rv-mg\sin\theta,
```

where $v$ is vehicle speed, $F_t$ is traction force, $c_r$ is a drag or rolling-resistance coefficient, and $\theta$ is road slope.

A sensible description is:

- **state:** vehicle speed $v$;
- **control input:** traction force $F_t$ or throttle command;
- **output:** vehicle speed $v$; and
- **disturbance:** road slope $\theta$.

This first-order model reminds us that a useful state set need not contain many variables.

## Common modeling mistakes

1. **Treating outputs as states without justification.** Outputs may equal states, but they do not have to.
2. **Ignoring disturbances.** This usually creates unrealistic conclusions about controller performance.
3. **Using too many states.** More states are not always better; the state set should be minimal and meaningful.
4. **Forgetting units.** Dynamic equations must be dimensionally consistent.
5. **Assuming plant design changes only constraints or cost.** In CCD, plant design often changes the differential equations themselves.
6. **Confusing stability with performance.** A stable system is not necessarily fast, efficient, comfortable, or optimal.
