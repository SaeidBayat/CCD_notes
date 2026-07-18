# Chapter Summary and Problems

## Summary

Shooting optimizes control parameters and simulates states, but may be ill-conditioned over long or unstable horizons. Multiple shooting shortens sensitivity propagation using segment states and continuity constraints. Direct transcription optimizes states and controls simultaneously and replaces dynamics with sparse defects. Collocation schemes trade polynomial order, mesh size, and robustness. Accurate sparse derivatives, scaling, initialization, continuation, refinement, dense constraint checks, and independent simulation are essential for numerical credibility.

## Key terms

Time discretization; mesh; control parameterization; direct shooting; multiple shooting; direct transcription; collocation; defect; quadrature; Euler forward; trapezoidal rule; Hermite–Simpson; pseudospectral method; sparse NLP; Jacobian sparsity; automatic differentiation; complex step; mesh refinement; warm start; continuation; independent simulation.

## Conceptual problems

1. Why is continuous optimal control infinite-dimensional?
2. Distinguish sequential and simultaneous direct methods.
3. Why can a transcription with thousands of variables remain manageable?
4. What is the physical meaning of a defect?
5. Why does node feasibility not guarantee continuous path feasibility?

## Time-discretization problems

6. Construct a uniform 20-interval mesh on $[0,10]$.
7. Propose a nonuniform mesh for a fast initial transient.
8. Estimate variables for 12 states, 4 controls, 200 intervals, 8 plant variables, and 6 controller parameters.
9. When is piecewise-constant control more physical than piecewise-linear control?
10. Why can a global polynomial struggle with bang–bang control?

## Shooting problems

11. Formulate direct shooting for $\dot{x}=ax+bu$ with five constant-control intervals.
12. Why are tight terminal constraints difficult for single shooting?
13. Derive state sensitivity for $\dot{x}=f(x,q,t)$ with respect to $q$.
14. Write continuity constraints for three-segment multiple shooting.
15. Compare single- and multiple-shooting decisions.

## Defect problems

16. Derive the Euler defect for $\dot{x}=-2x+u$.
17. Derive the trapezoidal defect for the same system.
18. Write the vector trapezoidal defect for $\dot{\mathbf{x}}=A\mathbf{x}+B\mathbf{u}$.
19. Write Hermite–Simpson midpoint and defect formulas.
20. Why are implicit formulas convenient in transcription?

## Sparse-NLP and derivative problems

21. Sketch trapezoidal-defect Jacobian sparsity for six intervals with one state and control.
22. Explain sparse finite-difference coloring.
23. Compare forward finite differences and complex step.
24. Derive Euler-defect Jacobian blocks with respect to $x_k$, $x_{k+1}$, and $u_k$.
25. When is reverse-mode AD attractive?

## Mesh and verification problems

26. Define objective and design convergence metrics for refinement.
27. Distinguish $h$-, $p$-, and $hp$-refinement.
28. List five checks after solver success.
29. Describe independent simulation for a transcription result.
30. Why are multiple starts still needed after mesh convergence?

## Computational and mini-project problems

31. Implement Euler and trapezoidal integration for $\dot{x}=-x$, $x(0)=1$, and verify their orders.
32. Solve a minimum-effort double-integrator transfer using shooting.
33. Solve the same problem using trapezoidal transcription and compare.
34. Refine at least four meshes and plot objective error, terminal error, and maximum defect.
35. Verify a hand-coded Jacobian using complex step.
36. Compare two numerical methods on the same small CCD formulation and tolerances.
37. Solve a nonlinear CCD problem with plant variables and a control trajectory, documenting formulation, scaling, mesh, transcription, derivatives, solver, refinement, independent simulation, and interpretation.

## References and further reading

1. Herber, D. R. (2017). *Advances in combined architecture, plant, and control design* (Doctoral dissertation, University of Illinois at Urbana–Champaign). Illinois Digital Environment for Access to Learning and Scholarship. https://www.ideals.illinois.edu/items/105359

2. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577

3. Biegler, L. T. (2010). *Nonlinear programming: Concepts, algorithms, and applications to chemical processes*. Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898719383

4. Kelly, M. (2017). An introduction to trajectory optimization: How to do your own direct collocation. *SIAM Review, 59*(4), 849–904. DOI: 10.1137/16M1062569

5. Rao, A. V. (2009). A survey of numerical methods for optimal control. *Advances in the Astronautical Sciences, 135*, 497–528.

6. Patterson, M. A., & Rao, A. V. (2014). GPOPS-II: A MATLAB software for solving multiple-phase optimal control problems using hp-adaptive Gaussian quadrature collocation methods. *ACM Transactions on Mathematical Software, 41*(1), Article 1, 1–37. DOI: 10.1145/2558904

7. Nocedal, J., & Wright, S. J. (2006). *Numerical optimization* (2nd ed.). Springer. DOI: 10.1007/978-0-387-40065-5

8. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

9. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705
