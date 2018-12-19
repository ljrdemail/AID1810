L=[1,2,3]

def f1(lst):
    L=lst #可以 也就是创建个局部变量 指向 传入的lst[4,5,6]

# def f2(lst):
#     L+=lst #b不可以 找不到局部变量 等同于L=L+lst 除非声明global 不可以直接操作全局变量
# 虽然如果传入的是列表类似于extend 但是也有可能别的比如元组  但是 即是是列表 也不行

def f3(lst):
    print(id(L))
    L.extend(lst) #可以 因为把列表拿来扩展 指向的地址不变 扩展的是列表
    print(id(L))

f1([4,5,6])
# f2([4,5,6])
f3([4,5,6])

print(L)