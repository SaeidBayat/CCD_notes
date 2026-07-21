# Chapter Summary and Problems

## Summary

Shooting optimizes control parameters and simulates states, but may be ill-conditioned over long or unstable horizons. Multiple shooting shortens sensitivity propagation using segment states and continuity constraints. Direct transcription optimizes states and controls simultaneously and replaces dynamics with sparse defects. Collocation schemes trade polynomial order, mesh size, and robustness. Accurate sparse derivatives, scaling, initialization, continuation, refinement, dense constraint checks, and independent simulation are essential for numerical credibility.

## Key terms

Time discretization; mesh; control parameterization; direct shooting; multiple shooting; direct transcription; collocation; defect; quadrature; Euler forward; trapezoidal rule; Hermite–Simpson; zero-order hold; pseudospectral method; Legendre–Gauss (LG), Legendre–Gauss–Radau (LGR), and Legendre–Gauss–Lobatto (LGL) points; differentiation matrix; static parameters; sparse NLP; Jacobian sparsity; $hp$-adaptive mesh refinement; automatic differentiation; complex step; dependency detection; mesh refinement; warm start; continuation; independent simulation.

## Problems

1. **Single-shooting sensitivity and conditioning.** For $\dot x=f(x,u(t;c),p)$ with terminal residual $r=x(T)-x_T$, derive the exact Jacobian $\partial r/\partial(p,c)$ from variational equations and show why its norm can grow exponentially with the horizon for unstable dynamics.

2. **Multiple-shooting Jacobian.** Partition $[0,T]$ into $N$ shooting intervals with independent initial states $s_i$. Derive the continuity constraints and their block-bidiagonal Jacobian, then prove how this structure limits sensitivity growth relative to single shooting.

3. **Hermite--Simpson transcription.** Transcribe $\min\Phi(x_N)+\int_0^T L(x,u,p)dt$ subject to $\dot x=f(x,u,p)$ using Hermite--Simpson collocation, deriving the midpoint state, midpoint dynamics, defect equation, and Simpson quadrature contribution for one generic interval.

4. **Legendre--Gauss--Radau collocation.** On one mesh interval, derive the LGR differentiation matrix and quadrature weights from the Lagrange basis, then express the state defects and endpoint update in a form suitable for a sparse nonlinear program.

5. **Sparse KKT complexity.** A direct transcription has $n_x$ states, $n_u$ controls, $n_p$ global plant variables, and $N$ intervals. Derive the asymptotic nonzero counts of the constraint Jacobian and KKT matrix and compare time-ordered sparse factorization with dense factorization.

6. **Derivative verification.** For a collocation NLP residual $F(z)$, derive truncation and roundoff error models for forward, central, complex-step, and algorithmic derivatives, then prescribe a numerical test that distinguishes a coding error from finite-difference noise.

7. **Goal-oriented mesh refinement.** Given collocation defects $d_i(t)$ and an adjoint $\lambda(t)$ for the objective, derive an adjoint-weighted local error indicator and a mesh-refinement rule that targets objective error rather than state error alone.

8. **hp-adaptive decision.** Suppose the estimated local error behaves as $C_ph^{p+1}$ for a smooth solution but only $C_sh^\nu$ near a nonsmooth control switch. Construct an hp-adaptive rule that chooses polynomial enrichment or interval subdivision from observed coefficient decay and justify its asymptotic behavior.

9. **Post-solution optimality audit.** For a transcribed CCD nonlinear program, define a single normalized verification metric combining primal feasibility, dual feasibility, complementarity, mesh defect, and objective stability under refinement, with scaling that prevents any physical unit from dominating the audit.

10. **Numerical convergence study.** For $\min\int_0^1(x^2+10^{-2}u^2)dt$ subject to $\dot x=-px+u$, $x(0)=1$, $x(1)=0$, $0.1\le p\le3$, and $|u|\le2$, design a reproducible comparison of trapezoidal, Hermite--Simpson, and LGR transcription that estimates each method's observed convergence order and separates discretization error from NLP termination error.

## References and further reading

1. Herber, D. R. (2017). *Advances in combined architecture, plant, and control design* (Doctoral dissertation, University of Illinois at Urbana–Champaign). Illinois Digital Environment for Access to Learning and Scholarship. https://www.ideals.illinois.edu/items/105359

2. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577

3. Biegler, L. T. (2010). *Nonlinear programming: Concepts, algorithms, and applications to chemical processes*. Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898719383

4. Kelly, M. (2017). An introduction to trajectory optimization: How to do your own direct collocation. *SIAM Review, 59*(4), 849–904. DOI: 10.1137/16M1062569

5. Rao, A. V. (2009). A survey of numerical methods for optimal control. *Advances in the Astronautical Sciences, 135*, 497–528.

6. Garg, D., Patterson, M., Hager, W. W., Rao, A. V., Benson, D. A., & Huntington, G. T. (2010). A unified framework for the numerical solution of optimal control problems using pseudospectral methods. *Automatica, 46*(11), 1843–1851. DOI: 10.1016/j.automatica.2010.06.048

7. Patterson, M. A., & Rao, A. V. (2014). GPOPS-II: A MATLAB software for solving multiple-phase optimal control problems using hp-adaptive Gaussian quadrature collocation methods. *ACM Transactions on Mathematical Software, 41*(1), Article 1, 1–37. DOI: 10.1145/2558904

8. Nocedal, J., & Wright, S. J. (2006). *Numerical optimization* (2nd ed.). Springer. DOI: 10.1007/978-0-387-40065-5

9. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

10. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705
