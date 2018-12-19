def make_exception():
    print("开始.....")
    error = ValueError("这是我故意制造的一个错误")  # 创建一个错误对象 如果不raise 不会报错 你只是创建 没有抛出
    raise error #投出这个错误 发的是对象 而不是 类型
    # int是类型 int("100") 是对象 所以叫构造函数
    # 这里ValueError 类似int  ValueError("这是我故意制造的一个错误") 类似int(100)

    print("结束......")


try:
    make_exception()
except ValueError as err:  # 通过err 拿到错误对象（注意是对象不是str） 并打印 err 所携带的信息
    print("我接收到你的报警，马上赶到！")
    print("报警信息:",err)
print("程序结束")
