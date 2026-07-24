#通过1，2，3，4四个数字进行组合，一共会有多少种三位数？输出所有的三位数组合。
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            print(i*100+j*10+k)
    
        
    