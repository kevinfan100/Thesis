# 論文開發流程

## 開發週期

```
1. 規劃 → 2. 撰寫 → 3. 編譯 → 4. 版控 → 5. 審閱
```

### 1. 規劃階段
- 與 Claude 討論章節大綱
- 確定每章要點

### 2. 撰寫階段
- Claude 協助生成 LaTeX（表格、方程式、演算法）
- Claude 協助格式化 BibTeX 參考文獻

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

## MCP 工具使用指南

### 文獻研究
- `Perplexity research` - 深度研究某個主題
- `Perplexity search` - 搜索最新論文/技術
- `Memory` - 記錄重要文獻和概念關係

### MATLAB 模擬（如需要）
- `MATLAB run_matlab_file` - 執行完整模擬
- `MATLAB evaluate_matlab_code` - 快速測試程式碼
- `MATLAB check_matlab_code` - 檢查程式碼品質

### LaTeX 撰寫
- `Context7` - 查詢 LaTeX 套件用法
- `Filesystem` - 編輯 .tex 檔案

### 常用指令範例

**文獻搜索：**
```
請用 Perplexity 搜索 "topic keywords 2024" 的最新研究
```

**記錄概念：**
```
請用 Memory 記錄：
- 實體：概念名稱
- 類型：Algorithm/Method/Theory
- 觀察：簡要說明
```

**MATLAB 執行：**
```
請執行這段 MATLAB 程式碼：
[貼上程式碼]
```

**LaTeX 語法查詢：**
```
請用 Context7 查詢 algorithm2e 如何使用
```

---

## 待細化

- [ ] 章節命名約定（如 `02_methodology.tex`）
- [ ] 圖片命名與目錄結構
- [ ] 參考文獻工作流（Zotero? 手動?）
- [ ] 與指導教授的協作方式
- [ ] MATLAB 程式碼管理（如需要）
