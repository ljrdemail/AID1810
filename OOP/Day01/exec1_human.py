# -*- coding:utf-8 -*-
class Human:
    def set_info(self, name, age, address="不详"):
        self.name = name
        self.age = age
        self.address = address

    def show_info(self):
        print(self.name, "今年", self.age, "岁", "家住：", self.address)


s1 = Human()
s1.set_info("李嘉睿", 27, "蛇口雍景湾")
s1.show_info()

s2 = Human()
s2.set_info("潘仁晓", 18)
s2.show_info()

s3 = Human()
s3.set_info(age=67,name="李幼兰",address="湾厦花园")
s3.show_info()
