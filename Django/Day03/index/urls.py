from django.conf.urls import url

from . import views

urlpatterns = [
    # 判断请求路径是否为show01

    url(r'^$', views.index),
    url(r'^01-add/$', views.add_views),
    url(r'^02-addexec/$', views.add_views_exec),
    url(r'^03-query/$', views.query_views),

]
