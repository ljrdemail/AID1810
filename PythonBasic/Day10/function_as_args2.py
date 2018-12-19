def goodbye(L):
    for x in L:
        print("再见:", x)


def hello(L):
    for x in L:
        print("你好:", x)


def fx(fn, L): #把fn的地址和列表传入fx函数
    fn(L)


fx(hello, ["Tom", "Jerry", "Spike"])
fx(goodbye, ["上海", "北京", "深圳"])
