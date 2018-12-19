# -*- coding:utf-8 -*-
class A:
    v = 0

    @classmethod
    def get_v(cls):
        # classmethod（get_v）
        # 此方法为类方法，此方法可以获取A类的类变量V的值

        return cls.v

    @classmethod
    def set_v(cls, value):
        cls.v = value


print(A.v)
print(A.get_v())  # 默认会传入A作为参数cls
A.set_v(100)
print(A.get_v())
print(A.v)
