# Ch.1 Section 1.1 Rebuild Review Pack (EN-first)

## 0) Entry Points
- Main Chinese thesis draft: `/Users/kevin/Code/worktrees/ch1-worktree/01_introduction.tex`
- English template chapter draft: `/Users/kevin/Code/worktrees/ch1-worktree/NTHU_Thesis_template_in_English_with_Chines_title_pages_compiled_with_pdfLaTeX_2025/contents/chapter01.tex`
- English template PDF: `/Users/kevin/Code/worktrees/ch1-worktree/NTHU_Thesis_template_in_English_with_Chines_title_pages_compiled_with_pdfLaTeX_2025/main.pdf`

## 1) Baseline References Used for 1.1
- `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Zhipeng Zhang_1_1_curated.txt`
- `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Fei Long_dissertation_1_1_curated.txt`
- `/Users/kevin/Code/worktrees/ch1-worktree/.claude/ch1_review/references/Control_of_Hexapole_Electromag_1_1_curated.txt`

## 2) Synthesis Strategy (Most Suitable Blend for Your Topic)
- Keep the broad motivation framing strength from Zhipeng Zhang 1.1.
- Keep the instrument-comparison clarity and Hall-sensor transition logic from Fei Long 1.1.
- Keep the control-oriented gap statement style from Control of Hexapole 1.1.
- Rebuild around your dissertation backbone: `System Identification -> Flux Control -> Force Generation`.
- Avoid naming any specific lab/team in 1.1 narrative.

## 3) Segment-by-Segment Review Template (for live discussion)

### Segment 1: Why this problem matters in aqueous manipulation
Problem to fix:
Current text is rich in technical details early, but the opening claim can be more direct about why force precision and high speed must be co-optimized.

Rewrite suggestion (EN):
Accurate force generation and measurement at pico- to nano-Newton levels are fundamental to mechanobiology and micro-scale interaction studies in aqueous solution. A practical platform must jointly satisfy precision, speed, and controllability; improving only one dimension is insufficient for reliable untethered operation.

改寫建議（ZH）:
在水溶液中進行微尺度交互作用研究時，皮牛頓至奈牛頓等級的力量生成與量測精度是核心需求。可實用的平台必須同時滿足精度、速度與可控性，僅提升單一指標不足以支撐可靠的無繫繩操控。

Why this change:
This opening establishes a clear thesis-level necessity statement before tool details.

Your decisions (1-2):
1. Keep explicit force range (`pN-nN`) in first sentence, or move to second sentence?
2. Keep “untethered operation” in opening, or introduce it after instrument comparison?

### Segment 2: Why magnetic actuation, and why Hall-sensor-based architecture
Problem to fix:
The comparison of AFM/optical/magnetic tools is present but can be tightened to directly support your Hall-sensor control perspective.

Rewrite suggestion (EN):
AFM and optical tweezers provide important capabilities, but each faces constraints in contact condition, specificity, or thermal side effects for high-speed aqueous operation. Magnetic actuation offers remote, non-contact, and probe-specific manipulation. The Hall-sensor-based hexapole platform further enables direct magnetic flux measurement, making closed-loop flux regulation feasible for reducing hysteresis-driven uncertainty.

改寫建議（ZH）:
AFM 與光學鉗夾各有關鍵能力，但在高速水溶液操作中，仍面臨接觸條件、特異性或熱效應等限制。磁致動提供遠端、非接觸且對磁性探針具特異性的操控能力。進一步地，霍爾感測式六極平台可直接量測磁通，使閉迴圈磁通調控得以降低磁滯造成的不確定性。

Why this change:
This paragraph creates a direct bridge from tool comparison to your core control architecture.

Your decisions (1-2):
1. Should we name “hexapole electromagnetic actuator” in this paragraph or in the next paragraph?
2. Do you want “hysteresis” stated here, or deferred to the gap paragraph?

### Segment 3: Prior baseline and the three-layer control chain
Problem to fix:
Current text contains many achievements but the chain `ID -> Flux -> Force` can be made more explicit as the thesis backbone.

Rewrite suggestion (EN):
Prior studies established key milestones, including current-based and flux-based force modeling, high-bandwidth flux feedback, and high-speed untethered manipulation in aqueous solution. However, these achievements are best understood through a layered chain: system identification defines the dynamic model, flux control determines magnetic-state tracking quality, and force generation maps flux commands into Cartesian force output.

