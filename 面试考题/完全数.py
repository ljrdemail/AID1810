# -*- coding:utf-8 -*-
lw = list()

# 完全数:
# 	    1 + 2 + 3 = 6 (6为完全数)
# 	    1,2,3都为6的因数(能被一个数x整数的数为y,则y为x的因数)
# 	    1 x 6 = 6
# 	    2 x 3 = 6
# 	    完全数是指除自身以外,所有的因数相加之和等于自身的数


x = 1
while True:
    ly = list()
    for i in range(1, x):

        if (x % i == 0):
            ly.append(i)

    if (sum(ly) == x):
        print(x)

    x += 1

# lw = list()
# ly = list()
#
# x = 1
# while True:
#     for i in range(1, x+1):
#        # print("x=",x)
#         if (x % i == 0):
#             ly.append(i)
#             print(ly)
#         if sum(ly) == x:
#             lw.append(x)
#             ly.clear()
#
#         x+=1
# #print(lw)
