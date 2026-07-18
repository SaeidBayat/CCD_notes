# Worked Examples and Architecture Comparison

## Example 5.1: active suspension

Let plant variables be $\mathbf{x}_p=[k_s,c_s]^T$ and controller gains be $\mathbf{x}_c=[K_1,K_2,K_3,K_4]^T$.

- **Single-pass:** choose $k_s,c_s$ using passive metrics, then tune gains.
- **Iterative sequential:** alternate plant redesign and gain tuning until performance stabilizes.
- **Nested:** solve an inner controller problem for every $(k_s,c_s)$ candidate.
- **Simultaneous:** optimize all six decisions in one problem.

The engineering system remains the same; only the solution organization changes.

## Example 5.2: wind turbine

Plant variables may include tower and structural parameters, while control variables include pitch settings. When feedback strongly influences structural loads, nested or simultaneous methods become attractive because the best plant depends on controller capability.

## Example 5.3: marine energy device

Buoy geometry and PTO properties can be plant decisions, while reactive or latching parameters define control. Strong hydrodynamic–control coupling may make nested or simultaneous coordination substantially better than a purely sequential process.

## Qualitative comparison

| Architecture | Coordination | Implementation | Typical burden | Good use case |
| --- | --- | --- | --- | --- |
| Single-pass sequential | Low | Low | Low | Weak coupling, quick baseline |
| Iterative sequential | Moderate | Low–moderate | Moderate | Reusable separate tools |
| Nested CCD | High | Moderate | High repeated inner solves | Best-control evaluation of each plant |
| Simultaneous CCD | Very high | High | Large integrated solve | Strong coupling and unified optimization |

## Common mistakes

1. **Assuming simultaneous always means better.** Poor scaling or derivatives can defeat its theoretical advantages.
2. **Assuming equivalence means identical computation.** Formal equivalence does not eliminate local minima or numerical error.
3. **Ignoring setup cost.** Elegant integration may not fit a short project.
4. **Using a single pass under strong coupling.** Important design opportunities may remain hidden.
5. **Ignoring nested inner-solve cost.** Controller optimization can dominate runtime.
6. **Neglecting initialization.** Architecture and initialization often interact strongly.
