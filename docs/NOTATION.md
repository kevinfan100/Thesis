# NOTATION — 符號表（唯一真相）

> 兩個 agent（Claude Code、Codex）撰寫論文時**一律查此表**，不得自創符號。
> 需要新符號時：先在此表登錄，再於 `.tex` 中使用。
> 表中「來源」欄標示該符號的權威出處，修改前請先核對來源。

---

## 1. 座標系統

| 符號 | 意義 | 備註 | 來源 |
|---|---|---|---|
| `{xm, ym, zm}` | Measurement coordinate | z 軸對齊顯微鏡光軸；用於粒子追蹤與運動控制 | hexapole notes |
| `{xa, ya, za}` | Actuation coordinate | 三對磁極分別沿三正交軸排列；用於力建模與磁通分配 | hexapole notes |
| `p` ∈ ℝ³ | 探測珠位置 | 上標區分座標系，如 ᵃp 為 actuation 座標下之位置 | hexapole notes |
| `ᵃp̄ = ᵃp / ℓ` | 無因次化位置 | 以工作空間半徑 ℓ 正規化 | hexapole notes |
| `ℓ` | 工作空間半徑 | 中心到各極尖端距離，可調，標稱值 500 μm | hexapole notes |

## 2. 磁通與電流

| 符號 | 維度 | 意義 | 來源 |
|---|---|---|---|
| `Φ` (`\Phi`) | ℝ⁶ | 六極磁通量向量 `[φ₁ … φ₆]ᵀ` | hexapole notes |
| `I` | ℝ⁶ | 六個線圈輸入電流 `[I₁ … I₆]ᵀ`，上限 3 A | hexapole notes |
| `Î = I / I_max` | ℝ⁶ | 正規化電流向量 | hexapole notes |
| `N_c` | 純量 | 線圈匝數 | hexapole notes |
| `R_a` | 純量 | Lumped magnetic reluctance | hexapole notes |
| `K_I` | ℝ⁶ˣ⁶ | 對稱磁通分布矩陣，描述多極耦合；非對角 | hexapole notes |

## 3. 霍爾感測器

| 符號 | 維度 | 意義 | 來源 |
|---|---|---|---|
| `v_H` | ℝ⁶ | 六個 Hall sensor 電壓讀數 `[v_H1 … v_H6]ᵀ` | ch02.tex:40 |
| `D_H` | ℝ⁶ˣ⁶ | 對角 voltage-to-flux gain matrix，實驗校準取得 | ch02.tex:40 |
| `D̂_H = D_H / ‖D_H‖` | ℝ⁶ˣ⁶ | 正規化 voltage-flux gain matrix | hexapole notes |

核心關係式（`contents/chapter02.tex:38`）：

```
Φ = D_H · v_H
```

## 4. 力模型

| 符號 | 維度 | 意義 | 來源 |
|---|---|---|---|
| `L(ᵃp̄)` | 三個 ℝ⁶ˣ⁶ | Gradient matrix，分量為 `L_x, L_y, L_z` | hexapole notes |
| `g_Φ(ℓ)` | 純量 | Flux-based force gain；正比於探測珠體積與磁化率，反比於 ℓ⁵ | hexapole notes |
| `g_I = (N_c/R_a)² · g_Φ` | 純量 | Current-based force gain | hexapole notes |
| `g_H = ‖D_H‖² · g_Φ` | 純量 | Hall-sensor-based force gain | hexapole notes |
| `F` | ℝ³ | 磁梯度力 | hexapole notes |
| `f_d` | ℝ³ | 期望力（由外迴圈給定） | legacy ch1 |

## 5. 系統鑑別模型

`contents/chapter03.tex:45` 的 6×6 MIMO 模型：

```
H(s) = A₂ / (s² + A₁·s + A₂) · B
```

