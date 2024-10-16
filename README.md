# 個人理財網站

專案使用Flask的網頁，設計用來追蹤和管理現金、股票和黃金資產。
使用者可以透過介面輸入和顯示不同資產的資訊，並生成圓餅圖來視覺化各類資產的比例。

## 主要功能

- **現金管理**：追蹤台幣和美金的金額，並根據美金匯率計算總額。
- **股票管理**：可輸入股票代碼、數量、成本等，應用程式會自動抓取最新的股價，計算股票的總市值和報酬率。
- **黃金管理**：可記錄黃金重量和購買價格，並根據黃金牌價顯示最新價值與報酬率。
- **動態圓餅圖**：繪製各類資產的圓餅圖，視覺化現金、股票與黃金的資產分佈。

## 技術部分

- **Python SQLite3 資料庫**：使用SQLite3儲存和管理現金、股票、黃金的交易記錄。
- **Python Flask 前後端互動**：基於Flask框架，實現前端表單提交和後端資料處理，並將結果呈現於網頁。
- **Python Matplotlib 圖形視覺化**：動態繪製圓餅圖，展示不同資產的分佈情況。
- **Web Scraping 爬蟲技術**：透過BeautifulSoup和Requests模組，實時抓取最新匯率、股票價格、黃金牌價等外部資料。
- **Bootstrap**：使用Bootstrap進行頁面布局，並通過HTML和JavaScript實現前端互動與動態更新。

## 使用說明

1. 刪除專案資料夾中的舊版 `datafile.db` 資料庫檔案，以確保沒有殘留的數據。
2. 重新執行 `db_setting.py`，以生成新的 `datafile.db` 資料庫檔案。
3. 執行 `index.py`，啟動伺服器並確保伺服器正常運行。
4. 打開瀏覽器，輸入 `http://127.0.0.1:5000`，即可進入個人理財網站，開始管理您的資產。

---

## Instructions

1. Delete any existing `datafile.db` in the project directory to ensure there are no old database records.
2. Run `db_setting.py` to generate a fresh `datafile.db` database file.
3. Execute `index.py` to start the server and ensure it is running properly.
4. Open your browser and navigate to `http://127.0.0.1:5000` to access the personal finance web

## 功能說明

* **首頁資產概況**  
  首頁可以查看所有資產的比例狀況，包括現金、股票、黃金等資產的分佈。使用者也可以直接刪除每筆資產紀錄，進行管理操作。  
  ![image](https://github.com/ShawnL-584/personal_finance/blob/main/static/index_show.png?raw=true)

* **現金庫存管理**  
  點擊現金庫存表單，可以提交新的現金資料，包括台幣與美金的數量，並記錄交易日期和備註。  
  ![image](https://github.com/ShawnL-584/personal_finance/blob/main/static/cash_show.png?raw=true)

* **股票庫存計算**  
  系統會自動將相同股票代號但不同股數的股票進行合併計算，讓使用者在股票庫存中能夠更方便地了解每支股票的總持倉情況。  
  ![image](https://github.com/ShawnL-584/personal_finance/blob/main/static/stock_show.png?raw=true)
