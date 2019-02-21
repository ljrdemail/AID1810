from django.db import models

# Create your models here.

# 创建一个实体类 -Publisher 表示出版社信息
# 注意 主键&自增列在Django ORM 中会自动创建
# 1 name 出版社的名称 -varchar
# 2 address  出版社的地址 varchar
# 3 city 出版社所在的城市varchar
# 4 country 出版社所在的国家 -varchar
# 5 website 出版社网址

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    website = models.URLField()  # Django帮你封装 底层还是varchar

class Author(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True, db_index=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=254, null=True)
    isActive = models.BooleanField(default=True)

class Book(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True, db_index=True)
    publicate_date = models.DateField(null=True, db_index=True)
