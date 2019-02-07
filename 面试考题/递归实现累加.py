def mysum(n):
    # print("开始加上：",n)
    if n == 0:
        return 0
    r=n + mysum(n - 1)
    # print("已经加上：", n)
    return r


print(mysum(1000))
