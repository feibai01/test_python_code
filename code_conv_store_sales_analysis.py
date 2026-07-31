# 使用import导入pandas模块，简称为pd
import pandas as pd

'''读取文件'''
data = pd.read_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\junjun\store.csv")


'''数据的处理与清洗'''
# 1. 识别并处理缺失值
# TODO 使用布尔索引和isnull()函数，将"订单量"的缺失值筛选出，赋值给变量quanNull
quanNull= data[data["订单量"].isnull()]
# TODO 使用drop()函数，将包含所有"订单量"这一列缺失值的行删除
data.drop(index=quanNull.index, inplace=True)
# TODO 使用info()函数，快速浏览数据集
#data.info()

# 2. 识别并处理异常值
# 2.1. 识别并处理缺失值
#quanNull= data[data["订单量"].isnull()]
#data.drop(index=quanNull.index, inplace=True)

# 2.2. 识别并处理异常值
# 查看data的描述性统计信息
#print(data.describe())
data = data[(data["订单量"]>0) & (data["订单量"]<100000000)]

# 3. 识别并处理重复值
#如果使用print()输出的是一个Empty DataFrame，代表是一个空DataFrame，说明没有重复的行，则不需要处理。
dup = data[data.duplicated()]

# 4. 数据类型转换
# TODO 使用pd.to_datetime()函数，将"订单日期"列的数据转化为时间格式
data["订单日期"]=pd.to_datetime(data["订单日期"])

# 使用print()输出data["订单日期"]
#print(data["订单日期"])


'''销售情况分析'''
# 1. 分析不同月份销售情况
# 使用data["订单日期"].dt.year获取 "订单日期" 这列数据的年
# 并作为data中的新列
data["年份"] = data['订单日期'].dt.year

# 为了在处理过程中更加方便，我们通常会把数据中时间格式的列作为行索引index后，再进行重采样。
# 使用set_index()函数，把"订单日期"列设置为index
data = data.set_index("订单日期")

#接下来，就可以对销售额完成分组、重采样和聚合操作。
#先对data["销售额"]使用groupby()函数，按照data["年份"]进行分组，这样最后的结果里就只会有销售额，不包含其它无关信息，比如订单量等。
#再按月（"M"）进行重采样，最后求和。
#新版 Pandas 中，resample("M") 写法已被废弃，不再支持，按月重采样需要改用 ME（MonthEnd，月末聚合）；
#同理: MS = MonthStart（月初）旧版简写 M 被移除，是版本迭代带来的语法变动。

# TODO 使用groupby()、resample()和sum()函数
# 计算每年每个月的销售额总和
# 将结果赋值给变量groupByMonth

groupByMonth=data["销售额"].groupby(data["年份"]).resample("ME").sum()

# 输出groupByMonth
#print(groupByMonth)

# 输出data
#print(data)

# 依次提取2018、2019、2020和2021对应的销售额数据
year_2018 = groupByMonth.loc[2018]
year_2019 = groupByMonth.loc[2019]
year_2020 = groupByMonth.loc[2020]
year_2021 = groupByMonth.loc[2021]

# 使用print()输出变量year_2021
print(year_2021)
