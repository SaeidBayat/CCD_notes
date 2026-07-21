# Sequential Design and Control Co-Design

## Why sequential design is common

Engineering organizations are divided into specialties for good reasons. Mechanical engineers develop structures and mechanisms; electrical engineers select sensors and power electronics; control engineers design feedback algorithms; software engineers implement them; and manufacturing teams evaluate cost and producibility.

Specialization, however, encourages a one-pass workflow:

1. design the physical plant using assumed operating conditions and an assumed control strategy;
2. freeze or largely fix the plant;
3. design the controller for that fixed plant; and
4. test the complete system and revise it if performance is unacceptable.

This workflow gives clear ownership, smaller models, and compatibility with established disciplinary tools. It may also be the only practical option after hardware is built. The difficulty is that freezing the plant can remove better system-level combinations before the final controller is known.

```{figure} imgs/sequential-vs-ccd.png
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

## Real consequences of ignoring coupling

The failure mode is not hypothetical. Two documented cases illustrate what happens when a physical system is finalized without full consideration of its interaction with active behavior.

When London's Millennium Bridge opened in June 2000, pedestrians crossing it excited unexpected lateral vibration. As the deck swayed, pedestrians unconsciously synchronized their footsteps to the motion to keep their balance, and that synchronized walking pumped more energy into the same lateral mode, amplifying the sway until the bridge had to be closed. The passive structural design had not accounted for how people—an uncontrolled but dynamically responsive part of the system—would interact with the deck's dynamics. The eventual fix retrofitted tuned mass and viscous dampers, an expensive redesign that earlier consideration of the coupled pedestrian-structure dynamics might have avoided or reduced.

A second case comes from agricultural equipment. Combine harvesters must hold their header at a narrow height above the ground to cut crops cleanly without hitting the soil, and header-height control performance is a real limit on how fast a harvester can operate. In at least one documented case, engineers found that further performance gains could not be reached by improving the controller alone: the physical-system design had not been developed with the header-height control problem in mind, and the control-relevant dynamics could only be improved by redesigning the physical header and its linkage—that is, by revisiting plant decisions that had already been frozen.

```{admonition} Key idea
:class: important
Both cases share the same structure: a physical design was finalized using assumptions about behavior that turned out to depend on the very control (or uncontrolled human) response the design was supposed to accommodate. Neither failure required exotic engineering—both arose from ordinary sequential design applied to a system whose plant and control behavior were, in fact, coupled.
```

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

CCD is a specialized instance of a broader field called **multidisciplinary dynamic system design optimization (MDSDO)**: design optimization for systems in which the evolution of state through time is a critical element of performance, multiple disciplines or energy domains must be integrated, and the specific properties of dynamic systems are exploited to improve performance and problem tractability. MDSDO is itself a branch of multidisciplinary design optimization (MDO), the broader field concerned with optimizing systems whose performance depends on interacting disciplines (structural, aerodynamic, electrical, thermal, economic, and so on). CCD adds one more ingredient on top of MDSDO: the explicit presence of an active *controller* as a first-class design object, not merely a fixed regulator applied after the fact. Realistic CCD formulations may combine structures, fluids, electrical systems, thermal systems, economics, reliability, sensing, software, and manufacturing—so a working command of MDO ideas transfers directly.

## Three complementary methodologies

CCD is often equated with the compact optimization statement introduced below, but that formal, mathematical style is only one of at least three complementary traditions engineers use to achieve integrated plant-control design:

1. **Control-inspired paradigms.** Practicing control engineers use frequency- and time-domain reasoning—Bode and Nichols diagrams, root locus, bandwidth, resonance, disturbance rejection, actuator-sensor colocation—to propose new mechanisms, sensor and actuator placements, and control structures directly from physical insight. This is the oldest and most engineering-intuitive route to CCD; the Wright brothers and Charles Brush, profiled later in this chapter, practiced it without ever writing an optimization problem.
2. **Co-optimization.** A formal mathematical methodology that poses plant and control decisions as variables in a single constrained optimization problem, typically nonlinear and often with dynamics enforced by an equality constraint. This is the most mature and most rigorously teachable of the three traditions, and it is the primary focus of this course starting with the mathematical statement below.
3. **Co-simulation.** Multiscale, multiphysics, high- or mixed-fidelity simulation—sometimes combined with data-driven or machine-learning models—used to explore designs iteratively when a closed-form or tractable optimization formulation is not yet available. Co-simulation becomes essential once models grow too complex or too expensive to embed directly inside an optimizer, a theme this course returns to in the discussion of model fidelity and surrogates.

These traditions are not mutually exclusive, and combining them tends to produce the most capable designs: control-inspired reasoning supplies engineering creativity and sanity checks, co-optimization supplies mathematical rigor and repeatability, and co-simulation supplies the ability to handle complexity that resists closed-form treatment. Two derived ideas sit at their intersections and are worth knowing by name even before they are developed later in the course: a **digital twin** couples co-simulation with real-time sensor data from the physical system, and **experimentally infused optimization** couples co-optimization with offline experimental data to reduce the uncertainty a numerical optimizer must otherwise absorb.

```{admonition} Checkpoint
:class: tip
Every CCD study also depends on the same five inputs regardless of which methodology is used: system objectives, a pre-design of the relevant components, physics-based models, real data (lab or field), and representative case studies. Missing or weak inputs propagate into a weak result no matter how sophisticated the chosen methodology is.
```

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

The iterative-sequential strategy has a precise mathematical identity: repeatedly optimizing the plant with the controller held fixed, then the controller with the plant held fixed, and alternating until neither subproblem changes, is an instance of **block coordinate descent (BCD)**—a general optimization algorithm that partitions the decision variables into blocks and optimizes one block at a time. If each subproblem is solved to a unique optimum and both blocks use the same, fully consistent system-level objective, BCD is guaranteed to converge to the same solution as the simultaneous problem. Two caveats matter in practice. First, if a coupling model is missing—if the plant subproblem is not actually re-solved against the true system objective once control is included—the iteration is not BCD at all; it is the one-pass sequential workflow criticized above, dressed up as "iteration." Second, even genuine BCD can converge slowly or fail to converge cleanly when the plant-control cross-coupling is strong: the number of iterations required grows sharply as the interaction between the plant and control blocks strengthens, and for non-convex or weakly identified coupling, BCD can cycle rather than converge. This is the same mechanism you will meet in Activity 1.1: the cross term in $J(p,c)=4p^2+3c^2+4pc-\cdots$ is exactly the kind of plant-control interaction whose magnitude governs how many alternating passes are needed—and whether alternating is even a sound strategy at all.

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
