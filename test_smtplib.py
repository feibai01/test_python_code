# 导入smtplib模块
import smtplib
# 从email.mime.multipart中导入MIMEMultipart类
from email.mime.multipart import MIMEMultipart
# 从email.header中导入Header类
from email.header import Header
# 从email.mime.text中导入MIMEText类
from email.mime.text import MIMEText

# 连接邮箱服务器：使用smtplib模块的类SMTP_SSL，创建一个实例对象qqMail
qqMail = smtplib.SMTP_SSL("smtp.qq.com", 465)
# 设置登录邮箱的帐号为："aLing@qq.com"，赋值给mailUser
mailUser="feibai15607935987@qq.com"
# 将邮箱授权码"abcnawckdujkdace"，赋值给mailPass 
mailPass="mpqoaquafnwdcfii"
# 登录邮箱：调用对象qqMail的login()方法，传入邮箱账号和授权码
qqMail.login(mailUser, mailPass)

# 设置发件人和收件人
sender="feibai15607935987@qq.com"
receiver = "3282742874@qq.com"
# 使用类MIMEMultipart，创建一个实例对象message
message = MIMEMultipart()
# 将主题写入 message["Subject"]
message["Subject"] = Header("团队合照")
# 将发件人信息写入 message["From"]
message["From"] = Header(f"feibai<{sender}>")
# 将收件人信息写入 message["To"]
message["To"] = Header(f"Π<{receiver}>")

# 设置邮件的内容，赋值给变量textContent
textContent = "feibai，这是插画同学绘制的团队合照，望查收~"
# 编辑邮件正文：使用类MIMEText，创建一个实例对象mailContent
mailContent = MIMEText(textContent, "plain", "utf-8")