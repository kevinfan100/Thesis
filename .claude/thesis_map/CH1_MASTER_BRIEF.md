# Thesis Argument Canon (Single Source of Truth)

Last updated: 2026-02-23 (late-3)  
Owner: Kevin + Codex

## 0. Purpose and Priority

This is the highest-priority thesis-argument file for this project.

Rules:
1. If any chapter draft conflicts with this file, this file wins.
2. New ideas must be merged into this file before large text rewrites.
3. Chapter writing must follow the claim-evidence structure defined here.

---

## 1. Locked Thesis Tone (定調)

Core tone:
1. Prior work already demonstrated strong end-performance.
2. This thesis does not re-argue feasibility by repeating performance showcase.
3. This thesis gives equal-weight emphasis to development-process structuring and workflow automation, then verifies both through traceable evidence.

In one sentence:
`The thesis contribution is not "more performance numbers," but "a reusable development process and an automation-enabled workflow for hexapole-form tweezers, validated through a traceable ID->Flux->Force evidence chain."`

---

## 2. Core Problem Statement

The key gap is a missing attribution chain between:
1. What is physically observed in the actuator.
2. What model representation is extracted.
3. Why a specific control design is selected.
4. What measurable outcome is improved.
5. What physical meaning that improvement implies for operation.

This missing chain prevents objective-level reasoning and reproducible design decisions, and is exactly where this thesis positions its value.

---

## 3. Contribution Hierarchy (Locked)

## 3.1 Primary Contribution A (Main, Equal Weight)

Development-process structuring as a reusable blueprint:
1. Decompose the full development path into explicit stages from open-loop calibration to force-output validation.
2. Preserve physical interpretation at each stage so design decisions are explainable.
3. Keep the chain explicit as:
   `Identification -> Flux Control -> Force Generation`.

Value:
1. Reduces development ambiguity for new hexapole-form tweezer platforms.
2. Converts tacit implementation experience into an explicit engineering path.

## 3.2 Primary Contribution B (Main, Equal Weight)

Workflow automation as a practical enabler:
1. Automate repeatable identification operations in a fixed pipeline.
2. Provide a simulation-and-tuning environment for flux control once identification is completed.
3. Connect automated outputs to downstream force-generation validation.

Value:
1. Lowers development difficulty and entry barrier.
2. Improves reproducibility and iteration speed across platforms.

## 3.3 Technical Realization Thread (Mainline)

Use ID/Flux/Force as the technical realization of the two primary contributions:
1. ID stage: extract design-relevant model information from calibration data.
2. Flux stage: analyze control design tradeoffs and decoupling behavior.
3. Force stage: evaluate downstream quality under allocation/scheduling choices.

Value:
1. Ensures that process structuring and automation are grounded in verifiable control evidence.
2. Maintains one continuous causal chain for chapter-level validation.

---

## 4. Boundary and Claim Strength

Claim boundary:
1. Main claims target hexapole-form tweezers and are not limited to one specific machine implementation.
2. Claims are supported by tested operating conditions and available evidence range.
3. Generalization is asserted at framework/workflow level; implementation details may vary by hardware.

Allowed claim style:
1. `evidence supports`
2. `consistent with`
3. `at the tested operating point`
4. `generalizable to hexapole-form tweezers with compatible architecture`

Avoid:
1. `universal across all actuation systems`
2. `always`
3. `fully general without architectural conditions`

---

## 5. Ch.1 Writing Responsibilities (Locked)

## 5.1 Ch1.1 Background and Motivation

Must do:
1. Problem context and system relevance.
2. Motivation-first narrative: why this thesis direction is necessary and meaningful for design and operation.
3. Prior baseline and current gap as supporting context (not the dominant tone).
4. Why ID is a natural starting point for this thesis logic.

Should not overdo:
1. Full technical details of your implementation pipeline.
2. Full contribution bullet-proofing (belongs to Ch1.2).
3. Detailed method internals and derivations (belong to later chapters).

## 5.2 Ch1.2 Research Objective and Scope

