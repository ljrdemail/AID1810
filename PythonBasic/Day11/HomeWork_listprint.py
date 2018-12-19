L = [[3, 5, 8], 10, [[13, 14], 15, 18], 20]

L2 = []


def listprint(l):
    for x in l:
        if (type(x) is list):
            listprint(x)
        else:
            L2.append(x)
            print(str(x), end="\t")


listprint(L)
print()

print("和为:%d" % sum(L2))
