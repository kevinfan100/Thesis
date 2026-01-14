# 論文開發流程

## 研究背景

### 研究主題
六極電磁致動器系統用於水溶液中磁性微探針的超精密高速無繫繩操控

### 核心論文系列（Ta-Min Meng & Chia-Hsiang Menq）

| 論文 | 期刊 | 核心貢獻 |
|------|------|----------|
| Design and Modeling of a 3-D Magnetic Actuator | IEEE/ASME Trans. Mechatronics | 六極致動器設計、集總參數力模型 |
| Optimal Current Allocation Rendering 3-D Magnetic Force Production | IEEE/ASME Trans. Mechatronics | 過驅動系統最佳電流分配、二次規劃 |
| Hall-Sensor-Based Magnetic Force Modeling | IEEE/ASME Trans. Mechatronics (2022) | 霍爾感測器直接測量磁通、提升力預測精度 |
| Control of Probe-Sample Interaction Force at Piconewton Scale | IEEE/ASME Trans. Mechatronics (2024) | 皮牛頓級力控制、六輸入六輸出控制律 |
| Ultra-Precise High-Speed Untethered Manipulation | IEEE/ASME Trans. Mechatronics (2023) | 高速無繫繩操控、3D視覺伺服 |

### 關鍵技術概念

```
┌─────────────────────────────────────────────────────────────────┐
│                      系統架構                                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │ 六極電磁     │    │ 磁性微探針   │    │ 生物樣品     │      │
│  │ 致動器       │───▶│ (水溶液中)   │───▶│ 掃描/量測    │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│         ▲                   │                                   │
│         │                   ▼                                   │
│  ┌──────────────┐    ┌──────────────┐                          │
│  │ 最佳電流     │◀───│ 3D 視覺      │                          │
│  │ 分配控制     │    │ 伺服追蹤     │                          │
│  └──────────────┘    └──────────────┘                          │
│         ▲                                                       │
│         │                                                       │
│  ┌──────────────┐                                              │
│  │ 霍爾感測器   │                                              │
│  │ 磁通回饋     │                                              │
│  └──────────────┘                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**核心方程式：**
- 磁場模型：$B = \sum_{j=1}^{6} k_m \frac{q_j}{r_j^2} u_j$
- Stokes 阻力：$F_{drag} = 6\pi\eta r v$（低雷諾數）
- 磁梯度力：$\mathbf{F} = \nabla(\boldsymbol{\mu} \cdot \mathbf{B})$

---

## 開發週期

```
1. 規劃 → 2. 撰寫 → 3. 編譯 → 4. 版控 → 5. 審閱
```

### 1. 規劃階段
- 與 Claude 討論章節大綱
- 確定每章要點
- 使用 Memory 記錄研究概念關係

### 2. 撰寫階段
- Claude 協助生成 LaTeX（表格、方程式、演算法）
- Claude 協助格式化 BibTeX 參考文獻
- 使用 MATLAB MCP 執行模擬並生成圖表

### 3. 編譯驗證
- VSCode 自動編譯（存檔時觸發）
- 或命令列：`latexmk thesis.tex`
- Claude 協助解讀錯誤訊息

### 4. 版本控制
- Claude 協助生成 commit message
- 定期推送到 GitHub

### 5. 審閱修改
- 收到指導教授回饋後
- Claude 協助批次修改、格式調整

---

## 章節命名約定

### 檔案結構
```
NTHU_template/
├── thesis.tex              # 主文件
├── nthuthesis.cls          # 論文格式類別
├── nthuvars.tex            # 論文元資料
├── thesis.bib              # 參考文獻
│
├── 00_abstract.tex         # 摘要
├── 00_acknowledgements.tex # 致謝
│
├── 01_introduction.tex     # 第一章：緒論
├── 02_literature.tex       # 第二章：文獻回顧
├── 03_theory.tex           # 第三章：理論基礎
├── 04_system.tex           # 第四章：系統設計
├── 05_control.tex          # 第五章：控制方法
├── 06_experiment.tex       # 第六章：實驗結果
├── 07_conclusion.tex       # 第七章：結論
│
├── 10_appendix.tex         # 附錄
│
└── figsrc/                 # 圖片目錄
    ├── ch01/               # 第一章圖片
    ├── ch02/               # 第二章圖片
    └── ...
