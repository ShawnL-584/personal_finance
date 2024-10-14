import matplotlib.pyplot as plt
from flask import Flask, render_template, request, g, redirect
import sqlite3
import requests
import math
import os
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plot
import matplotlib

matplotlib.use('agg')

app = Flask(__name__)
database = 'datafile.db'


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(database)
    return g.sqlite_db


@app.teardown_appcontext
def close_connection(exception):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def home():
    conn = get_db()
    cursor = conn.cursor()
    result = cursor.execute('select * from cash')
    cash_result = result.fetchall()
    # 計算台幣與美金總額
    taiwanese_dollars = 0
    us_dollars = 0
    for data in cash_result:
        taiwanese_dollars += data[1]
        us_dollars += data[2]
    # 獲取美金匯率資訊
    r = requests.get('https://tw.rter.info/capi.php')
    currency = r.json()
    total = math.floor(taiwanese_dollars + us_dollars * currency['USDTWD']['Exrate'])

    # 取得所有股票資訊
    result2 = cursor.execute("select * from stock")
    stock_result = result2.fetchall()
    unique_stock_list = []
    for data in stock_result:
        if data[1] not in unique_stock_list:
            unique_stock_list.append(data[1])
    # 計算股票總市值
    total_stock_value = 0
    # 計算單一股票資訊
    stock_info = []
    for stock in unique_stock_list:
        result = cursor.execute("select * from stock where stock_id=?", (stock,))
        result = result.fetchall()
        stock_cost = 0
        shares = 0

        for d in result:
            shares += d[2]
            stock_cost += d[2] * d[3] + d[4] + d[5]
        # 取得目前股價
        url = r'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&stockNo=' + stock
        response = requests.get(url)
        data = response.json()
        current_price = float(data['data'][-1][6].replace(',', ''))
        # 單一 股票總市值
        total_value = round(current_price * shares)
        total_stock_value += total_value
        # 單一 股票平均成本
        average_cost = round(stock_cost / shares, 2)
        # 單一 股票報酬率
        rate_of_return = round((total_value - stock_cost) * 100 / stock_cost, 2)
        stock_info.append(
            {'stock_id': stock, 'stock_cost': stock_cost, 'total_value': total_value, 'average_cost': average_cost,
             'shares': shares, 'current_price': current_price, 'rate_of_return': rate_of_return})
    for stock in stock_info:
        stock['value_percentage'] = round(stock['total_value'] * 100 / total_stock_value, 2)

    # 取得所有黃金資訊
    result3 = cursor.execute("select * from gold")
    gold_result = result3.fetchall()
    gold_result_new = []
    total_weight = 0
    total_cost = 0
    for data in gold_result:
        data_new = list(data)
        cost = round(data[2] / data[1])
        data_new.append(cost)
        gold_result_new.append(data_new)
        total_weight += round(data[1], 2)
        total_weight = round(total_weight, 2)
        total_cost += data[2]
    # 取得黃金牌價
    res = requests.get(r'https://rate.bot.com.tw/gold?Lang=zh-TW')
    soup = bs(res.text, 'html.parser')
    gold_tw = soup.findAll('td', attrs={'class': 'text-right ebank'})
    gold_rate = 0
    for num, data in enumerate(gold_tw):
        if num == 1:
            gold_rate = int(data.text.strip()[:4])

    gold_value = round(gold_rate * total_weight)
    if total_cost != 0:
        gold_rate_of_return = round((gold_value - total_cost) * 100 / total_cost, 2)
    else:
        gold_rate_of_return = 0
    gold_info = [total_weight, total_cost, gold_rate, gold_value, gold_rate_of_return]

    # 繪製股票圓餅圖
    if len(unique_stock_list) != 0:
        labels = tuple(unique_stock_list)
        sizes = [d['total_value'] for d in stock_info]
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.pie(sizes, labels=labels, autopct='%1.2f%%', shadow=None, textprops={'fontsize': 14})
        fig.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.savefig('static/piechart.jpg', dpi=200)
    else:
        try:
            os.remove('static/piechart.jpg')
        except:
            pass
    # 繪製股票現金圓餅圖
    if us_dollars != 0 or taiwanese_dollars != 0 or total_stock_value != 0 or gold_value != 0:
        labels = ('美金', '台幣', '股票', '黃金')
        sizes = (us_dollars * currency['USDTWD']['Exrate'], taiwanese_dollars, total_stock_value, gold_value)
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.pie(sizes, labels=labels, autopct='%1.2f%%', shadow=None, textprops={'fontsize': 14})
        fig.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.savefig('static/piechart2.jpg', dpi=200)
    else:
        try:
            os.remove('static/piechart2.jpg')
        except:
            pass
    # 繪製現金圓餅圖
    if us_dollars != 0 or taiwanese_dollars != 0:
        labels = ('美金', '台幣')
        sizes = (us_dollars * currency['USDTWD']['Exrate'], taiwanese_dollars)
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.pie(sizes, labels=labels, autopct='%1.2f%%', shadow=None, textprops={'fontsize': 14})
        fig.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
        plt.savefig('static/piechart3.jpg', dpi=200)
    else:
        try:
            os.remove('static/piechart3.jpg')
        except:
            pass
    data = {'show_pic1': os.path.exists(r'static/piechart.jpg'),
            'show_pic2': os.path.exists(r'static/piechart2.jpg'),
            'show_pic3': os.path.exists(r'static/piechart3.jpg'),
            'total': total, 'currency': round(currency['USDTWD']['Exrate'], 2), 'usd': us_dollars,
            'twd': taiwanese_dollars,
            'cash_result': cash_result, 'stock_info': stock_info, 'stock_result': stock_result,
            'gold_result_new': gold_result_new, 'gold_info': gold_info}
    print(data['show_pic2'])
    return render_template('index.html', data=data)


