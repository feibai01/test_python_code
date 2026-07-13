# 从PIL模块中导入类Image、ImageFont和ImageDraw
from PIL import Image, ImageFont, ImageDraw
# 使用Image类的open()方法打开图片，赋值给变量img
img = Image.open(r"C:\Users\feiba\Desktop\抠图\IMG_053_01.jpg")
# TODO 使用ImageFont类的方法truetype读取字体,赋值给变量font
font=ImageFont.truetype(r"C:\Windows\Fonts\simsun.ttc",size=32)
# TODO 将图片img创建为临时画布，赋值给变量draw
draw=ImageDraw.Draw(img)
# TODO 在临时画布draw上，使用text方法，绘制文字信息
draw.text(xy=(800,600),text="2026-7",fill="white",font=font)
# TODO 展示图片img
img.show()