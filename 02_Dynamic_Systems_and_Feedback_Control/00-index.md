# Chapter 2: Dynamic Systems and Feedback Control

*Modeling, analysis, and feedback ideas needed for control co-design*

> A controller can only improve a system through the dynamics of the plant it acts on. To do control co-design well, we must understand those dynamics clearly.

Control co-design (CCD) is fundamentally about **dynamic systems**. A plant is not just a static object with dimensions and mass. It moves, stores energy, dissipates energy, responds to disturbances, and interacts with sensors and actuators over time. Controllers also act over time: they measure, decide, and command. Because both the plant and controller affect time-domain behavior, CCD requires fluency in dynamic-system modeling and feedback ideas.

This chapter develops that foundation. We begin with physical system modeling and the language of states, inputs, outputs, and disturbances. We then introduce state-space representation, discuss open- and closed-loop systems, explain stability, and show how feedback modifies system behavior. The chapter closes by connecting these ideas back to plant design: changing stiffness, mass, damping, geometry, inertia, or actuator placement changes the system dynamics, which in turn changes what controller is best.

## Learning objectives

After completing this chapter, you should be able to:

1. explain why dynamic-system models are needed in control co-design;
2. identify states, inputs, outputs, and disturbances for a physical system;
3. derive a state-space model from differential equations;
4. distinguish open-loop and closed-loop systems;
5. explain equilibrium, stability, and asymptotic stability for linear systems;
6. show how feedback changes closed-loop dynamics; and
7. explain how plant design choices modify the dynamic model and therefore influence control design.

## Chapter roadmap

**Physical model** $\rightarrow$ **States and signals** $\rightarrow$ **State space** $\rightarrow$ **Feedback** $\rightarrow$ **Stability** $\rightarrow$ **Plant–control interaction**