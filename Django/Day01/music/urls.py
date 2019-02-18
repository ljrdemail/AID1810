from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # 判断请求路径是否为show01
    # (http://localhost:8000/music/show01/)
    url(r'^show01/$', views.show_01),
    url(r'^index/$', views.index),
    # 判断请求路径是否为 空
    # (http://localhost:8000/music/)
    url(r'^$', views.index),

]
