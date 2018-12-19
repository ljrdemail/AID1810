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

a=A()
print(a.get_v()) #a.__class__传入 装饰器干的 转为对象的class
a.set_v(200)
print(a.get_v())
print(A.v)

