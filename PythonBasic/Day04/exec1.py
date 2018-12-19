str1 = input("请输入第一行：")
str2 = input("请输入第二行：")
str3 = input("请输入第三行：")

# print("%20s" %str1)
# print("%20s" %str2)
# print("%20s" %str3)

# max = int(len(str1));
# if (int(len(str2)) > max):
#     max = int(len(str2))
#
# if (int(len(str3)) > max):
#     max = int(len(str3))

# 或者
zuida = max(len(str1), len(str2), len(str3))

# print((" " * (zuida - len(str1))) + str1)
# print((" " * (zuida - len(str2))) + str2)
# print((" " * (zuida - len(str3))) + str3)

fmt="%"+str(zuida)+"s"
print(fmt %str1)
print(fmt %str2)
print(fmt %str3)
