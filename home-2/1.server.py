#-*-coding:utf-8-*-
# Author:Lu Wei
import socket
sk=socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('127.0.0.1',9000))
l=[]
d={}
while True:
    msg,addr=sk.recvfrom(1024)
    print(addr)
    l.append(addr)
    cmsg=msg.decode('utf-8')
    a,b=cmsg.split('|')
    if b.upper()=='N':
        l.remove(addr)
    print(l)
    for i in l:
        if i ==addr:
            continue
        sk.sendto(b.encode('utf-8'),i)

