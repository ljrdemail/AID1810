# -*- coding:utf-8 -*-
import random

l2 = list()


def sort(l):
    for i in range(0, len(l) - 1):
        flag = 0
        for j in range(0, len(l) - 1 - i):
            if l[j] > l[j + 1]:
                tmp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = tmp
                flag = 1
        if flag == 0:
            return


list = [x for x in range(1, 101)]
# https://blog.csdn.net/lu_1079776757/article/details/80459370

random.shuffle(list)
print(list)

sort(list)

print(list)
