# 创建多进程的TCP并发

from socketserver import *


# 创建服务器类,TCP+多进程并发
# Python支持多继承,
class Server(TCPServer, ForkingMixIn):
    pass


# 创建处理请求的类,继承 StreamRequestHandler
class Handler(StreamRequestHandler):
    # 重写handle方法
    def handle(self):
        # client_address 属性 客户端地址
        print(self.client_address, "连接过来")
        while True:
            # 属性:self.request 客户端的套接字
            data = self.request.recv(1024)
            if not data:
                break;
            print(data.decode())
            self.request.send("服务器收到".encode())


# 创建服务器对象,第二个参数指定由哪个类处理客户端请求
server = Server(('0.0.0.0', 8888), Handler)

# 启动
server.serve_forever()
