# Examples and Architecture Comparison

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

## Example 5.4: a controlled comparison on active suspension

A quarter-car active-suspension CCD problem — sprung and unsprung mass connected by a force actuator, with a physically parameterized spring ($\mathbf{x}_p$ including wire diameter, helix diameter, pitch, and number of active coils) and a physically parameterized damper — was solved to a converged reference solution using both nested and simultaneous strategies at a fine mesh ($N_t=5000$) and tight tolerances. Both strategies converged to essentially the same design: an objective value of $o^*\approx2.0677$, with the simultaneous strategy giving an effective spring constant $k_s^*\approx2.366\times10^4$ N/m and damping $c_s^*\approx839.8$ Ns/m, within 2% of the nested strategy's values, so the resulting optimal state and control trajectories were nearly indistinguishable between the two strategies. This is a directly verified instance of the "same ideal solution" claim from the previous section — but the two strategies took very different amounts of computation to reach it, depending entirely on which derivative methods were available.

## Example 5.5: how the architecture ranking scales with mesh density

A strain-actuated solar-array co-design test problem, solved by direct transcription at three levels of mesh accuracy, shows how sensitive a nested-versus-simultaneous comparison is to the efficiency of the inner-loop solver. A naive, general-purpose nested implementation was always many orders of magnitude slower than a nested implementation that recognized the inner loop's linear-quadratic structure and solved it as a quadratic program. Comparing that efficient nested (QP) implementation against simultaneous CCD:

| Mesh accuracy | Simultaneous runtime | Nested (QP) runtime |
| --- | --- | --- |
| Low ($N_t=10$) | 0.06 s | 0.16 s |
| Medium ($N_t=100$) | 6.54 s | 1.22 s |
| High ($N_t=1{,}000$) | 11,464.33 s | 17.63 s |

At low accuracy, simultaneous CCD was actually faster, though both solve times were small in absolute terms. At medium and high accuracy, the efficient nested implementation was dramatically faster — by roughly $650\times$ at the highest mesh density tested — while both strategies converged to plant designs within a fraction of a percent of each other and of the closed-form solution available for this test problem. The lesson is not that nested is unconditionally faster: the advantage of nested CCD here is entirely contingent on having an efficient method for the *specific* inner-loop problem structure, exactly as the derivative-method dependence in Example 5.4 made the simultaneous-versus-nested ranking contingent on derivative availability rather than on architecture alone.

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
7. **Comparing architectures with mismatched implementation quality.** A published "nested is better" or "simultaneous is better" conclusion often reflects which implementation had accurate derivatives and a reliable inner solver, not an intrinsic property of the architecture. A fair comparison holds implementation quality fixed and varies only the architecture.
