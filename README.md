## 目标
房子作为大宗商品，具有价值高，转手周期长等特点。而购房者，往往希望买到的房子

未来升值，如果不能升值，至少好转手，因此，了解某小区某户型在市场上的热度或者喜好

就是二手房购买者需要攻克的难题，那么萦绕在购房者眼中的问题有哪些呢？

* 1.应该买哪个小区？（哪个小区更加保值）
* 2.应该买个哪个户型？（哪个户型更受大家喜爱且容易流转？）
* 3.应该买哪个楼层？
* 4.应该以什么样的价格买？

笔者希望通过数据分析的手段，找到最适合买的户型，楼层，小区。

通过计算出同一小区的，不同户型，不同楼层，不同的挂牌周期，来计算出什么样的房子挂牌周期比较短，成交比较快。

通过将独墅湾和其他苏州热门小区的挂牌周期做比较，看看独墅湾的成交周期的平均数，中位数，是否和其他热门小区短？从而衡量独墅湾相较于其他小区是否好转手。

甚至可以分析10个热门小区，不同年份，不同面积段的二手成交数据，进行分析，苏州市场人群偏好是否有变化，当前最适合上车的户型段是什么。

## ChatGPT帮助数据分析

在购买了GPT plus后，就拥有了Code interpreter的权限。

### 1.数据准备和清洗

* 检查数据中是否有缺失值。
* 检查数据类型是否正确。
* 检查是否有异常值。

```python
# Check for missing values in the dataset
missing_values = data.isnull().sum()

# Check the data types of each column
data_types = data.dtypes

# Descriptive statistics for numerical columns to check for outliers or anomalies
numerical_descriptive_stats = data[["总面积", "成交价格", "单价", "挂牌价格", "交易周期"]].describe()
```

TODO 可以得到如下结果

### 2.了解数据分布

* 分布分析：查看房屋类型、朝向、建筑类型和楼层类型的分布。
* 成交价格和挂牌价格的分布。
* 单价的分布。
* 交易周期的分布。

```python
import matplotlib.pyplot as plt

# Set up the figure and axes
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Plot distribution for categorical columns
data['房屋类型'].value_counts().plot(kind='bar', ax=axs[0, 0], title='房屋类型分布')
data['朝向'].value_counts().plot(kind='bar', ax=axs[0, 1], title='朝向分布')
data['建筑类型'].value_counts().plot(kind='bar', ax=axs[1, 0], title='建筑类型分布')
data['楼层类型'].value_counts().plot(kind='bar', ax=axs[1, 1], title='楼层类型分布')

# Adjust the layout
plt.tight_layout()
plt.show()

```

TODO 可以得到如下结果，可以注意到，4楼都是独栋的洋房，他们的数据应该和高层的数据分开分析。

```python
# Set up the figure and axes for numerical columns' distribution
fig, axs = plt.subplots(2, 2, figsize=(15, 10))

# Plot histograms for numerical columns
data['成交价格'].plot(kind='hist', bins=30, ax=axs[0, 0], title='成交价格分布', color='skyblue', edgecolor='black')
data['单价'].plot(kind='hist', bins=30, ax=axs[0, 1], title='单价分布', color='salmon', edgecolor='black')
data['挂牌价格'].plot(kind='hist', bins=30, ax=axs[1, 0], title='挂牌价格分布', color='lightgreen', edgecolor='black')
data['交易周期'].plot(kind='hist', bins=30, ax=axs[1, 1], title='交易周期分布', color='orchid', edgecolor='black')

# Adjust the layout
plt.tight_layout()
plt.show()
```

TODO 可以得到如下结果

### 3.分析

