def isprime(p):
    if(p<2):
        return False
    for i in range(2, p):
        if (p % i == 0):
            return False;
    return True


def prime_m2n(m, n):
    # l = list()
    # for i in range(x, y):
    #     flag = True
    #     for j in range(2, i):
    #         if (i % j == 0):
    #             flag = False
    #             break
    #     if (flag):
    #         l.append(i)
    #
    # return l

   return [x for x in range (m,n) if isprime(x)]

# print(prime_m2n(10,20))

def prime(n):
    # l = list()
    # for i in range(2, n):
    #     flag = True
    #     for j in range(2, i):
    #         if (i % j == 0):
    #             flag = False
    #             break
    #
    #     if (flag):
    #         l.append(i)
    # return l
    return prime_m2n(0,n)

# print(prime(100))

print(sum(prime(100)))

print(sum(prime_m2n(100,200)))
