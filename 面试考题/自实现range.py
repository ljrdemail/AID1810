#   1. 写一个生成器函数 myxrange(start, stop, step), 
#   来生成一系列整数,规则与range函数完全相同
#   (不允许调用range)
#     用自己写的myxrange结合生成器表达式求1~10的奇数的平方和
   
def myxrange(start, stop=None, step=None):
    if stop is None:
        stop = start
        start = 0
    if step is None:
        step = 1
    if step > 0:  # 正向生成
        i = start
        while i < stop:
            yield i
            i += step
    elif step < 0:  # 反向生成
        i = start
        while i > stop:
            yield i
            i += step

# for x in myxrange(10, 0, -3):
#     print(x)

s = sum( (x ** 2 for x in myxrange(1, 10) if x % 2 == 1) )
print(s)