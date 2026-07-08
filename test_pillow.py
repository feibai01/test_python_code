# 从PIL模块中导入类Image、ImageFont和ImageDraw
from PIL import Image,ImageFont,ImageDraw
# 使用Image类的open()方法打开图片，赋值给变量img
picture=r"C:\Users\feiba\Desktop\抠图\IMG_053_01.jpg"
img = Image.open(picture)
# 使用ImageFont类的方法truetype读取字体，赋值给变量font
font = ImageFont.truetype(r"C:\Windows\Fonts\simsun.ttc",size=36)
# 将图片img创建为临时画布，赋值给变量draw
draw = ImageDraw.Draw(img)
# 在临时画布draw上，使用text方法，绘制文字信息
# 要求：字体起始位置(360,420)，文字内容为@feibai01，填充颜色为white，字体样式为加载好的font
draw.text(xy=(360,420),text="@feibai01",fill="white",font=font)
# 展示图片img
img.show()
# 将处理后的img保存到路径r"C:\Users\feiba\Desktop\抠图\IMG_053_01_01.jpg"
img.save(r"C:\Users\feiba\Desktop\抠图\IMG_053_01_01.jpg")