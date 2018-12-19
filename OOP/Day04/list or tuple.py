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

    def __iadd__(self, other):
        self.data.extend(other.data)
        return self

    def __iter__(self):
        return MyListIterator(self.data)

    def __next__(self):
        return next(self.__iter__())


class MyListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        try:
            # print ("next 被调用")
            # return "hello"
            r = self.data[self.index]
            self.index += 1
        except IndexError:
            raise StopIteration

        return r


L = MyList([1, 2, 3])


def f1(lst):
    lst += MyList([4, 5, 6])


f1(L)
print(L)
