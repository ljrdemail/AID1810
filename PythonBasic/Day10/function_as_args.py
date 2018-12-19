def f1():
    print("f1被调用")


def f2():
    print("f2被调用")


def fx(fn):
    print(fn)
    fn()


fx(f1)
#fx(10000) #打印可以但是不能调用 所以报错
fx(f2)


#f1(0
#fn=f1
#fn() 等同于f1()