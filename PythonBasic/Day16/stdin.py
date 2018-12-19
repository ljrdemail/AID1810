
#此示例示意 标准输入文件的用法
import sys

s=sys.stdin.readline()
print(s)
print("len(s)=",len(s)) #换行 \n算一个 输入+换行

sys.stdin.close()#如果关了下面就个屁
s2=input("请输入文字：") #内部会间接调用 sys.stdin.readline()

print("s2=",s2)