Must do:
1. Explicitly define one overall objective with two equal-weight primary pillars:
   process structuring + workflow automation.
2. Keep three technical aims (ID/Flux/Force) as implementation of the two pillars.
3. State simulation and experiment as same-thread evidence in each aim.
4. Define scope, claim boundary, and what is out of scope.

## 5.3 Ch1.3 Dissertation Overview

Must do:
1. Chapter-to-question mapping.
2. Chapter-to-evidence mapping.
3. Make verification path visible before readers enter methods chapters.

---

## 6. Identification Narrative Blueprint (for Ch1.1 + Ch3 consistency)

Recommended sequence:
1. Open-loop calibration reveals physical phenomena.
2. Fundamental-component FRF extraction yields comparable data.
3. 36-channel behavior is represented in a controller-usable reduced structure.
4. Low-frequency-priority weighted fitting aligns with control objectives.
5. Identification output is interpreted by downstream design relevance.

Important integration rule:
1. In Ch1.1, mention digital-control issues naturally but do not force hard-layer boundaries in wording.
2. Detailed discretization treatment appears naturally when flux-control logic is introduced.

---

## 7. Traceability Checklist (Use for every key claim)

Each key claim must answer all five:
1. Observable fact: what was measured or observed?
2. Modeling meaning: what does it represent physically/systemically?
3. Design decision: what action was taken because of that meaning?
4. Evidence/metric: how is impact verified?
5. Limitation: under what condition is this statement valid?

If one item is missing, claim is incomplete.

---

## 8. Terminology and Notation (Locked)

Keep consistent:
1. `Optimal Current Allocation`
2. `Optimal Flux Allocation`
3. `\mathbf{u}, \mathbf{v}_m, \mathbf{v}_d, \mathbf{f}_d, \mathbf{B}, \boldsymbol{\Phi}`

Style:
1. English term first; Chinese as support.
2. One concept, one wording.
3. No inflated claim words without metrics.

---

## 9. Immediate Next Writing Plan

1. Freeze this canon as the reference before further chapter edits.
2. Finish Ch1.1 with background/gap logic first (avoid overloading contributions here).
3. Move detailed contribution framing to Ch1.2.
4. After Ch1 is stable, derive Abstract by compression only (no new claims).

---

## 10. Change Log

| Date | Change | Reason |
|---|---|---|
| 2026-02-21 | Rebuilt as thesis argument canon; locked contribution hierarchy and Ch1 responsibilities | Prevent thesis drift and maintain one stable argument baseline |
| 2026-02-22 | Shifted wording to explicit objective/goal framing in Ch1.1 argument baseline | Align motivation with "design intent, tradeoff explanation, and reproducible decisions" |
| 2026-02-23 | Locked System ID round-1 decisions and added professor-report alignment notes | Ensure discussion-to-chapter traceability before Ch1.2~Ch5 drafting |
| 2026-02-23 | Added Flux Control round-1 inventory and Force Generation discussion status | Build full cross-layer discussion map before unified Ch1 rewrite |
| 2026-02-23 (late) | Locked user decisions for Flux discussion scope and deferred validations | Keep Ch1 planning stable before simulation/experiment completion |
| 2026-02-23 (late-2) | Updated Ch1 wording policy: avoid explicit pending-bandwidth statement and treat B-decoupling comparison as validated evidence | Align chapter tone with latest user decision |
| 2026-02-23 (late-3) | Switched Ch1 strategy to two equal-weight pillars (process structuring + workflow automation) with strong framework-level generalization | Align thesis motivation with latest locked user direction |

---

## 11. Discussion Protocol (Locked)

This protocol is used for all upcoming chapter-level discussions to avoid thesis drift.

Step A: User oral record (you speak first)
1. Intended claim.
2. What was inherited.
3. What was changed.
4. What was compared.
5. What evidence exists.
6. What physical/operational meaning should be emphasized.

Step B: Repository/Git verification (Codex side)
1. Verify implementation paths under `/Users/kevin/Code`.
2. Verify timeline and ownership through Git history/blame.
3. Separate confirmed facts from inference.

