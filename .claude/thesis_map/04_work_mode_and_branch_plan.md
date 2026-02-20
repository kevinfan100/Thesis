# Work Mode and Branch Plan

## Current setup (already created)

1. Main branch (untouched working line):  
   `/Users/kevin/Code/NTHU_template` on `main`
2. Dedicated branch for thesis foundation work:  
   `codex/thesis-foundation-map-v1`
3. Dedicated worktree (isolated workspace):  
   `/tmp/thesis-foundation-map-v1`

## Why this setup

1. 不干擾你主線上正在進行的 Claude 工作。
2. 可以先產出 foundation 文件，再決定是否要合併正文修改。
3. 便於你做差異審閱（只看這個分支新增文件即可）。

## Suggested next branch sequence

1. `codex/thesis-foundation-map-v1`  
   產出：理解文件、對照矩陣、outline、claim chain（目前分支）
2. `codex/ch1-abstract-polish-v1`（從 foundation 分支切）  
   產出：最小改動版 Ch.1 + Abstract
3. `codex/ch3-id-writing-v1`（可選）  
   產出：Ch.3 由 pipeline 與實驗證據回填正文

## Merge strategy

1. 先審閱 foundation 文件是否準確描述你的研究定位。
2. 只在你確認後，才開正文修稿分支。
3. 每次只處理一個論文目標（避免大範圍難回退）。
