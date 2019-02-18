from django.http import HttpResponse

# Create your views here.

def show_01(request):
    return HttpResponse("这是music应用中的show01访问路径")


def index(request):
    return HttpResponse("这是music应用中的首页")
