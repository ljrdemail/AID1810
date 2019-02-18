from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("这是news应用中的首页")
