from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Blogger(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('FM', 'Female'),
        ('D', 'Default')
    )
    AGE_CHOICES = (
        ('B', 'Babe'),
        ('K', 'Kid'),
        ('S', 'Schoolchild'),
        ('T', 'Teenage'),
        ('Y', 'Youth'),
        ('P', 'Postadolescent'),
        ('O', 'Old'),
        ('D', 'Default')
    )
    Admin = models.OneToOneField(User)
    id = models.IntegerField(primary_key=True)
    Gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='D')
    Age = models.CharField(max_length=2, choices=AGE_CHOICES, default='D')
    Favicon = models.ImageField
    Intro = models.TextField(max_length=500, help_text='Introduce yourself in 500 words.', default='Default intro')

    def __str__(self):
        return self.Admin.username


class Article(models.Model):
    Title = models.CharField(max_length=30, default='A default title')
    Author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    Content = models.TextField(max_length=5000, default='A default content')
    Like = models.IntegerField(default=0)
    Pub_date = models.DateTimeField('published date', auto_now_add=True)

    def __str__(self):
        return self.Title


class Commenter(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Author = models.CharField(max_length=10)
    Content = models.TextField(max_length=500)
    Pub_date = models.DateTimeField('added date', auto_now_add=True)

    def __str__(self):
        return self.Content


class Tag(models.Model):
    Tag = models.CharField(max_length=30)
    Article = models.ManyToManyField(Article)

    def __str__(self):
        return self.Tag
