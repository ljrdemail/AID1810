from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("这是sport应用中的首页")
