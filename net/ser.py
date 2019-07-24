from socket import *
from time import ctime

HOST='192.168.1.102'
PORT=12345
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting connection")
    tcpCliSock,addr = tcpSerSock.accept()
    print('...connected from:',addr)
    while True:
        data = tcpCliSock.recv(BUFSIZE)
        print(data)
        if not data:
            break
        tcpCliSock.send(bytes(ctime(),'utf-8') + b"\nValue: "+data)
    tcpCliSock.close()
tcpSerSock.close()