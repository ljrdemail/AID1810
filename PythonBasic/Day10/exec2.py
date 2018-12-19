count=0

def hello(name):
    global count;
    print("你好, ",name)
    count+=1

hello("小张")
hello("小李")

print("hello 这个函数被调用了%d次" %count)