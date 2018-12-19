def show_menue():
    print("+------------------------------------+")
    print("| 1) 添加学生信息                    |")
    print("| 2) 显示学生信息                    |")
    print("| 3) 删除学生信息                    |")
    print("| 4) 修改学生信息                    |")
    print("| 5) 按学生成绩高~低显示学生信息     |")
    print("| 6) 按学生成绩低~高显示学生信息     |")
    print("| 7) 按学生年龄高~低显示学生信息     |")
    print("| 8) 按学生年龄低~高显示学生信息     |")
    print("| q) 退出                            |")
    print("+------------------------------------+")


def input_student():
    l = list()

    while True:
        d = {}
        name = input("请输入学生姓名：")
        if (name == ""):
            break
        age = int(input("请输入学生年龄："))
        score = int(input("请输入学生分数："))
        if (score < 0 or score > 100):
            print("分数必须在0~100分之间")
            continue

        d["name"] = name
        d["age"] = age
        d["score"] = score

        l.append(d)
    return l


def output_student(l):
    if (len(l) == 0):
        print("列表为空，请先输入学生信息!")
        return
    lmn = list()
    lma = list()
    lms = list()

    for i in l:
        lmn.append(len(i["name"]))
        lma.append(i["age"])
        lms.append(i["score"])

    if (max(lmn) > 10):
        print("+", "-" * (max(lmn) + 2), "+", "----------", "+", "----------", "+", sep="")
        print("|", "姓名".center(max(lmn)), "|", "年龄".center(8), "|", "分数".center(8), "|", sep="")
        print("+", "-" * (max(lmn) + 2), "-----------", "-----------", "+", sep="")
        for k in l:
            print("|", k["name"].center(max(lmn) + 2), "|", str(k["age"]).center(10), "|", str(k["score"]).center(10),
                  "|",
                  sep="")
        print("+", "-" * (max(lmn) + 2), "+", "----------", "+", "----------", "+", sep="")
    else:
        print("+", "-" * 10, "-----------", "-----------", "+", sep="")
        print("|", "姓名".center(8), "|", "年龄".center(8), "|", "分数".center(8), "|", sep="")
        print("+", "-" * 10, "+", "----------", "+", "----------", "+", sep="")
        for k in l:
            print("|", k["name"].center(10), "|", str(k["age"]).center(10), "|", str(k["score"]).center(10), "|",
                  sep="")
        print("+", "-" * 10, "+", "----------", "+", "----------", "+", sep="")


def del_student(name, l):
    for i in l:
        if (i['name'] == name):
            l.pop(l.index(i))  # 不用remove怕崇明
            print("删除%s成功" % name)
            return  # 如果不加会删除别的同名的
    print("你所输入的人%s不存在 " % name)


def update_student(name, l):
    for i in l:
        if (i['name'] == name):
            newname = input("请输入新姓名：")
            newage = int(input("请输入新年龄："))
            newscore = int(input("请输入新分数："))

            i['age'] = newage
            i['name'] = newname
            i['score'] = newscore

    print("你所输入的人%s不存在 " % name)

    return


def dessortbyscore(l):
    l2 = list()
    l3 = list()
    lnew = list()
    for x in l:
        a = x["score"]
        l2.append(a)
    l2.sort(reverse=True)

    for j in l2:
        if (j not in l3):
            l3.append(j)

    for y in l3:
        for z in l:
            if (z["score"] == y):
                lnew.append(z)
    return lnew


def showdessortbyscore(oldlist):
    newlist = dessortbyscore(oldlist)
    output_student(newlist)


def sortbyscore(l):
    l2 = list()
    l3 = list()
    lnew = list()
    for x in l:
        a = x["score"]
        l2.append(a)
    l2.sort()

    for j in l2:
        if (j not in l3):
            l3.append(j)

    for y in l3:
        for z in l:
            if (z["score"] == y):
                lnew.append(z)
    return lnew


def showsortbyscore(oldlist):
    newlist = sortbyscore(oldlist)
    output_student(newlist)


def dessortbyage(l):
    l2 = list()
    l3 = list()
    lnew = list()
    for x in l:
        a = x["age"]
        l2.append(a)
    l2.sort(reverse=True)

    for j in l2:
        if (j not in l3):
            l3.append(j)

    for y in l3:
        for z in l:
            if (z["age"] == y):
                lnew.append(z)
    return lnew


def showdessortyage(oldlist):
    newlist = dessortbyage(oldlist)
    output_student(newlist)


def sortbyage(l):
    l2 = list()
    l3 = list()
    lnew = list()
    for x in l:
        a = x["age"]
        l2.append(a)
    l2.sort()

    for j in l2:
        if (j not in l3):
            l3.append(j)

    for y in l3:
        for z in l:
            if (z["age"] == y):
                lnew.append(z)
    return lnew


def showsortbysage(oldlist):
    newlist = sortbyage(oldlist)
    output_student(newlist)


def main():
    infos = []
    while True:
        show_menue()
        s = input("请选择: ")
        if s == '1':
            infos += input_student()
        elif s == '2':
            output_student(infos)
        elif s == '3':
            str = input("请输入要删除的姓名！")
            del_student(str, infos)
        elif s == '4':
            str = input("请输入要修改的姓名！")
            update_student(str, infos)
        elif s == '5':
            showdessortbyscore(infos)
        elif s == '6':
            showsortbyscore(infos)
        elif s == '7':
            showdessortyage(infos)
        elif s == '8':
            showsortbysage(infos)
        elif s == 'q':
            break
        else:
            print("你输入的菜单不存在，请重新输入！")


main()
