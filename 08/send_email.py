import smtplib
from email.message import EmailMessage

SENDER_EMAIL = 'your_email@yourmail.com'  # 替换为你的邮箱地址
SENDER_PASSWORD = 'your_email_password'  # 替换为你的邮箱密码

def build_email(sender, receiver, subject, body):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.set_content(body)
    return msg

def send_email(receiver_email, subject, body):
    msg = build_email(SENDER_EMAIL, receiver_email, subject, body)
    server = smtplib.SMTP_SSL('smtp.qq.com', 465) # 替换为你的SMTP服务器地址和端口
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()


# 解决方案视频中使用的命令，仅供参考
# if __name__ == '__main__':
#     # 替换接收者邮箱地址
#     send_email('RECEIVER@EMAIL.COM', 'Notification', 'Everything is awesome!')
