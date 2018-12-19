# 此示例示意文件流对象是可迭代对象

try:
    fr = open("filetest.txt", encoding='utf-8')
    # while True:
    #     s = fr.readline()
    #     if s == '':
    #         break;
    #     print(s)


    fr.close()
except OSError:
    print("打开写文件失败！")
