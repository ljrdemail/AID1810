j = 1
while (j <= 10):
    num = 1
    while (num <= 20):
        print(num, end=" ")
        if num == 15:
            break
        num += 1
    #else: #如果放在else 下面会不打印print() 
    print()
    j += 1

print("程序结束")
