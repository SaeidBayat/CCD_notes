# Chapter 7: Numerical Methods for Control Co-Design

*Discretization, transcription, sparse optimization, derivatives, and verification*

> The numerical method, mesh, scaling, derivatives, and verification procedure can change the design reported as optimal.

CCD problems are often infinite-dimensional because states and controls are functions of time. Computers cannot optimize arbitrary continuous functions directly. Numerical methods replace them with finite variables and algebraic constraints, producing a nonlinear program (NLP).

This chapter develops time discretization, direct and multiple shooting, direct transcription, collocation and defect constraints, sparse NLP structure, derivative computation, scaling, initialization, mesh refinement, and numerical verification.

## Learning objectives

After completing this chapter, you should be able to:

1. convert a continuous CCD problem into a finite NLP;
2. construct and assess a computational mesh;
3. compare direct shooting, multiple shooting, and transcription;
4. write Euler, trapezoidal, and Hermite–Simpson defects;
5. explain direct-transcription sparsity;
6. compare numerical and exact derivative methods;
7. perform mesh-refinement and independent-simulation checks; and
8. organize a reliable CCD implementation workflow.

## Chapter roadmap

**Continuous problem** $\rightarrow$ **Mesh** $\rightarrow$ **Shooting or transcription** $\rightarrow$ **Sparse NLP** $\rightarrow$ **Derivatives** $\rightarrow$ **Refinement and verification**