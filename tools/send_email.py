# -*- coding:utf-8 -*-
# __author__ = majing

import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_mail(subject, mails_to, content, mails_from=None, mails_cc=None, mails_bcc=None, atts=None, _subtype='plain'):
    """
    发送文本内容的邮件
    mails_cc: 抄送   
    mails_bcc: 暗抄送 两者的区别在于在BCC栏中的收件人可以看到所有的收件人名(TO,CC,BCC)，而在TO 和CC栏中的收件人看不到BBC的收件人名
    atts: 附件 ['xx.xlsx', 'xxx.pdf', 'xxx.jpj']
    """
    try:
        mails_from = mails_from if mails_from else 'no-reply@163.com'

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = mails_from
        msg['To'] = ';'.join(mails_to)
        if mails_cc:
            msg['Cc'] = ';'.join(set(mails_cc) - set(mails_to))
        if mails_bcc:
            msg['Bcc'] = ';'.join(set(mails_bcc) - set(mails_to) - set(mails_cc or []))

        # 创建一个邮件正文内容
        body = MIMEText(content, _subtype=_subtype, _charset='utf-8')
        msg.attach(body)

        # 添加附件
        if atts:
            for att_name in atts:
                if "http" in att_name:
                    r = requests.get(att_name)       # 如果是远程的，先下载
                    part = MIMEApplication(r.content)
                else:
                    part = MIMEApplication(open(att_name, 'rb').read())
                part.add_header('Content-Disposition', 'attachment', filename=att_name)
                msg.attach(part)

        smtp = smtplib.SMTP()
        smtp.connect('smtp.com')      # 邮箱服务器
        smtp.sendmail(mails_from, list(set(mails_to) | set(mails_cc or []) | set(mails_bcc or [])),
                      msg.as_string())
        smtp.quit()
    except Exception as exc:
        return False, str(exc)
    return True, ''


if __name__ == '__main__':
    subject1 = '测试给群组发送邮件'
    mails_to_1 = ['xxxx@163.com']
    content_1 = '有异常日志'
    pages = ["http://image.baidu.com/search/down?tn=download&word=download&ie=utf8&fr=detail&url=http%3A%2F%2Fpic33.nipic.com%2F20131007%2F13639685_123501617185_2.jpg&thumburl=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D508387608%2C2848974022%26fm%3D26%26gp%3D0.jpg",
             'Downloads/v2-77d047b1fb49d4a9d6d4536117532478_hd.jpg']
    send_mail(subject1, mails_to_1, content_1, atts=pages)
