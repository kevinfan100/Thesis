# Thesis Argument Canon (Single Source of Truth)

Last updated: 2026-02-22  
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
3. This thesis makes design objectives and decision logic explicit, then verifies them through traceable evidence.

In one sentence:
`The thesis contribution is not "more performance numbers," but "an explicit, goal-oriented, and verifiable design logic from observed phenomena to control outcomes."`

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

## 3.1 Primary Contribution A (Main)

Construct a control-oriented identification logic from open-loop calibration:
1. Observe coupling, hysteresis/bias, and frequency-response nonlinearity from open-loop experiments.
2. Build 36 FRF sets via fundamental-component extraction (FFT-based pipeline).
3. Convert representation to a controller-usable form: shared 2nd-order dynamics + channel-dependent DC gains (`\mathbf{B}`).
4. Use weighted fitting to prioritize low-frequency model fidelity for control-relevant behavior.

Value:
1. Turns identification from "fit result reporting" into "design-relevant model extraction."
2. Provides physically meaningful model structure for downstream control reasoning.

## 3.2 Primary Contribution B (Main)

Build a cross-layer causal chain:
`Identification -> Flux Control -> Force Generation`

Value:
1. Every major design choice has measurable downstream impact.
2. End-performance can be explained by component-level and layer-level evidence.

## 3.3 Primary Contribution C (Main)

Define evaluation logic based on control relevance, not only global fitting score.

Value:
1. "Good identification" is judged by usefulness for control prediction and design decisions.
2. The thesis can explain why model mismatch matters (or does not matter) for specific control objectives.

## 3.4 Secondary Contribution D (Supporting, not main axis)

Engineering and workflow consolidation (automation/integration/tooling/HMI/FPGA pipeline).

Value:
1. Improves reproducibility and operational efficiency.
2. Supports the main scientific contribution, but is not the primary novelty claim.

---

## 4. Boundary and Claim Strength

Claim boundary:
1. Main claims are supported at tested operating conditions and available evidence range.
2. Avoid early universal/generalized claims across all possible configurations.

Allowed claim style:
1. `evidence supports`
2. `consistent with`
3. `at the tested operating point`

Avoid:
1. `universal`
2. `always`
3. `fully general`

---

## 5. Ch.1 Writing Responsibilities (Locked)

## 5.1 Ch1.1 Background and Motivation

Must do:
1. Problem context and system relevance.
2. Prior baseline and current gap.
3. Why the missing attribution chain matters.
4. Why ID is a natural starting point for this thesis logic.

Should not overdo:
1. Full technical details of your implementation pipeline.
2. Full contribution bullet-proofing (belongs to Ch1.2).
3. Detailed method internals and derivations (belong to later chapters).

## 5.2 Ch1.2 Research Objective and Scope

Must do:
1. Explicitly define research objectives and research questions.
2. State primary vs secondary contributions.
3. Define scope, metrics direction, and claim boundary.
4. Clarify what is not the central contribution.

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
