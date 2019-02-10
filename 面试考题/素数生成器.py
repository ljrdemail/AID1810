#   2. 写一个生成器函数 myprimes(n), 此生成器函数用来生成
#     n个素数
#       如:
#         for x in myprimes(5):
#             print(x)  # 2 3 5 7 11


def isprime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def myprimes(n):
    x = 0
    count = 0  # 计数
    while count < n:
        if isprime(x):
            yield x
            count += 1  # 已经生成了一个
        x += 1  # 整数变大
    

for x in myprimes(5):
    print(x)  # 2 3 5 7 11