Step C: Five-block inventory output (fixed)
1. `Baseline`
2. `Delta`
3. `Alternatives`
4. `Evidence`
5. `Interpretation`

Step D: Claim gate before chapter writing
1. No claim enters Ch1.2~Ch5 unless at least one concrete evidence path exists.
2. Claims are written as tested-condition claims, not universal claims.

Step E: Single-source update
1. Each round updates this file first.
2. Chapter text is updated only after this file is accepted.

---

## 12. System ID Inventory (Round 1, Provisional)

Source basis:
1. User oral description (current round).
2. `Openloop_Cali` code and Git history.
3. `r_controller_package` code and Git history.
4. Professor closing-report screenshots and equations already aligned with implemented constants.

### 12.1 Baseline (before your current round)

1. Open-loop frequency-response calibration and 6x6 modeling already existed as a valid technical route.
2. A 6x6 shared-dynamics-plus-gain-matrix representation was available in legacy MIMO fitting:
   `H(s) = [A2/(s^2 + A1 s + A2)] * B`.
3. Discrete control-model constants (`k_o`, `b`, `a1`, `a2`, `B`) were already used in controller parameterization.

### 12.2 Delta (your current round)

1. You rebuilt the identification pipeline end-to-end from raw data, instead of only inheriting final coefficients.
2. You made the observable-phenomena path explicit in the workflow:
   coupling + hysteresis/bias + frequency-dependent nonlinearity (magnitude/phase behavior).
3. You used dominant-frequency extraction for FRF construction while retaining THD/spectrum and Lissajous views as nonlinear evidence channels.
4. You kept the modeling path as:
   first 36 independent 2nd-order channels, then reduced to shared dynamics with channel-specific DC gain matrix for controller design.
5. You introduced weighted fitting with low-frequency priority as a deliberate control-oriented tradeoff (not pure global fit optimization).

### 12.3 Alternatives considered (for explicit comparison writing)

1. Unweighted or high-cutoff fitting versus low-frequency-priority weighted fitting.
2. Full 36-channel independent dynamics for control design versus shared-dynamics-plus-gain representation.
3. End-result-only comparison versus component/layer-linked reasoning from identification output.

### 12.4 Evidence map (code + history)

Openloop pipeline evidence:
1. Fundamental-bin FRF extraction in FFT:
   `/Users/kevin/Code/Openloop_Cali/pipeline/step_fft.m:75`
2. THD computation retained as nonlinear indicator:
   `/Users/kevin/Code/Openloop_Cali/pipeline/step_fft.m:84`
3. Phase-offset normalization before fitting:
   `/Users/kevin/Code/Openloop_Cali/pipeline/step_fit.m:73`
4. Weighted fitting (`p_weight`, `wc_Hz`) exposed as design knobs:
   `/Users/kevin/Code/Openloop_Cali/pipeline/step_fit.m:34`
5. Weighting law and low-frequency emphasis:
   `/Users/kevin/Code/Openloop_Cali/functions/fit_single_tf.m:50`
6. Lissajous comparison support (Vm-current loop inspection):
   `/Users/kevin/Code/Openloop_Cali/pipeline/step_compare.m:868`
7. 36-channel fitting and shared-dynamics MIMO reduction:
   `/Users/kevin/Code/Openloop_Cali/legacy/Model_6_6_Continuous_Weighted.m:309`
8. Shared dynamics + `B` reconstruction and ZOH conversion section:
   `/Users/kevin/Code/Openloop_Cali/legacy/Model_6_6_Continuous_Weighted.m:410`

Controller linkage evidence:
1. `r_controller_package` explicitly uses identification-derived constants and `B` matrix:
   `/Users/kevin/Code/r_controller_package/model/inner_loop_ctrl/model_base_ctrl_params.m:60`
2. Same coupling matrix mapping used in PI baseline path:
   `/Users/kevin/Code/r_controller_package/model/inner_loop_ctrl/pi_ctrl_params.m:50`
3. Git blame confirms these constants existed since initial package baseline and were preserved through refactors.

