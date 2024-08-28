import pandas as pd

白銀 = [ ]
s_year = [ str(n) for n in range(2020,2025,1)]
s_month = [ str(n).zfill(2) for n in range(1,13)]
for _year in s_year :
    for _month in s_month :
        file_name = f'./738/STOCK_DAY_00738U_{_year}{_month}.csv'
        df = pd.read_csv(file_name,encoding='big5',header=1,thousands=',')
        df = df[  df['日期'].str.match('\d\d\d/\d\d/\d\d')  ]
        df = df.drop(columns=['成交金額','漲跌價差','成交筆數','Unnamed: 9'])
        df['成交股數'] = df['成交股數'].astype('int32')
        白銀.append(df)
        if _year=='2024' and _month=='08':break
白銀股價 = pd.concat(白銀)
白銀股價 = 白銀股價.reset_index(drop=True)
# 白銀股價  日期	成交股數	開盤價	最高價	最低價	收盤價

日期 = 白銀股價['日期']
收盤價 = 白銀股價['收盤價']

import matplotlib.pyplot as plt

_fig = plt.gcf()
_axes = plt.gca()

_fig.set_facecolor((255/255,219/255,172/255))
_fig.set_figheight(10)
_fig.set_figwidth(30)
_fig.set_layout_engine(layout='tight')  # 'constrained', 'compressed', 'tight', 'none'
_axes.set_facecolor(((241/255,194/255,125/255)))

_xticks = [ n for n in range(0,len(日期),50) ]
_labels = [ 日期[n] for n in _xticks]

plt.title("元大白銀ETF股價折線圖", **{'fontsize':18})
plt.plot(日期,收盤價,**{'color':(0,0,1),
                            'linewidth':2.0,
                            'marker':',',
                            'markerfacecolor':(1,0,0)
                           })
plt.xticks(ticks=_xticks,labels=_labels,**{'rotation':90})
plt.xlabel("日期", **{'fontsize':12,'rotation':0})
plt.ylabel("收盤價", **{'fontsize':12})
plt.grid(visible=True,axis='y',**{'linestyle':'--'})
# plt.show()
plt.savefig("元大白銀ETF股價折線圖.pdf", dpi=300, bbox_inches="tight")