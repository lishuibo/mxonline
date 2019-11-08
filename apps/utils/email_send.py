from email.mime.text import MIMEText
import smtplib

__author__ = 'litl'
from random import Random

from users.models import EmailVerifyRecord

global send_user
global email_host
global password

email_host = "smtp.sina.com"
send_user = "litianle910124@sina.com"
password = "was123"

# 生成随机字符串
def random_str(random_length=8):
    str = ''
    # 生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str

# 发送注册邮件
def send_register_email(email, send_type="register"):
    # 发送之前先保存到数据库，到时候查询链接是否存在
    # 实例化一个EmailVerifyRecord对象
    email_record = EmailVerifyRecord()
    # 生成随机的code放入链接
        # 生成随机的code放入链接
    if send_type == 'update':
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()

    # 定义邮件内容:
    # email_title = ""
    # email_body = ""

    if send_type == "register":
        content = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)
        user = "litianle" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = "注册激活链接"
        message['From'] = user
        message['To'] = email_record.email
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, email_record.email, message.as_string())
        server.close()

    if send_type == "forget":
        content = "请点击下面的链接重置你的账号密码: http://127.0.0.1:8000/reset/{0}".format(code)
        user = "litianle" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = "忘记密码链接"
        message['From'] = user
        message['To'] = email_record.email
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, email_record.email, message.as_string())
        server.close()

    if send_type == "update":
        content = "你的邮箱验证码为{0}".format(code)
        user = "litianle" + "<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = "更改邮箱链接"
        message['From'] = user
        message['To'] = email_record.email
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, email_record.email, message.as_string())
        server.close()


if __name__ == '__main__':
    send_register_email("407378019@qq.com")