num=int(input("请输入终止值:"))



def print_even(num):
    l=list()
    for i in range(1,num+1):
        if(i%2==0):
            l.append(i)

    print(l)

print_even(num)