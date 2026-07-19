#用 for 循环和 break 找出以下列表中出现的第一个首字母为"a"的单词，并输出。
#定义单词列表wordList
wordList=["cherry","lemon","apricot","blueberry","durian","grape","apple"]
#通过for循环选取列表元素
for word in wordList:
    #索引切片获取元素首字母，通过if循环判断是否为"a"
    if word[0]=="a":
        #输出满足条件的word
        print(word)
        #找出的第一个并跳出循环
        break
        