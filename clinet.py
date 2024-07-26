#!/usr/bin/python3

import socket 

clt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clt.connect(("127.0.0.1",9999))

clt.send("GET / HTTP/1.1\r\nHost:127.0.0.1:9999\r\n\r\n".encode())

res = clt.recv(4096)

print (res)
