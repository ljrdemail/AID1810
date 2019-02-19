from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return HttpResponse("这是index应用中的register访问路径")


def cart(request):
    return render(request, "cart.html")
