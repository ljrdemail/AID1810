# -*- coding:utf-8 -*-
class Human:
    total_count = 0  # 类变量 用来记录此类的实例的个数


print(Human.total_count) #类的变量可以通过该类直接访问

Human.total_count = 100
print(Human.total_count)
