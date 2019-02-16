# -*- coding:utf-8 -*-
# 此示例示意用with语句和try-finally 来保证文件的正确关闭

try:
    with open("day19.txt") as fr:  # 读出文件流赋值给fr open 实现了 __enter__ __exit__ __del__

     s = fr.read()
     100/0
     print("字符个数：", len(s))  # 即使出错 在离开with语句之后自动关闭语句  with 也叫做环境管理器 会自动关文件 只能用来关闭文件不能处理异常
     # 避免了自己用 try -finally 忘了关文件
        #如果你要捕获异常 在外面套一层try -except
except ZeroDivisionError:
    print("被0除")
# fr.read() #文件流已经被with语句关闭不能读了
print("程序结束")
