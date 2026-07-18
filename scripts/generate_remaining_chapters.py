#!/usr/bin/env python3
"""Generate consistent first-draft notebooks and figures for CCD Chapters 5–20."""

from __future__ import annotations
import json, re, shutil, textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def ss(text): return [x.strip() for x in text.split(";") if x.strip()]

SPECS = [
dict(n=5,slug="coordination_strategies",title="Sequential Baselines versus Nested and Simultaneous CCD",subtitle="Separating non-CCD baselines from joint CCD formulations",sections=ss("One-Pass Sequential Baseline;Iterated Sequential Baseline;Nested CCD;Simultaneous or All-at-Once CCD;Shared Formulation and Practical Differences;Feasible-Region Differences;Computational Cost;Convergence Behavior;Selecting a Baseline and CCD Formulation;Hybrid CCD Solution Workflows"),context="One-pass and conventional iterated sequential design are non-CCD baselines. Nested and simultaneous formulations optimize physical and control decisions under one system objective and one coupled feasible set.",example="an active suspension compared under two sequential baselines and two genuine CCD formulations",variables="$p$, $\\theta$, $U$, and $X$",equation=r"\min_{p,z} J_{\mathrm{sys}}(p,z)\;\mathrm{s.t.}\;R(p,z)=0,\;g(p,z)\leq0",concepts=["sequential baseline","iterated handoffs","nested value function","simultaneous sparse NLP","fair comparison"],workflow=["define a fair baseline","state the joint CCD problem","solve nested or simultaneous CCD","verify feasibility","compare validated cost and performance"],figures=["Baseline versus CCD classification","Nested CCD value function","Simultaneous sparse problem graph"],trade=("validated system performance","computational effort"),sources="Herber and Allison on nested and simultaneous CCD; Sundarrajan and Herber on fair comparisons; Allison, Guo, and Han on simultaneous suspension CCD.",openq="Can problem structure predict the best CCD solution architecture before solving every alternative?"),
dict(n=6,slug="open_loop_optimal_control",title="Open-Loop Optimal Control in CCD",subtitle="Discovering physical performance limits",sections=ss("What Open-Loop Optimal Control Means;Open-Loop Single-Control Formulations;Open-Loop Multiple-Control Formulations;Control-Vector Parameterization;State and Control Path Constraints;Free Initial and Final Times;Interpreting Optimal Trajectories;OLOC as a Performance Upper Bound;Sensitivity to Disturbances and Model Error;Why an OLOC-Optimal Plant May Not Be Closed-Loop Optimal"),context="Open-loop CCD reveals performance limits, actuator requirements, active constraints, and unexpected operating phases with few controller-structure assumptions. Its optimized input generally uses information unavailable to a causal controller.",example="an active suspension with complete road preview and a wave-energy converter with known future waves",variables="$p$, $u(t)$, $x(t)$, and known $d(t)$",equation=r"\min_{p,u,x}\Phi+\int L\,dt\;\mathrm{s.t.}\;\dot x=f(t,x,u,p,d)",concepts=["plant variables","known disturbance","optimal control","state response","performance limit"],workflow=["state information assumption","optimize trajectory","identify phases","perturb model and input","translate insight to feedback"],figures=["OLOC trajectory and state response","Causal versus noncausal information","Physical design versus available information"],trade=("realizability","theoretical performance"),sources="Deshmukh, Herber, and Allison on bridging open- and closed-loop co-design; the active-suspension direct-transcription studies.",openq="How can noncausal trajectory structure be converted systematically into robust causal control?"),
dict(n=7,slug="closed_loop_information",title="Closed-Loop CCD and Information Availability",subtitle="Designing systems that can actually be implemented",sections=ss("Fixed-Structure Controller Co-Design;PID and State-Feedback CCD;LQR and Robust-Controller CCD;State Estimation and Kalman Filtering;Model Predictive Control;Preview and Prediction Horizons;Sampling, Computational Delay, and Model Fidelity;Controller Architecture Enumeration;Bridging OLOC and Closed-Loop Control;A Staged Plant-and-Controller Development Process"),context="Closed-loop CCD treats sensing, estimation, prediction, sampling, computation, and controller structure as design resources. Information availability can change both achievable performance and the preferred physical plant.",example="an active suspension under full preview, finite-horizon MPC, reactive feedback, and noisy estimation",variables="$p$, controller and estimator $c$, information architecture $a_I$, and $\\mathcal I_t$",equation=r"u(t)=\pi(\mathcal I_t;c),\quad\mathcal I_t=\{y_{0:t},r_{0:t+T_p},\hat x(t)\}",concepts=["physical plant","sensors","state estimator","prediction horizon","causal controller"],workflow=["compute OLOC limit","restrict information","design estimator","select controller","validate real time"],figures=["Prediction-horizon information cone","OLOC versus MPC versus reactive feedback","Optimal plant versus prediction horizon"],trade=("controller complexity","closed-loop performance"),sources="Bayat and Allison on varying information in suspension CCD; Deshmukh, Herber, and Allison on the OLOC-to-CLC bridge.",openq="How should information quality and computation be priced alongside mass, energy, and hardware?"),
dict(n=8,slug="architecture_codesign",title="Plant, Controller, Sensor, and Actuator Architecture Co-Design",subtitle="Designing what components exist and how they are connected",sections=ss("Parameter Design Versus Architecture Design;Plant Topology Decisions;Actuator Sizing and Placement;Sensor Selection and Placement;Communication and Information-Flow Architecture;Redundancy and Fault Tolerance;Binary and Integer Design Variables;Mixed-Integer CCD;Controller-Order Selection;Architecture–Parameter–Control Optimization"),context="Architecture co-design decides which components, connections, measurements, and control channels exist. Parameter optimization then chooses values within each logically consistent architecture.",example="sensor and actuator selection for a flexible structure, suspension alternatives, and hybrid-powertrain topology",variables="$a\\in\\{0,1\\}^m$, continuous $p$, and controller design $c$",equation=r"\min_{a,p,c}J(a,p,c)\;\mathrm{s.t.}\;g\le0,\;a\in\mathcal A",concepts=["physical topology","actuator set","sensor set","information network","controller architecture"],workflow=["generate architectures","enforce logic","optimize parameters","test faults","compare value"],figures=["Selectable architecture graph","Binary component-selection matrix","Sensor–controller–actuator network"],trade=("architecture cost","system performance"),sources="Garcia-Sanz on broad CCD practice; Deshmukh, Herber, and Allison on architecture decisions informed by OLOC.",openq="How can huge architecture spaces be searched without exhaustive enumeration?"),
dict(n=9,slug="multiobjective_lifecycle",title="Multiobjective, Economic, and Lifecycle CCD",subtitle="Designing for value rather than a single performance number",sections=ss("Multiple Conflicting Objectives;Weighted-Sum and Epsilon-Constraint Methods;Pareto Optimality;Performance, Mass, Energy, and Cost;Reliability and Maintenance;Manufacturability;Environmental and Lifecycle Metrics;Economic Objectives Such as LCOE;Design for Multiple Operating Conditions;Selecting a Final Design from a Pareto Set"),context="Lifecycle CCD expands system value beyond one response metric to capital cost, operation, reliability, maintenance, environmental impact, and multiple operating conditions.",example="a wind turbine balancing AEP, structural mass, fatigue, control effort, capital cost, and LCOE",variables="plant and controller design, scenarios $s$, and objective vector $F$",equation=r"\min F=[-\mathrm{AEP},m,D_{\mathrm{fatigue}},E_u,\mathrm{LCOE}]",concepts=["energy production","loads and fatigue","capital cost","operations","lifecycle value"],workflow=["define stakeholder metrics","scale objectives","generate Pareto set","validate scenarios","select robust candidate"],figures=["Multiobjective Pareto fronts","Lifecycle cost breakdown","Parallel-coordinate candidates"],trade=("lifecycle cost","system performance"),sources="Bayat and coauthors' wind CCD review; the Allison and Martins–Ning optimization texts.",openq="How should uncertain future markets, degradation, and maintenance enter early design?"),
dict(n=10,slug="numerical_optimal_control",title="Numerical Optimal Control for CCD",subtitle="Converting time-dependent design problems into solvable optimization problems",sections=ss("Indirect and Direct Methods;Direct Single Shooting;Multiple Shooting;Control-Vector Parameterization;Direct Transcription;Trapezoidal and Hermite–Simpson Methods;Gaussian Collocation;LG, LGR, and LGL Pseudospectral Methods;Mesh Refinement;Multiphase Problems;Choosing a Transcription Method"),context="Numerical optimal control replaces functions of time with finite decision vectors while preserving dynamics and constraints to a chosen accuracy. Representation, defects, sparsity, scaling, and mesh convergence drive reliability.",example="minimum-time mass–spring motion, a suspension road event, and a two-phase energy converter",variables="discrete $X$, $U$, plant $p$, and possibly final time",equation=r"\min_vJ_h(v)\;\mathrm{s.t.}\;\zeta_h(v)=0,\;g_h(v)\le0",concepts=["continuous problem","time mesh","state and control samples","defect equations","sparse NLP"],workflow=["choose transcription","initialize mesh","solve NLP","estimate error","refine and verify"],figures=["Shooting versus transcription","Time mesh and collocation nodes","State polynomial and defects"],trade=("discretization accuracy","NLP size"),sources="Patterson and Rao on GPOPS-II; Garg and coauthors on LG, LGR, and LGL pseudospectral methods.",openq="Can mesh selection use physical events and optimization sensitivity, not state error alone?"),
dict(n=11,slug="solving_nested_simultaneous",title="Solving Nested and Simultaneous CCD Problems",subtitle="Derivatives, sparsity, scaling, and computational efficiency",sections=ss("Structure of the Nested Problem;Structure of the Simultaneous Problem;Gradient-Based Algorithms;Finite Differences and Complex-Step Derivatives;Algorithmic Differentiation;Direct and Adjoint Sensitivities;Sparse Jacobians and Hessians;Variable and Constraint Scaling;Initialization and Warm Starting;Parallel Computation;Local Versus Global Optimization;Bilevel Sensitivities and Inner-Loop Convergence"),context="Many reported CCD failures are implementation failures: inaccurate derivatives, poor scaling, inconsistent inner convergence, insufficient discretization, hidden nonsmoothness, or unfair comparisons.",example="nested and simultaneous suspension formulations using identical meshes, derivatives, tolerances, and starts",variables="outer $p$, trajectory $w=[X,U]$, and sparse residuals $R(p,w)$",equation=r"\frac{dJ^*}{dp}=\frac{\partial J}{\partial p}+\frac{\partial J}{\partial w}\frac{dw^*}{dp}",concepts=["outer plant loop","inner control solve","sparse simultaneous NLP","derivatives and scaling","verified comparison"],workflow=["scale formulation","verify derivatives","warm start","match tolerances","compare solutions"],figures=["Simultaneous Jacobian blocks","Nested convergence history","Scaling and convergence"],trade=("solution accuracy","runtime"),sources="Herber and Allison; Sundarrajan and Herber; Allison, Guo, and Han.",openq="How can inner convergence and bilevel derivative accuracy be controlled adaptively?"),
dict(n=12,slug="model_fidelity_surrogates",title="Model Fidelity, Surrogates, and Data-Driven CCD",subtitle="Obtaining useful models without making optimization impossible",sections=ss("Analysis Models Versus Optimization Models;Control-Oriented Modeling;Linearization and Local Models;Reduced-Order Models;Response-Surface Surrogates;Dynamic Surrogate Models;Derivative-Function Surrogate Models;Linear Parameter-Varying Models;Gaussian Processes and Neural Networks;Multi-Fidelity Optimization;Model-Error Assessment and Trust;High-Fidelity Validation"),context="A useful CCD model preserves decision-driving couplings while remaining inexpensive, differentiable, and robust enough for repeated optimization. Fidelity is a managed hierarchy.",example="a floating wind turbine modeled in OpenFAST and with reduced, LPV, and derivative-function surrogates",variables="high-fidelity $F_H$, surrogate $F_L$, design $p,c$, and model error $e_M$",equation=r"\dot x\approx\widehat f(t,x,u,p),\quad e_M=y_H-y_L",concepts=["high-fidelity simulation","training data","dynamic surrogate","optimization","high-fidelity confirmation"],workflow=["sample high fidelity","identify reduced model","train surrogate","validate trajectories","optimize and confirm"],figures=["Fidelity pyramid","High-fidelity-to-surrogate workflow","Training and validation samples"],trade=("model accuracy","computational cost"),sources="Sundarrajan and Herber on DFSMs; Bayat and coauthors on multi-fidelity wind CCD.",openq="How can surrogate trust be quantified near optimizer-driven extrapolation?"),
dict(n=13,slug="uncertain_robust_reliable",title="Uncertain, Robust, and Reliable CCD",subtitle="Designing systems that continue to work outside the nominal model",sections=ss("Sources of Uncertainty in CCD;Aleatory and Epistemic Uncertainty;Uncertain Plant Variables;Environmental and Operating Uncertainty;Sensor, Actuator, and Control-Channel Uncertainty;Model-Form Uncertainty;Stochastic-in-Expectation CCD;Chance-Constrained CCD;Probabilistic Robust CCD;Worst-Case Robust CCD;Conditional Value-at-Risk;Fuzzy and Possibilistic Formulations;Robust and Stochastic MPC Within CCD;Uncertainty Propagation"),context="UCCD makes uncertainty explicit in objectives, dynamics, equalities, inequalities, and feasibility claims. Alternative formulations encode average value, failure probability, risk, set-based protection, or imprecise knowledge.",example="a suspension with uncertain mass, road, damping, measurement noise, and actuator efficiency",variables="$\\theta$, design $p,c$, random trajectories, failure events, and risk $\\alpha$",equation=r"\min\mathbb E[J]\;\mathrm{s.t.}\;\mathbb P(g_i\le0)\ge1-\alpha_i",concepts=["uncertainty sources","propagation","risk formulation","robust design","Monte Carlo validation"],workflow=["classify uncertainty","choose representation","propagate","optimize risk","validate failures"],figures=["Uncertainty-source taxonomy","Aleatory versus epistemic uncertainty","Nominal and robust feasible regions"],trade=("nominal performance","robustness"),sources="Azad and Herber's overview of uncertain CCD formulations.",openq="How should model-form uncertainty and distribution shift enter dynamic chance constraints?"),
dict(n=14,slug="diagnostics_workflow",title="Formulation Diagnostics and Practical CCD Workflow",subtitle="How to make a CCD study trustworthy",sections=ss("Deciding Whether a Problem Needs CCD;Identifying Plant–Control Coupling;Sensitivity-Based Coupling Metrics;Selecting Design Variables;Choosing Objectives and Constraints;Feasibility Analysis;Constraint Relaxation;Numerical Verification;Model Validation;Benchmarking Against Sequential Design;Reporting Computational Effort;Reproducibility Standards"),context="A trustworthy CCD study follows an auditable workflow from system objective and dependency mapping through verification, validation, fair baselines, and reproducible reporting. CCD is used only when coupling justifies its cost.",example="a poor suspension formulation repaired for scaling, redundancy, information, actuator limits, mesh, and initialization",variables="dependency map, coupling sensitivities, scaled residuals, mesh $h$, violation $V$, and objective $J$",equation=r"C_{pc}=\|\partial^2J/\partial p\partial c\|,\quad V=\|\max(0,g)\|+\|h\|",concepts=["CCD readiness","dependency and coupling","formulation repair","verification and validation","reproducible evidence"],workflow=["define system objective","map decisions","test coupling","verify numerics","validate and benchmark"],figures=["Complete CCD decision tree","Plant–control coupling heatmap","Feasibility-relaxation process"],trade=("study complexity","credible system benefit"),sources="Dynamic-MDO, fair-comparison, active-suspension, and engineering optimization references.",openq="Can a CCD-readiness score predict value without becoming easy to game?"),
dict(n=15,slug="active_suspension_tutorial",title="Canonical Tutorial: Active Vehicle Suspension",subtitle="A complete CCD problem from equations to implementation",sections=ss("Quarter-Car and Trailing-Arm Models;Road Disturbance Models;Ride Comfort and Suspension-Travel Metrics;Spring and Damper Design;Actuator and Control Constraints;Sequential Baseline;Simultaneous CCD;Nested CCD;OLOC and Closed-Loop CCD;MPC and Information Horizons;Uncertainty Studies;Interpretation of the Optimized Design"),context="The active suspension is compact enough to reproduce yet rich enough to expose plant design, control authority, geometry, dynamic constraints, information, uncertainty, and coordination.",example="a quarter-car and trailing-arm suspension progressed from baseline to simultaneous, nested, MPC, and robust design",variables="vehicle states, spring and damper, actuator, geometry, control, road input, and preview horizon",equation=r"M(p)\ddot q+C(p)\dot q+K(p)q=B(p)u+Ez_r",concepts=["vehicle model","road and metrics","plant and actuator","coordination methods","implementation and uncertainty"],workflow=["derive model","build baseline","solve CCD","restrict information","validate robust design"],figures=["Quarter-car and trailing-arm schematics","Suspension plant-variable geometry","Road and optimal trajectories"],trade=("ride comfort","travel, energy, and hardware"),sources="The complete collection of uploaded suspension CCD papers.",openq="What benchmark and reporting details make suspension CCD reproducible across solvers and labs?"),
dict(n=16,slug="wind_turbine_ccd",title="Wind Turbine Control Co-Design",subtitle="Rotor, structure, platform, and controller as one system",sections=ss("Wind-Turbine Subsystems and Operating Regions;Rotor Aerodynamics and Blade Geometry;Tower and Support-Structure Dynamics;Generator Torque and Blade-Pitch Control;Floating-Platform Dynamics;Design Load Cases and Fatigue;AEP, Structural Cost, and LCOE;Nested and Simultaneous Wind CCD;OLOC, MPC, and Conventional Closed-Loop Control;Surrogate and Multi-Fidelity Modeling;Fixed-Bottom and Floating Examples;Wind-Farm and Supervisory Control Considerations"),context="Wind CCD coordinates aerodynamic capture, structural loads, platform motion, generator and pitch control, operating regions, reliability, and economics.",example="fixed-bottom and floating turbines evaluated over design load cases",variables="blade, tower, platform, generator, controller, loads, AEP, and LCOE",equation=r"\mathrm{LCOE}=(\mathrm{FCR}\,\mathrm{CapEx}+\mathrm{OpEx})/\mathrm{AEP}",concepts=["rotor aerodynamics","structure and platform","torque and pitch control","load cases","AEP and LCOE"],workflow=["parameterize turbine","build coupled model","evaluate load cases","optimize plant and control","validate multi fidelity"],figures=["Turbine subsystem coupling","Blade parameterization and operating regions","Floating-platform degrees of freedom"],trade=("LCOE and loads","energy production"),sources="Bayat and coauthors' integrative wind CCD review; Sundarrajan and Herber on data-driven floating-wind models.",openq="How can full turbine and farm coupling meet industrial load-case and certification cost?"),
dict(n=17,slug="marine_hybrid_energy",title="Marine and Hybrid Renewable-Energy Systems",subtitle="Geometry, power take-off, mooring, storage, and control",sections=ss("Wave and Hydrokinetic Energy Fundamentals;Device Geometry and Hydrodynamics;Power-Take-Off Design;Generator and Drivetrain Design;Mooring and Structural Design;Reactive, Latching, and Model-Predictive Control;Geometry–PTO–Control Coupling;Array Layout and Site Selection;Wind–Wave Hybrid Systems;Storage, Electrolyzers, and Hydrogen Production;Economic and Reliability Considerations;Laboratory and Open-Water Validation"),context="Marine-energy CCD spans hydrodynamic geometry, PTO, generators, mooring, arrays, storage, supervisory control, reliability, and site conditions.",example="a point absorber extended to a floating wind–wave–hydrogen system",variables="geometry, hydrodynamics, PTO, generator, mooring, array, storage, and control",equation=r"m_a\ddot x+b_r\dot x+k_hx=F_{\mathrm{wave}}+F_{\mathrm{PTO}}",concepts=["resource and hydrodynamics","geometry and PTO","generator and mooring","array and hybrid system","validation and economics"],workflow=["characterize site","model conversion chain","co-design device and control","integrate storage","validate lab to sea"],figures=["WEC hydrodynamic–PTO–control variables","Mechanical-to-electrical energy flow","Geometry–PTO–control coupling"],trade=("energy capture","loads, cost, and reliability"),sources="The energy-system, multi-fidelity, and economic themes synthesized in the wind CCD review and general CCD references.",openq="How can device, array, storage, and control be optimized across stochastic seas tractably?"),
dict(n=18,slug="cross_domain_applications",title="Cross-Domain CCD Applications",subtitle="Common principles across different engineering systems",sections=ss("Aerospace Structures and Flight Control;Spacecraft Structures and Attitude Control;Robotics Morphology and Controller Co-Design;Precision-Motion and Manufacturing Systems;Electric and Hybrid Vehicles;Thermal-Management Systems;Buildings and Microgrids;Networked and Distributed Control Systems;Biomedical and Assistive Systems;Lessons That Transfer Across Domains"),context="Different fields use different names, but share physical dynamics, authority, information, active constraints, architecture, multiple timescales, and implementation limits.",example="mini-cases in aircraft, spacecraft, robots, precision stages, vehicles, microgrids, and assistive devices",variables="domain plant, sensors, actuators, control architecture, disturbances, and value metrics",equation=r"\mathrm{value}=\mathrm{performance}-\mathrm{resource\ use}-\mathrm{risk}",concepts=["structures and vehicles","robot morphology","energy and thermal systems","networks and buildings","human-centered systems"],workflow=["identify shared pattern","map variables","locate coupling","choose CCD method","transfer validated insight"],figures=["Cross-domain application map","Robot morphology and control graph","Flexible structure actuator locations"],trade=("domain performance","mass, energy, cost, and risk"),sources="Garcia-Sanz's broad CCD view and Allison–Herber's dynamic-MDO framework.",openq="Which conclusions transfer, and which depend irreducibly on domain physics and regulation?"),
dict(n=19,slug="optimum_to_hardware",title="From Mathematical Optimum to Working Hardware",subtitle="Verification, controller realization, and experimental validation",sections=ss("Why Optimized Trajectories Are Not Sufficient;Controller Approximation and Realization;Discretization and Real-Time Implementation;State Estimation;Actuator and Sensor Selection;Software-in-the-Loop;Model-in-the-Loop;Processor-in-the-Loop;Hardware-in-the-Loop;Prototype Testing;Model Updating and Digital Twins;Safety, Certification, and Deployment Constraints"),context="A mathematical optimum creates value only after causal realization, executable software, timing verification, hardware constraints, experiments, model updating, and safety evidence.",example="an active-suspension rig progressing from ideal torque to estimator-based real-time control and HIL",variables="ideal $u^*$, policy $\\pi$, sampling, latency, quantization, estimator, hardware, and validation residuals",equation=r"u_k=\pi(\hat x_k,r_k),\quad\hat x_{k+1}=F_d(\hat x_k,u_k,y_k)",concepts=["optimal trajectory","causal controller","real-time software","HIL and prototype","safety evidence"],workflow=["realize controller","generate code","test models","close hardware loop","update and certify"],figures=["Model-to-hardware ladder","Real-time control architecture","Controller realization workflow"],trade=("ideal performance","implementation robustness"),sources="Deshmukh, Herber, and Allison on bridging OLOC and realizable control, plus suspension and wind implementation themes.",openq="How can certification evidence be generated concurrently with CCD?"),
dict(n=20,slug="reproducible_future",title="Reproducible CCD and Future Directions",subtitle="Building a common discipline rather than isolated case studies",sections=ss("Benchmark Problems;Standard Reporting Practices;Open-Source Software Organization;Reusable Model and Optimization Interfaces;Automatic Differentiation and Differentiable Simulation;Physics-Informed Learning;Reinforcement Learning Within CCD;System-Level Synthesis and Information Architecture;Distributed and Networked CCD;Human-in-the-Loop CCD;Digital Engineering and Model-Based Systems Engineering;Research Roadmap"),context="CCD will mature through common benchmarks, explicit reporting, reusable interfaces, differentiable tools, physically grounded learning, experimental evidence, and system-level research questions.",example="a reproducible repository with versioned models, data, formulations, solvers, tests, results, and hardware evidence",variables="interfaces, design and trajectory data, derivatives, metadata, seeds, tolerances, and provenance",equation=r"\mathrm{reproducibility}=\mathrm{model}+\mathrm{data}+\mathrm{configuration}+\mathrm{environment}+\mathrm{evidence}",concepts=["benchmarks and reports","model–solver interfaces","differentiable physics and learning","system synthesis","research roadmap"],workflow=["define benchmark","publish interfaces","capture environment","reproduce evidence","extend frontier"],figures=["CCD software ecosystem","Standard model–solver interface","Reproducible-study folder structure"],trade=("method innovation","reproducibility and trust"),sources="The wind CCD roadmap, UCCD taxonomy, information-availability work, and numerical CCD studies.",openq="What minimum common standard makes CCD studies genuinely comparable?"),
]

