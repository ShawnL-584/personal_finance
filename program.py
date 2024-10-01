import pandas as pd

file_path = r'/Users/shawnlin/Documents/python/MyProject/baby_population.xls'
df = pd.read_excel(file_path)
df.columns = df.iloc[1]
df = df.drop(index=[0, 1])
df = df.set_index('縣市別')
df = df.loc[:,
     ['新北市', '臺北市', '桃園市', '臺中市', '臺南市', '高雄市', '宜蘭縣', '新竹縣', '苗栗縣', '彰化縣', '南投縣',
      '雲林縣', '嘉義縣', '屏東縣', '臺東縣', '花蓮縣', '澎湖縣', '基隆市', '新竹市', '嘉義市', '金門縣',
      '連江縣']]  # take from each county
print(df)
# print(df.index)
# print(df.columns)
