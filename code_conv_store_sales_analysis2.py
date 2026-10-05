# 使用import导入pandas模块，简称为pd
import pandas as pd

'''读取文件'''
data = pd.read_csv(r"D:\tools\Programming\VSCODE\python_vscode\Files_RequiredforPractice\junjun\junjun\store.csv")

'''数据的处理与清洗'''
# 1. 识别并处理缺失值
# TODO 使用布尔索引和isnull()函数，将"订单量"的缺失值筛选出，赋值给变量quanNull
quanNull= data[data["订单量"].isnull()]
# TODO 使用drop()函数，将包含所有"订单量"这一列缺失值的行删除
data.drop(index=quanNull.index, inplace=True)

# 2. 识别并处理异常值
# 过滤订单量大于0，小于100000000
data = data[(data["订单量"]>0) & (data["订单量"]<100000000)]

# 3. 识别并处理重复值
dup = data[data.duplicated()]
# 如果存在重复行，删除重复，keep='first'保留第一次出现的行
if not dup.empty:
    data.drop_duplicates(inplace=True, keep='first')

# ========== 新增：输出清洗后的csv文件 ==========
output_path = r"D:\tools\Programming\VSCODE\python_vscode\Files_RequiredforPractice\junjun\junjun\store_cleaned.csv"
data.to_csv(output_path, index=False, encoding="utf-8-sig")
print(f"清洗完成，文件已输出至：{output_path}")
