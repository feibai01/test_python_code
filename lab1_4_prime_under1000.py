count=0
for n in range(2,1001):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n,end=" ")
        count += 1
print(count)
