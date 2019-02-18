from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [

    url(r'^$', views.index),
    # 如果在总的url中用 url(r'^\w+/', include("index.urls")) 这里就会传入空走到了普通index 需要在总的那边放过来这边区分
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),


]
