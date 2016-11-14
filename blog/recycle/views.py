from django.shortcuts import render, get_object_or_404
from myblog.models import Article, Blogger, Commenter
# Create your views here.


def article_recycle(request, blogger_id):
    blogger = get_object_or_404(Blogger, id=blogger_id)
    article_deleted = Article.all_objects.filter(Author=blogger, Status=False)
    if request.method == 'POST':
        recycle_article_id = request.POST.getlist('recycle_article_id')
        for i in recycle_article_id:
            article = Article.all_objects.filter(id=i)[0]
            article.Status = True
            article.save()
    else:
        pass
    return render(request, 'recycle/article_recycle.html', {
        'article_deleted': article_deleted,
        'blogger': blogger
    })


def blogger_recycle(request, blogger_id):
    pass


def commenter_recycle(request):
    pass
