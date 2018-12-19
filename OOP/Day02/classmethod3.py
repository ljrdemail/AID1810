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


a1=A()
a2=A()

a1.v=100
a2.v=200

a1.get_v()#无法获得实例的实例变量 因为传入的是类 没有传入self方法不知道 创建了几个变量 和赋予了实例变量


