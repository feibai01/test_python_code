s=input("请输入一串字符：")
n=eval(input("加密常量："))
txt=""
for i in s:
    if "a"<=i<="z":
        key=chr(ord("a")+(ord(i)+n-ord("a"))%26)
    elif "A"<=i<="Z":
        key=chr(ord("A")+(ord(i)+n-ord("A"))%26)
    else:
        key=i
    txt=txt+key
print("密文是：",txt)
    
