# -*- coding:utf-8 -*-

import socket, sys

host = sys.argv[1]
port = 70
filename = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

fd = s.makefile('rw', 0)
fd.write(filename + '\r\n')

for line in fd.readlines():
    print "line:",line


