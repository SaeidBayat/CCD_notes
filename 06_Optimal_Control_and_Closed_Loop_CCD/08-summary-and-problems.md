# Chapter Summary and Problems

## Summary

OLOC directly optimizes a control trajectory and is valuable for ideal performance benchmarks, qualitative insight, and plant-design studies. It can also assume future information unavailable to a real controller. Controller-parameter optimization instead designs an implementable feedback policy. Feedback-controller CCD combines physical and policy decisions and evaluates them under measurements and realized disturbances. MPC bridges these views by repeatedly solving a short open-loop problem using updated information.

## Key terms

Open-loop optimal control; control trajectory; controller parameterization; feedback controller; feedback-controller co-design; future information; information availability; measured state; estimated state; forecast; implementable controller; model predictive control; receding horizon; prediction horizon; benchmark solution; realizability; complete horizon; instantaneous information; limited horizon; digital controller realization; prediction horizon as a design variable; nested CCD; covariance matrix adaptation evolution strategy (CMA-ES); hybrid Kalman filter.

## Problems

1. **Pontryagin analysis with a plant variable.** Minimize $J=\tfrac12q_fx(T)^2+\int_0^T\tfrac12(qx^2+ru^2+\gamma p^2)dt$ subject to $\dot x=-p x+u$, $x(0)=x_0$, and $p\in[p_-,p_+]$. Derive the costate, optimal control, boundary conditions, and stationarity condition determining an interior optimal $p$.

2. **LQR control co-design.** For $\dot x=A(p)x+B(p)u$ and infinite-horizon cost $\int_0^\infty(x^TQ(p)x+u^TRu)dt+C(p)$, derive a gradient of the optimized value with respect to $p$ using differentiated Riccati and Lyapunov equations without differentiating the feedback gain explicitly.

3. **Static output-feedback co-design.** The controller is $u=-Ky$ with $y=C(s)x$, where sensor placement $s$ changes $C$. Formulate an $H_2$ plant--sensor--controller co-design problem and derive first-order stationarity conditions using the closed-loop controllability and observability Gramians.

4. **Stabilizing model predictive control.** For $x_{k+1}=A(p)x_k+B(p)u_k$ with polyhedral state and input constraints, formulate a finite-horizon MPC law with terminal cost and terminal set, then derive a sufficient decrease inequality proving recursive feasibility and asymptotic stability for every admissible plant design.

5. **Value of preview.** A disturbance-preview controller knows $w_{k:k+N_p}$ for $x_{k+1}=Ax_k+Bu_k+Ew_k$. Derive the finite-horizon optimal control law and an explicit expression for the reduction in quadratic cost relative to the no-preview law as a function of $N_p$.

6. **Information-horizon monotonicity.** Let $J_N^*(p)$ be the optimal expected cost when a controller has an $N$-step information horizon. Prove that $J_{N+1}^*(p)\le J_N^*(p)$ under nested policy classes and construct a counterexample showing that the corresponding optimal plant design need not vary monotonically with $N$.

7. **Open-loop to closed-loop performance gap.** For $\dot x=ax+bu+w$ with bounded disturbance $|w|\le\bar w$, derive the worst-case tracking-cost gap between a nominal open-loop control optimized for $w=0$ and a stabilizing linear feedback law, including actuator saturation in the bound.

8. **Estimator-aware CCD.** For $\dot x=A(p)x+Bu+Gw$ and $y=C(s)x+v$, formulate a joint plant--sensor--LQG design and derive the coupled Riccati sensitivities showing how plant and sensor decisions affect both regulation and estimation cost.

9. **Actuator sizing under saturation.** The scalar system $\dot x=-ax+bu$ uses $u=\operatorname{sat}(-Kx,U)$, and actuator mass is $m_a(U)=m_0+\alpha U$. Determine the globally optimal rating $U$ for a prescribed initial-state distribution and quadratic regulation objective by deriving a one-dimensional optimality condition that accounts for switching between saturated and unsaturated arcs.

10. **Robust closed-loop CCD.** The uncertain plant is $x_{k+1}=(A(p)+H\Delta E)x_k+B(p)u_k$ with $\Delta^T\Delta\preceq I$. Formulate a min--max state-feedback CCD problem and derive an LMI-based sufficient condition that jointly certifies robust stability, an upper bound on worst-case quadratic cost, and admissible plant bounds.

## References and further reading

1. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577

2. Bryson, A. E., Jr., & Ho, Y.-C. (1975). *Applied optimal control: Optimization, estimation, and control*. Hemisphere Publishing Corporation.

3. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

4. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

5. Garcia-Sanz, M. (2019). Control co-design: An engineering game changer. *Advanced Control for Applications: Engineering and Industrial Systems, 1*(1), Article e18. DOI: 10.1002/adc2.18

6. Mayne, D. Q., Rawlings, J. B., Rao, C. V., & Scokaert, P. O. M. (2000). Constrained model predictive control: Stability and optimality. *Automatica, 36*(6), 789–814. DOI: 10.1016/S0005-1098(99)00214-9

7. Deshmukh, A. P., Herber, D. R., & Allison, J. T. (2015). Bridging the gap between open-loop and closed-loop control in co-design: A framework for complete optimal plant and control architecture design. In *2015 American Control Conference (ACC)* (pp. 4916-4922).

8. Bayat, S., & Allison, J. T. (2026). Control co-design with varying available information applied to vehicle suspensions. *ASME Journal of Dynamic Systems, Measurement, and Control, 148*(1), Article 011013. DOI: 10.1115/1.4069918
