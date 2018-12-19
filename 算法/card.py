# -*- coding:utf-8 -*-
import random

list = [x for x in range(1, 14)]

print(list)
random.shuffle(list)
print(list)
index = 0
for x in list:
    if x == 6:
        break
    index += 1

print("找到了:是第%d张牌" % (index + 1))
