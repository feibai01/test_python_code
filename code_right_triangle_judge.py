#定义函数judge(),传入参数a,b,c
def judge(a,b,c):
    #用if语句判断是否满足条件a*a+b*b==c*c
    if a*a+b*b==c*c:
        return f"以{a},{b},{c}为边的三角形是直角三角形"
    else:
        return f"以{a},{b},{c}为边的三角形不是直角三角形"
#传入参数3，4，5调用函数judge()
print(judge(3,4,5))
#传入参数4，6，9调用函数judge()
print(judge(4,6,9))