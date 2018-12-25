from threading import Event

# 创建一个事件对象
e = Event()  # 默认为未设置

# 将e改为已设置,打印一下e状态
e.set()
print(e.is_set())

# 清除e的设置（未设置）并打印状态
# e.clear()
# print(e.is_set())

# 使用wait(),超时时间为2秒
e.wait()
#e.wait(2)
#如果没有设置超时时间 由于 e上述代码最后是未设置 会阻塞
#如果注释掉s.clear() wait()不阻塞 立刻打印

print("*****************")
