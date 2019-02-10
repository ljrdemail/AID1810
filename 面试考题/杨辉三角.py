def get_nextline(l):
    fl = [1]
    for i in range(len(l) - 1):
        x = l[i] + l[i + 1]
        fl.append(x)
    fl.append(1)
    #print(fl)
    return fl


def get_lines(num):
    L = []
    line = [1]
    while len(L) < num:
        L.append(line)
        line = get_nextline(line)

    return L


def change_str(l):

    strl = []
    for i in l:
        temp = [str(x) for x in i]
        s = ' '.join(temp)
        strl.append(s)
   # print(strl)
    return strl


def print_trangle(l):

    le = len(l[-1])

    for s in l:
        print(s.center(le))

L=get_lines(6)

L3=change_str(L)
L4=print_trangle(L3)

