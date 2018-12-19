def printyh():
    row = 6
    for i in range(row):
        num = 1

        for j in range(i + 1):
            print(num,end=" ")
            num = int(num * (i - j) / (j + 1))
        print()


printyh()
