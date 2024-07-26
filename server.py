#!/usr/bin/python3 
import socket 
from base64 import encode 
import threading


bind_ip = "127.0.0.1"
bind_port = 9999

serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv.bind((bind_ip,bind_port))
serv.listen()
print("server is running ...")





#functions to threading req clinet 
def handler_clt_thread(clt_socket):
    req = clt_socket.recv(1024)
    print("Recive %s"%req)
    clt.send("you connceted to server !".encode())
    clt_socket.close()





 
#a loop for recive request many time and sende message for clinet and server 
while True :
    clt,addr = serv.accept()
    
    print("new connections %s"%str(addr))

    clt_handler = threading.Thread(target=handler_clt_thread , args=(clt,))

    clt_handler.start()
