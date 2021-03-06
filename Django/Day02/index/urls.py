from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    # 判断请求路径是否为show01

    url(r'^$', views.index),
    url(r'^01-temp/$', views.temp),
    url(r'^02-temp/$', views.render_Temp),
    url(r'^03-params/$', views.params),
    url(r'^04-static/$', views.static),
    url(r'^05-parent/$', views.parent),
    url(r'^06-child/$', views.child),
    url(r'^07-fruit/admin/user/manager/auth/login/$', views.auth, name="auth"),
    url(r'^08-birthday/(\d{4})/(\d{1,2})/(\d{1,2})/$', views.birthday, name="birthday"),

]
