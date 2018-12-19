def get_age(age):
    if not 1 <= age <= 140:
        raise ValueError("年龄必须在1~140之间")

    return age


try:
    age = int(input("请输入年龄，年龄必须在1~140之间："))
    age = get_age(age)
    print("你的年龄是:%d" % age)
except ValueError as err:
    print("获取年龄时出错，错误原因是%s" % err)
