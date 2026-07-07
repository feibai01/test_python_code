# 从PIL模块中导入Image类
from PIL import Image
# 使用Image类的open()方法打开图片，赋值给变量img
picture=r"C:\Users\feiba\Desktop\抠图\IMG_053_01.jpg"
img = Image.open(picture)
img.show()