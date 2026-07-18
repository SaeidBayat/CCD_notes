# Plant-Control Coupling

Two groups of decisions are **coupled** when changing one group changes the best choice in the other. In CCD, the plant changes dynamics, actuator requirements, sensor signals, and achievable performance; the controller changes loads, motions, energy flow, fatigue, and the value of alternative plant designs.

```{figure} imgs/bidirectional-coupling.svg
:alt: Circular dependence between plant design and controller design.
:width: 85%
:align: center

Plant decisions change the dynamics, the dynamics change the best controller, and controlled behavior changes which plant best serves the mission.
```

## A mass-spring-damper example

Consider a mass $m$, spring $k$, damper $c$, actuator force $u(t)$, and disturbance $d(t)$:

$$
m\ddot{x}(t)+c\dot{x}(t)+kx(t)=u(t)+d(t).
$$

With proportional-derivative feedback,

$$
u(t)=-K_px(t)-K_d\dot{x}(t),
$$

the closed-loop system becomes

$$
m\ddot{x}(t)+(c+K_d)\dot{x}(t)+(k+K_p)x(t)=d(t).
$$

Passive stiffness $k$ and proportional feedback $K_p$ both contribute to effective closed-loop stiffness. Passive damping $c$ and derivative feedback $K_d$ both contribute to effective damping. They are not interchangeable in practice: active action needs sensors, power, computation, bandwidth, and a functioning actuator. Nevertheless, they can partly substitute for or complement one another.

If $k$ is chosen before $K_p$ is considered, the design may contain more passive stiffness than needed once active control becomes available. If $K_p$ is chosen without plant cost or actuator limits, the controller may demand unrealistic force or energy.

## Worked allocation example

Suppose the design requires an effective stiffness

$$k+K_p=6,$$

with normalized cost

$$C(k,K_p)=0.08k^2+0.02K_p^2.$$

A passive-first design sets $K_p=0$, giving $k=6$ and

$$C_{\mathrm{seq}}=0.08(6)^2=2.88.$$

For co-design, substitute $K_p=6-k$:

$$C(k)=0.08k^2+0.02(6-k)^2.$$

Setting $dC/dk=0$ yields $k=1.2$ and $K_p=4.8$, with

$$C_{\mathrm{CCD}}=0.08(1.2)^2+0.02(4.8)^2=0.576.$$

The numbers are deliberately simple. The lesson is general: when passive and active decisions contribute to the same system property, the least-cost allocation may be invisible to a one-pass sequential workflow.

## Common forms of coupling

| Coupling type | Plant-to-control effect | Control-to-plant effect |
|---|---|---|
| Dynamic | Mass, stiffness, damping, geometry, and operating point change the state equations. | Feedback changes effective dynamics, resonance, damping, and transient loads. |
| Constraint | Plant design changes actuator, temperature, stress, or motion limits. | Control trajectories determine whether stress, fatigue, stroke, and power limits are satisfied. |
| Economic | Plant size and material alter capital and maintenance cost. | Controller complexity, sensing, computation, and energy use alter lifecycle cost. |
| Information | Sensor placement and observability change what the controller can know. | Information needs can motivate different sensor locations, structures, or architectures. |
| Reliability | Passive stability and redundancy alter failure behavior. | Control can reduce loads but introduces hardware, software, and cyber failure modes. |
| Architecture | Components and connections determine available dynamic pathways. | Desired authority may motivate adding, removing, or relocating components and actuators. |

## Coupling strength

Coupling is strong when a small plant change causes a large change in the optimal controller, or when a small change in control capability causes a large change in the optimal plant. Strong coupling is common when:

- active control has substantial authority relative to passive forces;
- dynamic behavior dominates performance;
- plant constraints depend strongly on state and control trajectories;
- multiple time scales or energy domains interact;
- control exploits flexible, unstable, resonant, or energy-storing behavior; or
- sensing, sampling, delay, or preview limitations influence physical design.

```{admonition} Checkpoint
:class: tip
Why does coupling in the mass-spring-damper example weaken as allowable actuator force approaches zero? Why does unlimited actuator authority still fail to guarantee a practical design?
```

