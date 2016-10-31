from django.contrib import admin
from models import Article, Blogger, Commenter, Tag
# Register your models here.

admin.site.register(Article)
admin.site.register(Blogger)
admin.site.register(Commenter)
admin.site.register(Tag)
