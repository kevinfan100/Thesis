# AGENTS.md — 專案規則（唯一真相）

> 本檔為本專案規則的**唯一來源**。Codex 原生讀取 `AGENTS.md`；Claude Code 讀取
> `CLAUDE.md`，而 `CLAUDE.md` 僅一行 `@AGENTS.md` 匯入本檔。
> **不要在 `CLAUDE.md` 寫規則**，否則 Codex 看不到，兩邊必然漂移。

---

## 1. 這是什麼專案

清華大學動力機械工程學系碩士論文。

| 項目 | 值 |
|---|---|
| 作者 | 范宏翌 (Hung-Yi Fan)，學號 113033543 |
| 指導教授 | 孟嘉祥 博士 (Chia-Hsiang Menq) |
| 論文題目（中） | 六極電磁致動器控制系統設計與自動化之實驗驗證 |
| 論文題目（英） | Control-System Design and Automation for a Hexapole Electromagnetic Actuator with Experimental Validation |
| 本文語言 | **英文**（封面與摘要含中文） |
| 章節數 | **5 章** |
| 格式 | 清大 114 年官方模板 `nthu_thesis.cls` |
| 上游計畫 | 國科會 NSTC 114-2223-E-007-005（主持人：孟嘉祥） |

研究主題為六極電磁致動器在水溶液中對磁性微探針的超精密高速無繫繩操控。
論文主軸是**自動化**：把平台專屬的 know-how 轉成可重現、可移轉的開發流程。
（教授的四個關鍵字：自動化、簡化、泛化、參數化。出處見
`docs/research/nstc_project_report.md`。）

## 2. 編譯

入口是根目錄的 `main.tex`。直接：

```bash
latexmk          # 已在 .latexmkrc 設定 XeLaTeX + biber，預設編 main.tex
latexmk -c       # 清除輔助檔
```

手動鏈：`xelatex → biber → xelatex → xelatex`。

輔助檔（`.aux` `.log` `.toc` …）集中在 `build/`（`.latexmkrc` 的 `$aux_dir`），
`main.pdf` 與 `main.synctex.gz` 留在根目錄。`build/` 已 gitignore。

**必須用 XeLaTeX**（中文封面需要 xeCJK）。現況基準：**38 頁、18 筆 bib、0 未定義引用**。
任何改動後編譯結果若偏離此基準，先查清楚原因再繼續。

## 3. 目錄

```
main.tex              論文唯一入口
nthu_thesis.cls       官方 114 年格式 — 唯讀
2025Titlepage.tex     中文封面
kaiu.ttf              唯一需要的中文字型
contents/             ★ 論文本體 chapter01~05.tex
front/                摘要、致謝、符號列表、授權書
back/                 附錄、references.bib（唯一 bib）
figures/              ch01~ch05 分章存放
build/                編譯輔助檔（gitignored，可隨時整個刪掉）
docs/                 給人與 agent 讀的資料（不編譯）
  NOTATION.md         ★ 符號表
  research/           已驗證事實（唯讀）
  thesis_map/         章節定位與貢獻對照
  drafts/             寫作草稿
legacy/               舊 8 章中文版，唯讀素材，不編譯
refs/                 參考文獻 PDF（gitignored）
```

章節對應：

| 檔案 | 章名 |
|---|---|
| `contents/chapter01.tex` | Introduction |
| `contents/chapter02.tex` | System Overview |
| `contents/chapter03.tex` | System Identification of Magnetic Flux Generation Dynamics |
| `contents/chapter04.tex` | Flux Control Design and Validation |
| `contents/chapter05.tex` | Force Generation, Motion Control, and Conclusions |

## 4. 兩個 agent 怎麼分工

**同一個目錄、同一條分支、依階段接力。不要再開 worktree 並行。**
論文章節間符號與敘事高度耦合，平行寫不同章必然產生不一致——本專案 2026-02 的分岔
就是這樣造成的。

### 每章四段管線

