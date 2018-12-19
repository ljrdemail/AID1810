# 此示例用于示意用二进制方式读取一个内部存有文字信息的文件内容

try:
    fr = open("filetest.txt", 'rb')  # 用二进制打开 r就不能省
    # b = fr.read()
    # s = b.decode("utf-8")  # 把字节串解码为文字 当然前提是你直到是个文件
    # print(b)  # 你在Windows运行 换行会打印\r\n
    # print(s)
    # print(len(b))

  # b2=fr.read(1)
    b3 = fr.readline()
    #b3 = fr.readline()
    print(b3)


    fr.close()

except OSError:
    print("文件打开失败")
