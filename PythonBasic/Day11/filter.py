# 打印一个可迭代对象中的所有奇数并放在一个列表中

L = range(1, 10)


def isodd(x):
    return x % 2 == 1


L2 = []
for x in filter(isodd, L):
    # print(x)
    L2.append(x)

print(L2)

L3 = [x for x in filter(isodd, L)]
print(L3)

L4 = list(filter(isodd, L))
print(L4)
