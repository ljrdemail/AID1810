from django.http import HttpResponse


def show(request):
    return HttpResponse("我的第一个Django程序")
