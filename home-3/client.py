#-*-coding:utf-8-*-
# Author:Lu Wei
import socket,hashlib

def md5(s):
    obj=hashlib.md5()
    obj.update(s.encode('utf-8'))
    return obj.hexdigest()
sk=socket.socket()
sk.connect(('127.0.0.1',9000))
username=sk.recv(1024).decode('utf-8')
inp=input('%s'%username).encode('utf-8')
sk.send(inp)
password=sk.recv(1024).decode('utf-8')
inp=md5(input('%s'%password)).encode('utf-8')
sk.send(inp)
ret=sk.recv(1024).decode('utf-8')
print(ret)
