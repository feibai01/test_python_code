#定义字典classStu
classStu={"LiQiang":81,"Tony":97,"Tim":76,"Kim":97,"WangCai":44,"ShuFen":90,"Max":62,"DaHuang":55,"Kevin":85,"Gary":74}
#for循环遍历字典
for name in classStu:
    #用if判断，字典的值小于60时
    if classStu[name] < 60:
        #用格式化输出  XX同学加油！
        print(f"{name}同学加油！")