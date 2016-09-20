# -*- coding:utf-8 -*-
"""
发送邮件
"""
import smtplib,logging,datetime
from email.mime.text import MIMEText

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Email')

sender = "majingrzl@163.com"
reciver = ['yanghongxingzzu@163.com']
host = 'smtp.163.com'
port = 25
msg = MIMEText('this is a smtplib email')
msg['Form'] = 'xxx@163.com'
msg['To'] = 'xxx@163.com'
msg['Subject'] = 'replay email'
msg['Date'] = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')


smtp = smtplib.SMTP()
try:
    code, message = smtp.connect(host,port)
    smtp.set_debuglevel(True)
    rest = smtp.verify(sender)
    smtp.ehlo(host)
    if smtp.has_extn('STARTTLS'):
       smtp.starttls()
       smtp.ehlo(host)


    smtp.login(sender,'xxxx')
    smtp.sendmail(sender, [reciver], msg.as_string())
    logger.info('send email success')
except Exception,e:
    logger.error(e)
finally:
    smtp.quit()