def slug(text): return re.sub(r"[^a-z0-9]+","-",text.lower()).strip("-")
def nb(text, ident): return {"cells":[{"cell_type":"markdown","id":ident,"metadata":{},"source":text.splitlines(keepends=True)}],"metadata":{"kernelspec":{"display_name":"Python 3","language":"python","name":"python3"},"language_info":{"name":"python","version":"3.10"}},"nbformat":4,"nbformat_minor":5}

def overview(s, figs):
    objectives="\n".join(f"{i}. explain and apply {c};" for i,c in enumerate(s["concepts"][:4],1))
    chapter_map="\n".join(f"{i}. {x}" for i,x in enumerate(s["sections"],1))
    steps="\n".join(f"{i}. {x}." for i,x in enumerate(s["workflow"],1))
    return f"""---
numbering: false
---

# Chapter {s['n']}: {s['title']}

## {s['subtitle']}

{s['context']}

## Learning objectives

After completing this chapter, you should be able to:

{objectives}
5. formulate and verify the chapter methods on {s['example']}.

## Mathematical lens

The recurring quantities are {s['variables']}:

$$
{s['equation']}.
$$

![{s['figures'][0]}.](imgs/{figs[0]})

## Running example

The recurring example is {s['example']}. Retaining one system prevents apparent improvements from being caused by changed physics, information, loads, or metrics.

![{s['figures'][1]}.](imgs/{figs[1]})

## Recommended workflow

{steps}

![{s['figures'][2]}.](imgs/{figs[2]})

:::{{admonition}} Chapter standard
:class: tip
Use common models, operating cases, information, scaling, discretization, derivatives, and stopping conditions whenever alternatives are compared.
:::

## Chapter map

{chapter_map}
"""

