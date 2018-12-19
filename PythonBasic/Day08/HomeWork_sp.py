def mysum(num1, num2, num3):
    return num1 + num2 + num3


def mypow(num):
    return num ** 3


print(mysum(mypow(1),mypow(2),mypow(3)))
print(mypow(mysum(1,2,3)))