from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("这是index应用中的首页")


def temp(request):
    t = loader.get_template("01-temp.html")
    html = t.render()
    return HttpResponse(html)


def renderTemp(request):
    return render(request, "02-temp.html")
