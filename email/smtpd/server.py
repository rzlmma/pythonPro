# -*- coding:utf-8 -*-
"""
继承SMTPServer来实现自己的邮件发送的服务器
"""
import smtpd
import asyncore

class MySMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data):
        print "reciving mail from:",peer
        print "mail from:",mailfrom
        print "mail to:", rcpttos
        print "mail data:",data

sever = MySMTPServer(('127.0.0.1',1025), None)
asyncore.loop()
