t=eval(input("请输入工作时长："))
if t>120:
    money=120*80+(t-120)*80*(1+0.15)
elif t<60:
    money=t*80-700
else:
    money=t*80
print("员工工资为{}元".format(money))
