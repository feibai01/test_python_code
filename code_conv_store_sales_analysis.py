# 使用import导入pandas模块，简称为pd
import pandas as pd

'''读取文件'''
data = pd.read_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\junjun\store.csv")

'''数据的处理与清洗'''
# 1. 识别并处理缺失值
quanNull= data[data["订单量"].isnull()]
data.drop(index=quanNull.index, inplace=True)

# 2. 识别并处理异常值
data = data[(data["订单量"]>0) & (data["订单量"]<100000000)]

# 3. 识别并处理重复值
dup = data[data.duplicated()]

# 4. 数据类型转换
# TODO 使用pd.to_datetime()函数，将"订单日期"列的数据转化为时间格式
data["订单日期"]=pd.to_datetime(data["订单日期"])

# 使用print()输出data["订单日期"]
print(data["订单日期"])