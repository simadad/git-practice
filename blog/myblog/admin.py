from django.contrib import admin
from models import Article, Blogger, Commenter, Tag
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title', 'Author', 'Like', 'Pub_date', 'Revise_date', 'Status')
    search_fields = ('id', 'Title', 'Author', 'Content')
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
    list_filter = ('Gender', 'Age', 'Followed', 'Followers', 'Register_date', 'Status')
    list_display = ('id', 'User', 'Nickname', 'Gender', 'Age', 'Register_date', 'Status')
    search_fields = ('id', 'User', 'Nickname', 'Gender', 'Age', 'Intro', 'Followed', 'Followers', 'Register_date')
    fieldsets = (
        ['Main', {
            'fields': ('id', 'Nickname', 'Gender', 'Age', 'Status', 'Favicon'),
        }],
        ['Advance', {
            'classes': ('collapse',),
            'fields': ('User', 'Followed', 'Intro'),
        }]
    )


class CommenterAdmin(admin.ModelAdmin):
    list_display = ('Article', 'Pub_date', 'Content', 'Status')
    list_filter = ('Article', 'Pub_date', 'Status')
    search_fields = ('id', 'Article', 'Pub_date', 'Content')


class TagAdmin(admin.ModelAdmin):
    search_fields = ('id', 'Article',)
    list_filter = ('Article',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Blogger, BloggerAdmin)
admin.site.register(Commenter, CommenterAdmin)
admin.site.register(Tag, TagAdmin)
