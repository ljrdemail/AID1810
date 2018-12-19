def myrange(*args):
    if (len(args) == 1):
        start = 0
        while start < args[0]:
            yield start
            start += 1
    if (len(args) == 2):
        start = args[0]
        while start < args[1]:
            yield start
            start += 1
    if (len(args) == 3 and args[2]>0):
        start = args[0]
        while start < args[1]:
            yield start
            start += args[2]
    if (len(args) == 3 and args[2]<0):
        start = args[0]
        while start > args[1]:
            yield start
            start += args[2]


# print([x for x in myrange(10)])
# print([x for x in myrange(1,5)])
# print([x for x in myrange(1,5,2)])
# print([x for x in myrange(5,1)])
# print([x for x in myrange(5,1,4)])
# print([x for x in myrange(5,1,-1)])
#print([x for x in myrange(1,10,3)])

L=[x**2 for x in myrange(1,10) if x%2==1]
# print (L)
print(sum(L))
