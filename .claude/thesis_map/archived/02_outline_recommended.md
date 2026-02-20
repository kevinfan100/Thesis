# Recommended Thesis Outline (Control-Centric)

## Design principle

以「研究問題（RQ）-> 方法 -> 對照 -> 量化證據」作為每章結構，不以「工具流程」作敘事主軸。

## Proposed chapter logic

1. **Ch.1 緒論**  
   目標：定義問題、前人基線、研究缺口、你的可驗證貢獻。

2. **Ch.2 系統建模**  
   目標：建立後續控制分析所需的最小模型集合（force model、measurement model、discrete dynamics）。

3. **Ch.3 系統鑑別（ID）**  
   目標：回答 `RQ1: 如何得到可用於控制設計的 6x6 模型，且品質可量化？`  
   內容：資料流程、穩態偵測、FFT/fitting、跨配置比較、誤差來源。  
   產出：模型可信度與適用範圍。

4. **Ch.4 內迴圈磁通控制**  
   目標：回答 `RQ2: PI 與 model-based/R-controller 各自解決哪些物理問題？`  
   內容：組件分解（DOB/FB/FF）、PI baseline 比較、參數敏感度。  
   產出：控制器設計規則與層級化比較結論。

5. **Ch.5 力生成控制**  
   目標：回答 `RQ3: Force generation 的誤差如何形成，如何在排程與控制層降低？`  
   內容：allocation + inverse model + Vd scheduling，非線性與諧波傳遞分析。  
   產出：力精度瓶頸圖與可操作的設計建議。

6. **Ch.6 FPGA 實作與實驗驗證**  
   目標：回答 `RQ4: simulation 與硬體結果是否一致？`  
   內容：時序、同步、資源、實驗流程、結果對照。  
   產出：sim-to-hw consistency 證據。

7. **Ch.7 運動控制模擬（可作延伸）**  
   目標：說明外迴圈與噪音/壁效應對系統上限的影響（若非主打可精簡）。

8. **Ch.8 結論與展望**  
   目標：總結「可驗證貢獻」與可外推邊界。

## Recommended RQs for Ch.1

1. RQ1: 如何建立可支持 6x6 控制設計的 Hall-sensor-based 動態模型，並量化其可靠度？
2. RQ2: 在相同硬體限制下，PI 與 model-based 控制在 inner-loop 的差異與成因為何？
3. RQ3: 力生成誤差如何由 Vd 排程與系統非線性傳遞而來，應如何設計？
4. RQ4: 從 ID 到 FPGA 實驗的整體鏈路是否可重現且一致？

## Suggested core figures/tables (minimum set)

1. 系統架構圖（三層 + 訊號流）。
2. 前人演進表（2011->2024）。
3. ID pipeline 流程圖 + 多配置比較圖。
4. PI vs model-based Bode 對照（含至少一組組件級拆解）。
5. Force generation 排程法比較圖（time/frequency domains）。
6. Sim vs FPGA 實驗對照圖。
7. 最終貢獻總表（每點對應章節與證據）。

## Writing tone constraints (per your requirement)

1. 不把「簡化/自動化」當主論述。
2. 先寫「問題與證據」，最後再總結其工程效益（例如可重現、可移植）。
3. 所有結論盡量量化，不用形容詞主導。
