# Multidisciplinary Design Optimization

## Why MDO is needed

Large engineering systems involve interacting disciplines. A wind turbine, for example, combines structures, aerodynamics, dynamics, controls, electrical systems, economics, and manufacturing. Improving one discipline in isolation may worsen another.

Multidisciplinary design optimization coordinates decisions across coupled disciplines. CCD is a specialized dynamic-system MDO problem in which plant and control design are dominant interacting disciplines.

![A system-level optimizer coordinating multiple discipline analyses through shared design variables and coupling variables.](imgs/fig_chp3_7.svg)

*A conceptual MDO problem. Coupling variables communicate interactions between disciplines.*

## Coupling variables

A coupling variable is an output from one discipline that becomes an input to another. Examples include:

- structural deflection affecting aerodynamic loads;
- aerodynamic loads affecting structural stress;
- plant dynamics affecting controller performance;
- control forces affecting fatigue and actuator sizing; and
- thermal behavior affecting electrical efficiency.

Coupling creates implicit dependencies. One design change may influence many disciplines through several paths.

## Coupled analysis equations

A two-discipline model can be written as

```{math}
\mathbf{y}_1=\mathbf{F}_1(\mathbf{x},\mathbf{y}_2),
\qquad
\mathbf{y}_2=\mathbf{F}_2(\mathbf{x},\mathbf{y}_1).
```

A consistent multidisciplinary state satisfies both equations simultaneously. Consistency may be enforced by an inner coupled solver or directly within the optimization formulation.

## Monolithic and distributed architectures

A monolithic architecture places most decisions and constraints in one optimization problem. Distributed architectures assign subproblems to disciplines and coordinate them using additional variables or penalties.

The central lesson is to recognize when analyses depend on one another and represent those dependencies consistently—not merely to memorize architecture names.

## CCD as MDO

Changing plant design can alter state-space matrices, natural frequencies, damping, actuator authority, control effort, and closed-loop performance. Changing controller design can alter performance, load histories, actuator sizing and power, and the value of passive stiffness, damping, or mass.

```{admonition} Plant–control coupling
:class: important
These reciprocal effects mean the plant and controller cannot be evaluated as independent disciplines. Their consistency and shared performance must be handled at the system level.
```

:::{tip} Activity 3.4: Total Derivatives through a Coupled Multidisciplinary Model
:class: dropdown

Consider two coupled disciplines:

```{math}
\begin{aligned}
r_1&=y_1-x_1^2-\frac{1}{2}y_2=0,\\
r_2&=y_2-\sin x_2-\frac{1}{4}y_1=0.
\end{aligned}
```

The objective and constraint are

```{math}
f=(y_1-1)^2+(y_2-0.5)^2+0.1(x_1^2+x_2^2),
```

and

```{math}
g=y_1+y_2-2\leq0.
```

The design bounds are

```{math}
-1.5\leq x_1\leq1.5,
\qquad
-2\leq x_2\leq2.
```

1. Write the coupled residual system in the compact form

   ```{math}
   \mathbf{r}\left(\mathbf{x},\mathbf{y}\right)=\mathbf{0}.
   ```

2. Solve the coupled equations analytically for

   ```{math}
   y_1(\mathbf{x}),
   \qquad
   y_2(\mathbf{x}).
   ```

3. Derive the total state sensitivity using the implicit-function theorem:

   ```{math}
   \frac{d\mathbf{y}}{d\mathbf{x}}
   =-\left(\frac{\partial\mathbf{r}}{\partial\mathbf{y}}\right)^{-1}
   \frac{\partial\mathbf{r}}{\partial\mathbf{x}}.
   ```

4. Derive the total derivatives

   ```{math}
   \frac{df}{d\mathbf{x}},
   \qquad
   \frac{dg}{d\mathbf{x}}.
   ```

5. Evaluate the analytical total derivatives at

   ```{math}
   \mathbf{x}=
   \begin{bmatrix}
   0.8\\
   0.4
   \end{bmatrix}.
   ```

6. Verify the derivatives using complex-step differentiation.

7. Show that using only the partial derivative

   ```{math}
   \frac{\partial f}{\partial\mathbf{x}}
   ```

   while ignoring

   ```{math}
   \frac{d\mathbf{y}}{d\mathbf{x}}
   ```

   gives an incorrect search direction.

8. Formulate and solve the problem using a multidisciplinary feasible architecture in which the coupling equations are converged at every design iteration.

9. Reformulate the same problem using an individual-discipline feasible architecture in which $y_1$ and $y_2$ are optimization variables and the coupling equalities are consistency constraints.

10. Compare the two formulations in terms of variable count, constraint count, derivative structure, and convergence.
:::

:::{tip} Activity 3.5: OpenMDAO Benchmark using the Sellar Coupled Problem
:class: dropdown

Consider the classical two-discipline Sellar problem:

```{math}
\begin{aligned}
y_1&=z_1^2+z_2+x-0.2y_2,\\
y_2&=\sqrt{y_1}+z_1+z_2.
\end{aligned}
```

The optimization problem is

```{math}
\begin{aligned}
\min_{x,z_1,z_2}\quad
&f=x^2+z_2+y_1+e^{-y_2},\\
\text{subject to}\quad
&3.16-y_1\leq0,\\
&y_2-24\leq0,
\end{aligned}
```

with bounds

```{math}
0\leq x\leq10,
\qquad
-10\leq z_1\leq10,
\qquad
0\leq z_2\leq10.
```

1. Identify:

   1. local design variables;
   2. shared design variables;
   3. discipline outputs;
   4. coupling variables; and
   5. system-level objective and constraints.

2. Derive the coupled residual equations.

3. Derive the fixed-point iteration that results from solving the disciplines in Gauss–Seidel order.

4. Determine the local convergence condition for the coupling iteration from the spectral radius of the iteration Jacobian.

5. Implement the multidisciplinary feasible formulation in OpenMDAO, using a nonlinear block Gauss–Seidel or Newton solver for the coupled analysis.

6. Supply exact partial derivatives for both disciplines and use OpenMDAO's total-derivative check.

7. Solve the optimization using at least three different initial designs.

8. Reformulate the problem using an individual-discipline feasible architecture by promoting $y_1$ and $y_2$ to design variables and adding consistency constraints.

9. Compare the two architectures in terms of:

   1. number of design variables;
   2. number of constraints;
   3. coupling-solver iterations;
   4. optimizer iterations;
   5. total derivative accuracy; and
   6. final objective value.

10. Perturb the discipline equations by replacing

   ```{math}
   -0.2y_2
   ```

   with

   ```{math}
   -\beta y_2,
   ```

   where

   ```{math}
   0.1\leq\beta\leq0.8.
   ```

   Determine how coupling strength affects fixed-point convergence and optimization performance.

11. Explain why a converged multidisciplinary analysis does not by itself prove that the optimization result is globally optimal or numerically reliable.
:::
