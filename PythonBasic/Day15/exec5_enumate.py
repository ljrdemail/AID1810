# -*- coding:utf-8 -*-
def myenumerate(iterable, start=0):
    i = start  # 开始索引
    for x in iterable:
        yield (i, x)  # 生成一个元组
        i += 1


d = myenumerate("ABCDE", 1)
for i in d:
    print(i)
