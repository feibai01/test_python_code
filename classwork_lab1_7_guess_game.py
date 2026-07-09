import random
n=random.randint(1,1000)
count=0
while True:
    try:
        g=eval(input("请输入一个数："))
        count +=1
    except:
        print("输入无效")
        continue
    if g>n:
        print("猜大了")
    elif g<n:
        print("猜小了")
    else:
        print("猜对了")
        break
print(count)
