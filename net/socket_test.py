from socket import  *
HOST="127.0.0.1"
PORT=52611
BUFSIZ=2048
ADDR=(HOST,PORT)

tcpClisock=socket(AF_INET,SOCK_STREAM)
tcpClisock.connect(ADDR)
# while   True:
# tcpClisock.send(bytes(data,encoding="utf8"))
# tcpClisock.send({cmdname="GetSystemInfoCJ", "ID"="1", "port"="30001", "MDSIPS"="10.11.12.27 10.11.12.32 ", "Role"="ls_client"})
tcpClisock.send(bytes())
data=tcpClisock.recv(BUFSIZ)
# if not data :
#     break
print(data)

tcpClisock.close()