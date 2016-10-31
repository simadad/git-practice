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
    commenter_data = {}
    if 'content' in request.POST:
        global commenter_data
        commenter_data = request.POST
        Commenter.objects.create(
            Author=commenter_data['author'],
            Content=commenter_data['content'],
            Article=article_data
        )
    else:
        article_data.Like += 1
        article_data.save()
    return render(request, 'myblog/article.html', {
        'article': article_data,
    })


def blogger(request, blogger_name):
    blogger_data = get_object_or_404(Blogger, Name=blogger_name)
    return render(request, 'myblog/blogger.html', {
        'blogger': blogger_data
    })
