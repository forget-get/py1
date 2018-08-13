# coding=utf-8
#服务套接字
import socket
client = socket.socket()
client.connect(('127.0.0.1',7788))    #访问服务端，服务端的ip，端口
while True:
    q = input('>>>')
    client.send(q.encode())   #发出数据，必须是字节型的
    a = client.recv(1024)   #接收数据
    print(a.decode())
    client.close()  #关闭





