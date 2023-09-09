import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 低中高楼层类型和挂牌价格和成交价格差值的折线图

# Load the data
data = pd.read_excel('C:\\Users\\A\\Desktop\\二手房\\beike_20230820_161919.xls')

plt.rcParams["font.sans-serif"]=["SimHei"] 

# 1. 按照年份分组，处理成交日期
data['成交日期'] = pd.to_datetime(data['成交日期'])
data['year'] = data['成交日期'].dt.year

# 2. 总楼层小于等于5或总面积大于等于145的数据，图例中使用别墅或洋房或大平层代替楼层类型
data['显示楼层类型'] = data['楼层类型']
data.loc[(data['总楼层'] <= 5) | (data['总面积'] >= 145), '显示楼层类型'] = '别墅或洋房或大平层'

# 3. 按照楼层类型分组，不展示分组数量小于2的分组
group_count = data.groupby(['year', '显示楼层类型']).size().reset_index(name='count')
valid_groups = group_count[group_count['count'] >= 2]['显示楼层类型'].unique()
data = data[data['显示楼层类型'].isin(valid_groups)]

# 4. 计算每一个年份和楼层类型的挂牌价格和成交价格差值的平均值
data['挂牌价格和成交价格差值'] = data['挂牌价格'] - data['成交价格']
grouped_data = data.groupby(['year', '显示楼层类型'])['挂牌价格和成交价格差值'].median().reset_index()

# 5. & 6. 使用折线图进行可视化
plt.figure(figsize=(12, 8))
sns.lineplot(data=grouped_data, x='year', y='挂牌价格和成交价格差值', hue='显示楼层类型', palette='tab10')
plt.title("年度挂牌价格和成交价格差值与楼层类型关系")
plt.xlabel("年份")
plt.ylabel("挂牌价格和成交价格差值")
plt.legend(title="显示楼层类型")
plt.grid(True)
plt.tight_layout()
plt.show()