改寫建議（ZH）:
前人研究已建立關鍵里程碑，包括電流基與磁通基力模型、高頻寬磁通回授，以及水溶液中的高速無繫繩操控。然而，這些成果需透過分層鏈結來理解：系統鑑別決定動態模型品質，磁通控制決定磁狀態追蹤品質，而力生成層將磁通命令映射為三維力量輸出。

Why this change:
This explicitly states the analytical ordering that your thesis will follow.

Your decisions (1-2):
1. Keep this as one paragraph or split into “baseline” and “layered chain” two paragraphs?
2. Should we already mention sample rates (100 kHz, 10 kHz, 1.6 kHz) here?

### Segment 4: Gap statement for system identification
Problem to fix:
Identification is described, but the methodological gap is not yet framed as a reproducibility problem.

Rewrite suggestion (EN):
At the identification layer, a 6x6 MIMO model has been used effectively, yet the methodology is not fully standardized in fitting strategy, weighting-function selection, and cross-configuration consistency checks. Consequently, the causal link between model quality and downstream controller behavior remains insufficiently traceable.

改寫建議（ZH）:
在鑑別層，6x6 MIMO 模型已被有效使用，但其方法論在擬合策略、加權函數選擇與跨實驗配置一致性檢查方面仍未完全標準化。因此，模型品質與下游控制器行為之間的因果鏈結仍缺乏足夠可追溯性。

Why this change:
It reframes “more details needed” into a concrete scientific gap: traceability and reproducibility.

Your decisions (1-2):
1. Use “standardized” or “systematized” as the key term?
2. Mention “super-period FFT” directly here, or keep it for Chapter 3?

### Segment 5: Gap statement for flux control
Problem to fix:
Current text lists controller blocks, but the claim-evidence logic can be sharper at component level.

Rewrite suggestion (EN):
At the flux-control layer, PI and model-based controllers have demonstrated different final performances, but most comparisons are end-to-end only. A component-level analysis is still needed to quantify how each element addresses specific physical issues, including hysteresis compensation, dynamic coupling suppression, ringing-zero handling, and bandwidth shaping.

改寫建議（ZH）:
在磁通控制層，PI 與模型基控制器已展現不同整體效能，但多數比較仍停留在端到端結果。仍需組件層級分析，以量化各元件如何對應特定物理問題，包括磁滯補償、動態耦合抑制、ringing-zero 處理與頻寬塑形。

Why this change:
It converts “controller description” into testable research questions and measurable comparison axes.

Your decisions (1-2):
1. Do we keep “ringing-zero” in 1.1 or only in Chapter 4?
2. Should “PI vs model-based” appear as a sentence-level contrast or as a later table?

### Segment 6: Gap statement for force generation and closing bridge to 1.2
Problem to fix:
The force-generation gap appears, but the end of 1.1 should close with a strong bridge sentence to objectives.

Rewrite suggestion (EN):
At the force-generation layer, prior work established inverse mapping and allocation feasibility, yet the quantitative impact of reference scheduling and harmonic distortion propagation through the nonlinear force model remains underexplored. Therefore, this dissertation adopts a control-oriented framework that analyzes and validates the full path from identification to force output, providing a verifiable basis for ultra-precise high-speed untethered manipulation in aqueous solution.

改寫建議（ZH）:
在力生成層，前人已建立逆映射與分配可行性，但參考訊號排程與諧波畸變經非線性力模型傳遞後的量化影響仍缺乏系統分析。因此，本論文採取控制導向框架，分析並驗證從鑑別到力量輸出的完整路徑，為水溶液中的超精密高速無繫繩操控建立可驗證基礎。

Why this change:
This ending gives a clean transition from motivation/gap to objective/scope in Section 1.2.

Your decisions (1-2):
1. Keep “verifiable basis” or strengthen to “quantitatively verifiable basis”?
2. Mention “ease of use” in 1.1 closing sentence, or reserve it for contribution discussion?

## 4) How to run the live review
- We review one segment per round, in order: Segment 1 -> Segment 6.
- For each round, only finalize:
  - one approved EN paragraph,
  - one approved ZH paragraph,
  - one terminology decision if needed.
- After Segment 6 is approved, we integrate into `/Users/kevin/Code/worktrees/ch1-worktree/01_introduction.tex`.
