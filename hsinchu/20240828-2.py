import pandas as pd
import numpy as np

dfs = []
year = [str(n) for n in range(2020,2025)]
month = [str(n).zfill(2) for n in range(1,13)]
for y in year:
    for m in month:
        file_name = r'./738/STOCK_DAY_00738U_'+ f'{y}{m}.csv'
        if y == '2024' and m =='09':
            break
        df = pd.read_csv(file_name, encoding = 'big5',header = 1,thousands = ',')
        df= df[df['日期'].str.match(r'^\d{3}/\d{2}/\d{2}$') ]
        df = df.drop(columns = ['成交金額','漲跌價差','成交筆數','Unnamed: 9'])
        df['成交股數']= df['成交股數'].astype('int32')
        dfs.append(df)

dfs = pd.concat(dfs)
dfs = dfs.reset_index(drop=True)
print(dfs)