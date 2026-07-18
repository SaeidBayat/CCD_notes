# Sequential Design and Control Co-Design

## Why sequential design is common

Engineering organizations are divided into specialties for good reasons. Mechanical engineers develop structures and mechanisms; electrical engineers select sensors and power electronics; control engineers design feedback algorithms; software engineers implement them; and manufacturing teams evaluate cost and producibility.

Specialization, however, encourages a one-pass workflow:

1. design the physical plant using assumed operating conditions and an assumed control strategy;
2. freeze or largely fix the plant;
3. design the controller for that fixed plant; and
4. test the complete system and revise it if performance is unacceptable.

This workflow gives clear ownership, smaller models, and compatibility with established disciplinary tools. It may also be the only practical option after hardware is built. The difficulty is that freezing the plant can remove better system-level combinations before the final controller is known.

```{figure} imgs/sequential-vs-ccd.svg
:alt: Sequential design compared with integrated control co-design.
:width: 95%
:align: center

Sequential design fixes the plant before final controller design. CCD coordinates both sets of decisions through shared dynamics, objectives, and constraints.
```

## Feasible does not mean system-optimal

A design is **feasible** when it satisfies its constraints. A design is **optimal** only relative to a specified objective, model, and feasible set. A sequential design can meet every safety and performance requirement yet still use excess material, require too much control effort, consume unnecessary energy, or deliver less performance than another feasible plant-controller pair.

```{admonition} Key idea
:class: important
The criticism of sequential design is not that it always fails. Fixing one design domain too early can remove better system-level solutions from consideration.
```

Sequential design may be adequate when coupling is weak, the controller has little authority, one subsystem is fixed by regulation or legacy hardware, the plant barely affects the control problem, or the coupled model is too uncertain to justify added complexity.

## What control co-design means

```{admonition} Definition
:class: important
Control co-design is the integrated design of an actively controlled engineering system in which physical-system and control-system decisions are coordinated using shared models, objectives, and constraints.
```

The definition contains four essential ideas:

- **Integrated:** plant and control decisions are not optimized independently and merely combined later.
- **Dynamic:** behavior through time is central to performance.
- **System-level:** objectives and constraints represent the mission and limitations of the complete system.
- **Coordinated:** the problem may be solved simultaneously, through nested optimization, or through a managed iterative strategy.

CCD is a specialized form of multidisciplinary design optimization for active dynamic systems. Realistic formulations may combine structures, fluids, electrical systems, thermal systems, economics, reliability, sensing, software, and manufacturing.

## A first mathematical statement

A compact deterministic CCD problem is

$$
\begin{aligned}
\underset{x_p,x_c,\xi(\cdot)}{\operatorname{minimize}}\quad
&J\bigl(x_p,x_c,\xi(\cdot),u(\cdot)\bigr)\\
\text{subject to}\quad
&\dot{\xi}(t)=f\bigl(t,\xi(t),u(t),x_p\bigr),\\
&g\bigl(t,\xi(t),u(t),x_p,x_c\bigr)\le 0,\\
&h\bigl(\xi(t_0),\xi(t_f),x_p,x_c\bigr)=0,\\
&u(t)=\mathcal{K}(\text{available information};x_c).
\end{aligned}
$$

The objective $J$ measures system performance. The dynamic equation enforces physical consistency. Inequalities can impose stress, displacement, temperature, actuator, power, or safety limits. Boundary equations impose initial and terminal conditions. The final relation makes the controller's information explicit.

## Common coordination strategies

```{figure} imgs/ccd-workflow.svg
:alt: Iterative sequential, nested, and simultaneous CCD strategies.
:width: 95%
:align: center

CCD is defined by integrated system design, not by a single numerical architecture.
```

- **Iterative sequential:** alternate plant and controller subproblems until a stopping rule is reached.
- **Nested:** solve an inner control problem for each candidate plant in an outer plant-design loop.
- **Simultaneous:** optimize plant variables, control variables, and often state trajectories in one problem.

All three attempt to account for plant-control coupling. A one-pass plant-then-controller workflow does not.

## One system-level objective

An active-suspension objective might combine comfort, road holding, effort, mass, and cost:

