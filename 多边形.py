import turtle as t
n = int(input("请输入n（3 <= n < 10）："))
t.pensize(2)
t.pencolor("blue")
t.fillcolor("yellow")
for i in range(3, n + 1):
    t.begin_fill()
    if i < n:
        t.circle(50, steps=i)
    else:
        t.circle(50)
    t.end_fill()
    t.penup()
    t.forward(100)
    t.pendown()
3