# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-02-21 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('index', '0003_auto_20190221_1650'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': '作者', 'verbose_name_plural': '作者'},
        ),
        migrations.AlterModelTable(
            name='publisher',
            table='publisher',
        ),
    ]