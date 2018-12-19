# -*- coding:utf-8 -*-
class Human:
    total_count = 0  # 类变量 用来记录此类的实例的个数 用来实现对象的自动计数



h1 = Human()
h1.__class__.total_count = 100 #h1.class等同于human.total_count 所以被修改了
print(h1.total_count) #100

print(Human.total_count) #100

h2=Human()

