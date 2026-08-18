# Hexapole Magnetic Tweezers: Force Model 與 Optimal Flux Allocation

## 參考文獻

- [Long2021a] F. Long, T.M. Meng, J.J. Wang, C.H. Menq, "Hall-Sensor-Based Magnetic Force Modeling and Inverse Modeling for Hexapole Electromagnetic Actuation," IEEE/ASME Trans. Mechatronics, 2021.
- [Long2021b] F. Long, P. Cheng, T.M. Meng, C.H. Menq, "Optimal Current Allocation Rendering 3-D Magnetic Force Production in Hexapole Electromagnetic Actuation," IEEE/ASME Trans. Mechatronics, vol. 26, no. 5, pp. 2408-2417, Oct. 2021.
- [Meng2023] T.M. Meng, C.H. Menq, "Ultra-Precise High-Speed Untethered Manipulation of Magnetic Scanning Microprobe in Aqueous Solutions," IEEE/ASME Trans. Mechatronics, vol. 28, no. 1, pp. 280-291, Feb. 2023.
- [Meng2023_diss] T.M. Meng, "Control of Hexapole Electromagnetic Actuator Enabling Ultra-Precise High-Speed 3-D Untethered Manipulation of Magnetic Microprobe and 3-D Scanning of Biological Sample in Aqueous Solutions," Ph.D. Dissertation, Ohio State University, 2023.
- [NSTC_Report] 國科會計畫 NSTC 114-2223-E-007-005 進度報告, 2025.

---

## 1. 系統概述

### 1.1 六極電磁致動器

六極電磁致動器由六個尖端形電磁極組成，材質為高飽和極限（>2 T）的 1018 鋼。六個磁極透過共用磁軛連接，每個磁極由獨立的線圈驅動（匝數 Nc，電流上限 3 A）。三對磁極對稱排列，尖端圍出一個多面體工作空間。

核心參數：
- **ℓ**：workspace 中心到各極尖端的距離（可調，標稱值 500 um）
- 六個 Hall sensor（Asahi Kasei EQ-730L）裝於各極表面，量測磁通量
- 六通道 16-bit ADC（TI/ADS8365）連接至 FPGA

### 1.2 座標系統

定義兩個座標系統：

- **Measurement coordinate** {xm, ym, zm}：z 軸對齊顯微鏡光軸，用於粒子追蹤和運動控制
- **Actuation coordinate** {xa, ya, za}：三對磁極分別沿三個正交軸排列，用於力建模和磁通分配

兩者的關係透過旋轉矩陣 R 連結：

```
ᵐp = ᵐₐR  ᵃp
ᵃp = (ᵐₐR)⁻¹ ᵐp
```

在 Meng 的設計中，將六極繞 x 軸旋轉 -45° 再繞 y 軸旋轉約 35°，使六個極尖分布在 measurement coordinate 的上下兩個水平面上，避免遮擋光路。

---

## 2. Force Model 的三代演進

### 2.1 Magnetic-Flux-Based Force Model（基礎力模型）

這是所有力模型的根基。在 actuator coordinate 下，六個極尖端的磁通量 phi 對磁性探測珠施加的 3D 磁梯度力為二次型：

```
ᵃf_m(ᵃp, phi) = g_phi * [ phi^T Lx(ᵃp̄) phi ]
                          [ phi^T Ly(ᵃp̄) phi ]
                          [ phi^T Lz(ᵃp̄) phi ]
```

其中：
- **phi** = [phi_1, phi_2, phi_3, phi_4, phi_5, phi_6]^T：六極磁通量向量（6x1）
- **Lx, Ly, Lz**：三個 6x6 gradient matrix，合稱 gradient matrix L(ᵃp̄)
- **ᵃp̄ = ᵃp / ℓ**：相對於 workspace 半徑 ℓ 的無因次化位置
- **g_phi(ℓ)**：force gain，與探測珠體積、磁化率成正比，與 ℓ⁻⁵ 成反比

等效地，可寫成更緊湊的張量形式 [NSTC_Report eq(7)]：

```
ᵃf_m(ᵃp, phi) = g_phi(ℓ) * Σᵢ₌₁⁶ Σⱼ₌₁⁶ phi_i phi_j ∇(uᵢuⱼ / rᵢ²rⱼ²)
```

其中 ∇(uᵢuⱼ / rᵢ²rⱼ²) 構成一個 dimensionless、位置相關的 **6x6x4 張量**，描述六極之間的耦合及力生成的位置相關性。

