# Prior Work vs Your Contribution Matrix (Draft v1)

## Scope

主軸限定於 Hall-sensor-based 路線，並以控制鏈三層架構為主：

`System Identification -> Flux Control -> Force Generation`

## Matrix

| Layer | Prior baseline | Prior limitation (writing gap) | Your contribution (draft) | Current evidence source | Suggested metrics |
|---|---|---|---|---|---|
| System ID | 6x6 MIMO model 已用於控制設計（Meng 2023/2024） | 方法論描述不足；擬合策略影響未系統化；跨配置一致性不足 | 建立可批量、可重現的 ID pipeline，提供多配置比較與品質檢核 | `Openloop_Cali`, `PT3D_SW` freq sweep logs, raw bode csv | fit RMSE, phase residual, repeatability, data quality pass rate |
| Flux Control | PI/SISO, 再到 model-based inner loop，最終 >4kHz（Meng 2024） | 組件級貢獻未獨立量化；PI vs model-based 多停留最終結果比較 | 以「物理問題對應控制組件」做分層比較，補充 PI vs model-based 在不同條件下的差異 | `r_controller_package`, `PT3D_HW2_imc2c16`, experiment bode data | bandwidth, gain/phase margin, THD, cross-coupling suppression, settling time |
| Force Generation | optimal allocation + inverse model 已可用於高精度控制 | Vd 排程方式與非線性誤差傳遞機制缺少系統比較 | 對 ZOH/linear/S-curve（或你最終採用方案）做誤差與頻寬比較，明確識別瓶頸 | `r_controller_package` test scripts + FPGA logs | force amplitude error, harmonic distortion, axis decoupling error, effective bandwidth |
| End-to-end chain | 先前文獻各層都有效，但多由論文個別呈現 | 缺「同一套流程」從 data->model->ctrl->HW 的一致性展示 | 建立可追溯鏈路，對齊 simulation 與 FPGA/實驗結果 | all repos + thesis artifacts | sim-exp gap, reproducibility over runs, parameter portability |

## Writing rule for each contribution statement

每個貢獻句需要同時滿足三項：

1. 說明解決的物理或控制問題（不是只說做了流程）。
2. 說明比較對象（baseline 是什麼）。
3. 說明量化結果與指標。

## Example claim style (recommended)

1. 「在相同硬體與取樣率下，模型基控制在 XX 指標相較 PI 改善 YY%，其改善主要來自對 ZZ 問題的補償。」
2. 「ID pipeline 在 N 組配置下維持模型殘差於 XX 以內，支持後續控制器參數移植。」
3. 「Vd 排程法在高頻段引入的 THD 差異可解釋 force output 誤差，且與實驗趨勢一致。」

## Gaps to fill before finalizing Ch.1 claims

- 尚需你確認的內容：
  - 最終要用的 3 個主指標（建議從 bandwidth / force error / THD 選）。
  - PI vs model-based 對照資料哪一組作主圖、哪一組作附錄。
  - Force generation 的「可穩定重現結果」數值範圍。

這份矩陣會直接回填到 Ch.1 貢獻段與 Abstract 四點聲明。