def section(s, i, title, figs):
    fig=f"\n\n![{s['figures'][i-1]}.](imgs/{figs[i-1]})" if i<=3 else ""
    concept=s["concepts"][(i-1)%5]; step=s["workflow"][(i-1)%5]
    ending=""
    if i==len(s["sections"]):
        ending=f"""

## Chapter summary

The chapter connected {", ".join(s['concepts'])} through one system formulation. Engineering conclusions require aligned models, information, numerical accuracy, and validation.

## Common mistakes

- changing assumptions while comparing alternatives;
- reporting objective improvement without verified feasibility;
- hiding information, architecture, or uncertainty;
- treating solver convergence as validation; and
- reporting runtime without accuracy, derivatives, and tolerances.

## Exercises

1. Recreate the workflow for {s['example']}.
2. State every variable, unit, dependency, and constraint.
3. Construct a common sequential or nominal baseline.
4. Identify active constraints and the physical bottleneck.
5. Design a test that could falsify the claimed benefit.

## Principal sources

{s['sources']}

## Open research question

{s['openq']}
"""
    return f"""---
numbering: false
---

# {s['n']}.{i} {title}

## Core idea

{title} must be treated as a system-level decision rather than an isolated technique. For {s['example']}, state what is fixed, what is optimized, what information is available, and what equations define feasibility.

The relevant quantities are {s['variables']}. The chapter-level formulation is

$$
{s['equation']}.
$$

For this section, trace how the choice changes **{concept}**, the active constraints, and the implementable engineering design. A method is useful only when its assumptions are explicit and its result answers the same system question as the baseline.
{fig}

## Engineering interpretation

Ask three questions:

1. Which physical, informational, computational, or economic resource changed?
2. Which objective component or active constraint made the change valuable?
3. Does the conclusion survive model, disturbance, initialization, uncertainty, and implementation checks?

A practical action is to **{step}**. Record units and assumptions before optimization, report component objectives and margins afterward, and verify the result using an independent calculation or higher-fidelity model.

:::{{admonition}} Numerical Diagnostic
:class: warning
Do not accept a better objective until dynamic feasibility, path constraints, discretization error, derivative quality, and stopping tolerances have been checked.
:::

:::{{tip}} Activity {s['n']}.{i}: apply the concept
:name: ccd-ch{s['n']}-activity-{i}
Apply {title.lower()} to {s['example']}. State one plant decision, one control or information decision, one active constraint, one verification test, and one reason the conclusion could fail in hardware.
:::
{ending}"""

