# Ch1 架構與名詞規範（V1，含 Motion Control 主線）

> 目的：先鎖定 Ch1 的故事線與術語，後續再逐段精修 1.1 / 1.2 / 1.3  
> 原則：用詞盡量對齊既有論文慣用語（尤其是 hexapole / magnetic flux / vision-based tracking 系列）

---

## A. Ch1 故事線（含層層遞進）

### 1.1 Background and Motivation（背景與動機）

1. 應用需求：pN/nN 力尺度 + 水溶液 + 高速 + 可重現。  
2. 文獻對照：AFM / optical tweezers / magnetic tweezers 的能力與邊界。  
3. Hexapole 脈絡：先前工作已建立可行平台與高性能控制。  
4. 演進回顧：Phase 1 → Phase 4，強調每階段解決的核心瓶頸。  
5. 關鍵缺口：現有成果偏 platform-specific performance，缺可移植開發方法。  
6. 動機收束：建立可追溯、可重現、可自動化的開發鏈。  
7. 銜接 1.2：四主線（ID → Flux → Force → Motion）。

### 1.2 Research Objective and Scope（目標與範圍）

1. 總目標：建立 generalizable automation framework for control development。  
2. Aim 1：System Identification（輸出 controller-ready model）。  
3. Aim 2：Magnetic Flux Control（輸出高頻寬且可解釋的 inner-loop）。  
4. Aim 3：Force Generation（輸出力品質與解耦分析）。  
5. Aim 4：Motion Control（在既有 force/flux 能力上做應用層閉迴路驗證）。  
6. Scope：聚焦控制與流程；生物機制詮釋不作為核心貢獻。  
7. 驗證原則：每一主線皆以 simulation + experiment 同步驗證。

### 1.3 Dissertation Overview（章節導覽）

1. Ch2：System Overview（平台與介面基礎）。  
2. Ch3：System Identification。  
3. Ch4：Flux Control Design and Validation。  
4. Ch5：Force Generation + Motion Control + Tracing Design Decisions + Conclusions。  
5. 收束句：形成連續證據鏈，而非分散式結果展示。

---

## B. Ch1 建議固定術語（優先用詞）

### 主術語（建議固定）

1. `hexapole electromagnetic actuating system`  
2. `magnetic-flux-based hexapole force model`  
3. `Hall-sensor-based force model`  
4. `measurement of magnetic flux`  
5. `dynamic modeling of magnetic flux generation`  
6. `magnetic flux control`  
7. `system identification`  
8. `force generation`  
9. `3-D vision-based tracking of scanning microprobe`  
10. `3-D visual servo control`  
11. `motion control`  
12. `tracing design decisions from identification to flux, force, and motion control`

### 盡量避免的混用詞（避免同義漂移）

1. `flux ctrl`（改用 `magnetic flux control`）  
2. `sys id`（改用 `system identification`）  
3. `model base ctrl`（改用 `model-based control`）  
4. `tracking system` / `vision system` / `visual system` 混用不分  
   建議：在 Ch1 固定為 `vision-based tracking`（必要時補 `visual servo control`）

---

## C. 關係詞與句型模板（Ch1 建議統一）

### 段落轉折（背景 → 缺口 → 動機）

1. `However, ...`  
2. `Therefore, ...`  
3. `Consequently, ...`  
4. `To address this need, ...`

### 因果與承接（上一層輸出 → 下一層輸入）

1. `Based on the identified model, ...`  
2. `This enables ...`  
3. `This stage provides ... for the next stage.`  
4. `The resulting interface is then used in ...`

### 邊界語氣（避免過度主張）

1. `under tested operating conditions`  
2. `evidence supports`  
3. `consistent with`  
4. `within compatible architecture assumptions`

---

## D. Ch1 命名待你確認（最小決策）

1. 1.2 是否明確寫 `Aim 4: Motion Control`（建議：要，寫清楚）  
2. 1.3 是否在 Ch5 標題內直接寫 `Motion Control`（建議：要，避免主線斷裂）  
3. 2.5 是否維持 `Vision-Based 3-D Probe Tracking`（建議：維持，與既有論文一致）
