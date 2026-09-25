# python-

Python 相關的練習與小工具集合，每個子目錄是一個獨立的小專案或腳本集合。

## 圖片與媒體處理

| 目錄 | 說明 |
|---|---|
| [Facebook文章抓取](Facebook文章抓取) | 利用 Facebook 官方 API 批次抓取用戶貼文，供後續儲存與分析 |
| [OpenCV實作](OpenCV實作) | OpenCV 驗證碼（captcha）辨識練習 |
| [文件管理](文件管理) | 圖片檔名統一編號、重複圖片偵測、批次調整圖片尺寸 |
| [音效播放器(UI實作介面)](音效播放器(UI實作介面)) | Tkinter 製作的音樂播放器 |
| [Youtube下載器(UI實作介面)](Youtube下載器(UI實作介面)) | Tkinter 製作的 YouTube 影片/音樂下載器（720p 以下） |
| [web-scrapying-photo](web-scrapying-photo) | Yande.re、WallpaperAbyss 圖片爬蟲（原獨立 repo 併入，保留原始 commit 歷史） |

## 爬蟲與資料擷取

| 目錄 | 說明 |
|---|---|
| [新聞爬蟲實作](新聞爬蟲實作) | 聯合新聞網、中時、經濟日報、CNN 等新聞來源的爬蟲 |
| [Selenium實作](Selenium實作) / [selenium_automation](selenium_automation) | Selenium 模擬使用者行為，可結合爬蟲抓取資料 |
| [twitter-testing](twitter-testing) | Twitter API 查詢練習（tweet lookup） |
| [python_tool-collection](python_tool-collection) | 104 找工作、591 找房子的自動化搜尋腳本（原獨立 repo 併入，保留原始 commit 歷史） |

## 資料分析與視覺化

| 目錄 | 說明 |
|---|---|
| [numpy-python](numpy-python) | Numpy / Pandas 練習 |
| [plotly-python](plotly-python) | Plotly 資料視覺化練習 |
| [台股市場分析統計](台股市場分析統計) | 抓取台股月/年統計資料（XHR/JSON），用 Plotly 呈現 |
| [天氣預報](天氣預報) | 中央氣象署 Web API 資料擷取，Flask 後端 + Plotly.js 前端呈現 |
| [全台PM2.5偵測(UI實作介面)](全台PM2.5偵測(UI實作介面)) | PM2.5 資料擷取 + Tkinter UI（資料來源需付費，功能已停用） |
| [python-faang-stock-analyzer](python-faang-stock-analyzer) | Finance API + Pandas + Plotly + Dash 的股票分析工具（原獨立 repo 併入，保留原始 commit 歷史） |
| [python-stock_suggestion](python-stock_suggestion) | 用 ChatGPT 分析投顧分析師發言、給出股票建議（原獨立 repo 併入，保留原始 commit 歷史） |

## 資料庫與後端小工具

| 目錄 | 說明 |
|---|---|
| [db_execrise](db_execrise) | PyMySQL / SQLAlchemy / Firebase 資料庫連線練習 |
| [檔案文字掃描](檔案文字掃描) | 在指定目錄下的文字檔（txt/word）中搜尋關鍵字/詞綴 |
| [flask](flask) | Flask 練習（原獨立 repo 併入，保留原始 commit 歷史） |
| [Flask 匯差判斷](Flask%20匯差判斷) | Flask 練習：匯率／匯差判斷小工具 |

## 其他 / 練習

| 目錄 | 說明 |
|---|---|
| [tutorial](tutorial) | Python 基礎語法練習 |

## 備註

- 標註「原獨立 repo 併入」的目錄，都是用 `git subtree` 從各自獨立的 GitHub repo 併入，原本的 commit 歷史都保留在這裡；原本的獨立 repo 目前仍保留，尚未刪除。
- 各腳本多為個人練習用途，執行前請自行檢查相依套件與所需的 API 金鑰設定。
