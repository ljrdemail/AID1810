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
    # 1.通过loader加载模板
    t = loader.get_template("01-temp.html")
    # 2.将模板转换成字符串
    html = t.render()
    # 3.通过HttpResponse进行响应
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


def static(request):
    return render(request, "04-static.html")


def parent(request):
    list = ["孙悟空", "猪八戒", "沙僧", "唐僧"]
    return render(request, "05-parent.html", locals())


def child(request):
    list = ["旋涡鸣人", "小樱", "卡卡西", "佐助"]
    return render(request, "06-child.html", locals())


def auth(request):
    return HttpResponse("<h1>07-fruit/admin/user/manager/auth/login</h1>")


def birthday(request, year, month, day):
    return HttpResponse("生日为:%s年%s月%s日" % (year, month, day))