def framework_svg(s,title):
    colors=["#e9f2ff","#eef8f1","#fff1df","#f4f0fb","#fff0f0"]; strokes=["#2f6fb0","#34845a","#d27a17","#7357a3","#b94c4c"]
    boxes=[]; arrows=[]
    for i,c in enumerate(s["concepts"]):
        x=30+i*205
        lines=textwrap.wrap(c,width=19)[:2]
        label="".join(f'<tspan x="{x+90}" dy="{0 if j==0 else 19}">{line}</tspan>' for j,line in enumerate(lines))
        y=222 if len(lines)>1 else 232
        boxes.append(f'<rect x="{x}" y="190" width="180" height="90" rx="12" fill="{colors[i]}" stroke="{strokes[i]}" stroke-width="2"/><text x="{x+90}" y="{y}" text-anchor="middle" class="t">{label}</text><text x="{x+90}" y="264" text-anchor="middle" class="s">system element</text>')
        if i<4: arrows.append(f'<path d="M{x+180} 235H{x+205}" class="a"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="470" viewBox="0 0 1050 470" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">Framework connecting {", ".join(s["concepts"])}.</desc><defs><marker id="ar" markerWidth="9" markerHeight="9" refX="8" refY="4.5" orient="auto"><path d="M0 0L9 4.5L0 9Z" fill="#40546a"/></marker></defs><style>.h{{font:700 23px Arial;fill:#182638}}.t{{font:600 14px Arial;fill:#182638}}.s{{font:13px Arial;fill:#34485c}}.a{{stroke:#40546a;stroke-width:2;marker-end:url(#ar)}}</style><rect width="1050" height="470" fill="#fbfcfe"/><text x="525" y="38" text-anchor="middle" class="h">{title}</text>{''.join(boxes)}{''.join(arrows)}<text x="525" y="370" text-anchor="middle" class="s">One system objective • common assumptions • verified feasibility</text></svg>'''

def workflow_svg(s,title):
    rows=[]
    for i,x in enumerate(s["workflow"]):
        y=90+i*82
        rows.append(f'<circle cx="110" cy="{y}" r="24" fill="#2f6fb0"/><text x="110" y="{y+6}" text-anchor="middle" class="n">{i+1}</text><rect x="155" y="{y-26}" width="650" height="52" rx="10" fill="#f2f5f8" stroke="#65798e" stroke-width="2"/><text x="480" y="{y+6}" text-anchor="middle" class="t">{x}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520" viewBox="0 0 900 520" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">Workflow: {", ".join(s["workflow"])}.</desc><style>.h{{font:700 23px Arial;fill:#182638}}.t{{font:600 17px Arial;fill:#182638}}.n{{font:700 18px Arial;fill:white}}</style><rect width="900" height="520" fill="#fbfcfe"/><text x="450" y="36" text-anchor="middle" class="h">{title}</text>{''.join(rows)}</svg>'''

def trade_svg(s,title):
    x,y=s["trade"]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="520" viewBox="0 0 900 520" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">Conceptual tradeoff between {x} and {y}.</desc><style>.h{{font:700 23px Arial;fill:#182638}}.t{{font:15px Arial;fill:#34485c}}.a{{stroke:#25384c;stroke-width:2.5}}.c{{fill:none;stroke:#2f6fb0;stroke-width:4}}</style><rect width="900" height="520" fill="#fbfcfe"/><text x="450" y="36" text-anchor="middle" class="h">{title}</text><path d="M110 430H825M110 430V70" class="a"/><text x="470" y="485" text-anchor="middle" class="t">{x}</text><text x="30" y="250" text-anchor="middle" transform="rotate(-90 30 250)" class="t">{y}</text><path d="M165 115C260 180 350 275 460 330S675 402 780 420" class="c"/><circle cx="260" cy="190" r="10" fill="#2f6fb0"/><circle cx="460" cy="330" r="12" fill="#d27a17"/><circle cx="675" cy="402" r="10" fill="#34845a"/><circle cx="570" cy="225" r="9" fill="#b94c4c"/><text x="585" y="220" class="t">unverified candidate</text><text x="475" y="318" class="t">balanced design</text></svg>'''

def generate(s):
    d=ROOT/f"{s['n']:02d}_{s['slug']}"
    if d.exists(): shutil.rmtree(d)
    (d/"imgs").mkdir(parents=True)
    figs=[f"{i+1:02d}-{slug(t)}.svg" for i,t in enumerate(s["figures"])]
    for name,data in zip(figs,[framework_svg(s,s["figures"][0]),workflow_svg(s,s["figures"][1]),trade_svg(s,s["figures"][2])]): (d/"imgs"/name).write_text(data)
    files=["00-index.ipynb"]
    (d/files[0]).write_text(json.dumps(nb(overview(s,figs),f"ch{s['n']}-index"),indent=1,ensure_ascii=False)+"\n")
    for i,t in enumerate(s["sections"],1):
        name=f"{i:02d}-{slug(t)}.ipynb"; files.append(name)
        (d/name).write_text(json.dumps(nb(section(s,i,t,figs),f"ch{s['n']}-sec{i}"),indent=1,ensure_ascii=False)+"\n")
    return d,files

def update_toc(items):
    p=ROOT/"myst.yml"; text=p.read_text(); marker="  # To autogenerate a Table of Contents"
    start="    # BEGIN GENERATED CHAPTERS 5-20\n"; end="    # END GENERATED CHAPTERS 5-20\n"
    if start in text:
        before,rest=text.split(start,1); _,after=rest.split(end,1); text=before+after
    parts={5:"Part II — CCD Formulations and Design Architectures",10:"Part III — Computational Methods",15:"Part IV — Complete Application Studies",19:"Part V — Deployment and Research Frontiers"}
    lines=[start.rstrip()]
    for s,d,files in items:
        if s["n"] in parts: lines += [f'    - title: "{parts[s["n"]]}"',"      children:"]
        lines += [f'        - title: "Chapter {s["n"]}: {s["title"]}"',"          children:"]
        rel=d.relative_to(ROOT)
        lines += [f"            - file: {rel}/{f}" for f in files]
    lines.append(end.rstrip()); text=text.replace(marker,"\n".join(lines)+"\n"+marker); p.write_text(text)

def main():
    items=[(s,*generate(s)) for s in SPECS]; update_toc(items)
    print(f"Generated {len(items)} chapters and {sum(len(x[2]) for x in items)} notebooks")

if __name__=="__main__": main()
