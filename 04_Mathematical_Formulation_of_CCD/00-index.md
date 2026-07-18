# Chapter 4: Mathematical Formulation of Control Co-Design

*Variables, trajectories, objectives, dynamics, and engineering constraints*

> A control co-design problem becomes solvable only after the engineering question is written as an optimization problem with clear variables, objectives, and constraints.

The previous chapters explained why control co-design (CCD) matters, developed the required dynamic-system concepts, and introduced engineering optimization. We can now answer a practical question: **How do we write a CCD problem mathematically?**

A weak formulation can make a good engineering idea impossible to solve. A clear formulation reveals problem structure, design tradeoffs, and appropriate computational methods. In CCD, it must describe plant and controller variables, time-dependent state and control trajectories, physical dynamics, objectives, and path and boundary constraints.

## Learning objectives

After completing this chapter, you should be able to:

1. identify plant variables, control variables, state trajectories, and control trajectories;
2. express system dynamics as equality constraints;
3. distinguish and write path and boundary constraints;
4. explain Lagrange, Mayer, and Bolza objectives;
5. write a general continuous-time CCD formulation; and
6. explain how a dynamic formulation differs from static optimization.

## Chapter roadmap

**Engineering question** $\rightarrow$ **Variables and trajectories** $\rightarrow$ **Dynamics** $\rightarrow$ **Constraints** $\rightarrow$ **Objective** $\rightarrow$ **Continuous-time CCD problem**