# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
"""
客户端  exit退出
"""
import socket

HOST = 'localhost'
PORT = 8808

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 12)
client.connect((HOST, PORT))
while 1:
    input = raw_input("client: ")
    client.send(input)

    data = client.recv(1024)
    print "client receive data:%s" % data
    if data == 'exit' or not data:
        break
client.close()

