from django.conf.urls import url

from . import views

urlpatterns = [
    # 判断请求路径是否为show01

    url(r'^$', views.index),
    url(r'^03-query-filter/$', views.query_filter),
    url(r'^04-query-exec/$', views.query_exec),
    url(r'^05-query-exclude/$', views.query_exclude),
    url(r'^06-query-get/$', views.query_get),
    url(r'^07-query-group/$', views.query_group),
    url(r'^08-query-group_exec/$', views.query_group_exec),
    url(r'^09-update_single/$', views.update_single),
    url(r'^10-update_mutiply/$', views.update_mutiply),
    url(r'^11-delete/$', views.delete_views),
    url(r'^12-queryall/$', views.interfacequery),
    url(r'^delete_exec/(\d+)/$', views.setisActive),



]