**關鍵特性**：力與磁通量之間是 **quadratic（二次型）** 關係，即 F ∝ ||phi||²。這個特性是後續 scalable optimal allocation 的數學基礎。

gradient matrix L(ᵃp̄) 的確定方式有三種：
1. 磁路分析 [Long2011]
2. 有限元分析 (FEA) [Long2016]
3. 實驗校準 [Long2016]

### 2.2 Current-Based Force Model（電流力模型）

由 Hopkinson's law，磁通量可準靜態地由輸入電流產生：

```
phi_I = (Nc / Ra) * K_I * I
```

其中：
- **Nc**：線圈匝數
- **Ra**：lumped magnetic reluctance
- **K_I**：6x6 symmetric flux distribution matrix（描述多極耦合下的磁通分布）
- **I** = [I_1, ..., I_6]^T：六個線圈的輸入電流

代入 flux-based model 得：

```
ᵃf_m(ᵃp, I) = g_I * Î^T K_I^T L(ᵃp̄) K_I Î
```

其中：
- **g_I = (Nc/Ra)² * g_phi**：current-based force gain
- **Î = I / I_max**：normalized current vector

**兩大缺陷**：
1. **Hysteresis & remanence 不確定性**：電流與磁通量之間的準靜態關係 phi_I = (Nc/Ra) K_I I 忽略了磁滯和殘磁。當需要較大力時，不確定性增加，導致力的誤差增大。
2. **忽略動態特性**：eddy current 引起的磁通量生成動態被忽略，限制了高頻力生成的精度。

### 2.3 Hall-Sensor-Based Force Model（Hall sensor 力模型 — 最終版本）

為克服 current-based model 的缺陷，在每個極尖端裝置 Hall sensor 直接量測磁通量。

磁通量與 Hall sensor 電壓的關係：

```
phi = D_H * v_H
```

其中：
- **D_H**：diagonal voltage-flux gain matrix（6x6 對角矩陣，透過實驗校準獲得）
- **v_H** = [v_H1, ..., v_H6]^T：六個 Hall sensor 的電壓讀數（6x1）

定義 normalized D̂_H = D_H / ||D_H||，代入 flux-based model 得 Hall-sensor-based force model：

```
ᵐf_m(ᵐp, v_H) = g_H * ᵐₐR [ v_H^T D̂_H^T L(ᵃₘR ᵐp/ℓ) D̂_H v_H ]
```

其中 **g_H = ||D_H||² * g_phi** 是與 sensor voltage vector 相關的 force gain。

**優勢**：
- 直接用量測到的磁通量（而非假設的電流-磁通關係）計算力
- **完全消除 hysteresis 和 remanence 的不確定性**
- 結合閉迴路磁通控制，可實現高頻寬、高精度的力生成

---

## 3. Optimal Flux Allocation（最優磁通分配 — Inverse Model）

### 3.1 問題定義

Hexapole 是一個 **6-input / 3-output** 系統，具有以下四個特性/挑戰：

| 特性 | 說明 |
|---|---|
| **Redundancy** | 6 個輸入（phi）只需產生 3 個輸出力分量 |
| **Coupling** | 各極之間存在磁路耦合，K_I 非對角 |
| **Nonlinearity** | 力與 phi 是二次型關係 |
| **Position-dependency** | gradient matrix L(ᵃp̄) 隨位置改變 |

**Inverse problem**：給定期望 3D 力 ᵃf_d 和探測珠位置 ᵃp，求最佳的 6x1 磁通量分配 phi_opt（以及對應的 Hall sensor 電壓 v_d）。

### 3.2 早期方法：Constant Constraints

最早的方法 [Long2013, Long2016] 在 workspace 中心用三個常數約束移除冗餘，得到 effective actuation current delta_Î 和 force 的精確線性關係：

```
F̂(0, delta_Î) = J_delta_I * delta_Î = 2J * delta_Î
```

其中 J = 3 * diag[cx, cy, cz] - (cx + cy + cz) * diag[1,1,1]。

可以用此求 inverse：

```
delta_Î ≈ (1/2) J⁻¹ F̂_d(ᵃp̄) - J ᵃp̄
```

**兩大限制**：
1. 常數約束導致 workspace 中心以外的電流過大（excessive current）
2. 透過一階 Taylor 展開到整個 workspace 會引入隨距離增加的顯著誤差

### 3.3 Scalable 最佳化公式

