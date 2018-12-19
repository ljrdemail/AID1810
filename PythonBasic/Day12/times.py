def make_functions(args):
    count = 0  # 用来记录某个函数的调用次数

    def f1(name):
        print(args, name)
        nonlocal count
        count += 1

    def f2():
        print("调用f1(", args, ")次数为", count)
        return count

    return (f1, f2)


say_hello, getcount = make_functions("你好：")  #f1 给 say_hello f2 给getcount 在 f1 中修改count 在getcount显示 能这么干是因为 count 属于 make_functions 是嵌套函数的  外部嵌套函数的变量 用nonlocal修饰了所以可以动
print("getcount() 返回:", getcount())  # 0
say_hello("小张")
say_hello("小李")
print("getcount() 返回:", getcount())  # 0
