#-*-coding:utf-8-*-
# Author:Lu Wei

import socket

sk=socket.socket()
sk.connect(('127.0.0.1',9000))
with open('cccc',mode='r',encoding='utf-8') as f:
    data=f.read()
    sk.send(data.encode('utf-8'))
    # for i in f:
    #     data=f.read()
    #     sk.send(data.encode('utf-8'))