| 段 | 誰 | 做什麼 | 產出 |
|---|---|---|---|
| 1 骨架 | **Claude Code** | 讀 `docs/research/` 對帳事實；定 section 結構、論證目標、公式、圖表清單；查原始碼確認數值 | 章節骨架：標題 + 公式 + `\label` + 圖表 placeholder + 每段一句 bullet |
| 2 散文 | **Codex** | 把 bullet 展開成英文學術散文 | 完整段落 |
| 3 收口 | **Claude Code** | 編譯、`\cref` 對照、bib key 檢查、符號比對 `docs/NOTATION.md` | 可編譯 PDF + 一致性報告 |
| 4 互審 | **交叉** | 上段誰動的另一個審 | 修訂清單 |

### 固定歸屬

| 工作 | 歸屬 |
|---|---|
| git 操作、分支、歷史 | Claude Code |
| 編譯鏈、`.cls`、`.latexmkrc` | Claude Code |
| MATLAB 生圖、資料處理 | Claude Code |
| `back/references.bib` 新增條目 | Claude Code |
| `docs/research/*` | Claude Code（唯一寫入者） |
| 中／英摘要、致謝 | Codex |
| 全文語氣統一、術語一致性掃描 | Codex |

## 5. Codex 禁區

以下**不要碰**：

- `nthu_thesis.cls`、`.latexmkrc` — 官方格式，改了會被系上退件
- `back/references.bib` — 引用正確性由 Claude Code 負責
- `docs/research/*` — 已驗證事實，唯讀
- `legacy/` — 唯讀素材
- `git rebase` / `reset` / `force push` / 任何歷史操作
- MATLAB 檔案與圖表生成

## 6. Codex 寫作硬規則

1. **只展開骨架 bullet。不新增事實、不改公式、不新增 `\cite`。**
2. 符號一律查 `docs/NOTATION.md`，**不自創**。表中沒有的先登錄再用。
3. 不確定的地方寫 `% TODO(codex): <問題>`，**不要自己編一個說法填掉**。
4. 收工前更新 `STATUS.md`。

第 3 條是最重要的一條。碩士論文最高成本的錯誤是假引用與假數值，不是句子不夠流暢。
把「不知道」外顯成可檢查的標記，比用流暢的文字蓋過去有價值得多。

## 7. 交接協定

`STATUS.md` 是接力棒。

- **開工前**：讀 `STATUS.md`，確認現在是哪一章、管線第幾段、輪到誰。
- **收工前**：更新 `STATUS.md`——做了什麼、下一棒是誰、有什麼待決。

任一時刻只有一個 agent 在動。交接全部走 git commit。

## 8. 慣例

**Git commit**：英文，格式 `type: description`（`feat` / `fix` / `docs` / `refactor` /
`chore` / `thesis` / `bib`）。訊息要說明**為什麼**，不只是做了什麼。

**LaTeX**：
- 交叉引用用 `\cref`，不要手寫「Chapter 3」
- 圖檔放 `figures/chNN/`，向量圖用 `.pdf`，照片用 `.png`
- `\label` 前綴：`c:` 章、`sec:` 節、`fig:` 圖、`tab:` 表、`eq:` 式

**對話輸出（僅限與作者對話，不影響 `.tex` 內容）**：
繁體中文，技術術語保留英文。不要用 LaTeX 數學語法，改用 Unicode 符號（∫ Σ ∂ α β θ ω → × ≈ ≤ ≥）。

**臨時檔**：一律放 `.temp/`，已 gitignore。

## 9. 不要重蹈的覆轍

這個 repo 在 2026-08 做過一次大整併，起因與教訓：

1. **不要把字型、參考文獻 PDF、編譯產物提交進 git。**
   曾有 118 MB 未使用中文字型與 37 MB 論文 PDF 進了歷史，`.git` 一度達 92 MB。
   `.gitignore` 對**已追蹤**的檔案無效——要先 `git rm --cached`。
2. **不要用 worktree 平行寫不同章。** 造成了 8 章中文版與 5 章英文版的分岔。
3. **不要留兩個 `.tex` 入口。** 曾有 `thesis.tex` 與 `main.tex` 並存，導致作者自己認不出專案現況。
4. **暫時關掉的東西要記得打開。** `\printbibliography` 曾被註解掉並標「temporarily
   disabled」，之後被遺忘。若必須暫時停用，同時在 `STATUS.md` 記一筆。

完整經過見 `docs/superpowers/specs/2026-08-18-project-consolidation-design.md`。
