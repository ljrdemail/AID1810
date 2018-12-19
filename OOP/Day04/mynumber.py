# -*- coding:utf-8 -*-

class MyNumber:
    # 此类用于定义一个自定义的数字类 用于示意运算符重载
    def __init__(self, value):
        self.data = value

    def __repr__(self):
        # return "MyNumber(%d)" % self.data
        return repr(self.data)

    def __add__(self, other):
        print("MyNumber add方法被调用")
        sum = self.data + other.data
        return MyNumber(sum)

    def __sub__(self, other):
        print("MyNumber sub方法被调用")
        sub = self.data - other.data
        return MyNumber(sub)


n1 = MyNumber(100)
n2 = MyNumber(200)
# n3 = n1.__add__(n2)
# n3 = n1 + n2 #等同于 n1.__add__(n2) 是解释执行器帮你 简化了
n4 = n1 - n2
print(n4)
#
# print(n3)
# i1= int(100)
# i2=int(100)
# # i3=i1+i2 #能加是因为等同于 i3 = i1.__add__(i2)
# print(i3)
