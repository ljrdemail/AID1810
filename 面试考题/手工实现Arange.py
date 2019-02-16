# -*- coding:utf-8 -*-
class myArrange:
    def __init__(self, start, stop=None, step=None):
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1

        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return MyRangeIterator(self.start, self.stop, self.step)


class MyRangeIterator:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.l = list()
        self.index = 0
        if (self.step > 0):
            i = self.start

            while i < self.stop:
                self.l.append(i)
                i += self.step
        elif self.step < 0:  # 反向生成
            i = self.start

            while i > self.stop:
                self.l.append(i)
                i += self.step

    def __next__(self):

        if self.index >= len(self.l):
            raise StopIteration  # 不再提供数据
        r = self.l[self.index]
        self.index += 1
        return r


L = list(myArrange(5))
print(L)
print(sum(myArrange(1, 101)))  # 5050
#
for x in myArrange(1, 10, 3):
    print(x, end=" ")
