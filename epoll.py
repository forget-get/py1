# coding=utf-8
# IO多路复用epoll来显示我们的并发服务器
import socket
import selectors    # IO多路复用选择器的模块

epoll_selector = selectors.EpollSelector()   # 实力化一个和epoll通信的选择器
# epoll_selector = selectors.DefaultSelector()  #根据系统自动选择通信器

server = socket.socket()    # 生成套接字
server.bind(('',7788))  # 指定端口
server.listen(1000)  # 开启监听

def read(conn):     # 传的对等连接套接字
    recv_data = conn.recv(1024)  # 接收数据
    if recv_data:   # 如果recv_data有数据就执行下面的代码，没有就执行else
        print(recv_data)
        conn.send(recv_data)    # 返回接收的数据
    else:
        epoll_selector.unregister(conn)  # 处理完数据后就不需要再监控了，就关闭监控
        conn.close()

def accept(server):     # 传一个监听套接字
    conn,addr = server.accept() # 当有连接过来的时候，生成对等连接套接字
    # 接收数据
    epoll_selector.register(conn, selectors.EVENT_READ,read)    # 注册事件，固定格式


epoll_selector.register(server, selectors.EVENT_READ, accept)   # 注册可读事件,当有连接过来的时候会被触发调   srever是套接字；accept是个回调函数
# 这个事件什么时候会被触发？当有连接过来的时候
# 上面写的代码不会自己主动执行，需要我们自己去查询，查出来之后我们自己给它执行一下

while True:  # epoll事惰性的，所以我们要自己去查询它，查出来自己执行这个回调函数
    events = epoll_selector.select()    #查询所有已经准备好的事件
    # 返回一个二元次元祖的列表
    for key,mask in events: # 拆包
        callback = key.data # 取出回调函数；key.data 相当于一个函数体
        sock = key.fileobj  # 取出套接字；key.fileobj 相当于一个套接字
        callback(sock)   # 回调函数



