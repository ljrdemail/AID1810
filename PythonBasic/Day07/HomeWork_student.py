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

lmn = list()
lma = list()
lms = list()

for i in l:
    lmn.append(len(i["name"]))
    lma.append(i["age"])
    lms.append(i["score"])

if (max(lmn) > 10):
    print("+", "-" * (max(lmn)+2), "+", "----------", "+", "----------", "+", sep="")
    print("|", "姓名".center(max(lmn)), "|", "年龄".center(8), "|", "分数".center(8), "|", sep="")
    print("+", "-" * (max(lmn) + 2), "-----------", "-----------", "+", sep="")
    for k in l:
        print("|", k["name"].center(max(lmn)+2), "|", str(k["age"]).center(10), "|", str(k["score"]).center(10), "|",
              sep="")
    print("+", "-" * (max(lmn) + 2), "+", "----------", "+", "----------", "+", sep="")
else:
    print("+", "-" * 10, "-----------",  "-----------", "+", sep="")
    print("|", "姓名".center(8), "|", "年龄".center(8), "|", "分数".center(8), "|", sep="")
    print("+", "-" * 10, "+", "----------", "+", "----------", "+", sep="")
    for k in l:
        print("|", k["name"].center(10), "|", str(k["age"]).center(10), "|", str(k["score"]).center(10), "|", sep="")
    print("+", "-" * 10, "+", "----------", "+", "----------", "+", sep="")
