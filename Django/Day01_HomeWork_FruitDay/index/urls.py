from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # 判断请求路径是否为show01
    # 1.匹配 /
    url(r'^$', views.index),
    # 2.匹配 /login
    url(r'^login/$', views.login),
    # 3.匹配 /register
    url(r'^register/$', views.register),
    # 4.匹配 /cart
    url(r'^cart/$', views.cart),

]
