#-*-coding:utf-8-*-
# Author:Lu Wei

import socket

sk=socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

with open('aaa',mode='w',encoding='utf-8') as f:
    conn,addr=sk.accept()
    data =conn.recv(1024).decode('utf-8')
    print(data)
    f.write(data)

