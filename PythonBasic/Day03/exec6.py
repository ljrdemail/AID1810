str = input("请输入整数值： ")

if (0 <= int(str) <= 65535):
    print("字符为", chr(int(str)))
else:
    print("请输入0~65535之间的数")

