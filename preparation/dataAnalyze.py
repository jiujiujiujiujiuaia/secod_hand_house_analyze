import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Set the style for the plots
data = pd.read_excel('C:\\Users\\A\\Desktop\\二手房\\beike_20230820_161919.xls')

plt.rcParams["font.sans-serif"]=["SimHei"] 

# 1. Analyzing the distribution of transaction cycle based on room types
plt.figure(figsize=(12, 6))
sns.boxplot(x='户型结构', y='交易周期', data=data, order=data['户型结构'].value_counts().index)
plt.title('交易周期分布根据户型结构')
plt.xlabel('户型结构')
plt.ylabel('交易周期 (天)')
plt.xticks(rotation=45)
plt.tight_layout()

# 2. Analyzing the distribution of transaction cycle based on total area
# Dividing the total area into different segments for easier analysis
bins = [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
labels = ['0-50', '50-100', '100-150', '150-200', '200-250', '250-300', '300-350', '350-400', '400-450', '450-500']
data['面积段'] = pd.cut(data['总面积'], bins=bins, labels=labels, right=False)

plt.figure(figsize=(12, 6))
sns.boxplot(x='面积段', y='交易周期', data=data, order=labels)
plt.title('交易周期分布根据总面积')
plt.xlabel('总面积 (平方米)')
plt.ylabel('交易周期 (天)')
plt.xticks(rotation=45)
plt.tight_layout()

# 3. Analyzing the distribution of transaction cycle based on floor type
plt.figure(figsize=(12, 6))
sns.boxplot(x='楼层类型', y='交易周期', data=data)
plt.title('交易周期分布根据楼层类型')
plt.xlabel('楼层类型')
plt.ylabel('交易周期 (天)')
plt.tight_layout()

plt.show()