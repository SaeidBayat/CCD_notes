---
numbering: false
---

# 0.6 Summary and Problems

## Chapter summary

This prerequisite chapter introduced the mathematical and computational foundations used throughout the course. It reviewed notation for scalars, vectors, matrices, and trajectories; functions, derivatives, gradients, Jacobians, Hessians, and integrals; essential linear-algebra concepts; the conversion of a second-order differential equation to first-order state-space form; basic optimization language; the discretization of continuous trajectories; and the minimal coding workflow required for simulation and optimization studies.

The aim was not to replace full courses in calculus, linear algebra, dynamics, optimization, or programming. It was to establish the vocabulary and tools needed to study control co-design clearly and efficiently. Chapter 1 now builds on this foundation to explain why plants and controllers should often be optimized together rather than separately.

## Key terms

| Mathematical language | Dynamics and computation | Optimization |
|---|---|---|
| Scalar | Trajectory | Decision variable |
| Vector | Ordinary differential equation | Objective function |
| Matrix | Initial condition | Equality constraint |
| Summation | State-space model | Inequality constraint |
| Derivative | Time discretization | Feasible point |
| Partial derivative | Sampled variable | Feasible region |
| Gradient | Simulation | Optimal point |
| Jacobian | Computational workflow | Performance index |
| Hessian | Numerical integration | Design bounds |
| Definite integral | Trapezoidal rule | Sensitivity |

## Problems

### Notation and basic interpretation

1. State whether each quantity is naturally viewed as a scalar, vector, matrix, or trajectory: $m$, $\mathbf{x}$, $A$, and $u(t)$.
2. Write a vector containing the three variables $k$, $c$, and $m$.
3. Explain the difference between $x_2$ and $x^{(2)}$.
4. Expand the summation $\sum_{i=1}^{4}i^2$.
5. Give one example of a plant design variable and one example of a controller parameter in a CCD problem.

### Derivatives and gradients

6. Compute $df/dx$ if $f(x)=3x^2-5x+1$.
7. Compute $d^2f/dx^2$ for the same function.
8. For $J(k,c)=k^2+2c^2-kc$, compute $\partial J/\partial k$ and $\partial J/\partial c$.
9. Write the gradient of $J(k,c)=k^2+2c^2-kc$.
10. If $z=f(y)$ and $y=g(x)$, state the chain rule for $dz/dx$.

### Integration and discretization

11. What physical meaning could the integral $\int_0^T u(t)^2\,dt$ have?
12. Write a rectangle-rule approximation of $\int_{t_0}^{t_f}q(t)\,dt$.
13. Write a trapezoidal-rule approximation of the same integral.
14. If $u=[1,2,3]$ is sampled with equal spacing $\Delta t=0.5$, compute the trapezoidal approximation of $\int u(t)^2\,dt$ over the two subintervals.
15. Explain why numerical integration is necessary in computation.

### Linear algebra

16. Let $\mathbf{x}=\begin{bmatrix}1&2\end{bmatrix}^{T}$ and $\mathbf{y}=\begin{bmatrix}3&4\end{bmatrix}^{T}$. Compute $\mathbf{x}+\mathbf{y}$.
17. Let $A=\begin{bmatrix}1&2\\0&3\end{bmatrix}$ and $\mathbf{x}=\begin{bmatrix}2\\1\end{bmatrix}$. Compute $A\mathbf{x}$.
18. What are the dimensions of a matrix in $\mathbb{R}^{3\times2}$?
19. Define an eigenvalue–eigenvector pair in words.
20. What does it mean for a matrix to be positive definite?

### Differential equations and state-space form

21. Identify the order of the equation $m\ddot{x}+c\dot{x}+kx=u$.
22. For the same equation, define states that convert it to first-order form.
23. Write the corresponding first-order state equations.
24. What additional information is needed, beyond the equation itself, to solve an initial-value problem?
25. Write a generic nonlinear state-space model and explain the meaning of each term.

### Optimization language

26. In your own words, define *decision variable*, *objective*, and *constraint*.
27. Write a small optimization problem with one variable, one objective, and one bound constraint.
28. What is a feasible point?
29. Explain the difference between equality and inequality constraints.
30. Why is a clear optimization formulation important in engineering design?

### Coding and mini-project exercises

31. Write pseudocode for simulating a dynamic system from a given initial condition.
32. In Python or MATLAB, create a short script that defines a vector of equally spaced times and a sampled control vector.
33. Using sampled data, compute a discrete approximation to an integral objective.
34. For a mass–spring–damper system, list which quantities could be plant variables, states, control inputs, and outputs in a CCD formulation.
35. **Mini-project:** Simulate a mass–spring–damper system, compute a performance metric, and explain how the problem could be turned into a control co-design study.

## References and further reading

1. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

2. Boyd, S., & Vandenberghe, L. (2018). *Introduction to applied linear algebra: Vectors, matrices, and least squares*. Cambridge University Press.

3. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577

4. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182
