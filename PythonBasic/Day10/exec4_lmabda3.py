def fx(f, x, y):
    print(f(x, y))

#h后面两个数作为 lambda函数的参数 因为 fx(f,x,y)
fx((lambda a, b: a + b), 100, 200)  # 300

fx((lambda c, d: c ** d), 3, 4)  # 81
