# 此示例示意读取当前文件夹下myfile.txt这个记录文字信息的文件
# 1 打开文件

try:
    #myfile = open("filetest.txt")  # 打开文件-相对路径
    #yfile = open(r"D:\Python\PythonBasic\Day16\filetest.txt")  # 绝对路径
   # myfile = open(r"..\Day16\filetest.txt") #相对路径
    myfile = open(r"..\Day16\不存在.txt")  # 相对路径
    print("文件打开成功！")

    # 读写文件

    # 关闭文件
    myfile.close()
    print("文件关闭成功！")



except FileNotFoundError:  # 无法进行输入输出:
    print("文件不存在哦")
except OSError:  # 无法进行输入输出:
    print("文件打开失败")