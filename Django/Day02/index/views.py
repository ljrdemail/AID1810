from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.

class person(object):
    name = None
    age = None

    def show(self):
        return "姓名：%s,年龄:%d" % (self.name, self.age)


def index(request):
    return HttpResponse("这是index应用中的首页")


def temp(request):
    t = loader.get_template("01-temp.html")
    html = t.render()
    return HttpResponse(html)


def render_Temp(request):
    return render(request, "02-temp.html")


def params(request):
    name = "张三丰"
    age = 98
    salary = 123.5
    list = ["白眉鹰王", "青翼蝠王", "紫衫龙王", "金毛狮王"]
    tuple = ("赵敏", "周芷若", "小昭")
    dic = {"XYJ": "西游记", "SG": "三国演义", "HLM": "红楼梦", "SHZ": "水浒传"}
    p = person()
    p.name = "王伟超"
    p.age = 37
    return render(request, "03-params.html", locals())
