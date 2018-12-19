def myrange(*args):
    l = list()

    if (len(args) == 0):
        print("TypeError: range expected 1 arguments, got 0")

    if (len(args) == 1):
        for x in range(0, args[0], 1):
            l.append(x)
    if (len(args) == 2):
        for x in range(args[0], args[1], 1):
            l.append(x)
    if (len(args) == 3):
        for x in range(args[0], args[1], args[2]):
            l.append(x)
    return l


L = myrange()
# L=range()
print(L)
