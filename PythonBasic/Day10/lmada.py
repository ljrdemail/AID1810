# def myadd(x, y):
#     return x + y


# print("20+30=", myadd(20, 30))
myadd = lambda x, y: x + y  # 返回值是一个函数，只能写简单的函数
print("20+30=", myadd(20, 30))
print("ABC+123=", myadd("ABC", "123"))