利用力的 quadratic 特性，將期望力分解為**大小**和**方向**：

```
ᵃf_d = ||ᵃf_d|| * r̂(varphi, theta)
```

其中 ||ᵃf_d|| 是力的大小，r̂(varphi, theta) 是球座標下的 unit force direction vector。

由於 F ∝ ||phi||²，最佳分配存在 scalable 關係：

```
phi_opt(ᵃf_d, ᵃp̄) = sqrt(||ᵃf_d|| / g_phi) * phi_hat_opt(varphi, theta, ᵃp̄)
```

即 **找最佳分配時只需考慮方向，大小只是 scaling factor**。

### 3.4 Lagrange Multiplier 最佳化

最佳化問題的正式表述：

```
min ||Î||²
s.t. Î^T N(ᵃp̄) Î = r̂(varphi, theta)     （三個非線性等式約束）
```

使用 Lagrange multipliers lambda = [lambda_x, lambda_y, lambda_z] 構造 Lagrange function：

```
L(varphi, theta, ᵃp̄) = ||Î||² + lambda^T ( Î^T N(ᵃp̄) Î - r̂(varphi, theta) )
```

共 9 個變數（6 個 phi + 3 個 lambda），局部最小值出現在 ∇(L) = 0。雖然此方法消除了一階 Taylor 近似的誤差，但直接求解此非線性系統不適合即時控制。

### 3.5 即時 Inverse Model 的兩種實現方法

兩種方法都採用 direction-dependent quadratic approximation 來構造解析式 inverse model。

#### 方法 A：Second-Order Taylor Expansion

從中心最佳解出發，對每個電流分量 i 做二階 Taylor 展開：

```
Î_opt^unit(varphi, theta, ᵃp̄)_i ≈ Î_opt^unit(varphi, theta)_i + G_i(varphi, theta) ᵃp̄ + (1/2) ᵃp̄^T H_i(varphi, theta) ᵃp̄
```

其中 G_i 是 3x1 gradient vector，H_i 是 3x3 Hessian matrix。

整理成 augmented position vector 的二次型：

```
Î_opt^unit(varphi, theta, ᵃp̄)_i ≈ P^T D_i^Taylor(varphi, theta) P
```

P = [x̄, ȳ, z̄, 1]^T（4x1 augmented position vector），D_i^Taylor 是 4x4 矩陣。

#### 方法 B：Least-Squares Fitting（精度更高，論文推薦）

1. 用 MATLAB optimization toolbox 在 3D workspace 預設的多個空間位置 × 多個方向 (varphi, theta) 數值求解最佳分配
2. 用 least squares 擬合成相同的二次型格式：

```
Î_opt^unit(varphi, theta, ᵃp̄)_i ≈ P^T D_i^LS(varphi, theta) P
```

D_i^LS 的格式與 Taylor 版相同（4x4），但係數透過 fitting 最小化整個空間範圍的誤差。

**精度比較**：
- Taylor：誤差隨離中心距離增加明顯增長
- **LS：在 45 um x 45 um x 45 um 空間內誤差 < 5%**

---

## 4. 即時磁通分配的歸一化和泛化 [NSTC_Report Section 2.3]

### 4.1 目標

利用同一控制系統和參數化數位控制律，控制任意給定的對稱六極電磁致動器。透過歸一化和縮放，使最優磁通分配技術具有泛化能力。

### 4.2 完整即時分配流程

信號流如下圖（對應 NSTC_Report 圖 16）：

```
ᵐf_d ──→ [ᵃₘR] ──→ ᵃf_d ──→ [Normalization] ──→ ||ᵃf_d||
ᵐp   ──→ [ᵃₘR] ──→ ᵃp   ──→ [ᵃp̄ = ᵃp/ℓ]        ᵃf̂_d = r̂(varphi, theta)
                                                          |
               ┌─────────────────────────────────────────┘
               v
    [Optimal Flux Allocation]  ──→  phi_hat_d (6x1, unit optimal)
               |
               v
    [Scaling: sqrt(||ᵃf_d|| / g_phi)] ──→ phi_d (6x1, actual flux)
               |
               v
    [D̂_H⁻¹]  ──→  v_d (6x1, 目標 Hall sensor 電壓)
```

### 4.3 各步驟詳解

#### Step 1: 位置座標變換

```
ᵐp = ᵐₐR ᵃp
```

旋轉矩陣 R 將 measurement coordinate 下的位置和力轉換至 actuator coordinate。

