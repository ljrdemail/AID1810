from django.http import HttpResponse


# Create your views here.

# 主路由:url(r'^index/',include("index.urls")),
# 应用的路由:url(r'^index/$',views.index),
def index(request):
    return HttpResponse("这是index应用中的首页")


def login(request):
    return HttpResponse("这是index应用中的login访问路径")


def register(request):
    return HttpResponse("这是index应用中的register访问路径")
