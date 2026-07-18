# Chapter 5: Control Co-Design Architectures and Coordination

*Sequential, iterative, nested, and simultaneous solution strategies*

> A CCD architecture is not the engineering problem itself. It is the organization used to solve that problem.

We now know what a control co-design (CCD) problem is and how to write a continuous-time formulation. A new question arises: **How should we organize the solution process?**

A plant and controller may be optimized one after another, alternated repeatedly, embedded in a nested architecture, or solved together in one simultaneous problem. These architectures often target the same engineering goal, but differ in coordination strength, computational burden, numerical difficulty, software integration, and organizational cost.

## Learning objectives

After completing this chapter, you should be able to:

1. describe the information flow in the main CCD architectures;
2. distinguish single-pass from iterative sequential design;
3. explain nested and simultaneous CCD;
4. distinguish mathematical equivalence from practical numerical behavior;
5. evaluate computational and implementation tradeoffs; and
6. select an architecture for a given engineering application.

## Chapter roadmap

**Single-pass sequential** $\rightarrow$ **Iterative sequential** $\rightarrow$ **Nested CCD** $\rightarrow$ **Simultaneous CCD** $\rightarrow$ **Tradeoffs and selection**