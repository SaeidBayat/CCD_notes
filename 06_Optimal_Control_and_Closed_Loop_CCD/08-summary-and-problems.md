# Chapter Summary and Problems

## Summary

OLOC directly optimizes a control trajectory and is valuable for ideal performance benchmarks, qualitative insight, and plant-design studies. It can also assume future information unavailable to a real controller. Controller-parameter optimization instead designs an implementable feedback policy. Feedback-controller CCD combines physical and policy decisions and evaluates them under measurements and realized disturbances. MPC bridges these views by repeatedly solving a short open-loop problem using updated information.

## Key terms

Open-loop optimal control; control trajectory; controller parameterization; feedback controller; feedback-controller co-design; future information; information availability; measured state; estimated state; forecast; implementable controller; model predictive control; receding horizon; prediction horizon; benchmark solution; realizability.

## Conceptual problems

1. Define open-loop optimal control.
2. What is the difference between a trajectory and a controller?
3. Why is feedback usually required in engineering systems?
4. What does perfect future information mean in OLOC?
5. Why is MPC feedback even though it solves open-loop subproblems?

## Comparison problems

6. Compare open-loop and feedback control in their information usage.
7. Compare trajectory and controller-parameter optimization.
8. Compare an ideal OLOC solution with MPC implementation.
9. Give one advantage and limitation of OLOC in CCD.
10. Give one advantage and limitation of feedback-controller CCD.

## Formulation problems

11. Write a generic OLOC problem with dynamics and path constraints.
12. Write $\mathbf{u}=\boldsymbol{\kappa}(\mathbf{y};\mathbf{x}_c)$ and explain every symbol.
13. Write a feedback-controller CCD problem with $\mathbf{x}_p$ and $\mathbf{x}_c$.
14. List the operations performed by MPC at one time step.
15. Explain how decisions change when moving from OLOC to feedback-controller CCD.

## Interpretation problems

16. “The open-loop optimum is best, so it is the controller we should implement.” Explain the flaw.
17. “MPC is not feedback because it computes an open-loop plan.” Explain why this is incomplete.
18. Why can the best plant under OLOC differ from the best under feedback?
19. How does forecast uncertainty reduce OLOC usefulness?
20. How can plant redesign improve controller information?

## Application problems

21. Explain how OLOC could support preliminary active-suspension design before feedback synthesis.
22. For wind-turbine control, give one measured and one forecast quantity.
23. Why is wave-record OLOC useful but insufficient for final marine-energy control?
24. Choose a system and decide between direct feedback CCD and an OLOC-first workflow.
25. Give one example where future information is nearly available and one where it is clearly unavailable.

## Mini-project problems

26. Draw open-loop study and implementable feedback block diagrams for a chosen system.
27. Classify information for that system as available now, predicted, or unknown.
28. Propose an MPC formulation including states, inputs, constraints, and horizon.
29. Describe how to turn an ideal trajectory into a simpler controller structure.
30. Write a one-page memo arguing whether OLOC is a final controller or design-analysis tool in your application.

## References and further reading

1. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577

2. Bryson, A. E., Jr., & Ho, Y.-C. (1975). *Applied optimal control: Optimization, estimation, and control*. Hemisphere Publishing Corporation.

3. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

4. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

5. Garcia-Sanz, M. (2019). Control co-design: An engineering game changer. *Advanced Control for Applications: Engineering and Industrial Systems, 1*(1), Article e18. DOI: 10.1002/adc2.18

6. Mayne, D. Q., Rawlings, J. B., Rao, C. V., & Scokaert, P. O. M. (2000). Constrained model predictive control: Stability and optimality. *Automatica, 36*(6), 789–814. DOI: 10.1016/S0005-1098(99)00214-9
