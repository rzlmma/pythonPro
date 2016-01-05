# -*- coding:utf-8 -*-
"""
发送邮件的客户端
"""
import smtplib
from email.mime.text import MIMEText

sender = "xxx@163.com"
reciver = ['xxx@163.com']
msg = MIMEText('this is a customer to send email')
msg['From'] = sender
msg['To'] = str(reciver)
msg['Subject'] = "this is a test"


server = smtplib.SMTP('127.0.0.1',1025)
server.set_debuglevel(True)
try:
    server.sendmail(sender,reciver, msg.as_string())
finally:
    server.quit()