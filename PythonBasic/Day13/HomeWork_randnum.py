import random


def getPassword():
    l = list()

    for i in range(0, 6):
        c = random.randint(1, 3)

        if (c == 1):
            d = random.randint(65, 90)

            l.append(chr(d))

        if (c == 2):
            x = random.randint(97, 122)

            l.append(chr(x))

        if (c == 3):
            s = random.randint(48, 57)

            l.append(chr(s))

    return ''.join(l)  # s = '1 2 1'


print(getPassword())
