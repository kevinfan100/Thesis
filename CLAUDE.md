# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a LaTeX thesis template for National Tsing Hua University (NTHU) graduate students, specifically designed for the Department of Power Mechanical Engineering. The template supports bilingual content (Traditional Chinese and English) with proper font handling.

## Build Commands

Compile with XeLaTeX (required for Unicode/CJK support):
```bash
xelatex thesis.tex
bibtex thesis
xelatex thesis.tex
xelatex thesis.tex
```

For SVG support, use `--shell-escape`:
```bash
xelatex --shell-escape thesis.tex
```

Recommended environments: Overleaf, TeXLive, MikTeX, or MacTeX.

## Architecture

### Entry Point
- `thesis.tex` - Main document that imports all components

### Core Files
- `nthuthesis.cls` - Custom document class defining page layout, cover page format, and environments (abstracten/abstractzh, acknowledgementsen/acknowledgementszh)
- `nthuvars.tex` - Thesis metadata (title, author, advisor, dates) using bilingual syntax: `\title{English}{Chinese}`
- `IEEEtran_rchen.bst` - Custom IEEE bibliography style

### Content Organization
- `00_abstract.tex`, `00_acknowledgements.tex` - Front matter
- `01_introduction.tex` through `06_conclusion.tex` - Chapter files (add via `\input{}` in thesis.tex)
- `10_appendix.tex` - Appendix content
- `thesis.bib` - BibTeX bibliography database
- `figsrc/` - Image directory with chapter-based subdirectories (e.g., `figsrc/ch01/`)

### Fonts
- English: Times New Roman
- Chinese: kaiu.ttf (Kai font with AutoFakeBold/AutoFakeSlant)

## Key Patterns

### Bilingual References (cleveref)
The template uses Chinese formatting for cross-references:
```latex
\crefformat{figure}{圖~#2#1#3~}
\crefformat{table}{表~#2#1#3~}
\crefformat{chapter}{第#2\zhnumber{#1}#3章}
```

### Document Class Options
- Default: Master's thesis (`\@typezh{碩士}`)
- PhD: Use `\documentclass[phd]{nthuthesis}`
- Proposal: Use `\documentclass[proposal]{nthuthesis}`

### Page Layout
- Front matter: Single-sided, Roman numerals (i, ii, iii)
- Main matter: Double-sided, Arabic numerals
- Line spacing: 2.0 (main), 1.5 (TOC/lists)
- Margins: top 1in, left 3.17cm, bottom 1in, right 1in

### Adding Chapters
1. Create new `.tex` file (e.g., `02_methodology.tex`)
2. Add `\input{02_methodology}` in thesis.tex between `\mainmatter` and bibliography section

## 進階規則

本專案使用模組化規則系統，詳細規範請參見：

- **PDF 處理**：參見 @.claude/rules/pdf-handling.md
- **MCP 管理**：參見 @.claude/rules/mcp-management.md
- **大檔案處理**：參見 @.claude/rules/large-file-workflow.md
- **副產物管理**：參見 @.claude/rules/artifact-management.md
- **開發流程**：參見 @.claude/WORKFLOW.md

### 臨時檔案目錄

所有工具產出的臨時檔案放在 `.temp/` 目錄：
```
.temp/
├── pdf_extracted/    # PDF 提取文字
├── pdf_chunks/       # PDF 分割塊
└── matlab_output/    # MATLAB 臨時輸出
```

### 常用指令速查

| 指令 | 用途 |
|------|------|
| `/mcp` | 檢查 MCP 連接狀態 |
| `/context` | 檢查 token 使用量 |
| `/memory` | 查看載入的記憶檔案 |
| `/clear` | 清除對話歷史 |
