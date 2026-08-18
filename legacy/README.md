# legacy — 舊版 8 章中文論文（唯讀素材）

## 這是什麼

2026 年 2 月之前，本論文採用自製的 `nthuthesis.cls`、8 章中文架構，入口為 `thesis.tex`。
2026 年 2 月下旬論文改用**清大 114 年官方模板**（`nthu_thesis.cls`）與**5 章英文**架構，
這批檔案自此停止維護。

保留的原因是 **Ch.1 的中文初稿仍有可回收的段落**，並非因為它還會被編譯。

## 不要做的事

- **不要編譯**。這些檔案已不在 `main.tex` 的 `\input` 路徑上，且 `nthuthesis.cls` 與現行
  官方 `.cls` 不相容。
- **不要修改**。要改內容請改 `contents/chapter0N.tex`。
- **不要從這裡新增引用**。現行唯一的 bib 是 `back/references.bib`；`legacy/thesis.bib`
  的 18 筆已全數併入（含 `tomizuka1987zpetc`、`xia1995precision` 兩筆 ZPETC 文獻）。

## 可回收的內容

| 檔案 | 大小 | 可用之處 |
|---|---|---|
| `01_introduction.tex` | 17 KB | 中文緒論初稿。含六極致動器結構描述、三層控制架構（100 kHz 磁通／10 kHz 力生成／1.6 kHz 運動）、前人貢獻回顧、內迴圈演進表。可作為中文摘要與口試簡報的素材 |
| `00_abstract.tex` | 4.2 KB | 中英摘要初稿 |
| `02~08_*.tex` | 各 &lt;1 KB | 僅章節骨架與 section 註解，記錄了當時的 8 章切分構想 |

## 完整歷史

舊架構的完整 git 歷史保存在分支 `legacy/main-8ch-chinese`：

```
git log legacy/main-8ch-chinese
git show legacy/main-8ch-chinese:01_introduction.tex
```

## 兩種架構的對應

| 舊（8 章中文） | 新（5 章英文） |
|---|---|
| 01 緒論 | ch01 Introduction |
| 02 系統建模 | ch02 System Overview |
| 03 系統鑑別 | ch03 System Identification of Magnetic Flux Generation Dynamics |
| 04 內迴圈磁通控制器 | ch04 Flux Control Design and Validation |
| 05 力生成控制 + 07 運動控制 + 08 結論 | ch05 Force Generation, Motion Control, and Conclusions |
| 06 FPGA 實現 | 併入 ch02 / ch04 |
