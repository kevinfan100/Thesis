# Ch.1 Section 1.1 Full Draft (Recommended, EN-first)

## EN Version

### 1.1 Background and Motivation

Accurate force generation and measurement at pico- to nano-Newton levels are fundamental to mechanobiology, intracellular probing, and micro-scale interaction studies in aqueous solution. From an engineering perspective, this requirement is not satisfied by force precision alone. A practical platform must simultaneously achieve high closed-loop bandwidth, robust disturbance rejection, and repeatable three-axis force controllability under fluidic disturbances.

Atomic force microscopy (AFM), optical tweezers, and magnetic tweezers each provide important capabilities, but each also has practical limitations for ultra-precise high-speed untethered operation in fluid. AFM provides strong force sensing for contact-based probing but is limited in untethered maneuverability. Optical tweezers provide high spatial resolution but may introduce photothermal effects and non-specific trapping. Magnetic actuation provides remote, non-contact, and probe-specific force generation, making it suitable for applications that require both force authority and operational safety in aqueous environments.

This dissertation focuses on a Hall-sensor-based hexapole electromagnetic actuator with six independently driven poles and six Hall sensors for real-time magnetic-flux measurement. The system is over-actuated for three-dimensional force output and is implemented as a layered control chain: System Identification -> Flux Control -> Force Generation. In implementation terms, this chain also defines the verification path from model quality to flux-tracking quality and finally to force-output quality.

Prior studies established a two-stage technical baseline. In the current-based stage, Optimal Current Allocation was developed for effective 3-D force generation. In the Hall-sensor-based stage, force modeling and inverse modeling advanced to flux-based formulations, and Optimal Flux Allocation was established for real-time force generation using Hall-voltage measurements. Closed-loop flux control further advanced from independent PI loops to model-based architectures with feedforward, feedback, and disturbance-compensation elements. Reported performance includes kilohertz-level flux-control bandwidth (from hundreds of hertz to beyond 4 kHz), high-speed untethered probe scanning in aqueous solution, and pico-Newton-level probe-sample interaction-force regulation. The available evidence supports system-level feasibility. However, the narrative is still dominated by end-performance demonstration, and the component-level attribution of why that performance is achieved remains incomplete.

At the system-identification layer, at the tested operating point, a single frequency-scan dataset already reveals three observable phenomena: multipole coupling, hysteresis/bias, and a ZOH-related discrete-time effect associated with a zero close to $-1$. The six-input-six-output plant from control input $\mathbf{u} \in \mathbb{R}^6$ to measured Hall-voltage output $\mathbf{v}_m \in \mathbb{R}^6$ can be represented by a second-order discrete model, e.g., $\mathbf{v}_m[k+1] = a_1\mathbf{v}_m[k] + a_2\mathbf{v}_m[k-1] + \mathbf{B}\{\mathbf{u}[k]+\mathbf{w}[k]\}$. Existing evidence supports that this structure captures static coupling through $\mathbf{B}$ and the zero-close-to-$-1$ effect. The remaining gap is a traceable and quantitative chain from observed phenomena to identified parameters and then to control-design implications. Therefore, this dissertation frames identification as extracting design-relevant model information at the tested operating point, without claiming universal dynamics across operating conditions.

At the flux-control layer, both PI and model-based controllers have demonstrated effective operation, but most comparisons remain end-to-end. A component-level comparison is needed so that each control element is tied to a specific physical issue: coupling represented in $\mathbf{B}$ motivates decoupling design, hysteresis/bias motivates disturbance estimation and compensation, and zero close to $-1$ motivates discrete-time design that avoids ringing-related risk. Under this framing, controllers are compared under matched hardware and sampling conditions, so measured differences in bandwidth and tracking error are attributable to controller structure rather than to setup variation.

At the force-generation layer, inverse allocation from desired actuation force $\mathbf{f}_d \in \mathbb{R}^3$ to allocated voltage (desired flux-reference voltage) $\mathbf{v}_d \in \mathbb{R}^6$ has been established via Optimal Flux Allocation. However, comparative evidence is still limited in three aspects: reference scheduling, harmonic-distortion propagation through the nonlinear quadratic force model $\mathbf{F}(\mathbf{p},\boldsymbol{\Phi}) = g_\Phi \boldsymbol{\Phi}^{T}\mathbf{L}(\hat{\mathbf{p}})\boldsymbol{\Phi}$, and bottleneck decomposition across the full chain from identification to flux tracking and then force output. As a result, the dominant limitation on force-output accuracy and bandwidth is not yet quantitatively attributable.

Accordingly, this dissertation adopts a control-oriented and evidence-driven framework centered on Hall-sensor-based feedback, and is organized by verification questions rather than by a single fixed controller structure. RQ1 asks how coupling, hysteresis/bias, and zero-close-to-$-1$ behavior can be converted into design-relevant model information at the tested operating point. RQ2 asks how individual control components improve corresponding physical issues and measurable flux-control metrics under matched hardware and sampling conditions. RQ3 asks how allocation, reference scheduling, and nonlinear distortion propagation jointly determine force-output quality and bandwidth limits. This RQ-based framing keeps the thesis extensible to PI, model-based, and other implementations while preserving a clear claim-evidence chain.

