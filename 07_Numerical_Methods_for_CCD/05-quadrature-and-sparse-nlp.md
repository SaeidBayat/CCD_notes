# Quadrature, Path Constraints, and Sparse NLPs

## Objective quadrature

The running cost must be discretized consistently with the trajectory approximation:

```{math}
\begin{aligned}
\text{rectangle:}\quad &\int_{t_k}^{t_{k+1}}L\,dt\approx h_kL_k,\\
\text{trapezoidal:}\quad &\int_{t_k}^{t_{k+1}}L\,dt\approx\frac{h_k}{2}(L_k+L_{k+1}),\\
\text{Simpson:}\quad &\int_{t_k}^{t_{k+1}}L\,dt\approx\frac{h_k}{6}(L_k+4L_{k+1/2}+L_{k+1}).
\end{aligned}
```

A low-order quadrature rule can limit the accuracy of an otherwise high-order transcription.

## Path constraints between nodes

Imposing $\mathbf{c}(\mathbf{x}_k,\mathbf{u}_k,\ldots)\leq\mathbf{0}$ only at nodes does not guarantee continuous feasibility. Reconstructed trajectories can overshoot. Remedies include dense-grid verification, extra enforcement points, margins, local refinement, and interpolation-error estimates.

Boundary constraints depend on selected endpoint nodes and do not create the same between-node issue.

## Why large NLPs remain manageable

A problem with 30 states, 10 controls, and 500 intervals has about 20,040 trajectory variables. Dimension alone is not decisive; **sparsity** is.

A local defect depends mainly on $\mathbf{x}_k$, $\mathbf{u}_k$, $\mathbf{x}_{k+1}$, $\mathbf{u}_{k+1}$, and global design variables. Its Jacobian touches only a small portion of the decision vector.

![A banded direct-transcription Jacobian compared with a dense cumulative shooting sensitivity pattern.](imgs/fig_chp7_7.svg)

*Local time dependence produces exploitable sparse structure.*

Sparse SQP and interior-point solvers benefit from exact sparsity patterns, sparse derivatives, scaled variables and constraints, and bounds separated from general constraints.

Decision-vector ordering changes fill-in in the solver’s linear systems. Condensing can eliminate states, reducing dimension but potentially destroying sparsity. Partial condensing balances these effects.
