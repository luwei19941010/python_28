#-*-coding:utf-8-*-
# Author:Lu Wei

import socket,hashlib
sk=socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

d={'username':'luwei','password':'202cb962ac59075b964b07152d234b70'}
conn,addr=sk.accept()
conn.send('username:'.encode('utf-8'))
username=conn.recv(1024).decode('utf-8')
if d['username']==username:
    conn.send('password:'.encode('utf-8'))
    password=conn.recv(1024).decode('utf-8')
    if password==d['password']:
        conn.send('Login OK:'.encode('utf-8'))
