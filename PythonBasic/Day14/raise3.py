def f1():
    print("f1开始")
    # 此处可能触发异常
    raise ValueError("f1里面出现值错误")
    print("f1结束")


def f2():
    print("f2开始")
    try:
        f1()
    except ValueError as err:
        print("f1里面值错误已经解决")
        raise err #转发给上级调用方 等同于raise 函数
   # raise err 必须放在except下面 因为放外面err 就不存在了
    print("f2结束")


try:
    f2()
except ValueError as err2:
    print("f2内发生错误，错误对象是", err2)