* -1.同小区中，把不同的户型分为不同的组，计算平均交易周期，年份作为变量，户型结构作为图例。（把别墅和洋房的户型直接设置为洋房）
* 0.同小区中，把不同的面积分成不同的组，计算平均交易周期，年份作为变量，总面积作为图例。（把别墅和洋房的户型直接设置为洋房） 
* 1.同小区中，把不同的楼层分为不同的组，计算平均交易周期，年份作为变量，楼层类型作为图例。（把别墅和洋房的户型直接设置为洋房）
* 2.同小区中，把不同的户型分为不同的组，计算房子的挂牌价格和成交价格差值，年份作为变量，户型结构作为图例。（把别墅和洋房的户型直接设置为洋房）
* 3.同小区中，把不同的面积分为不同的组，计算房子的挂牌价格和成交价格差值，年份作为变量，总面积作为图例。（把别墅和洋房的户型直接设置为洋房）
* 4.同小区中，把不同的楼层分为不同的组，计算房子的挂牌价格和成交价格差值，年份作为变量，楼层类型作为图例。（把别墅和洋房的户型直接设置为洋房）
* 5.同小区中，把不同的户型分为不同的组，计算房子的成交价格，年份作为变量，户型结构作为图例。（把别墅和洋房的户型直接设置为洋房）
* 6.同小区中，把不同的面积分为不同的组，计算房子的成交价格，年份作为变量，总面积作为图例。（把别墅和洋房的户型直接设置为洋房）
* 7.同小区中，把不同的楼层分为不同的组，计算房子的成交价格，年份作为变量，楼层类型作为图例。（把别墅和洋房的户型直接设置为洋房）
* 8.比较不同的小区，哪个小区的平均挂牌周期最短，细分到不同的年份，看看逐年之间的趋势

## 咒语(prompt)

### 分析同一个小区
假设你房屋分析大师，请你按照下面的指令，对我提供的数据进行分析。
请用下面的占位符替换掉下面指令中所有用大括号扩起来的文字。
替换完下面的指令后，用替换好的指令去生成代码。

占位符：
* {placeholder}=楼层类型
* {floor}=5
* {area}=145
* {count]=2
* {calculateType}=交易周期

指令:
* 1.把所有数据按照年份分成不同的组,请用pd.to_datetime处理成交日期。同时增加一个新的列为显示{placeholder}
* 2.总楼层小于等于{floor}，或者总面积大于等于{area}，图例中不要用{placeholder}显示，请用别墅或洋房或大平层代替。
* 3.把同一年份不同{placeholder}的数据按照显示{placeholder}分组，不展示分组count小于{count}的分组
* 4.对所有同一个年份同一个显示{placeholder}的数据，计算{calculateType}
* 5.横坐标是年份，纵坐标是{calculateType}，图例是显示{placeholder}，请用折线图进行可视化
* 6.图例的颜色尽量选择差别比较大的，这样能够分辨清楚。
* 7.请提供完整的代码。
* 8.不要展示每一步，直接展示可视化和提供代码。

### 分析不同的小区

假设你房屋分析大师，请你按照下面的指令，对我提供的数据进行分析。
请用下面的占位符替换掉下面指令中所有用大括号扩起来的文字。
替换完下面的指令后，用替换好的指令去生成代码。

占位符：
* {placeholder}=小区名
* {floor}=5
* {area}=145
* {count]=2
* {calculateType}=交易周期

指令:
* 1.把所有数据按照年份分成不同的组,请用pd.to_datetime处理成交日期。同时增加一个新的列为显示{placeholder}
* 2.不考虑总楼层小于等于{floor}，或者总面积大于等于{area}
* 3.只考虑'户型结构'为4室2厅,4室1厅，3室2厅，3室1厅
* 4.把同一年份不同{placeholder}的数据按照显示{placeholder}分组，不展示分组count小于{count}的分组
* 5.对所有同一个年份同一个显示{placeholder}的数据，计算{calculateType}
* 6.横坐标是年份，纵坐标是{calculateType}，图例是显示{placeholder}，请用折线图进行可视化
* 7.图例的颜色尽量选择差别比较大的，这样能够分辨清楚。
* 8.请提供完整的代码。
* 9.不要展示每一步，直接展示可视化和提供代码。

