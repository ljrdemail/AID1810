def save_phone():
    fw = open("phone_book.txt", "a", encoding="utf-8")
    while True:
        name = input("请输入姓名：")
        if name == "":
            fw.close()
            break

        phone = input("请输入电话号码：")
        str = ",".join([name, phone])
        fw.write(str)
        fw.write("\n")


save_phone()
