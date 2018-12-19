def mymax(x, y):
    if (x > y):
        return x
    else:
        return y


print(mymax(100, 200))
print(mymax("abc", "ABCD"))
# print(mymax("ABC",123))#字符串和数值不能比较 所以报错
