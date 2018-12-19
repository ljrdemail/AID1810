
def mysum(n):
    # sum = 0
    # num = int(n)
    # for i in range(1, num + 1):
    #     sum += i
    # return sum
    return sum(range(1,n+1))
    # return sum(list(range(1,n+1)))

def myfac(n):
    fac = 1
    num = int(n)
    for i in range(1, num + 1):
        fac *= i
    return fac
print(myfac(10))

def mypow(n):
    # sum = 0
    # num = int(n)
    # for i in range(1, num + 1):
    #     sum += i ** i
    # return sum
    return sum(map(lambda  x:x**x,range(1,n+1)))
