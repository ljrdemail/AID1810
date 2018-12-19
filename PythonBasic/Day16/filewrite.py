try:
    fw = open("filewritetest.txt", mode="w")
    print("打开文件成功！")

    fw.write("你好！")
    fw.write("\n")

    fw.write("ABC")
    fw.write("\n")
    fw.writelines(["这是第一行","这是第二行"]) #不会自动给你换行 需要自己加
    fw.write("\n")
    fw.writelines(["换行", "换行"])
    print("写入文件成功！")

    fw.close()
    print("关闭文件成功!")

except OSError:
    print("打开写文件失败！")
