# -*- coding:utf-8 -*-
"""
发送邮件
存在问题没解决：  ERROR:Email:(535, 'Error: authentication failed') 邮箱的用户名和密码都是对的
"""
import smtplib,logging
import email.utils
from email.mime.text import MIMEText

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('Email')

sender = "xxx@163.com"
reciver = ['xxx@qq.com']
host = 'smtp.163.com'
port = 25
msg = MIMEText('this is a smtplib email')
msg['Form'] = 'xxx@163.com'
msg['To'] = 'xxx@qq.com'
msg['Subject'] = 'system error warning'

try:
    smtp = smtplib.SMTP()
    code,msg=smtp.connect(host,port)
    smtp.set_debuglevel(True)
    rest = smtp.verify('xxx@163.com')
    smtp.ehlo(host)
    if smtp.has_extn('STARTTLS'):
       smtp.starttls()
       smtp.ehlo(host)


    smtp.login(sender,'xxxx')
    smtp.sendmail(sender, [reciver], msg.as_string())
    logger.info('send email success')
except Exception,e:
    logger.error(e)
    smtp.quit()

