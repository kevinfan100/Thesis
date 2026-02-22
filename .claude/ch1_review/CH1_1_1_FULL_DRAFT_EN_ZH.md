# Ch.1 Section 1.1 Full Draft (Recommended, EN-first)

## EN Version

### 1.1 Background and Motivation

Accurate force generation and measurement at pico- to nano-Newton levels are fundamental to mechanobiology, intracellular probing, and micro-scale interaction studies in aqueous solution. From an engineering perspective, this requirement is not satisfied by force precision alone. A practical platform must simultaneously achieve high closed-loop bandwidth, robust disturbance rejection, and repeatable three-axis force controllability under fluidic disturbances.

Atomic force microscopy (AFM), optical tweezers, and magnetic tweezers each provide important capabilities, but each also has practical limitations for ultra-precise high-speed untethered operation in fluid. AFM provides strong force sensing for contact-based probing but is limited in untethered maneuverability. Optical tweezers provide high spatial resolution but may introduce photothermal effects and non-specific trapping. Magnetic actuation provides remote, non-contact, and probe-specific force generation, making it suitable for applications that require both force authority and operational safety in aqueous environments.

This dissertation focuses on a Hall-sensor-based hexapole electromagnetic actuator with six independently driven poles and six Hall sensors for real-time magnetic-flux measurement. The system is over-actuated for three-dimensional force output and is implemented as a layered control chain: System Identification -> Flux Control -> Force Generation. In implementation terms, this chain also defines the verification path from model quality to flux-tracking quality and finally to force-output quality.

Prior studies established a two-stage technical baseline. In the current-based stage, Optimal Current Allocation was developed for effective 3-D force generation. In the Hall-sensor-based stage, force modeling and inverse modeling advanced to flux-based formulations, and Optimal Flux Allocation was established for real-time force generation using Hall-voltage measurements. Closed-loop flux control further advanced from independent PI loops to model-based architectures with feedforward, feedback, and disturbance-compensation elements. Reported performance includes kilohertz-level flux-control bandwidth (from hundreds of hertz to beyond 4 kHz), high-speed untethered probe scanning in aqueous solution, and pico-Newton-level probe-sample interaction-force regulation. The available evidence supports system-level feasibility. However, the narrative is still dominated by end-performance demonstration, and the component-level attribution of why that performance is achieved remains incomplete.

The key research gap is therefore not whether high performance can be achieved, but how that performance is established and attributed toward explicit design objectives. Prior studies have already demonstrated important links among observed physical phenomena, model construction, and control outcomes, together with convincing end-performance results. However, these links are still presented primarily through final outcomes, while the objective-level decision path remains less explicit. The mapping from specific physical observations to modeling choices, from modeling choices to controller components, and from controller components to quantitative performance changes is not yet systematically decomposed into a goal-oriented chain. Without this decomposition, design tradeoffs are difficult to explain, design decisions are harder to reproduce, and performance changes under different operating conditions are harder to diagnose.

This dissertation starts the attribution chain from system identification, because open-loop calibration directly captures actuator behaviors that later dominate closed-loop performance. At the tested operating point, single-pole frequency-scan experiments reveal multipole coupling, remanence-related bias and hysteresis, and frequency-dependent nonlinear behavior in both magnitude ratio and phase lag. By extracting dominant-frequency response data and recasting them into a control-oriented model form, the identification stage produces design-relevant information rather than only fitting statistics.

Under this motivation, identification is treated as the entry point of a layer-linked design logic. Its output informs flux-control structure selection and disturbance-handling priorities, and these choices then constrain force-generation quality and bandwidth. Chapter 1 therefore emphasizes traceable reasoning from observation to design and then to measurable outcome, with the goal of making design intent explicit, testable, and reusable. Section 1.2 formalizes the research objectives, scope, and contribution boundaries under this reasoning.

## ZH Version (Aligned Translation)

### 1.1 研究背景與動機

在水溶液中進行機械生物學、細胞內探測與微尺度交互作用研究時，皮牛頓至奈牛頓等級的力量生成與量測精度是核心需求。從工程驗證角度來看，僅有力量精度仍不足以支撐實際應用；可實用的平台必須同時達成高閉迴圈頻寬、良好擾動抑制能力，以及在流體擾動下可重現的三軸力量可控性。

原子力顯微鏡（AFM）、光學鉗夾與磁性鉗夾各自具備重要能力，但在水溶液中追求超精密高速無繫繩操控時，仍各有實務限制。AFM 在接觸式探測上能力突出，但無繫繩機動性受限；光學鉗夾具高空間解析度，但可能引入光熱效應與非特異性捕捉。磁致動可提供遠端、非接觸且對磁性探針具特異性的力量生成，更適合兼顧力量能力與操作安全性的水溶液操控任務。

本論文聚焦於霍爾感測式六極電磁致動器，其由六個可獨立驅動的磁極與六個霍爾感測器構成，用於即時量測磁通。系統在三維力量輸出上屬過驅動架構，並以分層控制鏈運作：System Identification -> Flux Control -> Force Generation。就實作而言，此鏈結同時也是驗證路徑，從模型品質一路對應到磁通追蹤品質與最終力量輸出品質。

前人研究已建立兩階段技術基線。在電流基階段，Optimal Current Allocation 已被提出以有效達成三維力生成；在霍爾感測階段，力模型與逆模型轉向磁通基表述，並建立了 Optimal Flux Allocation 以霍爾量測進行即時力生成。磁通閉迴圈也由獨立 PI 控制進展到包含前饋、回授與擾動補償的模型基架構。既有成果已展示 kHz 級磁通控制頻寬（由數百 Hz 提升到超過 4 kHz）、水溶液中的高速無繫繩掃描，以及 pN 等級探針互動力調控。現有證據支持系統層級可行性；但目前敘事仍偏重最終效能展示，尚缺「哪些組件造成哪些效能」的可歸因拆解。

因此，本研究的核心缺口不在於「能否達成高效能」，而在於「效能如何圍繞明確設計目標被建立並可被歸因」。前人研究其實已經展示了可觀測物理現象、模型建構與控制結果之間的重要連結，也已得到具說服力的最終效能結果；但這些連結仍多以最終成果呈現，目標層級的決策路徑仍不夠明確。從特定物理觀測到模型選擇、從模型選擇到控制器組件、再從控制器組件到量化效能變化的對應關係，尚未被系統化拆解成目標導向鏈。缺少這種拆解，就難以清楚說明設計取捨、重現決策邏輯，或在操作條件改變時診斷效能變化原因。

本論文以系統鑑別作為歸因鏈的起點，因為 open-loop calibration 可直接擷取後續閉迴路效能所受主導的致動器行為。在測試工作點下，單極頻率掃描可觀測到多極耦合、殘磁偏置與磁滯，以及體現在幅值比與相位延遲中的頻率相依非線性。透過萃取主頻響應資料並轉換為控制導向模型表徵，鑑別階段輸出的是設計可用資訊，而不只是擬合統計值。

在此動機下，鑑別被定位為分層設計邏輯的入口。其輸出會影響磁通控制的結構選擇與擾動處理重點，而這些選擇又進一步限制力生成的品質與頻寬。因此，Chapter 1 的主軸是從觀測到設計、再到可量測結果的可追溯推理，目的是讓設計意圖可明確、可驗證、可重用；正式的研究目標、範圍與貢獻邊界將在 Section 1.2 定義。
