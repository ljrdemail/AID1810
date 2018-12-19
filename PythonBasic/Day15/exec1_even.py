def get_even(start, stop):
    i = start
    while i < stop:
        if i % 2 == 0:
            yield i
        i += 1


for x in get_even(1, 10):
    print(x)

L = [x ** 2 for x in get_even(10, 20)]
print(L)

it = iter(get_even(3, 10))
print(next(it))
print(next(it))
print(next(it))
# print(next(it)) #stopIteration
