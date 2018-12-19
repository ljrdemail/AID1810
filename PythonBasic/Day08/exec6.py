L = list()


def input_number(num):
    return L.append(num)


while True:
    num = int(input("请输入整数，以负数结束:"))
    if (num < 0):
        break
    else:
        input_number(num)

print("列表为：",L)
print("最大值为：", max(L))
print("最小值为：", min(L))
print("和为：", sum(L))
