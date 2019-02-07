def mymax(iterable, *args):
    # def mymax(*args):
    #     # print('args=', args)
    #     # 当元组长度为1时,传入的是一个列表
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

    if len(args) == 0:
        zd = iterable[0]
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
print(mymax(4, 6, 9, 3))
# print(mymax("ABC",'abc','123'))
# print(mymax(1,2,3,4,5,6,7,8,9))
