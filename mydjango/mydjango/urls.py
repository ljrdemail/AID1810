"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin  # django 默认的后台管理包
from . import Views

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # 以admin/开始的请求会交给admin.site.urls 来处理 ^ 以什么开始 r 取消转义
    # 访问路径是show/的时候交给show() 函数去处理
    url(r'^show/', Views.show),  # show不用加() 加了就是调用
    url(r'^$', Views.index),
    url(r'^show_01$', Views.show_01),
]
