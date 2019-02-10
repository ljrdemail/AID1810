try:
   fw=open("binaryfile.txt",'wb')
   #写入256个字节 0x00 ox01 .......0xff
   b=bytes(range(256))
   fw.write(b) #只能通过字节串写  列表 等别的方式要转换为字节串才能写进去
  # fw.writeline(b) #二进制不支持


   fw.close()

except OSError:
    print("文件打开失败")
