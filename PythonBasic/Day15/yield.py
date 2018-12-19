def myyield():
    print("即将生成2")  # 如果不调用 it.next()也不执行
    yield 2  # 包含了yield（一条或多条） 语句 就是生成器函数 返回的就不是None 是内存空间
    print("即将生成3")
    yield 3
    print("即将生成5")
    yield 5
    print("即将生成7")
    yield 7

    print("生成结束")  # 加了yield之后 这句话就不打印了


gen = myyield()  # 绑定的是生成器函数
print(gen)  # None
it = iter(gen)  # 向生成器来获取迭代器
print(next(it))  # 调用next之后 生成器函数才开始执行 要数据的说才生成 2 并返回调用函数 不自动往下执行 并记住当前指定到哪里了
print(next(it))  # 生成3 再次调用 往下走返回3
print(next(it))  # 生成5 再次调用 往下走返回5
print(next(it))  # 生成7 再次调用 往下走返回7
print(next(it))  # 没东西了 会打印“生成结束”这一句  并 会报StopIteration
