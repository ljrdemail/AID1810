n = 1
sum = 0
while (n <= 100):
    if (n < 100):
        print(n, "+", end=" ")
    if (n == 100):
        print(n, "=", end=" ")
    sum += n
    n += 1

print(sum)
