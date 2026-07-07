# 导入模块 datetime
from datetime import datetime
# 使用模块datetime中的类datetime的now方法获取当前日期时间，赋值给nowTime
nowTime = datetime.now()
print(nowTime)
#获取当前日期的年份，赋值给nowYear
nowYear=nowTime.year
#获取当前日期的月份，赋值给nowMonth
nowMonth = nowTime.month
#格式化输出：现在是xxxx年x月，我在学习编程。
print(f"现在是{nowYear}年{nowMonth}月，我在学习编程。")
