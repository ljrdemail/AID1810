def call_fun(fn):
    L = [1, 3, 9, 7, 5]
    return fn(L)


print(call_fun(max))
print(call_fun(min))
print(call_fun(sum))
