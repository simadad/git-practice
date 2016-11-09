from django.contrib import admin
from models import Article, Blogger, Commenter, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Author', 'Like', 'Pub_date', 'Revise_date', 'Status')
    search_fields = ('id', 'Title', 'Author', 'Like', 'Pub_date', 'Content', 'Revise_date', 'Status')
    list_filter = ('Author', 'Pub_date', 'Revise_date', 'Status')
    fieldsets = (
        ['Main', {
            'fields': ('Title', 'Author', 'Status')
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('Like', 'Content')
        }]
    )


class BloggerAdmin(admin.ModelAdmin):
    list_filter = ('Gender', 'Age', 'Followed', 'Followers', 'Register_date')
    list_display = ('id', 'User', 'Gender', 'Age', 'Register_date')
    search_fields = ('id', 'User', 'Gender', 'Age', 'Intro', 'Followed', 'Followers', 'Register_date')
    fieldsets = (
        ['Main', {
            'fields': ('id', 'User', 'Gender', 'Age'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('Followed', 'Intro'),
        }]
    )


class CommenterAdmin(admin.ModelAdmin):
    list_display = ('Article', 'Pub_date', 'Content')
    list_filter = ('Article', 'Pub_date')
    search_fields = ('id', 'Article', 'Pub_date', 'Content')


class TagAdmin(admin.ModelAdmin):
    search_fields = ('id', 'Article',)
    list_filter = ('Article',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Blogger, BloggerAdmin)
admin.site.register(Commenter, CommenterAdmin)
admin.site.register(Tag, TagAdmin)
