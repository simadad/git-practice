# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ExistingManager(models.Manager):
    # 筛选未删除的信息 ##################################
    def get_queryset(self):
        return super(ExistingManager, self).get_queryset().filter(Status=True)


class Blogger(models.Model):
    GENDER_CHOICES = (
        ('M', '男'),
        ('FM', '女'),
    )
    AGE_CHOICES = (
        ('B', '童年'),
        ('K', '幼年'),
        ('S', '少年'),
        ('T', '青年'),
        ('Y', '壮年'),
        ('P', '中年'),
        ('O', '老年'),
    )
    id = models.IntegerField(primary_key=True)
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Status = models.BooleanField('激活', default=True)
    Nickname = models.CharField('昵称', max_length=30, default='AAA')
    Followed = models.ManyToManyField('Blogger', 'Followers')
    Gender = models.CharField('性别', max_length=2, choices=GENDER_CHOICES, default='M')
    Age = models.CharField('年纪', max_length=2, choices=AGE_CHOICES, default='B')
    Favicon = models.ImageField
    Register_date = models.DateField('注册时间', auto_now_add=True)
    Intro = models.TextField('自我介绍', max_length=500, help_text='Introduce yourself.', default='Default intro')

    all_objects = models.Manager()
    objects = ExistingManager()

    def __str__(self):
        return self.Nickname


class Article(models.Model):
    Title = models.CharField('标题', max_length=30, default='A default title')
    Author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    Content = models.TextField('内容', max_length=5000, default='A default content')
    Like = models.IntegerField('赞', default=0)
    Pub_date = models.DateTimeField('发表时间', auto_now_add=True)
    Revise_date = models.DateTimeField('最后修订', auto_now=True)
    Status = models.BooleanField('上线', default=True)

    all_objects = models.Manager()
    objects = ExistingManager()

    def __str__(self):
        return self.Title


class Commenter(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Author = models.CharField('评论人', max_length=10)
    Content = models.TextField('评论', max_length=500)
    Pub_date = models.DateTimeField('添加时间', auto_now_add=True)
    Status = models.BooleanField('展示', default=True)

    all_objects = models.Manager()
    objects = ExistingManager()

    def __str__(self):
        return self.Content


class Tag(models.Model):
    Tag = models.CharField('标签', max_length=30)
    Article = models.ManyToManyField(Article)

    def __str__(self):
        return self.Tag
