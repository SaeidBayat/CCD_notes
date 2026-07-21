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

### Example 4.2 revisited: physically concrete plant constraints

The abstract stiffness-and-damping version above is a reasonable first pass, but real suspension co-design studies replace $k_s$ and $c_s$ with the physical geometry that produces them, and replace the generic path constraint $\mathbf{g}(\cdot)\leq\mathbf{0}$ with a list of named engineering limits. In one such study, the quarter-car plant vector is the helical-spring and telescopic-damper geometry

```{math}
\mathbf{x}_p=[d,\,D,\,p,\,N_a,\,D_0,\,D_p,\,D_s]^T,
```

where $d$ is spring wire diameter, $D$ is spring coil diameter, $p$ is spring pitch, $N_a$ is the number of active coils, $D_0$ is the damper valve diameter, $D_p$ is the damper piston diameter, and $D_s$ is the damper stroke; spring stiffness $k_s$ and damping rate $c_s$ become *dependent* quantities computed from this geometry rather than independent design variables. The Lagrange objective weighs road holding, ride comfort, and control cost,

```{math}
J=\int_{t_0}^{t_f}\left(r_1(z_{us}(t)-z_0(t))^2+r_2\ddot{z}_s(t)^2+r_3u(t)^2\right)dt,
```

with weights on the order of $r_1=10^5$, $r_2=0.5$, and $r_3=10^{-5}$ chosen so that all three terms have comparable numerical magnitude—an ordinary but essential scaling step for any multi-term Lagrange objective.

The physical-constraint set $\mathbf{g}_p(\mathbf{x}_p)\leq\mathbf{0}$ for this system is not one generic bound but a list of named engineering limits, including:

- a **buckling constraint** relating free spring length to coil diameter;
- **packaging constraints** requiring the spring and damper to fit within a fixed pocket length (about 0.40 m) and outer diameter, with clearance around the coaxial damper;
- a **rattlespace constraint** bounding peak suspension travel, evaluated from a full vehicle simulation over a ramp road input rather than from a closed-form bound;
- a **spring stress and fatigue constraint** using a Soderberg criterion that combines mean and alternating shear stress computed from the mean and amplitude of the axial spring force under a rough-road simulation;
- a **damper thermal constraint** limiting the maximum damper fluid temperature (about 390 K), predicted by a lumped heat-transfer model of the damper fluid, steel housing, and surrounding air, to prevent fluid fade and seal damage;
- a **damper pressure constraint** limiting maximum damper pressure (about $4.75\times10^{6}$ Pa) to protect the seals; and
- a **damper velocity constraint** limiting piston velocity to protect internal valve components.

Several of these—rattlespace, fatigue, and the thermal limit—depend on the full state trajectory under a specified road disturbance, not merely on $\mathbf{x}_p$ in isolation, so they are best classified as path constraints evaluated along a simulated response rather than as simple bounds. The general lesson is that a physically faithful CCD formulation of even a "simple" quarter-car suspension has more than a dozen named engineering constraints, most of them unit-bearing and traceable to a specific failure mode, rather than one abstract $\mathbf{g}(\cdot)\leq\mathbf{0}$.

## Example 4.3: classify an objective

Suppose

```{math}
J=-P(t_f)+\int_{t_0}^{t_f}\left(0.02\theta_p(t)^2+0.1M_t(t)^2\right)dt,
```

where $P(t_f)$ is final delivered energy, $\theta_p$ is blade-pitch angle, and $M_t$ is tower-base moment. The terminal term $-P(t_f)$ is Mayer; the integral is Lagrange; together they form a Bolza objective.
