def fun(r,pi=3.14):
    c=pi*r*2
    s=pi*r**2
    return c,s
r=eval(input("请输入半径："))
c,s=fun(r)
print("圆的周长是{},面积是{}".format(c,s))
