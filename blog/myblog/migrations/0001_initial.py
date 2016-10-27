# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=5000)),
                ('pub_data', models.DateTimeField(verbose_name='published date')),
            ],
        ),
        migrations.CreateModel(
            name='Commenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=500)),
                ('pub_data', models.DateTimeField(verbose_name='added date')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Article')),
            ],
        ),
    ]
