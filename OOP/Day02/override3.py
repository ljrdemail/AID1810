# -*- coding:utf-8 -*-


class A:
    def work(self):
        print("A.work被调用")


class B(A):
    def work(self):
        print("B.work被调用") #覆盖了父类的同名方法


b1 = B()
#b1.work()
A.work(b1)#当覆盖发生时候 通过这种方式显示的调用父类被覆盖的方法

b=A() #绑定的是A类 找不着 也是找A的父类 不会是子类
b.work() #根据b绑定的类型来查找方法


