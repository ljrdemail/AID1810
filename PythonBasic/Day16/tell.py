try:
    fr=open("my20bytes.txt","rb")
    s=fr.read(3)
    print(s)
    s = fr.read(2)
    print(s)
    print(fr.tell()) #打印当前光标位置 因为你读多了 你也不记得在哪了 #最大也就是文件的大小
except OSError:
    print("文件打开失败")