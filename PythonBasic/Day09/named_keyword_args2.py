def fun1(a,b,*args,c=111,d=222):
    print(a,b,args,c,d)

fun1(1,2,3,4,d="6",c="5") #java中可变参数必须放在最后 但是python可以放中间 后面的通过指定变量名方式规避不确定性
fun1(1,2,3,4)
fun1(1,2,3,4,c=10) #如果有默认值 就可以不传或少传
