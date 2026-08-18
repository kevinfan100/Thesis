# Ch 1.1 研究背景與動機（V2）

> **版本定位**：依既有 Phase 1--4 脈絡重整之 V2 架構稿  
> **用途**：後續轉為 LaTeX 寫入 `chapter01.tex` 的 `\section{Background and Motivation}`  
> **語言策略**：繁體中文敘事 + 技術術語保留英文  
> **本版目標**：加強 literature review 比重，維持長篇背景，但將收束邏輯明確導向 1.2

---

在水溶液環境中進行微尺度操控時，研究需求往往不是單一指標最佳化，而是同時要求多項能力並存：包括 pico-Newton (pN) 至 nano-Newton (nN) 等級的力施加與量測、足夠高的閉迴路動態響應、三維空間中的穩定操控、以及跨實驗條件的可重現性。若只滿足「可施力」，但無法在速度、穩定性與重現性上維持一致，則很難支撐後續高精度掃描與系統化驗證。因此，本研究背景的核心不只是「能不能做」，而是「如何建立一條可持續擴展的控制開發路徑」。

從 literature review 來看，常見微尺度操控平台各有明確優勢與限制。Atomic force microscopy (AFM) 具備高解析力學量測能力，但受限於接觸式操作與掃描幾何條件；optical tweezers 在單粒子操控方面成熟，但受光學路徑、光熱效應與力輸出範圍限制，面對特定生物樣本時存在可操作邊界 \cite{gosse2002magnetic,devlaminck2012magnetic}。相較之下，magnetic tweezers 以非接觸梯度力作用於磁性標的，對液相環境與長時間操作更具彈性，因此成為三維微操控系統的重要發展方向。

在 magnetic manipulation 文獻中，hexapole electromagnetic actuator 的關鍵價值在於：以六通道致動對應三維力目標，提供 over-actuated 架構所需的自由度，讓「力生成」、「耦合管理」與「控制器設計」可在同一平台上被系統性處理。先前研究已建立 magnetic-force modeling、inverse allocation 與實驗平台整合能力 \cite{zhang2011design,long2021optimal,long2022hallsensor,meng2023ultraprecise,meng2024piconewton}。然而，既有成果多以性能驗證為主軸，方法論層面的可移植性與標準化開發流程仍有明顯擴展空間。

就技術演進而言，Phase 1（2009--2011）完成了從 quadrupole 概念到 hexapole 架構的基礎建立。早期研究以 lumped-parameter magnetic charge model 與 current-based 力模型為核心，成功證明三維力操控可行性 \cite{zhang2010quadrupole,zhang2011design}。此階段的重要貢獻是建立了可計算、可實作的第一代模型鏈條；但同時也暴露限制：在 six-input / three-output 的 over-actuated 條件下，若冗餘自由度處理方式過於固定，會壓縮可用力包絡並降低能量使用效率。此外，current-based 假設對 ferromagnetic hysteresis 的處理能力有限，為後續精度提升留下關鍵瓶頸。

Phase 2（2013--2016）則聚焦在系統成熟化與平台整合。相關研究把 3-D vision-based tracking 與閉迴路操作串接進既有平台，並透過硬體升級提升力輸出能力 \cite{zhang2013visual,long2016actively,long2016dissertation}。然而，硬體能力提升後，材料與磁路中的 remanence / hysteresis 問題變得更不可忽視：相同電流命令不再對應到一致磁通，導致跨操作歷史的偏移與誤差型態差異。這一階段說明了關鍵事實：提升硬體規格本身無法自動保證控制一致性，量測與控制架構必須同步升級。

Phase 3（2021--2022）出現兩個決定性轉折。第一，optimal current allocation 將 over-actuated 冗餘自由度由固定常數轉為可依任務方向調整，改善了力包絡與效率 \cite{long2021optimal}。第二，更關鍵的是 Hall sensor 整合後，系統由 current-based 轉向 flux-based：在控制鏈條中，不再僅依賴電流推估磁通，而是直接量測可被控制的物理量 \cite{long2022hallsensor}。此轉換實質上改變了控制問題的性質，使磁滯造成的不確定性可在架構層被顯式處理，並為後續高頻寬內迴路建立可驗證的基礎。

Phase 4（2023--2024）進一步把 flux-based 架構推向高精度與高頻寬實作。先前研究在分層控制架構下，整合 feedforward、feedback 與 disturbance compensation，並在 simulation 與 experiment 之間建立一致的驗證鏈 \cite{meng2023ultraprecise,meng2024piconewton,meng2025nearwall}。此階段顯示：當 identification、controller design 與 validation 流程可被一致串接時，性能提升不再只是參數調整結果，而能被解釋為一連串可追溯決策的結果。這也讓「設計取捨是否合理」與「決策邏輯是否可重現」成為比單點性能更重要的研究議題。

綜合上述文獻脈絡，可歸納三點觀察。第一，hexapole 平台的能力是跨多年、跨階段逐步堆疊而成，並非單一方法即可達成。第二，每一階段都在解決前一階段暴露的更深層問題，顯示系統開發本質上是循環式的「驗證--修正--再驗證」流程。第三，現有成果雖已充分證明特定平台的可行與高性能，但對「如何在另一套相容架構平台快速重建同等級能力」的工程方法描述仍不夠系統化。

因此，本論文在 1.1 所提出的動機是：將既有成果所累積的 know-how 轉化為一條可追溯、可重現、可自動化的控制開發鏈。具體而言，本研究不把焦點放在再次展示單點性能，而是強調如何把開發流程拆解為具物理意義與驗證接口的階段，並讓每個階段的輸出可直接成為下一階段輸入。這個動機將在下一節（1.2）進一步具體化為四條技術主線：system identification、magnetic flux control、force generation、motion control，以及其對應的 simulation/experiment 同步驗證方式。

---

## 本版引用 key（待最終 LaTeX 版確認）

- `gosse2002magnetic`
- `devlaminck2012magnetic`
- `zhang2010quadrupole`
- `zhang2011design`
- `zhang2013visual`
- `long2016actively`
- `long2016dissertation`
- `long2021optimal`
- `long2022hallsensor`
- `meng2023ultraprecise`
- `meng2024piconewton`
- `meng2025nearwall`

---

## V2 結構檢查清單

1. 是否已包含 literature review（平台比較 + hexapole 脈絡）  
2. 是否保留 Phase 1--4 遞進但不過度推導  
3. 是否把動機收束成「流程化/自動化/可重現」  
4. 是否避免在 1.1 提前寫成 1.2 的具體方法章  
5. 是否可自然銜接下一節 research objective and scope
