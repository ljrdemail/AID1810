# 此示例示意缓冲区的作用和清除方法

#此处省略try语句

fw=open("myflush.txt",'w')
fw.write("这是一行文字！")
fw.flush()#强制清空缓冲区 写一次磁盘 如果没有这一句 需要等到你点了回车之后文件中才有 这是一行文字
s=input("请输入回车键继续：")

fw.close() #默认清空缓冲区 并写入磁盘 如果没有这一句 程序正常结束也会flueh
print("程序退出")