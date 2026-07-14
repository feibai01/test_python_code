#定义身高体重变量并赋值
myWeight=65
myHeight=1.75

#BMI计算公式
BIM=myWeight/(myHeight*myHeight)

#利用if elif else判断BMI范围并输出
if BIM<18.5:
    print("under weight")
else:
    if BIM<23.9:
        print("normal weight")
    elif BIM<27:
        print("over weight")
    elif BIM<32:
            print("fat")
    else:
        print("obese")