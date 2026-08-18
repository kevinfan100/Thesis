# 專案整併設計書：碩士論文 repo 重整與雙 agent 協作規範

- 日期：2026-08-18
- 作者：范宏翌（Kevin Fan）／Claude Code 協作
- 狀態：待審閱

---

## 1. 問題陳述

專案在 2026-02 之後分岔成兩個互不相容的論文版本，且維護文件（`CLAUDE.md`、`WORKFLOW.md`、auto-memory）全部停留在舊版本的描述，導致作者重新開啟專案時無法辨識現況。

### 1.1 兩個分岔版本

| | `main` | `codex/thesis-foundation-map-v1` |
|---|---|---|
| 工作目錄 | `/Users/kevin/Code/NTHU_template` | worktree `/Users/kevin/Code/worktrees/ch1-worktree` |
| 入口 | `thesis.tex` | `NTHU_.../main.tex` |
| 格式 | `nthuthesis.cls`（舊版自製） | `nthu_thesis.cls`（官方 114 年） |
| 結構 | 8 章中文 `01~08_*.tex` | 5 章英文 `contents/chapter01~05.tex` |
| 內容 | Ch.1 中文 17 KB | Ch.1~5 英文約 29 KB |
| 敘事 | layer-by-layer 逐層分析 | dual-pillar／automation-first |
| 分岔點 | `34dc6fb` | 同左 |

`main` 領先兩個 commit（`45f502f`、`1668f07`），內容是把官方模板加入 repo 並對齊格式。
`codex` 分支領先十個 commit，是實際的論文重構工作。

### 1.2 僅存在於 codex 分支的資產

`main` 完全沒有這些檔案，一旦分支被誤刪即永久遺失：

- `.claude/thesis_map/CH1_MASTER_BRIEF.md`
- `.claude/thesis_map/archived/00_project_understanding.md`
- `.claude/thesis_map/archived/01_prior_vs_contribution_matrix.md`
- `.claude/thesis_map/archived/02_outline_recommended.md`
- `.claude/thesis_map/archived/03_ch1_abstract_claim_chain.md`
- `.claude/thesis_map/archived/04_work_mode_and_branch_plan.md`
- `.claude/thesis_map/archived/05_evidence_inventory_by_chapter.md`
- `.claude/ch1_review/CH1_1_1_FULL_DRAFT_EN_ZH.md`
- `.claude/ch1_review/paper_refs/*.txt`（三篇論文的提取文字）

### 1.3 未提交且未進版控的工作

worktree `/Users/kevin/Code/worktrees/ch1-worktree` 目前有：

- 已修改未提交：`contents/chapter01.tex`、`chapter02.tex`、`chapter04.tex`、`chapter05.tex`、`back/references.bib`、`thesis.bib`（共 6 檔，+84/−34 行）
- 完全未追蹤：`.claude/drafts/ch1_1_draft.md`（6.5 KB）、`.claude/drafts/ch1_structure_terms_v1.md`（3.8 KB）

### 1.4 倉庫衛生問題

| 問題 | 具體事實 |
|---|---|
| 倉庫過大 | `.git` 92 MB（全為 loose object，未 gc）、工作目錄 270 MB |
| 未使用字型入庫 | `fonts/chinese/` 114 MB（Kaiti-Black 37M、Kaiti-Bold 36M、Kaiti 28M、WHZ_Kai-Bold 8.2M、BiauKai 4.9M）+ `fonts/english/` 4.2 MB。經查 `nthu_thesis.cls:42,48` 僅使用 `\setmainfont{Times New Roman}`（系統字型）與 `\setCJKmainfont{kaiu.ttf}`，整個 `fonts/` 目錄零引用 |
| 編譯產物入庫 | `thesis.pdf`、`main.pdf` 被追蹤，每次編譯產生假 diff |
| 死圖檔 | `figsrc/ch01/` 內為原模板 demo 圖（taiwan_population、eurobot、high_income_population），全文 `\includegraphics` 引用數為 0；`figures/I2adsorption.png`、`ReactProbability.png` 為化學系範例圖 |
| 字型重複 | `kaiu.ttf` 存在 2 份、`Times New Roman.ttf` 存在 2 份 |
| 雜物 | `.DS_Store`、`.claude/settings.local.json.bak`、`Thesis/getPDF.jsp`（重複下載檔）、`.claude/recovery_snapshots/` 120 MB（已 gitignore） |
| 文件失準 | `CLAUDE.md` 記載 `02_literature.tex`（實為 `02_modeling.tex`）；`WORKFLOW.md` 進度表全標「未開始」但 Ch.1 已有初稿；auto-memory 指向不存在的 `.claude/plans/deep-popping-lagoon.md` |

