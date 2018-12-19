# 此示例示意标准输出和标准错误输出的用法
import sys

# sys.stdout.write("你好")
# sys.stdout.write("ABC")
# sys.stdout.writelines(["abc","123"])
sys.stdout.close()  # 关闭之后就无法再往屏幕写了
# sys.stdout.write("关闭个屁")
# print("hello world") #关闭之后 print也个屁了 因为print 基于sts.stdout 因为默认打印到屏幕 file=sys.stdout

sys.stderr.write("我正当红")  # 输出到屏幕 但是 是红色字体
# stderr 和 stdout是两个流 即使 stdout关了 不影响  stderr 所以这句正常打印

# print(1,2,3,4,file=sys.stderr) #红字打印

f = open("mystdout.txt", "w")
print("我要打印到文件", file=f)
