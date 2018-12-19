zc = lambda n: (n ** 2 + 1) % 5 == 0
# 等同于
# def zc(n):
#     return (n ** 2 + 1) % 5 == 0


print(zc(3))
print(zc(4))
