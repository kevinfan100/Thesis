# CH1 Master Brief

This is the single reading entry for Chapter 1 planning and execution.

## 1. Thesis Positioning

This thesis uses a Hall-sensor-based hexapole electromagnetic actuator and focuses on a control-centric chain:

`System Identification -> Flux Control -> Force Generation`

The goal is not only to report final performance, but to provide a quantitative and reproducible analysis framework that explains why each layer-level design choice is effective.

## 2. Prior Baseline (Condensed)

| Year | Baseline result | Reference |
|---|---|---|
| 2011 | Hexapole design + current-based force model | \cite{zhang2011design} |
| 2021 | Optimal current allocation for over-actuated force production | \cite{long2021optimal} |
| 2022 | Hall-sensor-based force model and inverse model | \cite{long2022hallsensor} |
| 2023 | Ultra-precise high-speed untethered manipulation | \cite{meng2023ultraprecise} |
| 2024 | High-bandwidth flux control and piconewton force control | \cite{meng2024piconewton} |

## 3. Research Gaps (Three locked gaps)

1. Identification gap: limited systematic discussion of fitting sensitivity, model-quality metrics, and cross-configuration consistency in 6x6 identification.
2. Flux-control gap: limited component-level comparison between PI and model-based control (disturbance observer, feedback law, prefilter).
3. Force-generation gap: limited quantitative analysis of how command scheduling and nonlinear transfer propagate into force-accuracy and bandwidth limits.

## 4. Objective and Scope

Primary objective: build a decision-complete analysis path from identification to force output, with quantitative traceability.

Scope includes:
- 6x6 system identification workflow and quality evaluation.
- Inner-loop flux-control comparison (PI vs model-based).
- Force-generation accuracy and bandwidth bottleneck analysis.
- FPGA-oriented implementation consistency.

Out of primary scope:
- Outer-loop motion control as the central contribution of Ch.1 (kept as downstream context).

## 5. Contribution Statements (with metrics hooks)

1. Reproducible 6x6 identification workflow with quality checks and cross-configuration comparison.
   Metrics hook: fitting residual, phase residual, repeatability.
2. Component-level flux-control analysis with PI baseline.
   Metrics hook: closed-loop bandwidth, cross-coupling suppression, tracking error.
3. Force-generation scheduling and nonlinear transfer analysis.
   Metrics hook: force amplitude error, THD-related distortion, effective bandwidth.
4. FPGA implementation alignment with design predictions.
   Metrics hook: sim-to-hardware response consistency.

## 6. Ch.1 Three-Section Logic

1.1 Background and Motivation:
- Context -> platform relevance -> prior baseline -> gap definition.

1.2 Research Objective and Scope:
- RQs -> methods -> metrics -> boundaries.

1.3 Dissertation Overview:
- chapter-to-question and chapter-to-evidence mapping.

## 7. Chapter-to-Evidence Mapping

- Ch.2: modeling foundation.
- Ch.3: RQ1 (identification workflow + model quality).
- Ch.4: RQ2 (PI vs model-based flux control).
- Ch.5: RQ3 (force-generation scheduling + bottlenecks).
- Ch.6: implementation and experiment-aligned verification.
- Ch.7: motion-control extension context.
- Ch.8: conclusions and validated claims.

## 8. Terminology Standard (English-first)

Use English terms as primary forms, with Chinese support at first mention.

| Primary English term | Chinese support | Acronym | Avoid |
|---|---|---|---|
| System Identification | 系統鑑別 | ID | system modeling (when you mean ID process) |
| Flux Control | 磁通控制 | - | magnetic control (too broad) |
| Force Generation | 力生成 | - | force control (unless specifically outer-loop) |
| Over-actuated | 過驅動 | - | redundant only (without actuator context) |
| Cross-coupling | 通道耦合 | - | coupling effect (too vague) |
| Ringing zero | 振盪零點 | - | unstable zero (not always precise here) |
| Disturbance Observer | 擾動觀測器 | DOB | disturbance estimator (unless estimator is explicitly defined) |
| Bandwidth | 頻寬 | BW | speed (as metric replacement) |

Writing rules:
1. First mention: `English term（中文）`.
2. Later mentions: English as primary, Chinese only when clarification is needed.
3. Avoid unquantified strong claims such as "significant" or "optimal" unless metrics are provided.

## 9. Next Step

1. Finalize Ch.1 section-by-section using this master brief.
2. Only after Ch.1 claims are locked, derive Abstract by compression.
3. Do not introduce new claims in Abstract.

---

Archived detailed planning files are kept in:
`/.claude/thesis_map/archived/`
