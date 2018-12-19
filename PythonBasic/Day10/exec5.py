local_dict = {}
while True:
    str = input("请输入程序：>>>")
    if (str == 'quit()'):
        break
    exec(str, None, local_dict)

print(local_dict)
