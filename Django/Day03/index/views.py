from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    return HttpResponse("这是index应用中的首页")


def add_views(request):
    # 方式１　使用Entry.objects.create()
    # author = Author.objects.create(name="老舍", age=86)
    # print(author)
    # 方式２　创建尸体类对象并调用save方法
    # author=Author()
    # author.name="bajin"
    # author.age=99
    # author.email="binxing@163.com"
    # id=author.save()
    # print(id) #无返回值
    # print(author)
    # 方式３　使用字典创建对象
    dic = {"name": "lijiarui2", "age": 99, "email": "ljrdemail@sohu.com"}
    obj = Author(**dic)
    obj.save()
    return HttpResponse("添加成功！")


def add_views_exec(request):
    book = Book.objects.create(title="流浪地球3", publicate_date="2018-9-7")
    book2 = Book()
    book2.title = "三体"
    book2.publicate_date = "2018-9-7"
    book2.save()
    dic = {"title": "疯狂的外星人3", "publicate_date": "2018-9-7"}
    obj = Book(**dic)
    obj.save()

    publisher = Publisher.objects.create(name="人民文学出版社", address="傻逼路", city="北京", country="中国",
                                         website="http://www.baidu.com")
    publisher2 = Publisher()
    publisher2.name = "人民教育出版社"
    publisher2.address = "友谊路"
    publisher2.city = "losangle"
    publisher2.country = "america"
    publisher2.website = "http://www.nihao.com"
    publisher2.save()

    dic = {"name": "大宗出版社", "address": "sss", "city": "shenzhen", "country": "england", "website": "pig"}
    obj2 = Publisher(**dic)
    obj2.save()
    return HttpResponse("添加成功！")


def query_views(request):
    # 1.all():查询实体中所有的数据
    # authors = Author.objects.all()
    # print("数据类型:",type(authors))
    # print("结果:",authors)
    # #authors:是一个可迭代对象
    # for au in authors:
    #   print("ID:%s,姓名:%s,年龄:%d,邮箱:%s" % (au.id,au.name,au.age,au.email))

    # 2.values('列1',..)
    # authors = Author.objects.values('name', 'email')
    # for au in authors:
    #     print("姓名:%s,邮件:%s" % (au['name'], au['email']))

    authors2 = Author.objects.values_list('name', 'email')
    for au in authors2:
        print("姓名:%s,邮箱%s" % (au[0], au[1]))

    authors3 = Author.objects.order_by('-name', 'email')
    for au in authors3:
        print("ID:%s,姓名:%s,年龄:%d,邮箱:%s" % (au.id, au.name, au.age, au.email))

    return HttpResponse("Query OK")
