def mymax(iterable, *args):
#     if len(args) == 1:
#         iterable = args[0]
#         zd = iterable[0]
#         for x in iterable:
#             if x > zd:
#                 zd = x
#         return zd
#     else:
#         zd = args[0]
#         for x in args:
#             if x > zd:
#                 zd = x
#         return zd

    # return max(args)
    if len(args) == 0:
        zd = iterable[0] #需要注意的时候如果只有一个整数的时候 这句话会报错 提示int 不是可迭代的对象
        for x in iterable:
            if x > zd:
                zd = x
        return zd
    # 当有两个或两个以上实参传入时
    zd = iterable
    for x in args:
        if x > zd:
            zd = x
    return zd

print(mymax([1, 2, 3, 4, 5]))
print(mymax(4,6,9,3))
# print(mymax("ABC",'abc','123'))
# print(mymax(1,2,3,4,5,6,7,8,9))
