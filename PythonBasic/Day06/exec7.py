begin = int(input("请输入开始整数:"))
end = int(input("请输入结束整数:"))

L = [x for x in range(begin, end) if x % 2 == 0]
print(L)
