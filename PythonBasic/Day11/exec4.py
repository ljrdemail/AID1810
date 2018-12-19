def strrev(s):
   # print("s=",s)
    l=list(s)
    #print("l=",l)
    #print("lrev=",l[::-1])
    return l[::-1]


names = ['Tom', 'Jerry', 'Spike', 'Tyke']
L2 = sorted(names, key=strrev) #key只负责加工（反向输出） 不负责排序 由sort排序

print(L2)
