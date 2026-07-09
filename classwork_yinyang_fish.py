import turtle as t
t.speed(10)
t.pensize(3)

# 画外圆
t.penup()
t.goto(0, -100)
t.pendown()
t.circle(100)

# 画阴阳鱼
t.fillcolor("black")
t.begin_fill()
t.circle(100, 180)
t.circle(50, 180)
t.circle(-50, 180)
t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.circle(-100, 180)
t.circle(-50, 180)
t.circle(50, 180)
t.end_fill()

# 画两个小圆
t.penup()
t.goto(0, 50)
t.pendown()
t.fillcolor("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(0, -50)
t.pendown()
t.fillcolor("white")
t.begin_fill()
t.circle(10)
t.end_fill()

t.hideturtle()
t.done()

