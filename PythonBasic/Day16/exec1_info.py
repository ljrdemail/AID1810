try:
    f = open("info.txt", encoding='utf-8')
    for s in f:
        name = s.split(" ")[0]
        age = s.split(" ")[1]
        score = s.split(" ")[2].strip("\n") #去掉换行
        print(name, "今年", age, "岁", "成绩是", score)
    f.close()
except OSError:
    print("文件操作失败")
