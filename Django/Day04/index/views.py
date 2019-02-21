from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *
from django.db.models import Sum, Avg, Count, Max, Min
from django.shortcuts import redirect
from django.db.models import F

# Create your views here.


def index(request):
    return HttpResponse("这是index应用中的首页")


def query_filter(request):
    # 查询Author 实体中id 为1 的信息
    authors = Author.objects.filter(id=6)
    # 查询 Author实体中 id 为1 并且 isActive 为True
    authors2 = Author.objects.filter(id=7, isActive=True)
    print(authors)
    print(authors2)  # 对象可以迭代访问
    print(authors.query)  # 打印SQL
    return HttpResponse("Query OK")


def query_exec(request):
    # 1 查询Author表中age大于等于85的信息
    authorage = Author.objects.filter(age__gte=85)
    print(authorage)
    # 2查询Author表中姓巴的人的信息
    authorname = Author.objects.filter(name__startswith='巴')
    print(authorname)
    # 3查询Author表中Email中包含in的人的信息
    authoremail = Author.objects.filter(name__contains='in')
    print(authoremail)
    # 4 查询Author表中Age大于”巴金”的age的信息
    author4 = Author.objects.filter(age__gt=(Author.objects.values("age").filter(name__exact='巴金')))
    print(author4.query)
    print(author4)
    for au in authorage:
        print("name:%s,age:%d" % (au.name, au.age))
    return HttpResponse("Query OK")


def query_exclude(request):
    authors = Author.objects.exclude(age=85)
    print(authors)
    print(authors.query)
    return HttpResponse("Query OK")


def query_get(requet):
    # 前两个都会报错
    # author=Author.objects.get(id__gte=6)
    # print(author)
    # author2=Author.objects.get(id__exact=1)
    # print(author2)
    author3 = Author.objects.get(id__exact=6)
    print(author3)

    return HttpResponse("Query OK")


def query_group(request):
    # 查询所有人的总年龄和平均年龄
    result = Author.objects.aggregate(avgAge=Avg('age'), sumAge=Sum('age'))
    print(result)
    # 查询Author 表中年纪>=80的人的平均年龄
    result2 = Author.objects.filter(name__gte=80).aggregate(avgAge=Avg('age'))
    print(result2)
    # 按isActve 分组并求每组人数
    result3 = Author.objects.values('isActive').annotate(count=Count('id')).values('isActive', 'count')
    print(result3.query)
    print(result3)

    return HttpResponse("Query OK")


def query_group_exec(request):
    # 1 查询Book表中共有多少本书
    result = Book.objects.aggregate(count=Count('id'))
    print(result)
    # 2 查询每个时间点所发布的书籍的数量
    result2 = Book.objects.values('publicate_date').annotate(count=Count('id')).values('publicate_date', 'count')
    print(result２)
    # 3 查询1986(不包含)年之后出版的图书的数量
    result3 = Book.objects.filter(publicate_date__year__gt=1986).aggregate(count=Count('id'))
    print(result３)
    # 4 查询Publisher中City 为北京的出版社的数量
    result4 = Publisher.objects.filter(city__exact='北京').aggregate(count=Count('id')).having(count__gt=2)
    print(result４)
    return HttpResponse("Query OK")


def update_single(request):
    lijiarui = Author.objects.get(name="lijiarui")
    lijiarui.email = "ljrdemail@sina.com"
    lijiarui.save()
    return HttpResponse("Update OK")


def update_mutiply(request):
    Author.objects.filter(isActive=False).update(isActive=True)
    Author.objects.filter(isActive=True).update(age=F('age') + 10)
    return HttpResponse("Update OK")


def delete_views(request):
    Author.objects.filter(isActive=False).delete()
    Author.objects.get(id=6).delete()
    return HttpResponse("delete OK")


def interfacequery(request):
    authors = Author.objects.filter(isActive=True)

    return render(request, "01-query_views.html", locals())


def setisActive(request, id):
    authordel = Author.objects.get(id=id)
    authordel.isActive = False
    authordel.save()
    return redirect("/12-queryall")
