def power2(x):
    print("+------------------------+")

    return x ** 2


for x in map(power2, range(1, 10)):  # 注意power2不要加括号 否则就变成调用
    print(x)

    # 把迭代对象每一个元素放到power2 ；里面执行并返回结果
