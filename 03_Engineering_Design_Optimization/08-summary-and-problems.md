# Chapter Summary and Problems

## Summary

Engineering design optimization formalizes a search using design variables, an objective, a predictive model, and constraints. The feasible space contains acceptable designs, and active constraints often explain the optimum. Nonlinear engineering problems can contain multiple local optima, so initialization and exploration matter. Gradient-based algorithms use derivative information efficiently; constrained methods balance improvement against active requirements. Scaling and conditioning strongly influence numerical reliability. MDO extends optimization across coupled disciplines, while dynamic-system optimization introduces trajectories, integral objectives, and path constraints.

```{admonition} Central lesson
:class: important
Optimization is valuable when its formulation, model, derivatives, scaling, convergence evidence, and engineering interpretation are all credible. A solver result alone is not a design decision.
```

## Key terms

Design variable; objective function; equality constraint; inequality constraint; bound; feasible design; infeasible design; active constraint; local optimum; global optimum; convexity; gradient; Hessian; line search; Newton method; quasi-Newton method; KKT conditions; Lagrange multiplier; scaling; conditioning; finite differences; complex-step differentiation; algorithmic (automatic) differentiation; direct and adjoint sensitivity methods; multidisciplinary design optimization; coupling variable; multidisciplinary feasible (MDF); individual discipline feasible (IDF); analytical target cascading (ATC); gradient-free optimization; CMA-ES; genetic algorithm; particle swarm optimization; path constraint; boundary constraint.

## Problems

1. **KKT interpretation of an engineering optimum.** Minimize $J(t,r)=\rho\pi r^2t+\alpha/t$ subject to $\sigma(t,r)=Fr/(2\pi r^2t)\le\sigma_y/S_f$, $r\le r_{\max}$, and $t\ge t_{\min}$. Derive every KKT point and classify the globally optimal pressure-vessel design as the parameters vary.

2. **Scaling and solver conditioning.** A design vector contains length in millimeters, stiffness in newtons per meter, mass in kilograms, and a dimensionless gain, while constraint residuals span eight orders of magnitude. Construct diagonal variable and residual scalings from characteristic physical values and derive how those scalings transform the gradient, Jacobian, Hessian, and KKT system condition number.

3. **Second-order optimality in a nonconvex design.** For $f(x,y)=(x^2-1)^2+\beta(y-x)^2$ subject to $x+y=1$ and $x\ge0$, derive all feasible stationary points and use the reduced Hessian to determine their local optimality as a function of $\beta>0$.

4. **Adjoint sensitivity of a multidisciplinary analysis.** Coupling variables satisfy $y_1=a_1(x,y_2)$ and $y_2=a_2(x,y_1)$, while $J=J(x,y_1,y_2)$. Derive an adjoint system that computes $dJ/dx$ with one linear solve independent of the number of design variables.

5. **MDF versus IDF equivalence.** For the two-discipline coupling model $y_1=x_1+\alpha y_2$ and $y_2=x_2+\beta y_1$, formulate multidisciplinary-feasible and individual-discipline-feasible optimization architectures and prove their local equivalence when $1-\alpha\beta\ne0$ and all consistency constraints are satisfied.

6. **Pareto geometry.** Consider $f_1(x)=(x-1)^2$ and $f_2(x)=\gamma(x+1)^2$ on $x\in[-2,2]$. Derive the complete Pareto set and Pareto front, then characterize which Pareto points cannot be recovered by a strictly positive weighted-sum scalarization if a nonconvex perturbation $-\delta\cos(3\pi x)$ is added to both objectives.

7. **Reliability-based design optimization.** A stress limit state is $g(A,F,Y)=Y-F/A$ with independent $F\sim\mathcal N(\mu_F,\sigma_F^2)$ and $Y\sim\mathcal N(\mu_Y,\sigma_Y^2)$. Derive a first-order reliability constraint for $\mathbb P[g\le0]\le10^{-4}$ and solve the minimum-area design including the sensitivity of the optimum to the target reliability index.

8. **Dynamic-system design optimization.** A thermal storage device follows $C(p)\dot T=-h(p)(T-T_a)+q(t)$ with $T(0)=T_0$. Formulate and solve for the design $p$ that minimizes material cost plus integrated temperature deviation while satisfying $T(t)\le T_{\max}$, using an adjoint to derive the continuous total derivative.

9. **Trust-region SQP step.** For a nonlinear program with twice differentiable objective $f(x)$, equalities $c(x)=0$, and inequalities $g(x)\le0$, derive the exact trust-region SQP subproblem and a merit-function acceptance ratio that remains meaningful when the linearized constraints are inconsistent.

10. **Bilevel design sensitivity.** Let $\psi(p)=\min_c J(p,c)$ subject to $h(p,c)=0$ and $g(p,c)\le0$. Under LICQ, strict complementarity, and second-order sufficiency, derive $d\psi/dp$ from the lower-level Lagrangian and identify the precise regularity loss that makes the outer objective nonsmooth.

## References and further reading

1. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

2. Nocedal, J., & Wright, S. J. (2006). *Numerical optimization* (2nd ed.). Springer. DOI: 10.1007/978-0-387-40065-5

3. Boyd, S., & Vandenberghe, L. (2004). *Convex optimization*. Cambridge University Press. DOI: 10.1017/CBO9780511804441

4. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

5. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

6. Bayat, S., Peterson, C., Lee, Y. H., Iori, J., & Allison, J. T. (2026). Advancing wind turbines through control co-design: An integrative review. *Applied Energy, 416*, Article 127951. DOI: 10.1016/j.apenergy.2026.127951
