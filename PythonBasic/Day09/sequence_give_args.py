def myfunl(a, b, c):
    print('a=', a)
    print('b=', b)
    print('c=', c)


s1=[11,22,33]
s2=(44,55,66)
s3="ABC"

#myfunl(s1[0],s1[1],s1[2])
myfunl(*s1) #等同于 yfunl(s1[0],s1[1],s1[2])
#* 会把 s1  拆开 成三个元素
myfunl(*s2)
myfunl(*s3)