# MCP 管理規則

## Context Token 管理

### 目前 MCP 佔用（約 5.3k tokens）

| MCP Server | 用途 | Tokens | 常用程度 |
|------------|------|--------|----------|
| perplexity | 文獻搜索、最新研究 | ~1.0k | 中 |
| context7 | 查詢套件文檔 | ~0.9k | 低 |
| matlab | MATLAB 模擬 | ~0.8k | 高 |
| memory | 概念記憶 | ~1.0k | 中 |
| sequential-thinking | 複雜推理 | ~1.1k | 低 |
| pdf-reader | PDF 讀取/搜索 | ~0.5k | 高 |

### 動態管理 MCP

MCP 可隨時添加/移除（需重啟會話生效）：

```bash
# 移除不常用的 MCP
claude mcp remove <name>

# 需要時再添加
claude mcp add <name> -- <command>

# 查看目前 MCP
claude mcp list
```

### 按需添加指令速查

```bash
# 文獻搜索
claude mcp add perplexity -- npx -y @perplexity-ai/mcp-server

# LaTeX 文檔查詢
claude mcp add context7 -- npx -y @upstash/context7-mcp

# PDF 讀取
claude mcp add pdf-reader -- npx -y @fabriqa.ai/pdf-reader-mcp@latest
```

### 最佳實踐

1. **按需載入**
   - 文獻研究階段：perplexity, memory
   - 撰寫階段：context7, filesystem
   - 模擬階段：matlab
   - PDF 處理：pdf-reader

2. **定期清理**
   ```bash
   # 列出所有 MCP
   claude mcp list

   # 移除不常用的
   claude mcp remove <name>

   # 檢查健康狀態
   /mcp
   ```

3. **失敗處理**
   - 若 MCP 顯示 "Failed to connect"
   - 先執行 `claude mcp list` 確認狀態
   - 嘗試 `claude mcp remove <name>` 後重新添加

## 會話管理

### 開始新會話前
1. `/context` - 檢查 token 使用量
2. `/mcp` - 確認需要的 MCP 已連接
3. `/memory` - 確認記憶檔案已載入

### 長時間工作後
1. `/clear` - 清除對話歷史（保留記憶檔案）
2. 若 context 超過 60%，考慮開新會話

### 結束會話前
1. 確認工作已提交 git
2. 重要發現記錄到 Memory
3. 清理臨時檔案

## MCP 安裝指令速查

```bash
# 添加 MCP
claude mcp add <name> -- <command>

# 添加帶參數的 MCP
claude mcp add pdf-extraction -- npx -y @some/pdf-mcp

# 移除 MCP
claude mcp remove <name>

# 列出所有 MCP
claude mcp list
```

## 常用指令

| 指令 | 用途 |
|------|------|
| `/mcp` | 檢查 MCP 連接狀態 |
| `/context` | 檢查 token 使用量 |
| `/memory` | 查看載入的記憶檔案 |
| `/clear` | 清除對話歷史 |
