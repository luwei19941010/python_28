#-*-coding:utf-8-*-
# Author:Lu Wei
import socket
sk=socket.socket(type=socket.SOCK_DGRAM)
while True:
    inp=input('sendto :')
    if inp.upper() == 'N': break
    inp=('b|'+inp).encode('utf-8')
    sk.sendto(inp,(('127.0.0.1',9000)))
    smsg=sk.recv(1024).decode('utf-8')
    print(smsg)