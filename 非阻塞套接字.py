# coding=utf-8
# 完成非阻塞套接字实现并发服务器（同时服务多个客户端）
# 整体思路：吃满cpu，不让cpu闲置（空闲的时候去做点别的事）
import socket
sever = socket.socket() # 实例化，生成一个套接字
sever.setblocking(False)    # 设置成非阻塞套接字（不让对等套接字阻塞）
sever.bind(('', 9999))  # 指定端口
sever.listen(1000)  # 开启监听，最多1000个

all_con = []    # 来保存所有的已经生成的对等套接字（这个客户端还在连接）
while True:
    try:
        con, addr = sever.accept()   # 非阻塞生成对等连接套接字
        con.setblocking(False)  # 设置非阻塞（不让接收阻塞）
        all_con.append(con)  # 把新连接的添加到这个表中
    except BlockingIOError:     # 没有连接的直接过，继续循环
        pass
    for con in all_con:  # 假设已经有了连接，没有也不会报错
        try:
            a = con.recv(1024)

            if a:   # 如果a有东西就执行下面的代码，如果没有东西就执行else的代码
                print(a.decode())
                con.send(a)     #返回发来的东西
            else:
                con.close()
                all_con.remove(con) # 没有连接了就让他退出去（删除不需要再服务的）
        except BlockingIOError:
            pass
