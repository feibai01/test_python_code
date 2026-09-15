#定义身高体重变量并赋值
height=1.75
weight=65

#计算BMI指数
BIM=weight/(height*height)

#通过if比较BMI指数确定范围并输出
if BIM <= 18.5:
    print("过轻")
if BIM > 32:
    print("非常肥胖")
if 18.5 < BIM <=24:
    print("正常")
if 24 < BIM <= 28:
    print("过重")
if 28 < BIM <= 32:
    print("肥胖")