### 1.5 協作規範缺失

- 專案無 `AGENTS.md`；`~/.codex/AGENTS.md` 為 0 bytes 空檔。Codex 進入此專案時無法取得 `CLAUDE.md` 的任何規則。
- 無符號表（notation）單一真相，兩個 agent 各自定義符號。
- 無狀態檔，作者與 agent 皆無法快速判斷「現在做到哪」。

**結論：1.5 是 1.1 的成因。** 缺乏交接契約導致兩個 agent 各自演化出不相容的論文結構。

---

## 2. 已定決策

| 編號 | 決策 | 值 |
|---|---|---|
| D1 | 論文主線版本 | **5 章英文官方模板**（codex 分支內容） |
| D2 | 論文主體語言 | **英文本文 + 中文封面** |
| D3 | 舊 8 章中文版處置 | 移入 `legacy/`，唯讀素材，不編譯 |
| D4 | 並行模式 | **廢除 worktree 並行**，改為單目錄單分支接力 |
| D5 | 規則檔真相來源 | `AGENTS.md` 為唯一真相，`CLAUDE.md` 以 `@AGENTS.md` 匯入 |

### 待確認決策

| 編號 | 決策 | 選項 | 建議 |
|---|---|---|---|
| **D6** | git 歷史是否重寫以移除 114 MB 字型 | (a) `git filter-repo` 重寫 + force push，`.git` 降至個位數 MB (b) 僅在新 commit 移除，歷史保留 92 MB | 傾向 (a)。作者為唯一 contributor、無協作者、遠端僅 `origin/main`，force push 風險低。執行前先完整鏡像備份 |

---

## 3. 目標架構

```
NTHU_template/
├── main.tex                    論文唯一入口
├── nthu_thesis.cls             官方 114 年格式（唯讀）
├── 2025Titlepage.tex           中文封面
├── kaiu.ttf                    唯一需要的中文字型
├── references.bib              單一 bib
├── .latexmkrc  .gitignore
│
├── front/                      C_Abstract / Eng_Abstract / acknowledgement
│                               / Nomenclature / 授權書 / 審定書
├── contents/                   ★ 論文本體
│   ├── chapter01.tex   Introduction
│   ├── chapter02.tex   System Overview
│   ├── chapter03.tex   System Identification of Magnetic Flux Generation Dynamics
│   ├── chapter04.tex   Flux Control Design and Validation
│   └── chapter05.tex   Force Generation, Motion Control, and Conclusions
├── back/                       appendix01.tex / appendix02.tex
├── figures/                    ch01/ ch02/ ch03/ ch04/ ch05/
│
├── AGENTS.md                   ★ 專案規則唯一真相
├── CLAUDE.md                   單行 `@AGENTS.md`
├── STATUS.md                   ★ 交接儀表板
│
├── docs/
│   ├── NOTATION.md             符號表
│   ├── research/
│   │   ├── foundation.md       已驗證物理理解（原 research_foundation.md）
│   │   ├── menq_papers.md      12 篇論文分析
│   │   ├── nstc_project.md     ★ 國科會計畫報告（動機章節權威依據）
│   │   └── papers_extracted/   論文提取文字（原 .claude/ch1_review/paper_refs）
│   ├── thesis_map/             定位文件（原 codex 分支 thesis_map）
│   ├── drafts/                 寫作草稿（原 .claude/drafts）
│   ├── latex-guide.md
│   └── superpowers/specs/      設計文件（本檔所在）
│
├── legacy/                     舊 8 章中文版（唯讀，附 README 說明）
├── refs/                       參考文獻 PDF（gitignored）
└── .temp/                      工具暫存（gitignored）
```

### 3.1 設計原則

