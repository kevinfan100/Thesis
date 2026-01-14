# 大型檔案處理工作流

## PDF 檔案（> 10MB 或 > 50 頁）

### 判斷檔案大小
```bash
ls -lh path/to/file.pdf
# 或
du -h path/to/file.pdf
```

### 處理流程

1. **小型 PDF（< 5MB, < 30 頁）**
   - 直接使用 Claude 的 Read 工具

2. **中型 PDF（5-15MB, 30-80 頁）**
   - 使用 pdf-extraction MCP
   - 指定需要的頁面範圍

3. **大型 PDF（> 15MB, > 80 頁）**
   - 先用 Python 腳本提取文字
   - 分割成多個 .txt 檔案
   - 逐個讓 Claude 閱讀

## 分割策略

### 論文分割
```
.temp/pdf_extracted/
├── paper_intro.txt      # 摘要、緒論（1-10 頁）
├── paper_methods.txt    # 方法（10-30 頁）
├── paper_results.txt    # 結果（30-60 頁）
├── paper_discussion.txt # 討論、結論（60-80 頁）
└── paper_appendix.txt   # 附錄、參考文獻
```

### 處理順序
1. 先讀 intro 了解主題
2. 按需讀取相關章節
3. 最後讀結論確認理解

## 分割腳本

```python
#!/usr/bin/env python3
"""將大型 PDF 分割成多個文字檔"""
import fitz
import os

def split_pdf(pdf_path, output_dir=".temp/pdf_extracted", pages_per_chunk=20):
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    os.makedirs(output_dir, exist_ok=True)

    for start in range(0, total_pages, pages_per_chunk):
        end = min(start + pages_per_chunk, total_pages)
        text = "\n\n".join(
            f"=== Page {i+1} ===\n{doc[i].get_text()}"
            for i in range(start, end)
        )

        chunk_file = f"{output_dir}/{base_name}_p{start+1:03d}-{end:03d}.txt"
        with open(chunk_file, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Created: {chunk_file}")

    doc.close()

# 使用：split_pdf("large_paper.pdf")
```

## 圖片處理

### 從 PDF 提取圖片
```python
import fitz
import os

def extract_images(pdf_path, output_dir=".temp/pdf_extracted/images"):
    doc = fitz.open(pdf_path)
    os.makedirs(output_dir, exist_ok=True)

    for page_num, page in enumerate(doc):
        for img_idx, img in enumerate(page.get_images()):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)

            if pix.n > 4:  # CMYK
                pix = fitz.Pixmap(fitz.csRGB, pix)

            output_file = f"{output_dir}/page{page_num+1}_img{img_idx+1}.png"
            pix.save(output_file)

    doc.close()
```

### 圖片檔案限制
- Claude 可直接讀取 < 20MB 的圖片
- 大圖先壓縮或降解析度

## 輸出位置

所有提取的檔案應放在 `.temp/` 目錄：
- `.temp/pdf_extracted/` - 文字提取
- `.temp/pdf_chunks/` - PDF 分割
- `.temp/pdf_extracted/images/` - 圖片提取

這些目錄已加入 `.gitignore`，不會提交到版本控制。
