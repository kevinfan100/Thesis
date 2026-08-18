# STATUS — 現在做到哪

> **開工前先讀這份。收工前一定要更新這份。**
> 這是兩個 agent 的接力棒，也是作者回到專案時唯一需要看的檔。

**最後更新**：2026-08-19 ｜ **更新者**：Claude Code

---

## 一句話現況

專案整併剛完成（結構、git、協作規範都已就緒）。**論文內容仍是骨架**——
Ch.1 有實質散文，Ch.2–5 只有 section 標題與少量段落，全書 **0 張圖**。

## 下一棒

**Claude Code，管線第 1 段（骨架），從 Ch.3 開始。**

理由：Ch.3 系統鑑別是你自己做的工作、有實驗 Bode 資料、且是 Ch.4 的前置。
先把它的骨架（section 結構、要證明什麼、公式、圖表清單）立起來，Codex 才有東西可展開。

## 章節進度

| 章 | 標題 | 大小 | section | 公式 | 引用 | 管線段 | 狀態 |
|---|---|---|---|---|---|---|---|
| 1 | Introduction | 10.7 KB | 3 | 0 | 10 | 2 完成 | 🟡 散文已成形，待第 3、4 段收口與互審 |
| 2 | System Overview | 5.3 KB | 6 | 2 | 0 | 1–2 之間 | 🟠 有段落但**零引用**，硬體參數需對帳 `docs/NOTATION.md` |
| 3 | System Identification | 5.7 KB | 6 | 2 | 0 | 1 未完成 | 🟠 **下一個要做的** |
| 4 | Flux Control | 4.7 KB | 6 | 0 | 0 | 1 未完成 | 🔴 骨架 |
| 5 | Force Gen + Motion + Conclusions | 2.3 KB | 6 | 0 | 0 | 1 未完成 | 🔴 最薄，且塞了三個主題 |

圖例：🔴 骨架 ／ 🟠 進行中 ／ 🟡 初稿 ／ 🟢 可送審

## 全書層級的缺口

| # | 缺口 | 嚴重度 | 備註 |
|---|---|---|---|
| 1 | **`figures/` 一張圖都沒有** | 高 | 五個 `chNN/` 子目錄都空的。控制論文沒有 Bode 圖、方塊圖、力包絡圖不成立 |
| 2 | **Ch.2–5 零引用** | 高 | 目前 18 筆 bib 只有 Ch.1 在用 |
| 3 | `front/Nomenclature.tex` 還是模板佔位 | 中 | 內容是光速與普朗克常數。應依 `docs/NOTATION.md` 重寫 |
| 4 | 中英摘要僅 1.2 / 1.4 KB | 中 | 內容待整併後重寫 |
| 5 | Ch.5 同時裝力生成、運動控制、結論 | 中 | 待確認是否維持 5 章，或結論獨立成 Ch.6 |

## 待作者決定

| # | 問題 | 卡住什麼 |
|---|---|---|
| 1 | `f_{B,f}` / `f_{B,c}` / `f_{B,e}` 三個頻寬參數的下標各代表什麼？ | `docs/NOTATION.md` §7 只能寫推測；Ch.4 無法展開 |
| 2 | 極間距 594 μm 與工作空間半徑 ℓ = 500 μm 的關係？ | `docs/NOTATION.md` §8；Ch.2 硬體描述無法定稿 |
| 3 | 結論要不要從 Ch.5 獨立出來成第 6 章？ | Ch.5 的骨架設計 |
| 4 | `codex/thesis-foundation-map-v1` 分支可否刪除？ | 它已 100% 含於 `main`，留著只會再造成混淆 |

## 最近做了什麼

**2026-08-18 ～ 08-19 — 專案大整併**（詳見
`docs/superpowers/specs/2026-08-18-project-consolidation-design.md`）

- 修好 2026-02 起的分支分岔：8 章中文版 vs 5 章英文版。**5 章英文版成為主線**
- 官方 114 年模板從 70 字元長的子目錄升到根目錄，`main.tex` 成為唯一入口
- 舊 8 章中文版移入 `legacy/`（唯讀），完整歷史保存在 `legacy/main-8ch-chinese` 分支
- 重寫 git 歷史剷除 118 MB 未使用字型與 37 MB 論文 PDF：`.git` 92 MB → **3.8 MB**
- 移除 worktree 並行模式，改為單目錄單主線接力
- 國科會計畫報告 NSTC 114-2223-E-007-005 納入 `docs/research/`
- 建立 `AGENTS.md`、`docs/NOTATION.md`、本檔

## 環境備忘

```bash
latexmk        # 編譯，基準：38 頁、18 筆 bib、0 未定義引用
latexmk -c     # 清輔助檔
```

- 兩個 agent 都開 `/Users/kevin/Code/NTHU_template`，**不要再開 worktree**
- Codex 啟動：`codex --profile thesis`
- 備份：`~/Code/_backup/NTHU_template_20260818/`（整併前的完整鏡像）
