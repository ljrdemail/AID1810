list1 = [1001, 1002, 1005, 1008]
list2 = ['Tom', 'Jerry', 'Spike', 'Tyke']

# 错误的做法
# d={x:y for x in list2 for y in list1} 这样写 因为x =Tom 的时候 Y 轮训1001~1008 但是字典不存在重复的键值对 所以留下最后'tom':1008
# print (d)


d1={list2[i]:list1[i] for i in range(len(list1))}
print(d1)

d2 = {k: list1[list2.index(k)] for k in list2}
print(d2)

# d={}
#
# i=0
# for x in list2 :
#     d[x]=list1[i]
#     i+=1
#
# print(d)
