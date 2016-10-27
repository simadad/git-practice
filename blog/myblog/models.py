from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Blogger(models.Model):
    Name = models.CharField(max_length=10)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    AGE = (
        ('B', 'Babe'),
        ('K', 'Kid'),
        ('S', 'Schoolchild'),
        ('T', 'Teenage'),
        ('Y', 'Youth'),
        ('P', 'Postadolescent'),
        ('O', 'Old')
    )
    Email = models.EmailField
    Favicon = models.ImageField
    Register_date = models.DateField(auto_now_add=True)
    Intro = models.CharField(max_length=500)

    def __str__(self):
        return self.Name


class Article(models.Model):
    Title = models.CharField(max_length=30)
    Author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    Content = models.CharField(max_length=5000)
    Pub_date = models.DateTimeField('published date', auto_now_add=True)

    def __str__(self):
        return self.Title


class Commenter(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE)
    Author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    Content = models.CharField(max_length=500)
    Pub_date = models.DateTimeField('added date', auto_now_add=True)

    def __str__(self):
        return self.Content
