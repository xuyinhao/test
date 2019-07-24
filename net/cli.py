from socket import *
from time import ctime

HOST='192.168.1.102'
PORT=12345
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while  True:
    data= input(">>>")
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    new = tcpCliSock.recv(BUFSIZE)
    print(new.decode('utf-8'))
tcpCliSock.close()