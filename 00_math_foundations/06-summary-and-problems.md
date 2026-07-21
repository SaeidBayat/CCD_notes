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

1. **Second-order sensitivity of a coupled objective.** Let $J(p,c)=\tfrac12(ap^2+2bpc+dc^2)+\alpha e^{p-c}$, where $a,d>0$ and $ad-b^2>0$. Derive the second-order Taylor model of $J$ about an arbitrary point $(p_0,c_0)$ and determine an explicit condition on $\alpha$ and a rectangular domain $\mathcal D$ that guarantees strict convexity throughout $\mathcal D$.

2. **KKT system for a constrained design.** Consider $\min_{x_1,x_2}(x_1-2)^2+3(x_2+1)^2$ subject to $x_1^2+x_2^2\le4$ and $x_1+x_2\ge1$. Derive and solve the complete Karush--Kuhn--Tucker system, then certify the global optimizer using the geometry and convexity of the problem.

3. **State transition and controllability.** For $\dot{\mathbf x}=A\mathbf x+B u$ with $A=\begin{bmatrix}0&1\\-k/m&-c/m\end{bmatrix}$ and $B=\begin{bmatrix}0\\1/m\end{bmatrix}$, derive the finite-horizon controllability Gramian $W_c(T)$ in terms of the matrix exponential and prove that $W_c(T)\succ0$ for every $T>0$ when $m>0$.

4. **Lyapunov certificate with a design parameter.** For $A(q)=\begin{bmatrix}0&1\\-q&-2\end{bmatrix}$, solve $A(q)^TP+PA(q)=-I$ analytically for the symmetric matrix $P$ and determine the complete range of $q$ for which this equation supplies a positive-definite Lyapunov certificate.

5. **Trajectory sensitivity.** The nonlinear system $\dot x=-p x^3+u(t)$ has $x(0)=x_0$ and objective $J(p)=\int_0^T x(t;p)^2\,dt$. Derive a forward-sensitivity initial-value problem whose solution gives $dJ/dp$ without finite differences.

6. **Index-one differential-algebraic model.** A constrained mechanism is modeled by $M(q,p)\ddot q+h(q,\dot q,p)+G(q)^T\lambda=Bu$ with holonomic constraint $\phi(q)=0$. Derive a first-order index-one DAE for $(q,v,\lambda)$ and state a nonsingularity condition that makes the algebraic multiplier locally unique.

7. **Error of trajectory quadrature.** For $J=\int_0^T q(t)\,dt$ with $q\in C^2[0,T]$, derive a global error bound for the composite trapezoidal rule on a nonuniform mesh and use it to construct a mesh-spacing condition that guarantees $|J-J_h|\le\varepsilon$.

8. **Direct transcription of a dynamic optimization problem.** Transcribe $\min_u\int_0^T(x^2+\rho u^2)\,dt$ subject to $\dot x=-ax+bu$, $x(0)=x_0$, and $|u|\le u_{\max}$ using trapezoidal defects on $N$ intervals, giving the resulting nonlinear program in matrix form and its exact sparsity pattern.

9. **Adjoint gradient.** For $\dot{\mathbf x}=\mathbf f(\mathbf x,\mathbf u,p)$ and $J(p)=\Phi(\mathbf x(T),p)+\int_0^T L(\mathbf x,\mathbf u,p)\,dt$, derive the continuous adjoint equation, terminal condition, and a single integral expression for $dJ/dp$ that eliminates the state sensitivity.

10. **Nondimensionalization and conditioning.** For $m\ddot z+c\dot z+kz=F$ with characteristic displacement $z_0$ and time $t_0=\sqrt{m/k}$, derive the dimensionless dynamics and objective $J=\int_0^T(q_z z^2+q_FF^2)\,dt$, then choose variable and residual scalings that make every coefficient and typical decision magnitude order one.

## References and further reading

1. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

2. Boyd, S., & Vandenberghe, L. (2018). *Introduction to applied linear algebra: Vectors, matrices, and least squares*. Cambridge University Press.

3. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577

4. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182
