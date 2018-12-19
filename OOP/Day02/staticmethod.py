# -*- coding:utf-8 -*-
class A:
    @staticmethod
    def myadd(a, b):
        return a + b


print(A.myadd(100, 200)) #用类来调用

a=A()
print(a.myadd(20,40)) #用实例访问