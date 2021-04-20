# 1. 导入相关库和方法
import smtplib
import email

# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 2. 设置邮箱域名、发件人邮箱、授权码、收件人邮箱
# SMIP服务器
mail_host = "smtp.126.com"
# 发件人游戏
mail_sender = "wyshishui@126.com"
# 邮箱授权码
mail_license = "OGIXYKIWKBHRHRGD"
mail_receivers = ["904559896@qq.com"]

# 3. 构建MIMEMUltipart对象代表邮箱本身，可以往里面添加文字、图片、附件...
mm = MIMEMultipart('related')

# 4. 设置邮件头部内容
# 邮件主题
subject_content = """python邮件测试"""
# 设置发送者
mm["Form"] = "sender_name<wyshishui@126.com>"
# 设置接受者
mm["To"] = "receiver_1_name<904559896@qq.com>"
# 设置邮件主题
mm["Subject"] = Header(subject_content, 'utf-8')

# 5. 添加正文文本
# 邮件正文内容
body_content = """你好！ 这是一个测试邮件"""
# 构造文本
message_text = MIMEText(body_content,"plain","utf-8")
# 向MIMEMultipart对象中添加文本对象
mm.attach(message_text)

# 6. 添加图片
# 二进制读取图片
image_data = open('a.jpg', 'rb')
# 设置读取获取二进制数据
message_image = MIMEImage(image_data.read())
# 关闭刚才打开的文件
image_data.close()
# 添加图片文件到邮件信息当中去
mm.attach(message_image)

# 7. 添添加附件（excel表格）
# 构造附件
atta = MIMEText(open('sample.xlsx', 'rb').read(), 'base64', 'utf-8')
# 设置附件信息
atta["Content-Disposition"] = 'attachment; filename="sample.xlsx"'
# 添加附件到邮件信息当中去
mm.attach(atta)

# 8. 发送邮件
# 创建SMTP对象
stp = smtplib.SMTP()
# 设置发件人邮箱域名和端口，端口地址25
stp.connect(mail_host, 25)
# set_debuglevel(1) 可以打印和SMTP服务器交互的所有信息
stp.set_debuglevel(1)
# 登录邮箱，传递参数1：发件人邮箱地址，参数2：发件人邮箱地址，参数3：把邮件内容格式改为str
stp.sendmail(mail_sender, mail_receivers, mm.as_string())
# 关闭SMTP对象
stp.quit()