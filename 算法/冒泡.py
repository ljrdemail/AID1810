# -*- coding:utf-8 -*-
import random

l2 = list()


def sort(l):
    for i in range(0, len(l) - 1):
        for j in range(0, len(l) - 1 - i):
            if l[j] > l[j + 1]:
                tmp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = tmp


list = [x for x in range(1, 101)]

random.shuffle(list)
print(list)

sort(list)

print(list)
