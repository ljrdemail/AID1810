# # 定义一些函数能实现求x的ncifang
#
# def pow2(x):
#     return x ** 2
#
#
# def pow3(x):
#     return x ** 3
#
# #...
# def pow100(x):
#     return x ** 100
#
# print("5的立方是:",pow3(5))
# print("6的平方是:",pow2(6))
# print("2的100次方是:",pow100(2))

def make_power(y):
    def fn(x):
        return x ** y

    return fn


pow3 = make_power(3)  # x**3 指向创建的fn 调用的时候传入x即可 由于返回的fn 里面用了外层的 y所以 返回fn之后 y 没有被清除 y 和生成的函数一直不会被清除 很占用空间
#所以不要多搞
pow2 = make_power(2)  # x**2
pow100 = make_power(100)  # x**100

print("5的立方是:", pow3(5))
print("6的平方是:", pow2(6))
print("2的100次方是:", pow100(2))
