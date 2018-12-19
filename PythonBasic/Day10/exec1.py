def myadd(x, y):
    return x + y


def myminus(x, y):
    return x - y


def myplus(x, y):
    return x * y


def mydivide(x, y):
    return x / y


def other(x, y):
    print("不支持的操作符号！！")


def getfunc(L):
    if (L == "加" or L == "+"):
        return myadd
    elif (L == "减" or L == "-"):
        return myminus
    elif (L == "乘" or L == "*"):
        return myplus
    elif (L == "除" or L == "/"):
        return mydivide
    else:
        return other


def main():
    while True:
        str = input("请输入计算公式：以空格分隔！")
        a = str.split()[0]
        b = str.split()[2]
        op = str.split()[1]
        fn = getfunc(op)
        print("计算结果是:", fn(int(a), int(b)))


main()
