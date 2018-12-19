# -*- coding:utf-8 -*-
#total_count = 0
class Human:
    total_count = 0  # 类变量 用来记录此类的实例的个数 用来实现对象的自动计数

    def __init__(self):
        #global total_count
        #total_count+=1
        self.__class__.total_count += 1  # 通过全局变量也能实现 但是如果放在外面 就不光是这个类单独所属的 按照面向对象编程 属于谁的 就放在那里 不要什么都放在全局

    def __del__(self):
        self.__class__.total_count -= 1

    def sleep(self):
        '''注 方法名也属于类变量'''
        pass


h1 = Human()
h2 = Human()

L = [Human() for x in range(100)]

print("现在有实例的个数是：", Human.total_count)
#print("现在有实例的个数是：", total_count)

del (h1)

del L[50:]
print("现在有实例的个数是：", Human.total_count)

del L

print("现在有实例的个数是：", Human.total_count)
