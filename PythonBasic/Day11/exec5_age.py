def age(n):
    if n == 1:
        print("第1位同学10岁")
        return 10;
    r = 2 + age(n - 1)
    print("第%d位同学%d岁" % (n, r))
    return r


print(age(5))
