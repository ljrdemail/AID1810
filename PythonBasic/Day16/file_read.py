# 此示例示意用文件流对象的读方法来获取filetest内的字符书库

try:
    fr = open("filetest.txt",encoding='utf-8')
    s=fr.read(2) #从一个文件流中最多读取size个字符 读的是字节串并编码和解码
    print(s)
    s2 = fr.read(4) #回车换行算一个字符 逐个读 从上次读取到的地方继续读 不是从头读
    print(s2)
    print("读出长度",len(s))

except OSError:
    print("文件打开错误")
