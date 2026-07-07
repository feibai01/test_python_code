# TODO 导入模块 random
import random
# TODO 生成1到6的随机整数，赋值给player
player=random.randint(1,6)
# TODO 生成1到6的随机整数，赋值给computer
computer=random.randint(1,6)

print(f"玩家丢出{player}点")
print(f"电脑丢出{computer}点")

# TODO 通过if-elif-else语句判断玩家和电脑的输赢
if player > computer:
    print("玩家胜利，电脑弱爆了")
elif player == computer:
    print("平局，再来一盘")
else:
    print("电脑胜利，决战到天亮！")