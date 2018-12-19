# -*- coding:utf-8 -*-
class MyList:

    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __abs__(self): #返回类型不受限制
        l = list()
        for i in self.data:
            l.append(abs(i))
        l2=MyList(l)
        return l2

    def __repr__(self):
        return "MyList(%s)" % self.data


myl = MyList([1, -2, 3, -4])  # 从列表转为字符串 %s
print(myl)
print(abs(myl))  # object 没有len 所以要自己写 否则出错
