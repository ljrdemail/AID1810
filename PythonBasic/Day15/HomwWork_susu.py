def find_susu(n):
    count = 0
    end = 2
    while True:
        flag = True

        for i in range(2, end):
            if end % i == 0:
                break
        else:
            count += 1
            yield end

        end += 1
        if (count == n):
            break


L = [x for x in find_susu(5)]
print(L)
