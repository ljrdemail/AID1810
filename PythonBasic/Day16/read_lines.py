# 此示例示意用文件流对象的读方法来获取filetest内的字符书库

try:
    fr = open("filetest.txt", encoding='utf-8')
    s=fr.readlines()
    print(s)


    fr.close()

except OSError:
    print("文件打开错误")