### 12.5 Interpretation (how this supports your thesis tone)

1. Identification is not only "fit quality reporting"; it is the stage where physical observations are converted into control-usable structure.
2. The low-frequency weighted fit is an engineering choice aligned with control objectives, not a purely numerical preference.
3. The reduced model (shared dynamics + channel gains) is a design-tractability decision that preserves coupling information needed by controller synthesis.
4. This supports the thesis main line:
   explicit design intent -> explicit tradeoff -> reproducible controller-relevant model.

### 12.6 Decisions Confirmed (Locked)

1. No extra compensation block is claimed beyond the current identification processing path.
2. The "hysteresis-related handling" in this stage is described as phase-offset and response-shape processing in the FRF/fitting workflow, not as a separate standalone compensation controller.
3. Primary ID quality criterion is low-frequency error within the effective control bandwidth.
4. High-frequency fitting degradation is explicitly treated as an allowed tradeoff when it improves low-frequency control relevance.
5. Ch1.1 stays at control-oriented motivation level; detailed ZOH/discrete-time derivation is deferred to Flux Control chapter context.

### 12.7 Frequency-Dependent Nonlinearity: Wording Guide (for Ch1.1/Ch3 consistency)

Use this interpretation consistently:
1. Time-domain evidence: Vm-current loops (Lissajous-type views) vary with frequency and show non-elliptic behavior plus low-frequency phase lag.
2. Frequency-domain evidence: at low frequency, phase is not exactly zero and magnitude/phase trends shift with excitation frequency.
3. Modeling implication: dominant-frequency FRF extraction is used to build a control-usable linearized representation at each operating condition.
4. Boundary statement: this representation is an engineering reduction for controller design, not a claim that actuator physics is globally linear.

Recommended sentence pattern:
1. Observable fact -> "Frequency sweep data show frequency-dependent shape and phase behavior, with low-frequency phase lag consistent with hysteresis-related effects."
2. Design choice -> "Therefore, the ID workflow extracts dominant-frequency FRF components and applies low-frequency-priority weighted fitting."
3. Scope/boundary -> "This treatment targets control-relevant accuracy in bandwidth, while allowing higher-frequency mismatch."

### 12.8 Professor Report Alignment (text-converted source)

Reference file:
`/Users/kevin/Downloads/1.5_FPGA_GUI_and_automation.md`

Aligned points:
1. Automated open-loop scan + steady-state detection + FFT-based fundamental extraction for 36 components.
2. 6x6 to simplified shared-dynamics model with coupling matrix `B`.
3. Low-frequency coupling/bandwidth characterization as useful basis for digital control design.
4. Controller-side constants and matrix continuity are consistent with current package implementation (`k_o`, `b`, `a1`, `a2`, `B`).

Important writing guard:
1. Mention the above as "consistent with project documentation and implemented code path".
2. Avoid claiming any additional compensation module unless code-level evidence is explicitly provided.

---

## 13. Flux Control Inventory (Round 1, Provisional)

Source basis:
1. User oral description (current round).
2. `r_controller_package` controller code and test scripts.
3. Current thesis Ch1 framing (`01_introduction.tex`).
4. Professor report text-converted file.

### 13.1 Baseline (before your current round)

1. Prior studies established PI and model-based flux control paths with Hall-sensor feedback.
2. The controller form already includes three roles: feedforward, feedback, disturbance compensation.
3. Existing scripts already support frequency-response verification (gain/phase, bandwidth, theory-error summary).

### 13.2 Delta (your current round framing)

1. Start the flux-control chapter from controller-design usage of identified discrete-time model (ZOH-based form), not from generic control theory.
2. Use PI as a physically interpretable baseline: design from model, then compare simulated and measured frequency response.
3. Make decoupling importance explicit through `B`-matrix logic (`B^{-1}` mapping), with planned ablation against diagonal-only treatment.
4. Use high-frequency mismatch between design prediction and measured response to motivate why PI-only is not enough in this system.
5. Introduce disturbance-observer and model-based control as targeted responses to model mismatch and hysteresis-related residual effects.
6. Keep feedforward motivation tied to bandwidth objective: make inner-loop behavior close to a first-order design target in the validated band, so downstream layers can be designed more independently.

