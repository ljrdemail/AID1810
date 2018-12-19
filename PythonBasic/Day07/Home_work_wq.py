lw = list()

x = 1
while True:
    ly = list()
    for i in range(1, x):

        if (x % i == 0):
            ly.append(i)
            
    if (sum(ly) == x):
        print(x)

    x += 1

# lw = list()
# ly = list()
#
# x = 1
# while True:
#     for i in range(1, x+1):
#        # print("x=",x)
#         if (x % i == 0):
#             ly.append(i)
#             print(ly)
#         if sum(ly) == x:
#             lw.append(x)
#             ly.clear()
#
#         x+=1
# #print(lw)
