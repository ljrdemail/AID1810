"""Day01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('admin/', admin.site.urls),
    # 判断访问路径是否为music/开头的
    url(r'^music/', include("music.urls")),  # 注意music/后没有$ 余下的交给music目录下的urls.py进一步处理
    url(r'^index/', include("index.urls")),  # 注意index/后没有$ 余下的交给index目录下的urls.py进一步处理
    url(r'^sport/', include("sport.urls")),  # 注意sport/后没有$ 余下的交给sport目录下的urls.py进一步处理
    url(r'^news/', include("news.urls")),  # 注意news/后没有$ 余下的交给news目录下的urls.py进一步处理
    # url(r'^\w+/', include("index.urls")),  # 注意index/后没有$ 余下的交给index目录下的urls.py进一步处理
    url(r'^', include("index.urls")),  # 如果什么都不输入交给index来处理

]
