#定义字典classStu
#classStu={"LiQiang":81,"Tony":97,"Tim":76,"Kim":97,"WangCai":44,"ShuFen":90,"Max":62,"DaHuang":55,"Kevin":85,"Gary":74}
#for循环遍历字典
#for name in classStu:
    #用if判断，字典的值小于60时
    #if classStu[name] < 60:
        #用格式化输出  XX同学加油！
        #print(f"{name}同学加油！")

# 婷婷的单词表
letters1 = ["a", "bc", "def", "g", "hinj"]
# 陈陈的单词表
letters2 = ["abc", "defg", "h", "injs"]
a=""
b=""
#用for循环遍历列表，拼接字符串
for n in letters1:
    a=a+n
for m in letters2:
    b=b+m
#使用if判断
if a==b:
    print("赶快写作业")
else:
    print("去找老师评评理")