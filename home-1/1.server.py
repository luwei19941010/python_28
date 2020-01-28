#-*-coding:utf-8-*-
# Author:Lu Wei
import socket

sk=socket.socket(type=socket.SOCK_STREAM)
sk.bind(('127.0.0.1',9000))
sk.listen()
while True:
    conn,addr=sk.accept()
    conn.send('server:'.encode('utf-8'))
    cmsg=conn.recv(1024).decode('utf-8')
    while True:
        msgall=conn.recv(1024).decode('utf-8')
        if msgall.upper() == 'N': break
        if cmsg=='6693969502:':
            print('\033[1;32;41m', '%s:' % cmsg, msgall, '\033[0m')
        else:
            print('\033[1;32;43m', '%s:' % cmsg, msgall, '\033[0m')
        inp=input('send to %s'%cmsg)
        conn.send(inp.encode('utf-8'))
        if inp.upper()=='N':break
    conn.close()

sk.close()
