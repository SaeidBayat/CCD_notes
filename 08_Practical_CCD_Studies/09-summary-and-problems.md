# Chapter Summary and Problems

## Summary

The active-suspension tutorial connected a dynamic model to a system-level CCD formulation and showed how to compare sequential, nested, and simultaneous architectures. The wind–wave application extended the principles to expensive multiphysics systems, many operating conditions, and multiple controllers. Scenario, worst-case, chance-constrained, and risk-aware methods addressed uncertainty. Staged fidelity and surrogates supported efficient exploration without replacing high-fidelity checks. Hardware constraints, reproducibility, and validation completed the path from an optimization result to credible engineering evidence.

CCD is not complete when the optimizer stops. It is complete when the coordinated design is explained, numerically verified, tested against uncertainty, checked at suitable fidelity, translated into realizable hardware and control, and documented reproducibly.

## Key terms

Practical CCD study; active suspension; fair baseline; system-level objective; nominal optimum; robust optimization; scenario optimization; chance constraint; CVaR; aleatory and epistemic uncertainty; uncertain control co-design (UCCD); worst-case robust CCD (WCR-UCCD); epigraph reformulation; matched and mismatched uncertainty; model fidelity; surrogate model; derivative function surrogate model (DFSM); linear parameter-varying (LPV) surrogate; multi-fidelity optimization; infill; cross-fidelity validation; software-in-the-loop; hardware-in-the-loop; passive safety; trilevel architecture-plant-control design; reproducibility; verification; validation.

## Problems

1. **Detailed active-suspension CCD.** A quarter car satisfies $m_s\ddot z_s=-k_s(z_s-z_u)-c_s(\dot z_s-\dot z_u)+F$, $m_u\ddot z_u=k_s(z_s-z_u)+c_s(\dot z_s-\dot z_u)-k_t(z_u-r)-F$. Formulate a simultaneous CCD problem over spring geometry, damping, actuator rating, and $F(t)$ that minimizes ride acceleration and control energy while enforcing suspension travel, tire load, fatigue, buckling, packaging, and passive-failure constraints.

2. **Chance-constrained suspension travel.** Let uncertain parameters $\theta=[m_s,k_t,c_s]^T\sim\mathcal N(\bar\theta,\Sigma)$ and $g(t,\theta)=|z_s(t)-z_u(t)|-r_{\max}$. Derive a first-order, two-sided deterministic approximation guaranteeing $\mathbb P[g(t_j,\theta)\le0\ \forall j]\ge0.999$ using sensitivity propagation and an explicit allocation of risk across time nodes.

3. **Surrogate selection under a fixed budget.** A DFSM surrogate has structural bias $B_D^2$, variance $\alpha p/N$, and evaluation cost $c_D$, while an LSTM has bias $B_L^2<B_D^2$, variance $\beta W/N$, and cost $c_L>c_D$. Derive a budget-dependent decision boundary that selects the model giving the lowest expected validation error after accounting for training, optimization evaluations, and iterative infill.

4. **Trust-region multi-fidelity CCD.** With low- and high-fidelity objectives $J_L(z)$ and $J_H(z)$, construct an additive first-order discrepancy model inside $\|z-z_k\|\le\Delta_k$ and derive fully-linear error constants and an acceptance rule sufficient for convergence to first-order stationarity of $J_H$.

5. **Fatigue-limited spring design.** A helical spring has $k_s=Gd^4/(8D^3N_a)$ and corrected shear stress $\tau=K_w(D/d)8FD/(\pi d^3)$. Formulate and solve the minimum-mass spring design subject to target stiffness, Soderberg fatigue, spring-index, buckling, and packaging constraints, identifying the active set as load amplitude varies.

6. **Floating-wind-turbine co-design.** A linear parameter-varying model is $\dot x=A(V,p)x+B_u(V,p)u+B_w(V,p)w$, where $p$ contains platform and tower variables. Formulate a multi-operating-point CCD problem minimizing levelized cost of energy while constraining fatigue-equivalent loads, platform pitch, generator speed, actuator usage, stability margin, and annual-energy production.

7. **Hardware-aware implementation.** A digital controller has sample period $h$, computation delay $\tau_d$, quantization step $\Delta_y$, and actuator rate limit $\dot u_{\max}$. Derive an augmented closed-loop model and one robust feasibility certificate that guarantees stability and constraint satisfaction for all admissible delays and quantization errors.

8. **Statistical validation of CCD benefit.** Given paired sequential and CCD performance samples over $M$ common uncertainty realizations and $N$ multistart solutions per formulation, derive a hierarchical bootstrap confidence interval for the percentage improvement and a preregistered acceptance rule that accounts for optimization-path variability, feasibility violations, and multiple metrics.

9. **Architecture-value attribution.** For design domains $D=\{\text{architecture},\text{plant},\text{control}\}$, define a coalition value as the verified improvement obtained when only domains in $S\subseteq D$ are optimized. Derive all three Shapley values and specify the minimum set of controlled optimization runs required to estimate them without confounding domain interactions.

10. **Reproducible end-to-end study.** For an actively controlled engineering system of your choice with explicit dynamics $\dot x=f(x,u,p,w)$, design one complete computational experiment that compares a sequential baseline with CCD and yields a defensible claim through formulation disclosure, derivative checks, mesh convergence, multistart analysis, uncertainty validation, high-fidelity verification, and archived solver metadata.

## References and further reading

1. Allison, J. T., Guo, T., & Han, Z. (2014). Co-design of an active suspension using simultaneous dynamic optimization. *Journal of Mechanical Design, 136*(8), Article 081003.

2. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

3. Deshmukh, A. P., Herber, D. R., & Allison, J. T. (2015). Bridging the gap between open-loop and closed-loop control in co-design: A framework for complete optimal plant and control architecture design. In *2015 American Control Conference (ACC)* (pp. 4916–4922).

4. Herber, D. R. (2017). *Advances in combined architecture, plant, and control design* (Doctoral dissertation, University of Illinois at Urbana–Champaign). Illinois Digital Environment for Access to Learning and Scholarship. https://www.ideals.illinois.edu/items/105359

5. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

6. Sundarrajan, A. K., & Herber, D. R. (2021). Towards a fair comparison between the nested and simultaneous control co-design methods using an active suspension case study. In *2021 American Control Conference (ACC)* (pp. 358–365).

7. Azad, S., & Herber, D. R. (2023). An overview of uncertain control co-design formulations. *Journal of Mechanical Design, 145*(9), Article 091709. DOI: 10.1115/1.4062753

8. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

9. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577

10. Lee, Y. H., Bayat, S., & Allison, J. T. (2025). Wind turbine control co-design using dynamic system derivative function surrogate model (DFSM) based on OpenFAST linearization. *Applied Energy, 396*, Article 126203. [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S030626192500933X)

11. Sundarrajan, A. K., & Herber, D. R. (2025). Comparison of data-driven modeling approaches for control optimization of floating offshore wind turbines. In *Proceedings of the ASME 2025 International Design Engineering Technical Conferences and Computers and Information in Engineering Conference (IDETC-CIE2025)*, Article DETC2025-167963.

12. Bayat, S., Peterson, C., Lee, Y. H., Iori, J., & Allison, J. T. (2026). Advancing wind turbines through control co-design: An integrative review. *Applied Energy, 416*, Article 127951. [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S0306261926006033)

13. Mayne, D. Q., Rawlings, J. B., Rao, C. V., & Scokaert, P. O. M. (2000). Constrained model predictive control: Stability and optimality. *Automatica, 36*(6), 789–814. DOI: 10.1016/S0005-1098(99)00214-9
