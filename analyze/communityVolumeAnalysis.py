import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 不同小区的成交价格的折线图

# Set the style for the plots
df = pd.read_excel('C:\\Users\\A\\Desktop\\二手房\\四个小区_20230826_161919.xls')

plt.rcParams["font.sans-serif"]=["SimHei"] 

# 把所有数据按照年份分成不同的组,使用pd.to_datetime处理成交日期
df['成交日期'] = pd.to_datetime(df['成交日期'])
df['成交年份'] = df['成交日期'].dt.year

# 根据年份和小区名分组，统计成交量
transaction_volume_per_year = df.groupby(['成交年份', '小区名']).size().unstack()

# 使用折线图展示每一年的成交量
plt.figure(figsize=(12, 6))
for column in transaction_volume_per_year.columns:
    plt.plot(transaction_volume_per_year.index, transaction_volume_per_year[column], label=column, marker='o')

# 设置图例、标题、坐标轴标签等
plt.legend()
plt.title('年度成交量变化')
plt.xlabel('年份')
plt.ylabel('成交量')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
