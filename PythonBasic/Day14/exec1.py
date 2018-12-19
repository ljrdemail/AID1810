def get_score(score):
    if int(score) < 0:
        print("成绩不能小于0")
        return -1
    elif int(score) > 100:
        print("成绩不能大于100")
        return -1
    else:
        return int(score)


try:
    score = input("请输入学生成绩：")
    s = get_score(score)
    if (s == -1):
        print("学生成绩不合法！")
    else:
        print("学生成绩为：", s)
except ValueError:
    print("成绩必须为正整数！")
