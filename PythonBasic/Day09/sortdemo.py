L = [5, -2, -4, 0, 3, 1]
L2 = sorted(L)
print(L2)

L3 = sorted(L, reverse=True)
print(L3)

L4 = sorted(L, key=abs)
print(L4)

L5 = sorted(L, key=abs, reverse=True)
print(L5)


def myabs(x):
    print("x=",x)
    if x < 0:
        return -x
    return x


L6 = sorted(L, key=myabs)
print(L6)
