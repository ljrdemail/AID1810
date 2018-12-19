# -*- coding:utf-8 -*-
class A:
    def __init__(self):
        self.__money = 0  # 加了双下划线 就是私有属性 此类以外的方法不能访问

    def show_info(self):
        print(self.__money)  # 方法内可以访问私有属性和调用私有方法
        self.__m() #类内可以调用私有方法

    def __m(self):  # 私有方法
        print("A类的__m方法被调用")


a = A()
# print(a.__money)#出错不能访问私有属性
# a.money-=100
# print(a.money)

a.show_info()
# a.__m()#错误 私有方法不能再类外调用

print(a._A__money) #间接访问 类名前面_
