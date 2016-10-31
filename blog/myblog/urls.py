from django.conf.urls import url
from . import views

app_name = 'myblog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/([0-9]+)', views.article, name='article'),
    url(r'^blogger/([a-zA-Z0-9]+)', views.blogger, name='blogger'),
]
