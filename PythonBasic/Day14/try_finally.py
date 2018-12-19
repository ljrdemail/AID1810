# 此示例以控制天然气为例子 执行必须要关闭天然气的do顾总

def fry_egg():
    print("打开天然气，点燃....")
    try:
        count = int(input("请输入鸡蛋个数："))
        print("完成煎鸡蛋，共煎好%d个鸡蛋" % count)
    finally:
        print("关闭天然气")  # 不管报不报错 都跑这一句 确保关闭天然气


try:
    fry_egg()
except ValueError:
    print("煎鸡蛋过程中发生错误，现已恢复正常")
print("程序结束")
