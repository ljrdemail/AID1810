# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-21 08:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('index', '0004_auto_20190221_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': '出版社', 'verbose_name_plural': '出版社'},
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]