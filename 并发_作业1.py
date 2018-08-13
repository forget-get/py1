# coding=utf-8
import socket
sever = socket.socket()
sever.bind(('',8899))
sever.listen(5)

while True:
    conn, addr = sever.accept()
    while True:
        a = conn.recv(1024)
        print(a.decode())
        conn.send(a)
        if a == b'':
            conn.close()
            break

