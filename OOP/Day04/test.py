# -*- coding:utf-8 -*-
# L = [1, 2, 3]
#
#
# def f1(lst):
#     lst += [4, 5, 6]
#
#
# f1(L)
# print(L)  # [1,2,3,4,5,6]


L = (1, 2, 3)


def f1(lst):
    lst += (4, 5, 6) #指向了合并之后的地址
    print(lst)


f1(L)
print(L)
