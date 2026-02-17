# LaTeX 論文開發指南

> 本文件整合了 LaTeX 基礎知識和本專案的開發方法，供日常撰寫參考。

---

## 目錄

1. [專案檔案架構](#專案檔案架構)
2. [VSCode 編譯環境](#vscode-編譯環境)
3. [日常撰寫流程](#日常撰寫流程)
4. [LaTeX 常用語法](#latex-常用語法)
5. [數學方程式](#數學方程式)
6. [圖片](#圖片)
7. [表格](#表格)
8. [引用與參考文獻](#引用與參考文獻)
9. [演算法](#演算法)
10. [常見問題排解](#常見問題排解)

---

## 專案檔案架構

```
NTHU_template/
│
├── thesis.tex              ← 主文件（引入所有章節，通常不需修改）
├── nthuthesis.cls           ← 論文格式（頁面、封面、環境定義，勿修改）
├── nthuvars.tex             ← ★ 你的個人資訊（標題、姓名、日期）
├── thesis.bib               ← ★ 參考文獻資料庫
├── IEEEtran_rchen.bst       ← 參考文獻排版樣式（勿修改）
│
├── 00_abstract.tex          ← ★ 中英文摘要
├── 00_acknowledgements.tex  ← ★ 致謝
│
├── 01_introduction.tex      ← ★ Ch.1 緒論
├── 02_modeling.tex          ← ★ Ch.2 系統建模
├── 03_identification.tex    ← ★ Ch.3 系統鑑別
├── 04_flux_control.tex      ← ★ Ch.4 磁通控制器設計
├── 05_force_generation.tex  ← ★ Ch.5 力生成控制
├── 06_implementation.tex    ← ★ Ch.6 FPGA 實現與實驗
├── 07_motion_control.tex    ← ★ Ch.7 運動控制模擬
├── 08_conclusion.tex        ← ★ Ch.8 結論
├── 10_appendix.tex          ← ★ 附錄
│
├── figsrc/                  ← ★ 圖片目錄
│   ├── ch01/ ~ ch07/        ← 各章圖片（PDF 優先，PNG/JPG 次之）
│   └── nthu_logo*.png       ← 校徽（勿修改）
│
├── .vscode/settings.json    ← VSCode LaTeX Workshop 設定
└── .claude/                 ← Claude Code 設定（不影響論文）
```

**★ = 你需要編輯的檔案**

### 新增章節的步驟

1. 建立 `.tex` 檔案（如 `09_new_chapter.tex`）
2. 在 `thesis.tex` 中加入 `\input{09_new_chapter}`
3. 在 `figsrc/` 中建立對應的圖片目錄

---

## VSCode 編譯環境

### 已安裝的工具

- **TeX Live 2025**（包含 XeLaTeX、BibTeX、latexmk）
- **LaTeX Workshop** VSCode 擴充套件
- **XeLaTeX**：支援 Unicode/CJK 中文字體的編譯器

### 編譯方式

#### 自動編譯（預設）

**存檔 `Ctrl+S` / `Cmd+S` 即自動編譯**，使用 recipe：
```
xelatex → bibtex → xelatex → xelatex（四步完整編譯）
```

#### 手動觸發編譯

- `Cmd+Shift+P` → 輸入 `LaTeX Workshop: Build LaTeX project`
- 或點擊左側邊欄的 TEX 圖示 → 選擇 recipe

#### 切換 recipe

在 `.vscode/settings.json` 中有兩個 recipe：
- `xelatex -> bibtex -> xelatex x 2`：完整編譯（新增引用後使用）
- `xelatex (single)`：快速編譯（只改文字時使用）

若要改為存檔時只做快速編譯：
```json
"latex-workshop.latex.recipe.default": "xelatex (single)"
```

#### 終端機手動編譯

```bash
# 完整編譯
xelatex thesis.tex && bibtex thesis && xelatex thesis.tex && xelatex thesis.tex

# 快速編譯（只改文字）
xelatex thesis.tex
```

### PDF 預覽

- 存檔後自動在 VSCode 右側 tab 顯示 PDF
- 點擊 PDF 上的文字 → 跳到對應的 .tex 原始碼（SyncTeX）
- 點擊 .tex 原始碼 → `Cmd+Option+J` 跳到 PDF 對應位置

### 何時需要完整編譯？

| 修改內容 | 需要的步驟 |
|---------|-----------|
| 只改文字內容 | `xelatex` 一次 |
| 新增/修改 `\cite{}` | 完整四步（bibtex 需要更新） |
| 新增/修改 `\label{}` 和 `\cref{}` | `xelatex` 兩次 |
| 修改 `thesis.bib` | 完整四步 |
| 修改 `nthuvars.tex` | `xelatex` 一次 |

---

## 日常撰寫流程

### 典型工作流

1. 打開章節 `.tex` 檔
2. 寫內容（文字、方程式、圖片）
3. `Cmd+S` 存檔 → 自動編譯 → 右側 PDF 更新
4. 檢查 PDF 排版
5. 重複 2-4

### 有用的快捷鍵

| 快捷鍵 | 功能 |
|--------|------|
| `Cmd+S` | 存檔並編譯 |
| `Cmd+Option+J` | 從 .tex 跳到 PDF 對應位置 |
| `Cmd+B` | 切換側邊欄 |
| `Cmd+Shift+P` | 命令面板 |
| `Cmd+/` | 註解/取消註解選取行 |

### 用 Claude Code 協助撰寫

```bash
# 請 Claude 幫你寫某個 section
claude "請幫我撰寫 04_flux_control.tex 中 4.2 節 R-Controller 的推導"

# 請 Claude 幫你格式化方程式
claude "請把這個方程式轉成 LaTeX align 格式：F = g_phi * sum..."

# 請 Claude 幫你加入 BibTeX
claude "請幫我將這篇論文加入 thesis.bib：[貼上論文資訊]"

# 請 Claude 幫你產生圖表
claude "請用 MATLAB 計算六極磁場分布並輸出為 PDF 圖片"
```

---

## LaTeX 常用語法

### 文字格式

```latex
\textbf{粗體}
\textit{斜體}
\underline{底線}
\texttt{等寬字體（用於程式碼）}
```

### 段落與換行

```latex
% 新段落：空一行即可（會自動縮排）
第一段結束。

第二段開始，會自動縮排。

% 不縮排
\noindent 這行不會縮排。

% 強制換行（不建議常用）
第一行 \\
第二行
```

### 章節結構

```latex
\chapter{章標題}           % 第一章、第二章...
\section{節標題}           % 1.1、1.2...
\subsection{小節標題}      % 1.1.1、1.1.2...
\subsubsection{子小節標題} % 無編號，僅標題
```

### Label 與交叉引用

```latex
% 設定標籤（放在 chapter/section/figure/table/equation 後面）
\label{c:introduction}        % 章
\label{sec:background}        % 節
\label{fig:hexapole_geometry}  % 圖
\label{table:system_params}    % 表
\label{eqn:force_model}        % 方程式

% 引用（使用 cleveref，自動產生中文格式）
\cref{c:introduction}          % → 第一章
\cref{sec:background}          % → 1.1 節
\cref{fig:hexapole_geometry}   % → 圖 2.1
\cref{table:system_params}     % → 表 2.1
\cref{eqn:force_model}         % → (2.1) 式
```

### 列舉

```latex
% 有序列表
\begin{enumerate}[nosep]
\item 第一點
\item 第二點
\end{enumerate}

% 無序列表
\begin{itemize}[nosep]
\item 項目一
\item 項目二
\end{itemize}
```

---

## 數學方程式

### 行內公式

```latex
磁梯度力 $\mathbf{F} = \nabla(\boldsymbol{\mu} \cdot \mathbf{B})$ 驅動微珠運動。
```

### 獨立方程式（有編號）

```latex
\begin{align}
    \gamma \dot{\mathbf{p}}(t) = \mathbf{f}_m(\mathbf{p}(t), \mathbf{I}(t)) + \mathbf{f}_T(t)
    \label{eqn:langevin}
\end{align}
```

### 多行對齊方程式

```latex
\begin{align}
    x[k+1] &= x[k] + \frac{\Delta t}{\gamma} (f_d[k] + f_T[k])
    \label{eqn:discrete_motion} \\
    \delta x[k+1] &= \lambda_c \cdot \delta x[k] - \varepsilon[k]
    \label{eqn:error_dynamics}
\end{align}
```

### 矩陣

```latex
\begin{align}
    \mathbf{B} = \begin{bmatrix}
        b_{11} & b_{12} & \cdots & b_{16} \\
        b_{21} & b_{22} & \cdots & b_{26} \\
        \vdots & \vdots & \ddots & \vdots \\
        b_{61} & b_{62} & \cdots & b_{66}
    \end{bmatrix}
    \label{eqn:coupling_matrix}
\end{align}
```

### 常用數學符號速查

| 語法 | 結果 | 用途 |
|------|------|------|
| `\mathbf{F}` | **F** (粗體) | 向量/矩陣 |
| `\boldsymbol{\phi}` | φ (粗斜體) | 希臘字母向量 |
| `\hat{x}` | x̂ | 估測值 |
| `\dot{x}` | ẋ | 時間導數 |
| `\bar{x}` | x̄ | 平均值 |
| `\delta x` | δx | 微小變化 |
| `\Delta t` | Δt | 差值 |
| `\sum_{i=1}^{N}` | Σ | 求和 |
| `\frac{a}{b}` | a/b | 分數 |
| `\partial` | ∂ | 偏微分 |
| `\nabla` | ∇ | 梯度 |
| `\times` | × | 叉乘 |
| `\cdot` | · | 點乘 |
| `\leq`, `\geq` | ≤, ≥ | 不等式 |
| `\approx` | ≈ | 約等於 |
| `\pm` | ± | 正負 |
| `\infty` | ∞ | 無窮 |
| `\sqrt{}` | √ | 根號 |

### 物理單位（siunitx 套件）

```latex
工作空間半徑為 $\ell = \SI{500}{\micro\metre}$。
頻寬達 $\SI{4}{\kilo\hertz}$。
力精度約 $\SI{0.1}{\pico\newton}$。
```

---

## 圖片

### 單張圖片

```latex
\begin{figure}[htbp]
    \centering
    \includegraphics[width=0.8\textwidth]{figsrc/ch03/bode_mimo.pdf}
    \caption{6$\times$6 MIMO 系統開迴路 Bode 圖}
    \label{fig:bode_mimo}
\end{figure}
```

### 並排圖片（subfigure）

```latex
\begin{figure}[htbp]
    \centering
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{figsrc/ch04/bode_theory.pdf}
        \caption{理論預測}
        \label{fig:bode_theory}
    \end{subfigure}
    \hfill
    \begin{subfigure}[b]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{figsrc/ch04/bode_experiment.pdf}
        \caption{實驗量測}
        \label{fig:bode_experiment}
    \end{subfigure}
    \caption{閉迴圈磁通控制 Bode 圖：理論與實驗比較}
    \label{fig:bode_comparison}
\end{figure}
```

### 圖片格式建議

| 類型 | 格式 | 理由 |
|------|------|------|
| MATLAB 繪圖 | `.pdf` | 向量圖，縮放不失真 |
| 方塊圖 / 流程圖 | `.pdf` | 向量圖 |
| 硬體照片 | `.jpg` / `.png` | 點陣圖 |
| 螢幕截圖 | `.png` | 保留銳利邊緣 |

### MATLAB 輸出 PDF 圖片

```matlab
fig = figure;
% ... 繪圖 ...
exportgraphics(fig, 'figsrc/ch03/bode_mimo.pdf', 'ContentType', 'vector');
% 或
saveas(fig, 'figsrc/ch03/bode_mimo.pdf');
```

### 圖片位置參數

`[htbp]` 控制圖片擺放位置：
- `h` = here（當前位置）
- `t` = top（頁面頂部）
- `b` = bottom（頁面底部）
- `p` = page（獨立頁面）

建議使用 `[htbp]` 讓 LaTeX 自動選擇最佳位置。

---

## 表格

### 基本表格

```latex
\begin{table}[htbp]
\caption{系統物理參數}
\label{table:system_params}
\centering
\begin{tabular}{lcc}
\toprule
參數 & 數值 & 單位 \\
\midrule
工作空間半徑 $\ell$ & 500 & $\mu$m \\
探針半徑 $R$ & 2.25 & $\mu$m \\
線圈匝數 & 70 & -- \\
最大電流 & 3 & A \\
\bottomrule
\end{tabular}
\end{table}
```

### 表格線條

- `\toprule`：頂部粗線
- `\midrule`：中間細線
- `\bottomrule`：底部粗線
- `\hline`：一般水平線（較不美觀，盡量用 booktabs）

### 線上工具

推薦使用 [Tables Generator](https://www.tablesgenerator.com/latex_tables) 產生 LaTeX 表格程式碼。

---

## 引用與參考文獻

### BibTeX 工作流

1. **在 `thesis.bib` 中新增條目**
2. **在 `.tex` 中使用 `\cite{key}`**
3. **完整編譯**（需要 bibtex 步驟）

### 常見 BibTeX 條目格式

```bibtex
% 期刊論文
@article{meng2023ultraprecise,
  author  = {Meng, Ta-Min and Menq, Chia-Hsiang},
  title   = {Ultra-Precise High-Speed Untethered Manipulation...},
  journal = {IEEE/ASME Transactions on Mechatronics},
  year    = {2023},
  volume  = {28},
  number  = {1},
  pages   = {280--291}
}

% 博士論文
@phdthesis{long2016dissertation,
  author = {Long, Fei},
  title  = {Three-Dimensional Motion Control and...},
  school = {The Ohio State University},
  year   = {2016}
}

% 研討會論文
@inproceedings{some_conference,
  author    = {Author, First and Author, Second},
  title     = {Paper Title},
  booktitle = {Conference Name},
  year      = {2024},
  pages     = {100--110},
  address   = {City, Country, Month Day - Day}
}

% 書籍
@book{some_book,
  author    = {Author, Name},
  title     = {Book Title},
  publisher = {Publisher},
  year      = {2020}
}
```

### 引用語法

```latex
% 數字引用（本模板預設）
如文獻 \cite{meng2023ultraprecise} 所述...
多篇引用 \cite{meng2023ultraprecise, long2021optimal}

% 列出但不在文中顯示（放在參考文獻頁）
\nocite{some_reference}
```

### 取得 BibTeX 條目

1. **Google Scholar**：搜尋論文 → 點「引用」→ 選 BibTeX
2. **IEEE Xplore**：論文頁面 → Cite This → BibTeX
3. **請 Claude 幫忙**：貼上論文資訊，請 Claude 格式化

---

## 演算法

```latex
\begin{algorithm}[htbp]
\caption{R-Controller 計算流程}
\label{algo:r_controller}
\KwIn{$\mathbf{v}_d[k]$, $\mathbf{v}_m[k]$}
\KwOut{$\mathbf{u}[k]$}
\BlankLine

% Phase 1: Prefilter
$\mathbf{v}_f[k] \leftarrow \lambda_f \mathbf{v}_f[k-1] + k_{ff}\{b \cdot \mathbf{v}_d[k] + (1-\lambda_c b)\mathbf{v}_d[k-1] - \lambda_c \mathbf{v}_d[k-2]\}$\;

% Phase 2: Error calculation
$\delta\mathbf{v}[k] \leftarrow \mathbf{v}_f[k] - \mathbf{v}_m[k]$\;

% Phase 3: Disturbance estimation
$\hat{\mathbf{w}}[k] \leftarrow$ \text{EstimateDisturbance}($\delta\mathbf{v}[k]$)\;

% Phase 4: Feedback control
$\mathbf{u}_{fb}[k] \leftarrow (1-b_c)\mathbf{u}_{fb}[k-1] + b_c\mathbf{u}_{fb}[k-2] + k_u \cdot \mathbf{B}^{-1} \delta\mathbf{v}_c[k]$\;

\Return $\mathbf{u}[k] \leftarrow \mathbf{u}_{fb}[k]$
\end{algorithm}
```

---

## 常見問題排解

### 編譯錯誤

| 錯誤訊息 | 原因 | 解決方法 |
|---------|------|---------|
| `Undefined control sequence` | 使用了未定義的指令 | 檢查拼寫、確認套件已載入 |
| `Missing $ inserted` | 數學符號出現在文字模式 | 用 `$...$` 包住數學符號 |
| `File not found` | 圖片路徑錯誤 | 確認檔案在 `figsrc/` 中 |
| `Label multiply defined` | 重複的 label | 改成唯一的 label 名稱 |
| `Citation undefined` | cite key 不存在 | 確認 `thesis.bib` 中有該 key |
| `I found no \citation commands` | 文中沒有 `\cite{}` | 正常現象（骨架階段），加入引用後消失 |

### 清理編譯產物

```bash
# 刪除所有暫存檔
latexmk -c

# 或手動刪除
rm -f thesis.aux thesis.bbl thesis.blg thesis.log thesis.out thesis.toc thesis.lof thesis.lot thesis.synctex.gz
```

### 強制重新完整編譯

如果遇到交叉引用不正確或參考文獻編號異常：
```bash
latexmk -c && xelatex thesis.tex && bibtex thesis && xelatex thesis.tex && xelatex thesis.tex
```

### 中文字體問題

本模板使用 `kaiu.ttf`（楷體）作為中文字體。如果編譯報錯找不到字體：
```bash
# 確認字體已安裝
fc-list | grep kaiu
```

若未安裝，macOS 通常內建此字體。如仍有問題，將 `kaiu.ttf` 放在專案根目錄即可。

---

## 本專案特殊設定

### 頁面格式
- **前頁**（摘要、目錄）：單面列印、羅馬數字頁碼
- **正文**（Ch.1 起）：雙面列印、阿拉伯數字頁碼
- **行距**：正文 2.0、目錄 1.5
- **邊距**：上 1in、左 3.17cm、下 1in、右 1in

### 中文交叉引用格式（cleveref）

已在 `thesis.tex` 中設定：
```
圖 → 圖~X~
表 → 表~X~
章 → 第X章
節 → X 節
方程式 → (X) 式
```

### 圖表標題格式
- 圖標題在圖下方
- 表標題在表上方（floatrow 套件控制）

---

*最後更新：2026-02-17*
