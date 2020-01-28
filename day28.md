day28

### 今日内容：

- socket
  - tcp
  - udp

#### tcp协议

​	I/O操作 （input，output)操作，输入和输出是相对内存来说的

- write send  -output
- read recv   -input

基础

server：

```
import socket

sk=socket.socket(type=socket.SOCK_STREAM)
sk.bind(('127.0.0.1',9000))
sk.listen()
conn,addr=sk.accept()
msg=conn.recv(1024)
print(msg.decode('utf-8'))
conn.send('helld'.encode('utf-8'))
conn.close()
sk.close()
```

client：

```
import socket

sk=socket.socket(type=socket.SOCK_STREAM)
sk.connect(('127.0.0.1',9000))
sk.send('123'.encode('utf-8'))
msg=sk.recv(1024)
print(msg.decode('utf-8'))
```