:::{tip} Activity 1.3: Quantifying Plant-Control Coupling
:class: dropdown

Consider the parameterized system-level objective

```{math}
J(p,c;\gamma)
=\frac{1}{2}ap^2+\frac{1}{2}bc^2+\gamma pc-r_pp-r_cc,
```

where $a>0$, $b>0$, and $\gamma$ represents plant-control coupling strength.

1. Derive the condition on $\gamma$ for $J$ to be strictly convex.

2. Derive the optimal controller $c^*(p)$ for a fixed plant.

3. Compute the controller sensitivity

   ```{math}
   \frac{dc^*}{dp}.
   ```

4. Derive the optimal plant $p^*(c)$ for a fixed controller and compute

   ```{math}
   \frac{dp^*}{dc}.
   ```

5. Show that both sensitivities vanish when $\gamma=0$.

6. Solve for the simultaneous optimum

   ```{math}
   p^*(\gamma),
   \qquad
   c^*(\gamma).
   ```

7. Use

   ```{math}
   a=4,
   \qquad
   b=3,
   \qquad
   r_p=6,
   \qquad
   r_c=5,
   ```

   and evaluate the optimum for

   ```{math}
   \gamma\in\{0, 0.5, 1, 2, 3\}.
   ```

8. Plot

   ```{math}
   \left|\frac{dc^*}{dp}\right|
   ```

   and the sequential performance loss as functions of $\gamma$.

9. Propose a dimensionless coupling index based on the Hessian cross-term and justify your choice.
:::

:::{tip} Activity 1.4: Control Authority and the Value of Integration
:class: dropdown

Consider

```{math}
m\ddot{x}+c\dot{x}+kx=u,
```

with

```{math}
m=1,
\qquad
x(0)=1,
\qquad
\dot{x}(0)=0.
```

Use the PD controller

```{math}
u=-K_px-K_d\dot{x},
\qquad
0\leq K_p\leq K_{p,\max},
\qquad
0\leq K_d\leq K_{d,\max},
```

with plant-design bounds

```{math}
0.1\leq k\leq6,
\qquad
0.05\leq c\leq3.
```

Define

```{math}
A_{\mathrm{cl}}=
\begin{bmatrix}
0&1\\
-(k+K_p)&-(c+K_d)
\end{bmatrix}.
```

For stable designs, let $P$ solve

```{math}
A_{\mathrm{cl}}^TP+PA_{\mathrm{cl}}+Q+K^TRK=0,
```

where

```{math}
Q=
\begin{bmatrix}
1&0\\0&0.05
\end{bmatrix},
\qquad
R=0.02,
\qquad
K=\begin{bmatrix}K_p&K_d\end{bmatrix}.
```

Define the total cost

```{math}
J=\mathbf{x}_0^TP\mathbf{x}_0+0.02k^2+0.03c^2,
\qquad
\mathbf{x}_0=
\begin{bmatrix}1\\0\end{bmatrix}.
```

1. Derive the closed-loop stability conditions.

2. Explain why $\mathbf{x}_0^TP\mathbf{x}_0$ equals the infinite-horizon dynamic performance cost.

3. For

   ```{math}
   K_{p,\max}=K_{d,\max}\in\{0, 0.5, 1, 2, 4, 8\},
   ```

   solve:

   1. the passive-first sequential problem; and
   2. the simultaneous CCD problem.

4. Plot the relative CCD advantage

   ```{math}
   \eta_{\mathrm{CCD}}=
   \frac{J_{\mathrm{seq}}-J_{\mathrm{CCD}}}{J_{\mathrm{seq}}}
   ```

   against allowable control authority.

5. Determine whether the coupling becomes weak as the allowable controller gains approach zero.

6. Determine whether unlimited control authority drives the optimal passive stiffness and damping to their lower bounds.

7. Add the actuator-effort regularization

   ```{math}
   \beta(K_p^2+K_d^2),
   \qquad
   \beta\in\{0, 10^{-3}, 10^{-2}, 10^{-1}\},
   ```

   and repeat the study.

8. Explain why strong control authority does not automatically imply that the most active design is the most practical design.
:::
