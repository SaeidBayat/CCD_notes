# Chapter Summary and Problems

## Summary

Engineering design optimization formalizes a search using design variables, an objective, a predictive model, and constraints. The feasible space contains acceptable designs, and active constraints often explain the optimum. Nonlinear engineering problems can contain multiple local optima, so initialization and exploration matter. Gradient-based algorithms use derivative information efficiently; constrained methods balance improvement against active requirements. Scaling and conditioning strongly influence numerical reliability. MDO extends optimization across coupled disciplines, while dynamic-system optimization introduces trajectories, integral objectives, and path constraints.

```{admonition} Central lesson
:class: important
Optimization is valuable when its formulation, model, derivatives, scaling, convergence evidence, and engineering interpretation are all credible. A solver result alone is not a design decision.
```

## Key terms

Design variable; objective function; equality constraint; inequality constraint; bound; feasible design; infeasible design; active constraint; local optimum; global optimum; convexity; gradient; Hessian; line search; Newton method; quasi-Newton method; KKT conditions; Lagrange multiplier; scaling; conditioning; multidisciplinary design optimization; coupling variable; path constraint; boundary constraint.

## Conceptual problems

1. Explain the difference between engineering analysis and engineering design optimization.
2. Why is the optimization algorithm not always the most important part of an optimization study?
3. Give three examples each of continuous, integer, binary, and functional design variables.
4. Explain the difference between a preference and a requirement. Which normally belongs in the objective and which in the constraints?
5. Why does convergence not prove that a global optimum was found?

## Formulation problems

6. Formulate a minimum-mass cantilever beam problem with width and height as variables, tip-deflection and stress limits, and geometric bounds.
7. Formulate a battery-pack problem that minimizes mass while meeting energy, power, voltage, and temperature requirements.
8. Formulate a wind-turbine blade problem that maximizes annual energy production subject to stress, deflection, fatigue, and manufacturability limits.
9. Rewrite $\max_{\mathbf{x}}P(\mathbf{x})$ in minimization form.
10. Convert $\sigma(\mathbf{x})\leq250$ MPa to a dimensionless $g(\mathbf{x})\leq0$ constraint.

## Feasible-space and optimality problems

11. Sketch the feasible region defined by $x_1+x_2\leq4$, $x_1\geq0$, and $x_2\geq0$.
12. At $(x_1,x_2)=(1,2)$, classify $x_1+x_2-3\leq0$ and $x_1^2+x_2^2-10\leq0$ as active, inactive, or violated.
13. Explain why a minimum-mass design often has active strength or stiffness constraints.
14. Give an engineering example with a disconnected feasible set.
15. Describe how Lagrange multipliers can help prioritize which requirement to relax.

## Gradient and algorithm problems

16. Compute the gradient and Hessian of $f(x_1,x_2)=3x_1^2+2x_1x_2+4x_2^2$.
17. Starting from $(2,1)$, perform two gradient-descent iterations for Problem 16 with $\alpha=0.1$.
18. Find the stationary point of $f(x_1,x_2)=x_1^2+2x_2^2-4x_1-8x_2$.
19. Explain the difference between line-search and trust-region methods.
20. Compare analytical derivatives, finite differences, complex step, and automatic differentiation.

## Scaling problems

21. A problem contains thickness $t\approx0.005$ m and cost $C\approx2\times10^6$ dollars. Propose a scaled variable and objective.
22. Map $20\leq x\leq120$ to $[0,1]$.
23. Explain why an absolute tolerance of $10^{-6}$ may be inappropriate for a force-balance equation measured in newtons.
24. For $f=10^8x_1^2+x_2^2$, propose a coordinate scaling that balances curvature.
25. Give an example of physical ill-conditioning that scaling cannot eliminate.

## MDO and dynamic optimization problems

26. Identify at least three disciplines and four coupling variables in electric-aircraft design.
27. Explain why plant and control design form a multidisciplinary coupled problem.
28. Write a dynamic objective that balances tracking error and control effort.
29. Give four examples of path constraints and two examples of boundary constraints.
30. For the mass–spring–damper CCD example, identify plant variables, controller variables, states, disturbances, objective terms, and constraints.

## Computational and mini-project problems

31. Use MATLAB or Python to solve Worked Example 3.2 from at least four starting points. Compare convergence histories.
32. Implement gradient descent for a poorly scaled quadratic before and after variable scaling. Compare iteration counts.
33. Solve the pressure-vessel formulation using reasonable numerical values. Report the optimum and active constraints.
34. Choose a two-variable constrained problem and plot its feasible region, initial design, final design, and active constraints.
35. Formulate and solve a small engineering optimization problem. Submit a 5–7 page report containing the mission, variables, model, objective, constraints, scaling, solver, initial guesses, convergence evidence, active constraints, and engineering interpretation.

## References and further reading

1. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

2. Nocedal, J., & Wright, S. J. (2006). *Numerical optimization* (2nd ed.). Springer. DOI: 10.1007/978-0-387-40065-5

3. Boyd, S., & Vandenberghe, L. (2004). *Convex optimization*. Cambridge University Press. DOI: 10.1017/CBO9780511804441

4. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

5. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705
