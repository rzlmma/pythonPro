# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
"""
服务器端  exit退出
"""
import socket

HOST = '127.0.0.1'
PORT = 8808
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
client, address = server.accept()
# 通信
while 1:
    data = client.recv(1024)
    print "server receive data:%s"% data
    if data == 'exit' or not data:
        break
    input = raw_input("server: ")
    client.send(input)
client.close()

