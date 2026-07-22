#用 for 循环和 break 找出以下列表中出现的第一个首字母为"a"的单词，并输出。
#定义单词列表wordList
#wordList=["cherry","lemon","apricot","blueberry","durian","grape","apple"]
#通过for循环选取列表元素
#for word in wordList:
    #索引切片获取元素首字母，通过if循环判断是否为"a"
    #if word[0]=="a":
        #输出满足条件的word
        #print(word)
        #找出的第一个并跳出循环
        #break
        
# 王老师的要求有两个：1. 不要重量小于4kg的西瓜；2. 按列表顺序挑选够3个西瓜就停止挑选。
# 请运用break和continue写一段代码为王老师挑选西瓜，并以列表的形式输出这3个西瓜的重量。
# 定义melonlist列表用于保存超市的西瓜重量
#melonList = [4, 3.5, 2, 5, 6, 3, 4.7, 5.3]
#定义一个用于计数的变量
#a=0
#定义一个用于输出三个西瓜重量的列表
#buylist=[]
#for i in melonList:
    #if i < 4:           #if语句判断西瓜重量是否小于4
        #continue        #满足条件即进入下一个循环
    #else:
        #buylist.append(i)     #若不满足条件则将西瓜重量用append函数追加至列表中
        #a=a+1           #列表追加一个，计数器加一
        #if a==3:        #if语句判断西瓜数量n是否等于3
            #break       #满足条件则跳出for循环
#print(buylist)

#记录为0则当天未背单词，记录大于0则当天已背单词。
record=[60,0,73,139,64,48,73,63,0,59,100,121,44,30,0,0,43,67,64,51,106,0,80,0,119,59,0,58,100,90]
count=0
for i in record:
    if i!=0:
        continue
    count+=1
print(f"这个月有{count}天没有背单词")