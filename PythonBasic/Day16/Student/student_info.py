def input_student():
    l = list()
    while True:

        d = {}
        name = input("请输入学生姓名：")
        if (name == ""):
            break
        try:
            age = int(input("请输入学生年龄："))
            score = int(input("请输入学生分数："))
        except ValueError:
            print("年龄或分数输入错误,请重新输入！")
            input()
            continue

        if (score < 0 or score > 100):
            print("分数必须在0~100分之间")
            continue
        d["name"] = name
        d["age"] = age
        d["score"] = score

        l.append(d)

    return l


def read_info(l):
    try:
        fr = open("si.txt")
        while True:
            s = fr.readline()
            if not s:
                fr.close()
                break
            s2 = s.strip("\n")
            str = s2.split(",")
            d = {}
            d["name"] = str[0]
            try:
                d["age"] = int(str[1])
                d["score"] = int(str[2])
            except ValueError:
                print("文件中分数和成绩必须为数字")
            l.append(d)
    except OSError:
        print("读取数据失败")



def write_list_tofile(l):
    try:
        fw = open("so.txt", "a")
        for d in l:
            name = d["name"]
            age = d["age"]
            score = d["score"]

            str2 = ",".join([name, str(age), str(score)])

            fw.write(str2 + "\n")
        fw.close()
        print("打印成功")
    except:
        print("打印失败")


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


def sor_by_score_asc(l):
    def get_score(d):
        return d["score"]

    l2 = sorted(l, key=get_score)
    output_student(l2)


def sor_by_score_desc(l):
    def get_score(d):
        return d["score"]

    l2 = sorted(l, key=get_score, reverse=True)
    output_student(l2)


def sor_by_age_asc(l):
    def get_age(d):
        return d["age"]

    l2 = sorted(l, key=get_age)
    output_student(l2)


def sor_by_age_desc(l):
    def get_age(d):
        return d["age"]

    l2 = sorted(l, key=get_age, reverse=True)
    output_student(l2)
