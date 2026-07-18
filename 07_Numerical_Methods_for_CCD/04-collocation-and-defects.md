# Collocation and Defect Constraints

A **defect** measures disagreement between discrete state variables and the state change predicted by the dynamics. Zero defect means local dynamic consistency under the chosen approximation.

![Euler, trapezoidal, and Hermite-Simpson collocation arrangements across a mesh interval.](imgs/fig_chp7_6.svg)

*Higher-order schemes use more information within each interval.*

## Euler forward

```{math}
\boldsymbol{\zeta}_k^{\mathrm{EF}}=
\mathbf{x}_{k+1}-\mathbf{x}_k-h_k\mathbf{f}_k=\mathbf{0}.
```

Euler forward is globally first order and typically needs a fine mesh.

## Trapezoidal rule

```{math}
\boldsymbol{\zeta}_k^{\mathrm{TR}}=
\mathbf{x}_{k+1}-\mathbf{x}_k-\frac{h_k}{2}(\mathbf{f}_k+\mathbf{f}_{k+1})=\mathbf{0}.
```

It is globally second order and implicit. Implicitness is natural in transcription because the NLP solver determines states and defects together.

## Hermite–Simpson

Define

```{math}
\mathbf{x}_{k+1/2}=\frac{\mathbf{x}_k+\mathbf{x}_{k+1}}{2}
+\frac{h_k}{8}(\mathbf{f}_k-\mathbf{f}_{k+1}),
\qquad
\mathbf{u}_{k+1/2}=\frac{\mathbf{u}_k+\mathbf{u}_{k+1}}{2}.
```

Then

```{math}
\boldsymbol{\zeta}_k^{\mathrm{HS}}=
\mathbf{x}_{k+1}-\mathbf{x}_k-
\frac{h_k}{6}(\mathbf{f}_k+4\mathbf{f}_{k+1/2}+\mathbf{f}_{k+1})=\mathbf{0}.
```

Hermite–Simpson offers high accuracy, local sparsity, and moderate implementation complexity.

Other options include Runge–Kutta defects and exact zero-order-hold mappings for linear systems. Pseudospectral methods use high-order Lagrange interpolation and differentiation matrices at Legendre or Chebyshev nodes. They can converge rapidly for smooth trajectories but need multiple intervals or adaptation near discontinuities.

| Feature | Local collocation | Global/pseudospectral |
| --- | --- | --- |
| Approximation | Low order per interval | High order over large intervals |
| Sparsity | Strong local bands | Denser within each polynomial interval |
| Smooth solutions | Algebraic mesh convergence | Potentially spectral convergence |
| Nonsmooth solutions | Local refinement | Multiple intervals or adaptation |
| Implementation | Relatively direct | Specialized matrices and quadrature |
