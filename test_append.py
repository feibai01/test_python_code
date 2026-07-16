#定义一个空列表allInfo
#allInfo=[]
#Info1=("Max","21","female")
#Info2=("Tom","23","male")
#Info3=("Jerry","22","male")

#使用append追加
#allInfo.append(Info1)
#allInfo.append(Info2)
#allInfo.append(Info3)

#输出allInfo
#print(allInfo)

# 设置列表nameList
nameList = ["xiaofang", "xiaofei", "xiaobai"]
# 空列表newList
newList = []

# TODO for循环遍历列表nameList，将元素赋值给name
for name in nameList:
    # 字符串拼接"Hi~"+name,赋值给word
    word="Hi~"+name
    # 将word追加到列表newList
    newList.append(word)

# print()输出newList
print(newList)