from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.


def index(request):
    return HttpResponse("这是index应用中的首页")
