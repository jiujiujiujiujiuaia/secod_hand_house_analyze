import pandas as pd

data = pd.read_excel('C:\\Users\\A\\Desktop\\二手房\\beike_20230820_161919.xls')

# Check for missing values in the dataset
missing_values = data.isnull().sum()

# Check the data types of each column
data_types = data.dtypes

# Descriptive statistics for numerical columns to check for outliers or anomalies
numerical_descriptive_stats = data[["总面积", "成交价格", "单价", "挂牌价格", "交易周期","总楼层"]].describe()

## print the results with titles
print("===Missing values in the dataset:=== \n", missing_values)
print("\n===Data types of each column:=== \n", data_types)
print("\n===Descriptive statistics for numerical columns:=== \n", numerical_descriptive_stats)

## print title

## print title with the number of fourth floor and percentage
print("\n===Number of fourth floor in the dataset:=== \n", data[data["总楼层"] <= 4].shape[0], "(", round(data[data["总楼层"] <= 4].shape[0] / data.shape[0] * 100, 2), "%)")
