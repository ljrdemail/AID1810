'''
此示例为自定义模块
此模块内有两个函数和两个字符串
。。。。此处省略20个字


'''


def fac(n):  # 视为变量
    print("正在计算%d!的阶乘" % n)


def sum(n):
    print("正在计算%d!的和" % n)


name1 = "AUDI"  # 如果你改为TESLA 即是你再次加载 还是Audi

name2 = "BYD"

print("mymod 模块被加载,模块文件为:", __file__)
print("mymod name属性为", __name__)

if __name__ == '__main__':
    print("通过他来运行")
