# 此示例示意用F.seel方法来修改文件读写指针的位置
try:
    fr = open("my20bytes.txt", "rb")
    b1 = fr.read(3)
    print("读完3个字节后指针的位置在:", fr.tell())
    # 相对文件头偏移
    #fr.seek(5,0)
    # 相对于当前位置向后移动两个字节
    fr.seek(2,1) #走到了C 偏移两个到D
    # 相对于文件尾向前移动
    #fr.seek(-15, 2)
    b2 = fr.read(5)  # 要读取从第5个到第9个字节 b2=abcde
    print(b2)

    fr.close()
except OSError:
    print("文件打开失败")
