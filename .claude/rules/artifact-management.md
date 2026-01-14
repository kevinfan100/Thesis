# 副產物管理規則

## 目錄結構

### 臨時檔案目錄 `.temp/`

所有工具產出的臨時檔案應放在此目錄：

```
.temp/
├── pdf_extracted/    # PDF 提取文字
├── pdf_chunks/       # PDF 分割塊
└── matlab_output/    # MATLAB 臨時輸出
```

### 工具產出物對照

| 工具 | 副產物 | 存放位置 | 大小估計 |
|------|--------|----------|----------|
| PDF 提取（MCP） | 無（直接回傳） | - | - |
| PDF 提取（腳本） | `*_extracted.txt` | `.temp/pdf_extracted/` | 原 PDF 10-30% |
| PDF 分割（腳本） | `*.pdf` | `.temp/pdf_chunks/` | 每塊 1-5MB |
| MATLAB 執行 | `.mat`, `.fig` | `.temp/matlab_output/` | 變化大 |
| LaTeX 編譯 | `.aux`, `.log` 等 | 專案根目錄 | 約 100KB |

## 使用規範

### 1. PDF 提取時
```bash
# 輸出到臨時目錄
python extract_pdf.py paper.pdf --output .temp/pdf_extracted/
```

### 2. MATLAB 執行時
```matlab
% 設定輸出目錄
outputDir = '.temp/matlab_output/';
if ~exist(outputDir, 'dir'), mkdir(outputDir); end

% 儲存臨時結果
save([outputDir 'simulation_result.mat'], 'data');
```

### 3. 生成正式圖片時
```matlab
% 儲存到正式目錄（會提交 git）
saveas(gcf, 'figsrc/ch03/force_envelope.pdf');
```

## 清理指令

### 快速清理（保留最近 7 天）
```bash
find .temp -type f -mtime +7 -delete
```

### 完整清理
```bash
rm -rf .temp/*
```

### LaTeX 清理
```bash
latexmk -c  # 清理編譯產物
```

### 一鍵全清理
```bash
rm -rf .temp/* && latexmk -c
```

## 檔案大小監控

### 檢查臨時目錄大小
```bash
du -sh .temp/
du -sh .temp/*/  # 各子目錄大小
```

### 清理建議

| 條件 | 動作 |
|------|------|
| `.temp/` > 100MB | 執行快速清理 |
| `.temp/` > 500MB | 執行完整清理 |
| 論文提交前 | 執行完整清理 |
| 每章完成後 | 刪除該章臨時檔 |

## Claude 協助清理

當需要清理時，告訴 Claude：

```
請幫我清理 .temp 目錄中超過 7 天的檔案
```

```
請檢查臨時目錄大小，如果超過 100MB 就清理
```

```
請清理所有臨時檔案，準備提交論文
```

## 正式檔案 vs 臨時檔案

| 類型 | 位置 | 提交 git |
|------|------|----------|
| 正式圖片 | `figsrc/` | 是 |
| 正式資料 | `figsrc/matlab/` | 是（.mat） |
| 臨時提取 | `.temp/` | 否 |
| 參考文獻 PDF | `Thesis/references/` | 否 |
| LaTeX 編譯產物 | 根目錄 | 否 |
