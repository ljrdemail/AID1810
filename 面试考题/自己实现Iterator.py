# -*- coding:utf-8 -*-
class MyList:

    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        return "MyList(%s)" % self.data

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


# for x in MyList("123"):
#     print(x,end="")


# 以上语句等同于
myl = MyList("123")
it = iter(myl)
while True:
    try:
        x = next(it)
        print(x, end=" ")
    except StopIteration:
        break
