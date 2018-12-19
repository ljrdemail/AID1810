def change_for(L):
    it = iter(L)
    while True:
        try:
            print(next(it))
        except StopIteration as err:
            print("集合遍历结束")
            break


l = list()
for x in {'唐僧', '悟空', '八戒', '沙僧'}:
    l.append(x)

# print(l)

change_for(l)