#### Step 2: 位置歸一化

```
ᵃp̄ = ᵃp / ℓ       （無因次化位置）
P = [x̄, ȳ, z̄, 1]^T  （4x1 augmented position vector）
```

歸一化後，六極尖端位於 x̄ = ±1, ȳ = ±1, z̄ = ±1。

歸一化位置決定了 dimensionless gradient tensor（6x6x4），描述六極耦合和位置相關性。

#### Step 3: 力歸一化 — 分解為大小和方向

```
ᵃf_d = ||ᵃf_d|| * r̂(varphi, theta)
```

varphi, theta 為球座標角度，定義 unit force direction。

此分解利用 quadratic 特性，使分配問題 scale-invariant：只需對方向做最佳化。

#### Step 4: Optimal Flux Allocation（核心計算）

方向相關的 **6x4x4 最優磁通分配張量 D(varphi, theta)** 是 inverse model 的核心。給定歸一化位置 P 和 unit force direction r̂(varphi, theta)，unit optimal flux allocation 為：

```
phi_hat_d = phi_hat_opt(varphi, theta, ᵃp̄) ≈ P^T D(varphi, theta) P     --- (8)
```

此處 D(varphi, theta) 包含 6 個 4x4 矩陣（每個磁極一個 D_i），即 phi_hat_d 是 6x1 向量，第 i 個元素為：

```
phi_hat_d_i = P^T D_i(varphi, theta) P     for i = 1, ..., 6
```

D_i 的係數透過離線 least-squares fitting 預先計算好，即時計算時只需做矩陣乘法。

#### Step 5: Scaling — 從 unit allocation 到 actual flux

```
phi_d = sqrt(||ᵃf_d|| / g_phi) * phi_hat_d     --- (9)
```

g_phi(ℓ) 是 probe-specific 的 force gain，需透過實驗校準。

#### Step 6: 轉換為 Hall sensor 電壓

磁通量 phi 不易直接設定，但可透過 Hall sensor 間接控制。利用 phi = D_H v_H：

```
v_d(ᵃf_d, ᵃp̄) = sqrt(||ᵃf_d|| / g_H) * D̂_H⁻¹ * phi_hat_opt(varphi, theta, ᵃp̄)     --- (10)
```

其中：
- **g_H = ||D_H||² * g_phi**：Hall-sensor-based force gain
- **D̂_H = D_H / ||D_H||**：normalized voltage-flux gain matrix
- **D̂_H⁻¹** 為對角矩陣的逆，計算量極小

v_d 即為六個 Hall sensor 的目標電壓，送入 6-input-6-output 閉迴路磁通控制系統作為 reference。

### 4.4 泛化能力

透過以上分析，optimal flux allocation 的泛化僅需提供三個校準參數：

| 參數 | 說明 | 確定方式 |
|---|---|---|
| **ℓ** | workspace 半徑（極尖到中心距離） | 致動器設計/量測 |
| **g_H** | Hall-sensor-based force gain | 實驗校準（探測珠 + 致動器） |
| **D_H** | diagonal voltage-flux gain matrix | 實驗校準（Hall sensor） |

加上預計算好的 D(varphi, theta) 張量，即可將最優分配技術應用於**任何對稱六極電磁致動器**。

---

## 5. 閉迴路磁通控制系統（Magnetic Flux Control）

Optimal flux allocation 輸出的 v_d 是目標，但仍需閉迴路控制來實現精確的磁通量生成。

### 5.1 為何需要閉迴路

直接用電流開迴路驅動（current-based）會面臨：
- **Multipole coupling**：激發一個極時，其他極也會產生磁通量
- **Hysteresis / remanence**：磁通量與電流不是單值函數
- **Limited bandwidth**：開迴路 flux 生成頻寬受限

### 5.2 6-Input-6-Output 動態模型

六極致動器視為 6-input-6-output 系統。輸入為六個線圈的電壓 u，輸出為六個 Hall sensor 量測的電壓 v_m。

**簡化連續時間模型** [NSTC_Report eq(1)]：

```
G(s) = [1.1592e7 / (s² + 6.6172e3 s + 1.1592e7)] * B
```

B 是 6x6 增益歸一化矩陣，捕捉低頻多極耦合。此模型用單一二階動態模擬所有 36 組頻率響應。

**離散時間模型**（ZOH + 取樣 @ 100 kHz）[NSTC_Report eq(3)]：

