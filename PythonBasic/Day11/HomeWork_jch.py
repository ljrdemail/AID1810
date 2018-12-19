def myfac(n):
    fac = 1
    num = int(n)
    for i in range(1, num + 1):
        fac *= i
    return fac


def facsum():
    sum = 0
    for i in range(1, 21):
        sum += myfac(i)
    return sum


print(facsum())

print("和：", sum(map(myfac, range(1, 21))))
