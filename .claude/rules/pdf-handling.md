---
paths:
  - "*.pdf"
  - "Thesis/**/*.pdf"
  - "figsrc/**/*.pdf"
---

# PDF 處理規則

## 問題：PDF too large

Claude Code 原生 PDF 讀取限制：
- 官方限制：32MB / 100 頁
- 實際限制：約 10-15MB / 30-50 頁
- 觸發後會拒絕讀取任何 PDF

## 解決方案：使用 pdf-reader MCP

已安裝：`@fabriqa.ai/pdf-reader-mcp`

### 1. 檢查 MCP 狀態
```
/mcp
# 確認 pdf-reader 已連接
```

### 2. 提取 PDF 文字
```
請讀取這個 PDF 的內容：
/path/to/large-paper.pdf
```

### 3. 處理特定頁面
```
請讀取 PDF 的第 1-10 頁：
/path/to/document.pdf pages: "1-10"
```

### 4. 搜索 PDF 內容
```
在這個 PDF 中搜索 "magnetic actuator"：
/path/to/paper.pdf
```

### 5. 取得 PDF 元資料
```
請取得這個 PDF 的元資料：
/path/to/document.pdf
```

## 論文 PDF 處理工作流

### 閱讀參考文獻
1. 將 PDF 放入 `Thesis/references/` 目錄
2. 使用 pdf-extraction 提取全文
3. Claude 協助摘要重點
4. 記錄到 Memory 或 thesis.bib

### 處理教授回饋
1. 收到批註 PDF
2. 提取批註內容
3. 建立修改清單（使用 TodoWrite）
4. 逐項處理

## 備用方案：Python 腳本

當 MCP 無法使用時：

```python
# 執行此腳本提取 PDF 文字
import fitz  # PyMuPDF

def extract_pdf(path, output_path=None):
    doc = fitz.open(path)
    text = "\n".join(page.get_text() for page in doc)
    doc.close()

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
    return text

# 使用：extract_pdf("large.pdf", ".temp/pdf_extracted/output.txt")
```

然後讓 Claude 讀取 `.temp/pdf_extracted/output.txt`。

## 檔案大小判斷

```bash
# 檢查 PDF 大小
ls -lh path/to/file.pdf
```

| 大小 | 頁數 | 處理方式 |
|------|------|----------|
| < 5MB | < 30 頁 | 直接 Read |
| 5-15MB | 30-80 頁 | pdf-extraction MCP |
| > 15MB | > 80 頁 | Python 腳本 + 分割 |