```
H(z⁻¹) = z⁻¹ * [5.6695e-4 * (1 + 0.9782 z⁻¹) / (1 - 1.9348 z⁻¹ + 0.9359 z⁻²)] * B
```

參數化形式 [NSTC_Report eq(4)]：

```
H(z⁻¹) = z⁻ᵈ * [k_o(1 + b z⁻¹) / (1 - a₁ z⁻¹ - a₂ z⁻²)] * B
```

### 5.3 控制律組成

磁通控制律由三個部分組成 [Meng2023]：

```
u[k] = B⁻¹ { v_ff[k] + delta_v_fb[k] - ŵ[k] }
```

- **v_ff[k]**：feedforward control（一步預測實現）
- **delta_v_fb[k]**：feedback control（基於估測的 tracking error）
- **ŵ[k]**：disturbance estimate（補償建模誤差和殘磁）

控制目標：delta_v[k+1] = lambda_c * delta_v[k]，其中 0 ≤ lambda_c < 1。

### 5.4 Augmented State Estimator

```
ŝ₁[k+1] = lambda_e ŝ₁[k] + L₁{delta_v[k] - ŝ₁[k]}
ŝ₂[k+1] = ŝ₁[k] + L₂{delta_v[k] - ŝ₁[k]}
ŵ[k+1]  = ŵ[k] + delta_ŵ[k] + L₃{delta_v[k] - ŝ₁[k]}
delta_ŵ[k+1] = delta_ŵ[k] + L₄{delta_v[k] - ŝ₁[k]}
```

所有 eigenvalue 設為 lambda_e，四個 feedback matrix L₁~L₄ 有解析解。

### 5.5 閉迴路性能

- 磁通控制頻寬：**~1000 Hz**（lambda_c = 0.9391）
- Estimator 頻寬：**~5000 Hz**（lambda_e = 0.7304）
- 取樣率：**100 kHz**
- Multipole coupling：從 28% 降至 **< 0.1%**
- Hysteresis / remanence：被 disturbance estimator 有效補償

---

## 6. 完整系統信號流總結

```
                    [Motion Control Law]     (1.6 kHz)
                    計算期望力 ᵐf_d
                           |
                           v
                    [Coordinate Transform]
                    ᵐf_d → ᵃf_d,  ᵐp → ᵃp
                           |
                           v
                    [Normalization]
                    ᵃp̄ = ᵃp/ℓ,  P = [x̄,ȳ,z̄,1]^T
                    ||ᵃf_d||,  r̂(varphi, theta)
                           |
                           v
                    [Optimal Flux Allocation]  (1.6 kHz, FPGA2)
                    phi_hat_d_i = P^T D_i(varphi,theta) P
                           |
                           v
                    [Scaling + Hall Voltage Mapping]
                    v_d = sqrt(||ᵃf_d||/g_H) * D̂_H⁻¹ * phi_hat_d
                           |
                           v
                    [6-in-6-out Flux Control Law]  (100 kHz, FPGA2)
                    u[k] = B⁻¹{v_ff + delta_v_fb - ŵ}
                           |
                           v
                    [D/A → Amplifier k_A → Coils → Poles]
                           |
                           v
                    [phi at pole tips]
                           |
                           v
                    [Hall Sensors → A/D → v_m]  (feedback to flux control)
                           |
                           v
                    [Hall-sensor-based Force Model]
                    ᵐf_m = g_H * R * [v_m^T D̂_H^T L(ᵃp̄) D̂_H v_m]
                           |
                           v
                    [磁力作用於 probe → particle dynamics]
```

**雙迴路架構**：
- **外迴路（Motion Control）**：1.6 kHz，決定期望力，透過 optimal allocation 映射為目標磁通電壓
- **內迴路（Flux Control）**：100 kHz，精確追蹤目標磁通，抑制 hysteresis/coupling/dynamics

---

## 7. 與 Constant Constraints 的比較

```
                        Constant Constraints         Optimal Allocation
─────────────────────────────────────────────────────────────────────
冗餘消除方式              固定三個約束                  Lagrange multiplier 最佳化
適用範圍                  僅中心點精確                  整個 workspace（LS fitting < 5%）
電流/磁通大小             excessive（過大）             最小化 2-norm
Force production volume  較小                         顯著增大
位置相關性處理             不處理（一階 Taylor）          完整處理（二次型 + LS）
Force error               隨距離/力增大而增長           整體 < 5%
即時計算量                較低                         稍高（6 個 4x4 quadratic form）
```
