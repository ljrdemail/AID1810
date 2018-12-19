# 此示例示意用for 语句来调用生成器语句
def myyield():
    print("即将生成2")  # 如果不调用 it.next()也不执行
    yield 2  # 包含了yield（一条或多条） 语句 此函数就是生成器函数 返回的就不是None 而是生成器的内存空间
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    #return
    print("即将生成7")
    yield 7

    print("生成结束")  # 加了yield之后 等yield都跑完 会报StopIteration 错误 跑不到这一句 除非 for 会处理异常 就能跑到 next(it) 跑不到


gen = myyield()  # 绑定的是生成器函数
print(gen)  # None
it = iter(gen)  # 向生成器来获取迭代器
print(next(it))  # 调用next之后 生成器函数才开始执行 要数据的说才生成 2 并返回调用函数 不自动往下执行 并记住当前指定到哪里了
print(next(it))  # 生成3 再次调用 往下走返回3
print(next(it))  # 生成5 再次调用 往下走返回5
print(next(it))  # 生成7 再次调用 往下走返回7
print(next(it))  # 没东西了 会打印“生成结束”这一句  并 会报StopIteration

for x in myyield(): #用for 语句 会自动创建迭代器 并自动next(it) 并处理最后的 StopIteration 停止迭代 并处理这个异常 不会报错
    print(x)
