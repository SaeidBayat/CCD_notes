# Uncertainty and Robustness

Nominal CCD assumes a fixed model and operating condition. Real systems encounter environmental variability, payload changes, manufacturing tolerances, sensor noise and delay, model-form error, and actuator saturation or derating. A nominal optimum near a constraint boundary may therefore be fragile.

## Scenario formulation

For scenario $s$ with uncertain quantities $\boldsymbol{\theta}_s$ and weight $p_s$,

$$
\min_{\mathbf{x}_p,\mathbf{x}_c}\sum_{s=1}^{N_s}p_sJ(\mathbf{x}_p,\mathbf{x}_c;\boldsymbol{\theta}_s)
$$

subject to required scenario constraints

$$
g(\mathbf{x}_p,\mathbf{x}_c;\boldsymbol{\theta}_s)\le0,
\qquad s=1,\ldots,N_s.
$$

Suspension scenarios might combine bump, rough-road, pothole, and sinusoidal inputs; light, nominal, and heavy payloads; tire-property changes; sensor delay; and actuator derating.

## Risk-aware alternatives

- **Worst case:** $\min_{\mathbf{x}_p,\mathbf{x}_c}\max_{\boldsymbol{\theta}\in\Theta}J(\mathbf{x}_p,\mathbf{x}_c;\boldsymbol{\theta})$ protects against the most damaging defined case, but may be conservative.
- **Mean–variance:** $\min\ \mathbb{E}[J]+\lambda\operatorname{Var}(J)$ balances average and dispersion.
- **Chance constraint:** $\mathbb{P}(g(\mathbf{x}_p,\mathbf{x}_c;\boldsymbol{\theta})\le0)\ge1-\epsilon$ imposes a satisfaction probability.
- **CVaR:** penalizes the upper tail of poor outcomes and reveals more than mean performance alone.

![Common uncertainty-aware CCD strategies.](imgs/fig_chp8_6.svg)

## Verification under uncertainty

Even a nominal optimization should be tested with Monte Carlo simulation or a structured validation set. Report mean and worst objective, constraint-violation probability, percentiles of key outputs, sensitivities, and observed failure modes. Keep validation scenarios independent from those used to tune the design whenever possible.

:::{tip} Activity 8.2: Robust Suspension Design Using Expected Value, Worst Case, and CVaR
:class: dropdown

Use the suspension model from Activity 8.1. Define the uncertain sprung mass and bump height as

```{math}
m_s\in\{240, 300, 360\}\ \mathrm{kg},
\qquad
h_b\in\{0.03, 0.05, 0.07\}\ \mathrm{m}.
```

This produces nine equally probable scenarios. Let the scenario objective be

```{math}
J_s(\mathbf{x}_p,\mathbf{x}_c),
\qquad
s=1,\ldots,9.
```

1. Formulate the expected-value problem

   ```{math}
   \min_{\mathbf{x}_p,\mathbf{x}_c}
   \frac{1}{9}\sum_{s=1}^{9}J_s.
   ```

2. Formulate the worst-case problem using an epigraph variable $\eta$:

   ```{math}
   \begin{aligned}
   \min_{\mathbf{x}_p,\mathbf{x}_c,\eta}\quad&\eta,\\
   \text{subject to}\quad&J_s\leq\eta,
   \qquad s=1,\ldots,9.
   \end{aligned}
   ```

3. Formulate the combined mean-worst-case problem

   ```{math}
   \min\quad\frac{1}{9}\sum_{s=1}^{9}J_s+\lambda\eta,
   \qquad
   \lambda\in\{0, 0.1, 0.5, 1, 2\}.
   ```

4. Formulate the empirical CVaR objective at confidence level $\alpha=0.9$ using auxiliary variables $\xi_s$:

   ```{math}
   \operatorname{CVaR}_{\alpha}
   =\eta+\frac{1}{(1-\alpha)N_s}\sum_{s=1}^{N_s}\xi_s,
   ```

   subject to

   ```{math}
   \xi_s\geq J_s-\eta,
   \qquad
   \xi_s\geq0.
   ```

5. Require every path constraint to hold in all nine scenarios.

6. Solve the nominal, expected-value, worst-case, and CVaR designs.

7. Compare

   ```{math}
   J_{\mathrm{nominal}},
   \qquad
   \mathbb{E}[J],
   \qquad
   \max_sJ_s,
   \qquad
   \operatorname{CVaR}_{0.9}.
   ```

8. Quantify the nominal-performance penalty of robustness.

9. Determine which plant and controller variables change most strongly when moving from nominal to robust design.

10. Explain why a robust design can have a worse nominal objective but still be the more credible engineering design.
:::
