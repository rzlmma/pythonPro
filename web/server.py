# -*- coding:utf-8 -*-

import socket

host = ''
port = 51423
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(2)
print "server is running on port %d"%(port)

while True:
    clientsocket, clientaddr = s.accept()
    print "clientaddr:",clientaddr
    fd = clientsocket.makefile('rw',0)
    fd.write('welcome' + str(clientaddr) + '\r\n')
    fd.write('please enter a string:')
    line = fd.readline().strip()
    fd.write('you enter %d characters'%(len(line)))
    fd.close()
    clientsocket.close()