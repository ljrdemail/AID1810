def mypow(x, y):
    return x ** y


l = list()
for x in map(mypow, range(1, 10), [2] * 9):
    l.append(x)

print(sum(l))

m = list()
for x in map(mypow, range(1, 10), [3] * 9):
    m.append(x)
print(sum(m))

n = list()
for x in map(mypow, range(1, 10), range(9, 0, -1)):  # 注意 按照数少的参数决定跑几次 即是前面的 有9个 因为后面只有4个 没有配对的 也停止
    n.append(x)

print(sum(n))
