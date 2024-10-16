# 個人理財網站

專案使用Flask 的網頁，設計用來追蹤和管理現金、股票和黃金資產。
使用者可以透過介面輸入和顯示不同資產的資訊，並生成圓餅圖來視覺化各類資產的比例。

## 功能

- **現金管理**：追蹤台幣和美金的金額。
- **股票管理**：監控股票總市值，並根據最新股價即時更新。
- **黃金管理**：追蹤黃金持有量並顯示當前市值。
- **動態圓餅圖**：視覺化現金、股票與黃金的資產分佈。
- **資料庫整合**：所有資料皆存儲在 SQLite 資料庫中（`datafile.db`）。

## 使用技術

* python sqlite3 資料庫
* python flask 前後端互動
* python matpotlib 圖形視覺化
* web scraping 爬蟲抓取最新匯率、股價等資訊
* bootstrap, html, javascript 進行網頁排版以及互動

##   

1.Execute db_setting.py to create the database if there is no datafile.db.\
2.Execute index.py to run the server and make sure the server is working.\
3.Open browser and enter http://127.0.0.1:5000 to use.
