# Dokimon 繁體中文補丁（Traditional Chinese Fan Translation）

這是一個 **Dokimon 非官方繁體中文翻譯補丁**。目前版本使用遊戲內 **Japanese 語言槽**載入繁中，角色、NPC、訓練家與 Dokimon 名稱保留英文原名。

> 本專案不是 Dokimon 官方專案。你需要自行擁有正版 Dokimon。

## 目前版本

**v9 — 人名原文版**

- 12 份 Localization 全部繁體中文化
- 角色／NPC／訓練家人名保留英文原名
- Dokimon 種族名稱保留英文原名
- 已補入繁中文字形
- 英文與數字使用較接近原遊戲的比例字寬
- **HD Text 請關閉**（開啟時繁中字會被遊戲原本的 HD 縮放邏輯縮得過小）

## 安裝

請到 **Releases** 下載：

`Dokimon_完整繁中補丁_v9_人名原文版.zip`

關閉遊戲後，將壓縮檔內的：

```text
data.win
Localization/
```

覆蓋到 Dokimon 遊戲根目錄。

建議先備份原本的：

```text
data.win
Localization/japanese/
```

進入遊戲後：

1. Language 選擇 **Japanese / 繁體中文**
2. **HD Text 設為 OFF**

## 還原

最簡單的方式是透過 Steam 執行「驗證遊戲檔案完整性」，或把你事先備份的 `data.win` 與 `Localization/japanese` 放回去。

## 翻譯說明

- 翻譯主要由 AI／機器翻譯協助產生，並針對遊戲控制碼、名稱一致性與部分 UI 進行調整。
- `/n/`、`/name/`、`/region/` 等遊戲控制碼均保留。
- 人物名字不翻譯，例如 `Rei`、`Aki`、`Yumeko` 等保持英文。
- `Professor Rei`、`Master Aki`、`Elite Battler Yumeko` 等姓名＋稱號也盡量維持英文原文。
- Dokimon 種族名稱保留英文。

## 已知問題

- **HD Text 必須關閉。** 目前遊戲的 HD Font 路徑會額外縮放文字，造成繁中文字過小。
- 少數句子可能仍有語氣不自然、文字框長度或 UI 排版問題。

如果遇到錯字、翻譯不自然、缺字、文字超出 UI 等問題，歡迎開 Issue，最好附上截圖。

##碎碎念
- **我是用Chatgpt做的** 所以如果有一些問題的話歡迎大家補強，我只是剛好領了這個限免遊戲，沒中文可以看小痛苦，覺得有60分的中文我就接受了。

## 版權說明

Dokimon 與其遊戲資產之權利歸原作者／權利人所有。本專案僅為非官方繁體中文 fan translation。
