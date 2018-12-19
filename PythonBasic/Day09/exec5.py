def myprint(*args, sep2=" ", end2="\n"):
    # flag = False
    # for i in args:
    #     s = str(i)
    #     if flag:
    #         print(sep2, end='')
    #     print(s, end='')
    #     flag = True
    # print(end2, end='')
    print(*args, sep=sep2, end=end2)


myprint(1, 2, 3, 4)
myprint(1, 2, 3, 4, sep2="#")
myprint(1, 2, 3, 4, 5, end2=" ")
myprint(1, 2, 3, 4, 5, end2=" ", sep2="%")
