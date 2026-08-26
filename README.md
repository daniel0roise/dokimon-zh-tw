# Dokimon 繁體中文補丁（Traditional Chinese Fan Translation）

這是一個 **Dokimon 非官方繁體中文機翻／人工調整補丁**。目前版本以遊戲內 **Japanese 語言槽**載入繁中，角色、NPC、訓練家與 Dokimon 名稱盡量保留英文原名。

> 本專案不是 Dokimon 官方專案，也不包含完整遊戲檔案。你需要自行擁有正版 Dokimon。

## 目前版本

**v9 — 人名原文版**

- 12 份 Localization 全部繁體中文化
- 角色／NPC／訓練家人名保留英文原名
- Dokimon 種族名稱保留英文原名
- 已補入繁中文字形
- 英文與數字保留較接近原遊戲的比例字寬
- **HD Text 請關閉**（目前 HD Font 路徑會把繁中字縮得過小）

## 安裝方式

### 方法 1：一鍵安裝（推薦）

1. 從 GitHub 下載本 repo（Code → Download ZIP）並解壓縮。
2. 找到 Dokimon 遊戲資料夾。Steam 可用：
   `Dokimon → 內容/管理 → 瀏覽本機檔案`
3. 執行：

```bash
python tools/apply_patch.py "/path/to/Dokimon"
```

Windows 若 `python` 不可用，可嘗試：

```powershell
py tools\apply_patch.py "C:\path\to\Dokimon"
```

安裝器會：

- 驗證你的 `data.win` 是否為支援版本
- 自動備份原始 `data.win`
- 套用繁中文字型差分補丁
- 備份原 Japanese Localization
- 安裝繁中 Localization

### 方法 2：手動處理 Localization

`Localization/japanese/` 裡是完整繁中語系檔。僅複製它們可以載入翻譯文字，但 **若未套用 `data.win` 差分補丁，中文字可能顯示成 □**。

## 遊戲內設定

1. 語言選擇 **Japanese / 繁體中文**
2. **HD Text：OFF**

目前 v9 使用的是一般字型路徑；HD Text 開啟後會因遊戲原本的縮放邏輯讓中文字變得非常小。

## 支援的遊戲檔版本

本補丁只會修改 SHA-256 完全一致的原始 `data.win`，不同遊戲版本會直接停止，不會硬改：

```text
Original data.win SHA-256
1ee03ce65bb0eaa7a6cb8af90a1a6c266691c8b46e5b2d20123032f3f23806f5

Patched data.win SHA-256
77cc82e20de7e97f7cae6795e7f742bc8e1e03c51ba1095267b4171ec1b85235
```

若更新遊戲後無法安裝，請開 Issue 並附上新版 `data.win` 的 SHA-256。

## 還原

安裝器會建立：

```text
data.win.zhTW-backup
Localization/japanese.zhTW-backup/
```

可以用備份還原，或直接透過 Steam「驗證遊戲檔案完整性」。

## 專案內容

```text
Localization/japanese/     完整繁中翻譯
patches/                    data.win 二進位差分（不包含完整遊戲檔）
tools/apply_patch.py        差分安裝器
dist/                       可直接下載的補丁包
```

## 注意事項

- 翻譯主要由機器翻譯／AI 輔助產生，可能仍有語氣、術語或文字框長度問題。
- 若遇到錯字、翻譯不自然、文字超出 UI、缺字等問題，歡迎開 Issue 並附截圖與原句位置。
- 本 repo 不提供 Dokimon 本體或完整 `data.win`。