### 13.3 Alternatives considered (for explicit comparison writing)

1. PI baseline versus model-based controller.
2. Feedforward enabled versus bypassed.
3. Full `B` decoupling versus diagonal-only decoupling (validated comparison evidence available).
4. End-to-end performance-only comparison versus component-level attribution.

### 13.4 Evidence map (code + docs)

Controller structure and parameters:
1. Identification-derived constants and `B` matrix in model-based parameters:
   `/Users/kevin/Code/r_controller_package/model/inner_loop_ctrl/model_base_ctrl_params.m:60`
2. PI path also uses `B^{-1}` mapping:
   `/Users/kevin/Code/r_controller_package/model/inner_loop_ctrl/pi_ctrl_params.m:50`
3. Disturbance compensation output (`u_w1`) is explicitly exported:
   `/Users/kevin/Code/r_controller_package/model/inner_loop_ctrl/model_base_ctrl_function.m:199`

Test and verification scripts:
1. Controller switching (PI/model-based) in frequency-sweep script:
   `/Users/kevin/Code/r_controller_package/test_script/inner_loop/run_inner_loop_bode.m:56`
2. Theory-vs-experiment error summary and -3 dB bandwidth extraction:
   `/Users/kevin/Code/r_controller_package/test_script/inner_loop/run_inner_loop_bode.m:708`
3. `u_w1` collection in single-frequency script:
   `/Users/kevin/Code/r_controller_package/test_script/inner_loop/run_inner_loop_test.m:319`

Professor report alignment:
1. Discrete-time model from ZOH conversion and controller design context:
   `/Users/kevin/Downloads/1.5_FPGA_GUI_and_automation.md:46`
2. Feedback + feedforward + disturbance observer structure:
   `/Users/kevin/Downloads/1.5_FPGA_GUI_and_automation.md:58`
3. Expected-frequency-response discussion under model assumptions:
   `/Users/kevin/Downloads/1.5_FPGA_GUI_and_automation.md:68`

### 13.5 Interpretation (thesis-level meaning)

1. Flux-control contribution is framed as explicit design tradeoff explanation and reproducible decision logic, not only final-performance restatement.
2. PI is not dismissed; it is used as a transparent baseline that exposes where prediction and measured response start to diverge.
3. Model-based components are justified by physically interpretable mismatch channels, then validated by frequency-domain evidence.
4. Claim boundary: statements are made for tested conditions and validated frequency range.

### 13.6 Optional quality gate (not mandatory for current drafting)

1. High-frequency discrete-consistency check can be added later to show that observed mismatch is not mainly from numerical solver artifacts.
2. This is a method-validity safeguard, not a main thesis claim.

### 13.7 User-locked decisions (current stage)

1. Bandwidth target may still be refined after additional validation, but Ch1 text should not explicitly emphasize "pending fixation."
2. Current quantitative indicators follow the already discussed set (frequency response gain/phase, bandwidth-related behavior, theory-vs-measurement error, tracking/error observations, and disturbance-related signals such as `u_w1` when applicable).
3. `B`-matrix decoupling comparison (`full B` vs `diag(B)`) is treated as validated evidence and can be written as an established comparison in Ch1.
4. Current writing stage prioritizes complete cross-layer argument construction; final numeric-strength claims are deferred until evidence is closed.

---

## 14. Force Generation Inventory (Round 1, Locked Scope)

Source basis:
1. User-locked scope in current discussion.
2. `r_controller_package` force-generation code and test scripts (primary).
3. Current Ch1 motivation/gap framing.
4. Professor report-aligned force-allocation context (as prior baseline context only).

### 14.1 Baseline (before your current round)

1. Force generation is already established as:
   `f_d -> inverse model -> v_d -> flux control -> v_m -> force model -> f_m`.
2. Optimal flux allocation and inverse-model route are available as prior technical baseline.
3. Single-axis force-frequency characterization and cross-axis observation paths already exist in test scripts.

