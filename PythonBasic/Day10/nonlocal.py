v = 100


def f1():
    v = 200
    print("f1.v=", v)

    def f2():
        nonlocal v #声明 V不是局部变量 也不是全局变量 就是200 被修改为300
        v = 300
        print("f2.v=", v)

    f2()
    print("调用结束后f1.v=", v)


f1()
