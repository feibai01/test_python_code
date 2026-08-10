# 导入pandas模块，简称为pd
import pandas as pd  

# TODO 使用read_csv()函数，sep参数，header参数，names参数和usecols参数
# 读取路径为"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\ratings.csv"的文件
# 设置参数分隔符号sep="::"
# 重点增加 engine="python" 支持 sep="::"

# 传入参数header = None和names = ["用户id","电影id","评分","评分时间"]，设置columns
# 传入参数usecols = ["用户id","电影id","评分"]，读取指定列
# 将结果赋值给变量ratings
ratings=pd.read_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\ratings.csv",sep="::",header=None,names=["用户id","电影id","评分","评分时间"],usecols=["用户id","电影id","评分"],engine="python")

# TODO 使用to_csv()函数，将处理好的ratings保存至"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\ratings01.csv"，传入参数index = False不将行索引信息写入第一列
ratings.to_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\ratings01.csv",index=False)

# 输出查看ratings
#print(ratings)

# 读取路径为"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movies.csv"的文件
movies = pd.read_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movies.csv",usecols = ["电影id","电影名"])

# 将处理好的movies保存至"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movies01.csv"
movies.to_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movies01.csv",index = False)

# 输出查看movies
#print(movies)

# TODO 使用merge()函数将ratings和movies按照电影id这一列连接起来
movieRatings=pd.merge(ratings,movies)

# 输出查看movieRatings
#print(movieRatings)

# 使用pivot_table()函数创建数据透视表
# 设置行索引index为"电影名"，列索引columns为"用户id"
# 值values为"评分"，并将结果赋值给userRatings变量
userRatings = movieRatings.pivot_table(index = "电影名", columns = "用户id", values = "评分") 

# 输出查看透视表userRatings
print(userRatings)