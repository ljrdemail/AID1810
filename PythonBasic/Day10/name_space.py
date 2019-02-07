v = 100 #global


def f1():
    v = 200#enclosure ±‰¡ø
    print("f1.v=", v)

    def f2():
        v = 300 #local
        print("f2.v=", v)
    f2()

f1()

print("v=",v)