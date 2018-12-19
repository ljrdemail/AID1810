def get_newlist(l):
    for i in l:
        yield i ** 2 + 1


L = [2, 3, 5, 7]

for i in get_newlist(L):
    print(i)
print("----------------华丽丽的分割线-------------------------")
gen = (x ** 2 + 1 for x in L)

# for x in gen: #通过中间变量 gen 来生成 你再跑一次 就不能再次生成
for x in (x ** 2 + 1 for x in L):  # 建议每次重新生成
    print(x)
print("----------------华丽丽的分割线-------------------------")
L2 = [x ** 2 + 1 for x in L] #通过列表生成
print(L2)

print("----------------华丽丽的分割线-------------------------")
L3 = list(map(lambda x: x ** 2 + 1, L)) #通过Map生成
print(L3)
