from django.http import HttpResponse


def show(request):
    return HttpResponse("我的第一个Django程序")


def index(requet):
    return HttpResponse("这是我的首页")


def show_01(request):
    return HttpResponse("<h1>这是show01的访问路径</h1>")


# url(r'^show02/(\d{4})/$',views.show_02),
def show_02(request, year):
    return HttpResponse("年份是:" + year)


# r'^show03/(\d{4})/(\d{1,2})/(\d{1,2})/$'
def show_03(request, year, month, day):

    return HttpResponse("生日为：" + year + "年" + month + "月" + day + "日")
    # return HttpResponse("生日为：",year,"年",month,"月",day,"日") 不能这么传参 因为视为7个参数
