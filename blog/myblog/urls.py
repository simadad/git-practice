from django.conf.urls import url, include
from . import views

app_name = 'myblog'
ajax_patterns = [
    url(r'^like', views.ajax_like, name='like'),
    url(r'^commenter', views.ajax_commenter, name='commenter'),
    url(r'^tcloud', views.ajax_tag_cloud, name='tcloud'),
    url(r'^adel', views.ajax_article_del, name='adel'),
    url(r'^follow', views.ajax_follow, name='follow'),
]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/([0-9]+)', views.article, name='article'),
    url(r'^blogger/([0-9]+)', views.blogger, name='blogger'),
    url(r'^tag/([0-9]+)', views.tag, name='tag'),
    url(r'^editor/', views.editor, name='editor'),
    url(r'^blogger/editor/([0-9]+)', views.blogger_editor, name='blogger_editor'),
    url(r'^reprint/', views.reprint, name='reprint'),
    url(r'^ajax/', include(ajax_patterns, namespace='ajax')),
    # url(r'^ajax/like', views.ajax_like, name='ajax_like'),
    # url(r'ajax/commenter', views.ajax_commenter, name='ajax_commenter'),
    # url(r'ajax/tcloud', views.ajax_tag_cloud, name='tcloud')
]
