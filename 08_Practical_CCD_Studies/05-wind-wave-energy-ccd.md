# Wind and Wave Energy CCD

Floating wind and wave-energy systems combine aerodynamics, hydrodynamics, structural dynamics, moorings, power electronics, and multiple controllers. Their stochastic environment affects annual energy, extreme loads, fatigue, platform motion, power quality, and reliability.

![System-level map for a hybrid offshore wind–wave CCD application.](imgs/fig_chp8_8.svg)

## Plant and control decisions

Candidate plant variables include rotor and blade properties, tower dimensions, platform geometry and mass distribution, mooring layout and stiffness, wave-energy-converter (WEC) geometry and placement, power-take-off (PTO) force and stroke ratings, and storage or conversion capacity.

Control decisions may include generator-torque and blade-pitch gains, platform-motion or load feedback, WEC PTO damping or optimal-force parameters, MPC horizons and weights, supervisory power sharing, and fault-handling thresholds.

## Multi-scenario objective

A representative objective combines energy, loads, motion, power variation, and cost:

$$
\begin{aligned}
\min_{\mathbf{x}_p,\mathbf{x}_c}J={}&-w_EE_{\mathrm{ann}}(\mathbf{x}_p,\mathbf{x}_c)
+w_LD_{\mathrm{fat}}(\mathbf{x}_p,\mathbf{x}_c)\\
&+w_MM_{\mathrm{motion}}(\mathbf{x}_p,\mathbf{x}_c)
+w_PP_{\mathrm{var}}(\mathbf{x}_p,\mathbf{x}_c)
+w_CC_{\mathrm{cap}}(\mathbf{x}_p).
\end{aligned}
$$

Annual behavior is approximated with weighted wind–wave bins, turbulent seeds, or representative scenarios. Constraints can address blade, tower, and mooring loads; platform pitch, heave, and surge; WEC angle, stroke, and PTO force; electrical power; closed-loop stability; clearance; survivability; and fault conditions.

## Multi-fidelity strategy

A practical hierarchy uses:

1. frequency-domain or linear models for screening;
2. reduced or identified dynamic models for controller optimization;
3. engineering time-domain simulation for detailed design; and
4. CFD, high-order structural models, or experiments for selected verification.

A low-fidelity optimum is a candidate hypothesis, not final evidence.

## Sequential versus integrated outcomes

A sequential process may optimize platform stability, add WECs, and then tune controllers. Integrated CCD may instead select a platform that moves more but enables better energy capture, locate WECs to reduce turbine motion, balance PTO rating against structural-load mitigation, or coordinate wind, wave, and storage subsystems. The system optimum can therefore differ qualitatively from individually optimized subsystems.
