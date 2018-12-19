def info(name,age=1,address="不详"):
     print(name,"今年",age,"岁，家庭住址：",address)

info("李嘉睿",25,"爱榕路48号雍景湾6B8G")
info("李嘉睿",25)#不给用默认参数
info("张飞")
#info()#name 没有默认参数 必须要有