@app.route('/cash')
def cash_form():
    return render_template('cash.html')


@app.route('/cash', methods=['POST'])
def submit_cash():
    # 取得金額與日期
    taiwanese_dollars = 0
    us_dollars = 0
    if request.values['taiwanese-dollars'] != '':
        taiwanese_dollars = request.values['taiwanese-dollars']
    if request.values['us-dollars'] != '':
        us_dollars = request.values['us-dollars']
    note = request.values['note']
    date = request.values['date']
    # 更新資料庫
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""insert into cash(taiwanese_dollars, us_dollars, note, date_info) values (?,?,?,?)""",
                   (taiwanese_dollars, us_dollars, note, date))
    conn.commit()
    # 將使用者導回主頁面

    return redirect('/')


@app.route('/cash-delete', methods=['POST'])
def cash_delete():
    transaction_id = request.values['id']
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""delete from cash where transaction_id = ?""", (transaction_id,))
    conn.commit()

    return redirect('/')


@app.route('/stock')
def stock_form():
    return render_template('stock.html')


@app.route('/stock', methods=['POST'])
def submit_stock():
    # 取得股票日期,資料
    stock_id = request.values['stock-id']
    stock_num = request.values['stock-num']
    stock_price = request.values['stock-price']
    processing_fee = 0
    tax = 0
    if request.values['processing-fee'] != '':
        processing_fee = request.values['processing-fee']
    if request.values['tax'] != '':
        tax = request.values['tax']
    date = request.values['date']
    print(stock_id, stock_num, stock_price, processing_fee, tax, date)
    # 更新數據庫資料
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """insert into stock(stock_id, stock_num , stock_price, processing_fee, tax, date_info) values (?,?,?,?,?,?)""",

        (stock_id, stock_num, stock_price, processing_fee, tax, date))
    conn.commit()
    # 將使用者導回主頁面
    return redirect('/')


@app.route('/stock-delete', methods=['POST'])
def stock_delete():
    transaction_id = request.values["stock_t_id"]
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""delete from stock where transaction_id = ?""", (transaction_id,))
    conn.commit()
    return redirect('/')


@app.route('/gold')
def gold_form():
    return render_template('gold.html')


@app.route('/gold', methods=['POST'])
def submit_gold():
    # 取得黃金資料
    gold_weight = request.values['gold-weight']
    gold_price = request.values['gold-price']
    date = request.values['date']

    # 更新資料庫
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""insert into gold(gold_weight, gold_price,date_info) values (?,?,?)""",
                   (gold_weight, gold_price, date))
    conn.commit()
    # 將使用者導回主頁面
    return redirect('/')


@app.route('/gold-delete', methods=['POST'])
def gold_delete():
    transaction_id = request.values["gold_id"]
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""delete from gold where transaction_id = ?""", (transaction_id,))
    conn.commit()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