1. **單一入口**：根目錄只有一個 `main.tex`。目前 `thesis.tex` 與 `main.tex` 並存是「打開專案認不得」的直接成因。
2. **官方模板升為主體**：不再埋在 70 字元長的子目錄。
3. **參考資料與論文本體分離**：`docs/` 是給人與 agent 讀的，`contents/` 是要編譯的。
4. **舊版保留但隔離**：`legacy/` 不進編譯路徑，但保留 Ch.1 中文稿 17 KB 供回收。

### 3.2 刪除清單

| 對象 | 大小 | 理由 |
|---|---|---|
| `fonts/chinese/`、`fonts/english/` | 118 MB | `.cls` 零引用，實測確認 |
| `figsrc/` 全部 | 1.7 MB | 原模板 demo 圖，全文零 `\includegraphics` 引用 |
| `figures/I2adsorption.png`、`ReactProbability.png` | 1.7 MB | 化學系範例圖 |
| `.claude/recovery_snapshots/` | 120 MB | 字型的重複快照，已 gitignore |
| `thesis.tex`、`nthuthesis.cls`、`01~08_*.tex`、`00_*.tex`、`10_appendix.tex`、`nthuvars.tex`、`IEEEtran_rchen.bst` | — | **移入 `legacy/`**（唯讀素材） |
| `thesis.pdf`、`nthu_thesis_template_mod.pdf`、`main.pdf` | — | **刪除**（編譯產物／舊模板輸出） |
| 所有編譯產物 | — | `.aux .log .toc .lof .lot .bbl .blg .fls .fdb_latexmk .xdv .synctex.gz .glo .ist .nlo .out .run.xml` |
| `.DS_Store`、`*.bak`、`Thesis/getPDF.jsp`、`NTHU_worktrees.code-workspace` | — | 雜物 |

---

## 4. 分工模型

### 4.1 分工軸線：階段，不是章節

論文章節之間符號、cross-reference、敘事高度耦合。兩個 agent 在不同 worktree 平行寫不同章，必然產生術語與符號不一致，且 `.tex` merge 成本極高——本專案的分岔正是此模式的結果。

改採：**同一目錄、同一分支、依階段接力**。交接介面為 git commit 與 `STATUS.md`。

### 4.2 每章四段管線

| 段 | 執行者 | 工作 | 產出 |
|---|---|---|---|
| 1 骨架 | **Claude Code** | 讀 `docs/research/foundation.md` 對帳事實；定 section 結構、論證目標、公式、圖表清單；查 MATLAB／FPGA 原始碼確認數值為真 | `contents/chapterNN.tex` 骨架：章節標題 + 公式 + `\label` + 圖表 placeholder + 每段一句 bullet |
| 2 散文 | **Codex** | 將 bullet 展開為英文學術散文。**不新增事實、不改公式、不新增 `\cite`** | 同檔案，完整段落 |
| 3 收口 | **Claude Code** | XeLaTeX 編譯；`\cref` 對照；bib key 檢查；符號比對 `docs/NOTATION.md`；圖檔路徑 | 可編譯 PDF + 一致性報告 |
| 4 互審 | **交叉** | 上段誰動的另一個審。Codex 審英文與敘事流暢度；Claude Code 審事實、公式、引用真偽 | 修訂清單 |

第 2 段的三個禁令是本設計的核心：Codex 取得的是**已查核骨架**，其職責為語言而非內容，將編造事實的空間壓至最低。碩士論文最高成本的錯誤是假引用與假數值，而非句子不夠流暢。

### 4.3 固定歸屬

| 工作 | 歸屬 |
|---|---|
| git 操作、分支、歷史 | Claude Code |
| XeLaTeX 編譯鏈、`.cls`、`.latexmkrc` | Claude Code |
| MATLAB 生圖、資料處理 | Claude Code |
| `references.bib` 新增條目 | Claude Code |
| `docs/research/*` | Claude Code（唯一寫入者） |
| 中／英摘要、致謝 | Codex |
| 全文語氣統一、術語一致性掃描 | Codex |

### 4.4 交接契約三檔

1. **`AGENTS.md`** — 規則唯一真相，含 Codex 禁區清單。
2. **`docs/NOTATION.md`** — 符號表。新增符號須先入表再使用。
3. **`STATUS.md`** — 接力棒。**收工前必須更新**：目前章節、管線段數、下一棒執行者、待決事項。

