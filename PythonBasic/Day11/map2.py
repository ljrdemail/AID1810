def power2(x, y):
    return x ** y


# for x in map(power2, range(1, 5), range(4, 0, -1)):  # 注意 有几个可迭代对象 函数也要有几个形参
#     print(x)


for x in map(power2, range(1, 10), range(4, 0, -1)):  # 注意 按照数少的参数决定跑几次 即是前面的 有9个 因为后面只有4个 没有配对的 也停止
    print(x)
