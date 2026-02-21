# Ch1 1.1 Logic and Notation Audit (Targeted Paragraphs)

## A) Sentence-style difference (what you asked in Q1)

### Example on the same claim
- Theory-oriented:
  - "A layered control chain is required to establish causal traceability from model uncertainty to force-output error."
- Engineering-verification-oriented:
  - "A layered control chain is required so each design choice can be verified by measurable outcomes from identification, flux tracking, and force output."

### Example on controller paragraph
- Theory-oriented:
  - "Component-level decomposition is necessary to separate internal-loop mechanisms for stability and robustness."
- Engineering-verification-oriented:
  - "Component-level decomposition is necessary so each controller block can be tied to measured changes in bandwidth, tracking error, and disturbance rejection."

## B) Logic check against prior dissertations (paragraph-by-paragraph)

## Paragraph 1 (baseline evolution and achieved performance)
- Your paragraph logic: baseline exists -> model evolved -> controller evolved -> performance achieved -> but design logic still under-decomposed.
- Prior support:
  - Tool comparison and magnetic-actuation motivation: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Zhipeng Zhang_1_1_curated.txt:54`, `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Zhipeng Zhang_1_1_curated.txt:135`
  - Force-modeling importance and hysteresis challenge: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Fei Long_dissertation_1_1_curated.txt:101`, `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Fei Long_dissertation_1_1_curated.txt:186`
  - Current-based control limitation under hysteresis/dynamics: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Control_of_Hexapole_Electromag_1_1_curated.txt:117`, `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Control_of_Hexapole_Electromag_1_1_curated.txt:128`
- Judgment: logically consistent with prior dissertations and your current thesis context.

## Paragraph 2 (system identification gap)
- Your paragraph logic: 6 x 6 MIMO model exists -> methodology not fully systematized -> downstream traceability gap.
- Prior support:
  - Over-actuated 6-input/3-output context and coupling emphasis: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Control_of_Hexapole_Electromag_1_1_curated.txt:101`
  - Your current chapter-specific ID framing (newer stage): `/Users/kevin/Code/worktrees/ch1-worktree/01_introduction.tex:29`
- Judgment: logically valid; this is mostly a newer-generation gap statement extending beyond earlier dissertations.

## Paragraph 3 (flux-control gap, including ringing zero)
- Your paragraph logic: PI/model-based both effective -> end-to-end comparisons insufficient -> component-level quantification needed.
- Prior support:
  - Need for feedback under instability and hysteresis/coupling: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Fei Long_dissertation_1_1_curated.txt:58`, `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Fei Long_dissertation_1_1_curated.txt:186`
  - Current-based closed-loop limitation due to hysteresis/dynamics: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Control_of_Hexapole_Electromag_1_1_curated.txt:121`, `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Control_of_Hexapole_Electromag_1_1_curated.txt:132`
  - PI/model-based/ringing-zero progression from your current thesis corpus: `/Users/kevin/Code/worktrees/ch1-worktree/01_introduction.tex:33`
- Judgment: logically strong, and "ringing zero" should stay in 1.1 as you requested.

## Paragraph 4 (force-generation gap)
- Your paragraph logic: inverse allocation established -> scheduling/nonlinear propagation/full-chain bandwidth bottlenecks still under-quantified.
- Prior support:
  - Inverse modeling and allocation necessity in over-actuated systems: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Fei Long_dissertation_1_1_curated.txt:149`, `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Fei Long_dissertation_1_1_curated.txt:254`
  - Optimal current allocation framing: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Control_of_Hexapole_Electromag_1_1_curated.txt:105`
  - Force-generation scheduling/THD/bottleneck framing in your current draft: `/Users/kevin/Code/worktrees/ch1-worktree/01_introduction.tex:59`
- Judgment: logically consistent and well positioned as a chapter-driving gap.

## Paragraph 5 (closing objective)
- Your paragraph logic: summarize three-layer gaps -> define evidence-driven objective.
- Prior support:
  - 1.1-to-1.2 bridge pattern in prior dissertations: `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Fei Long_dissertation_1_1_curated.txt:202`
- Judgment: structure is correct and aligned with dissertation conventions.

## C) Notation alignment (standardized set used now)

- Control input: `\mathbf{u} \in \mathbb{R}^6`
- Measured Hall-voltage vector: `\mathbf{v}_m \in \mathbb{R}^6`
- Desired flux reference (Hall-voltage form): `\mathbf{v}_d \in \mathbb{R}^6`
- Desired Cartesian force: `\mathbf{f}_d \in \mathbb{R}^3`
- Flux-based force model: `\mathbf{F}(\mathbf{p},\boldsymbol{\Phi}) = g_\Phi \boldsymbol{\Phi}^{T}\mathbf{L}(\hat{\mathbf{p}})\boldsymbol{\Phi}`
- Identification model class: second-order `6 \times 6` MIMO discrete model
- Coupling matrix: `\mathbf{B}`
- Key non-minimum-phase artifact wording: `ringing zero`
- Control-family wording: `PI` and `model-based`
- Layer names: `System Identification`, `Flux Control`, `Force Generation`

## D) Files updated to enforce alignment

- Main 1.1 EN source:
  - `/Users/kevin/Code/worktrees/ch1-worktree/NTHU_Thesis_template_in_English_with_Chines_title_pages_compiled_with_pdfLaTeX_2025/contents/chapter01.tex`
- EN+ZH review copy:
  - `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/CH1_1_1_FULL_DRAFT_EN_ZH.md`
