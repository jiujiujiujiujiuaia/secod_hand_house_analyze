import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 户型和成交价的折线图

# Load the data
data = pd.read_excel('C:\\Users\\A\\Desktop\\二手房\\beike_20230820_161919.xls')

plt.rcParams["font.sans-serif"]=["SimHei"]

# 1. 按照年份分组，处理成交日期
data['成交日期'] = pd.to_datetime(data['成交日期'])
data['year'] = data['成交日期'].dt.year

# 2. 总楼层小于等于5或总面积大于等于145的数据，图例中使用别墅或洋房或大平层代替户型结构
data['显示户型结构'] = data['户型结构']
data.loc[(data['总楼层'] <= 5) | (data['总面积'] >= 145), '显示户型结构'] = '别墅或洋房或大平层'

# 3. 按照户型结构分组，不展示分组数量小于2的分组
group_count = data.groupby(['year', '显示户型结构']).size().reset_index(name='count')
valid_groups = group_count[group_count['count'] >= 2]['显示户型结构'].unique()
data = data[data['显示户型结构'].isin(valid_groups)]

# 4. 计算每一个年份和户型结构的成交价格平均值
grouped_data = data.groupby(['year', '显示户型结构'])['成交价格'].mean().reset_index()

# 5. & 6. 使用折线图进行可视化
plt.figure(figsize=(12, 8))
sns.lineplot(data=grouped_data, x='year', y='成交价格', hue='显示户型结构', palette='tab10')
plt.title("年度成交价格与户型结构关系")
plt.xlabel("年份")
plt.ylabel("成交价格")
plt.legend(title="显示户型结构")
plt.grid(True)
plt.tight_layout()
plt.show()
