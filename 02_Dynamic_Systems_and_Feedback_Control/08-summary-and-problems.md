# Chapter Summary and Problems

## Summary

This chapter introduced the dynamic-system ideas needed for CCD. Physical modeling leads to differential equations, and state-space representation organizes those equations using states, inputs, outputs, and disturbances. Open-loop control relies on prediction, while closed-loop control uses feedback to respond to actual behavior. Stability describes what trajectories do near an equilibrium, and feedback changes stability and response by changing the closed-loop dynamics. Most importantly for CCD, plant design variables change the dynamic model and therefore change which controller is best.

```{admonition} The central message
:class: important
Controllers do not act on abstract equations; they act on physical systems with specific dynamics. When the plant changes, the control problem changes too.
```

## Key terms

Dynamic system; state; control input; output; disturbance; differential equation; state-space representation; linearization; open-loop system; closed-loop system; feedback; equilibrium; stability; asymptotic stability; eigenvalue; natural frequency; damping ratio; closed-loop poles.

## Conceptual problems

1. Explain why dynamic-system models are especially important in control co-design.
2. Give one state, input, output, and disturbance for each system: (a) active suspension, (b) robot arm, and (c) wind turbine.
3. A student says, “If a system is stable, then it is well designed.” Explain why this statement is incomplete.
4. Describe one situation in which open-loop control may be acceptable and one in which closed-loop control is essential.
5. Why can it be dangerous to optimize a plant assuming a fixed controller that will later be replaced?

## Modeling and derivation problems

6. For the mass–spring–damper system, derive a state-space model when the output is acceleration rather than displacement.
7. A rotational inertia $J$ is connected to a torsional spring $k_t$ and damper $c_t$, and torque $\tau$ acts on the shaft. Derive a state-space model using angular displacement and angular velocity as states.
8. Derive a state-space model of

   ```{math}
   m\dot{v}=F_t-c_rv-mg\sin\theta
   ```

   using $v$ as the state, $F_t$ as the control input, and $\theta$ as the disturbance.
9. For the DC motor model, choose shaft speed as the only output. Write the corresponding $C$ and $D$ matrices.
10. For the nonlinear pendulum

    ```{math}
    ml^2\ddot{\theta}+b\dot{\theta}+mgl\sin\theta=\tau,
    ```

    define states and write the nonlinear state-space model.

## Analysis problems

11. For

    ```{math}
    \dot{\mathbf{x}}=\begin{bmatrix}0&1\\-5&-2\end{bmatrix}\mathbf{x},
    ```

    compute the eigenvalues and determine whether the origin is asymptotically stable.
12. For Problem 11, compute the natural frequency and damping ratio if the system is interpreted as a second-order mechanical model.
13. Show that the closed-loop matrix under state feedback $u=-Kx$ is $A-BK$. Why is this central to feedback control?
14. For $m=1$, $c=0.6$, and $k=2.5$, compute the open-loop poles of the mass–spring–damper model.
15. Suppose $m$ is doubled while $c$ and $k$ remain unchanged. How do the natural frequency and damping ratio change?

## Control and design interaction problems

16. Explain physically what $K_p$ and $K_d$ in {eq}`eq-ch2-pd-law` do to effective stiffness and damping.
17. Identify a tradeoff between making a mass–spring–damper plant stiffer and making its controller more aggressive.
18. Describe how changing actuator placement on a flexible structure could alter the plant model and feedback effectiveness.
19. A marine energy device is redesigned with a larger buoy. List at least four ways this might alter the dynamic model relevant to control design.
20. A robot joint is made lighter but less stiff. Explain qualitatively how that might affect bandwidth, vibration, and controller tuning.

## Computational and mini-project problems

21. Use MATLAB or Python to simulate mass–spring–damper responses for at least three values of $c$ while holding $m$ and $k$ fixed. Plot and explain the trends.
22. Plot the system poles as stiffness $k$ varies over a wide range. What trend do you observe?
23. Choose an engineering system and identify at least three plant design variables and three control design variables. Explain why it is a good CCD candidate.
24. Build a first- or second-order state-space model from your research area or engineering interests. Define its states, inputs, outputs, and disturbances.
25. Select an actively controlled system and prepare a 3–4 page modeling memo containing: (a) a system diagram, (b) assumptions, (c) differential equations, (d) a state-space representation, (e) a stability discussion, and (f) an explanation of how plant design could change the model and control problem.

## References and further reading

1. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

2. Allison, J. T., Guo, T., & Han, Z. (2014). Co-design of an active suspension using simultaneous dynamic optimization. *Journal of Mechanical Design, 136*(8), Article 081003.

3. Garcia-Sanz, M. (2019). Control co-design: An engineering game changer. *Advanced Control for Applications: Engineering and Industrial Systems, 1*(1), Article e18. DOI: 10.1002/adc2.18

4. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

5. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

6. Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2019). *Feedback control of dynamic systems* (8th ed.). Pearson.
