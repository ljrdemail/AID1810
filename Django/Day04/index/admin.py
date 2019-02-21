from django.contrib import admin
from .models import *


# 声明Author的高级管理类 -AuthorAdmin
class AuthorAdmin(admin.ModelAdmin):
    # list_display 定义在列表页上显示额字段
    list_display = ('name', 'age', 'email')
    # list_display_link 定义在列表页中能链接到详情页的字段
    list_display_links = ('name', 'age')
    # list_editable:定义在列表页中就允许编辑的字段们
    # 注意:取值不能出现在list_display_links 中
    list_editable = ('email',)
    # list_filter: 在列表页的右侧增加一个过滤器实现筛选
    list_filter = ('name', 'email')
    # search_fields: 添加允许被搜索的字段们
    search_fields = ('name', 'email', 'age')

    # fields 定义在详情页中要显示的字段和顺序
    # fields=('isActive','name','email') #显示顺序按照书写顺序
    # fieldsets 定义在详情页中的字段分组
    # 注意　fieldsets　和　fields 不能共存
    fieldsets = (
        # 分组1
        ('基本选项', {
            'fields': ('name', 'email'),
        }),
        # 分组2
        ('可选选项', {
            'fields': ('age', 'isActive'),
            'classes': ('collapse',)
        })
    )


class BookAdmin(admin.ModelAdmin):
    # date_hierarchy 在列表页中增加一个时间分层选择器
    date_hierarchy = "publicate_date"


# admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