### 4.5 日常循環

```
讀 STATUS.md          → 知道現在是 chNN 第 k 段
Claude Code 執行第 1 段 → commit → 更新 STATUS.md（下一棒 Codex）
codex --profile thesis → 讀 AGENTS.md + STATUS.md → 第 2 段 → commit → 更新 STATUS.md
Claude Code 執行第 3、4 段 → 回報
```

任一時刻僅一個 agent 作動，交接全走 git commit，可追溯且不再分岔。

---

## 5. 執行計畫

### Phase 0 — 搶救（最高優先，不可跳過）

目標：確保沒有任何工作在後續操作中遺失。

1. 建立完整鏡像備份至專案外：`git clone --mirror` + 工作目錄 `rsync`，存放於 `~/Code/_backup/NTHU_template_20260818/`
2. 在 worktree 提交所有未提交改動（6 個已修改檔）
3. 將 `.claude/drafts/` 兩份草稿加入版控並提交
4. 將 `~/Downloads/國科會計畫補助專題研究計畫報告.md`（30 KB）、`.pdf`（39 MB）、`hexapole_force_model_and_optimal_flux_allocation.md`（18 KB）、`研究獎助生學習計畫書.pdf` 複製進專案（`.md` 進版控，`.pdf` 進 `refs/` 並 gitignore）
5. 推送 codex 分支至 origin 作為異地備份

**回退點**：本階段結束後，所有資產至少存在兩份。後續任何步驟出錯皆可從鏡像還原。

### Phase 1 — 定主線

1. 將 `codex/thesis-foundation-map-v1` 合入 `main`（採其內容為準，保留 main 領先的兩個 commit 中的官方模板檔）
2. 移除 worktree：`git worktree remove`
3. 刪除 `NTHU_worktrees.code-workspace`
4. 驗證：`main` 上 `NTHU_.../main.tex` 可用 XeLaTeX 編譯成功

### Phase 2 — 瘦身

1. `git rm -r --cached` 移除 `fonts/`、編譯產物、`thesis.pdf`、`main.pdf`、demo 圖
2. 檔案系統刪除 `fonts/`、`figsrc/`、`.claude/recovery_snapshots/`、雜物
3. 重寫 `.gitignore`（補上 `main.pdf`、`*.glo`、`*.ist`、`*.nlo`、`missfont.log`、`.claude/settings.local.json*`）
4. `git gc --aggressive --prune=now`
5. 驗證：刪除 `fonts/` 後 XeLaTeX 仍能編譯成功（確認字型確實未使用）
6. **【D6 待確認】** 若採重寫歷史：`git filter-repo --path fonts/ --invert-paths` 後 force push

**回退點**：Phase 2 步驟 5 若編譯失敗，從備份還原 `fonts/` 並改為保留必要字型。

### Phase 3 — 重整目錄

1. 官方模板內容提升至根目錄（`git mv`，保留檔案歷史）
2. 舊 8 章中文版移入 `legacy/`，撰寫 `legacy/README.md` 說明來由與可回收段落
3. `.claude/*.md` 遷至 `docs/`，`thesis_map`、`ch1_review`、`drafts` 一併遷入
4. `Thesis/` 更名 `refs/`
5. 合併 `thesis.bib` 與 `back/references.bib` 為根目錄 `references.bib`，比對重複 key
6. `figures/` 建立 `ch01~ch05` 子目錄
7. 驗證：`latexmk` 全新編譯成功，頁數與 Phase 1 一致

### Phase 4 — 建立交接契約

1. 撰寫 `AGENTS.md`（含 Codex 禁區清單與寫作硬規則）
2. `CLAUDE.md` 改為單行 `@AGENTS.md`
3. 從 `nthu_thesis.cls`、既有章節、`front/Nomenclature.tex` 抽取符號，建立 `docs/NOTATION.md`
4. 建立 `STATUS.md`
5. `~/.codex/config.toml` 加入 `[profiles.thesis]`

### Phase 5 — 文件對齊

