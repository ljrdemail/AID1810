def musum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(musum())
print(musum(1,2,3,4))
