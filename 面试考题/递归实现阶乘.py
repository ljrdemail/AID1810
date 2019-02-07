def fattorial(n):
    print("n=",n)
    if n == 0:
        return 1

    r = n * fattorial(n - 1)
    return r


print(fattorial(5))
