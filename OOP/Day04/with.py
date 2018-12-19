# -*- coding:utf-8 -*-
# 此示例示意用with语句和try-finally 来保证文件的正确关闭


fr = open("day19.txt")
try:
    s = fr.read()
    print("字符个数：", len(s))
finally:
    fr.close()
