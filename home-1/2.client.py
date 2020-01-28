#-*-coding:utf-8-*-
# Author:Lu Wei
import socket

sk=socket.socket(type=socket.SOCK_STREAM)
sk.connect(('127.0.0.1',9000))
sk.send('6693969502:'.encode('utf-8'))
smsg = sk.recv(1024).decode('utf-8')
while True:
    inp=input('send to %s'%smsg)
    sk.send(inp.encode('utf-8'))
    if inp.upper()=='N':break
    msgall=sk.recv(1024).decode('utf-8')
    if msgall.upper()=='N':break
    print('\033[1;31;40m%s'%smsg,msgall,'\033[0m')
sk.close()