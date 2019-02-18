from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # 判断请求路径是否为show01

    url(r'^$', views.index),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),


]
