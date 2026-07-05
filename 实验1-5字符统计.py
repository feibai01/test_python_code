s=input("请输入一行字符：")
a=b=c=d=0
for i in s:
    if "a"<=i<="z" or "A"<=i<="Z":
        a += 1
    elif "0"<=i<="9":
        b += 1
    elif i==" ":
        c += 1
    else:
        d += 1
print("其中英文字符有{}个，数字有{}个，空格有{}个，其他字符有{}个。".format(a,b,c,d))
