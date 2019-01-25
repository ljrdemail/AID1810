a = 1
b = 2
c = 3


def fn(c, d):
    e = 200
  #  print(locals())
   # print(globals())
    print(a, b, c, d, e)
    print(c)  # 优先输出局部变量
    print("全局的C",globals()['c'])


fn(100, 200)

#print("globals返回",globals())
