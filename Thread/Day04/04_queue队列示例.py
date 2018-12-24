from multiprocessing import Queue

# 创建消息队列

q = Queue(maxsize=3)

# # put() 值
# q.put("消息1")
# q.put("消息2")
# q.put("消息3")
# #q.put("消息4")#阻塞在这里了 因为 队列长度3
# time.sleep(0.1)

# q.empty（） 和q.get()
# while True:
#     if q.empty():#一般和get 搭配自用
#         print("队列中没值了！")
#         break
#     print(q.get())
#

i = 0
while True:
    if q.full():
        print("队列满了")
        break
    q.put("消息：%d" % i)
    i+=1
print("当前队列中有%d条消息" %i)
