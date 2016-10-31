# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20161026_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=10)),
                ('Register_date', models.DateField(auto_now_add=True)),
                ('Intro', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='Title',
        ),
        migrations.RenameField(
            model_name='commenter',
            old_name='article',
            new_name='Article',
        ),
        migrations.RenameField(
            model_name='commenter',
            old_name='author',
            new_name='Author',
        ),
        migrations.RenameField(
            model_name='commenter',
            old_name='content',
            new_name='Content',
        ),
        migrations.RenameField(
            model_name='commenter',
            old_name='pub_date',
            new_name='Pub_date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='article',
            name='Pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='published date'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='Author',
            field=models.ForeignKey(default=20161026, on_delete=django.db.models.deletion.CASCADE, to='myblog.Blogger'),
            preserve_default=False,
        ),
    ]