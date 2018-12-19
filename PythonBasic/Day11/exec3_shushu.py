def isprime(x):
    if (x < 2):
        return False
    for i in range(2, x):
        if (x % i == 0):
            return False;
    return True


pirme = list()

for x in filter(isprime, range(1, 101)):
    pirme.append(x)

print(pirme)
