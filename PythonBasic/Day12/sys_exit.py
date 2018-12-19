def f1():
    print('aaaaaaaa')
    # 能否在此处不返回到调用的方就退出程序呢?
    import sys #创建 一个局部变量只在函数内部用 import  就是把sys已有的方法放进环境中 你可以放在任意地方
    #sys.exit() #不返回调用程序直接跳出程序
    return # 返回调用的程序
    print('bbbbbbb') #后面不执行了

f1()
print("程序结束")