1. 依實際結構重寫 `AGENTS.md` 的專案說明段落
2. 更新 auto-memory（`/Users/kevin/ClaudeVault/auto-memory/nthu-template/`）：修正章節表、移除不存在檔案的指向、記錄 D1~D6 決策
3. 刪除或改寫 `.claude/WORKFLOW.md`（其進度表已失準）
4. 驗證：全新 clone 後可直接 `latexmk` 成功

---

## 6. AGENTS.md 內容規格

### 6.1 Codex 禁區

```
- nthu_thesis.cls / .latexmkrc（官方格式，變更將導致系上退件）
- references.bib（引用正確性由 Claude Code 負責）
- docs/research/*（已驗證事實，唯讀）
- git rebase / reset / force push / 任何歷史操作
- legacy/（唯讀素材）
- MATLAB 檔案與圖表生成
```

### 6.2 Codex 寫作硬規則

```
- 僅展開骨架 bullet，不新增事實、不改公式、不新增 \cite
- 符號一律查 docs/NOTATION.md，不自創
- 不確定處寫 % TODO(codex): <問題>，不得自行編造說法填補
- 收工前更新 STATUS.md
```

最後一條是 LLM 撰寫學術文件時最有效的單一防線：將「不知道」外顯為可檢查的標記，而非被流暢的文字掩蓋。

### 6.3 檔案格式選擇說明

`AGENTS.md` 為真相來源而非 `CLAUDE.md`，原因：Claude Code 支援 `@檔名` 匯入語法，Codex 不支援。真相必須置於 Codex 原生讀取的檔案，由 Claude Code 匯入。反向設計會使 Codex 僅讀到一行指標。

不使用 symlink：作者的 `ClaudeVault` 經 Obsidian Sync 跨 Mac/Windows 同步，symlink 在 Windows 端失效。

---

## 7. 風險

| 風險 | 影響 | 緩解 |
|---|---|---|
| 合併分支時遺失內容 | 高 | Phase 0 完整鏡像備份；合併後逐檔比對行數 |
| 刪除字型後編譯失敗 | 中 | Phase 2 步驟 5 明確驗證；失敗即從備份還原 |
| 重寫歷史後遠端不一致 | 中 | 僅單一 contributor；先鏡像備份再 force push |
| `git mv` 大量搬移後 cross-reference 失效 | 中 | Phase 3 每步後編譯驗證 |
| bib 合併產生重複或衝突 key | 中 | 合併前列出兩檔 key 交集，逐一裁決 |
| 兩個 agent 未遵守 STATUS.md 更新 | 中 | 寫入 AGENTS.md 硬規則；作者每次開工先讀 STATUS.md 即可察覺 |

---

## 8. 驗收標準

1. 全新 `git clone` 後，執行 `latexmk` 一次成功產出 PDF
2. `.git` 體積：採 D6(a) 則小於 10 MB；採 D6(b) 則不再成長
3. `git status` 在編譯後保持乾淨（無編譯產物出現）
4. 根目錄僅一個 `.tex` 入口
5. `STATUS.md` 能在 30 秒內讓作者判斷「現在做到哪、下一步是誰做什麼」
6. Phase 0 清單中每一項資產皆可在新結構中定位
7. Codex 以 `--profile thesis` 啟動後，能正確讀到 `AGENTS.md` 的禁區清單

---

## 9. 附錄：關鍵事實出處

| 事實 | 驗證方式 |
|---|---|
| 字型未被使用 | `grep -nE 'setCJKmainfont|setmainfont' nthu_thesis.cls` → 僅 `Times New Roman`（系統字型）與 `kaiu.ttf` |
| 圖檔未被引用 | `grep -rnoE 'includegraphics' *.tex` → 空 |
| 分岔點 | `git merge-base main codex/thesis-foundation-map-v1` → `34dc6fb` |
| `.git` 體積 | `git count-objects -vH` → 91.77 MiB，全為 loose object |
| Codex 設定 | `codex-cli 0.146.0`、`gpt-5.6-terra`、`model_reasoning_effort = "high"`、專案 `trust_level = "trusted"`、`~/.codex/AGENTS.md` 為 0 bytes |
| 國科會計畫 | NSTC 114-2223-E-007-005，主持人孟嘉祥，執行期間 2025/02/01–2026/01/31，16 頁 |
