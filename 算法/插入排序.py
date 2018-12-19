# -*- coding:utf-8 -*-
import random

l = []
for i in range(0, 10):
    height = random.randint(80, 100)
    l.append(height)

print(l)


def InsertSort(a):
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
            else:
                break


# 内层循环 对应遍历所有的有序数据
# 从后往前扫描
# 从当前无序数据的前一位开始
# 遍历到下表为0 包括0


InsertSort(l)
print(l)
