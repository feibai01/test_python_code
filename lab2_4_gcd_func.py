def gcd(m,n):
    x=m
    y=n
    while n != 0:
        r=m%n
        m=n
        n=r
    min=m
    max=x*y//min
    return min,max
a,b=eval(input("请输入两个数："))
c,d=gcd(a,b)
print("最大公约数是{}，最小公倍数是{}".format(c,d))