$$
J=\int_{t_0}^{t_f}\!\left(w_a a_s^2(t)+w_r\Delta z_t^2(t)+w_uF^2(t)\right)dt
+w_mM(x_p)+w_CC(x_p).
$$

This does not imply that every system has only one goal. Multiobjective or constrained formulations are often appropriate. The important requirement is that the same system-level priorities govern both plant and control decisions.

:::{tip} Activity 1.1: Exact Sequential versus Simultaneous Co-Design
:class: dropdown

Consider the coupled quadratic design problem

```{math}
J(p,c)=4p^2+3c^2+4pc-12p-10c+20,
```

where $p$ is a plant-design variable and $c$ is a controller-design variable, subject to

```{math}
0\leq p\leq3,
\qquad
0\leq c\leq3.
```

1. Compute the Hessian of $J$ and determine whether the problem is strictly convex.

2. In a single-pass sequential workflow, set the nominal controller to $\hat{c}=0$. First optimize $p$, then freeze $p$ and optimize $c$. Compute

   ```{math}
   p_{\mathrm{seq}},
   \qquad
   c_{\mathrm{seq}},
   \qquad
   J_{\mathrm{seq}}.
   ```

3. Solve the simultaneous CCD problem

   ```{math}
   \min_{p,c}J(p,c)
   ```

   analytically.

4. Compute the percentage improvement

   ```{math}
   \eta=
   \frac{J_{\mathrm{seq}}-J_{\mathrm{CCD}}}{J_{\mathrm{seq}}}
   \times100\%.
   ```

5. Repeat the sequential calculation using

   ```{math}
   \hat{c}\in\{0.5, 1, 2\}.
   ```

   Determine how strongly the final sequential design depends on the assumed nominal controller.

6. Derive the value of $\hat{c}$ for which the single-pass sequential workflow reproduces the simultaneous optimum exactly.

7. Explain why this special value does not make sequential design generally equivalent to CCD.
:::

:::{tip} Activity 1.2: System-Level Objective and Hidden Tradeoffs
:class: dropdown

An active-suspension study uses the weighted objective

```{math}
J=w_aJ_a+w_tJ_t+w_uJ_u+w_mJ_m,
```

where

```{math}
\begin{aligned}
J_a&=\int_0^T a_s(t)^2\,dt, &
J_t&=\int_0^T \Delta z_t(t)^2\,dt,\\
J_u&=\int_0^T F(t)^2\,dt, &
J_m&=M(\mathbf{x}_p).
\end{aligned}
```

Two feasible designs produce the normalized metrics

```{math}
\mathbf{J}^{(A)}=
\begin{bmatrix}
0.60\\1.10\\1.45\\0.75
\end{bmatrix},
\qquad
\mathbf{J}^{(B)}=
\begin{bmatrix}
0.85\\0.80\\0.70\\1.10
\end{bmatrix}.
```

1. Determine the region of nonnegative weight vectors

   ```{math}
   \mathbf{w}=
   \begin{bmatrix}
   w_a&w_t&w_u&w_m
   \end{bmatrix}^{T},
   \qquad
   \sum_i w_i=1,
   ```

   for which design $A$ is preferred.

2. Determine the region for which design $B$ is preferred.

3. Show that neither design dominates the other in the Pareto sense.

4. Determine which design is selected for each weight vector:

   ```{math}
   \begin{aligned}
   \mathbf{w}^{(1)}&=
   \begin{bmatrix}0.55&0.20&0.15&0.10\end{bmatrix}^{T},\\
   \mathbf{w}^{(2)}&=
   \begin{bmatrix}0.25&0.25&0.25&0.25\end{bmatrix}^{T},\\
   \mathbf{w}^{(3)}&=
   \begin{bmatrix}0.20&0.25&0.15&0.40\end{bmatrix}^{T}.
   \end{aligned}
   ```

5. Suppose passenger comfort must satisfy the hard requirement $J_a\leq0.75$. Determine which designs remain feasible.

6. Suppose actuator effort must satisfy $J_u\leq1$. Determine which designs remain feasible.

7. Explain why moving an engineering requirement from the objective to a constraint can change the selected CCD solution even when the same physical metric is used.

8. Construct a third feasible design $C$ that dominates either $A$ or $B$, but not both.

9. Explain why reporting only the aggregate weighted objective can hide an unacceptable engineering compromise.
:::
