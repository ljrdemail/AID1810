def myinteger(n):
    # 用来生成从0开始的一系列整数
    i = 0
    while i < n:
        yield i  # 返回给调用函数
        i += 1


# for x in myinteger(3):  # 调用一次后 n 和 i 虽然是局部变量 但是不会消失 从i+ 1继续走
#     # for x in myinteger(300000000000):#即使很大也不会死机 因为 随用随生成 立刻返回 不在内存中保存生成的数据
#     print(x)
gen1 = myinteger(3)

for x in gen1:
    print(x)
print("+++++++++++++")
# 再跑一次
for x in gen1:
    print(x)  # 什么都没有打印 因为上一个 已经跑到头了 直接 stopIteration 了所以没有打印

print("------------第二种写法------------")
for x in myinteger(4):  # 区别是  gen1=myinteger(3) 然后 in gen1 因为下面调用了两次 myinteger(4) 产生了两次生成器 但是gen1 只生成一次生成器
    print(x)
print("--------------------")
for x in myinteger(4):
    print(x)
