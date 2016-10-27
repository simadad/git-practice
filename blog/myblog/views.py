from django.shortcuts import render, get_object_or_404
from models import Article, Blogger, Commenter
# Create your views here.


def index(request):
    article_data = Article.objects.order_by('-Pub_date')[:5]
    return render(request, 'myblog/index.html', {
        'articles': article_data
    })


def article(request, article_id):
    article_data = get_object_or_404(Article, pk=article_id)
    return render(request, 'myblog/article.html', {
        'article': article_data
    })


def blogger(request, blogger_id):
    blogger_data = get_object_or_404(Blogger, pk=blogger_id)
    return render(request, 'myblog/blogger.html', {
        'blogger': blogger_data
    })
