def make_exception():
    print("开始.....")
    # 触发ValueError异常 给调用者
    raise ValueError  # ValueError 是错误类型
    # raise ZeroDivisionError
    # raise ImportError
    #  def int(s):
    #   if not s.isdigit():
    #   raise ValueError #导入错误
    print("结束......")#raise后面的不会执行


try:
    make_exception()
except ValueError:  # 必须要错误类型和raise一致 才会处理
    print("我接收到你的报警，马上赶到！")
print("程序结束")
