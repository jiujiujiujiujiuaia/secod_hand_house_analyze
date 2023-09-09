import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 不同小区的成交价格的折线图

# Set the style for the plots
df = pd.read_excel('C:\\Users\\A\\Desktop\\二手房\\四个小区_20230826_161919.xls')

plt.rcParams["font.sans-serif"]=["SimHei"] 

# 1. 把所有数据按照年份分成不同的组,请用pd.to_datetime处理成交日期。同时增加一个新的列为显示小区名
df['成交日期'] = pd.to_datetime(df['成交日期'])
df['成交年份'] = df['成交日期'].dt.year
df['显示小区名'] = df['小区名']

# 2. 不考虑总楼层小于等于5，或者总面积大于等于145
df = df[(df['总楼层'] > 5) & (df['总面积'] < 145)]

# 3. 只考虑户型结构为4室2厅,4室1厅，3室2厅，3室1厅
df = df[df['户型结构'].isin(['4室2厅', '4室1厅', '3室2厅', '3室1厅'])]

# 4. 把同一年份不同小区名的数据按照显示小区名分组，不展示分组count小于2的分组
grouped = df.groupby(['成交年份', '显示小区名']).filter(lambda x: len(x) >= 2)

# 5. 对所有同一个年份同一个显示小区名的数据，计算挂牌价格和成交价格差值
grouped['挂牌价格和成交价格差值'] = grouped['挂牌价格'] - grouped['成交价格']
grouped_result = grouped.groupby(['成交年份', '显示小区名'])['挂牌价格和成交价格差值'].median().unstack()

# 6. 横坐标是年份，纵坐标是挂牌价格和成交价格差值，图例是显示小区名，请用折线图进行可视化
plt.figure(figsize=(12, 6))
for column in grouped_result.columns:
    plt.plot(grouped_result.index, grouped_result[column], label=column, marker='o')

# 7. 图例的颜色尽量选择差别比较大的，这样能够分辨清楚。
colors = ['blue', 'green', 'red', 'purple']
for i, line in enumerate(plt.gca().get_lines()):
    line.set_color(colors[i])

plt.title('年度挂牌价格和成交价格差值变化')
plt.xlabel('年份')
plt.ylabel('挂牌价格和成交价格差值')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
