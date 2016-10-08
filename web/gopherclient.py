# -*- coding:utf-8 -*-

import socket,sys

host = sys.argv[1]
port = 70
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
except Exception,e:
    print "Error:",e
    sys.exit(1)

s.sendall(filename + '\r\n')

while True:
    data = s.recv(2048)
    if not len(data):
        break
    print "recv from service:\n",data