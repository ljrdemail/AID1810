# -*- coding:utf-8 -*-
class MyList:

    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        # return "MyList(%s)" % self.data
        return repr(self.data)

    def __contains__(self, item):
        print("contains被调用 e=",item)
        return item in self.data


L1 = MyList([1, -2, 3, -4, 5])
print(3 in L1)
print(4 in L1)
print(5 not in L1)
print(6 not in L1)
