def judge(a,b,c):
    if a*a+b*b==c*c:
        return f"以{a},{b},{c}为边的三角形是直角三角形"
    else:
        return f"以{a},{b},{c}为边的三角形不是直角三角形"
print(judge(3,4,5))
print(judge(4,6,9))