def fun(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
count=0
for j in range(2,1001):
    if fun(j):
        print(j,end=" ")
        count +=1
print("1000以内素数的个数是：{}".format(count))
