# -*- coding:utf-8 -*-
class MySet:
    def __init__(self, itertable=()):
        self.data = [x for x in itertable]

    def __and__(self, other):
        l = set()
        for x in self.data:
            for j in other.data:
                if (x == j):
                    l.add(x)
        return l

    def __or__(self, other):
        s = set()
        l = self.data + other.data
        for i in l:
            s.add(i)
        return s

    def __sub__(self, other):
        s = set()
        for i in self.data:
            if (i not in other.data):
                s.add(i)
        return s

    def __xor__(self, other):
        s1 = set()
        s2 = set()
        for i in self.data:
            s1.add(i)
        for j in other.data:
            s2.add(j)
        return s1 ^ s2

    def __contains__(self, item):
        l = list()
        for i in item.data:
            for j in self.data:
                if (i == j):
                    l.append(i)

        return l == item.data

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __repr__(self):
        return repr(self.data)


s1 = MySet([1, 2, 3, 4])

s2 = MySet([3, 4, 5, 6])

s99 = MySet([3, 4, 5])

s3 = s1 & s2
print(s3)

s4 = s1 | s2
print(s4)

s5 = s1 - s2
print(s5)

s6 = s1 ^ s2
print(s6)

print(s1 == s2)

print(s1 != s2)

print(s2 in s99)

print(s99 not in s2)
