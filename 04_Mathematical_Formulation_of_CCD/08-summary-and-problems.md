# Chapter Summary and Problems

## Summary

A CCD formulation identifies plant and controller decisions, state and control trajectories, performance objectives, physical equality constraints, time-dependent path constraints, endpoint boundary constraints, and variable bounds. Lagrange objectives measure accumulated behavior, Mayer objectives measure terminal behavior, and Bolza objectives combine both. The resulting continuous-time problem is infinite-dimensional and must later be transcribed into a finite nonlinear program.

```{admonition} Central lesson
:class: important
Formulation bridges engineering intuition and numerical computation. It states precisely what can change, what should improve, and what must remain true.
```

## Key terms

Plant design variables; control design variables; state trajectory; control trajectory; equality constraint; path constraint; boundary constraint; running cost; terminal cost; Lagrange objective; Mayer objective; Bolza objective; feasible trajectory; bounds; formulation; dynamic optimization.

## Conceptual problems

1. Explain why a CCD problem needs a mathematical formulation before numerical solution.
2. Give three plant and three control variables for a robot manipulator.
3. Explain the difference between $\mathbf{x}_c$ and $u(t)$.
4. Why are state trajectories necessary in dynamic but not simple static optimization?
5. Describe a situation where a path constraint is more appropriate than a boundary constraint.

## Formulation problems

6. Formulate a mass–spring–damper CCD problem with $k$ and $K_p$ as decisions, one objective, and one path constraint.
7. For cruise control with state $v(t)$ and traction force $F_t(t)$, write an equality, path, and boundary constraint.
8. A manipulator moves from $q_0$ to $q_f$ in fixed time $t_f$. Write its boundary constraints.
9. Write a Lagrange objective penalizing tracking error $e(t)$ and effort $u(t)$.
10. Write a Mayer objective minimizing $x_3(t_f)$.

## Classification problems

11. Classify actuator torque limit, rotor speed, pitch gain, wave elevation, and buoy radius as plant variables, control variables, states, disturbances, or constraints.
12. Classify maximum motor temperature, desired final position, maximum suspension travel, periodicity, and minimum final battery energy as path or boundary constraints.
13. Identify the Lagrange and Mayer terms in

    ```{math}
    J=5x_1(t_f)^2+\int_0^{10}\left(x_2(t)^2+0.3u(t)^2\right)dt.
    ```

14. Is $x(0)=x_0$ a dynamic equation, path constraint, or boundary constraint? Explain.
15. Explain why $|u(t)|\leq2$ for all $t$ is not a simple bound on $\mathbf{x}_c$ unless control is already parameterized.

## Modeling problems

16. Write a generic continuous-time active-suspension CCD formulation with plant variables, controller variables, states, and input.
17. Write a Bolza objective for wind-turbine design that values power while penalizing tower loading and control activity.
18. Write constraints for a marine energy device with a PTO-force limit, pitch-angle limit, and required final stored energy.
19. Give an algebraic equality constraint that could appear in CCD.
20. For a fixed initial state and free final state, write a general boundary-condition statement.

## Analytical problems

21. Show how a Bolza objective reduces to Lagrange form.
22. Show how a Bolza objective reduces to Mayer form.
23. Why is the continuous-time CCD problem infinite-dimensional?
24. Explain how plant variables in the dynamics change the feasible trajectory set.
25. A student says, “The simulator already knows the dynamics, so they are not constraints.” Explain why this is incorrect from an optimization viewpoint.

## Computational and mini-project problems

26. Choose a system and list plant variables, control variables, states, disturbances, an objective, a path constraint, and a boundary constraint.
27. Write a one-page CCD formulation memo from your research area, explaining every decision, objective, and constraint.
28. Simulate a simple system and approximate

    ```{math}
    J=\int_0^T(x(t)^2+u(t)^2)dt
    ```

    on successively refined time grids. Report convergence of the approximation.
29. For $u(t)=Kx(t)$, compare the optimization variable set with one in which $u(t)$ is optimized directly.
30. Formulate a complete CCD problem for a suspension, robot, wind turbine, or marine-energy device, justifying the plant variables, controller variables, states, objective, and constraints.

## References and further reading

1. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

2. Allison, J. T., Guo, T., & Han, Z. (2014). Co-design of an active suspension using simultaneous dynamic optimization. *Journal of Mechanical Design, 136*(8), Article 081003.

3. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

4. Garcia-Sanz, M. (2019). Control co-design: An engineering game changer. *Advanced Control for Applications: Engineering and Industrial Systems, 1*(1), Article e18. DOI: 10.1002/adc2.18

5. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

6. Bryson, A. E., Jr., & Ho, Y.-C. (1975). *Applied optimal control: Optimization, estimation, and control*. Hemisphere Publishing Corporation.

7. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577
