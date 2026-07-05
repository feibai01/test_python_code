def Caesar(s,k):
    txt=""
    for i in s:
        if "a"<=i<="z":
            key=chr(ord("a")+(ord(i)+k-ord("a"))%26)
        elif "A"<=i<="Z":
            key=chr(ord("A")+(ord(i)+k-ord("A"))%26)
        else:
            key=i
        txt=txt+key
    return txt
s1=input("请输入一串字符：")
k1=eval(input("加密常量："))
newtxt=Caesar(s1,k1)
print("密文是：",newtxt)
