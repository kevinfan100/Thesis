# 文獻筆記：六極電磁致動器系統

> 本文件記錄論文閱讀筆記，供論文撰寫參考。
> 最後更新：2026-01-17

---

## 目錄

1. [核心論文系列](#核心論文系列)
2. [技術發展脈絡](#技術發展脈絡)
3. [關鍵技術概念](#關鍵技術概念)
4. [重要方程式](#重要方程式)
5. [實驗參數彙整](#實驗參數彙整)
6. [待補充文獻](#待補充文獻)

---

## 核心論文系列

### 博士論文

#### 1. Fei Long 博士論文 (2016)
**標題**: Three-Dimensional Motion Control and Dynamic Force Sensing of a Magnetically Propelled Micro Particle Using a Hexapole Magnetic Actuator

**來源**: The Ohio State University

**核心貢獻**:
- 六極電磁致動器的設計與建模
- 集總參數磁力模型 (Lumped Parameter Force Model)
- 過驅動系統的最佳逆模型推導
- 霍爾感測器整合，解決磁滯效應
- 動態力感測估測器 (Kalman Filter)

**解決的四大問題**:
1. 冗餘性與耦合 (Redundancy & Coupling)
2. 不穩定性 (Instability)
3. 非線性 (Nonlinearity)
4. 位置依賴性 (Position Dependency)

**關鍵發現**:
- 霍爾感測器直接測量磁通量大幅提升力模型精度
- 電流基模型在磁滯效應下精度下降
- 提出非線性磁化效應建模

---

#### 2. Ta-Min Meng 博士論文 (2023)
**標題**: Control of Hexapole Electromagnetic Actuator Enabling Ultra-Precise High-Speed 3-D Untethered Manipulation of Magnetic Microprobe and 3-D Scanning of Biological Sample in Aqueous Solutions

**來源**: The Ohio State University

**核心貢獻**:
- 六輸入六輸出閉迴路磁通控制
- 最佳磁通分配 (Optimal Flux Allocation)
- 位置相關離散時間運動控制律
- 皮牛頓級探針-樣品交互作用力控制
- 活細胞 3D 掃描驗證

**研究目標**:
> "The ability to apply precisely controlled forces to individual cells, acquire their mechanical properties, visualize their dynamics in real time, and manipulate their conformation in their native environment."

**系統架構**:
```
六極致動器 → 磁通控制 → 最佳分配 → 運動控制 → 力控制
    ↑                                           |
    └─── 霍爾感測器回饋 ←── 3D視覺追蹤 ←─────────┘
```

---

### 期刊論文

#### 3. Optimal Current Allocation (2021)
**標題**: Optimal Current Allocation Rendering 3-D Magnetic Force Production in Hexapole Electromagnetic Actuation

**期刊**: IEEE/ASME Transactions on Mechatronics, Vol. 26, No. 5

**作者**: Fei Long, Peng Cheng, Ta-Min Meng, Chia-Hsiang Menq

**核心貢獻**:
- 最小化輸入電流向量 2-norm 的最佳逆模型
- FPGA 實時電流分配實現
- 力生成體積 (Force Production Volume) 概念
- 實驗驗證：定位精度與軌跡追蹤

**關鍵方程式**:

磁力二次型：
$$\mathbf{F}(\mathbf{p}, \mathbf{I}) = g_I I_{max}^2 \hat{\mathbf{I}}^T K_I^T L(\hat{\mathbf{p}}) K_I \hat{\mathbf{I}}$$

Lagrange 函數：
$$L(\phi, \theta, \hat{\mathbf{p}}) = \|\hat{\mathbf{I}}\|^2 + \boldsymbol{\lambda}^T \left( \hat{\mathbf{I}}^T N(\hat{\mathbf{p}}) \hat{\mathbf{I}} - \hat{\mathbf{r}}(\phi, \theta) \right)$$

**實驗結果**:
- 工作空間：45μm × 45μm × 45μm
- 最佳逆模型誤差 < 5%
- 大幅減少所需驅動電流

---

#### 4. Ultra-Precise High-Speed (2023)
**標題**: Ultra-Precise High-Speed Untethered Manipulation of Magnetic Scanning Microprobe in Aqueous Solutions

**期刊**: IEEE/ASME Transactions on Mechatronics, Vol. 28, No. 1

**作者**: Ta-Min Meng, Chia-Hsiang Menq

**核心貢獻**:
- 六輸入六輸出磁通控制系統（頻寬 1000 Hz）
- 最佳電壓分配結合磁通控制
- 位置相關離散時間運動控制律
- 零均值隨機誤差追蹤

**三大核心功能**:
1. **閉迴路磁通控制**: 抑制磁滯效應，提升頻寬
2. **最佳磁通分配**: 解決冗餘、耦合、非線性、位置依賴
3. **離散時間運動控制**: 考慮熱力與量測雜訊

**控制律設計**:

追蹤誤差動態：
$$\delta x[k+1] = \lambda_c \cdot \delta x[k] - \varepsilon[k]$$

其中 $\varepsilon[k]$ 為零均值隨機變數：
$$\varepsilon[k] = \frac{\Delta t}{\gamma} \left[ f_T[k] + (1-\lambda_c) \sum_{i=1}^{d} f_T[k-i] \right] + (1-\lambda_c) n_x[k]$$

**實驗結果**:
- 2D 光柵掃描：40μm × 16μm / 2秒
- 追蹤誤差標準差：~32 nm (x,y), ~31 nm (z)
- 3D 快速轉向驗證成功

---

#### 5. Piconewton Scale Force Control (2023/2024)
**標題**: Control of the Probe-Sample Interaction Force at the Piconewton Scale by a Magnetic Microprobe in Aqueous Solutions

**期刊**: IEEE/ASME Transactions on Mechatronics

**作者**: Ta-Min Meng, Chia-Hsiang Menq

**核心貢獻**:
- 改進的六輸入六輸出控制律（頻寬 > 4 kHz）
- 探針-樣品交互作用力控制
- Kalman 濾波實時參數估計
- 活細胞壓痕實驗驗證

**改進的磁通控制**:
- 預濾波器 (Prefilter) 設計
- 擾動估測器 (Disturbance Estimator)
- 精確匹配理論預測

**交互作用力模型**:

壓痕過程運動方程：
$$\gamma_z[k] \delta \dot{z}(t) = -k_z[k] \delta z(t) + \{f_{mz}[k] - f_E[k] + f_{Tz}[k]\}$$

壓痕增益：
$$a_z[k] = \frac{1 - \exp\left(-\frac{k_z[k]}{\gamma_z[k]} \Delta t\right)}{k_z[k]}$$

**實驗結果**:
- 力生成頻寬 > 4 kHz
- 活細胞壓痕：1, 10, 100 Hz
- 力誤差標準差 ~0.1 pN（< 10% 熱力）

---

## 技術發展脈絡

```
2016: Fei Long 博士論文
      └── 六極設計、集總參數模型、最佳逆模型
          ↓
2021: Optimal Current Allocation
      └── FPGA 實時電流分配、力生成體積
          ↓
2022: Hall-Sensor-Based Force Modeling
      └── 霍爾感測器整合、提升力模型精度
          ↓
2023: Ultra-Precise High-Speed
      └── 六輸入六輸出磁通控制、運動控制律
          ↓
2023/2024: Piconewton Scale Control
      └── > 4 kHz 頻寬、探針-樣品力控制
          ↓
2023: Ta-Min Meng 博士論文
      └── 整合所有技術、活細胞 3D 掃描
```

---

## 關鍵技術概念

### 1. 六極電磁致動器 (Hexapole Electromagnetic Actuator)

**幾何配置**:
- 六個尖端磁極，成對排列於三個正交軸
- 三個上平面（P2, P4, P5）、三個下平面（P1, P3, P6）
- 工作空間半徑 ℓ = 500 μm（可調 200-1000 μm）
- 避免光學路徑阻擋

**材料**:
- 磁極：1018 鋼棒（飽和限 > 2T）
- 線圈：70 匝，電流限制 3A
- 磁軛：連接所有磁極

### 2. 過驅動系統 (Over-Actuated System)

**特性**:
- 6 輸入（電流/電壓）→ 3 輸出（力）
- 存在冗餘自由度
- 需要最佳分配策略

**最佳分配目標**:
- 最小化 $\|\mathbf{I}\|^2$ 或 $\|\boldsymbol{\phi}\|^2$
- 滿足力生成約束

### 3. 磁通控制 vs 電流控制

| 特性 | 電流控制 | 磁通控制 |
|------|----------|----------|
| 磁滯效應 | 受影響 | 抑制 |
| 頻寬 | ~200 Hz | > 4 kHz |
| 實現複雜度 | 低 | 高 |
| 精度 | 較低 | 高 |

### 4. 霍爾感測器整合

**配置**:
- 6 個霍爾感測器 (Asahi Kasei EQ-730L)
- 尺寸：4.1mm × 3mm × 1.15mm
- 表面安裝（非尖端）

**校正**:
- 表面測量 $v_s$ 與尖端 $v_t$ 比例 ~0.47
- 頻率響應在 4000 Hz 內保持準靜態關係

### 5. 視覺追蹤系統

**硬體**:
- CMOS 相機 (Mikrotron MC3010)
- FPGA 實時影像處理
- 超發光二極體 (SLD) 照明

**性能**:
- 取樣率：最高 10,000 fps
- 解析度：~0.7 nm (x,y), ~2.3 nm (z)
- 雙珠追蹤：漂移補償

---

## 重要方程式

### 磁梯度力模型

**磁通基模型**:
$${}^A\mathbf{f}_m({}^A\mathbf{p}, \boldsymbol{\phi}) = g_\phi \sum_{i=1}^{6} \sum_{j=1}^{6} \Phi_i \Phi_j \nabla \left( \frac{\mathbf{u}_i \cdot \mathbf{u}_j}{\hat{r}_i^2 \hat{r}_j^2} \right)$$

其中：
- $g_\phi = \frac{V\chi}{2\mu_0} \cdot \frac{1}{(4\pi)^2 \ell^5}$
- $V$: 探針體積
- $\chi$: 磁化率
- $\ell$: 工作空間半徑

### Langevin 方程

低雷諾數下探針運動：
$$\gamma \dot{\mathbf{p}}(t) = \mathbf{f}_m(\mathbf{p}(t), \mathbf{I}(t)) + \mathbf{f}_T(t)$$

Stokes 阻力係數：$\gamma = 6\pi\eta R$

### 熱力變異數

$$\sigma_{f_T}^2 = \frac{4 k_B T \gamma}{\Delta t}$$

### 離散時間運動方程

$$x[k+1] = x[k] + \frac{\Delta t}{\gamma} (f_d[k] + f_T[k])$$

---

## 實驗參數彙整

### 系統參數

| 參數 | 數值 | 說明 |
|------|------|------|
| 工作空間半徑 ℓ | 500 μm | 可調 200-1000 μm |
| 探針半徑 R | 2.25 μm | 鐵磁性球 |
| 線圈匝數 | 70 | - |
| 最大電流 | 3 A | - |
| 中心磁通密度 | ~100 Gauss | 1A 單極激勵 |

### 控制系統參數

| 參數 | 數值 | 說明 |
|------|------|------|
| 磁通控制取樣率 | 100 kHz | FPGA |
| 視覺伺服取樣率 | 1.6 kHz | 雙珠追蹤 |
| 磁通控制頻寬 | > 4 kHz | 改進版 |
| 力生成頻寬 | > 4 kHz | - |

### 性能指標

| 指標 | 數值 | 來源 |
|------|------|------|
| 定位解析度 (x,y) | ~0.7 nm | 視覺追蹤 |
| 定位解析度 (z) | ~2.3 nm | 視覺追蹤 |
| 追蹤誤差 (x,y) | ~32 nm | 熱力+雜訊 |
| 追蹤誤差 (z) | ~31 nm | 熱力+雜訊 |
| 力誤差 | ~0.1 pN | < 10% 熱力 |
| 掃描速度 | 40μm × 16μm / 2s | 光柵掃描 |

---

## 待補充文獻

### 優先閱讀

1. **Hall-Sensor-Based Magnetic Force Modeling (2022)**
   - Long, Meng, Wang, Menq
   - IEEE/ASME Trans. Mechatronics, Vol. 27, No. 5
   - 霍爾感測器力模型詳細推導

2. **Design and Modeling of a 3-D Magnetic Actuator (2011)**
   - Zhang, Menq
   - IEEE/ASME Trans. Mechatronics, Vol. 16, No. 3
   - 早期六極設計

### 背景文獻

- [ ] 光學鉗夾技術比較
- [ ] AFM 技術限制
- [ ] 細胞力學相關文獻
- [ ] 低雷諾數流體力學

---

## 論文撰寫建議

### 文獻回顧章節結構

1. **磁性操控技術發展**
   - 傳統磁鉗（力施加器）
   - 多極電磁致動器演進
   - 與光學鉗夾、AFM 比較

2. **六極電磁致動系統**
   - 設計原理與幾何配置
   - 力模型推導（電流基 → 磁通基）
   - 過驅動系統最佳分配

3. **控制技術**
   - 電流控制 vs 磁通控制
   - 視覺伺服控制
   - 力控制與參數估計

4. **生物應用**
   - 皮牛頓級力量測
   - 細胞機械特性探測
   - 活細胞掃描

### 關鍵圖表建議

1. 六極配置示意圖
2. 力模型發展時間線
3. 控制系統方塊圖
4. 實驗結果對比表

---

*此文件將持續更新，新增論文請加入「待補充文獻」區塊*
