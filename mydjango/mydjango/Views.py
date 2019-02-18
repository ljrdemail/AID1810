from django.http import HttpResponse


def show(request):
    return HttpResponse("我的第一个Django程序")


def index(requet):
    return HttpResponse("这是我的首页")


def show_01(request):
    return HttpResponse("<h1>这是show01的访问路径</h1>")
