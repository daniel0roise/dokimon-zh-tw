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

## 安裝方法

### 1. 下載補丁

請到右側的 **Releases** 下載：

`Dokimon_zh-TW_v9_names-original_patch.zip`

下載後先把 ZIP **完整解壓縮**，不要直接在壓縮檔裡執行程式。

> 這個 ZIP **不包含完整的 `data.win`**。裡面只有繁中 Localization、字型用的二進位差分檔，以及套用差分的 Python 工具。你必須自行擁有正版 Dokimon。

### 2. 找到 Dokimon 遊戲資料夾

如果你是 Steam 版：

1. Steam 遊戲庫中對 **Dokimon** 按右鍵
2. 選擇 **管理（Manage）**
3. 選擇 **瀏覽本機檔案（Browse local files）**

打開後的資料夾裡應該可以直接看到：

```text
data.win
Localization/
```

這一層就是等等要指定的 Dokimon 遊戲資料夾。

### 3. 安裝 Python 3

補丁安裝器只使用 Python 內建功能，不需要另外安裝套件。

先確認電腦有 Python 3：

Windows：

```powershell
py --version
```

Linux / macOS：

```bash
python3 --version
```

如果有顯示 Python 3.x.x 就可以繼續。

### 4. 執行補丁

先在終端機 / PowerShell 進入你剛剛解壓縮的補丁資料夾。

#### Windows

```powershell
py tools\apply_patch.py "C:\你的\Dokimon\遊戲資料夾"
```

例如 Steam 安裝在預設位置時可能會像：

```powershell
py tools\apply_patch.py "C:\Program Files (x86)\Steam\steamapps\common\Dokimon"
```

#### Linux

```bash
python3 tools/apply_patch.py "/你的/Dokimon/遊戲資料夾"
```

#### macOS

```bash
python3 tools/apply_patch.py "/你的/Dokimon/遊戲資料夾"
```

如果你已經把整個補丁資料夾放進 Dokimon 遊戲根目錄，也可以在補丁目錄中直接執行並把遊戲路徑指定成 `.`：

```bash
python3 tools/apply_patch.py .
```

Windows 則是：

```powershell
py tools\apply_patch.py .
```

### 5. 安裝器會做什麼？

安裝器會先檢查你的原始 `data.win` 是否為目前支援的版本，不符合就會直接停止，不會硬改檔案。

成功時它會自動：

1. 備份原本的 `data.win` 為：

```text
data.win.zhTW-backup
```

2. 對你自己的正版 `data.win` 套用繁中文字型差分
3. 驗證修改後檔案是否正確
4. 備份原本的 Japanese 語系資料夾為：

```text
Localization/japanese.zhTW-backup/
```

5. 將完整繁中翻譯安裝到：

```text
Localization/japanese/
```

如果最後看到類似：

```text
data.win patch applied successfully.
Traditional Chinese localization installed.
```

就代表安裝成功。

### 6. 遊戲內設定

進入 Dokimon 後：

1. Language 選擇 **Japanese / 繁體中文**
2. **HD Text 設為 OFF**

目前 **HD Text 一定要關閉**，不然遊戲原本的 HD Font 縮放邏輯會把繁中字縮得非常小。

## 如果安裝器顯示 Unsupported data.win version

代表你的 `data.win` 和製作這個補丁時的遊戲版本不同。

安裝器會直接停止，**不會修改你的遊戲檔案**。

你可以先在 Steam 對 Dokimon 執行「驗證遊戲檔案完整性」後再試一次。如果遊戲後續更新造成版本真的不同，可以開 Issue 回報。

## 還原

### 方法 1：Steam 驗證檔案

Steam → Dokimon → 內容 / Properties → Installed Files → **Verify integrity of game files**。

這是最簡單的還原方式。

### 方法 2：使用安裝器建立的備份

把：

```text
data.win.zhTW-backup
```

改回：

```text
data.win
```

並將：

```text
Localization/japanese.zhTW-backup/
```

還原為：

```text
Localization/japanese/
```

即可回到安裝前的狀態。

## 補丁包裡有什麼？

```text
Localization/japanese/                         完整繁中翻譯
patches/data.win.v9-names-original.dokipatch.gz  data.win 差分補丁
tools/apply_patch.py                            安裝工具
```

其中 `data.win` 差分檔只保存這個繁中補丁需要修改的差異，**不是 Dokimon 的完整遊戲檔案**。

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

## 碎碎念
- **我是用Chatgpt做的** 所以如果有一些問題的話歡迎大家補強，我只是剛好領了這個限免遊戲，沒中文可以看小痛苦，覺得有60分的中文我就接受了。

## 版權說明

Dokimon 與其遊戲資產之權利歸原作者／權利人所有。本專案僅為非官方繁體中文 fan translation。
