# Chapter Summary and Problems

## Summary

The active-suspension tutorial connected a dynamic model to a system-level CCD formulation and showed how to compare sequential, nested, and simultaneous architectures. The wind–wave application extended the principles to expensive multiphysics systems, many operating conditions, and multiple controllers. Scenario, worst-case, chance-constrained, and risk-aware methods addressed uncertainty. Staged fidelity and surrogates supported efficient exploration without replacing high-fidelity checks. Hardware constraints, reproducibility, and validation completed the path from an optimization result to credible engineering evidence.

CCD is not complete when the optimizer stops. It is complete when the coordinated design is explained, numerically verified, tested against uncertainty, checked at suitable fidelity, translated into realizable hardware and control, and documented reproducibly.

## Key terms

Practical CCD study; active suspension; fair baseline; system-level objective; nominal optimum; robust optimization; scenario optimization; chance constraint; CVaR; model fidelity; surrogate model; multi-fidelity optimization; infill; cross-fidelity validation; software-in-the-loop; hardware-in-the-loop; passive safety; reproducibility; verification; validation.

## Conceptual problems

1. Explain the difference between a numerically optimal design and a practically credible CCD design.
2. Why is an active vehicle suspension a useful CCD tutorial?
3. Why is suspension travel often better represented as a path constraint than as an objective term?
4. Why can a low aggregate objective hide an unacceptable design?
5. Distinguish verification from validation.

## Suspension-modeling problems

6. Derive the state-space form of the quarter-car equations using $[z_s,\dot z_s,z_u,\dot z_u]^T$.
7. Add tire damping $c_t(\dot z_u-\dot z_r)$ and derive the revised equations.
8. Identify at least five plant and five control variables for a higher-fidelity active suspension.
9. Propose a physically meaningful suspension-actuator power model.
10. Write plant constraints for spring packaging, actuator stroke, and maximum component mass.

## Architecture-comparison problems

11. Write sequential, nested, and simultaneous formulations for the same suspension objective.
12. List the conditions required for a fair comparison among the three methods.
13. Why may nested and simultaneous CCD target the same optimum yet produce different numerical results?
14. Give three reasons why sequential design may remain attractive in industry.
15. Design a results table with enough information for a critical comparison.

## Uncertainty and robustness problems

16. Define six uncertainty sources for an active suspension and classify each as aleatory or epistemic.
17. Formulate a nine-scenario expected-value objective using three roads and three payloads.
18. Write a worst-case version of the same problem.
19. Write a chance constraint requiring suspension-travel limits to hold with probability at least $0.999$.
20. Explain the tradeoff between nominal performance and robustness.

## Model-fidelity and surrogate problems

21. Propose low-, medium-, and high-fidelity models for the suspension.
22. Give four model details that could change its optimized design.
23. Outline a surrogate-assisted workflow for an expensive wind-turbine model.
24. Why may a surrogate predicting only scalar metrics be inadequate for controller optimization?
25. Define a plan that validates surrogate accuracy near the predicted optimum.

## Wind and wave energy problems

26. List at least eight plant and six control variables for a hybrid floating wind–wave system.
27. Construct a multiobjective formulation balancing annual energy, motion, fatigue, and capital cost.
28. Define five path constraints for the application.
29. How may WEC placement affect both wave-energy capture and wind-turbine platform motion?
30. Propose a multi-fidelity optimization and validation plan.

## Implementation and reproducibility problems

31. Add actuator bandwidth, sampling delay, and sensor noise to the suspension formulation.
32. Explain passive safety and propose one passive-safety suspension requirement.
33. Design software-in-the-loop, HIL, and bench-test stages for an optimized controller.
34. Create a reproducibility checklist for a numerical CCD paper.
35. Explain how independent forward simulation validates a direct-transcription solution.

## Course capstone

36. Select an actively controlled engineering system and complete a full CCD study. Include a sequential baseline; nested or simultaneous formulation; convergence checks; uncertainty analysis; at least two fidelity levels; an implementation plan; and a reproducible package of equations, code, data, and solver settings.
37. Prepare a ten-minute design review explaining the result, why the design changed physically, the evidence supporting it, and remaining risks before deployment.

## References and further reading

1. Allison, J. T., Guo, T., & Han, Z. (2014). Co-design of an active suspension using simultaneous dynamic optimization. *Journal of Mechanical Design, 136*(8), Article 081003.

2. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

3. Herber, D. R. (2017). *Advances in combined architecture, plant, and control design* (Doctoral dissertation, University of Illinois at Urbana–Champaign). Illinois Digital Environment for Access to Learning and Scholarship. https://www.ideals.illinois.edu/items/105359

4. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

5. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

6. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577

7. Lee, Y. H., Bayat, S., & Allison, J. T. (2025). Wind turbine control co-design using dynamic system derivative function surrogate model (DFSM) based on OpenFAST linearization. *Applied Energy, 396*, Article 126203. [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S030626192500933X)

8. Bayat, S., Peterson, C., Lee, Y. H., Iori, J., & Allison, J. T. (2026). Advancing wind turbines through control co-design: An integrative review. *Applied Energy, 416*, Article 127951. [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S0306261926006033)

9. Mayne, D. Q., Rawlings, J. B., Rao, C. V., & Scokaert, P. O. M. (2000). Constrained model predictive control: Stability and optimality. *Automatica, 36*(6), 789–814. DOI: 10.1016/S0005-1098(99)00214-9
