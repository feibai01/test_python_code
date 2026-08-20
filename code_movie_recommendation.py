# 导入pandas模块，简称为pd
import pandas as pd  

# TODO 使用read_csv()函数，sep参数，header参数，names参数和usecols参数
# 读取路径为"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\ratings.csv"的文件
# 设置参数分隔符号sep="::"
# 重点增加 engine="python" 支持 sep="::"

# 传入参数header = None和names = ["用户id","电影id","评分","评分时间"]，设置columns
# 传入参数usecols = ["用户id","电影id","评分"]，读取指定列,若不传入则以names为准
# 将结果赋值给变量ratings
#ratings=pd.read_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\ratings.csv",
                    #sep="::",
                    #header=None,
                    #names=["用户id","电影id","评分","评分时间"],
                    #usecols=["用户id","电影id","评分"],
                    #engine="python"
                    #)

# TODO 使用to_csv()函数，将处理好的ratings保存至"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\ratings01.csv"，传入参数index = False不将行索引信息写入第一列
#ratings.to_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\ratings01.csv",index=False)

# 输出查看ratings
#print(ratings)

# 读取路径为"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\movies.csv"的文件
#movies = pd.read_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\movies.csv",
                     #usecols = ["电影id","电影名"]
                     #)

# 将处理好的movies保存至"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\movies01.csv"
#movies.to_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\movies01.csv",index = False)

# 输出查看movies
#print(movies)

#####################################################################

# 读取并处理路径为r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\ratings01.csv"的数据集，将结果赋值给变量ratings
ratings01 = pd.read_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\ratings01.csv")
# 读取路径为r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\movies01.csv"的数据集，将结果赋值给变量movies
movies01 = pd.read_csv(r"D:\tools\编程\VSCODE\python_vscode\练习所需文件\movie\movie\movies01.csv")
# TODO 使用merge()函数将ratings和movies按照电影id这一列连接起来
movieRatings=pd.merge(ratings01,movies01)

# 输出查看movieRatings
#print(movieRatings)

# 使用pivot_table()函数创建数据透视表
# 设置行索引index为"电影名"，列索引columns为"用户id"
# 值values为"评分"，并将结果赋值给userRatings变量
userRatings = movieRatings.pivot_table(index = "电影名", columns = "用户id", values = "评分") 

# 输出查看透视表userRatings
#print(userRatings)

# 2. 计算用户间的相关系数
# corr()函数，计算列与列之间非空数据的相关系数
# method：指定相关性计算方法，可选值包括： 
#'pearson'：默认方法，适用于线性数据，计算皮尔逊相关系数。 
#'kendall'：适用于分类变量或无序序列，计算肯德尔相关系数。 
#'spearman'：适用于非线性或非正态分布数据，计算斯皮尔曼相关系数。
# min_periods：指定计算相关性所需的最小样本数量。

# 使用corr()函数，计算userRatings的皮尔逊相关系数
# 传入参数method="pearson"，min_periods=10
# 将结果赋值给变量corrMatrix
corrMatrix = userRatings.corr(method="pearson", min_periods=10)


# 3. 寻找相似用户
# 3.1 获取「用户1」与其他用户之间的皮尔逊相关系数，并赋值给userCorr
userCorr = corrMatrix[1].drop(index=1)

# 输出查看userCorr
#print(userCorr)

# TODO 3.2 获取最大值对应的索引，并赋值给变量mostCorrUser
mostCorrUser=userCorr.idxmax()

# 输出查看mostCorrUser
#print(mostCorrUser)

# 4. 筛选可推荐电影
# 4.1 获取相似用户的电影评分数据
targetMovie = userRatings[mostCorrUser]

# 4.2 获取相似用户评分为5的电影
targetMovie = targetMovie[targetMovie.values==5]

# 4.3 获取目标用户评分过的电影
user1Ratings = userRatings[1].dropna()


# 输出查看user1Ratings
#print(user1Ratings)

# 4.4 删除目标用户看过的电影
# 获取相似用户评分为5的电影名称，并赋值给targetName
targetName = targetMovie.index

# 获取目标用户评分过的电影名称，并赋值给user1Name
user1Name = user1Ratings.index

# 输出查看targetName
#print(targetName)

# 输出查看user1Name
#print(user1Name)

# 筛选「用户1」未评分过的电影名称
movieList = targetName[~targetName.isin(user1Name)]

# 输出movieList
#print(movieList)