from django.conf.urls import url
from . import views

app_name = 'myblog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/([0-9]+)', views.article, name='article'),
    url(r'^blogger/([0-9]+)', views.blogger, name='blogger'),
    url(r'^tag/([0-9]+)', views.tag, name='tag'),
    url(r'^editor/', views.editor, name='editor'),
    url(r'^blogger/editor/([0-9]+)', views.blogger_editor, name='blogger_editor'),
    url(r'^reprint/', views.reprint, name='reprint'),
]
