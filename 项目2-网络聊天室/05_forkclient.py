from socket import *
import  sys

#创建TCP套接字
client=socket(AF_INET,SOCK_STREAM)


HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDRESS = (HOST,PORT)

client.connect(ADDRESS)

while  True :
     content=input("你想说：")
     client.send(content.encode())
     if not content:
         break;
     data=client.recv(1024)
     print("服务器向你说:"+data.decode())