class Shape:
    def draw(self):
        print("shape.draw������")


class Point(Shape):
    def draw(self):
        print("point.draw������")


class Circle(Point):
    def draw(self):
        print("Circle.draw������")

def my_draw(s): #��̬���� MyDraw(Point s) ��д�����ʱ���ָ���� ���Ǿ�̬��̬ ��Ϊ python���������û�Ҳ û�취ָ�� ���ĸ��� ֻ�������е�ʱ��̬�������ĸ�
    s.draw()

s1=Circle()
s2=Point
my_draw(s2) #�����ĸ��� ȡ���ڴ������ʲô���� point.draw
my_draw(s1) #�����ĸ��� ȡ���ڴ������ʲô���� Cricket.draw
