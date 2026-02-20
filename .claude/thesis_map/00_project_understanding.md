# Thesis Foundation: Current Understanding

## 1. 你的研究定位（控制觀點）

本論文以 **Hall-sensor-based 六極電磁致動器** 為核心平台，主軸不是單純展示最終效能，而是用「控制設計鏈」的方式，建立可驗證、可比較、可實作的工程方法：

`System Identification -> Flux Control -> Force Generation`

目標是支撐後續 `Ultra-Precise High-Speed Untethered Manipulation in Aqueous Solutions`，其中「力生成精度與穩定性」是必要基礎。

## 2. 前人工作基線（你承接前的已完成進度）

## A. 團隊論文主線

1. 2011 (`zhang2011design`): 建立 hexapole 設計與 current-based 力模型。
2. 2021 (`long2021optimal`): 最佳電流分配，處理 over-actuated 逆問題。
3. 2022 (`long2022hallsensor`): Hall-sensor-based force model，提升力模型準確性，建立 flux-based 路線。
4. 2023 (`meng2023ultraprecise`): 三層控制架構成熟化，inner-loop flux control + high-speed manipulation。
5. 2024 (`meng2024piconewton`): 精確離散模型與 >4 kHz flux control，進入 piconewton interaction force control。

## B. Dissertations

1. `Fei Long_dissertation.pdf`: 3D motion control、inverse modeling、hysteresis 問題與 Hall-sensor 路線奠基。
2. `Control_of_Hexapole_Electromag.pdf` (Ta-Min Meng dissertation): 高頻寬 flux control、掃描模式、interaction force control 的系統整合。

上述代表：你接手前，「可行性」已被驗證；你的論文空間在於「分層可比較、可量化、可重現」。

## 3. 你目前開發鏈路（repo 層級）

## A. System Identification / Data Pipeline

- `Openloop_Cali`
  - 2026-02: 建立 v3.0 pipeline（read/steady/FFT/fit/compare），加入 dual-channel、pair experiments、super-period FFT、品質檢核。
  - 角色：把 ID 從單次分析變成可批量驗證的方法。

- `PT3D_SW`
  - 2026-02: 新增 Freq Sweep、自動重試、資料腐敗偵測、USB 診斷。
  - 角色：把硬體量測資料鏈路穩定化，確保 ID 資料可信。

## B. Flux Control / Controller Design

- `r_controller_package`
  - 2026-02: 模型更新、VD LPF 測試、FFT 分析工具、測試腳本重構。
  - 角色：提供 PI 與 model-based/R-controller 的可比較模擬框架。

- `PT3D_HW2_imc2c16`
  - 2026-01: 100kHz 同步驗證、InvModel 與 controller timing、R-controller 細節修正（`delta_v_hat` 等）。
  - 角色：把設計落到 FPGA 實作，驗證實時性與同步性。

## C. Motion/Physics Extension

- `MotionControl_Simu`, `MotionControl_KalmanFilter_Simu`
  - 2025-12: 熱噪音、deterministic/random 分離、Kalman 估測與對照。
  - 角色：補強外迴圈與物理噪音分析，可作為後續章節支撐，不一定是本文主軸。

## D. Thesis Integration

- `NTHU_template`
  - 2026-02-20: 已有 Ch.1 + Abstract 改寫版（layer-by-layer 敘事）。
  - 角色：目前已可作為「論文主張框架」草稿。

## 4. 你的可主張貢獻（目前理解版）

1. **分層控制方法論貢獻**：將 ID -> Flux Ctrl -> Force Generation 建成可重現、可比較的工程流程（不只結果展示）。
2. **細緻量化比較貢獻**：在每層提供可驗證對照（PI vs model-based、不同排程法、不同擬合策略），明確對應「各方法解決哪個物理問題」。
3. **Sim-to-HW chain 貢獻**：從資料、模型、控制律到 FPGA/實驗的閉環一致性驗證。

## 5. 目前最關鍵寫作策略

1. 不把「簡化/自動化」當主賣點，而是當「分析結果自然導出的工程效益」。
2. 每個主張都要有指標：bandwidth、tracking error、THD、cross-coupling、repeatability、模型殘差。
3. Ch.1 與 Abstract 的每句貢獻都應可追到至少一個章節圖表與一組實驗/模擬證據。