### 14.2 Delta (your current round framing)

1. Force layer will be discussed as a control-chain analysis problem, not only end-result demonstration.
2. The main comparative focus is scheduling effect at the input of inverse model:
   ZOH versus Linear interpolation (no S-curve in current locked scope).
3. The verification context is locked to:
   single-axis frequency sweep with simultaneous three-axis decoupling/coupling inspection.
4. At this stage, force-layer evidence is interpreted as chain-level behavior analysis:
   scheduling effect -> inner-loop interaction -> force-output behavior, with explicit design tradeoff explanation.

### 14.3 Alternatives considered (locked for this stage)

1. Scheduling: ZOH (`sample_rate_mode=1`) versus Linear (`sample_rate_mode=2`).
2. Observation perspective A: frequency-domain transfer and decoupling (`main-axis` + `cross-axis`).
3. Observation perspective B: time-domain interpolation/detail and worst-case deviation.
4. Reporting style: pipeline-level attribution versus performance-only summary.

### 14.4 Evidence map (primary: r_controller_package)

Pipeline and model path:
1. End-to-end force pipeline statement in script header:
   `/Users/kevin/Code/r_controller_package/test_script/force_generation/run_force_bode.m:5`
2. Inverse-model scheduling modes (ZOH/Linear/Direct) implemented:
   `/Users/kevin/Code/r_controller_package/model/flux_allocation/inverse_model_function.m:32`
3. Scheduling mode application in force bode sweep:
   `/Users/kevin/Code/r_controller_package/test_script/force_generation/run_force_bode.m:455`

Frequency-domain indicators in script:
1. Main-axis transfer ratio `|f_m/f_d|` and phase:
   `/Users/kevin/Code/r_controller_package/test_script/force_generation/run_force_bode.m:362`
2. Cross-axis coupling ratio:
   `/Users/kevin/Code/r_controller_package/test_script/force_generation/run_force_bode.m:366`
3. Cross-axis isolation (derived from coupling vs main-axis transfer):
   `/Users/kevin/Code/r_controller_package/test_script/force_generation/run_force_bode.m:949`

Time-domain indicators in script:
1. Force max error (and RMS) from force-error signal:
   `/Users/kevin/Code/r_controller_package/test_script/force_generation/run_force_generation_test.m:729`
2. Interpolation-detail error (`f_d_interp - f_m`) in hardware-mode detail view:
   `/Users/kevin/Code/r_controller_package/test_script/force_generation/run_force_generation_test.m:1041`

Frequency-sweep context:
1. Nyquist/hardware-limit guard in sweep script:
   `/Users/kevin/Code/r_controller_package/test_script/force_generation/run_force_bode.m:410`
2. Scheduling attenuation model shown explicitly (`sinc`/`sinc^2`) for ZOH/Linear:
   `/Users/kevin/Code/r_controller_package/test_script/force_generation/run_force_bode.m:775`

### 14.5 Interpretation (thesis-level meaning)

1. Force-generation contribution is framed as clarifying design tradeoffs and reproducing decision logic in the full chain, not as a single metric comparison.
2. Main-axis transfer, cross-axis coupling, interpolation effect, and worst-case error should be read as a connected evidence set.
3. In the current script-level stage, most comparisons are chain-consistency oriented (e.g., `f_d_interp` versus `f_m`) and are used for design reasoning.
4. Stronger physical-endpoint claims are deferred until simulation/experiment closure.

### 14.6 User-locked decisions (current stage)

1. Primary evidence repository for force layer is:
   `/Users/kevin/Code/r_controller_package`
2. Scheduling comparison scope is fixed to:
   ZOH and Linear only.
3. Verification context is fixed to:
   single-axis sweep plus three-axis decoupling/coupling readout.
4. Priority evidence focus is fixed to:
   transfer/decoupling behavior plus worst-case error, with no over-commitment to a single ratio-only narrative.
5. Additional experiments and stronger final numeric claims will be added later and do not block current Ch1 planning.

---
