def mymax2(*args):
    max = 0
    print('args=', args)
    if (len(args) == 1):
        iterable = args[0]
    else:
        iterable = args

    for x in iterable:
        if (x > max):
            max = x

    return max


print(mymax2([6, 8, 3, 5]))
print(mymax2(100, 200))
print(mymax2(1, 3, 9, 5, 7))