### 成交量

把所有数据按照年份分成不同的组,请用pd.to_datetime处理成交日期，
用折现图展示每一年的成交量，图例是小区名。


### Prompt启示：

* 1.步骤要按照代码步骤给GPT，步骤不能和代码步骤出现不一致
* 2.prompt的表述尽量和excel表格header一致
* 3.逻辑语言例如
* 
## 结果展示

### 1.同一小区

#### 1.1 户型结构和成交价格的关系

![img.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img.png)

#### 1.2 户型结构和交易周期的关系

* 1.别墅的成交周期远低高楼，有钱人还是多啊
* 2.别墅的价格降下来了，因此成交周期逐渐缩短了。
* 3.疫情三年，3室和4室的房子交易周期不断变长。
* 4.尽管疫情结束了，看房子更加容易了，但是4室的房子交易周期仍在增加，3室的房子受到疫情解封福利，有下降趋势。

![img_1.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img_1.png)

#### 1.3 户型结构与成交价和挂牌价的差值的关系

* 1.差值越大，说明房东心理价位过高，不得不降价以促成交易
* 2.对于别墅而言，疫情结束后，房东可以用少降价，尽量贴近挂牌价的方式成交
* 3.对于3室和4室的房子，房东在不断降价已促成成交，平均降价15w左右

![img_2.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img_2.png)

#### 1.4 楼层和成交价的关系

* 1.低楼层在走高，中高楼层在走低，走低大概在10w左右
* 2.别墅也在跳水

![img_3.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img_3.png)



#### 1.5 楼层和交易周期的关系

* 1.低楼层虽然成交价格在走高，但是成交周期在不断上升
* 2.低楼层交易周期中位数为455天，而中高楼层差不多在190天左右
* 3.别墅卖的很快

![img_4.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img_4.png)

中位数

![img_5.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img_5.png)

#### 1.6 楼层与成交价和挂牌价的差值的关系

* 1.无论是中低高楼层哪一种，平均值和中位数都在上升，房东不得多让一些利益，以达到成交的目的
* 2.房东中位数让利15w左右，因此成交价至少是挂牌价减去15w
* 3.不得不说别墅的价格和坚挺，别墅尽管总价价格大，但是却和高层的房子降价幅度差不多。

![img_6.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img_6.png)

### 2.不同小区

* A小区的区位差于其他小区
* B小区是笔者最先去的小区
* C小区和D小区区位是最好的，C小区是次新房，D小区是房龄20年左右的二手房
* 下面的表格中仅仅考虑了4室2厅,4室1厅，3室2厅，3室1厅

#### 2.1 小区和成交价的关系

* 除B小区外，所有小区成交价格都在下跌，下跌在20w左右

![img_8.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img_8.png)
 
#### 2.2 楼层和交易周期的关系

* 同样的，除B小区外，所有小区的成交周期都在变长

![img_7.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img_7.png)

#### 2.3 楼层与成交价和挂牌价的差值的关系

* B小区非常枪手，房东需要降10w左右，就可以成交，并且和去年持平
* A小区虽然略微增加，但是抢手程度和B小区类似，可以降价不多的情况下完成交易

![img_9.png](https://raw.githubusercontent.com/jiujiujiujiujiuaia/jiujiujiujiujiuaia.github.io/master/_posts/pic/spider/img_9.png)

## TODO
1.抓包环境配置
2.抓包原理
3.wc的建模分析的视频？有一个kaggle国外大神的书
4.分析不同的户型的不同楼层，成交价，成交周期，降价幅度的关系，得出最应该买什么类型的房子

## Reference:
* 1.https://blog.csdn.net/weixin_45195493/article/details/122466796
* 2.https://cloud.tencent.com/developer/article/1819306
* 3.https://github.com/WuFengXue/android-reverse