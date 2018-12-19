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

