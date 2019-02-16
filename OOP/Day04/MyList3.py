# -*- coding:utf-8 -*-
class MyList:

    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        # return "MyList(%s)" % self.data
        print(id(self))
        return repr(self.data)

    def __mul__(self, other):
        print("mul被调用")
        L = MyList(self.data * other)

        return L

    def __imul__(self,other):
        print("imul被调用")
        print(id(self))
        self.data*=other
        return self
    def __del__(self):
        print(self,"被销毁了")

print("程序结束")

L1 = MyList([1, 2, 3])

L1 *= 2  # L1=L1*2 如果有imul 优先调用 没有拆解为L1*22 调用mul

print(L1)
