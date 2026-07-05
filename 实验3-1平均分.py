import random
s=[]
for i in range(1,11):
    n=random.randint(1,100)
    s.append(n)
s.sort(reverse=False)
print("十个评委的评分：",s)
s.remove(max(s))
s.remove(min(s))
average=sum(s)/8
print("平均分为：{:.2f}".format(average))

