# 此示例示意 用迭代器来代替for 语句实现对可迭代对象的数据遍历
L = [11, 13, 17, 19]
for x in L:
    print(x)


print("--------------------------------------")
it = iter(L)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
