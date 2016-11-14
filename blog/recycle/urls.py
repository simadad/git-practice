from django.conf.urls import url
from . import views

app_name = 'recycle'
urlpatterns = [
    url(r'^article/([0-9]+)', views.article_recycle, name='article_re'),
    url(r'^blogger/([0-9]+)', views.blogger_recycle, name='blogger_re'),
    url(r'^commenter/', views.commenter_recycle, name='commenter_re'),
]
