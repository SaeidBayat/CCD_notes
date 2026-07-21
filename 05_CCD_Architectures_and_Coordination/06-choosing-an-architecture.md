# Choosing an Appropriate Architecture

No architecture is always best. Selection depends on coupling strength, simulation cost, derivatives, model structure, available software, and the goal of the study.

![A decision guideline starting with plant-control coupling strength and branching toward sequential, iterative, nested, or simultaneous CCD.](imgs/fig_chp5_8.svg)

*Plant–control coupling is central to architecture choice, but it is not the only consideration.*

## Favor single-pass sequential design when

- coupling is weak;
- a quick baseline is needed;
- ease of implementation dominates; and
- the controller has modest influence on plant tradeoffs.

## Favor iterative sequential design when

- some coupling exists but full integration is impractical;
- separate plant and controller tools must remain;
- repeated coordination is affordable; and
- moderate improvement over a baseline is desired.

## Favor nested CCD when

- controller optimization is reliable and well defined;
- every plant should be evaluated under best achievable control;
- the structure naturally suggests outer plant and inner control loops; and
- controller-tool reuse is important.

## Favor simultaneous CCD when

- plant–control coupling is strong;
- maximum coordinated performance is sought;
- accurate gradients and modern nonlinear-programming tools are available; and
- unified model integration is feasible.

## A sharper criterion: what derivatives can you actually get?

A controlled comparison on an active-suspension co-design problem suggests a more specific, checkable version of "favor simultaneous when coupling is strong": ask first whether the dynamic model can supply symbolic or complex-step derivatives with respect to the plant and control variables. If it can, simultaneous CCD's coordination advantage tends to show up as a real computational advantage too, especially at fine time discretization. If only real-valued finite differences are available — common with legacy, black-box, or multiphysics simulation codes — nested CCD, using a tailored and reliable inner-loop solver (a closed-form LQR solve, or a quadratic program when the inner problem is linear-quadratic), can be faster by an order of magnitude despite its repeated inner solves. This turns the derivative-availability question already listed below from a soft preference into the single most decisive factor observed in a rigorous, implementation-controlled study.

```{admonition} A companion checklist item
:class: tip
Before committing to nested CCD, check that the inner problem is feasible for every plant design the outer loop might propose, or add an explicit outer-loop feasibility constraint. In a documented case, uniform sampling within simple design bounds left 44% of candidate plants without a feasible inner solution.
```

## Questions to ask before choosing

1. How expensive is each simulation?
2. Are accurate derivatives available?
3. How nonlinear and nonconvex is the problem?
4. How many variables and trajectory points are involved?
5. Which legacy tools must be preserved?
6. Is the aim a quick baseline or the best achievable design?
