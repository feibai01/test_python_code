#导入模块 random
import random

# TODO 生成0到1的随机浮点数，并输出
#print(random.uniform(0,1))

#randint函数，可以产生指定范围的随机整数。整数的范围，由randint函数中的参数决定。
# TODO 生成一个从1到10的随机整数，并输出
#print(random.randint(1,10))

#choice函数, random模块的choice函数，可以从序列中随机选取一个元素。
option = ["石头","剪刀","布"]
print(random.choice(option))
