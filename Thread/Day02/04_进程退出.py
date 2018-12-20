# -*- coding:utf-8 -*-
import os
import sys

# print("进程%d 开始执行" % os.getpid())
# os._exit(0) #只能是0 1
# #exit 后面的语句不会执行
# print("进程%d结束" % os.getpid())

#sys模块中eixt()方法退出进程
print("进程%d 开始执行" % os.getpid())
sys.exit("我结束了！") #进程退出之后 输出"我结束了" #相当于return
print("sys后的语句也不会执行")
