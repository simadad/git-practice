from django.shortcuts import render, get_object_or_404, redirect
from models import Article, Blogger, Commenter, Tag

# Create your views here.


def index(request):
    article_data = Article.objects.order_by('-Pub_date')[:5]
    print article_data[0].Author.id
    return render(request, 'myblog/index.html', {
        'articles': article_data
    })


def article(request, article_id):
    article_data = get_object_or_404(Article, pk=article_id)
    commenter_data = {}
    if request.method == 'POST':
        if 'content' in request.POST:
            global commenter_data
            commenter_data = request.POST
            Commenter.objects.create(
                Author=commenter_data['author'],
                Content=commenter_data['content'],
                Article=article_data
            )
        elif 'like' in request.POST:
            article_data.Like += 1
            article_data.save()
        else:
            pass
    else:
        pass
    return render(request, 'myblog/article.html', {
        'article': article_data,
    })


def blogger(request, blogger_id):
    blogger_data = get_object_or_404(Blogger, id=blogger_id)
    return render(request, 'myblog/blogger.html', {
        'blogger': blogger_data
    })


def tag(request, tag_id):
    tag_data = get_object_or_404(Tag, id=tag_id)
    return render(request, 'myblog/tag.html', {
        'tag': tag_data
    })


def editor(request, blogger_id, article_id):
    # tags = Tag.objects.filter()
    # print tags
    blogger_data = get_object_or_404(Blogger, id=blogger_id)
    if request.method == 'POST':
        article_data = request.POST
        title = article_data['title']
        content = article_data['content']
        if title and content:
            if article_id < 0:
                edited_article = Article.objects.create(
                    Author=blogger_data,
                    Title=title,
                    Content=content
                )
            else:
                edited_article = get_object_or_404(Article, id=article_id)
                edited_article.Author = blogger_data,
                edited_article.Title = title,
                edited_article.Content = content
            return redirect('/blog/article/%d' % edited_article.id)
        else:
            pass
    else:
        if article_id < 0:
            return render(request, 'myblog/editor.html', {
                'edited_article': False
            })
        else:
            edited_article = get_object_or_404(Article, id=article_id)
            return render(request, 'myblog/editor.html', {
                'edited_article': edited_article
            })
