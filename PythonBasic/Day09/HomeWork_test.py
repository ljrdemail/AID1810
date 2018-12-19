def f1():
    print("f1")


def f2():
    print("f2")


f3 = f1
f3()
f1, f2 = f2, f1
f1()  # ??? f2
f2()  # 打印什么？为什么？ f1
