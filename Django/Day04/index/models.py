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
    name = models.CharField(max_length=30, verbose_name='名称')
    address = models.CharField(max_length=100, verbose_name='地址')
    city = models.CharField(max_length=20, verbose_name='城市')
    country = models.CharField(max_length=20, verbose_name='国家')
    website = models.URLField(verbose_name='官网')  # Django帮你封装 底层还是varchar

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

    # 重写　__str__() 方法
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True, db_index=True, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(max_length=254, null=True, verbose_name='邮箱')
    isActive = models.BooleanField(default=True, verbose_name='激活状态')

    # 通过内部类修改展现形式
    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name

    # 重写　__str__() 方法
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, null=False, unique=True, db_index=True, verbose_name='书名')
    publicate_date = models.DateField(null=True, db_index=True, verbose_name='出版日期')

    class Meta:
        db_table = 'book'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name

    # 重写　__str__() 方法
    def __str__(self):
        return self.title
