# -*- coding:utf-8 -*-
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.learnedtech = []
        self.earnedmoney = 0

    def teach(self, obj, tech):
        print(self.name, "教", obj.name, tech)
        obj.learnedtech.append(tech)

    def earn_money(self, money):
        print(self.name, "挣了", money)
        self.earnedmoney = money

    def jieqian(self, obj, money):
        if (self.earnedmoney < money):
            print("地主家也没余粮啊！")
        else:
            self.earnedmoney = (self.earnedmoney - money)
            obj.earnedmoney = money

    def show_info(self):
        print(self.age, "的", self.name, "有钱", self.earnedmoney, "他学会的技能是", self.learnedtech)


zhang = Human("张三", 35)
lisi = Human("李四", 10)

zhang.teach(lisi, "python")
lisi.teach(zhang, "王者荣耀")
zhang.earn_money(1000)
zhang.jieqian(lisi, 200)

zhang.show_info()
lisi.show_info()
