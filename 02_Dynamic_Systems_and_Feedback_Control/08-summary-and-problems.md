# Chapter Summary and Problems

## Summary

This chapter introduced the dynamic-system ideas needed for CCD. Physical modeling leads to differential equations, and state-space representation organizes those equations using states, inputs, outputs, and disturbances. Open-loop control relies on prediction, while closed-loop control uses feedback to respond to actual behavior. Stability describes what trajectories do near an equilibrium, and feedback changes stability and response by changing the closed-loop dynamics. Most importantly for CCD, plant design variables change the dynamic model and therefore change which controller is best.

```{admonition} The central message
:class: important
Controllers do not act on abstract equations; they act on physical systems with specific dynamics. When the plant changes, the control problem changes too.
```

## Key terms

Dynamic system; state; control input; output; disturbance; differential equation; multidisciplinary analysis (MDA); differential-algebraic equation (DAE); index-1 DAE; algebraic constraint; state-space representation; linearization; open-loop system; closed-loop system; feedback; equilibrium; stability; asymptotic stability; eigenvalue; natural frequency; damping ratio; closed-loop poles.

## Problems

1. **Nonlinear modeling and local dynamics.** A torque-actuated pendulum satisfies $ml^2\ddot\theta+b\dot\theta+mgl\sin\theta=u$. Derive its nonlinear state-space model and the exact linearization about the upright equilibrium, then determine the state-feedback gains that place the linearized poles at a prescribed stable conjugate pair.

2. **Plant design and controllability.** A flexible two-mass system obeys $M(p)\ddot q+C\dot q+K(p)q=b(r_a)u$, where $p$ changes stiffness and $r_a$ is actuator location. Derive a modal controllability metric and use it to state a quantitative co-design criterion that prevents any retained mode from becoming weakly actuated.

3. **LQR-dependent plant selection.** For $\dot x=\begin{bmatrix}0&1\\-k/m&-c/m\end{bmatrix}x+\begin{bmatrix}0\\1/m\end{bmatrix}u$ and $J=\int_0^\infty(x^TQx+ru^2)dt+\gamma m$, derive the algebraic-Riccati sensitivity equations needed to compute the total derivative of the optimized closed-loop cost with respect to $m$.

4. **Robust stability over a design family.** The closed-loop matrix is $A_{cl}(p)=A_0+pA_1-BK$ for $p\in[p_-,p_+]$. Formulate and justify a common quadratic Lyapunov inequality that certifies a uniform exponential decay rate over the entire interval, reducing the infinite family to finitely many matrix inequalities when the dependence is affine.

5. **Observer--plant interaction.** A sensor placement variable $s$ changes the output matrix $C(s)$ in $\dot x=A(p)x+Bu$, $y=C(s)x+v$. Derive the observability Gramian and formulate a joint placement--estimator design constraint that bounds the worst-direction state-estimation uncertainty over a finite horizon.

6. **Sampled-data feedback.** For $\dot x=Ax+Bu$ with zero-order-hold control $u(t)=-Kx(kh)$ on $kh\le t<(k+1)h$, derive the exact discrete closed-loop matrix and determine the largest sampling period $h$ that preserves asymptotic stability for a specified numerical pair $(A,B,K)$.

7. **Disturbance attenuation.** The quarter-car model is $M\ddot q+C\dot q+Kq=B_uu+B_ww$, with performance output $z=C_zx+D_zu$. Derive the bounded-real linear matrix inequality that certifies $\|T_{w\to z}\|_\infty<\gamma$ and identify which matrix terms change when suspension stiffness is a design variable.

8. **Region of attraction under actuator saturation.** For $\dot x=Ax+B\operatorname{sat}(-Kx,u_{\max})$, derive an invariant ellipsoidal inner approximation $\mathcal E(P)=\{x:x^TPx\le1\}$ by combining a Lyapunov inequality with constraints ensuring the feedback remains unsaturated inside $\mathcal E(P)$.

9. **Unmodeled flexible dynamics.** A nominal rigid-body plant $G_0(s)=1/(Js^2)$ is augmented by a flexible mode $G_f(s)=\omega_f^2/(s^2+2\zeta_f\omega_fs+\omega_f^2)$. Derive a robust-stability restriction on controller bandwidth using multiplicative uncertainty and show how increasing structural stiffness can enlarge the admissible bandwidth.

10. **Dynamic feasibility of an index-one DAE.** An electromechanical actuator satisfies $L\dot i+Ri+k_e\omega=v$, $J\dot\omega=k_ti-\tau_L$, and the algebraic saturation law $0=i-\operatorname{sat}(i_c,i_{\max}(T))$. Formulate a consistent state--algebraic representation and derive the conditions under which an equilibrium and its local linearization are well defined.

## References and further reading

1. Allison, J. T., & Herber, D. R. (2014). Multidisciplinary design optimization of dynamic engineering systems. *AIAA Journal, 52*(4), 691–710. DOI: 10.2514/1.J052182

2. Allison, J. T., Guo, T., & Han, Z. (2014). Co-design of an active suspension using simultaneous dynamic optimization. *Journal of Mechanical Design, 136*(8), Article 081003.

3. Garcia-Sanz, M. (2019). Control co-design: An engineering game changer. *Advanced Control for Applications: Engineering and Industrial Systems, 1*(1), Article e18. DOI: 10.1002/adc2.18

4. Herber, D. R., & Allison, J. T. (2019). Nested and simultaneous solution strategies for general combined plant and control design problems. *Journal of Mechanical Design, 141*(1), Article 011402. DOI: 10.1115/1.4040705

5. Martins, J. R. R. A., & Ning, A. (2021). *Engineering design optimization*. Cambridge University Press.

6. Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (2019). *Feedback control of dynamic systems* (8th ed.). Pearson.

7. Herber, D. R. (2017). *Advances in Combined Architecture, Plant, and Control Design* (Doctoral dissertation). University of Illinois at Urbana-Champaign.
