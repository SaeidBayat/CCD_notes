# Worked CCD Formulations

## Example 4.1: mass–spring–damper CCD

Choose spring stiffness $k$ and a proportional–derivative controller

```{math}
u(t)=-K_px(t)-K_d\dot{x}(t)
```

to reduce motion and effort for a system with fixed $m$ and $c$.

**Decisions:**

```{math}
\mathbf{x}_p=[k],
\qquad
\mathbf{x}_c=[K_p,K_d].
```

**States and dynamics:** With $x_1=x$ and $x_2=\dot{x}$,

```{math}
\dot{x}_1=x_2,
\qquad
\dot{x}_2=-\frac{k}{m}x_1-\frac{c}{m}x_2+\frac{1}{m}u.
```

Substituting the controller produces a closed-loop model in $k$, $K_p$, and $K_d$.

**Objective:**

```{math}
J=\int_{t_0}^{t_f}\left(q_xx_1(t)^2+q_vx_2(t)^2+ru(t)^2\right)dt.
```

**Bounds and path constraint:**

```{math}
0<k_{\min}\leq k\leq k_{\max},
\quad
0\leq K_p\leq K_{p,\max},
\quad
0\leq K_d\leq K_{d,\max},
\quad
|u(t)|\leq u_{\max}.
```

This is a complete, if small, CCD formulation.

## Example 4.2: active suspension

For a quarter-car suspension, let

```{math}
\mathbf{x}_p=[k_s,c_s]^T,
\qquad
\mathbf{x}_c=[K_1,K_2,K_3,K_4]^T.
```

A possible objective is

```{math}
J=\int_{t_0}^{t_f}\left(w_1a_b(t)^2+w_2z_s(t)^2+w_3u(t)^2\right)dt,
```

where $a_b$ is body acceleration and $z_s$ is suspension deflection. The quarter-car equations enforce the dynamics; path constraints can limit suspension travel, tire load, and actuator force. Plant and controller variables are optimized together while the state trajectory obeys the model.

## Example 4.3: classify an objective

Suppose

```{math}
J=-P(t_f)+\int_{t_0}^{t_f}\left(0.02\theta_p(t)^2+0.1M_t(t)^2\right)dt,
```

where $P(t_f)$ is final delivered energy, $\theta_p$ is blade-pitch angle, and $M_t$ is tower-base moment. The terminal term $-P(t_f)$ is Mayer; the integral is Lagrange; together they form a Bolza objective.