```

### 建議章節內容（六極電磁致動器研究）

| 章節 | 內容 | 對應參考論文 |
|------|------|-------------|
| Ch.1 緒論 | 研究動機、目標、貢獻 | - |
| Ch.2 文獻回顧 | 磁性操控技術發展、現有系統比較 | All papers |
| Ch.3 理論基礎 | 電磁學原理、集總參數模型、力模型推導 | Design & Modeling |
| Ch.4 系統設計 | 六極致動器硬體、霍爾感測器整合 | Hall-Sensor-Based |
| Ch.5 控制方法 | 最佳電流分配、視覺伺服、力控制 | Optimal Current, Piconewton |
| Ch.6 實驗結果 | 定位精度、速度測試、生物樣品掃描 | Ultra-Precise High-Speed |
| Ch.7 結論 | 總結與未來展望 | - |

---

## 圖片命名與目錄結構

### 目錄結構
```
figsrc/
├── ch01/
│   └── motivation_overview.pdf
│
├── ch02/
│   ├── comparison_table.pdf
│   └── existing_systems.pdf
│
├── ch03/
│   ├── hexapole_geometry.pdf          # 六極幾何配置
│   ├── magnetic_field_distribution.pdf # 磁場分布
│   ├── force_envelope.pdf             # 力包絡圖
│   └── lumped_parameter_model.pdf     # 集總參數模型
│
├── ch04/
│   ├── system_architecture.pdf        # 系統架構
│   ├── hall_sensor_placement.pdf      # 霍爾感測器位置
│   ├── hardware_photo.jpg             # 實際硬體照片
│   └── microscope_integration.pdf     # 顯微鏡整合
│
├── ch05/
│   ├── control_block_diagram.pdf      # 控制方塊圖
│   ├── visual_servo_flowchart.pdf     # 視覺伺服流程
│   ├── optimal_current_algorithm.pdf  # 最佳電流算法
│   └── force_control_scheme.pdf       # 力控制架構
│
├── ch06/
│   ├── trajectory_tracking.pdf        # 軌跡追蹤結果
│   ├── positioning_accuracy.pdf       # 定位精度
│   ├── speed_comparison.pdf           # 速度比較
│   ├── force_measurement.pdf          # 力量測結果
│   └── biological_scanning.pdf        # 生物掃描結果
│
└── matlab/                            # MATLAB 生成的圖
    ├── simulation_results/
    └── data_plots/
```

### 命名規則
- 格式：`{描述}_{細節}.{副檔名}`
- 使用小寫英文、底線分隔
- 向量圖優先使用 `.pdf`，照片使用 `.jpg` 或 `.png`

---

## 參考文獻工作流

### BibTeX 管理

**thesis.bib 結構：**
```bibtex
% ========== 核心參考論文 ==========
@article{meng2023ultraprecise,
  author  = {Meng, Ta-Min and Menq, Chia-Hsiang},
  title   = {Ultra-Precise High-Speed Untethered Manipulation of
             Magnetic Scanning Microprobe in Aqueous Solutions},
  journal = {IEEE/ASME Trans. Mechatronics},
  year    = {2023},
  volume  = {28},
  number  = {1},
  pages   = {280--291}
}

@article{meng2024piconewton,
  author  = {Meng, Ta-Min and Menq, Chia-Hsiang},
  title   = {Control of the Probe-Sample Interaction Force at the
             Piconewton Scale by a Magnetic Microprobe in Aqueous Solutions},
  journal = {IEEE/ASME Trans. Mechatronics},
  year    = {2024},
  volume  = {29},
  number  = {1},
  pages   = {400--411}
}

% ========== 電磁學理論 ==========

% ========== 控制理論 ==========

% ========== 生物應用 ==========
```

### 工作流程
1. **新增文獻**：直接編輯 `thesis.bib`
2. **引用格式**：使用 `\cite{key}` 或 `\citep{key}`
3. **編譯順序**：`xelatex → bibtex → xelatex × 2`

### Claude 協助範例
```
請幫我將這篇論文格式化為 BibTeX：
[貼上論文資訊]
```

---

## 與指導教授的協作方式

### Git 分支策略
```
main                    # 穩定版本（提交給教授審閱）
├── develop            # 開發中版本
├── ch03-theory        # 第三章撰寫分支
├── ch05-control       # 第五章撰寫分支
└── revision-v1        # 第一次修訂
```

### 版本標記
```bash
# 提交初稿
git tag v1.0-draft -m "初稿完成"

