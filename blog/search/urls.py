from django.conf.urls import url
from . import views

app_name = 'search'
urlpatterns = [
    url(r'^new', views.article_new, name='article_new'),
    url(r'^like', views.article_like, name='article_like'),
    url(r'tag', views.article_tag, name='article_tag'),
    url(r'search', views.search_engine, name='search_engine'),
]
