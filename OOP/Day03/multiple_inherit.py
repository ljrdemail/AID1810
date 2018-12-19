# -*- coding:utf-8 -*-
class Car:
    def run(self, speed):
        print("汽车正以", speed, "公里/小时的速度行驶")


class Plane:
    def fly(self, height):
        print("飞机以海拔", height, "米的高度飞行")


class PlaneCar(Car, Plane):
    # 同时继承自汽车和飞机（多继承）
    pass


pc = PlaneCar()
pc.run(300)
pc.fly(1000)
