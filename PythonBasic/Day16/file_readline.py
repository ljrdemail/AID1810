# 此示例示意用文件流对象的读方法来获取filetest内的字符书库

try:
    fr = open("filetest.txt", encoding='utf-8')
    s = fr.readline()  # 需要注意的是最后的换行符也读进来了 所以多了一个空行
    str2 = s.strip("\n")  # 去掉多余的换行符
    print(str2)
    s2 = fr.readline().strip("\n")  # 当文件结束 返回空行 如果读完之后调用readline 和 read 都是空
    print(s2)

    fr.close()

except OSError:
    print("文件打开错误")
