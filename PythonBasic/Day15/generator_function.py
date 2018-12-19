def myinteger(n):
    # 用来生成从0开始的一系列整数
    i = 0
    while i < n:
        yield i  # 返回给调用函数
        i += 1


for x in myinteger(3):  # 调用一次后 n 和 i 虽然是局部变量 但是不会消失 从i+ 1继续走
    # for x in myinteger(300000000000):#即使很大也不会死机 因为 随用随生成 立刻返回 不在内存中保存生成的数据
    print(x)
