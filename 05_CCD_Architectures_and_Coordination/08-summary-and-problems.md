# Chapter Summary and Problems

## Summary

Single-pass design is simple and inexpensive but weakly coordinated. Iterative sequential design exchanges information repeatedly while preserving disciplinary subproblems. Nested CCD evaluates each plant through an inner optimal controller and can be computationally costly. Simultaneous CCD solves all coupled decisions in one problem and provides the strongest coordination, at the cost of numerical and software complexity.

Architectures can target the same ideal solution yet behave differently because of initialization, local minima, derivative quality, scaling, approximate solves, and stopping criteria. Architecture choice should reflect both mathematical coupling and practical engineering constraints. A controlled, implementation-fair comparison shows that two of these practical factors — derivative-method availability and inner-loop feasibility — can matter more than the choice of architecture itself, and that nested CCD's bi-level structure connects directly to the multidisciplinary feasible (MDF) formulation used more broadly in multidisciplinary design optimization.

## Key terms

CCD architecture; coordination strategy; single-pass sequential design; iterative sequential design; nested CCD; simultaneous CCD; outer loop; inner loop; bi-level optimization; one-level optimization; mathematical equivalence; practical difference; coupling strength; computational tradeoff; legacy tools; derivative availability; multidisciplinary feasible (MDF); individual disciplinary feasible (IDF); augmented Lagrangian coordination (ALC); analytical target cascading (ATC); induced region; outer-loop feasibility constraint; inner-loop feasibility; derivative method (symbolic, complex-step, finite difference); direct transcription; algebraic Riccati equation.

## Problems

1. **Convergence of iterated sequential design.** Let $J(p,c)=\tfrac12p^TH_{pp}p+p^TH_{pc}c+\tfrac12c^TH_{cc}c-b_p^Tp-b_c^Tc$ with a positive-definite joint Hessian. Derive the exact iteration matrix for alternating plant and control minimization and prove the necessary and sufficient spectral condition for linear convergence.

2. **Nested value-function gradient.** The inner optimal-control problem defines $\psi(p)=\min_{x,u}J(p,x,u)$ subject to transcription constraints $c(p,x,u)=0$ and $g(p,x,u)\le0$. Under strong regularity, derive $\nabla_p\psi$ from the inner KKT multipliers and show its equivalence to simultaneous first-order stationarity.

3. **Failure of nested differentiability.** Consider $\psi(p)=\min_c(c^2-p)^2+\rho c^2$. Determine all lower-level minimizers and derive the points at which the value function or optimizer mapping loses differentiability, explaining the consequence for a gradient-based outer loop.

4. **Simultaneous transcription structure.** For $\dot x=f(x,u,p)$ transcribed by a one-step defect on $N$ intervals, order the NLP variables by time and derive the block sparsity pattern of its constraint Jacobian and Lagrangian Hessian, including the dense columns created by time-invariant plant variables.

5. **Nested infeasibility restoration.** The inner problem is infeasible for some $p$ because $g(p,x,u)\le0$ cannot be satisfied. Construct an exact-penalty feasibility-restoration inner problem that defines a finite outer value for every bounded $p$, and derive a condition on the penalty weight under which feasible local minima of the original problem are preserved.

6. **Fair comparison of coordination strategies.** For the active quarter-car equations $M(p)\ddot q+C(p)\dot q+K(p)q=B_uu+B_ww$, specify a numerical experiment that compares nested and simultaneous CCD under identical discretization, tolerances, derivatives, starts, bounds, and feasibility tests, reducing the comparison to one statistically defensible performance metric.

7. **Augmented-Lagrangian coordination.** Split a CCD problem into plant and control subproblems coupled through a trajectory copy $y_p(t)=y_c(t)$. Derive an augmented-Lagrangian iteration with multiplier and penalty updates and state a residual-based stopping condition that certifies coupling consistency.

8. **Architecture selection as mixed-integer CCD.** A suspension may contain a passive spring, damper, active actuator, and tuned-mass absorber, each selected by a binary variable. Formulate a mixed-integer dynamic optimization problem with logical sizing bounds, a component-count penalty, common ride and handling metrics, and physically valid dynamics for every selected topology.

9. **Computational break-even analysis.** A nested solve requires $n_o$ outer iterations and an average of $n_i$ inner NLP solves, whereas a simultaneous solve has $n_z$ variables and a sparse KKT factorization cost proportional to $n_z^\alpha$. Derive a break-even inequality that includes derivative cost, warm-start savings, parallelism, and the probability of inner infeasibility.

10. **Architecture-selection rule.** Given estimates of coupling strength, inner-problem failure rate, derivative availability, transcription size, and required solution accuracy, construct a quantitative decision rule that selects single-pass sequential, iterated sequential, nested, or simultaneous CCD and justify the rule using conditioning and convergence arguments.

## References and further reading

1. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

2. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

3. Garcia-Sanz, M. (2019). Control co-design: An engineering game changer. *Advanced Control for Applications: Engineering and Industrial Systems, 1*(1), Article e18. DOI: 10.1002/adc2.18

4. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

5. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577

6. Sundarrajan, A. K., & Herber, D. R. (2021). Towards a fair comparison between the nested and simultaneous control co-design methods using an active suspension case study. In *2021 American Control Conference (ACC)* (pp. 358–365).
