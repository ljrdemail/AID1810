def say_hello():
    print("Hello aaa")
    print("hello bbb")
    #return  #不给表达式 就是Nome
    return  [1,2,3]
    print("hello ccc") #return后的语句不再执行
    # return 语句 作用 1 结束函数 2 返回调用的值给调用方


v = say_hello()
print('v=', v)  # 没返回返回None 类似Java中的void

v2 = say_hello()
print(id(v))
print(id(v2))