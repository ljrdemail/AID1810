# -*- coding:utf-8 -*-
class Bicycle():
    def run(self, km):
        print("人力骑行了：", km, "公里")


class EBicycle(Bicycle):
    def __init__(self, voulme):
        super().__init__()
        self.voulme = voulme

    def fill_charge(self, v):
        self.voulme += v
        print("电动自行车充电%d度" %v)
        # print(self.voulme)

    def run(self, km):
        d = abs(km // 10 - (self.voulme))

        if (km // 10 < self.voulme):
            print("电动骑行了", km, "公里", "还剩", self.voulme - km // 10, "度电")
            self.voulme -= km // 10
        if (km // 10 > self.voulme):
            print("电动骑行了", self.voulme * 10, "公里","还剩0度电")

            super().run((km // 10 - self.voulme) * 10)
            self.voulme = 0


b = EBicycle(5)  # 新买的电动车内有5度电
b.run(10)  # 电动骑行了10KM 还剩5度电
b.run(100)  # 电动骑行了40KM 还剩0度电 自行车骑行了60KM
b.fill_charge(10)  # 电动自行车充电10度
b.run(50)  # 电动自行车骑行了50 KM 还剩5度电
