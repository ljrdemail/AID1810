def fun():
    print("启动生成器")
    for i in range(5):
        yield i
    print("结束生成器")


g = fun()

while True:
    try:
        print(next(g))
        print('*' * 20)
    except StopIteration:
        break;
        print("到头了")
