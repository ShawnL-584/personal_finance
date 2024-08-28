# 新竹市重要遊憩據點遊客人次統計.csv
# 新竹市重要遊憩據點遊客人次統計.xlsx
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import squarify

df = pd.read_csv('新竹市重要遊憩據點遊客人次統計.csv')
df = df.drop(columns=['Countycode','YYYMM'])
df = df.astype('int32')
df['民國年月'] = df['民國年月'].astype('str')
df['年'] =  df['民國年月'].str[:3]
df = df.set_index('民國年月')
df_g = df.groupby('年').sum() # 各年總人數
s1 = df.sum(numeric_only = True).sort_values(ascending=False) # 每年總人數最大值

Accent = mpl.colormaps['Accent']
new_Accent = [Accent(n) for n in range(8)]

fig, ax = plt.subplots(nrows = 3, ncols=2,constrained_layout = True, figsize = (20,18))
plt.title('108-112年 新竹市重要遊憩據點遊客人數分布統計')

# pic1
據點 = s1.index
據點 = [item[:-2] for item in 據點]
據點索引 = [n for n in range(len(據點))]
人數 = s1
ax[0,0].bar(據點,人數,color = new_Accent, zorder = 10)
ax[0,0].set_xlabel('據點',color = 'red',fontsize = 12 )
ax[0,0].set_ylabel('人數(百萬)',color = 'red',fontsize = 12 )
ax[0,0].set_xticks(據點索引,據點,rotation = 30)
ax[0,0].set_yticks([n for n in range(0,20000001,5000000)],[str(n) for n in range(0,21,5)],color = 'red')
ax[0,0].set_title('5年總人數統計')



# pic2
據點 = df_g.columns
據點 = [item[:-2] for item in 據點]
據點索引 = [n for n in range(len(據點))]
人數 = df_g.loc['108']
ax[0,1].bar(據點,人數,color = new_Accent, zorder = 10)
ax[0,1].set_xlabel('據點',color = 'red',fontsize = 12 )
ax[0,1].set_ylabel('人數',color = 'red',fontsize = 12 )
ax[0,1].set_xticks(據點索引,據點,rotation = 30)
ax[0,1].set_yticks([n for n in range(0,5000001,1000000)],[str(n) for n in range(0,51,10)],color = 'red')
ax[0,1].set_title('108年人數統計')


# pic3
人數 = df_g.loc['109']
ax[1,0].bar(據點,人數,color = new_Accent, zorder = 10)
ax[1,0].set_xlabel('據點',color = 'red',fontsize = 12 )
ax[1,0].set_ylabel('人數',color = 'red',fontsize = 12 )
ax[1,0].set_xticks(據點索引,據點,rotation = 30)
ax[1,0].set_yticks([n for n in range(0,5000001,1000000)],[str(n) for n in range(0,51,10)],color = 'red')
ax[1,0].set_title('109年人數統計')

# pic4
人數 = df_g.loc['110']
ax[1,1].bar(據點,人數,color = new_Accent, zorder = 10)
ax[1,1].set_xlabel('據點',color = 'red',fontsize = 12 )
ax[1,1].set_ylabel('人數',color = 'red',fontsize = 12 )
ax[1,1].set_xticks(據點索引,據點,rotation = 30)
ax[1,1].set_yticks([n for n in range(0,5000001,1000000)],[str(n) for n in range(0,51,10)],color = 'red')
ax[1,1].set_title('110年人數統計')


# pic5
人數 = df_g.loc['111']
ax[2,0].bar(據點,人數,color = new_Accent, zorder = 10)
ax[2,0].set_xlabel('據點',color = 'red',fontsize = 12 )
ax[2,0].set_ylabel('人數',color = 'red',fontsize = 12 )
ax[2,0].set_xticks(據點索引,據點,rotation = 30)
ax[2,0].set_yticks([n for n in range(0,5000001,1000000)],[str(n) for n in range(0,51,10)],color = 'red')
ax[2,0].set_title('111年人數統計')

# pic6
人數 = df_g.loc['112']
ax[2,1].bar(據點,人數,color = new_Accent, zorder = 10)
ax[2,1].set_xlabel('據點',color = 'red',fontsize = 12 )
ax[2,1].set_ylabel('人數',color = 'red',fontsize = 12 )
ax[2,1].set_xticks(據點索引,據點,rotation = 30)
ax[2,1].set_title('112年人數統計')
ax[2,1].set_yticks([n for n in range(0,5000001,1000000)],[str(n) for n in range(0,51,10)],color = 'red')

print(df_g)
plt.savefig('108-112年人數統計.pdf', dpi=300, bbox_inches="tight")