# 此示例用于解释装饰器的基本作用和原理
def mydeco(fn):  # 手机壳函数
    #print(id(fn))
    def fx():
        print("++++++++++++")
        fn()
        print("------------")
    #print(id(fx))
    return fx  # 加工之后的函数



#@mydeco  # 等同于 mfun=mydeco(myfun)
def myfun():
    '''此函数是被装饰函数'''

    print("myfunc被调用")


# 以下语句的实质是调用mydeco 绑定mydeco 返回装饰后的fx函数
#myfun()

mfunw=mydeco(myfun) # 此条语句可以改写为@mydeco 详见mydeco2.py
mfunw()

#给装饰函数传入被装饰函数的内存空间  装饰函数装饰之后 给调用方返回装饰后函数的内存地址
