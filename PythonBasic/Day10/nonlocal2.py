v = 100


def f1():
    v = 200

    def f2():
        v = 300

        def f3():
            nonlocal v
            v = 400 #只修改了300 位400 只往上修改一层

        f3()
        print("f2.v=", v)

    f2()
    print("调用结束后f1.v=", v)


f1()