| 符號 | 維度 | 意義 | 來源 |
|---|---|---|---|
| `H(s)` | ℝ⁶ˣ⁶ | 鑑別所得之磁通生成動態模型 | ch03.tex:45 |
| `B` | ℝ⁶ˣ⁶ | 通道增益／耦合矩陣；保存通道間相對耦合與增益分布 | ch03.tex:47 |
| `B⁻¹` | ℝ⁶ˣ⁶ | 解耦用之耦合矩陣逆 | ch04.tex:13 |
| `A₁, A₂` | 純量 | 共享二階動態係數 | ch03.tex:45 |

## 6. 控制訊號

| 符號 | 維度 | 意義 | 來源 |
|---|---|---|---|
| `v_d` | ℝ⁶ | 期望磁通電壓向量 | legacy ch1 |
| `v_m` | ℝ⁶ | 量測磁通電壓向量 | legacy ch1 |
| `u` | ℝ⁶ | 驅動電壓（控制輸入） | legacy ch1 |
| `v_ff[k]` | ℝ⁶ | 前饋控制量（一步預測實現） | hexapole notes |
| `Δv_fb[k]` | ℝ⁶ | 回饋控制量（基於估測追蹤誤差） | hexapole notes |
| `ŵ[k]` | ℝ⁶ | 擾動估測（補償建模誤差與殘磁） | hexapole notes |

## 7. 控制頻寬參數

`contents/chapter04.tex:29` 以頻寬參數化模型基控制器的三個組件：

| 符號 | 對應組件 | 狀態 |
|---|---|---|
| `f_{B,f}` | Feedforward 相關頻寬 | ⚠️ **待作者確認**下標語意 |
| `f_{B,c}` | Feedback / controller 相關頻寬 | ⚠️ **待作者確認** |
| `f_{B,e}` | Disturbance estimator 相關頻寬 | ⚠️ **待作者確認** |

> 這三個符號目前只在 ch04 出現一次且無定義。上表為依上下文（回饋／前饋／擾動補償三組件）
> 之推測，**尚未由作者或文獻確認**。定案前不要在其他章節使用。

## 8. 系統參數（非符號，但需全文一致）

| 項目 | 值 | 來源 |
|---|---|---|
| 磁極材質 | 1018 鋼，飽和極限 > 2 T | hexapole notes |
| 磁極數 | 6（上下兩層各 3） | legacy ch1 |
| 磁極尖端半徑 | 約 40 μm | legacy ch1 |
| 極間距 (pole gap) | 約 594 μm | legacy ch1 |
| ℓ 標稱值 | 500 μm | hexapole notes |
| 電流上限 | 3 A | hexapole notes |
| Hall sensor | Asahi Kasei EQ-730L ×6 | hexapole notes |
| ADC | TI ADS8365，16-bit，六通道 | hexapole notes |
| 探測珠直徑 | 約 2.8 μm，超順磁性 | legacy ch1 |

> ⚠️ 極間距 594 μm 與 ℓ 標稱值 500 μm 出自不同文件，**兩者關係待作者釐清**
> （594 是否為 pole gap 而 500 為中心到極尖距離？）。

## 9. 控制迴圈取樣率

| 迴圈 | 取樣率 | 職責 | 來源 |
|---|---|---|---|
| 內迴圈 Flux Control | 100 kHz | 追蹤 `v_d`，抑制磁滯／耦合／動態 | legacy ch1、hexapole notes |
| 中層 Force Generation | 10 kHz | 由 `f_d` 經最佳磁通分配求 `v_d` | legacy ch1 |
| 外迴圈 Motion Control | 1.6 kHz | 由視覺回饋 `p` 求 `f_d` | legacy ch1、hexapole notes |

---

## 來源代碼

| 代碼 | 檔案 |
|---|---|
| hexapole notes | `docs/research/hexapole_force_model_notes.md` |
| foundation | `docs/research/foundation.md` |
| NSTC | `docs/research/nstc_project_report.md` |
| legacy ch1 | `legacy/01_introduction.tex`（舊中文初稿） |
| chNN.tex | `contents/chapterNN.tex` |
