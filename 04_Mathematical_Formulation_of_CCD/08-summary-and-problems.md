# Chapter Summary and Problems

## Summary

A CCD formulation identifies plant and controller decisions, state and control trajectories, performance objectives, physical equality constraints, time-dependent path constraints, endpoint boundary constraints, and variable bounds. When algebraic equalities accompany the state derivatives, the dynamics form a differential-algebraic equation, and an active inequality path constraint can raise its index by converting a state or control into a dependent algebraic variable. Physical-design limits such as stress, fatigue, and packaging are often collected in a dedicated physical-constraint function, separate from operating limits such as actuator saturation. Lagrange objectives measure accumulated behavior, Mayer objectives measure terminal behavior, and Bolza objectives combine both. The resulting continuous-time problem is infinite-dimensional and must later be transcribed into a finite nonlinear program.

```{admonition} Central lesson
:class: important
Formulation bridges engineering intuition and numerical computation. It states precisely what can change, what should improve, and what must remain true.
```

## Key terms

Plant design variables; control design variables; control parameters; open-loop control (OLC) variables; state trajectory; control trajectory; equality constraint; path constraint; boundary constraint; physical-constraint function; differential-algebraic equation (DAE); algebraic variable; algebraic constraint; index-1; running cost; terminal cost; Lagrange objective; Mayer objective; Bolza objective; feasible trajectory; bounds; formulation; dynamic optimization.

## Problems

1. **Canonical continuous-time CCD formulation.** An active oscillator satisfies $m\ddot x+c\dot x+kx=u+w$, where $(m,k,c)$ are bounded plant variables and $u(\cdot)$ is the control trajectory. Formulate a complete Bolza CCD problem that minimizes mass, vibration, and control energy while enforcing displacement, velocity, force, terminal-state, and passive-failure constraints.

2. **Nondimensional CCD model.** For the oscillator in Problem 1, use $t_0=\sqrt{m_0/k_0}$, $x_0$, and $F_0=k_0x_0$ to derive a dimensionless state equation, objective, design bounds, and path constraints, identifying every independent dimensionless group.

3. **Variable-final-time formulation.** A point mass obeys $\dot r=v$, $m\dot v=u-c_dv|v|$ and must travel from $(0,0)$ to $(L,0)$. Transform a free-final-time CCD problem over $[0,t_f]$ to the fixed domain $\tau\in[0,1]$ and derive the transformed dynamics and objective when $m$, actuator rating, and $t_f$ are decisions.

4. **Path-constraint tangency.** For $\dot x_1=x_2$ and $\dot x_2=f(x)+bu$, impose the state-only path constraint $x_1(t)\le x_{\max}$. Derive its relative degree, boundary-control law, and entry tangency conditions required for a nonzero-duration constrained arc.

5. **Index-one DAE co-design.** A circuit model has $E(p)\dot x=A(p)x+Bu$ with singular $E(p)$ and algebraic variables embedded in $x$. Formulate a CCD problem that preserves the DAE rather than eliminating it and state regularity conditions on the matrix pencil $sE-A$ and initial conditions that ensure a unique admissible trajectory.

6. **Hybrid architecture dynamics.** A powertrain switches between modes $q\in\{1,2\}$ with $\dot x=f_q(x,u,p)$ and reset $x^+=R_{12}(x^-,p)$ at switching time $t_s$. Formulate the hybrid CCD problem with $p$, $u(\cdot)$, and $t_s$ as decisions and derive the interior transversality condition at $t_s$.

7. **Integral versus pointwise requirements.** For actuator temperature $\dot T=-a(p)(T-T_a)+b(p)u^2$, prove by counterexample that an energy constraint $\int_0^{t_f}u^2dt\le E_{\max}$ does not generally enforce $T(t)\le T_{\max}$, then formulate the correct thermal path constraint within a CCD problem.

8. **Uncertain CCD formulation.** The dynamics are $\dot x=f(x,u,p,\theta)$ with random, time-invariant parameter $\theta\sim\mathcal N(\bar\theta,\Sigma)$. Construct a chance-constrained CCD formulation requiring $\mathbb P[g(x(t),u(t),p,\theta)\le0\ \forall t]\ge1-\epsilon$ and derive a conservative finite-grid deterministic approximation using first-order propagation and risk allocation.

9. **Feedback-policy parameterization.** Replace an open-loop trajectory by $u(t)=\pi(x(t),t;c)$ in a nonlinear CCD problem. Derive the closed-loop state and design sensitivities with respect to $(p,c)$ and show exactly where the controller Jacobian $\partial\pi/\partial x$ enters.

10. **First-order necessary conditions for CCD.** For a general Bolza problem with plant vector $p$, dynamics $\dot x=f(x,u,p)$, equality path constraints $h=0$, inequality path constraints $g\le0$, and endpoint constraint $\Psi=0$, derive the augmented Hamiltonian system and the stationarity condition with respect to the time-invariant plant variables.

## References and further reading

1. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

2. Allison, J. T., Guo, T., & Han, Z. (2014). Co-design of an active suspension using simultaneous dynamic optimization. *Journal of Mechanical Design, 136*(8), Article 081003. DOI: 10.1115/1.4027335

3. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

4. Garcia-Sanz, M. (2019). Control co-design: An engineering game changer. *Advanced Control for Applications: Engineering and Industrial Systems, 1*(1), Article e18. DOI: 10.1002/adc2.18

5. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

6. Bryson, A. E., Jr., & Ho, Y.-C. (1975). *Applied optimal control: Optimization, estimation, and control*. Hemisphere Publishing Corporation.

7. Betts, J. T. (2010). *Practical methods for optimal control and estimation using nonlinear programming* (2nd ed.). Society for Industrial and Applied Mathematics. DOI: 10.1137/1.9780898718577
