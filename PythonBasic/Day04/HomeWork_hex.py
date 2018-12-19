begin=int(input("请输入起始值："))
end=int(input("请输入结束值："))

print("十进制编码","十六进制编码","文字",sep="\t")
while(begin<=end):
   print(str(begin).center(10),str(hex(begin)).center(12),str(chr(begin)).center(4),sep="\t")
   begin+=1

