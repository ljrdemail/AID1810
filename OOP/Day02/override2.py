# -*- coding:utf-8 -*-
class Mylist(list):
    def append(self, x):
        print("我就是不干活")



L = Mylist("ABC")
L.append(100)
print(L)
