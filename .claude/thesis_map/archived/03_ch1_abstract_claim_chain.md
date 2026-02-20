# Ch.1 and Abstract Claim Chain (Minimal-Change Strategy)

## Why this file

目的是確保 `00_abstract.tex` 與 `01_introduction.tex` 的每個主張都有章節證據，避免後續正文寫完才發現 claim 過強或無法驗證。

## Claim chain template

| Claim ID | Ch.1 location | Abstract sentence | Evidence chapter | Evidence type | Status |
|---|---|---|---|---|---|
| C1 | 研究背景/缺口 | 系統為三層控制且各層有不同控制挑戰 | Ch.1/Ch.2 | prior works + architecture fig | Ready |
| C2 | 貢獻 1 (ID) | 建立 6x6 鑑別流程並分析多配置模型品質 | Ch.3 | pipeline + fitting + comparison | Pending data selection |
| C3 | 貢獻 2 (flux ctrl) | PI 與 model-based 在組件層級有量化差異 | Ch.4 | bode + component ablation | Pending final figure set |
| C4 | 貢獻 3 (force gen) | Vd 排程與非線性傳遞影響力精度，可定量識別 | Ch.5 | schedule comparison + THD/force error | Pending final experiment |
| C5 | 貢獻 4 (implementation) | FPGA 實現與理論/模擬結果一致 | Ch.6 | sim-vs-hw comparison | Pending final exp summary |

## Minimal-change editing policy for current draft

1. 保留目前 Ch.1 的三層主軸敘事（已符合你的方向）。
2. 僅調整以下兩類句子：
   - 過強且暫無數據支持的句子。
   - 尚未與後續章節證據明確對應的句子。
3. Abstract 優先使用「已完成證據」；未完成結果用保守描述（例如 “analyzed” 而非 “demonstrated”）。

## Red-flag phrases to avoid until data is fixed

1. 「顯著提升」但無百分比或基準。
2. 「最佳」但未定義比較集合。
3. 「可泛化至任意系統」但未定義邊界條件。

## Recommended Ch.1 wording pattern

每段採固定邏輯：

1. 問題：此層控制面臨的物理與工程限制。
2. 既有方法：前人如何處理、留下什麼空間。
3. 本文切入：你要比較什麼、分析什麼。
4. 證據：本章/下章會給的量化指標。

## Next action before rewriting body text

1. 先鎖定 3 個主指標（建議：`bandwidth`, `force amplitude error`, `THD or coupling suppression`）。
2. 每個 Claim ID 指定 1 張主圖 + 1 張備援圖。
3. 再進行 Ch.1 / Abstract 的最小改動版修稿。
