def fun(ls,target,low,high):
    if low>high:
        return False
    mid=(low+high)//2
    if ls[mid]==target:
        return True
    elif ls[mid]>target:
        return fun(ls,target,low,mid-1)
    else:
        return fun(ls,target,mid+1,high)
ls=[7,9,12,34,57,89,123,221,345,456]
target=eval(input("请输入目标值："))
s=fun(ls,target,0,len(ls)-1)
if s:   
    print("目标值{}找到了".format(target))
else:
    print("没有找到目标值")

    
