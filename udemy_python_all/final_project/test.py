import requests
from bs4 import BeautifulSoup as bs

res = requests.get(r'https://rate.bot.com.tw/gold?Lang=zh-TW')
soup = bs(res.text, 'html.parser')
gold_tw = soup.findAll('td', attrs={'class': 'text-right ebank'})
gold_rate = 0
for num, data in enumerate(gold_tw):
    if num == 1:
        gold_rate = int(data.text.strip()[:4])

print(gold_rate)
