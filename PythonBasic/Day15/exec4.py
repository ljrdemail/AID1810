L = [2, 3, 5, 7]
A = [x * 10 for x in L]
it = iter(A)
print(next(it))  # ?? 20
L[1] = 333
print(next(it))

L = [2, 3, 5, 7]
A = (x * 10
     for x in L)
it = iter(A)
print(next(it))  # ?? 20
L[1] = 333
print(next(it))  # ??30
#这个例子想说明 列表推导式产生的新列表立即产生即使后面修改了原始列表已经生成的不受影响
#生成器由于是随用随生成 所以改了列表会影响

