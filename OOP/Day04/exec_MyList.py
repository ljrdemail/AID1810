# -*- coding:utf-8 -*-
class MyList:

    def __init__(self, iterable=()):
        self.it = iterable
        self.data = [x for x in iterable]

    def __repr__(self):
        # return "MyList(%s)" % self.data
        return repr(self.data)



    def __add__(self, other):
        return MyList(self.data + other.data)

    def __mul__(self, other):
        return MyList(self.it * other)




myl = MyList([1, 2, 3])
print(myl)
myl2 = MyList([4, 5, 6])
print(myl + myl2)
print(myl2 + myl)

myl3 = myl * 3
print(myl3)
