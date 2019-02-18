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
    # 访问路径是 show/ 的时候,交给views.show()函数取处理 http://localhost:8000/show/
    url(r'^show/$', Views.show),  # show不用加() 加了就是调用
    # 访问路径是 http://locahohst:8000的时候,交给views.index 函数去处理
    url(r'^$', Views.index),
    #访问路径是 http://localhost:8000/show01,交给views.show_01去处理
    url(r'^show_01/$', Views.show_01),  # 最后的/你不加系统也会给你加 但是建议自己写上
    #访问路径是 http://localhost:8000/show02/四位数字,交给views.show_02去处理
    url(r'^show_02/(\d{4})/$', Views.show_02),
    #/show03/四位数字/两位数字/两位数字
    url(r'^show_03/(\d{4})/(\d{1,2})/(\d{1,2})/$', Views.show_03),
]
