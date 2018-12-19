class Shape:
    def draw(self):
        print("shape.draw被调用")


class Point(Shape):
    def draw(self):
        print("point.draw被调用")


class Circle(Point):
    def draw(self):
        print("Circle.draw被调用")

def my_draw(s): #静态的是 MyDraw(Point s) 在写代码的时候就指定了 就是静态多态 因为 python是弱类型用户也 没办法指定 是哪个类 只能在运行的时候动态决定是哪个
    s.draw()

s1=Circle()
s2=Point
my_draw(s2) #调用哪个？ 取决于传入的是什么对象 point.draw
my_draw(s1) #调用哪个？ 取决于传入的是什么对象 Cricket.draw
