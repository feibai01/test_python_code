num=eval(input("请输入一个数："))
for i in range(2,num):
    if num%i==0:
        print(False)
        break
else:
    print(True)
