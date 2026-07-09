a,b=eval(input("请输入两个数："))
x=a
y=b
while b != 0:
    r=a%b
    a=b
    b=r
min=a
max=x*y//min
print("最大公约数是：{}".format(min))
print("最小公倍数是：{}".format(max))
