# Chapter 3: Engineering Design Optimization

*Formulation, search, numerical reliability, and multidisciplinary coupling*

> Optimization does not replace engineering judgment. It organizes engineering judgment into a precise search over decisions, performance measures, models, and constraints.

Control co-design requires more than knowing how dynamic systems behave. It also requires a disciplined method for choosing among many possible plant and controller designs. Engineering design optimization provides that method. An optimization problem defines what decisions may change, how designs are compared, which designs are physically or operationally acceptable, and how a numerical algorithm searches for an improved solution.

This chapter introduces the optimization concepts needed throughout the rest of the course: design variables, objectives, constraints, feasible design spaces, local and global optima, gradient-based search, constrained optimality, scaling, numerical conditioning, multidisciplinary design optimization (MDO), and optimization of dynamic systems.

## Learning objectives

After completing this chapter, you should be able to:

1. identify design variables, objectives, equality constraints, inequality constraints, and bounds;
2. write an engineering design problem in standard mathematical form;
3. interpret feasible, infeasible, active, and inactive constraints geometrically;
4. distinguish local and global optima and explain why initialization matters;
5. describe gradient descent, line search, Newton, and quasi-Newton methods;
6. explain why scaling and numerical conditioning influence reliability;
7. identify disciplines and coupling variables in an MDO problem; and
8. formulate problems whose objectives and constraints depend on dynamic simulations.

## Chapter roadmap

**Formulation** $\rightarrow$ **Feasible space** $\rightarrow$ **Optimality** $\rightarrow$ **Gradient methods** $\rightarrow$ **Scaling** $\rightarrow$ **MDO** $\rightarrow$ **Dynamic optimization**