# 第一次修訂後
git tag v1.1-revision1 -m "回應教授第一輪意見"
```

### 回饋處理流程
1. 收到教授回饋（PDF 批註 / 口頭 / 電子郵件）
2. 在 Claude 中整理待修改清單
3. 逐項修改並標記完成
4. 提交新版本

---

## MATLAB 程式碼管理

### 目錄結構
```
matlab/
├── simulation/
│   ├── hexapole_field.m           # 六極磁場計算
│   ├── force_model.m              # 力模型
│   ├── optimal_current.m          # 最佳電流分配
│   └── trajectory_planning.m      # 軌跡規劃
│
├── control/
│   ├── visual_servo.m             # 視覺伺服
│   ├── force_controller.m         # 力控制器
│   └── kalman_filter.m            # 卡爾曼濾波器
│
├── data_processing/
│   ├── load_experiment_data.m     # 載入實驗數據
│   └── plot_results.m             # 繪製結果圖
│
├── data/
│   └── experiment_YYYYMMDD/       # 實驗數據
│
└── figures/
    └── exported/                  # 輸出的圖片
```

### Claude MATLAB MCP 使用範例

**磁場計算：**
```
請用 MATLAB 計算六極配置的磁場分布：
- 極間距：594 μm
- 電流：1 A
- 繪製 x-y 平面的磁場向量圖
```

**力包絡分析：**
```
請用 MATLAB 計算並繪製工作空間中心的力包絡圖：
- 六個線圈電流範圍：-1A 到 +1A
- 微珠磁化率：χ = 0.5
```

**實驗數據處理：**
```
請用 MATLAB 處理這組軌跡追蹤數據：
- 繪製實際軌跡 vs 期望軌跡
- 計算 RMSE 誤差
- 輸出為 PDF 圖片
```

---

## MCP 工具使用指南

### 文獻研究
- `Perplexity research` - 深度研究某個主題
- `Perplexity search` - 搜索最新論文/技術
- `Memory` - 記錄重要文獻和概念關係

### MATLAB 模擬
- `MATLAB run_matlab_file` - 執行完整模擬
- `MATLAB evaluate_matlab_code` - 快速測試程式碼
- `MATLAB check_matlab_code` - 檢查程式碼品質

### LaTeX 撰寫
- `Context7` - 查詢 LaTeX 套件用法
- `Filesystem` - 編輯 .tex 檔案

### 常用指令範例

**文獻搜索（針對本研究）：**
```
請用 Perplexity 搜索 "hexapole electromagnetic actuation micromanipulation 2024" 的最新研究
```

```
請用 Perplexity 搜索 "piconewton force control magnetic tweezers" 的最新進展
```

**記錄概念：**
```
請用 Memory 記錄：
- 實體：Hexapole Electromagnetic Actuator
- 類型：Hardware System
- 觀察：六極配置實現3D力控制，解決過驅動問題需最佳電流分配
- 關聯：連結到 Optimal Current Allocation, Hall Sensor Feedback
```

**MATLAB 執行：**
```
請執行這段 MATLAB 程式碼計算磁場分布：
[貼上程式碼]
```

**LaTeX 語法查詢：**
```
請用 Context7 查詢如何在 LaTeX 中繪製控制系統方塊圖（使用 tikz）
```

---

## 核心概念速查

| 術語 | 英文 | 說明 |
|------|------|------|
| 六極致動器 | Hexapole Actuator | 六個磁極實現3D力控制 |
| 過驅動系統 | Over-actuated System | 6輸入3輸出，存在冗餘 |
| 最佳電流分配 | Optimal Current Allocation | 二次規劃求解冗餘問題 |
| 霍爾感測器 | Hall Sensor | 直接測量磁通量 |
| 視覺伺服 | Visual Servo | 基於影像的閉迴路控制 |
| 皮牛頓 | Piconewton (pN) | 10⁻¹² N，分子級力量 |
| Stokes 阻力 | Stokes Drag | 低雷諾數黏滯阻力 |
| 力包絡 | Force Envelope | 可達力向量的邊界 |
| 無繫繩操控 | Untethered Manipulation | 無機械連接的遠端操控 |

---

## 撰寫進度追蹤

| 章節 | 狀態 | 預計完成 | 備註 |
|------|------|----------|------|
| Ch.1 緒論 | ⬜ 未開始 | | |
| Ch.2 文獻回顧 | ⬜ 未開始 | | |
| Ch.3 理論基礎 | ⬜ 未開始 | | |
| Ch.4 系統設計 | ⬜ 未開始 | | |
| Ch.5 控制方法 | ⬜ 未開始 | | |
| Ch.6 實驗結果 | ⬜ 未開始 | | |
| Ch.7 結論 | ⬜ 未開始 | | |

狀態圖例：⬜ 未開始 / 🟡 進行中 / ✅ 初稿完成 / 🔵 修訂中 / ✔️ 定稿
