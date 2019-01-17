from socket import *

#创建TCP套接字
client=socket(AF_INET,SOCK_STREAM)
ip=input("请输入IP：")
port=input("请输入端口：")
address=(ip,int(port))


client.connect(address)

while  True :
     content=input("你想说：")
     client.send(content.encode())
     if not content:
         break;
     data=client.recv(1024)
     print("服务器向你说:"+data.decode())