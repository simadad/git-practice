# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0005_auto_20161109_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Status',
            field=models.BooleanField(default=True, verbose_name='\u4e0a\u7ebf'),
        ),
    ]
