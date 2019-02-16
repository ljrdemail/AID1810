# -*- coding:utf-8 -*-
class MyList:

    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        # return "MyList(%s)" % self.data
        return repr(self.data)

    def __mul__(self, other):
        L=MyList(self.data * other)
        print("mul中的ID为", id(L))
        return L

    def __imul__(self, other):
        L=MyList(self.data * other)
        print("imul中的ID为", id(L))
        return L

    def __del__(self):
        print(self,"被销毁了")




print("程序结束")



L1 = MyList([1, 2, 3])
print(id(L1)) #调用  return repr(self.data)的ID
L1 *= 2  # L1=L1*2 如果有imul 优先调用 没有拆解为L1*22 调用mul
print("外面的ID为：",id(L1)) # 调用  return MyList(self.data * other) 的ID 也就是向说 *2 之后产生新的列表 id 跟老列表不一样
print(L1)
