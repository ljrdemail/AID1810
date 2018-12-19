# poll.py
# 使用poll实现IO多路复用
from socket import *
from select import *

address = ("0.0.0.0", 9999)
server = socket()
server.bind(address)
server.listen(5)
print("服务器已启动:", address)

# 字典:存放fd和socket的映射关系
fdmap = { server.fileno() : server }

p = poll()  # 创建poll对象
p.register(server, POLLIN) # 注册IO 关注server的pollin事件
# 循环监控
while True:
    events = p.poll() #阻塞,等待IO事件 跟socket区别是 返回不是三个列表是一个列表 每个列表是一根文件描述符和 IO操作的一串数字
    print(events)
    for fd,e in events:#循环处理
        sock = fdmap[fd]#通过fd取得socket对象
        # 判断就绪IO是不是监听socket
        if fd == server.fileno():#监听socket
            client,addr = server.accept()
            print("收到连接:",addr)
            p.register(client, POLLIN)#注册事件
            #将新建的socket放入映射表
            fdmap[client.fileno()]=client
        elif e & POLLIN:#判断event是否有读事件
            data = sock.recv(1024)
            if not data:
                p.unregister(fd)#从关注列表移除
                sock.close()#关闭连接
                del sock#释放对象
            else:
                print("收到数据:", data.decode())
                sock.send(b"test msg")