## ZH Version (Aligned Translation)

### 1.1 研究背景與動機

在水溶液中進行機械生物學、細胞內探測與微尺度交互作用研究時，皮牛頓至奈牛頓等級的力量生成與量測精度是核心需求。從工程驗證角度來看，僅有力量精度仍不足以支撐實際應用；可實用的平台必須同時達成高閉迴圈頻寬、良好擾動抑制能力，以及在流體擾動下可重現的三軸力量可控性。

原子力顯微鏡（AFM）、光學鉗夾與磁性鉗夾各自具備重要能力，但在水溶液中追求超精密高速無繫繩操控時，仍各有實務限制。AFM 在接觸式探測上能力突出，但無繫繩機動性受限；光學鉗夾具高空間解析度，但可能引入光熱效應與非特異性捕捉。磁致動可提供遠端、非接觸且對磁性探針具特異性的力量生成，更適合兼顧力量能力與操作安全性的水溶液操控任務。

本論文聚焦於霍爾感測式六極電磁致動器，其由六個可獨立驅動的磁極與六個霍爾感測器構成，用於即時量測磁通。系統在三維力量輸出上屬過驅動架構，並以分層控制鏈運作：System Identification -> Flux Control -> Force Generation。就實作而言，此鏈結同時也是驗證路徑，從模型品質一路對應到磁通追蹤品質與最終力量輸出品質。

前人研究已建立兩階段技術基線。在電流基階段，Optimal Current Allocation 已被提出以有效達成三維力生成；在霍爾感測階段，力模型與逆模型轉向磁通基表述，並建立了 Optimal Flux Allocation 以霍爾量測進行即時力生成。磁通閉迴圈也由獨立 PI 控制進展到包含前饋、回授與擾動補償的模型基架構。既有成果已展示 kHz 級磁通控制頻寬（由數百 Hz 提升到超過 4 kHz）、水溶液中的高速無繫繩掃描，以及 pN 等級探針互動力調控。現有證據支持系統層級可行性；但目前敘事仍偏重最終效能展示，尚缺「哪些組件造成哪些效能」的可歸因拆解。

在系統鑑別層，在目前測試工作點下，單次頻率掃描資料已可觀測三類現象：多極耦合、磁滯/偏置，以及與 zero close to $-1$ 相關的 ZOH 離散效應。六輸入六輸出受控對象（由控制輸入 $\mathbf{u} \in \mathbb{R}^6$ 到霍爾量測輸出 $\mathbf{v}_m \in \mathbb{R}^6$）可由二階離散模型表示，例如 $\mathbf{v}_m[k+1] = a_1\mathbf{v}_m[k] + a_2\mathbf{v}_m[k-1] + \mathbf{B}\{\mathbf{u}[k]+\mathbf{w}[k]\}$。現有證據支持該模型可捕捉 $\mathbf{B}$ 對應的靜態耦合與 zero close to $-1$ 行為。缺口在於：尚未建立「可觀測現象 $\rightarrow$ 已識別參數 $\rightarrow$ 控制設計意義」的可追溯量化鏈。因此，本論文將鑑別任務界定為在測試工作點萃取設計可用模型資訊，不先宣稱跨條件普適動態。

在磁通控制層，PI 與模型基控制器皆已展現有效運作，但多數比較仍是端到端結果。需要進一步做組件層級比較，讓每個控制元件對應到特定物理問題：$\mathbf{B}$ 反映的耦合對應解耦需求，磁滯/偏置對應擾動估測與補償需求，zero close to $-1$ 對應離散設計中的 ringing 風險處理。在此框架下，控制器需在相同硬體與取樣條件比較，才能把頻寬與追蹤誤差差異歸因於控制器結構，而不是測試設定差異。

在力生成層，從期望作用力 $\mathbf{f}_d \in \mathbb{R}^3$ 到配置電壓（期望磁通參考電壓）$\mathbf{v}_d \in \mathbb{R}^6$ 的逆向分配已可透過 Optimal Flux Allocation 建立。然而，三項關鍵比較證據仍不足：參考訊號排程、諧波畸變經非線性二次型力模型 $\mathbf{F}(\mathbf{p},\boldsymbol{\Phi}) = g_\Phi \boldsymbol{\Phi}^{T}\mathbf{L}(\hat{\mathbf{p}})\boldsymbol{\Phi}$ 的傳遞、以及從鑑別到磁通追蹤再到力輸出的全鏈瓶頸分解。因此，目前仍難以量化歸因最主要的力輸出精度與頻寬限制來源。

基於上述缺口，本論文採取以霍爾感測回饋為核心的控制導向、證據導向框架，並以研究問題而非單一固定控制器作為主軸。RQ1 探討如何把耦合、磁滯/偏置與 zero close to $-1$ 轉化為測試工作點下的設計可用模型資訊。RQ2 探討控制組件如何在相同硬體與取樣條件下，分別改善對應物理問題與磁通控制指標。RQ3 探討 allocation、reference scheduling 與非線性畸變傳遞如何共同決定最終力輸出品質與頻寬限制。此 RQ 架構可同時保留 PI、模型基與其他控制策略的擴展性，且維持清楚的 claim-evidence 鏈。
