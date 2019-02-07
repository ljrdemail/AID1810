v = 100


def f1():
    v = 200

    def f2():
        v = 300

        def f3(v):
            nonlocal v# nonlocal不能修饰形参
            v = 400 #只修改了300 位400 只网上修改一层


        f3(111) #你告诉我 到底是 111 还是400
        print("f2.v=", v)

    f2()
    print("调用结束后f1.v=", v)


f1()
