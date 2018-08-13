# coding=utf-8
#监听套接字
import socket
sever = socket.socket() #创建一个套接字实例
sever.bind(('',8899))   #指定端口（'ip'，端口）ip不写默认为0.0.0.0
sever.listen(5) #监听最多 5 个
#拆包，生成对等连接套接字，只用conn
conn,addr = sever.accept()  #没有客户端连接就会阻塞
a = conn.recv(1024) #接收数据，1024个字节；没有收到数据也会阻塞
print(a.decode())
conn.send('嗯，吃饭了吗？'.encode())   #服务端再发数据
b = conn.recv(1024) #再次接收数据，空数据就是客户端关闭了
print(b.decode())
conn.send('哎，老师这次布置的作业完全没头脑'.encode())
conn.recv(1024)
conn.close()    #服务端关闭





